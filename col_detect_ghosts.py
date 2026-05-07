#!/usr/bin/env python3
"""
COL Ghost Entry Detection & Quarantine
========================================

The Colonial Office List includes historical sections (e.g., "Governors and
Commanders-in-Chief") listing ALL past governors, not just the current one.
Our extraction pipeline didn't distinguish these from the current establishment,
so historical governors appear as PersonRecords in every edition year.

Primary detection: Use Wikidata governor chains to identify PersonRecords
from historical sections. If a governor's tenure ended before the edition year,
that PersonRecord is a historical listing, not a current official.

Secondary detection: Name-match COL_Officials to WD_Persons for broader
ghost detection (death year after last COL appearance).

Usage:
    python col_detect_ghosts.py                  # full detection + quarantine
    python col_detect_ghosts.py --dry-run        # detect only, no writes
    python col_detect_ghosts.py --stats          # report quarantine status
    python col_detect_ghosts.py --clear          # remove all quarantine flags & CANDIDATE_MATCH edges
    python col_detect_ghosts.py --governors-only # only governor chain quarantine
    python col_detect_ghosts.py --link-only      # only name matching, no quarantine
    python col_detect_ghosts.py --report         # write GHOST_DETECTION_REPORT.md

Requires:
    pip install neo4j
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

from col_normalize_names import (
    extract_initials,
    initials_compatible,
    _tokenize_given,
    _is_initial,
    clean_given_names,
)


# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
BATCH_SIZE = 1000
MERGED_PEOPLE_PATH = REPO_DIR / "wikidata_harvest" / "merged_all_people.json"
CROSSWALK_PATH = REPO_DIR / "scaffolding" / "col_kg_crosswalk.json"

# Governor-class position keywords in COL PersonRecords
GOVERNOR_POSITION_KEYWORDS = [
    "governor", "administrator", "high commissioner",
    "governor-general", "governor general",
    "officer administering", "acting governor",
    "lieutenant-governor", "lieutenant governor",
    "captain-general", "captain general",
    "commander-in-chief", "commander in chief",
]

# Broader official position keywords for expanded ghost detection
OFFICIAL_POSITION_KEYWORDS = [
    "governor", "administrator", "high commissioner",
    "governor-general", "governor general",
    "lieutenant-governor", "lieutenant governor",
    "captain-general", "captain general",
    "commander-in-chief", "commander in chief",
    "chief justice", "attorney-general", "attorney general",
    "colonial secretary", "chief secretary",
    "solicitor-general", "solicitor general",
    "auditor-general", "auditor general",
    "treasurer", "surveyor-general", "surveyor general",
    "commissioner of police", "inspector-general",
    "bishop", "archbishop",
]


def _load_dotenv():
    """Load .env file from repo root."""
    env_path = REPO_DIR / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())


_load_dotenv()

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")


# =============================================================================
# NAME PARSING
# =============================================================================

def parse_col_name(canonical_name: str):
    """Parse COL canonical_name "Surname, Given" → (surname, given)."""
    if ", " in canonical_name:
        surname, given = canonical_name.split(", ", 1)
        return surname.strip(), given.strip()
    return canonical_name.strip(), ""


def parse_wd_name(name: str):
    """Parse Wikidata name "Given Surname" → (surname, given)."""
    if not name:
        return "", ""
    name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
    parts = name.split()
    if len(parts) == 0:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    return parts[-1], " ".join(parts[:-1])


# =============================================================================
# COLONY CROSSWALK
# =============================================================================

def load_crosswalk():
    """Load colony crosswalk: COL colony name → set of Wikidata QIDs."""
    if not CROSSWALK_PATH.exists():
        print(f"WARNING: Crosswalk not found at {CROSSWALK_PATH}")
        return {}

    with open(CROSSWALK_PATH) as f:
        data = json.load(f)

    col_to_qids = {}
    for col_name, info in data.items():
        qids = set()
        for mapping in info.get("mappings", []):
            qid = mapping.get("wikidata_id")
            if qid:
                qids.add(qid)
        if qids:
            col_to_qids[col_name] = qids

    return col_to_qids


# =============================================================================
# WIKIDATA DATA LOADING
# =============================================================================

def load_wd_persons():
    """Load WD_Person data from merged_all_people.json with death years."""
    if not MERGED_PEOPLE_PATH.exists():
        print(f"ERROR: {MERGED_PEOPLE_PATH} not found")
        return []

    with open(MERGED_PEOPLE_PATH) as f:
        people = json.load(f)

    persons = []
    for p in people:
        birth_year = None
        death_year = None

        for assoc in p.get("associations", []):
            if assoc.get("birth"):
                m = re.search(r'(\d{4})', str(assoc["birth"]))
                if m:
                    birth_year = int(m.group(1))
            if assoc.get("death"):
                m = re.search(r'(\d{4})', str(assoc["death"]))
                if m:
                    death_year = int(m.group(1))
            if birth_year:
                break

        if not birth_year and p.get("description"):
            m = re.search(r'\((\d{4})[–-](\d{4})\)', p["description"])
            if m:
                birth_year = int(m.group(1))
                death_year = int(m.group(2))

        persons.append({
            "qid": p["qid"],
            "name": p["name"],
            "description": p.get("description", ""),
            "positions": p.get("positions", []),
            "associations": p.get("associations", []),
            "birthYear": birth_year,
            "deathYear": death_year,
        })

    return persons


# =============================================================================
# PHASE 1: HISTORICAL OFFICIAL DETECTION (PRIMARY)
# =============================================================================

def _extract_colony_from_label(label: str) -> str | None:
    """Extract colony name from a Wikidata position label.

    E.g. "Governor of Hong Kong" → "Hong Kong"
         "Chief Justice of Ceylon" → "Ceylon"
         "Attorney-General of British Guiana" → "British Guiana"
    """
    m = re.search(
        r'(?:governor|commissioner|administrator|chief justice|'
        r'attorney.general|colonial secretary|chief secretary|'
        r'solicitor.general|auditor.general|surveyor.general|'
        r'bishop|archbishop|treasurer|inspector.general)'
        r'(?:-general)?\s+of\s+(?:the\s+)?(.+)',
        label, re.IGNORECASE,
    )
    if m:
        colony = m.group(1).strip()
        # Strip "British " prefix for matching (e.g. "British Mauritius" → "Mauritius")
        # but keep "British Guiana", "British Honduras" etc. that are actual COL names
        for prefix in ["British "]:
            stripped = colony.removeprefix(prefix)
            if stripped != colony and stripped not in (
                "Guiana", "Honduras", "Somaliland", "New Guinea",
                "Central Africa", "East Africa", "Columbia",
                "Antarctic Territory", "Bechuanaland",
            ):
                colony = stripped
        return colony
    return None


def _build_label_to_col_name(col_to_qids):
    """Build a fuzzy mapping from extracted colony labels → COL colony names.

    Handles cases like "Mauritius" (from WD label) → "Mauritius" (COL name)
    and "New South Wales" → "New South Wales" etc.
    """
    col_names = set(col_to_qids.keys())
    # Exact match + lowercase match
    mapping = {}
    col_lower = {n.lower(): n for n in col_names}
    for n in col_names:
        mapping[n] = n
        mapping[n.lower()] = n
    return mapping, col_lower


def load_official_tenures(wd_persons, col_to_qids):
    """Build per-colony official timelines from ALL Wikidata positions.

    Unlike the old load_governor_chains which only matched governors,
    this matches ALL officials with tenure end dates — governors, chief
    justices, attorneys-general, colonial secretaries, etc.

    Returns {colony_name: [{qid, name, surname, given, start_year, end_year,
                            position_label, death_year, is_governor}, ...]}
    sorted by start_year within each colony.
    """
    # Invert crosswalk: wikidata QID → COL colony name
    qid_to_colony = {}
    for col_name, qids in col_to_qids.items():
        for qid in qids:
            qid_to_colony[qid] = col_name

    # Build label-based colony mapping for positions without colony_qid
    col_names_set = set(col_to_qids.keys())
    col_lower_map = {n.lower(): n for n in col_names_set}

    tenures = defaultdict(list)
    mapped_via_qid = 0
    mapped_via_label = 0
    skipped_no_colony = 0

    for p in wd_persons:
        for pos in p.get("positions", []):
            if not pos.get("end"):
                continue

            label = pos.get("position_label", "")
            label_lower = label.lower()

            # Check if this is an official-class position
            is_official = any(kw in label_lower for kw in OFFICIAL_POSITION_KEYWORDS)
            if not is_official:
                continue

            is_governor = any(kw in label_lower for kw in GOVERNOR_POSITION_KEYWORDS)

            # Resolve colony name — try colony_qid first, then parse from label
            colony_qid = pos.get("colony_qid", "")
            colony_name = qid_to_colony.get(colony_qid) if colony_qid else None

            if colony_name:
                mapped_via_qid += 1
            else:
                # Try extracting from position label
                extracted = _extract_colony_from_label(label)
                if extracted:
                    colony_name = col_lower_map.get(extracted.lower())
                if colony_name:
                    mapped_via_label += 1
                else:
                    skipped_no_colony += 1
                    continue

            start_year = None
            end_year = None
            if pos.get("start"):
                m = re.search(r'(\d{4})', str(pos["start"]))
                if m:
                    start_year = int(m.group(1))
            if pos.get("end"):
                m = re.search(r'(\d{4})', str(pos["end"]))
                if m:
                    end_year = int(m.group(1))

            if not end_year:
                continue

            surname, given = parse_wd_name(p["name"])

            tenures[colony_name].append({
                "qid": p["qid"],
                "name": p["name"],
                "surname": surname,
                "given": given,
                "start_year": start_year,
                "end_year": end_year,
                "position_label": label,
                "death_year": p.get("deathYear"),
                "is_governor": is_governor,
            })

    # Sort by start_year
    for colony in tenures:
        tenures[colony].sort(key=lambda x: x["start_year"] or 9999)

    print(f"  Mapped via colony_qid: {mapped_via_qid}")
    print(f"  Mapped via label parsing: {mapped_via_label}")
    print(f"  Skipped (no colony match): {skipped_no_colony}")

    return dict(tenures)


def _is_governor_position(position: str) -> bool:
    """Check if a COL PersonRecord position is a governor-class role."""
    if not position:
        return False
    pos_lower = position.lower()
    return any(kw in pos_lower for kw in GOVERNOR_POSITION_KEYWORDS)


def _surname_matches(col_surname: str, wd_surname: str) -> bool:
    """Check if surnames match (case-insensitive)."""
    if not col_surname or not wd_surname:
        return False
    return col_surname.lower().strip() == wd_surname.lower().strip()


# Mapping from WD position label keywords → COL position_raw keywords
_POSITION_TYPE_MAP = [
    (["chief justice"], ["chief justice"]),
    (["attorney-general", "attorney general"], ["attorney-general", "attorney general"]),
    (["solicitor-general", "solicitor general"], ["solicitor-general", "solicitor general"]),
    (["colonial secretary", "chief secretary"], ["colonial secretary", "chief secretary"]),
    (["auditor-general", "auditor general"], ["auditor-general", "auditor general"]),
    (["surveyor-general", "surveyor general"], ["surveyor-general", "surveyor general"]),
    (["treasurer"], ["treasurer"]),
    (["commissioner of police"], ["commissioner of police", "inspector general of police"]),
    (["inspector-general"], ["inspector-general", "inspector general"]),
    (["bishop", "archbishop"], ["bishop", "archbishop"]),
]


def _position_type_matches(wd_label: str, col_position_raw: str) -> bool:
    """Check if a WD position label and COL position_raw describe the same role type."""
    if not wd_label or not col_position_raw:
        return False
    wd_lower = wd_label.lower()
    col_lower = col_position_raw.lower()

    for wd_keys, col_keys in _POSITION_TYPE_MAP:
        wd_match = any(k in wd_lower for k in wd_keys)
        col_match = any(k in col_lower for k in col_keys)
        if wd_match and col_match:
            return True
    return False


def detect_historical_officials(session, tenures):
    """Find PersonRecords that are historical listings (governor chains, etc.).

    For each official in the Wikidata tenure index, find COL PersonRecords
    in that colony with a matching surname. If the PersonRecord year is
    AFTER the official's tenure ended, it's a historical listing from the
    printed chain, not a current official.

    For governors: any post-tenure appearance is flagged (they appear in
    the printed "Governors since..." chain).

    For non-governor officials: we require the COL position_raw to also
    match the role type (to avoid false positives from common surnames).

    Returns list of quarantine actions.
    """
    quarantine_actions = []
    matched_officials = 0
    seen_pr_uris = set()  # deduplicate across multiple WD matches

    for colony, officials in tenures.items():
        for off in officials:
            if not off["end_year"] or not off["surname"]:
                continue

            # Find COL PersonRecords with matching surname in this colony
            # appearing AFTER the official's tenure ended
            result = session.run(
                "MATCH (pr:COL_PersonRecord) "
                "WHERE pr.colony = $colony "
                "  AND pr.surname = $surname "
                "  AND pr.year > $end_year "
                "  AND (pr.quarantined IS NULL OR pr.quarantined = false) "
                "RETURN pr.uri AS uri, pr.year AS year, "
                "       pr.position_raw AS position, "
                "       pr.canonical_name AS name, "
                "       pr.given_names AS given_names",
                colony=colony,
                surname=off["surname"],
                end_year=off["end_year"],
            )

            records = [dict(r) for r in result]
            if not records:
                continue

            for rec in records:
                if rec["uri"] in seen_pr_uris:
                    continue

                pos_raw = rec.get("position", "") or ""

                if off["is_governor"]:
                    # For governors: require governor-class position in COL
                    if not _is_governor_position(pos_raw):
                        continue
                    reason_prefix = "historical_governor"
                else:
                    # For non-governors: require matching position type in COL
                    if not _position_type_matches(off["position_label"], pos_raw):
                        continue
                    reason_prefix = "historical_official"

                # Verify initials are compatible
                col_given = rec.get("given_names", "") or ""
                if off["given"] and col_given:
                    if not initials_compatible(col_given, off["given"]):
                        continue

                seen_pr_uris.add(rec["uri"])
                quarantine_actions.append({
                    "colony": colony,
                    "year": rec["year"],
                    "pr_uri": rec["uri"],
                    "pr_name": rec["name"],
                    "pr_position": pos_raw,
                    "official_name": off["name"],
                    "wd_position": off["position_label"],
                    "qid": off["qid"],
                    "tenure_end": off["end_year"],
                    "death_year": off["death_year"],
                    "is_governor": off["is_governor"],
                    "reason": f"{reason_prefix}:tenure_ended_{off['end_year']}:wd:{off['qid']}",
                })

            matched_officials += 1

    governor_count = sum(1 for a in quarantine_actions if a["is_governor"])
    other_count = len(quarantine_actions) - governor_count
    print(f"  {matched_officials} WD officials matched against COL")
    print(f"  {len(quarantine_actions)} historical PersonRecords identified")
    print(f"    Governors: {governor_count}")
    print(f"    Other officials: {other_count}")
    return quarantine_actions


QUARANTINE_HISTORICAL_QUERY = """
UNWIND $batch AS q
MATCH (pr:COL_PersonRecord {uri: q.pr_uri})
WHERE pr.quarantined IS NULL OR pr.quarantined = false
SET pr.quarantined = true,
    pr.quarantine_reason = q.reason,
    pr.quarantine_date = $today
RETURN count(pr) AS quarantined
"""


def quarantine_historical_governors(session, actions, today):
    """Mark historical governor PersonRecords as quarantined."""
    total = 0
    for i in range(0, len(actions), BATCH_SIZE):
        batch = actions[i:i + BATCH_SIZE]
        r = session.run(QUARANTINE_HISTORICAL_QUERY, batch=batch, today=today).single()
        total += r["quarantined"]
    return total


# =============================================================================
# PHASE 2: BROADER NAME MATCHING (SECONDARY)
# =============================================================================

def build_surname_index(officials):
    """Build {normalized_surname: [official_dicts]} index."""
    index = defaultdict(list)
    for off in officials:
        surname, given = parse_col_name(off["name"])
        off["_surname"] = surname
        off["_given"] = given
        key = surname.lower().strip()
        if key:
            index[key].append(off)
    return index


def build_wd_surname_index(wd_persons):
    """Build {normalized_surname: [wd_person_dicts]} index."""
    index = defaultdict(list)
    for p in wd_persons:
        surname, given = parse_wd_name(p["name"])
        p["_surname"] = surname
        p["_given"] = given
        key = surname.lower().strip()
        if key:
            index[key].append(p)
    return index


def colonies_overlap(col_colony, wd_person, col_to_qids):
    """Check if a WD_Person has associations/positions in the same colony."""
    colony_qids = col_to_qids.get(col_colony, set())
    if not colony_qids:
        return False
    for pos in wd_person.get("positions", []):
        if pos.get("colony_qid") in colony_qids:
            return True
    for assoc in wd_person.get("associations", []):
        if assoc.get("colony_qid") in colony_qids:
            return True
    return False


def _temporally_plausible(off, wd):
    """Check if a COL_Official and WD_Person could be the same person."""
    death_year = wd.get("deathYear")
    birth_year = wd.get("birthYear")

    if death_year and off["first_year"] > death_year:
        return False
    if birth_year and off["last_year"] < birth_year + 15:
        return False
    if birth_year and birth_year > 1970:
        return False

    return True


def match_officials_to_wd(officials, wd_persons, col_to_qids):
    """Match COL_Official names to WD_Person nodes using three tiers.

    Tier 1: Exact surname + full given name (0.95)
    Tier 2: Surname + initials + colony overlap (0.80) or without (0.70)
    Tier 3: Surname + colony overlap + bare surname (0.65)

    All tiers require temporal plausibility.
    """
    col_index = build_surname_index(officials)
    wd_index = build_wd_surname_index(wd_persons)

    matches = []
    matched_officials = set()

    for surname_key, col_group in col_index.items():
        wd_group = wd_index.get(surname_key, [])
        if not wd_group:
            continue

        for off in col_group:
            if off["id"] in matched_officials:
                continue

            best_match = None
            best_confidence = 0
            best_tier = 0
            best_reason = ""

            for wd in wd_group:
                if not _temporally_plausible(off, wd):
                    continue

                # Tier 1: Full given name match
                if off["_given"] and wd["_given"]:
                    off_tokens = _tokenize_given(off["_given"])
                    wd_tokens = _tokenize_given(wd["_given"])

                    if (off_tokens and wd_tokens
                            and not _is_initial(off_tokens[0])
                            and not _is_initial(wd_tokens[0])):
                        if initials_compatible(off["_given"], wd["_given"]):
                            has_full = any(not _is_initial(t) for t in off_tokens)
                            if has_full:
                                conf = 0.95
                                if conf > best_confidence:
                                    best_match = wd
                                    best_confidence = conf
                                    best_tier = 1
                                    best_reason = f"Full name: {off['_given']} ≈ {wd['_given']}"

                # Tier 2: Initials compatible (+ colony for bonus confidence)
                if best_tier < 2 or best_confidence < 0.80:
                    if off["_given"] and wd["_given"]:
                        if initials_compatible(off["_given"], wd["_given"]):
                            has_colony = colonies_overlap(off["colony"], wd, col_to_qids)
                            conf = 0.80 if has_colony else 0.70
                            if conf > best_confidence:
                                best_match = wd
                                best_confidence = conf
                                best_tier = 2
                                colony_note = " + colony" if has_colony else ""
                                best_reason = f"Initials{colony_note}: {off['_given']} ≈ {wd['_given']}"

                # Tier 3: Colony overlap + bare surname
                if best_tier < 3 or best_confidence < 0.65:
                    if colonies_overlap(off["colony"], wd, col_to_qids):
                        if not off["_given"] or not wd["_given"] or \
                           initials_compatible(off["_given"], wd["_given"]):
                            conf = 0.65
                            if conf > best_confidence:
                                best_match = wd
                                best_confidence = conf
                                best_tier = 3
                                best_reason = f"Colony overlap: {off['colony']}"

            if best_match and best_confidence >= 0.65:
                matches.append({
                    "official_id": off["id"],
                    "official_name": off["name"],
                    "colony": off["colony"],
                    "first_year": off["first_year"],
                    "last_year": off["last_year"],
                    "qid": best_match["qid"],
                    "wd_name": best_match["name"],
                    "confidence": best_confidence,
                    "tier": best_tier,
                    "reason": best_reason,
                    "death_year": best_match.get("deathYear"),
                    "birth_year": best_match.get("birthYear"),
                })
                matched_officials.add(off["id"])

    return matches


# =============================================================================
# CANDIDATE_MATCH EDGES
# =============================================================================

CLEAR_CANDIDATE_MATCH = """
MATCH ()-[r:CANDIDATE_MATCH]->()
DELETE r
RETURN count(r) AS deleted
"""

CREATE_CANDIDATE_MATCH = """
UNWIND $batch AS m
MATCH (o:COL_Official {id: m.official_id})
MATCH (p:WD_Person {qid: m.qid})
MERGE (o)-[r:CANDIDATE_MATCH]->(p)
SET r.confidence = m.confidence,
    r.tier = m.tier,
    r.reason = m.reason
"""


def write_candidate_matches(driver, matches):
    """Write CANDIDATE_MATCH edges to Neo4j."""
    with driver.session() as session:
        r = session.run(CLEAR_CANDIDATE_MATCH).single()
        print(f"  Cleared {r['deleted']} old CANDIDATE_MATCH edges")

        total = 0
        for i in range(0, len(matches), BATCH_SIZE):
            batch = matches[i:i + BATCH_SIZE]
            session.run(CREATE_CANDIDATE_MATCH, batch=batch)
            total += len(batch)

    print(f"  Created {total} CANDIDATE_MATCH edges")
    return total


# =============================================================================
# PHASE 2B: DEATH YEAR GHOST DETECTION (for non-governor matches)
# =============================================================================

def detect_death_year_ghosts(matches):
    """Find matched officials appearing after their WD_Person death year."""
    ghosts = []
    for m in matches:
        death_year = m.get("death_year")
        if not death_year:
            continue
        if m["last_year"] > death_year:
            posthumous_years = [
                y for y in range(m["first_year"], m["last_year"] + 1)
                if y > death_year
            ]
            ghosts.append({
                **m,
                "posthumous_years": posthumous_years,
                "posthumous_count": len(posthumous_years),
            })
    return ghosts


QUARANTINE_GHOSTS_QUERY = """
UNWIND $batch AS g
MATCH (o:COL_Official {id: g.official_id})<-[:RECORD_OF]-(pr:COL_PersonRecord)
WHERE pr.year > g.death_year
  AND (pr.quarantined IS NULL OR pr.quarantined = false)
SET pr.quarantined = true,
    pr.quarantine_reason = 'posthumous_listing:died_' + toString(g.death_year) + ':wd:' + g.qid,
    pr.quarantine_date = $today
RETURN count(pr) AS quarantined
"""


def quarantine_death_year_ghosts(session, ghosts, today):
    """Mark posthumous PersonRecords as quarantined."""
    total = 0
    for i in range(0, len(ghosts), BATCH_SIZE):
        batch = ghosts[i:i + BATCH_SIZE]
        r = session.run(QUARANTINE_GHOSTS_QUERY, batch=batch, today=today).single()
        total += r["quarantined"]
    return total


# =============================================================================
# STATS & CLEAR
# =============================================================================

def print_stats(driver):
    """Report on quarantine and matching status."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("GHOST DETECTION STATISTICS")
        print("=" * 60)

        r = session.run(
            "MATCH (pr:COL_PersonRecord) "
            "WHERE pr.quarantined = true "
            "RETURN count(pr) AS n"
        ).single()
        print(f"\n  Quarantined PersonRecords: {r['n']}")

        # By reason prefix
        result = session.run(
            "MATCH (pr:COL_PersonRecord) "
            "WHERE pr.quarantined = true "
            "WITH CASE "
            "  WHEN pr.quarantine_reason STARTS WITH 'historical_governor' THEN 'historical_governor' "
            "  WHEN pr.quarantine_reason STARTS WITH 'posthumous_listing' THEN 'posthumous_listing' "
            "  ELSE 'other' END AS category, pr "
            "RETURN category, count(pr) AS n "
            "ORDER BY n DESC"
        )
        print("\n  By category:")
        for r in result:
            print(f"    {r['category']:<30} {r['n']:>6}")

        # Top colonies
        result = session.run(
            "MATCH (pr:COL_PersonRecord) "
            "WHERE pr.quarantined = true "
            "RETURN pr.colony AS colony, count(pr) AS n "
            "ORDER BY n DESC LIMIT 15"
        )
        print("\n  Top colonies by quarantined records:")
        for r in result:
            print(f"    {r['colony']:<35} {r['n']:>6}")

        # CANDIDATE_MATCH edges
        r = session.run(
            "MATCH ()-[r:CANDIDATE_MATCH]->() RETURN count(r) AS n"
        ).single()
        print(f"\n  CANDIDATE_MATCH edges: {r['n']}")

        result = session.run(
            "MATCH ()-[r:CANDIDATE_MATCH]->() "
            "RETURN r.tier AS tier, count(r) AS n, avg(r.confidence) AS avg_conf "
            "ORDER BY tier"
        )
        for r in result:
            print(f"    Tier {r['tier']}: {r['n']} matches (avg conf {r['avg_conf']:.2f})")

        r = session.run(
            "MATCH (o:COL_Official) "
            "OPTIONAL MATCH (o)-[:CANDIDATE_MATCH]->(p:WD_Person) "
            "RETURN count(o) AS total, count(p) AS matched"
        ).single()
        if r["total"] > 0:
            print(f"\n  COL_Officials matched: {r['matched']}/{r['total']} "
                  f"({100*r['matched']/r['total']:.1f}%)")


def clear_all(driver):
    """Remove all quarantine flags and CANDIDATE_MATCH edges."""
    with driver.session() as session:
        r = session.run(
            "MATCH (pr:COL_PersonRecord) "
            "WHERE pr.quarantined = true "
            "REMOVE pr.quarantined, pr.quarantine_reason, pr.quarantine_date "
            "RETURN count(pr) AS n"
        ).single()
        print(f"  Cleared quarantine from {r['n']} PersonRecords")

        r = session.run(CLEAR_CANDIDATE_MATCH).single()
        print(f"  Deleted {r['deleted']} CANDIDATE_MATCH edges")


# =============================================================================
# REPORT GENERATION
# =============================================================================

def generate_report(gov_actions, matches, ghosts, write_file=False):
    """Print and optionally write ghost detection report."""

    lines = []
    lines.append("# Ghost Detection Report")
    lines.append(f"\nGenerated: {date.today().isoformat()}")
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append("### Phase 1: Historical Official Detection")
    gov_phase1 = [a for a in gov_actions if a.get("is_governor")]
    other_phase1 = [a for a in gov_actions if not a.get("is_governor")]
    lines.append(f"- **Historical PersonRecords identified**: {len(gov_actions)}")
    lines.append(f"  - Governor chain entries: {len(gov_phase1)}")
    lines.append(f"  - Other historical officials: {len(other_phase1)}")
    if gov_actions:
        colonies = set(a["colony"] for a in gov_actions)
        officials = set(a["qid"] for a in gov_actions)
        lines.append(f"- **Colonies affected**: {len(colonies)}")
        lines.append(f"- **Unique WD persons**: {len(officials)}")
    lines.append("")

    lines.append("### Phase 2: Name-Matched Ghost Detection")
    lines.append(f"- **CANDIDATE_MATCH edges**: {len(matches)}")
    tier_counts = defaultdict(int)
    for m in matches:
        tier_counts[m["tier"]] += 1
    for tier in sorted(tier_counts):
        lines.append(f"  - Tier {tier}: {tier_counts[tier]}")
    lines.append(f"- **Death-year ghosts**: {len(ghosts)}")
    if ghosts:
        total_posthumous = sum(g["posthumous_count"] for g in ghosts)
        lines.append(f"- **Posthumous PersonRecords**: {total_posthumous}")
    lines.append("")

    # Phase 1 details
    if gov_actions:
        lines.append("## Historical Official Listings (Phase 1)")
        lines.append("")

        # Group by colony and official
        by_colony_off = defaultdict(list)
        for a in gov_actions:
            key = (a["colony"], a.get("official_name", a.get("governor_name", "")),
                   a["qid"], a["tenure_end"])
            by_colony_off[key].append(a)

        lines.append("| Colony | Official | WD Position | Tenure End | Ghost Records | Wikidata |")
        lines.append("|--------|----------|-------------|-----------|--------------|----------|")
        for (colony, off_name, qid, end_year), actions in sorted(by_colony_off.items()):
            years = sorted(set(a["year"] for a in actions))
            year_range = f"{years[0]}-{years[-1]}" if len(years) > 1 else str(years[0])
            wd_pos = actions[0].get("wd_position", "Governor")
            # Truncate long position labels
            if len(wd_pos) > 35:
                wd_pos = wd_pos[:32] + "..."
            lines.append(
                f"| {colony} | {off_name} | {wd_pos} | {end_year} "
                f"| {len(actions)} ({year_range}) "
                f"| [{qid}](https://www.wikidata.org/wiki/{qid}) |"
            )
        lines.append("")

    # Death-year ghost details
    if ghosts:
        lines.append("## Death-Year Ghosts (Phase 2)")
        lines.append("")
        lines.append("| Official | Colony | Death Year | Last COL Year | Posthumous | Wikidata |")
        lines.append("|----------|--------|-----------|---------------|-----------|----------|")
        for g in sorted(ghosts, key=lambda x: -x["posthumous_count"])[:50]:
            lines.append(
                f"| {g['official_name']} | {g['colony']} | {g['death_year']} "
                f"| {g['last_year']} | {g['posthumous_count']} "
                f"| [{g['qid']}](https://www.wikidata.org/wiki/{g['qid']}) |"
            )
        if len(ghosts) > 50:
            lines.append(f"| ... | ... | ... | ... | ... | ({len(ghosts) - 50} more) |")
        lines.append("")

    report_text = "\n".join(lines)

    # Terminal output
    print("\n" + "=" * 70)
    print("GHOST DETECTION RESULTS")
    print("=" * 70)

    print(f"\n  Phase 1 — Historical Official Detection:")
    print(f"    PersonRecords to quarantine: {len(gov_actions)}")
    gov_p1 = sum(1 for a in gov_actions if a.get("is_governor"))
    other_p1 = len(gov_actions) - gov_p1
    print(f"      Governors: {gov_p1}, Other officials: {other_p1}")
    if gov_actions:
        colonies = set(a["colony"] for a in gov_actions)
        officials = set(a["qid"] for a in gov_actions)
        print(f"    Colonies: {len(colonies)}")
        print(f"    Unique WD persons: {len(officials)}")

        # Show top colonies
        col_counts = defaultdict(int)
        for a in gov_actions:
            col_counts[a["colony"]] += 1
        print(f"\n    Top colonies:")
        for colony, n in sorted(col_counts.items(), key=lambda x: -x[1])[:10]:
            print(f"      {colony:<35} {n:>4} records")

    print(f"\n  Phase 2 — Name-Matched Ghosts:")
    print(f"    CANDIDATE_MATCH edges: {len(matches)}")
    for tier in sorted(tier_counts):
        print(f"      Tier {tier}: {tier_counts[tier]}")
    print(f"    Death-year ghosts: {len(ghosts)}")
    if ghosts:
        total_posthumous = sum(g["posthumous_count"] for g in ghosts)
        print(f"    Posthumous PersonRecords: {total_posthumous}")
        print(f"\n    Top ghosts:")
        for g in sorted(ghosts, key=lambda x: -x["posthumous_count"])[:10]:
            print(f"      {g['official_name']:<35} {g['colony']:<25} "
                  f"died {g['death_year']}, until {g['last_year']} ({g['posthumous_count']})")

    if write_file:
        report_path = REPO_DIR / "GHOST_DETECTION_REPORT.md"
        with open(report_path, "w") as f:
            f.write(report_text)
        print(f"\nReport written to {report_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Detect ghost/historical entries in Colonial Office Lists"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Detect only, no writes to Neo4j")
    parser.add_argument("--stats", action="store_true",
                        help="Report quarantine/matching status")
    parser.add_argument("--clear", action="store_true",
                        help="Remove all quarantine flags and CANDIDATE_MATCH edges")
    parser.add_argument("--governors-only", action="store_true",
                        help="Only governor chain quarantine")
    parser.add_argument("--link-only", action="store_true",
                        help="Only name matching, no quarantine")
    parser.add_argument("--report", action="store_true",
                        help="Write GHOST_DETECTION_REPORT.md")
    args = parser.parse_args()

    print("=" * 60)
    print("COL GHOST ENTRY DETECTION")
    print("=" * 60)

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print(f"Connected to {NEO4J_URI}")

        if args.stats:
            print_stats(driver)
            return

        if args.clear:
            clear_all(driver)
            return

        # --- Load Wikidata ---
        print("\nLoading Wikidata persons...")
        wd_persons = load_wd_persons()
        wd_with_death = sum(1 for p in wd_persons if p["deathYear"])
        print(f"  {len(wd_persons)} persons ({wd_with_death} with death years)")

        print("Loading colony crosswalk...")
        col_to_qids = load_crosswalk()
        print(f"  {len(col_to_qids)} colonies with Wikidata QIDs")

        today = date.today().isoformat()

        # =============================================================
        # PHASE 1: Historical official detection (PRIMARY)
        # =============================================================
        print("\n--- Phase 1: Historical Official Detection ---")
        print("Building official tenure index from Wikidata...")
        tenures = load_official_tenures(wd_persons, col_to_qids)
        total_entries = sum(len(v) for v in tenures.values())
        gov_entries = sum(
            1 for v in tenures.values() for e in v if e["is_governor"]
        )
        print(f"  {len(tenures)} colonies, {total_entries} tenure entries "
              f"({gov_entries} governors, {total_entries - gov_entries} other officials)")

        print("Matching against COL PersonRecords...")
        with driver.session() as session:
            gov_actions = detect_historical_officials(session, tenures)
        print(f"  {len(gov_actions)} historical PersonRecords identified")

        if gov_actions and not args.dry_run:
            print("Quarantining historical governor records...")
            with driver.session() as session:
                n = quarantine_historical_governors(session, gov_actions, today)
            print(f"  Quarantined {n} PersonRecords")

        if args.governors_only:
            generate_report(gov_actions, [], [], write_file=args.report)
            if args.dry_run:
                print("\n[DRY RUN] No data written.")
            return

        # =============================================================
        # PHASE 2: Broader name matching (SECONDARY)
        # =============================================================
        print("\n--- Phase 2: Name-Matched Ghost Detection ---")
        print("Fetching COL_Official nodes...")
        with driver.session() as session:
            officials = [dict(r) for r in session.run(
                "MATCH (o:COL_Official) "
                "RETURN o.id AS id, o.name AS name, o.colony AS colony, "
                "       o.first_year AS first_year, o.last_year AS last_year, "
                "       o.num_editions AS num_editions"
            )]
        print(f"  {len(officials)} COL_Officials")

        print("Matching to WD_Persons...")
        matches = match_officials_to_wd(officials, wd_persons, col_to_qids)
        print(f"  {len(matches)} matches")

        tier_counts = defaultdict(int)
        for m in matches:
            tier_counts[m["tier"]] += 1
        for tier in sorted(tier_counts):
            print(f"    Tier {tier}: {tier_counts[tier]}")

        if not args.dry_run:
            print("Writing CANDIDATE_MATCH edges...")
            write_candidate_matches(driver, matches)

        if args.link_only:
            generate_report(gov_actions, matches, [], write_file=args.report)
            if args.dry_run:
                print("\n[DRY RUN] No data written.")
            return

        # Detect death-year ghosts from matches
        print("Detecting death-year ghosts...")
        ghosts = detect_death_year_ghosts(matches)
        print(f"  {len(ghosts)} ghost officials")

        if ghosts and not args.dry_run:
            print("Quarantining posthumous PersonRecords...")
            with driver.session() as session:
                n = quarantine_death_year_ghosts(session, ghosts, today)
            print(f"  Quarantined {n} PersonRecords")

        # --- Report ---
        generate_report(gov_actions, matches, ghosts, write_file=args.report)

        if args.dry_run:
            print("\n[DRY RUN] No data written.")

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()

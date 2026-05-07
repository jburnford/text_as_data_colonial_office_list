"""
COL Ground Truth Builder
========================

Matches external career knowledge (Wikidata + Gemini) to COL_Official nodes
to produce labeled ground truth for ML career discovery.

FOCUS: Within-colony career integrity. The primary question is whether our
pipeline correctly groups year-sliced PersonRecords into COL_Official nodes.
For each known person, we find all same-surname officials in that colony and
classify them as: (a) belonging to this career, or (b) a different person.
This gives us both positive pairs (split careers) and hard negatives
(same surname, same colony, same era, different person).

Outputs:
  - known_careers.json: careers with matched COL_Official IDs
  - ground_truth_pairs.csv: positive/negative pairs for ML training
  - gt_matching_review.csv: sample matches for human spot-check
  - gt_stats.txt: summary statistics

Usage:
    python col_build_ground_truth.py                # full run
    python col_build_ground_truth.py --stats         # just report what we have
    python col_build_ground_truth.py --diagnose      # trace matching failures

Requires:
    pip install neo4j
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

# Import name utilities from existing pipeline
from col_normalize_names import initials_compatible, clean_given_names

# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent

# Load .env file if present (handles special characters in passwords)
_env_file = REPO_DIR / ".env"
if _env_file.exists():
    with open(_env_file) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _key, _val = _line.split("=", 1)
                os.environ.setdefault(_key.strip(), _val.strip())

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")

WD_PEOPLE_FILE = REPO_DIR / "wikidata_harvest" / "merged_all_people.json"
CROSSWALK_FILE = REPO_DIR / "scaffolding" / "col_kg_crosswalk.json"
LLM_CAREERS_DIR = REPO_DIR / "llm_careers"

OUTPUT_DIR = REPO_DIR / "ml_data"
CURATED_CAREERS_FILE = OUTPUT_DIR / "curated_cross_colony_careers.json"
KNOWN_CAREERS_FILE = OUTPUT_DIR / "known_careers.json"
GT_PAIRS_FILE = OUTPUT_DIR / "ground_truth_pairs.csv"
REVIEW_FILE = OUTPUT_DIR / "gt_matching_review.csv"
STATS_FILE = OUTPUT_DIR / "gt_stats.txt"

# Year tolerance for matching
YEAR_TOLERANCE = 3

# Our data range
DATA_START = 1877
DATA_END = 1966


# =============================================================================
# COLONY NAME MAPPING
# =============================================================================

def build_colony_qid_map():
    """Map Wikidata QIDs to COL_Territory names using the crosswalk."""
    with open(CROSSWALK_FILE) as f:
        crosswalk = json.load(f)

    qid_to_colony = {}
    for col_name, info in crosswalk.items():
        for m in info["mappings"]:
            qid_to_colony[m["wikidata_id"]] = col_name
    return qid_to_colony


# =============================================================================
# LOAD EXTERNAL CAREER DATA
# =============================================================================

def load_wd_people(qid_to_colony):
    """Load Wikidata people who have positions in mapped colonies.

    Filters out:
    - Positions with no dates (can't verify overlap with our 1877-1966 data)
    - Positions outside our data range
    - Local government politicians (parliament members, ministers, premiers)
      who would not appear in the Colonial Office List

    Returns list of dicts with standardized fields:
        source, source_id, person_name, surname, given_names,
        positions: [{colony, position_label, start_year, end_year}]
    """
    with open(WD_PEOPLE_FILE) as f:
        raw = json.load(f)

    people = []
    skipped_undated = 0
    skipped_local_govt = 0

    for p in raw:
        # Map positions to our colonies
        mapped_positions = []
        for pos in p.get("positions", []):
            cq = pos.get("colony_qid", "")
            if cq not in qid_to_colony:
                continue

            start_year = _parse_wd_year(pos.get("start", ""))
            end_year = _parse_wd_year(pos.get("end", ""))

            # Skip undated positions — can't verify they overlap our data
            if start_year is None and end_year is None:
                skipped_undated += 1
                continue

            # Skip positions entirely outside our data range
            pos_end = end_year or (start_year + 30 if start_year else None)
            pos_start = start_year or (end_year - 30 if end_year else None)
            if pos_end and pos_end < DATA_START - YEAR_TOLERANCE:
                continue
            if pos_start and pos_start > DATA_END + YEAR_TOLERANCE:
                continue

            # Skip local government positions (not in Colonial Office List)
            label = pos.get("position_label", "")
            if _is_local_govt_position(label):
                skipped_local_govt += 1
                continue

            mapped_positions.append({
                "colony": qid_to_colony[cq],
                "position_label": label,
                "start_year": start_year,
                "end_year": end_year,
            })

        if not mapped_positions:
            continue

        # Parse name: WD format is "FirstName LastName" or with titles
        name = p.get("name", "").strip()
        surname, given = _parse_wd_name(name)
        if not surname:
            continue

        people.append({
            "source": "wikidata",
            "source_id": p["qid"],
            "person_name": name,
            "surname": surname.lower(),
            "given_names": given,
            "positions": mapped_positions,
        })

    print(f"    (filtered: {skipped_undated} undated positions, "
          f"{skipped_local_govt} local govt positions)")
    return people


def _parse_wd_year(date_str):
    """Extract year from WD date string like '1951-01-01' or ''."""
    if not date_str:
        return None
    m = re.match(r"(\d{4})", date_str)
    return int(m.group(1)) if m else None


# Patterns for local government positions (NOT in Colonial Office List)
_LOCAL_GOVT_PATTERNS = [
    re.compile(r"[Mm]ember of the.*(?:Parliament|Assembly|Legislature|Senate|House)", re.I),
    re.compile(r"[Mm]ember of (?:the )?(?:\d+(?:st|nd|rd|th) )?Parliament", re.I),
    re.compile(r"[Pp]remier of", re.I),
    re.compile(r"[Mm]inister (?:of|for) (?!State)(?!Colony)", re.I),
    re.compile(r"[Tt]reasurer of", re.I),
    re.compile(r"[Mm]ayor of", re.I),
    re.compile(r"[Mm]ember of.*Legislative Council", re.I),
    re.compile(r"[Ss]peaker of.*(?:Assembly|House)", re.I),
    re.compile(r"[Ll]eader of the [Oo]pposition", re.I),
]


def _is_local_govt_position(label):
    """Check if a position label indicates local government (not colonial service)."""
    for pat in _LOCAL_GOVT_PATTERNS:
        if pat.search(label):
            return True
    return False


# Title/peerage patterns to strip before extracting surname
_TITLE_SUFFIXES = re.compile(
    r",?\s*\d+(?:st|nd|rd|th)\s+"
    r"(?:Baron(?:et|ess)?|Viscount(?:ess)?|Earl|Marquess|Duke|Duchess|"
    r"Count(?:ess)?|Lord|Lady)\s+(?:of\s+)?\w+.*$",
    re.IGNORECASE,
)
_TITLE_PREFIXES = re.compile(
    r"^(?:Sir|Dame|Lord|Lady|The\s+(?:Right\s+)?(?:Hon(?:ourable|\.)?)\s+)",
    re.IGNORECASE,
)
_JR_SR = re.compile(r",?\s+(?:Jr\.?|Sr\.?|III?|IV)$", re.IGNORECASE)


def _parse_wd_name(name):
    """Parse WD name into (surname, given_names).

    Handles:
    - 'George Bowen' → ('Bowen', 'George')
    - 'Arthur Lawley, 6th Baron Wenlock' → ('Lawley', 'Arthur')
    - 'Sir John Dalling, 1st Baronet' → ('Dalling', 'John')
    - 'Howe Browne, 2nd Marquess of Sligo' → ('Browne', 'Howe')
    - 'Robert Napier, 1st Baron Napier of Magdala' → ('Napier', 'Robert')
    - 'James Norton, Jr.' → ('Norton', 'James')
    """
    if not name:
        return "", ""

    # Strip title suffixes (peerage)
    cleaned = _TITLE_SUFFIXES.sub("", name).strip()
    # Strip Jr./Sr./III
    cleaned = _JR_SR.sub("", cleaned).strip()
    # Strip title prefixes
    cleaned = _TITLE_PREFIXES.sub("", cleaned).strip()
    # Remove trailing commas
    cleaned = cleaned.rstrip(",").strip()

    if not cleaned:
        return "", ""

    parts = cleaned.split()
    if len(parts) == 1:
        return parts[0], ""

    # Handle common surname particles
    particles = {"de", "van", "von", "du", "le", "la", "di", "del"}
    if len(parts) >= 3 and parts[-2].lower() in particles:
        surname = " ".join(parts[-2:])
        given = " ".join(parts[:-2])
    else:
        surname = parts[-1]
        given = " ".join(parts[:-1])

    return surname, given


def load_gemini_careers(qid_to_colony):
    """Load Gemini-extracted careers from llm_careers/*.json.

    Returns list of dicts with same structure as WD people.
    """
    # Build reverse map for colony name lookup
    all_colony_names = set(qid_to_colony.values())

    people = []
    career_id = 0

    for json_file in sorted(LLM_CAREERS_DIR.glob("*.json")):
        colony_key = json_file.stem  # e.g., 'ceylon'
        # Find matching colony name (case-insensitive)
        colony_name = None
        for cn in all_colony_names:
            if cn.lower() == colony_key.lower():
                colony_name = cn
                break
        if not colony_name:
            colony_name = colony_key.title()

        with open(json_file) as f:
            careers = json.load(f)

        for career in careers:
            career_id += 1
            name = career.get("name", "").strip()
            if not name:
                continue

            # Gemini names are in "Surname, Given" format
            surname, given = _parse_gemini_name(name)
            if not surname:
                continue

            # Convert stints to positions
            positions = []
            for stint in career.get("stints", []):
                years = stint.get("years", [])
                if not years:
                    continue
                positions.append({
                    "colony": colony_name,
                    "position_label": stint.get("position", ""),
                    "start_year": min(years),
                    "end_year": max(years),
                })

            if not positions:
                continue

            # Also store the raw year list for precise stint matching
            all_years = sorted(set(
                y for stint in career.get("stints", [])
                for y in stint.get("years", [])
            ))

            people.append({
                "source": "gemini",
                "source_id": f"gemini_{colony_key}_{career_id:04d}",
                "person_name": name,
                "surname": surname.lower(),
                "given_names": given,
                "positions": positions,
                "all_years": all_years,
                "colony": colony_name,
            })

    return people


def _parse_gemini_name(name):
    """Parse Gemini name 'Surname, Given' or 'Surname, G. H.' into (surname, given)."""
    if "," in name:
        parts = name.split(",", 1)
        return parts[0].strip(), parts[1].strip()
    return name.strip(), ""


# =============================================================================
# LOAD COL_OFFICIALS FROM NEO4J
# =============================================================================

def load_officials(driver):
    """Load all COL_Official nodes, indexed by (surname_lower, colony).

    Returns:
        by_surname: {surname_lower: [official_dict, ...]}
        by_surname_colony: {(surname_lower, colony): [official_dict, ...]}
    """
    query = """
    MATCH (o:COL_Official)
    RETURN o.id AS id,
           o.name AS name,
           o.colony AS colony,
           o.first_year AS first_year,
           o.last_year AS last_year,
           o.num_editions AS num_editions
    """

    by_surname = defaultdict(list)
    by_surname_colony = defaultdict(list)
    total = 0

    with driver.session() as session:
        result = session.run(query)
        for record in result:
            official = dict(record)
            name = official.get("name", "") or ""

            # Extract surname and given from "Surname, Given" format
            if "," in name:
                surname = name.split(",", 1)[0].strip().lower()
                official["_given"] = name.split(",", 1)[1].strip()
            else:
                surname = name.strip().lower()
                official["_given"] = ""

            official["_surname"] = surname
            by_surname[surname].append(official)
            by_surname_colony[(surname, official["colony"])].append(official)
            total += 1

    print(f"  Loaded {total} COL_Officials across {len(by_surname)} distinct surnames")
    return by_surname, by_surname_colony


# =============================================================================
# WITHIN-COLONY MATCHING (PRIMARY MODE)
# =============================================================================

def load_curated_careers():
    """Load hand-curated cross-colony careers.

    These are historically verified careers of known colonial officials
    (governors, senior administrators) whose movements between colonies
    are well-documented. Official IDs are pre-verified against Neo4j.

    Returns list of career dicts with official IDs, or empty list if file missing.
    """
    if not CURATED_CAREERS_FILE.exists():
        return []
    with open(CURATED_CAREERS_FILE) as f:
        return json.load(f)


def match_within_colony(gemini_people, wd_people, by_surname_colony, by_surname):
    """Match external careers to COL_Officials within each colony.

    For each known person:
    1. Find ALL same-surname officials in that colony
    2. Classify each as: SAME_PERSON or DIFFERENT_PERSON
    3. Generate positive pairs (same person) and hard negatives (different person)

    Returns: careers list, positive_pairs, negative_pairs, stats
    """
    careers = []
    positive_pairs = []
    negative_pairs = []
    stats = {
        "gemini_total": len(gemini_people),
        "gemini_matched": 0,
        "gemini_multi_official": 0,
        "gemini_with_negatives": 0,
        "wd_total": len(wd_people),
        "wd_matched": 0,
        "wd_multi_official": 0,
        "wd_with_negatives": 0,
        "total_positive_pairs": 0,
        "total_negative_pairs": 0,
        "total_anchors": 0,
        "conflicts": [],
    }

    # Track which officials are claimed
    official_claims = defaultdict(list)

    # --- GEMINI CAREERS (within-colony, best ground truth) ---
    for person in gemini_people:
        colony = person["colony"]
        surname = person["surname"]
        given = person["given_names"]

        # Get ALL same-surname officials in this colony
        candidates = by_surname_colony.get((surname, colony), [])
        if not candidates:
            continue

        # Compute the career's overall year range
        all_years = person.get("all_years", [])
        if not all_years:
            # Fall back to position year ranges
            for pos in person["positions"]:
                if pos["start_year"]:
                    all_years.append(pos["start_year"])
                if pos["end_year"]:
                    all_years.append(pos["end_year"])
        if not all_years:
            continue

        career_min = max(min(all_years), DATA_START - YEAR_TOLERANCE)
        career_max = max(all_years)

        # Classify each candidate
        same_person = []  # officials belonging to this career
        diff_person = []  # officials confirmed as different people
        ambiguous = []    # can't tell

        for official in candidates:
            fy = official["first_year"]
            ly = official["last_year"]
            if fy is None or ly is None:
                continue

            # Check year overlap with career range
            has_year_overlap = (fy <= career_max + YEAR_TOLERANCE and
                                ly >= career_min - YEAR_TOLERANCE)

            # Check name compatibility
            name_compat = _check_name_compat(given, official["_given"])

            if has_year_overlap and name_compat != "incompatible":
                same_person.append({
                    "official": official,
                    "name_match": name_compat,
                })
            elif not has_year_overlap and name_compat == "incompatible":
                diff_person.append(official)
            elif not has_year_overlap:
                # Same-ish name but outside career years — different person
                # (unless it's a very close gap)
                gap = min(abs(fy - career_max), abs(career_min - ly))
                if gap > 10:
                    diff_person.append(official)
                else:
                    ambiguous.append(official)
            elif name_compat == "incompatible" and has_year_overlap:
                # Different initials but overlapping years — definitely different
                diff_person.append(official)
            else:
                ambiguous.append(official)

        if not same_person:
            continue

        stats["gemini_matched"] += 1

        # Record career
        matched_ids = [sp["official"]["id"] for sp in same_person]
        career_record = {
            "career_id": person["source_id"],
            "source": "gemini",
            "person_name": person["person_name"],
            "surname": surname,
            "colony": colony,
            "career_years": f"{min(all_years)}-{max(all_years)}",
            "officials": [{
                "official_id": sp["official"]["id"],
                "name": sp["official"]["name"],
                "years": f"{sp['official']['first_year']}-{sp['official']['last_year']}",
                "name_match": sp["name_match"],
            } for sp in same_person],
            "different_persons": [{
                "official_id": dp["id"],
                "name": dp["name"],
                "years": f"{dp['first_year']}-{dp['last_year']}",
            } for dp in diff_person],
        }
        careers.append(career_record)

        for sp in same_person:
            official_claims[sp["official"]["id"]].append(person["source_id"])

        if len(same_person) >= 2:
            stats["gemini_multi_official"] += 1
            # Generate positive pairs
            for a, b in combinations(same_person, 2):
                positive_pairs.append({
                    "official_a": a["official"]["id"],
                    "official_b": b["official"]["id"],
                    "label": 1,
                    "source": "gemini",
                    "career_id": person["source_id"],
                    "pair_type": "within_colony",
                })
        else:
            stats["total_anchors"] += 1

        # Generate hard negatives: same_person officials vs diff_person officials
        if diff_person:
            stats["gemini_with_negatives"] += 1
            for sp in same_person:
                for dp in diff_person:
                    negative_pairs.append({
                        "official_a": sp["official"]["id"],
                        "official_b": dp["id"],
                        "label": 0,
                        "source": "gemini_hard_negative",
                        "career_id": person["source_id"],
                        "pair_type": "within_colony_hard",
                    })

        # Also: pairs among diff_person officials are NOT necessarily
        # the same as each other (they could be 2+ different people).
        # We don't label these — they're unlabeled.

    # --- WIKIDATA CAREERS ---
    for person in wd_people:
        given = person["given_names"]
        surname = person["surname"]

        # Group positions by colony for within-colony matching
        by_colony = defaultdict(list)
        for pos in person["positions"]:
            by_colony[pos["colony"]].append(pos)

        person_matched_officials = []

        for colony, positions in by_colony.items():
            candidates = by_surname_colony.get((surname, colony), [])
            if not candidates:
                continue

            # Year range for this person in this colony
            years = []
            for pos in positions:
                if pos["start_year"]:
                    years.append(pos["start_year"])
                if pos["end_year"]:
                    years.append(pos["end_year"])
            if not years:
                # Undated — try name-only matching if surname is rare enough
                if len(candidates) == 1:
                    off = candidates[0]
                    nc = _check_name_compat(given, off["_given"])
                    if nc != "incompatible":
                        person_matched_officials.append({
                            "official": off,
                            "name_match": nc,
                            "colony": colony,
                        })
                continue

            career_min = max(min(years), DATA_START - YEAR_TOLERANCE)
            career_max = max(years)

            same_person = []
            diff_person = []

            for official in candidates:
                fy = official["first_year"]
                ly = official["last_year"]
                if fy is None or ly is None:
                    continue

                has_year_overlap = (fy <= career_max + YEAR_TOLERANCE and
                                    ly >= career_min - YEAR_TOLERANCE)
                name_compat = _check_name_compat(given, official["_given"])

                if has_year_overlap and name_compat != "incompatible":
                    same_person.append({
                        "official": official,
                        "name_match": name_compat,
                        "colony": colony,
                    })
                elif name_compat == "incompatible" and has_year_overlap:
                    diff_person.append(official)
                elif not has_year_overlap:
                    gap = min(abs(fy - career_max), abs(career_min - ly))
                    if gap > 10 or name_compat == "incompatible":
                        diff_person.append(official)

            person_matched_officials.extend(same_person)

            # Generate negatives for this colony
            for sp in same_person:
                for dp in diff_person:
                    negative_pairs.append({
                        "official_a": sp["official"]["id"],
                        "official_b": dp["id"],
                        "label": 0,
                        "source": "wd_hard_negative",
                        "career_id": person["source_id"],
                        "pair_type": "within_colony_hard",
                    })

        if not person_matched_officials:
            continue

        stats["wd_matched"] += 1

        career_record = {
            "career_id": person["source_id"],
            "source": "wikidata",
            "person_name": person["person_name"],
            "surname": surname,
            "colony": ",".join(sorted(set(m["colony"] for m in person_matched_officials))),
            "officials": [{
                "official_id": m["official"]["id"],
                "name": m["official"]["name"],
                "years": f"{m['official']['first_year']}-{m['official']['last_year']}",
                "name_match": m["name_match"],
                "colony": m["colony"],
            } for m in person_matched_officials],
        }
        careers.append(career_record)

        for m in person_matched_officials:
            official_claims[m["official"]["id"]].append(person["source_id"])

        if len(person_matched_officials) >= 2:
            stats["wd_multi_official"] += 1
            for a, b in combinations(person_matched_officials, 2):
                pair_type = "within_colony" if a["colony"] == b["colony"] else "cross_colony"
                positive_pairs.append({
                    "official_a": a["official"]["id"],
                    "official_b": b["official"]["id"],
                    "label": 1,
                    "source": "wikidata",
                    "career_id": person["source_id"],
                    "pair_type": pair_type,
                })
        else:
            stats["total_anchors"] += 1

    # Check for conflicts
    for off_id, claimants in official_claims.items():
        if len(claimants) >= 2:
            # Filter to unique claimants
            unique = list(set(claimants))
            if len(unique) >= 2:
                stats["conflicts"].append({
                    "official_id": off_id,
                    "claimants": unique,
                })

    # --- CURATED CROSS-COLONY CAREERS ---
    curated = load_curated_careers()
    stats["curated_careers"] = len(curated)
    stats["curated_pairs"] = 0

    for career in curated:
        off_ids = career["officials"]
        if len(off_ids) < 2:
            # Single-official curated entry — anchor only
            stats["total_anchors"] += 1
            careers.append({
                "career_id": career["career_id"],
                "source": "curated",
                "person_name": career["person_name"],
                "surname": career["person_name"].split(",")[0].split()[-1].lower()
                           if "," in career["person_name"]
                           else career["person_name"].split()[-1].lower(),
                "colony": "cross-colony",
                "officials": [{"official_id": oid, "name_match": "curated"} for oid in off_ids],
            })
            continue

        # Generate positive pairs
        for a, b in combinations(off_ids, 2):
            positive_pairs.append({
                "official_a": a,
                "official_b": b,
                "label": 1,
                "source": "curated",
                "career_id": career["career_id"],
                "pair_type": "cross_colony",
            })
            stats["curated_pairs"] += 1

        # Track claims
        for oid in off_ids:
            official_claims[oid].append(career["career_id"])

        careers.append({
            "career_id": career["career_id"],
            "source": "curated",
            "person_name": career["person_name"],
            "surname": career["person_name"].split(",")[0].split()[-1].lower()
                       if "," in career["person_name"]
                       else career["person_name"].split()[-1].lower(),
            "colony": "cross-colony",
            "officials": [{"official_id": oid, "name_match": "curated"} for oid in off_ids],
        })

    # Recheck conflicts after adding curated
    stats["conflicts"] = []
    for off_id, claimants in official_claims.items():
        unique = list(set(claimants))
        if len(unique) >= 2:
            stats["conflicts"].append({
                "official_id": off_id,
                "claimants": unique,
            })

    stats["total_positive_pairs"] = len(positive_pairs)
    stats["total_negative_pairs"] = len(negative_pairs)

    return careers, positive_pairs, negative_pairs, stats


def _check_name_compat(ext_given, off_given):
    """Check name compatibility between external person and official.

    Returns: 'exact', 'initial_compatible', 'bare', or 'incompatible'
    """
    if not ext_given and not off_given:
        return "bare"
    if not ext_given or not off_given:
        return "bare"

    ext_clean = clean_given_names(ext_given)
    off_clean = clean_given_names(off_given)

    if not ext_clean or not off_clean:
        return "bare"

    # Check exact match first
    if ext_clean.lower() == off_clean.lower():
        return "exact"

    # Check initials compatibility
    if initials_compatible(ext_clean, off_clean):
        return "initial_compatible"

    return "incompatible"


# =============================================================================
# DIAGNOSTICS
# =============================================================================

def diagnose_within_colony(gemini_people, by_surname_colony, n=30):
    """Show detailed matching trace for Gemini careers."""
    import random
    random.seed(42)

    # Focus on multi-stint careers that should produce pairs
    multi_stint = [p for p in gemini_people if len(p.get("positions", [])) >= 2]
    sample = random.sample(multi_stint, min(n, len(multi_stint)))

    print(f"\n{'='*80}")
    print(f"WITHIN-COLONY DIAGNOSTICS — {len(sample)} multi-stint Gemini careers")
    print(f"{'='*80}")

    for person in sample:
        colony = person["colony"]
        surname = person["surname"]
        candidates = by_surname_colony.get((surname, colony), [])

        all_years = person.get("all_years", [])
        career_range = f"{min(all_years)}-{max(all_years)}" if all_years else "?"

        print(f"\n--- {person['person_name']} in {colony} ({career_range}) ---")
        print(f"  Stints: {len(person['positions'])}")
        for pos in person["positions"]:
            print(f"    {pos['start_year']}-{pos['end_year']}: {pos['position_label']}")

        print(f"  Same-surname officials in {colony}: {len(candidates)}")
        for c in sorted(candidates, key=lambda x: x.get("first_year", 0) or 0):
            fy, ly = c["first_year"], c["last_year"]
            compat = _check_name_compat(person["given_names"], c["_given"])
            tag = "✓" if compat != "incompatible" else "✗"
            print(f"    {tag} {c['name']} ({fy}-{ly}) [{compat}]")


# =============================================================================
# OUTPUT
# =============================================================================

def write_outputs(careers, positive_pairs, negative_pairs, stats):
    """Write all output files."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 1. Known careers JSON
    with open(KNOWN_CAREERS_FILE, "w") as f:
        json.dump(careers, f, indent=2)
    print(f"  Wrote {len(careers)} careers to {KNOWN_CAREERS_FILE}")

    # 2. Ground truth pairs CSV
    with open(GT_PAIRS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "official_a", "official_b", "label", "source", "career_id", "pair_type",
        ])
        writer.writeheader()
        for pair in positive_pairs + negative_pairs:
            writer.writerow({
                "official_a": pair["official_a"],
                "official_b": pair["official_b"],
                "label": pair["label"],
                "source": pair["source"],
                "career_id": pair.get("career_id", ""),
                "pair_type": pair.get("pair_type", ""),
            })
    print(f"  Wrote {len(positive_pairs)} positive + {len(negative_pairs)} negative pairs to {GT_PAIRS_FILE}")

    # 3. Review sample — focus on multi-official careers
    import random
    random.seed(42)
    review_careers = [c for c in careers if len(c["officials"]) >= 2]
    sample = random.sample(review_careers, min(100, len(review_careers)))
    with open(REVIEW_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["career_id", "source", "person_name", "colony",
                         "num_officials", "officials", "different_persons"])
        for c in sample:
            offs = [f"{m.get('name', m.get('official_id','?'))} ({m.get('years', '?')})"
                   for m in c["officials"]]
            diffs = [f"{d.get('name', d.get('official_id','?'))} ({d.get('years', '?')})"
                     for d in c.get("different_persons", [])]
            writer.writerow([
                c["career_id"], c["source"], c["person_name"],
                c.get("colony", ""),
                len(c["officials"]),
                " | ".join(offs),
                " | ".join(diffs) if diffs else "",
            ])
    print(f"  Wrote {len(sample)} multi-official careers to {REVIEW_FILE} for human review")

    # 4. Stats
    with open(STATS_FILE, "w") as f:
        f.write("Ground Truth Construction Statistics\n")
        f.write("=" * 50 + "\n\n")

        f.write("GEMINI CAREERS (within-colony focus):\n")
        f.write(f"  Total: {stats['gemini_total']}\n")
        f.write(f"  Matched to ≥1 official: {stats['gemini_matched']}\n")
        f.write(f"  Multi-official (yield positive pairs): {stats['gemini_multi_official']}\n")
        f.write(f"  With hard negatives (same surname, diff person): {stats['gemini_with_negatives']}\n\n")

        f.write("WIKIDATA CAREERS:\n")
        f.write(f"  Total (in date range): {stats['wd_total']}\n")
        f.write(f"  Matched to ≥1 official: {stats['wd_matched']}\n")
        f.write(f"  Multi-official (yield positive pairs): {stats['wd_multi_official']}\n")
        f.write(f"  With hard negatives: {stats['wd_with_negatives']}\n\n")

        f.write("CURATED CROSS-COLONY CAREERS:\n")
        f.write(f"  Careers: {stats.get('curated_careers', 0)}\n")
        f.write(f"  Pairs: {stats.get('curated_pairs', 0)}\n\n")

        f.write("TRAINING DATA:\n")
        f.write(f"  Positive pairs (same person): {stats['total_positive_pairs']}\n")
        f.write(f"  Negative pairs (different person, same surname+colony): {stats['total_negative_pairs']}\n")
        f.write(f"  Single-match anchors: {stats['total_anchors']}\n\n")
        f.write(f"Conflicts (official claimed by 2+ people): {len(stats['conflicts'])}\n")
        for conflict in stats["conflicts"][:20]:
            f.write(f"  {conflict['official_id']}: {conflict['claimants']}\n")

    print(f"  Wrote stats to {STATS_FILE}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Build ML ground truth from WD + Gemini careers (within-colony focus)")
    parser.add_argument("--stats", action="store_true",
                        help="Just report existing ground truth stats")
    parser.add_argument("--diagnose", action="store_true",
                        help="Trace matching for multi-stint Gemini careers")
    parser.add_argument("--diagnose-n", type=int, default=30,
                        help="Number of careers to diagnose")
    args = parser.parse_args()

    if args.stats:
        if KNOWN_CAREERS_FILE.exists():
            with open(KNOWN_CAREERS_FILE) as f:
                careers = json.load(f)
            multi = [c for c in careers if len(c["officials"]) >= 2]
            print(f"Known careers: {len(careers)}")
            print(f"  With 2+ officials (yield pairs): {len(multi)}")
            print(f"  Single-match anchors: {len(careers) - len(multi)}")
            if STATS_FILE.exists():
                print(f"\n{STATS_FILE.read_text()}")
        else:
            print("No ground truth built yet. Run without --stats first.")
        return

    # Verify Neo4j password
    if not NEO4J_PASSWORD:
        print("ERROR: Set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    print("Building ground truth dataset (within-colony focus)...")

    # Step 1: Load colony mapping
    print("\n1. Loading colony QID mapping...")
    qid_to_colony = build_colony_qid_map()
    print(f"  {len(qid_to_colony)} QID → colony mappings")

    # Step 2: Load external career data
    print("\n2. Loading external career data...")
    wd_people = load_wd_people(qid_to_colony)
    print(f"  Wikidata: {len(wd_people)} people with in-range mapped positions")
    gemini_people = load_gemini_careers(qid_to_colony)
    print(f"  Gemini: {len(gemini_people)} careers")

    # Step 3: Load COL_Officials
    print("\n3. Loading COL_Officials from Neo4j...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        by_surname, by_surname_colony = load_officials(driver)
    finally:
        driver.close()

    # Step 4: Diagnose or match
    if args.diagnose:
        diagnose_within_colony(gemini_people, by_surname_colony, args.diagnose_n)
        return

    print("\n4. Matching careers to COL_Officials (within-colony focus)...")
    careers, pos_pairs, neg_pairs, stats = match_within_colony(
        gemini_people, wd_people, by_surname_colony, by_surname)

    print(f"\n  GEMINI: {stats['gemini_matched']}/{stats['gemini_total']} matched, "
          f"{stats['gemini_multi_official']} multi-official")
    print(f"  WIKIDATA: {stats['wd_matched']}/{stats['wd_total']} matched, "
          f"{stats['wd_multi_official']} multi-official")
    print(f"  CURATED: {stats.get('curated_careers', 0)} careers, "
          f"{stats.get('curated_pairs', 0)} cross-colony pairs")
    print(f"  Positive pairs: {len(pos_pairs)}")
    print(f"  Negative pairs: {len(neg_pairs)}")
    print(f"  Anchors: {stats['total_anchors']}")
    print(f"  Conflicts: {len(stats['conflicts'])}")

    # Step 5: Write outputs
    print("\n5. Writing outputs...")
    write_outputs(careers, pos_pairs, neg_pairs, stats)

    print("\nDone! Next steps:")
    print(f"  1. Review {REVIEW_FILE} — spot-check multi-official careers")
    print(f"  2. Run --diagnose to trace matching for multi-stint Gemini careers")
    print(f"  3. Key question: are multi-official matches true splits or false matches?")


if __name__ == "__main__":
    main()

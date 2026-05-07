#!/usr/bin/env python3
"""
London Gazette LOD: Harvest, Parse, and Match
===============================================

Queries the London Gazette's SPARQL endpoint for entries mentioning each
colony/place, extracts person data, and matches against COL_Official and
IOL_Person nodes in Neo4j.

Per colony:
  1. SPARQL query for entries mentioning that colony in entryText or title
  2. Aggregate by entry URI (dedup multi-honour rows)
  3. Match to COL_Official / IOL_Person by surname + initials + year proximity
  4. Cache results to gazette_data/{colony_slug}.json

Usage:
    python col_gazette_harvest.py                         # all COL colonies
    python col_gazette_harvest.py --colony "Gold Coast"   # single colony
    python col_gazette_harvest.py --indian                # IOL places only
    python col_gazette_harvest.py --all                   # COL + IOL
    python col_gazette_harvest.py --write                 # write to Neo4j
    python col_gazette_harvest.py --stats                 # report cached data
    python col_gazette_harvest.py --dry-run               # harvest + match, no write

Requires:
    pip install neo4j
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

from col_gazette_config import (
    GAZETTE_COL_TERMS, GAZETTE_IOL_TERMS,
    sparql_query, build_entry_query,
    aggregate_bindings, add_honours_to_entries, fetch_surname_forenames,
    extract_role_from_entry, colony_slug,
)
from col_normalize_names import (
    initials_compatible, clean_given_names, extract_initials,
)
from col_link_officials import classify_domain, is_bare_member_position, COMMON_SURNAMES
from col_link_wikidata import normalize_surname


# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
DATA_DIR = REPO_DIR / "gazette_data"
BATCH_SIZE = 500

# Matching thresholds
MATCH_THRESHOLD = 0.70       # minimum confidence for auto-match
HIGH_CONFIDENCE = 0.90       # auto-accept threshold
MAX_YEAR_GAP = 10            # max years between gazette entry and official stint


def _load_dotenv():
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
# NEO4J DATA LOADING — Surname indexes
# =============================================================================

def load_col_surname_index(driver):
    """Build {normalized_surname: [official_dict]} index from COL_Official nodes."""
    print("Loading COL_Official surname index...")
    with driver.session() as s:
        result = s.run("""
            MATCH (o:COL_Official)
            WHERE o.name IS NOT NULL
            RETURN o.id AS id, o.name AS name, o.colony AS colony,
                   o.first_year AS first_year, o.last_year AS last_year,
                   o.position AS position, o.department AS department,
                   o.editions AS editions
        """)
        officials = [dict(r) for r in result]

    index = defaultdict(list)
    for o in officials:
        name = o.get("name", "")
        if ", " in name:
            surname = name.split(", ", 1)[0]
        else:
            surname = name
        norm = normalize_surname(surname)
        if norm:
            o["_surname_raw"] = surname
            o["_given"] = name.split(", ", 1)[1] if ", " in name else ""
            index[norm].append(o)

    print(f"  {len(officials)} officials, {len(index)} unique surnames")
    return index


def load_iol_surname_index(driver):
    """Build {normalized_surname: [person_dict]} index from IOL_Person nodes.

    Enriches with SERVED_IN places and APPOINTED roles for matching.
    Returns empty index if IOL_Person label doesn't exist.
    """
    print("Loading IOL_Person surname index...")
    with driver.session() as s:
        # Check if IOL_Person label exists
        check = s.run("CALL db.labels() YIELD label WHERE label = 'IOL_Person' RETURN label")
        if not check.peek():
            print("  No IOL_Person nodes found — skipping")
            return defaultdict(list)

        # Get persons with their places and appointment years
        result = s.run("""
            MATCH (p:IOL_Person)
            OPTIONAL MATCH (p)-[:SERVED_IN]->(pl:IOL_Place)
            OPTIONAL MATCH (p)-[:APPEARS_IN]->(v:IOL_Volume)
            RETURN p.id AS id, p.name AS name,
                   p.birth_date AS birth_date,
                   collect(DISTINCT pl.name) AS places,
                   min(v.year) AS first_year,
                   max(v.year) AS last_year
        """)
        persons = [dict(r) for r in result]

    index = defaultdict(list)
    for p in persons:
        name = p.get("name", "")
        # IOL names are often UPPERCASE — handle both formats
        if ", " in name:
            surname = name.split(", ", 1)[0]
            given = name.split(", ", 1)[1]
        else:
            # All uppercase single-word or space-separated
            parts = name.split()
            surname = parts[0] if parts else name
            given = " ".join(parts[1:]) if len(parts) > 1 else ""

        norm = normalize_surname(surname)
        if norm:
            p["_surname_raw"] = surname
            # Title-case the given names for matching
            p["_given"] = given.title() if given.isupper() else given
            p["_places"] = p.get("places", [])
            index[norm].append(p)

    print(f"  {len(persons)} IOL persons, {len(index)} unique surnames")
    # Count those with places and years
    with_places = sum(1 for p in persons if p.get("places"))
    with_years = sum(1 for p in persons if p.get("first_year"))
    print(f"  With places: {with_places}, with years: {with_years}")
    return index


# =============================================================================
# MATCHING LOGIC
# =============================================================================

def compute_gazette_match_score(
    gaz_entry: dict,
    candidate: dict,
    colony: str,
    namespace: str,
) -> float:
    """Score a gazette entry against a COL/IOL candidate.

    Returns 0.0-1.0 confidence score.
    """
    # 1. Name compatibility
    gaz_forenames = clean_given_names(gaz_entry.get("forenames", ""))

    # Clean gazette forenames of role-text contamination
    # e.g. "John Nominated Official Member" → "John"
    _ROLE_WORDS = {"nominated", "official", "member", "unofficial", "legislative",
                   "executive", "council", "puisne", "judge", "chief", "justice",
                   "governor", "colonial", "secretary", "acting", "temporary"}
    if gaz_forenames:
        clean_tokens = []
        for tok in gaz_forenames.split():
            if tok.strip(".,").lower() in _ROLE_WORDS:
                break  # stop at first role word, rest is contamination
            clean_tokens.append(tok)
        gaz_forenames = " ".join(clean_tokens)

    cand_given = clean_given_names(candidate.get("_given", ""))

    if not initials_compatible(gaz_forenames, cand_given):
        return 0.0

    # Name specificity bonus
    gaz_initials = extract_initials(gaz_forenames)
    cand_initials = extract_initials(cand_given)
    gaz_tokens = [t.strip(".,") for t in gaz_forenames.split() if t.strip(".,")]
    cand_tokens = [t.strip(".,") for t in cand_given.split() if t.strip(".,")]

    # Both have initials and they match at 2+ positions = stronger
    matched_initials = 0
    for i in range(min(len(gaz_initials), len(cand_initials))):
        if gaz_initials[i] == cand_initials[i]:
            matched_initials += 1

    # Stricter check: if one side has more initials than the other's tokens,
    # the extra initials are unverified. "J. R." vs "Joseph" — R is unverified.
    # If the longer side has 2+ initials and the shorter has only 1 full name,
    # this is suspect: "Joseph" is unlikely to be "J. R. Smith".
    # But "F. G." vs "Frederic Gordon" is fine (both have 2 tokens).
    if len(gaz_tokens) >= 2 and len(cand_tokens) == 1 and len(cand_tokens[0]) > 2:
        # Gazette has 2+ initials, candidate has one full name only
        # e.g. "J. R." vs "Joseph" — reject unless full name matches first initial
        if gaz_initials[0] == cand_initials[0]:
            matched_initials = 1  # downgrade, don't count extra gazette initials
        else:
            return 0.0
    elif len(cand_tokens) >= 2 and len(gaz_tokens) == 1 and len(gaz_tokens[0]) > 2:
        # Candidate has 2+ initials, gazette has one full name
        if cand_initials[0] == gaz_initials[0]:
            matched_initials = 1
        else:
            return 0.0

    # Check if gazette and candidate are in the same colony
    cand_colony = candidate.get("colony", "")
    cand_places = candidate.get("_places", [])
    same_colony = False
    if cand_colony and cand_colony.lower() == colony.lower():
        same_colony = True
    elif cand_places and any(p and p.lower() == colony.lower() for p in cand_places):
        same_colony = True

    # Cross-colony matches need stronger name evidence:
    # "Anderson, J." in Brunei matching "Anderson, J. H" in Gold Coast is noise.
    # Require 2+ initials for cross-colony, or full name match.
    surname_norm = normalize_surname(gaz_entry.get("surname", ""))
    is_common = surname_norm in COMMON_SURNAMES

    if not same_colony:
        if is_common and matched_initials < 3:
            # Common surnames need 3+ matching initials for cross-colony
            # "Smith, H. C." in Bermuda matching "Smith, H. C. C" in Tanganyika — reject
            return 0.0
        elif matched_initials < 2:
            # Uncommon surnames: require 2+ initials or full name match
            gaz_has_full = any(len(t) > 2 for t in gaz_tokens)
            cand_has_full = any(len(t) > 2 for t in cand_tokens)
            if not (gaz_has_full and cand_has_full):
                return 0.0

    if not gaz_initials and not cand_initials:
        name_score = 0.15  # bare surname only
    elif matched_initials >= 2:
        name_score = 0.50  # strong name match
    elif matched_initials == 1:
        name_score = 0.35  # single initial match
    elif not gaz_initials or not cand_initials:
        name_score = 0.20  # one side has no initials
    else:
        return 0.0  # initials incompatible (shouldn't reach here)

    # 2. Year proximity
    # Gazette index starts at 1900 — officials whose careers ended before
    # 1900 can only appear in early 1900s entries (honours, references).
    # Don't penalize these late-coverage matches.
    GAZETTE_START_YEAR = 1900
    gaz_year = gaz_entry.get("year")
    cand_first = candidate.get("first_year")
    cand_last = candidate.get("last_year")

    year_score = 0.0
    if gaz_year and cand_first and cand_last:
        if cand_first <= gaz_year <= cand_last:
            # Gazette year falls within official's tenure — best case
            year_score = 0.35
        else:
            gap = min(abs(gaz_year - cand_first), abs(gaz_year - cand_last))

            # If career ended before gazette started, the gap is artificial
            # e.g., career 1885-1898, gazette entry 1902 → gap=4 but
            # this is the earliest the gazette could possibly show them
            if cand_last < GAZETTE_START_YEAR and gaz_year <= GAZETTE_START_YEAR + 5:
                # Early gazette entry for pre-1900 career — treat as near-overlap
                year_score = 0.25
            elif gap <= 3:
                year_score = 0.25
            elif gap <= MAX_YEAR_GAP:
                year_score = 0.15
            elif gap <= 15:
                # Wider gap but still plausible (honours awarded years later)
                year_score = 0.08
            else:
                year_score = 0.0
    elif gaz_year and cand_first:
        gap = abs(gaz_year - cand_first)
        if gap <= 5:
            year_score = 0.20
        elif gap <= MAX_YEAR_GAP:
            year_score = 0.10
    else:
        year_score = 0.05  # no temporal data

    # 3. Colony match (already filtered by colony, boost exact matches)
    if same_colony:
        colony_score = 0.15
    elif cand_colony:
        colony_score = 0.08
    elif cand_places and any(p and (colony.lower() in p.lower() or p.lower() in colony.lower()) for p in cand_places):
        colony_score = 0.10
    else:
        colony_score = 0.05

    # 4. Honours match
    gaz_honours = set(h.upper().replace(" ", "") for h in gaz_entry.get("honours", []))
    honour_score = 0.0
    if gaz_honours:
        # Check if gazette honours appear in the candidate's name or record
        cand_name = candidate.get("name", "")
        for hon in gaz_honours:
            hon_clean = hon.replace(".", "")
            if hon_clean in cand_name.upper().replace(".", "").replace(" ", ""):
                honour_score = 0.08
                break

    confidence = name_score + year_score + colony_score + honour_score
    return round(max(0.0, min(1.0, confidence)), 3)


def match_entries_to_officials(
    entries: dict[str, dict],
    col_index: dict,
    iol_index: dict,
    colony: str,
    namespace: str,
    forename_candidates: dict[str, list[str]] | None = None,
) -> list[dict]:
    """Match gazette entries to COL/IOL candidates.

    For entries missing forenames, tries each candidate forename from
    sibling surname entries and keeps the best-scoring combination.

    Returns list of match dicts with entry, candidate, confidence.
    """
    forename_candidates = forename_candidates or {}
    matches = []

    for uri, entry in entries.items():
        surname = entry.get("surname", "")
        if not surname:
            continue

        norm_surname = normalize_surname(surname)
        if not norm_surname:
            continue

        # Build list of forename variants to try
        # If the entry has forenames, use them; otherwise try each candidate
        entry_forenames = entry.get("forenames", "")
        if entry_forenames:
            forenames_to_try = [entry_forenames]
            enriched = False
        elif uri in forename_candidates:
            forenames_to_try = forename_candidates[uri]
            enriched = True
        else:
            forenames_to_try = [""]
            enriched = False

        # Find best match across all forename variants
        best_match = None
        best_score = 0.0
        best_forenames = entry_forenames

        for try_forenames in forenames_to_try:
            # Temporarily set forenames for scoring
            entry["forenames"] = try_forenames

            for candidate in col_index.get(norm_surname, []):
                score = compute_gazette_match_score(entry, candidate, colony, "COL")
                if score > best_score and score >= MATCH_THRESHOLD:
                    best_score = score
                    best_match = {"candidate": candidate, "score": score, "namespace": "COL"}
                    best_forenames = try_forenames

            for candidate in iol_index.get(norm_surname, []):
                score = compute_gazette_match_score(entry, candidate, colony, "IOL")
                if score > best_score and score >= MATCH_THRESHOLD:
                    best_score = score
                    best_match = {"candidate": candidate, "score": score, "namespace": "IOL"}
                    best_forenames = try_forenames

        # Restore original forenames (or best enriched)
        entry["forenames"] = entry_forenames

        match_record = {
            "uri": uri,
            "year": entry.get("year"),
            "surname": surname,
            "forenames": entry_forenames,
            "role": extract_role_from_entry(entry),
            "honours": entry.get("honours", []),
            "colony": colony,
            "namespace": namespace,
        }

        if best_match:
            match_record["match_id"] = best_match["candidate"].get("id")
            match_record["match_name"] = best_match["candidate"].get("name")
            match_record["match_namespace"] = best_match["namespace"]
            match_record["confidence"] = best_match["score"]
            match_record["match_colony"] = best_match["candidate"].get("colony", "")
            match_record["match_years"] = (
                f"{best_match['candidate'].get('first_year', '?')}-"
                f"{best_match['candidate'].get('last_year', '?')}"
            )
            if enriched and best_forenames != entry_forenames:
                match_record["enriched_forenames"] = best_forenames
        else:
            match_record["match_id"] = None
            match_record["confidence"] = 0.0

        matches.append(match_record)

    return matches


# =============================================================================
# HARVEST PIPELINE
# =============================================================================

def harvest_colony(colony: str, search_terms: list[str], namespace: str,
                   col_index: dict, iol_index: dict) -> dict:
    """Harvest gazette entries for a single colony/place.

    Returns dict with entries, matches, and stats.
    """
    slug = colony_slug(colony)
    cache_file = DATA_DIR / f"{slug}.json"

    print(f"\n{'='*60}")
    print(f"Harvesting: {colony} ({namespace})")
    print(f"  Search terms: {search_terms}")

    # Build and execute SPARQL query (two-phase: entries first, then honours)
    query = build_entry_query(search_terms)
    try:
        result = sparql_query(query)
    except Exception as e:
        print(f"  ERROR: SPARQL query failed: {e}")
        return {"colony": colony, "namespace": namespace, "entries": 0, "matches": 0, "error": str(e)}

    bindings = result.get("results", {}).get("bindings", [])
    print(f"  Raw bindings: {len(bindings)}")

    # Aggregate by entry URI
    entries = aggregate_bindings(bindings)
    print(f"  Unique entries: {len(entries)}")

    # Fetch honours separately (avoids cross-product)
    if entries:
        add_honours_to_entries(entries)

    if not entries:
        return {"colony": colony, "namespace": namespace, "entries": 0, "matches": 0}

    # First pass: match without enrichment
    matches = match_entries_to_officials(
        entries, col_index, iol_index, colony, namespace
    )

    # Second pass: for unmatched bare-surname entries, try forename enrichment
    # Only for surnames with ≤5 COL/IOL candidates (skip common names)
    unmatched_bare = [
        m for m in matches
        if not m.get("match_id") and not m.get("forenames")
    ]
    if unmatched_bare:
        # Filter to rare surnames only
        rare_uris = {}
        for m in unmatched_bare:
            norm = normalize_surname(m["surname"])
            col_count = len(col_index.get(norm, []))
            iol_count = len(iol_index.get(norm, []))
            if col_count + iol_count <= 5:
                rare_uris[m["uri"]] = True

        if rare_uris:
            # Build subset of entries needing enrichment
            rare_entries = {u: entries[u] for u in rare_uris if u in entries}
            forename_candidates = fetch_surname_forenames(rare_entries)
            if forename_candidates:
                print(f"  Forename enrichment: {len(forename_candidates)} rare surnames")

                # Re-match only the enriched entries
                enriched_matches = match_entries_to_officials(
                    rare_entries, col_index, iol_index, colony, namespace,
                    forename_candidates
                )

                # Replace unmatched entries with enriched results
                enriched_by_uri = {m["uri"]: m for m in enriched_matches if m.get("match_id")}
                if enriched_by_uri:
                    matches = [
                        enriched_by_uri.get(m["uri"], m) if not m.get("match_id") else m
                        for m in matches
                    ]
                    print(f"  Enrichment recovered: {len(enriched_by_uri)} matches")
    matched = [m for m in matches if m.get("match_id")]
    print(f"  Matched: {len(matched)}/{len(matches)} entries")

    # High-confidence matches
    high_conf = [m for m in matched if m["confidence"] >= HIGH_CONFIDENCE]
    if high_conf:
        print(f"  High confidence (≥{HIGH_CONFIDENCE}): {len(high_conf)}")

    # Save to cache
    DATA_DIR.mkdir(exist_ok=True)
    cache_data = {
        "colony": colony,
        "namespace": namespace,
        "search_terms": search_terms,
        "entry_count": len(entries),
        "match_count": len(matched),
        "matches": matches,
    }
    with open(cache_file, "w") as f:
        json.dump(cache_data, f, indent=2, default=str)
    print(f"  Cached: {cache_file}")

    return {
        "colony": colony,
        "namespace": namespace,
        "entries": len(entries),
        "matches": len(matched),
    }


# =============================================================================
# NEO4J WRITE
# =============================================================================

def write_to_neo4j(driver):
    """Write harvested gazette data to Neo4j.

    Creates GAZ_Entry nodes and GAZETTE_MATCH relationships.
    """
    print("\n" + "="*60)
    print("Writing gazette data to Neo4j...")

    # Create indexes first
    with driver.session() as s:
        s.run("CREATE INDEX gaz_entry_uri IF NOT EXISTS FOR (g:GAZ_Entry) ON (g.uri)")
        s.run("CREATE INDEX gaz_entry_surname IF NOT EXISTS FOR (g:GAZ_Entry) ON (g.surname)")
    print("  Created indexes")

    # Load all cached match files
    total_entries = 0
    total_matches = 0

    for cache_file in sorted(DATA_DIR.glob("*.json")):
        if cache_file.name == "harvest_stats.json":
            continue

        with open(cache_file) as f:
            data = json.load(f)

        colony = data.get("colony", "")
        namespace = data.get("namespace", "COL")
        matches = data.get("matches", [])

        if not matches:
            continue

        # Create GAZ_Entry nodes in batches
        entries_batch = []
        match_batch = []

        for m in matches:
            entries_batch.append({
                "uri": m["uri"],
                "surname": m.get("surname", ""),
                "forenames": m.get("forenames", ""),
                "year": m.get("year"),
                "colony": m.get("colony", ""),
                "role_raw": m.get("role", ""),
                "honours": ", ".join(m.get("honours", [])),
                "namespace": namespace,
            })

            if m.get("match_id") and m.get("confidence", 0) >= MATCH_THRESHOLD:
                match_batch.append({
                    "uri": m["uri"],
                    "match_id": m["match_id"],
                    "match_namespace": m.get("match_namespace", "COL"),
                    "confidence": m["confidence"],
                })

        # Write entries
        with driver.session() as s:
            for i in range(0, len(entries_batch), BATCH_SIZE):
                batch = entries_batch[i:i+BATCH_SIZE]
                s.run("""
                    UNWIND $entries AS e
                    MERGE (g:GAZ_Entry {uri: e.uri})
                    SET g.surname = e.surname,
                        g.forenames = e.forenames,
                        g.year = e.year,
                        g.colony = e.colony,
                        g.role_raw = e.role_raw,
                        g.honours = e.honours,
                        g.namespace = e.namespace
                """, entries=batch)
            total_entries += len(entries_batch)

            # Write COL matches
            col_matches = [m for m in match_batch if m["match_namespace"] == "COL"]
            if col_matches:
                for i in range(0, len(col_matches), BATCH_SIZE):
                    batch = col_matches[i:i+BATCH_SIZE]
                    s.run("""
                        UNWIND $matches AS m
                        MATCH (o:COL_Official {id: m.match_id})
                        MATCH (g:GAZ_Entry {uri: m.uri})
                        MERGE (o)-[r:GAZETTE_MATCH]->(g)
                        SET r.confidence = m.confidence
                    """, matches=batch)
                total_matches += len(col_matches)

            # Write IOL matches
            iol_matches = [m for m in match_batch if m["match_namespace"] == "IOL"]
            if iol_matches:
                for i in range(0, len(iol_matches), BATCH_SIZE):
                    batch = iol_matches[i:i+BATCH_SIZE]
                    s.run("""
                        UNWIND $matches AS m
                        MATCH (p:IOL_Person {id: m.match_id})
                        MATCH (g:GAZ_Entry {uri: m.uri})
                        MERGE (p)-[r:GAZETTE_MATCH]->(g)
                        SET r.confidence = m.confidence
                    """, matches=batch)
                total_matches += len(iol_matches)

    print(f"\n  Total GAZ_Entry nodes created/updated: {total_entries}")
    print(f"  Total GAZETTE_MATCH edges created: {total_matches}")


# =============================================================================
# STATS
# =============================================================================

def report_stats():
    """Report on cached gazette harvest data."""
    if not DATA_DIR.exists():
        print("No gazette_data directory found. Run harvest first.")
        return

    total_entries = 0
    total_matches = 0
    total_high = 0
    colonies = []

    for cache_file in sorted(DATA_DIR.glob("*.json")):
        if cache_file.name == "harvest_stats.json":
            continue

        with open(cache_file) as f:
            data = json.load(f)

        colony = data.get("colony", cache_file.stem)
        ns = data.get("namespace", "?")
        entries = data.get("entry_count", 0)
        matched = data.get("match_count", 0)
        matches = data.get("matches", [])
        high = sum(1 for m in matches if m.get("confidence", 0) >= HIGH_CONFIDENCE)

        total_entries += entries
        total_matches += matched
        total_high += high
        colonies.append((colony, ns, entries, matched, high))

    print(f"\n{'='*70}")
    print(f"Gazette Harvest Statistics")
    print(f"{'='*70}")
    print(f"{'Colony':<35} {'NS':>4} {'Entries':>8} {'Matched':>8} {'High':>6}")
    print(f"{'-'*70}")

    for colony, ns, entries, matched, high in sorted(colonies):
        if entries > 0:
            print(f"{colony:<35} {ns:>4} {entries:>8} {matched:>8} {high:>6}")

    print(f"{'-'*70}")
    print(f"{'TOTAL':<35} {'':>4} {total_entries:>8} {total_matches:>8} {total_high:>6}")
    print(f"\nFiles: {len(colonies)}")


# =============================================================================
# REMATCH (offline re-scoring from cache)
# =============================================================================

def rematch_all(col_index, iol_index):
    """Re-run matching on all cached gazette data without SPARQL queries.

    Reconstructs entry dicts from cached match records and re-scores.
    Useful after adjusting scoring parameters.
    """
    if not DATA_DIR.exists():
        print("No gazette_data directory found.")
        return

    all_stats = []
    for cache_file in sorted(DATA_DIR.glob("*.json")):
        if cache_file.name in ("harvest_stats.json", "career_report.txt"):
            continue

        with open(cache_file) as f:
            data = json.load(f)

        colony = data.get("colony", "")
        namespace = data.get("namespace", "COL")
        old_matches = data.get("matches", [])

        if not old_matches:
            all_stats.append({"colony": colony, "namespace": namespace,
                              "entries": 0, "matches": 0})
            continue

        # Reconstruct entry dicts from cached match records
        entries = {}
        for m in old_matches:
            uri = m["uri"]
            entries[uri] = {
                "uri": uri,
                "year": m.get("year"),
                "surname": m.get("surname", ""),
                "forenames": m.get("forenames", ""),
                "titles": [],
                "honours": m.get("honours", []),
                "texts": [m.get("role", "")] if m.get("role") else [],
            }

        # Re-match
        matches = match_entries_to_officials(
            entries, col_index, iol_index, colony, namespace
        )

        matched = [m for m in matches if m.get("match_id")]
        high = [m for m in matched if m["confidence"] >= HIGH_CONFIDENCE]

        print(f"{colony}: {len(matched)}/{len(matches)} matched, {len(high)} high")

        # Overwrite cache
        cache_data = {
            "colony": colony,
            "namespace": namespace,
            "search_terms": data.get("search_terms", []),
            "entry_count": len(entries),
            "match_count": len(matched),
            "matches": matches,
        }
        with open(cache_file, "w") as f:
            json.dump(cache_data, f, indent=2, default=str)

        all_stats.append({
            "colony": colony, "namespace": namespace,
            "entries": len(entries), "matches": len(matched),
        })

    total_entries = sum(s["entries"] for s in all_stats)
    total_matches = sum(s["matches"] for s in all_stats)
    print(f"\nREMATCH COMPLETE: {total_matches}/{total_entries} matched")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Harvest London Gazette LOD data")
    parser.add_argument("--colony", help="Single colony to harvest")
    parser.add_argument("--indian", action="store_true", help="IOL places only")
    parser.add_argument("--all", action="store_true", help="COL + IOL")
    parser.add_argument("--write", action="store_true", help="Write to Neo4j")
    parser.add_argument("--stats", action="store_true", help="Report cached data")
    parser.add_argument("--dry-run", action="store_true", help="Harvest + match, no write")
    parser.add_argument("--rematch", action="store_true",
                        help="Re-run matching on cached data (no SPARQL queries)")
    args = parser.parse_args()

    if args.stats:
        report_stats()
        return

    # Connect to Neo4j
    if not NEO4J_PASSWORD:
        print("ERROR: NEO4J_PASSWORD not set")
        sys.exit(1)

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        driver.verify_connectivity()
    except Exception as e:
        print(f"ERROR: Cannot connect to Neo4j: {e}")
        sys.exit(1)

    if args.write:
        write_to_neo4j(driver)
        driver.close()
        return

    # Load surname indexes
    col_index = load_col_surname_index(driver)
    iol_index = load_iol_surname_index(driver)

    if args.rematch:
        # Re-run matching on cached data without SPARQL queries
        rematch_all(col_index, iol_index)
        driver.close()
        return

    # Determine which colonies to harvest
    colonies_to_harvest = []

    if args.colony:
        # Single colony — check both COL and IOL
        if args.colony in GAZETTE_COL_TERMS:
            colonies_to_harvest.append((args.colony, GAZETTE_COL_TERMS[args.colony], "COL"))
        elif args.colony in GAZETTE_IOL_TERMS:
            colonies_to_harvest.append((args.colony, GAZETTE_IOL_TERMS[args.colony], "IOL"))
        else:
            print(f"ERROR: Colony '{args.colony}' not found in COL or IOL terms")
            sys.exit(1)
    elif args.indian:
        for place, terms in sorted(GAZETTE_IOL_TERMS.items()):
            colonies_to_harvest.append((place, terms, "IOL"))
    elif args.all:
        for colony, terms in sorted(GAZETTE_COL_TERMS.items()):
            colonies_to_harvest.append((colony, terms, "COL"))
        for place, terms in sorted(GAZETTE_IOL_TERMS.items()):
            # Skip Ceylon if already in COL
            if place not in GAZETTE_COL_TERMS:
                colonies_to_harvest.append((place, terms, "IOL"))
    else:
        # Default: all COL colonies
        for colony, terms in sorted(GAZETTE_COL_TERMS.items()):
            colonies_to_harvest.append((colony, terms, "COL"))

    print(f"\nHarvesting {len(colonies_to_harvest)} colonies/places...")

    # Harvest each colony
    all_stats = []
    for colony, terms, namespace in colonies_to_harvest:
        stats = harvest_colony(colony, terms, namespace, col_index, iol_index)
        all_stats.append(stats)

    # Save summary stats
    DATA_DIR.mkdir(exist_ok=True)
    stats_file = DATA_DIR / "harvest_stats.json"
    with open(stats_file, "w") as f:
        json.dump({
            "total_colonies": len(all_stats),
            "total_entries": sum(s.get("entries", 0) for s in all_stats),
            "total_matches": sum(s.get("matches", 0) for s in all_stats),
            "results": all_stats,
        }, f, indent=2)

    # Summary
    total_entries = sum(s.get("entries", 0) for s in all_stats)
    total_matches = sum(s.get("matches", 0) for s in all_stats)
    errors = [s for s in all_stats if s.get("error")]

    print(f"\n{'='*60}")
    print(f"HARVEST COMPLETE")
    print(f"  Colonies processed: {len(all_stats)}")
    print(f"  Total entries: {total_entries}")
    print(f"  Total matches: {total_matches}")
    if errors:
        print(f"  Errors: {len(errors)}")
        for e in errors:
            print(f"    {e['colony']}: {e['error']}")

    if not args.dry_run:
        print(f"\nRun with --write to create GAZ_Entry nodes and GAZETTE_MATCH edges")

    driver.close()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
London Gazette LOD: Career Confirmation + COL↔IOL Bridging
=============================================================

Uses gazette matches from col_gazette_harvest.py to:
  A. Confirm existing POSSIBLE_MATCH edges (gazette_confirmed: true)
  B. Discover new COL↔COL career links not found by ML
  C. Bridge COL_Official ↔ IOL_Person via shared gazette presence
  D. Find appointment date gaps (gazette year before COL first_year)

Usage:
    python col_gazette_careers.py                 # analyze + report
    python col_gazette_careers.py --write         # write confirmations + bridges

Requires:
    pip install neo4j
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

from col_normalize_names import initials_compatible, extract_initials, clean_given_names
from col_link_wikidata import normalize_surname


# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
DATA_DIR = REPO_DIR / "gazette_data"
BATCH_SIZE = 500

CROSS_SERVICE_THRESHOLD = 0.70
DISCOVERY_THRESHOLD = 0.75


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
# LOAD GAZETTE MATCHES
# =============================================================================

def load_all_matches():
    """Load all gazette match data from cached JSON files.

    Returns list of match dicts with match_id populated.
    """
    all_matches = []
    if not DATA_DIR.exists():
        print("ERROR: No gazette_data directory. Run col_gazette_harvest.py first.")
        return []

    for cache_file in sorted(DATA_DIR.glob("*.json")):
        if cache_file.name == "harvest_stats.json":
            continue

        with open(cache_file) as f:
            data = json.load(f)

        for m in data.get("matches", []):
            if m.get("match_id"):
                all_matches.append(m)

    return all_matches


def build_person_gazette_map(matches):
    """Build {match_id: [match_dicts]} — all gazette entries matched to each person."""
    person_map = defaultdict(list)
    for m in matches:
        mid = m.get("match_id")
        if mid:
            person_map[mid].append(m)
    return person_map


def build_surname_gazette_map(matches):
    """Build {normalized_surname: [match_dicts]} — gazette entries by surname."""
    surname_map = defaultdict(list)
    for m in matches:
        surname = m.get("surname", "")
        if surname:
            norm = normalize_surname(surname)
            if norm:
                surname_map[norm].append(m)
    return surname_map


# =============================================================================
# A. CONFIRM EXISTING POSSIBLE_MATCH EDGES
# =============================================================================

def find_confirmations(person_map, driver):
    """Find POSSIBLE_MATCH edges that can be confirmed by gazette evidence.

    If gazette matches show person X in colony A AND colony B, and a
    POSSIBLE_MATCH edge exists between those officials → confirm it.
    """
    print("\n" + "="*60)
    print("A. POSSIBLE_MATCH Confirmations via Gazette")
    print("="*60)

    # Load existing POSSIBLE_MATCH edges
    with driver.session() as s:
        result = s.run("""
            MATCH (a:COL_Official)-[r:POSSIBLE_MATCH]->(b:COL_Official)
            RETURN a.id AS a_id, b.id AS b_id,
                   a.name AS a_name, b.name AS b_name,
                   a.colony AS a_col, b.colony AS b_col,
                   r.ml_probability AS prob,
                   r.gazette_confirmed AS already_confirmed
        """)
        edges = [dict(r) for r in result]

    print(f"  Total POSSIBLE_MATCH edges: {len(edges)}")

    # For each edge, check if both sides have gazette matches
    confirmations = []
    for edge in edges:
        if edge.get("already_confirmed"):
            continue

        a_id = edge["a_id"]
        b_id = edge["b_id"]

        a_gaz = person_map.get(a_id, [])
        b_gaz = person_map.get(b_id, [])

        if not a_gaz or not b_gaz:
            continue

        # Check if gazette entries show compatible person identity
        # Same surname + compatible initials across both matches
        for a_m in a_gaz:
            for b_m in b_gaz:
                a_surname = normalize_surname(a_m.get("surname", ""))
                b_surname = normalize_surname(b_m.get("surname", ""))

                if a_surname != b_surname:
                    continue

                a_fore = clean_given_names(a_m.get("forenames", ""))
                b_fore = clean_given_names(b_m.get("forenames", ""))

                if initials_compatible(a_fore, b_fore):
                    confirmations.append({
                        "a_id": a_id,
                        "b_id": b_id,
                        "a_name": edge["a_name"],
                        "b_name": edge["b_name"],
                        "a_colony": edge["a_col"],
                        "b_colony": edge["b_col"],
                        "prob": edge.get("prob"),
                        "a_gaz_year": a_m.get("year"),
                        "b_gaz_year": b_m.get("year"),
                        "a_gaz_colony": a_m.get("colony"),
                        "b_gaz_colony": b_m.get("colony"),
                    })
                    break  # one confirmation per edge is enough
            else:
                continue
            break

    print(f"  Confirmable edges: {len(confirmations)}")
    if confirmations:
        print(f"\n  Sample confirmations:")
        for c in confirmations[:10]:
            print(f"    {c['a_name']} ({c['a_colony']}) → {c['b_name']} ({c['b_colony']})")
            print(f"      Gazette: {c['a_gaz_colony']} ({c['a_gaz_year']}) + "
                  f"{c['b_gaz_colony']} ({c['b_gaz_year']})")

    return confirmations


# =============================================================================
# B. DISCOVER NEW COL↔COL CAREER LINKS
# =============================================================================

def find_discoveries(surname_map, person_map, driver):
    """Find gazette entries that suggest COL↔COL career links not yet in the graph.

    If gazette entries with same surname+initials appear in different colonies,
    but no POSSIBLE_MATCH edge exists → potential discovery.
    """
    print("\n" + "="*60)
    print("B. New COL↔COL Career Discoveries via Gazette")
    print("="*60)

    # Load existing edges for quick lookup
    with driver.session() as s:
        result = s.run("""
            MATCH (a:COL_Official)-[:POSSIBLE_MATCH]-(b:COL_Official)
            RETURN a.id AS a_id, b.id AS b_id
        """)
        existing_edges = set()
        for r in result:
            a, b = r["a_id"], r["b_id"]
            existing_edges.add((min(a, b), max(a, b)))

    print(f"  Existing POSSIBLE_MATCH edges: {len(existing_edges)}")

    # Find pairs of matched officials from different colonies
    discoveries = []
    seen_pairs = set()

    # Group matches by matched official ID
    for match_id, gaz_entries in person_map.items():
        if not match_id or not gaz_entries[0].get("match_namespace") == "COL":
            continue
        # This official has gazette evidence — check if other officials
        # share the same surname+initials in different colonies
        pass

    # Better approach: group by normalized surname, then find pairs
    for norm_surname, entries in surname_map.items():
        # Get unique matched COL officials
        col_matches = {}
        for m in entries:
            mid = m.get("match_id")
            if mid and m.get("match_namespace") == "COL":
                if mid not in col_matches:
                    col_matches[mid] = m

        if len(col_matches) < 2:
            continue

        # Check pairs of officials
        officials = list(col_matches.values())
        for i in range(len(officials)):
            for j in range(i+1, len(officials)):
                a = officials[i]
                b = officials[j]

                a_id = a["match_id"]
                b_id = b["match_id"]
                pair_key = (min(a_id, b_id), max(a_id, b_id))

                if pair_key in existing_edges or pair_key in seen_pairs:
                    continue

                # Check initials compatibility
                a_fore = clean_given_names(a.get("forenames", ""))
                b_fore = clean_given_names(b.get("forenames", ""))
                if not initials_compatible(a_fore, b_fore):
                    continue

                # Different colonies?
                a_col = a.get("match_colony", "")
                b_col = b.get("match_colony", "")
                if a_col == b_col:
                    continue

                # Both above discovery threshold?
                if a.get("confidence", 0) < DISCOVERY_THRESHOLD:
                    continue
                if b.get("confidence", 0) < DISCOVERY_THRESHOLD:
                    continue

                seen_pairs.add(pair_key)
                discoveries.append({
                    "a_id": a_id,
                    "b_id": b_id,
                    "a_name": a.get("match_name", ""),
                    "b_name": b.get("match_name", ""),
                    "a_colony": a_col,
                    "b_colony": b_col,
                    "surname": a.get("surname", ""),
                    "a_forenames": a.get("forenames", ""),
                    "b_forenames": b.get("forenames", ""),
                    "a_gaz_year": a.get("year"),
                    "b_gaz_year": b.get("year"),
                    "a_confidence": a.get("confidence"),
                    "b_confidence": b.get("confidence"),
                })

    print(f"  Potential discoveries: {len(discoveries)}")
    if discoveries:
        print(f"\n  Sample discoveries:")
        for d in discoveries[:10]:
            print(f"    {d['surname']}, {d['a_forenames']} / {d['b_forenames']}")
            print(f"      {d['a_name']} ({d['a_colony']}, gaz {d['a_gaz_year']})")
            print(f"      {d['b_name']} ({d['b_colony']}, gaz {d['b_gaz_year']})")

    return discoveries


# =============================================================================
# C. BRIDGE COL↔IOL
# =============================================================================

def find_cross_service_bridges(surname_map):
    """Find persons who appear in both COL and IOL gazette matches.

    If gazette entries with same surname+compatible initials match both
    a COL_Official and an IOL_Person → cross-service bridge.
    """
    print("\n" + "="*60)
    print("C. COL↔IOL Cross-Service Bridges")
    print("="*60)

    bridges = []

    for norm_surname, entries in surname_map.items():
        col_matches = [m for m in entries if m.get("match_namespace") == "COL" and m.get("match_id")]
        iol_matches = [m for m in entries if m.get("match_namespace") == "IOL" and m.get("match_id")]

        if not col_matches or not iol_matches:
            continue

        # Check initials compatibility between COL and IOL matches
        for col_m in col_matches:
            for iol_m in iol_matches:
                col_fore = clean_given_names(col_m.get("forenames", ""))
                iol_fore = clean_given_names(iol_m.get("forenames", ""))

                if not initials_compatible(col_fore, iol_fore):
                    continue

                # Both above threshold?
                if col_m.get("confidence", 0) < CROSS_SERVICE_THRESHOLD:
                    continue
                if iol_m.get("confidence", 0) < CROSS_SERVICE_THRESHOLD:
                    continue

                bridges.append({
                    "col_id": col_m["match_id"],
                    "iol_id": iol_m["match_id"],
                    "col_name": col_m.get("match_name", ""),
                    "iol_name": iol_m.get("match_name", ""),
                    "col_colony": col_m.get("match_colony", ""),
                    "iol_colony": iol_m.get("colony", ""),
                    "surname": col_m.get("surname", ""),
                    "col_forenames": col_m.get("forenames", ""),
                    "iol_forenames": iol_m.get("forenames", ""),
                    "col_gaz_year": col_m.get("year"),
                    "iol_gaz_year": iol_m.get("year"),
                    "col_confidence": col_m.get("confidence"),
                    "iol_confidence": iol_m.get("confidence"),
                    "col_gaz_uri": col_m.get("uri", ""),
                    "iol_gaz_uri": iol_m.get("uri", ""),
                })
                break  # one bridge per pair
            else:
                continue
            break

    # Deduplicate by (col_id, iol_id)
    seen = set()
    unique_bridges = []
    for b in bridges:
        key = (b["col_id"], b["iol_id"])
        if key not in seen:
            seen.add(key)
            unique_bridges.append(b)

    print(f"  Cross-service bridges found: {len(unique_bridges)}")
    if unique_bridges:
        print(f"\n  Bridges:")
        for b in unique_bridges[:15]:
            print(f"    {b['surname']}, {b['col_forenames']} / {b['iol_forenames']}")
            print(f"      COL: {b['col_name']} ({b['col_colony']}, gaz {b['col_gaz_year']})")
            print(f"      IOL: {b['iol_name']} ({b['iol_colony']}, gaz {b['iol_gaz_year']})")

    return unique_bridges


# =============================================================================
# D. APPOINTMENT DATE GAPS
# =============================================================================

def find_date_gaps(person_map):
    """Find officials whose gazette career starts before their COL record.

    This catches cases like Guggisberg where the gazette shows military
    appointments before the COL first_year.
    """
    print("\n" + "="*60)
    print("D. Appointment Date Gaps (Gazette before COL)")
    print("="*60)

    gaps = []

    for match_id, gaz_entries in person_map.items():
        # Only COL officials
        col_entries = [m for m in gaz_entries if m.get("match_namespace") == "COL"]
        if not col_entries:
            continue

        # Get the official's COL years from the match data
        match_years_str = col_entries[0].get("match_years", "")
        if "-" not in match_years_str:
            continue

        parts = match_years_str.split("-")
        try:
            col_first = int(parts[0])
        except (ValueError, IndexError):
            continue

        # Find earliest gazette year for this official
        gaz_years = [m.get("year") for m in gaz_entries if m.get("year")]
        if not gaz_years:
            continue

        earliest_gaz = min(gaz_years)
        if earliest_gaz < col_first:
            gaps.append({
                "match_id": match_id,
                "name": col_entries[0].get("match_name", ""),
                "colony": col_entries[0].get("match_colony", ""),
                "col_first_year": col_first,
                "gaz_earliest_year": earliest_gaz,
                "gap_years": col_first - earliest_gaz,
                "gaz_entries": len(gaz_entries),
            })

    # Sort by gap size
    gaps.sort(key=lambda g: g["gap_years"], reverse=True)

    print(f"  Officials with pre-COL gazette entries: {len(gaps)}")
    if gaps:
        print(f"\n  Top gaps:")
        for g in gaps[:20]:
            print(f"    {g['name']} ({g['colony']}): "
                  f"gazette {g['gaz_earliest_year']} vs COL {g['col_first_year']} "
                  f"(gap: {g['gap_years']} years, {g['gaz_entries']} entries)")

    return gaps


# =============================================================================
# WRITE TO NEO4J
# =============================================================================

def write_confirmations(driver, confirmations):
    """Set gazette_confirmed on POSSIBLE_MATCH edges."""
    if not confirmations:
        return

    print(f"\n  Writing {len(confirmations)} confirmations...")
    with driver.session() as s:
        for i in range(0, len(confirmations), BATCH_SIZE):
            batch = confirmations[i:i+BATCH_SIZE]
            params = [{"a_id": c["a_id"], "b_id": c["b_id"]} for c in batch]
            s.run("""
                UNWIND $edges AS e
                MATCH (a:COL_Official {id: e.a_id})-[r:POSSIBLE_MATCH]-(b:COL_Official {id: e.b_id})
                SET r.gazette_confirmed = true
            """, edges=params)


def write_discoveries(driver, discoveries):
    """Create new POSSIBLE_MATCH edges for gazette-discovered career links."""
    if not discoveries:
        return

    print(f"\n  Writing {len(discoveries)} discoveries...")
    with driver.session() as s:
        for i in range(0, len(discoveries), BATCH_SIZE):
            batch = discoveries[i:i+BATCH_SIZE]
            params = [{
                "a_id": d["a_id"],
                "b_id": d["b_id"],
                "a_conf": d["a_confidence"],
                "b_conf": d["b_confidence"],
            } for d in batch]
            s.run("""
                UNWIND $edges AS e
                MATCH (a:COL_Official {id: e.a_id})
                MATCH (b:COL_Official {id: e.b_id})
                MERGE (a)-[r:POSSIBLE_MATCH]->(b)
                SET r.method = 'gazette_discovery',
                    r.gazette_confirmed = true,
                    r.confidence = (e.a_conf + e.b_conf) / 2.0
            """, edges=params)


def write_bridges(driver, bridges):
    """Create CROSS_SERVICE relationships between COL and IOL."""
    if not bridges:
        return

    print(f"\n  Writing {len(bridges)} cross-service bridges...")
    with driver.session() as s:
        for i in range(0, len(bridges), BATCH_SIZE):
            batch = bridges[i:i+BATCH_SIZE]
            params = [{
                "col_id": b["col_id"],
                "iol_id": b["iol_id"],
                "col_gaz_uri": b["col_gaz_uri"],
                "iol_gaz_uri": b["iol_gaz_uri"],
                "confidence": min(b["col_confidence"], b["iol_confidence"]),
            } for b in batch]
            s.run("""
                UNWIND $bridges AS b
                MATCH (c:COL_Official {id: b.col_id})
                MATCH (i:IOL_Person {id: b.iol_id})
                MERGE (c)-[r:CROSS_SERVICE]->(i)
                SET r.gazette_evidence = true,
                    r.col_gaz_uri = b.col_gaz_uri,
                    r.iol_gaz_uri = b.iol_gaz_uri,
                    r.confidence = b.confidence
            """, bridges=params)


# =============================================================================
# REPORT
# =============================================================================

def write_report(confirmations, discoveries, bridges, gaps):
    """Write a text report of all findings."""
    DATA_DIR.mkdir(exist_ok=True)
    report_path = DATA_DIR / "career_report.txt"

    with open(report_path, "w") as f:
        f.write("London Gazette Career Analysis Report\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"A. POSSIBLE_MATCH Confirmations: {len(confirmations)}\n")
        f.write("-" * 40 + "\n")
        for c in confirmations:
            f.write(f"  {c['a_name']} ({c['a_colony']}) → {c['b_name']} ({c['b_colony']})\n")
            f.write(f"    Gazette: {c['a_gaz_colony']} ({c['a_gaz_year']}) + "
                    f"{c['b_gaz_colony']} ({c['b_gaz_year']})\n")

        f.write(f"\nB. New COL↔COL Discoveries: {len(discoveries)}\n")
        f.write("-" * 40 + "\n")
        for d in discoveries:
            f.write(f"  {d['surname']}: {d['a_name']} ({d['a_colony']}) ↔ "
                    f"{d['b_name']} ({d['b_colony']})\n")
            f.write(f"    Gazette years: {d['a_gaz_year']} / {d['b_gaz_year']}\n")

        f.write(f"\nC. COL↔IOL Bridges: {len(bridges)}\n")
        f.write("-" * 40 + "\n")
        for b in bridges:
            f.write(f"  {b['surname']}: COL {b['col_name']} ({b['col_colony']}) ↔ "
                    f"IOL {b['iol_name']} ({b['iol_colony']})\n")

        f.write(f"\nD. Appointment Date Gaps: {len(gaps)}\n")
        f.write("-" * 40 + "\n")
        for g in gaps:
            f.write(f"  {g['name']} ({g['colony']}): gazette {g['gaz_earliest_year']} "
                    f"vs COL {g['col_first_year']} (gap: {g['gap_years']}y)\n")

    print(f"\n  Report saved: {report_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Gazette career analysis")
    parser.add_argument("--write", action="store_true", help="Write to Neo4j")
    args = parser.parse_args()

    # Load gazette matches
    all_matches = load_all_matches()
    if not all_matches:
        return

    print(f"Loaded {len(all_matches)} gazette matches")

    person_map = build_person_gazette_map(all_matches)
    surname_map = build_surname_gazette_map(all_matches)

    print(f"Unique matched persons: {len(person_map)}")
    print(f"Unique matched surnames: {len(surname_map)}")

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

    # Run analyses
    confirmations = find_confirmations(person_map, driver)
    discoveries = find_discoveries(surname_map, person_map, driver)
    bridges = find_cross_service_bridges(surname_map)
    gaps = find_date_gaps(person_map)

    # Write report
    write_report(confirmations, discoveries, bridges, gaps)

    # Write to Neo4j if requested
    if args.write:
        print("\n" + "="*60)
        print("WRITING TO NEO4J")
        print("="*60)
        write_confirmations(driver, confirmations)
        write_discoveries(driver, discoveries)
        write_bridges(driver, bridges)
        print("\nDone.")
    else:
        print("\nRun with --write to persist changes to Neo4j")

    driver.close()


if __name__ == "__main__":
    main()

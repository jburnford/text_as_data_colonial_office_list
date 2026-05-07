"""
Test Research Set: Check if 44 known cross-colony movers have POSSIBLE_MATCH edges.

Reads wd_cross_colony_research.json and queries the graph to find:
1. Which WD people have COL_Official stints in their known colonies?
2. Are those stints connected by POSSIBLE_MATCH edges?
3. What are the scores?

Usage:
    python col_test_research_set.py                    # check research set
    python col_test_research_set.py --test             # check hold-out test set
    python col_test_research_set.py --simulate         # simulate new scoring offline
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

from col_link_officials import (
    classify_domain, compute_domain_match, compute_name_specificity,
)
from col_link_cross_colony import (
    compute_seniority_progression, compute_seniority_direction,
    compute_regional_proximity, compute_honours_match,
    compute_rank_match, compute_cross_colony_uncertainty,
)


REPO_DIR = Path(__file__).parent


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


def _extract_surname(full_name: str) -> str:
    """Extract likely surname from a WD name like 'Arthur Hamilton-Gordon, 1st Baron Stanmore'."""
    # Remove titles/peerage
    name = re.sub(r',\s*\d+(st|nd|rd|th)\s+\w+\s+\w+', '', full_name)
    name = re.sub(r'\bSir\b', '', name)
    parts = name.strip().split()
    if not parts:
        return full_name
    return parts[-1]


def check_research_set(driver, data_file: str, simulate: bool = False):
    """Check each WD person against the graph."""
    with open(data_file) as f:
        people = json.load(f)

    print(f"\nChecking {len(people)} people from {Path(data_file).name}")
    print("=" * 80)

    stats = {
        "total": len(people),
        "found_officials": 0,
        "found_in_multiple_colonies": 0,
        "has_cross_colony_edge": 0,
        "missing_officials": 0,
        "missing_edges": 0,
    }

    with driver.session() as session:
        for person in people:
            name = person["name"]
            qid = person["qid"]
            wd_colonies = [c for c in person["colonies"] if c]

            if len(wd_colonies) < 2:
                continue

            print(f"\n--- {name} ({qid}) ---")
            print(f"  WD colonies: {', '.join(wd_colonies)}")
            for pos in person["positions"]:
                if pos["colony_name"]:
                    print(f"    {pos['colony_name']}: {pos['label']} "
                          f"({pos.get('start', '?')} - {pos.get('end', '?')})")

            # Find COL_Officials with matching surname
            surname = _extract_surname(name)
            result = session.run(
                "MATCH (o:COL_Official) "
                "WHERE o.name CONTAINS $surname "
                "RETURN o.id AS id, o.name AS name, o.colony AS colony, "
                "       o.first_year AS first_year, o.last_year AS last_year, "
                "       o.editions AS editions "
                "ORDER BY o.colony, o.first_year",
                surname=surname,
            )
            officials = [dict(r) for r in result]

            if not officials:
                print(f"  NO COL_Officials found matching surname '{surname}'")
                stats["missing_officials"] += 1
                continue

            # Group by colony
            by_colony = defaultdict(list)
            for off in officials:
                by_colony[off["colony"]].append(off)

            print(f"  Found {len(officials)} COL_Officials across "
                  f"{len(by_colony)} colonies:")
            for colony, offs in sorted(by_colony.items()):
                for off in offs:
                    eds = len(off["editions"]) if off["editions"] else 0
                    print(f"    {colony}: {off['name']} "
                          f"({off['first_year']}-{off['last_year']}, "
                          f"{eds} editions) [{off['id'][:20]}...]")

            if len(by_colony) >= 2:
                stats["found_in_multiple_colonies"] += 1
            stats["found_officials"] += 1

            # Check for cross-colony POSSIBLE_MATCH edges between these officials
            off_ids = [o["id"] for o in officials]
            if len(off_ids) < 2:
                continue

            result = session.run(
                "MATCH (a:COL_Official)-[r:POSSIBLE_MATCH]->(b:COL_Official) "
                "WHERE a.id IN $ids AND b.id IN $ids "
                "  AND a.colony <> b.colony "
                "RETURN a.name AS a_name, a.colony AS a_colony, "
                "       a.last_year AS a_year, "
                "       b.colony AS b_colony, b.first_year AS b_year, "
                "       r.uncertainty AS unc, r.method AS method, "
                "       r.domain_match AS domain, "
                "       r.seniority_direction AS seniority, "
                "       r.seniority_progression AS progression, "
                "       r.overlap_type AS overlap_type, "
                "       r.a_last_position AS a_pos, "
                "       r.b_first_position AS b_pos",
                ids=off_ids,
            )
            edges = [dict(r) for r in result]

            if edges:
                stats["has_cross_colony_edge"] += 1
                print(f"  POSSIBLE_MATCH edges ({len(edges)}):")
                for e in edges:
                    prog = f" prog={e.get('progression', 'n/a')}" if e.get('progression') else ""
                    print(f"    {e['unc']:.3f}  {e['a_colony']} ({e['a_year']}) → "
                          f"{e['b_colony']} ({e['b_year']})  "
                          f"domain={e.get('domain', '?')} sen={e.get('seniority', '?')}"
                          f"{prog} [{e.get('overlap_type', '?')}]")
                    if e.get('a_pos') or e.get('b_pos'):
                        print(f"          a_pos: {e.get('a_pos', '?')}")
                        print(f"          b_pos: {e.get('b_pos', '?')}")
            else:
                stats["missing_edges"] += 1
                print(f"  NO cross-colony POSSIBLE_MATCH edges found!")
                if len(by_colony) >= 2:
                    print(f"  ** MISSED LINK ** — officials in {len(by_colony)} colonies "
                          f"but no edges")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"  Total WD people checked: {stats['total']}")
    print(f"  Found COL_Officials: {stats['found_officials']}")
    print(f"  Found in 2+ colonies: {stats['found_in_multiple_colonies']}")
    print(f"  Have cross-colony edges: {stats['has_cross_colony_edge']}")
    print(f"  Missing officials: {stats['missing_officials']}")
    print(f"  Missing edges (officials exist but no link): {stats['missing_edges']}")

    recall = 0
    if stats["found_in_multiple_colonies"] > 0:
        recall = stats["has_cross_colony_edge"] / stats["found_in_multiple_colonies"]
    print(f"\n  Cross-colony recall: {stats['has_cross_colony_edge']}/{stats['found_in_multiple_colonies']} "
          f"= {recall:.1%}")


def main():
    parser = argparse.ArgumentParser(description="Test research set against graph")
    parser.add_argument("--test", action="store_true",
                        help="Use hold-out test set instead of research set")
    parser.add_argument("--simulate", action="store_true",
                        help="Simulate new scoring (not yet implemented)")
    args = parser.parse_args()

    if args.test:
        data_file = REPO_DIR / "wd_cross_colony_test.json"
    else:
        data_file = REPO_DIR / "wd_cross_colony_research.json"

    if not data_file.exists():
        print(f"ERROR: {data_file} not found")
        sys.exit(1)

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        driver.verify_connectivity()
        print(f"Connected to {NEO4J_URI}")
        check_research_set(driver, str(data_file), simulate=args.simulate)
    finally:
        driver.close()


if __name__ == "__main__":
    main()

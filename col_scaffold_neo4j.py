"""
Neo4j Stage 0: COL Temporal-Geographic Scaffolding
====================================================

Builds the temporal-geographic skeleton for the Colonial Office List
knowledge graph in a shared Neo4j instance. All node labels use the
COL_ prefix to coexist with IOL_ and AW_ data.

Nodes created:
  COL_Year          — one per year (1867-1966)
  COL_Territory     — one per canonical colony name
  COL_TerritoryYear — one per colony-file per year (the "slice")

Edges created:
  (COL_TerritoryYear)-[:IN_YEAR]->(COL_Year)
  (COL_TerritoryYear)-[:INSTANCE_OF]->(COL_Territory)
  (COL_TerritoryYear)-[:CONTINUES_AS]->(COL_TerritoryYear)

Usage:
    python col_scaffold_neo4j.py --dry-run     # preview without loading
    python col_scaffold_neo4j.py               # load scaffold
    python col_scaffold_neo4j.py --clear       # remove COL scaffold only
    python col_scaffold_neo4j.py --stats       # report current state

Requires:
    pip install neo4j
"""

import argparse
import os
import sys
from collections import defaultdict
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

from scaffold_neo4j import normalize_colony_name, EXPLICIT_ALIASES


# =============================================================================
# CONFIGURATION
# =============================================================================

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")

REPO_DIR = Path(__file__).parent
BATCH_SIZE = 500


# =============================================================================
# CORPUS SCANNING
# =============================================================================

def scan_corpus(repo_dir: Path) -> dict[int, list[tuple[str, str, str]]]:
    """Scan year-directories and return {year: [(filename, stem, canonical_name), ...]}."""
    corpus = {}

    for entry in sorted(repo_dir.iterdir()):
        if not entry.is_dir() or not entry.name.endswith("_manual_parsed"):
            continue

        year_str = entry.name.replace("_manual_parsed", "")
        try:
            year = int(year_str)
        except ValueError:
            continue

        files = []
        for txt_file in sorted(entry.glob("*.txt")):
            stem = txt_file.stem
            canonical = normalize_colony_name(stem)
            files.append((txt_file.name, stem, canonical))

        # Also check .md files
        for md_file in sorted(entry.glob("*.md")):
            stem = md_file.stem
            canonical = normalize_colony_name(stem)
            files.append((md_file.name, stem, canonical))

        corpus[year] = files

    return corpus


def build_inventory(corpus: dict) -> dict:
    """Build territory inventory from corpus scan."""
    territory_years = defaultdict(list)
    all_years = sorted(corpus.keys())

    for year, files in sorted(corpus.items()):
        for filename, stem, canonical in files:
            territory_years[canonical].append(year)

    return {
        "years": all_years,
        "territories": dict(sorted(territory_years.items())),
        "total_year_dirs": len(all_years),
        "total_territories": len(territory_years),
        "total_territory_years": sum(len(years) for years in territory_years.values()),
    }


# =============================================================================
# NEO4J LOADING
# =============================================================================

SCHEMA_STATEMENTS = [
    "CREATE CONSTRAINT col_year_value IF NOT EXISTS FOR (y:COL_Year) REQUIRE y.value IS UNIQUE",
    "CREATE CONSTRAINT col_territory_name IF NOT EXISTS FOR (t:COL_Territory) REQUIRE t.name IS UNIQUE",
    "CREATE CONSTRAINT col_territory_year_id IF NOT EXISTS FOR (ty:COL_TerritoryYear) REQUIRE ty.id IS UNIQUE",
]


def create_schema(session):
    """Create constraints and indexes (idempotent)."""
    print("Creating constraints...")
    for stmt in SCHEMA_STATEMENTS:
        try:
            session.run(stmt)
        except Exception as e:
            if "already exists" not in str(e).lower() and "equivalent" not in str(e).lower():
                print(f"  WARNING: {e}")


def load_scaffolding(driver, corpus: dict, inventory: dict):
    """Load the temporal-geographic scaffolding into Neo4j."""

    with driver.session() as session:
        create_schema(session)

        # --- COL_Year nodes ---
        years = inventory["years"]
        print(f"Creating {len(years)} COL_Year nodes ({years[0]}-{years[-1]})...")
        session.run(
            "UNWIND $years AS y "
            "MERGE (n:COL_Year {value: y})",
            years=years
        )

        # --- COL_Territory nodes ---
        territories = list(inventory["territories"].keys())
        print(f"Creating {len(territories)} COL_Territory nodes...")
        session.run(
            "UNWIND $names AS name "
            "MERGE (t:COL_Territory {name: name})",
            names=territories
        )

        # --- COL_TerritoryYear slices + edges ---
        print("Creating COL_TerritoryYear slices and edges...")
        batch = []
        for year, files in sorted(corpus.items()):
            for filename, stem, canonical in files:
                ty_id = f"{canonical}_{year}"
                batch.append({
                    "id": ty_id,
                    "territory": canonical,
                    "year": year,
                    "source_file": f"{year}_manual_parsed/{filename}",
                })

        for i in range(0, len(batch), BATCH_SIZE):
            chunk = batch[i:i + BATCH_SIZE]
            session.run(
                "UNWIND $records AS r "
                "MERGE (ty:COL_TerritoryYear {id: r.id}) "
                "SET ty.territory = r.territory, "
                "    ty.year = r.year, "
                "    ty.source_file = r.source_file "
                "WITH ty, r "
                "MATCH (y:COL_Year {value: r.year}) "
                "MERGE (ty)-[:IN_YEAR]->(y) "
                "WITH ty, r "
                "MATCH (t:COL_Territory {name: r.territory}) "
                "MERGE (ty)-[:INSTANCE_OF]->(t)",
                records=chunk
            )

        print(f"Created {len(batch)} COL_TerritoryYear nodes")

        # --- CONTINUES_AS temporal chains ---
        print("Creating CONTINUES_AS temporal chains...")
        continues_count = 0
        for territory, appearances in inventory["territories"].items():
            sorted_years = sorted(appearances)
            if len(sorted_years) < 2:
                continue

            pairs = []
            for i in range(len(sorted_years) - 1):
                from_id = f"{territory}_{sorted_years[i]}"
                to_id = f"{territory}_{sorted_years[i + 1]}"
                pairs.append({"from_id": from_id, "to_id": to_id})

            if pairs:
                session.run(
                    "UNWIND $pairs AS p "
                    "MATCH (a:COL_TerritoryYear {id: p.from_id}) "
                    "MATCH (b:COL_TerritoryYear {id: p.to_id}) "
                    "MERGE (a)-[:CONTINUES_AS]->(b)",
                    pairs=pairs
                )
                continues_count += len(pairs)

        print(f"Created {continues_count} CONTINUES_AS edges")


# =============================================================================
# STATS / CLEAR (label-scoped — safe for shared database)
# =============================================================================

def print_stats(driver):
    """Report on COL scaffold state."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("COL SCAFFOLD STATISTICS")
        print("=" * 60)

        r = session.run("MATCH (y:COL_Year) RETURN count(y) AS c").single()
        print(f"  COL_Year nodes:          {r['c']}")

        r = session.run("MATCH (t:COL_Territory) RETURN count(t) AS c").single()
        print(f"  COL_Territory nodes:     {r['c']}")

        r = session.run("MATCH (ty:COL_TerritoryYear) RETURN count(ty) AS c").single()
        print(f"  COL_TerritoryYear nodes: {r['c']}")

        r = session.run(
            "MATCH (:COL_TerritoryYear)-[r:CONTINUES_AS]->(:COL_TerritoryYear) "
            "RETURN count(r) AS c"
        ).single()
        print(f"  CONTINUES_AS edges:      {r['c']}")

        r = session.run(
            "MATCH (:COL_TerritoryYear)-[r:IN_YEAR]->(:COL_Year) "
            "RETURN count(r) AS c"
        ).single()
        print(f"  IN_YEAR edges:           {r['c']}")

        r = session.run(
            "MATCH (:COL_TerritoryYear)-[r:INSTANCE_OF]->(:COL_Territory) "
            "RETURN count(r) AS c"
        ).single()
        print(f"  INSTANCE_OF edges:       {r['c']}")

        # Stage 1 loading progress (if any)
        r = session.run(
            "MATCH (ty:COL_TerritoryYear) WHERE ty.stage1_loaded = true "
            "RETURN count(ty) AS loaded"
        ).single()
        if r['loaded'] > 0:
            print(f"\n  Stage 1 loaded:          {r['loaded']} territory-years")


def clear_col_scaffold(driver):
    """Remove all COL scaffold nodes and edges. Does NOT touch IOL_ or AW_ data."""
    with driver.session() as session:
        print("Clearing COL scaffold data (COL_ labels only)...")

        # Delete in dependency order: slices first, then territories, then years
        r = session.run(
            "MATCH (ty:COL_TerritoryYear) DETACH DELETE ty RETURN count(ty) AS c"
        ).single()
        print(f"  Deleted {r['c']} COL_TerritoryYear nodes")

        r = session.run(
            "MATCH (t:COL_Territory) DETACH DELETE t RETURN count(t) AS c"
        ).single()
        print(f"  Deleted {r['c']} COL_Territory nodes")

        r = session.run(
            "MATCH (y:COL_Year) DETACH DELETE y RETURN count(y) AS c"
        ).single()
        print(f"  Deleted {r['c']} COL_Year nodes")

        print("COL scaffold cleared.")


# =============================================================================
# REPORTING
# =============================================================================

def print_report(inventory: dict):
    """Print corpus inventory report."""
    print("\n" + "=" * 60)
    print("CORPUS INVENTORY")
    print("=" * 60)
    print(f"Year directories: {inventory['total_year_dirs']}")
    print(f"Years span: {inventory['years'][0]}-{inventory['years'][-1]}")
    print(f"Unique territories: {inventory['total_territories']}")
    print(f"Total territory-years: {inventory['total_territory_years']}")

    print(f"\n--- Top 30 territories by coverage ---")
    sorted_territories = sorted(
        inventory["territories"].items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    for territory, appearances in sorted_territories[:30]:
        bar = "#" * (len(appearances) * 40 // inventory["total_year_dirs"])
        print(f"  {territory:<45} {len(appearances):>3} years  {bar}")

    if len(sorted_territories) > 30:
        print(f"  ... and {len(sorted_territories) - 30} more territories")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Build COL temporal-geographic scaffolding in Neo4j"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Print stats without loading into Neo4j")
    parser.add_argument("--clear", action="store_true",
                        help="Remove COL scaffold data only (safe for shared DB)")
    parser.add_argument("--stats", action="store_true",
                        help="Report on current COL scaffold state")
    args = parser.parse_args()

    print("=" * 60)
    print("NEO4J STAGE 0: COL TEMPORAL-GEOGRAPHIC SCAFFOLDING")
    print("=" * 60)

    # --- Stats only ---
    if args.stats:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        try:
            driver.verify_connectivity()
            print_stats(driver)
        finally:
            driver.close()
        return

    # --- Clear only ---
    if args.clear and not args.dry_run:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        try:
            driver.verify_connectivity()
            clear_col_scaffold(driver)
        finally:
            driver.close()
        return

    # Scan corpus
    print(f"\nScanning: {REPO_DIR}")
    corpus = scan_corpus(REPO_DIR)
    inventory = build_inventory(corpus)

    print_report(inventory)

    if args.dry_run:
        print("\n[DRY RUN] Skipping Neo4j loading.")
        return

    # Connect and load
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        load_scaffolding(driver, corpus, inventory)

        # Verify
        print_stats(driver)
        print("\nScaffolding complete!")

    finally:
        driver.close()


if __name__ == "__main__":
    main()

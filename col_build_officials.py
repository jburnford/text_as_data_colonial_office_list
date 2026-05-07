"""
COL Stage 2: Build COL_Official Career Stint Nodes
====================================================

Groups COL_PersonRecord observations into persistent career stints.
Each COL_Official represents one person's continuous service in one colony,
identified by appearing in 3+ COL editions.

A PersonRecord is an OBSERVATION (name appeared in a list in a year).
A COL_Official is an ENTITY (a person who served continuously in a colony).

Chaining logic:
  - For each (canonical_name, colony), collect all years with a PersonRecord
  - Chain consecutive years, allowing a skip of 1 edition (using per-colony
    COL_TerritoryYear coverage to determine what "consecutive" means)
  - Each chain of 3+ editions = one COL_Official node
  - Skip 1867 as orphan year (10-year gap to 1877)

ID pattern: {name}___{colony}___{first_year}

Usage:
    python col_build_officials.py                # full build
    python col_build_officials.py --dry-run      # preview, no writes
    python col_build_officials.py --stats        # report
    python col_build_officials.py --clear        # remove COL_Official nodes
    python col_build_officials.py --colony X     # single colony

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

from col_normalize_names import initials_compatible, clean_given_names, choose_best_name


# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
BATCH_SIZE = 2000
MIN_EDITIONS = 2
SKIP_BEFORE = 1877  # 1867 is an orphan year (10-year gap)


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
# BUILD COLONY EDITION INDEX
# =============================================================================

def build_colony_edition_index(session) -> dict[str, list[int]]:
    """Get the sorted list of edition years per colony from COL_TerritoryYear.

    This tells us which years each colony actually has data, so we can
    determine what "consecutive" means (e.g., 1894→1896 is consecutive
    if there's no 1895 edition for that colony).
    """
    result = session.run(
        "MATCH (ty:COL_TerritoryYear) "
        "WHERE ty.stage1_loaded = true AND ty.year >= $min_year "
        "RETURN ty.name AS colony, ty.year AS year",
        min_year=SKIP_BEFORE,
    )
    index = defaultdict(set)
    for record in result:
        index[record["colony"]].add(record["year"])
    return {colony: sorted(years) for colony, years in index.items()}


# =============================================================================
# FETCH PERSON RECORDS
# =============================================================================

def fetch_person_record_details(session, colony_filter=None) -> dict[tuple[str, str], list[dict]]:
    """Fetch PersonRecord details grouped by (canonical_name, colony).

    Returns dict keyed by (name, colony) with list of per-record dicts
    containing year, given_names, position_raw, department_raw.
    """
    colony_clause = "AND pr.colony = $colony " if colony_filter else ""
    params = {"min_year": SKIP_BEFORE}
    if colony_filter:
        params["colony"] = colony_filter

    result = session.run(
        "MATCH (pr:COL_PersonRecord) "
        "WHERE pr.year >= $min_year "
        "  AND (pr.quarantined IS NULL OR pr.quarantined = false) "
        + colony_clause +
        "RETURN pr.canonical_name AS name, pr.colony AS colony, "
        "       pr.year AS year, pr.given_names AS given_names, "
        "       pr.position_raw AS position_raw, "
        "       pr.department_raw AS department_raw",
        **params,
    )

    groups = defaultdict(list)
    for record in result:
        key = (record["name"], record["colony"])
        groups[key].append({
            "year": record["year"],
            "given_names": record["given_names"] or "",
            "position_raw": record["position_raw"] or "",
            "department_raw": record["department_raw"] or "",
        })

    # Sort each group by year
    for key in groups:
        groups[key].sort(key=lambda r: r["year"])

    return dict(groups)


def _normalize_dept(dept: str) -> str:
    """Normalize department string for comparison."""
    return dept.lower().strip().rstrip(".")


def _dept_compatible(a: str, b: str) -> bool:
    """Check if two department strings refer to the same department."""
    a_n = _normalize_dept(a)
    b_n = _normalize_dept(b)
    if not a_n or not b_n:
        return True  # unknown department matches anything
    if a_n == b_n:
        return True
    # Substring match (handles "Audit Branch" vs "Audit")
    if a_n in b_n or b_n in a_n:
        return True
    return False


def subgroup_by_identity(records: list[dict]) -> list[list[dict]]:
    """Split records sharing (canonical_name, colony) into sub-groups
    representing distinct individuals.

    Uses given-name compatibility and position/department continuity.

    Algorithm:
      1. Sort records by year
      2. For each record, try to assign to an existing cluster:
         a. Given names must be initials_compatible with the cluster
         b. Department/position should show continuity
         c. Year gap should be reasonable
      3. If no cluster matches, start a new cluster

    Key constraints:
      - Large year gap (>10) requires same department to merge
      - Incompatible given names always split (different person)
      - Same department in adjacent years is the strongest merge signal
    """
    if not records:
        return []

    clusters = []  # list of lists of records

    for rec in records:
        rec_given = clean_given_names(rec["given_names"])
        rec_dept = rec["department_raw"]
        rec_year = rec["year"]

        best_cluster = None
        best_score = -1

        for idx, cluster in enumerate(clusters):
            # Check given-name compatibility with ALL records in cluster
            cluster_givens = [clean_given_names(r["given_names"]) for r in cluster]
            non_empty_givens = [cg for cg in cluster_givens if cg]
            if rec_given and non_empty_givens:
                compatible = all(
                    initials_compatible(rec_given, cg) for cg in non_empty_givens
                )
                if not compatible:
                    continue

            # Score this cluster: prefer recent + same department
            last_rec = cluster[-1]
            year_gap = rec_year - last_rec["year"]
            same_dept = _dept_compatible(rec_dept, last_rec["department_raw"])

            # Hard constraint: large gap without department continuity → don't merge
            if year_gap > 10 and not same_dept:
                continue

            score = 0

            # Strong signal: same department in adjacent year
            if same_dept and year_gap <= 5:
                score += 20

            # Same department but larger gap
            elif same_dept:
                score += 10

            # Different/unknown department but small gap
            elif year_gap <= 3:
                score += 5
            elif year_gap <= 5:
                score += 2

            # Penalize large gaps without department evidence
            if year_gap > 5 and not same_dept:
                score -= 5

            # Prefer longer clusters (more evidence)
            score += len(cluster) * 0.1

            if score > best_score:
                best_score = score
                best_cluster = idx

        if best_cluster is not None and best_score > 0:
            clusters[best_cluster].append(rec)
        else:
            clusters.append([rec])

    return clusters


# =============================================================================
# CHAIN INTO STINTS
# =============================================================================

def chain_into_stints(
    years: list[int],
    colony_editions: list[int],
) -> list[list[int]]:
    """Chain a person's appearance years into continuous career stints.

    Two appearances are "consecutive" if there are 0 or 1 colony editions
    between them that the person missed. This allows for leave, temporary
    absence, etc.

    Args:
        years: Sorted list of years this person appeared in this colony.
        colony_editions: Sorted list of all edition years for this colony.

    Returns:
        List of stints, where each stint is a list of years.
    """
    if not years:
        return []

    # Build a set for O(1) lookup
    edition_set = set(colony_editions)

    stints = []
    current_stint = [years[0]]

    for i in range(1, len(years)):
        prev_year = years[i - 1]
        curr_year = years[i]

        # Count how many colony editions exist between prev and curr
        # that this person MISSED
        editions_between = [
            y for y in colony_editions
            if prev_year < y < curr_year
        ]
        missed = len(editions_between)

        if missed <= 1:
            # Consecutive (allowing 1 skip): same stint
            current_stint.append(curr_year)
        else:
            # Gap too large: start new stint
            stints.append(current_stint)
            current_stint = [curr_year]

    stints.append(current_stint)
    return stints


def _best_name_for_cluster(canonical_name: str, cluster: list[dict]) -> str:
    """Choose the best canonical name for a sub-cluster.

    If the cluster has given-name variants, pick the most specific one
    and rebuild the canonical name.
    """
    given_variants = []
    for rec in cluster:
        gn = clean_given_names(rec["given_names"])
        if gn:
            given_variants.append(gn)

    if not given_variants:
        return canonical_name

    best_given = choose_best_name(given_variants)
    # Extract surname from canonical_name
    surname = canonical_name.split(",", 1)[0].strip()
    if best_given:
        return f"{surname}, {best_given}"
    return canonical_name


def build_all_stints(
    name_colony_records: dict[tuple[str, str], list[dict]],
    colony_edition_index: dict[str, list[int]],
    min_editions: int = MIN_EDITIONS,
) -> list[dict]:
    """Build all career stint records from PersonRecord data.

    For each (canonical_name, colony) group, first splits into sub-groups
    by given-name compatibility and position/department continuity, then
    chains each sub-group into stints.

    Returns list of dicts ready for Neo4j insertion.
    """
    officials = []
    splits_performed = 0

    for (name, colony), records in name_colony_records.items():
        colony_editions = colony_edition_index.get(colony, [])
        if not colony_editions:
            continue

        # Sub-group by identity (given name + department)
        clusters = subgroup_by_identity(records)
        if len(clusters) > 1:
            splits_performed += 1

        for cluster in clusters:
            years = sorted({r["year"] for r in cluster})
            stints = chain_into_stints(years, colony_editions)

            # Pick the best name for this cluster
            cluster_name = _best_name_for_cluster(name, cluster)

            # Collect all given_names variants in this cluster for RECORD_OF matching
            cluster_given_variants = list({
                r["given_names"] for r in cluster if r["given_names"]
            })

            for stint in stints:
                if len(stint) < min_editions:
                    continue

                first_year = stint[0]
                last_year = stint[-1]
                official_id = f"{cluster_name}___{colony}___{first_year}"

                officials.append({
                    "id": official_id,
                    "name": cluster_name,
                    "canonical_name": name,  # original grouping key for RECORD_OF
                    "colony": colony,
                    "first_year": first_year,
                    "last_year": last_year,
                    "num_editions": len(stint),
                    "editions": stint,
                    "given_variants": cluster_given_variants,
                })

    if splits_performed:
        print(f"  Sub-grouped {splits_performed} name/colony groups by identity")

    return officials


# =============================================================================
# WRITE TO NEO4J
# =============================================================================

CREATE_OFFICIALS_QUERY = """
UNWIND $batch AS b
MERGE (o:COL_Official {id: b.id})
SET o.name = b.name,
    o.colony = b.colony,
    o.first_year = b.first_year,
    o.last_year = b.last_year,
    o.num_editions = b.num_editions,
    o.editions = b.editions
"""

LINK_RECORD_OF_QUERY = """
UNWIND $batch AS b
MATCH (o:COL_Official {id: b.id})
WITH o, b
UNWIND b.editions AS yr
MATCH (pr:COL_PersonRecord {canonical_name: b.canonical_name, colony: b.colony, year: yr})
WHERE size(b.given_variants) = 0 OR pr.given_names IN b.given_variants
   OR pr.given_names IS NULL
MERGE (pr)-[:RECORD_OF]->(o)
"""

LINK_TERRITORY_QUERY = """
MATCH (o:COL_Official)
WHERE NOT (o)-[:SERVED_IN_COLONY]->()
MATCH (t:COL_Territory {name: o.colony})
MERGE (o)-[:SERVED_IN_COLONY]->(t)
"""

SCHEMA_STATEMENTS = [
    "CREATE CONSTRAINT col_official_id IF NOT EXISTS FOR (o:COL_Official) REQUIRE o.id IS UNIQUE",
    "CREATE INDEX col_official_name IF NOT EXISTS FOR (o:COL_Official) ON (o.name)",
    "CREATE INDEX col_official_colony IF NOT EXISTS FOR (o:COL_Official) ON (o.colony)",
]


def create_schema(session):
    """Create constraints and indexes for COL_Official."""
    for stmt in SCHEMA_STATEMENTS:
        try:
            session.run(stmt)
        except Exception as e:
            if "already exists" not in str(e).lower() and "equivalent" not in str(e).lower():
                print(f"  WARNING: {e}")


def write_officials(driver, officials: list[dict]):
    """Write COL_Official nodes and RECORD_OF edges."""
    with driver.session() as session:
        create_schema(session)

        # Create/update COL_Official nodes
        print(f"Creating {len(officials)} COL_Official nodes...")
        for i in range(0, len(officials), BATCH_SIZE):
            batch = officials[i:i + BATCH_SIZE]
            session.run(CREATE_OFFICIALS_QUERY, batch=batch)
            print(f"  Created {min(i + BATCH_SIZE, len(officials))}/{len(officials)} officials...")

        # Link PersonRecords via RECORD_OF
        print("\nLinking PersonRecords to Officials...")
        total_linked = 0
        for i in range(0, len(officials), BATCH_SIZE):
            batch = officials[i:i + BATCH_SIZE]
            result = session.run(
                LINK_RECORD_OF_QUERY + " RETURN count(*) AS c",
                batch=batch,
            ).single()
            total_linked += result["c"]
            print(f"  Linked {total_linked} records so far...")

        # Link to COL_Territory
        print("\nLinking Officials to COL_Territory...")
        session.run(LINK_TERRITORY_QUERY)

    return total_linked


# =============================================================================
# STATS
# =============================================================================

def print_stats(driver):
    """Report on COL_Official nodes."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("COL_OFFICIAL STATISTICS")
        print("=" * 60)

        r = session.run("MATCH (o:COL_Official) RETURN count(o) AS c").single()
        total = r["c"]
        print(f"\n  Total COL_Official nodes: {total}")

        if total == 0:
            return

        r = session.run(
            "MATCH (pr:COL_PersonRecord)-[:RECORD_OF]->(o:COL_Official) "
            "RETURN count(pr) AS linked"
        ).single()
        linked = r["linked"]

        r = session.run(
            "MATCH (pr:COL_PersonRecord) WHERE pr.year >= $min_year "
            "RETURN count(pr) AS total",
            min_year=SKIP_BEFORE,
        ).single()
        total_pr = r["total"]

        print(f"  RECORD_OF edges: {linked}")
        print(f"  PersonRecords (1877+): {total_pr}")
        if total_pr > 0:
            print(f"  Coverage: {100 * linked / total_pr:.1f}%")

        # Edition count distribution
        print("\n  Edition count distribution:")
        result = session.run(
            "MATCH (o:COL_Official) "
            "RETURN o.num_editions AS editions, count(o) AS n "
            "ORDER BY editions"
        )
        for record in result:
            bar = "█" * max(1, record["n"] * 40 // total)
            print(f"    {record['editions']:>3} editions: {record['n']:>6}  {bar}")

        # Top colonies
        print("\n  Top 15 colonies by COL_Official count:")
        result = session.run(
            "MATCH (o:COL_Official) "
            "RETURN o.colony AS colony, count(o) AS n "
            "ORDER BY n DESC LIMIT 15"
        )
        for record in result:
            print(f"    {record['colony']:<40} {record['n']:>6}")

        # Unique names
        r = session.run(
            "MATCH (o:COL_Official) "
            "RETURN count(DISTINCT o.name) AS names"
        ).single()
        print(f"\n  Unique names: {r['names']}")


# =============================================================================
# DRY RUN
# =============================================================================

def dry_run_report(officials: list[dict]):
    """Preview without writing."""
    print("\n" + "=" * 60)
    print("[DRY RUN] COL_OFFICIAL PREVIEW")
    print("=" * 60)

    print(f"\n  Career stints found: {len(officials)}")

    if not officials:
        print("  No stints to create.")
        return

    # Edition distribution
    edition_counts = defaultdict(int)
    for o in officials:
        edition_counts[o["num_editions"]] += 1

    print("\n  Edition count distribution:")
    for ed in sorted(edition_counts):
        n = edition_counts[ed]
        bar = "█" * max(1, n * 40 // len(officials))
        print(f"    {ed:>3} editions: {n:>6}  {bar}")

    # Colony distribution (top 15)
    colony_counts = defaultdict(int)
    for o in officials:
        colony_counts[o["colony"]] += 1

    print("\n  Top 15 colonies:")
    for colony, n in sorted(colony_counts.items(), key=lambda x: -x[1])[:15]:
        print(f"    {colony:<40} {n:>6}")

    # Unique names
    names = {o["name"] for o in officials}
    print(f"\n  Unique names: {len(names)}")

    # Sample officials
    sorted_officials = sorted(officials, key=lambda o: -o["num_editions"])
    print("\n  Longest-serving officials:")
    for o in sorted_officials[:10]:
        print(f"    {o['name']:<35} {o['colony']:<25} "
              f"{o['first_year']}-{o['last_year']} ({o['num_editions']} editions)")

    print("\n[DRY RUN] No data written.")


# =============================================================================
# CLEAR
# =============================================================================

def clear_officials(driver):
    """Remove all COL_Official nodes and their edges."""
    with driver.session() as session:
        r = session.run(
            "MATCH (o:COL_Official) DETACH DELETE o RETURN count(o) AS c"
        ).single()
        print(f"Deleted {r['c']} COL_Official nodes (and all RECORD_OF/SERVED_IN_COLONY edges).")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Stage 2: Build COL_Official career stint nodes"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without writing to Neo4j")
    parser.add_argument("--stats", action="store_true",
                        help="Report COL_Official statistics")
    parser.add_argument("--clear", action="store_true",
                        help="Remove all COL_Official nodes")
    parser.add_argument("--colony", type=str,
                        help="Filter to specific colony")
    args = parser.parse_args()

    print("=" * 60)
    print("COL STAGE 2: BUILD COL_OFFICIAL CAREER STINTS")
    print("=" * 60)

    # Connect to Neo4j
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        # --- Stats only ---
        if args.stats:
            print_stats(driver)
            return

        # --- Clear ---
        if args.clear:
            clear_officials(driver)
            return

        # --- Build colony edition index ---
        print("\nBuilding colony edition index...")
        with driver.session() as session:
            colony_edition_index = build_colony_edition_index(session)
        print(f"  {len(colony_edition_index)} colonies with loaded editions")

        # --- Fetch PersonRecord details ---
        print("Fetching PersonRecord details...")
        with driver.session() as session:
            name_colony_records = fetch_person_record_details(
                session, colony_filter=args.colony,
            )
        print(f"  {len(name_colony_records)} (name, colony) combinations")

        # --- Sub-group and chain into stints ---
        print("Sub-grouping by identity and chaining into career stints...")
        officials = build_all_stints(
            name_colony_records, colony_edition_index,
        )
        print(f"  {len(officials)} stints with {MIN_EDITIONS}+ editions")

        if not officials:
            print("\nNo stints found. Nothing to do.")
            return

        # --- Dry run or write ---
        if args.dry_run:
            dry_run_report(officials)
            return

        total_linked = write_officials(driver, officials)
        print(f"\nFinal: {len(officials)} COL_Official nodes, "
              f"{total_linked} RECORD_OF edges")

        # --- Final stats ---
        print_stats(driver)

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()

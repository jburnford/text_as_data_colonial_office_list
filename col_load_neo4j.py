"""
Neo4j Stage 1: Load COL PersonRecords into Knowledge Graph
============================================================

Loads extracted personnel data from Colonial Office List corpus into Neo4j,
creating COL_PersonRecord and COL_InstitutionInstance nodes linked to the
existing COL_TerritoryYear scaffold (Stage 0).

All labels use the COL_ prefix to coexist with IOL_ and AW_ data in the
shared Arbutus Neo4j instance.

Important epistemological note:
  A COL_PersonRecord is an OBSERVATION, not a Person. It records that a name
  appeared in a specific colony's list in a specific year. The same human may
  have multiple PersonRecords across years and colonies. Linking observations
  into persistent Person entities is Stage 4 (entity resolution) — not here.

Usage:
    python col_load_neo4j.py                          # load all available
    python col_load_neo4j.py --year 1896              # load one year
    python col_load_neo4j.py --colony "Sierra Leone"  # load one colony
    python col_load_neo4j.py --dry-run                # preview only
    python col_load_neo4j.py --clear                  # remove Stage 1 data only
    python col_load_neo4j.py --stats                  # report current state

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

from scaffold_neo4j import normalize_colony_name


# =============================================================================
# CONFIGURATION
# =============================================================================

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")

REPO_DIR = Path(__file__).parent
GENERATED_DIR = REPO_DIR / "generated"

PIPELINE_VERSION = "1.0"
BATCH_SIZE = 500
DEFAULT_CONFIDENCE = 0.95


# =============================================================================
# CURRENCY INFERENCE
# =============================================================================

RUPEE_COLONIES = {
    "Ceylon", "Straits Settlements", "Mauritius",
    "Federated Malay States", "Unfederated Malay States",
}

DOLLAR_COLONIES = {
    "Hong Kong",
}


def infer_currency(colony: str) -> str:
    """Infer the likely salary currency for a colony. Default: GBP."""
    if colony in RUPEE_COLONIES:
        return "Rs"
    if colony in DOLLAR_COLONIES:
        return "HKD"
    return "GBP"


# =============================================================================
# URI / SLUG HELPERS
# =============================================================================

def slugify(text: str) -> str:
    """Convert text to a URL-safe slug."""
    s = text.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '_', s)
    s = s.strip('_')
    return s


def make_name_key(record_index: int, surname: str, given_names: str) -> str:
    """Generate a deterministic name key for a PersonRecord URI.

    Uses record_index for determinism; name parts for readability.
    """
    parts = [str(record_index)]
    if surname:
        parts.append(slugify(surname))
    if given_names:
        initials = ''.join(
            w[0].lower() for w in given_names.split() if w and w[0].isalpha()
        )
        if initials:
            parts.append(initials)
    return '_'.join(parts)


def make_pr_uri(colony_slug: str, year: int, record_index: int,
                surname: str, given_names: str) -> str:
    """Generate a COL_PersonRecord URI."""
    name_key = make_name_key(record_index, surname, given_names)
    return f"col:pr/{colony_slug}/{year}/{name_key}"


def make_inst_uri(colony_slug: str, year: int, department: str) -> str:
    """Generate a COL_InstitutionInstance URI."""
    dept_slug = slugify(department)
    return f"col:inst/{colony_slug}/{year}/{dept_slug}"


# =============================================================================
# FILE DISCOVERY
# =============================================================================

def parse_extraction_filename(filename: str):
    """Parse extraction filename to get (colony_stem, year).

    Expected pattern: {colony_stem}_{year}_data_{model}.json
    """
    m = re.match(r'^(.+)_(\d{4})_data_.+\.json$', filename)
    if m:
        return m.group(1), int(m.group(2))
    return None


def discover_extraction_files(year_filter=None, colony_filter=None):
    """Find all extraction data JSON files in generated/.

    Prefers non-chunked versions when both exist for the same colony-year.
    Returns list of dicts: {path, colony_stem, year, canonical_name, ty_id}
    """
    if not GENERATED_DIR.exists():
        print(f"WARNING: {GENERATED_DIR} does not exist")
        return []

    candidates = {}
    for path in sorted(GENERATED_DIR.glob("*_data_*.json")):
        parsed = parse_extraction_filename(path.name)
        if not parsed:
            continue

        colony_stem, year = parsed
        canonical_name = normalize_colony_name(colony_stem)
        ty_id = f"{canonical_name}_{year}"
        is_chunked = "_chunked" in path.name

        if year_filter is not None and year != year_filter:
            continue
        if colony_filter is not None and canonical_name != colony_filter:
            continue

        candidates.setdefault(ty_id, []).append(
            (path, colony_stem, year, canonical_name, is_chunked)
        )

    files = []
    for ty_id, entries in sorted(candidates.items()):
        if len(entries) == 1:
            path, colony_stem, year, canonical_name, _ = entries[0]
        else:
            entries.sort(key=lambda e: (e[4], -e[0].stat().st_mtime))
            path, colony_stem, year, canonical_name, _ = entries[0]

        files.append({
            "path": path,
            "colony_stem": colony_stem,
            "year": year,
            "canonical_name": canonical_name,
            "ty_id": ty_id,
        })

    return files


# =============================================================================
# RECORD PREPARATION
# =============================================================================

def prepare_records(data: dict, colony_stem: str, canonical_name: str,
                    year: int, extraction_file: str):
    """Convert extraction JSON into Neo4j-ready record dicts.

    Returns (person_records, dept_records).
    """
    colony_slug = slugify(canonical_name)
    currency = infer_currency(canonical_name)
    officials = data.get("officials", [])

    person_records = []
    dept_records = []
    seen_depts = set()

    for idx, official in enumerate(officials):
        surname = official.get("surname", "") or ""
        given_names = official.get("given_names", "") or ""
        department = official.get("department")

        pr_uri = make_pr_uri(colony_slug, year, idx, surname, given_names)
        ty_id = f"{canonical_name}_{year}"

        rec = {
            "uri": pr_uri,
            "ty_id": ty_id,
            "year": year,
            "colony": canonical_name,
            "name_raw": official.get("name", ""),
            "canonical_name": official.get("canonical_name", ""),
            "surname": surname,
            "given_names": given_names,
            "position_raw": official.get("position", ""),
            "department_raw": department,
            "salary_min": official.get("salary_min"),
            "salary_max": official.get("salary_max"),
            "salary_currency": currency,
            "salary_scale": official.get("salary_scale"),
            "allowances_raw": official.get("allowances"),
            "honors": official.get("honors") or [],
            "qualifications": official.get("qualifications") or [],
            "military_rank": official.get("military_rank"),
            "location": official.get("location"),
            "extraction_file": extraction_file,
            "record_index": idx,
            "confidence": DEFAULT_CONFIDENCE,
        }
        person_records.append(rec)

        if department and department not in seen_depts:
            seen_depts.add(department)
            inst_uri = make_inst_uri(colony_slug, year, department)
            dept_records.append({
                "inst_uri": inst_uri,
                "ty_id": ty_id,
                "year": year,
                "colony": canonical_name,
                "department_raw": department,
            })

        rec["inst_uri"] = make_inst_uri(colony_slug, year, department) if department else None

    return person_records, dept_records


# =============================================================================
# SCHEMA SETUP
# =============================================================================

SCHEMA_STATEMENTS = [
    # Uniqueness constraints
    "CREATE CONSTRAINT col_pr_uri IF NOT EXISTS FOR (pr:COL_PersonRecord) REQUIRE pr.uri IS UNIQUE",
    "CREATE CONSTRAINT col_ii_uri IF NOT EXISTS FOR (ii:COL_InstitutionInstance) REQUIRE ii.uri IS UNIQUE",

    # Lookup indexes
    "CREATE INDEX col_pr_colony_year IF NOT EXISTS FOR (pr:COL_PersonRecord) ON (pr.colony, pr.year)",
    "CREATE INDEX col_pr_surname IF NOT EXISTS FOR (pr:COL_PersonRecord) ON (pr.surname)",
    "CREATE INDEX col_pr_canonical IF NOT EXISTS FOR (pr:COL_PersonRecord) ON (pr.canonical_name)",
    "CREATE INDEX col_ii_colony_year IF NOT EXISTS FOR (ii:COL_InstitutionInstance) ON (ii.colony, ii.year)",

    # Full-text search for fuzzy name matching (Stage 4 entity resolution)
    "CREATE FULLTEXT INDEX col_pr_name_ft IF NOT EXISTS FOR (n:COL_PersonRecord) ON EACH [n.name_raw, n.canonical_name, n.surname]",
]


def create_schema(session):
    """Create constraints and indexes (idempotent)."""
    print("Creating constraints and indexes...")
    for stmt in SCHEMA_STATEMENTS:
        try:
            session.run(stmt)
        except Exception as e:
            if "already exists" not in str(e).lower() and "equivalent" not in str(e).lower():
                print(f"  WARNING: {e}")


# =============================================================================
# CYPHER QUERIES — all use COL_ labels
# =============================================================================

PERSON_QUERY = """
UNWIND $batch AS rec
MATCH (ty:COL_TerritoryYear {id: rec.ty_id})
MATCH (y:COL_Year {value: rec.year})
MERGE (pr:COL_PersonRecord {uri: rec.uri})
ON CREATE SET
  pr.name_raw = rec.name_raw,
  pr.canonical_name = rec.canonical_name,
  pr.surname = rec.surname,
  pr.given_names = rec.given_names,
  pr.position_raw = rec.position_raw,
  pr.department_raw = rec.department_raw,
  pr.salary_min = rec.salary_min,
  pr.salary_max = rec.salary_max,
  pr.salary_currency = rec.salary_currency,
  pr.salary_scale = rec.salary_scale,
  pr.allowances_raw = rec.allowances_raw,
  pr.honors = rec.honors,
  pr.qualifications = rec.qualifications,
  pr.military_rank = rec.military_rank,
  pr.location = rec.location,
  pr.source_file = ty.source_file,
  pr.extraction_file = rec.extraction_file,
  pr.record_index = rec.record_index,
  pr.colony = rec.colony,
  pr.year = rec.year
MERGE (pr)-[r:SERVED_IN]->(ty)
ON CREATE SET
  r.method = 'automated_extraction',
  r.confidence = rec.confidence,
  r.pipeline_version = $pipeline_version,
  r.date_created = $today
MERGE (pr)-[:IN_YEAR]->(y)
"""

DEPT_QUERY = """
UNWIND $batch AS rec
MATCH (ty:COL_TerritoryYear {id: rec.ty_id})
MATCH (y:COL_Year {value: rec.year})
MERGE (ii:COL_InstitutionInstance {uri: rec.inst_uri})
ON CREATE SET
  ii.name_raw = rec.department_raw,
  ii.colony = rec.colony,
  ii.year = rec.year
MERGE (ii)-[:DEPARTMENT_OF]->(ty)
MERGE (ii)-[:IN_YEAR]->(y)
"""

PERSON_DEPT_QUERY = """
UNWIND $batch AS rec
MATCH (pr:COL_PersonRecord {uri: rec.uri})
MATCH (ii:COL_InstitutionInstance {uri: rec.inst_uri})
MERGE (pr)-[r:IN_DEPARTMENT]->(ii)
ON CREATE SET
  r.method = 'automated_extraction',
  r.pipeline_version = $pipeline_version,
  r.date_created = $today
"""

MARK_LOADED_QUERY = """
MATCH (ty:COL_TerritoryYear {id: $ty_id})
SET ty.stage1_loaded = true, ty.stage1_count = $count
"""


# =============================================================================
# LOADING LOGIC
# =============================================================================

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_loaded_territory_years(session):
    """Return set of COL_TerritoryYear IDs already loaded in Stage 1."""
    result = session.run(
        "MATCH (ty:COL_TerritoryYear) WHERE ty.stage1_loaded = true RETURN ty.id AS id"
    )
    return {record["id"] for record in result}


def get_existing_territory_years(session):
    """Return set of all COL_TerritoryYear IDs in the scaffold."""
    result = session.run("MATCH (ty:COL_TerritoryYear) RETURN ty.id AS id")
    return {record["id"] for record in result}


def load_file(session, person_records, dept_records, ty_id, year, today_str):
    """Load one extraction file's records into Neo4j in a single transaction."""
    tx = session.begin_transaction()
    try:
        for batch in chunks(dept_records, BATCH_SIZE):
            tx.run(DEPT_QUERY, batch=batch,
                   pipeline_version=PIPELINE_VERSION, today=today_str)

        for batch in chunks(person_records, BATCH_SIZE):
            tx.run(PERSON_QUERY, batch=batch,
                   pipeline_version=PIPELINE_VERSION, today=today_str)

        dept_linked = [r for r in person_records if r.get("inst_uri")]
        for batch in chunks(dept_linked, BATCH_SIZE):
            tx.run(PERSON_DEPT_QUERY, batch=batch,
                   pipeline_version=PIPELINE_VERSION, today=today_str)

        tx.run(MARK_LOADED_QUERY, ty_id=ty_id, count=len(person_records))

        tx.commit()
        return True

    except Exception as e:
        tx.rollback()
        raise e


# =============================================================================
# STATS / CLEAR (label-scoped — safe for shared database)
# =============================================================================

def print_stats(driver):
    """Report on current COL Stage 1 graph contents."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("COL STAGE 1 STATISTICS")
        print("=" * 60)

        # Scaffold
        r = session.run("MATCH (y:COL_Year) RETURN count(y) AS c").single()
        print(f"\n  Scaffold:")
        print(f"    COL_Year nodes:              {r['c']}")
        r = session.run("MATCH (t:COL_Territory) RETURN count(t) AS c").single()
        print(f"    COL_Territory nodes:          {r['c']}")
        r = session.run("MATCH (ty:COL_TerritoryYear) RETURN count(ty) AS c").single()
        print(f"    COL_TerritoryYear nodes:      {r['c']}")

        # Stage 1
        r = session.run("MATCH (pr:COL_PersonRecord) RETURN count(pr) AS c").single()
        pr_count = r['c']
        print(f"\n  Stage 1 data:")
        print(f"    COL_PersonRecord nodes:       {pr_count}")
        r = session.run("MATCH (ii:COL_InstitutionInstance) RETURN count(ii) AS c").single()
        print(f"    COL_InstitutionInstance nodes: {r['c']}")

        # Edges
        r = session.run(
            "MATCH (:COL_PersonRecord)-[r:SERVED_IN]->(:COL_TerritoryYear) "
            "RETURN count(r) AS c"
        ).single()
        print(f"    SERVED_IN edges:              {r['c']}")
        r = session.run(
            "MATCH (:COL_PersonRecord)-[r:IN_DEPARTMENT]->(:COL_InstitutionInstance) "
            "RETURN count(r) AS c"
        ).single()
        print(f"    IN_DEPARTMENT edges:          {r['c']}")

        # Loading progress
        r = session.run(
            "MATCH (ty:COL_TerritoryYear) WHERE ty.stage1_loaded = true "
            "RETURN count(ty) AS loaded, sum(ty.stage1_count) AS officials"
        ).single()
        loaded = r['loaded']
        officials = r['officials'] or 0
        r2 = session.run("MATCH (ty:COL_TerritoryYear) RETURN count(ty) AS total").single()
        total_ty = r2['total']

        print(f"\n  Loading progress:")
        if total_ty:
            print(f"    TerritoryYears loaded: {loaded} / {total_ty} ({100*loaded/total_ty:.1f}%)")
        else:
            print(f"    TerritoryYears loaded: 0 (scaffold not loaded yet)")
        print(f"    Total officials:       {officials}")

        # Top colonies
        if pr_count > 0:
            print(f"\n  Top 15 colonies:")
            result = session.run(
                "MATCH (pr:COL_PersonRecord) "
                "RETURN pr.colony AS colony, count(pr) AS n "
                "ORDER BY n DESC LIMIT 15"
            )
            for record in result:
                print(f"    {record['colony']:<40} {record['n']:>6}")


def clear_stage1(driver):
    """Remove all COL Stage 1 nodes and edges. Does NOT touch scaffold or other datasets."""
    with driver.session() as session:
        print("Clearing COL Stage 1 data...")

        r = session.run(
            "MATCH (pr:COL_PersonRecord) DETACH DELETE pr RETURN count(pr) AS c"
        ).single()
        print(f"  Deleted {r['c']} COL_PersonRecord nodes")

        r = session.run(
            "MATCH (ii:COL_InstitutionInstance) DETACH DELETE ii RETURN count(ii) AS c"
        ).single()
        print(f"  Deleted {r['c']} COL_InstitutionInstance nodes")

        r = session.run(
            "MATCH (ty:COL_TerritoryYear) WHERE ty.stage1_loaded = true "
            "SET ty.stage1_loaded = null, ty.stage1_count = null "
            "RETURN count(ty) AS c"
        ).single()
        print(f"  Reset {r['c']} COL_TerritoryYear loading flags")

        print("COL Stage 1 cleared.")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Load COL extracted personnel data into Neo4j (Stage 1)"
    )
    parser.add_argument("--year", type=int, help="Load only this year")
    parser.add_argument("--colony", type=str, help="Load only this colony (canonical name)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview what would be loaded without touching Neo4j")
    parser.add_argument("--clear", action="store_true",
                        help="Remove all COL Stage 1 nodes (safe for shared DB)")
    parser.add_argument("--stats", action="store_true",
                        help="Report on current COL graph contents")
    args = parser.parse_args()

    print("=" * 60)
    print("NEO4J STAGE 1: LOAD COL PERSONRECORDS")
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

    # --- Discover extraction files ---
    print(f"\nScanning: {GENERATED_DIR}")
    files = discover_extraction_files(
        year_filter=args.year,
        colony_filter=args.colony,
    )
    print(f"Found {len(files)} extraction file(s)")

    if not files:
        print("Nothing to load.")
        return

    # Group by year for display
    by_year = defaultdict(list)
    for f in files:
        by_year[f["year"]].append(f["canonical_name"])
    for year in sorted(by_year):
        colonies = sorted(by_year[year])
        print(f"  {year}: {len(colonies)} colonies")

    # --- Dry run ---
    if args.dry_run:
        print("\n[DRY RUN] Reading files to preview records...")
        total_officials = 0
        total_depts = 0
        for f in files:
            try:
                with open(f["path"]) as fh:
                    data = json.load(fh)
                n_officials = len(data.get("officials", []))
                depts = {o.get("department") for o in data.get("officials", [])
                         if o.get("department")}
                total_officials += n_officials
                total_depts += len(depts)
            except Exception as e:
                print(f"  ERROR reading {f['path'].name}: {e}")

        print(f"\nTotal: {total_officials} officials, {total_depts} departments "
              f"across {len(files)} files")
        print("[DRY RUN] No data loaded.")
        return

    # --- Connect to Neo4j ---
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        # --- Clear if requested ---
        if args.clear:
            clear_stage1(driver)

        with driver.session() as session:
            create_schema(session)
            loaded_tys = get_loaded_territory_years(session)
            existing_tys = get_existing_territory_years(session)

        # --- Load files ---
        today_str = date.today().isoformat()
        stats = {"loaded": 0, "skipped_already": 0, "skipped_no_scaffold": 0,
                 "errors": 0, "total_officials": 0, "total_depts": 0}

        for f in files:
            ty_id = f["ty_id"]
            colony = f["canonical_name"]
            year = f["year"]

            if ty_id in loaded_tys:
                stats["skipped_already"] += 1
                continue

            if ty_id not in existing_tys:
                print(f"  SKIP (no scaffold): {colony} {year} (id: {ty_id})")
                stats["skipped_no_scaffold"] += 1
                continue

            try:
                with open(f["path"]) as fh:
                    data = json.load(fh)
            except Exception as e:
                print(f"  ERROR reading {f['path'].name}: {e}")
                stats["errors"] += 1
                continue

            extraction_file = f"generated/{f['path'].name}"
            person_records, dept_records = prepare_records(
                data, f["colony_stem"], colony, year, extraction_file
            )

            if not person_records:
                print(f"  SKIP (no officials): {colony} {year}")
                continue

            try:
                with driver.session() as session:
                    load_file(session, person_records, dept_records,
                              ty_id, year, today_str)

                loaded_tys.add(ty_id)
                stats["loaded"] += 1
                stats["total_officials"] += len(person_records)
                stats["total_depts"] += len(dept_records)
                print(f"  LOADED: {colony} {year} -- "
                      f"{len(person_records)} officials, "
                      f"{len(dept_records)} departments")

            except Exception as e:
                print(f"  ERROR loading {colony} {year}: {e}")
                stats["errors"] += 1

        # --- Summary ---
        print("\n" + "=" * 60)
        print("LOADING SUMMARY")
        print("=" * 60)
        print(f"  Files loaded:                {stats['loaded']}")
        print(f"  Skipped (already loaded):    {stats['skipped_already']}")
        print(f"  Skipped (no scaffold):       {stats['skipped_no_scaffold']}")
        print(f"  Errors:                      {stats['errors']}")
        print(f"  Total officials loaded:      {stats['total_officials']}")
        print(f"  Total departments loaded:    {stats['total_depts']}")

        if stats["loaded"] > 0:
            print_stats(driver)

    finally:
        driver.close()


if __name__ == "__main__":
    main()

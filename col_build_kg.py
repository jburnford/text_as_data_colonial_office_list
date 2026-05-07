"""
COL Knowledge Graph Builder (unified scaffold + loader)
========================================================

Replaces scaffold_neo4j.py (Stage 0) and col_load_neo4j.py (Stage 1) with a
single script that uses col_kg_crosswalk.json as the authoritative colony→KG
mapping.

Key features:
  - All nodes use COL_ label prefix
  - COL_TerritoryYear nodes linked to HistoricalTerritory via MAPS_TO edges
  - Crosswalk resolves temporal splits (Aden, Kenya, etc.) per year
  - Dual mappings (Niger Protectorate, British East Africa and Zanzibar) produce
    multiple MAPS_TO edges
  - no_kg_node entries get null colony_id/wikidata_id and no MAPS_TO edge

Usage:
    python col_build_kg.py                     # full build (scaffold + load)
    python col_build_kg.py --scaffold-only     # just scaffold, no person records
    python col_build_kg.py --load-only         # just person records (scaffold must exist)
    python col_build_kg.py --colony "Aden"     # single colony
    python col_build_kg.py --year 1896         # single year
    python col_build_kg.py --force                         # reload with updated extractions
    python col_build_kg.py --colony "Gold Coast" --force   # reload one colony
    python col_build_kg.py --dry-run           # preview
    python col_build_kg.py --clear             # remove all COL_ nodes
    python col_build_kg.py --stats             # report

Requires:
    pip install neo4j
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

from scaffold_neo4j import (
    EXPLICIT_ALIASES,
    normalize_colony_name,
)
from col_load_neo4j import (
    BATCH_SIZE,
    DEFAULT_CONFIDENCE,
    PIPELINE_VERSION,
    discover_extraction_files,
    infer_currency,
    make_inst_uri,
    make_pr_uri,
    prepare_records,
    slugify,
)

# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
CROSSWALK_PATH = REPO_DIR / "scaffolding" / "col_kg_crosswalk.json"


def _load_dotenv():
    """Load .env file from repo root, handling special characters safely."""
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
# CROSSWALK LOADING
# =============================================================================

def load_crosswalk() -> dict:
    """Load col_kg_crosswalk.json. Returns {col_name: crosswalk_entry}."""
    with open(CROSSWALK_PATH) as f:
        return json.load(f)


def resolve_mapping(crosswalk_entry: dict, year: int) -> list[dict]:
    """Resolve crosswalk mappings for a specific year.

    Returns list of matching mappings (usually 1, but can be 2+ for dual mappings).
    Returns empty list if no mapping covers this year.
    """
    matches = []
    for m in crosswalk_entry["mappings"]:
        if m["year_start"] <= year <= m["year_end"]:
            matches.append(m)
    return matches


# =============================================================================
# CORPUS SCANNING (handles both .txt and .md files)
# =============================================================================

def scan_corpus(repo_dir: Path) -> dict[int, list[tuple[str, str, str]]]:
    """Scan year-directories and return {year: [(filename, stem, canonical_name), ...]}.

    Handles both .txt and .md source files.
    """
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
        # Collect both .txt and .md, preferring .txt if both exist for same stem
        seen_stems = set()
        for ext in ("*.txt", "*.md"):
            for src_file in sorted(entry.glob(ext)):
                stem = src_file.stem
                if stem in seen_stems:
                    continue
                seen_stems.add(stem)
                canonical = normalize_colony_name(stem)
                files.append((src_file.name, stem, canonical))

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
# SCHEMA (all COL_ prefixed)
# =============================================================================

SCHEMA_STATEMENTS = [
    # Constraints
    "CREATE CONSTRAINT col_year_value IF NOT EXISTS FOR (y:COL_Year) REQUIRE y.value IS UNIQUE",
    "CREATE CONSTRAINT col_territory_name IF NOT EXISTS FOR (t:COL_Territory) REQUIRE t.name IS UNIQUE",
    "CREATE CONSTRAINT col_ty_id IF NOT EXISTS FOR (ty:COL_TerritoryYear) REQUIRE ty.id IS UNIQUE",
    "CREATE CONSTRAINT col_pr_uri IF NOT EXISTS FOR (pr:COL_PersonRecord) REQUIRE pr.uri IS UNIQUE",
    "CREATE CONSTRAINT col_ii_uri IF NOT EXISTS FOR (ii:COL_InstitutionInstance) REQUIRE ii.uri IS UNIQUE",

    # Indexes
    "CREATE INDEX col_pr_colony_year IF NOT EXISTS FOR (pr:COL_PersonRecord) ON (pr.colony, pr.year)",
    "CREATE INDEX col_pr_surname IF NOT EXISTS FOR (pr:COL_PersonRecord) ON (pr.surname)",
    "CREATE INDEX col_pr_canonical IF NOT EXISTS FOR (pr:COL_PersonRecord) ON (pr.canonical_name)",
    "CREATE INDEX col_ii_colony_year IF NOT EXISTS FOR (ii:COL_InstitutionInstance) ON (ii.colony, ii.year)",
    "CREATE INDEX col_ty_colony_id IF NOT EXISTS FOR (ty:COL_TerritoryYear) ON (ty.colony_id)",

    # Full-text search
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
# SCAFFOLD LOADING
# =============================================================================

def load_scaffold(driver, corpus: dict, inventory: dict, crosswalk: dict,
                  colony_filter: list[str] | None = None,
                  year_filter: int | None = None):
    """Load COL_Year, COL_Territory, COL_TerritoryYear nodes + all edges."""

    with driver.session() as session:
        create_schema(session)

        # --- COL_Year nodes ---
        years = inventory["years"]
        if year_filter:
            years = [y for y in years if y == year_filter]
        else:
            # Always create all years for IN_YEAR edges to work
            pass
        print(f"Creating {len(years)} COL_Year nodes ({years[0]}–{years[-1]})...")
        session.run(
            "UNWIND $years AS y MERGE (n:COL_Year {value: y})",
            years=years,
        )

        # --- COL_Territory nodes (with crosswalk data) ---
        territories = list(inventory["territories"].keys())
        if colony_filter:
            territories = [t for t in territories if t in colony_filter]

        territory_data = []
        for name in territories:
            cw_entry = crosswalk.get(name)
            if cw_entry:
                # Primary colony_id: first mapping's colony_id (for non-temporal-split,
                # there's only one; for temporal splits, this is the "default")
                primary = cw_entry["mappings"][0]
                has_split = cw_entry.get("has_temporal_split", False)
                is_no_kg = primary.get("confidence") == "no_kg_node"
                territory_data.append({
                    "name": name,
                    "colony_id": None if is_no_kg else primary["colony_id"],
                    "wikidata_id": None if is_no_kg else primary.get("wikidata_id"),
                    "canonical_name_kg": None if is_no_kg else primary.get("canonical_name"),
                    "has_temporal_split": has_split,
                })
            else:
                territory_data.append({
                    "name": name,
                    "colony_id": None,
                    "wikidata_id": None,
                    "canonical_name_kg": None,
                    "has_temporal_split": False,
                })

        print(f"Creating {len(territory_data)} COL_Territory nodes...")
        session.run(
            "UNWIND $data AS d "
            "MERGE (t:COL_Territory {name: d.name}) "
            "SET t.colony_id = d.colony_id, "
            "    t.wikidata_id = d.wikidata_id, "
            "    t.canonical_name_kg = d.canonical_name_kg, "
            "    t.has_temporal_split = d.has_temporal_split",
            data=territory_data,
        )

        # --- COL_TerritoryYear nodes ---
        print("Creating COL_TerritoryYear nodes...")
        ty_batch = []
        maps_to_batch = []  # (ty_id, colony_id, confidence) for MAPS_TO edges

        for year, files in sorted(corpus.items()):
            if year_filter and year != year_filter:
                continue
            for filename, stem, canonical in files:
                if colony_filter and canonical not in colony_filter:
                    continue

                ty_id = f"{canonical}_{year}"
                cw_entry = crosswalk.get(canonical)

                # Resolve colony_id and wikidata_id for this specific year
                resolved_colony_id = None
                resolved_wikidata_id = None
                if cw_entry:
                    mappings = resolve_mapping(cw_entry, year)
                    if mappings:
                        # Use first mapping for node properties
                        resolved_colony_id = mappings[0]["colony_id"]
                        resolved_wikidata_id = mappings[0].get("wikidata_id")
                        # Track all MAPS_TO edges
                        for m in mappings:
                            if m.get("confidence") != "no_kg_node":
                                maps_to_batch.append({
                                    "ty_id": ty_id,
                                    "colony_id": m["colony_id"],
                                    "confidence": m.get("confidence", "verified"),
                                })
                    # Check if no_kg_node
                    if mappings and mappings[0].get("confidence") == "no_kg_node":
                        resolved_colony_id = None
                        resolved_wikidata_id = None

                ty_batch.append({
                    "id": ty_id,
                    "name": canonical,
                    "year": year,
                    "source_file": f"{year}_manual_parsed/{filename}",
                    "colony_id": resolved_colony_id,
                    "wikidata_id": resolved_wikidata_id,
                    "stage1_loaded": False,
                })

        # Load TerritoryYear nodes in chunks
        chunk_size = 500
        for i in range(0, len(ty_batch), chunk_size):
            chunk = ty_batch[i:i + chunk_size]
            session.run(
                "UNWIND $records AS r "
                "MERGE (ty:COL_TerritoryYear {id: r.id}) "
                "SET ty.name = r.name, "
                "    ty.year = r.year, "
                "    ty.source_file = r.source_file, "
                "    ty.colony_id = r.colony_id, "
                "    ty.wikidata_id = r.wikidata_id, "
                "    ty.stage1_loaded = r.stage1_loaded "
                "WITH ty, r "
                "MATCH (y:COL_Year {value: r.year}) "
                "MERGE (ty)-[:IN_YEAR]->(y) "
                "WITH ty, r "
                "MATCH (t:COL_Territory {name: r.name}) "
                "MERGE (ty)-[:INSTANCE_OF]->(t)",
                records=chunk,
            )

        print(f"Created {len(ty_batch)} COL_TerritoryYear nodes")

        # --- CONTINUES_AS temporal chains ---
        print("Creating CONTINUES_AS temporal chains...")
        # Build territory→sorted years from the batch we just created
        territory_appearances = defaultdict(list)
        for rec in ty_batch:
            territory_appearances[rec["name"]].append(rec["year"])

        continues_count = 0
        for territory, appearances in territory_appearances.items():
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
                    pairs=pairs,
                )
                continues_count += len(pairs)

        print(f"Created {continues_count} CONTINUES_AS edges")

        # --- MAPS_TO edges to HistoricalTerritory ---
        print("Creating MAPS_TO edges to HistoricalTerritory...")
        maps_to_created = 0
        maps_to_missing = 0

        for i in range(0, len(maps_to_batch), chunk_size):
            chunk = maps_to_batch[i:i + chunk_size]
            result = session.run(
                "UNWIND $edges AS e "
                "MATCH (ty:COL_TerritoryYear {id: e.ty_id}) "
                "MATCH (ht:HistoricalTerritory {colony_id: e.colony_id}) "
                "MERGE (ty)-[r:MAPS_TO]->(ht) "
                "ON CREATE SET r.source = 'col_kg_crosswalk', "
                "             r.confidence = e.confidence "
                "RETURN count(r) AS created",
                edges=chunk,
            )
            maps_to_created += result.single()["created"]

        # Count how many TerritoryYears have no MAPS_TO edge (expected for no_kg_node)
        result = session.run(
            "MATCH (ty:COL_TerritoryYear) "
            "WHERE NOT (ty)-[:MAPS_TO]->() "
            "RETURN count(ty) AS c"
        )
        maps_to_missing = result.single()["c"]

        print(f"Created {maps_to_created} MAPS_TO edges "
              f"({maps_to_missing} TerritoryYear nodes without MAPS_TO)")

    return len(ty_batch)


# =============================================================================
# PERSON RECORD LOADING (reuses col_load_neo4j queries)
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
SET ty.stage1_loaded = true,
    ty.stage1_count = $count,
    ty.stage1_date = $today,
    ty.stage1_file = $extraction_file
"""

CLEAR_TY_RECORDS_QUERY = """
MATCH (ty:COL_TerritoryYear {id: $ty_id})
OPTIONAL MATCH (pr:COL_PersonRecord)-[:SERVED_IN]->(ty)
OPTIONAL MATCH (ii:COL_InstitutionInstance)-[:DEPARTMENT_OF]->(ty)
DETACH DELETE pr, ii
SET ty.stage1_loaded = null, ty.stage1_count = null,
    ty.stage1_date = null, ty.stage1_file = null
RETURN count(pr) AS pr_deleted, count(ii) AS ii_deleted
"""


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def clear_territory_year_records(session, ty_id):
    """Delete all PersonRecords and InstitutionInstances for a TerritoryYear.

    Returns (pr_deleted, ii_deleted) counts.
    """
    # Delete in two passes to avoid cartesian product in OPTIONAL MATCH
    r1 = session.run(
        "MATCH (pr:COL_PersonRecord)-[:SERVED_IN]->(ty:COL_TerritoryYear {id: $ty_id}) "
        "DETACH DELETE pr RETURN count(pr) AS c",
        ty_id=ty_id,
    ).single()
    r2 = session.run(
        "MATCH (ii:COL_InstitutionInstance)-[:DEPARTMENT_OF]->(ty:COL_TerritoryYear {id: $ty_id}) "
        "DETACH DELETE ii RETURN count(ii) AS c",
        ty_id=ty_id,
    ).single()
    session.run(
        "MATCH (ty:COL_TerritoryYear {id: $ty_id}) "
        "SET ty.stage1_loaded = null, ty.stage1_count = null, "
        "    ty.stage1_date = null, ty.stage1_file = null",
        ty_id=ty_id,
    )
    return r1["c"], r2["c"]


def load_file(session, person_records, dept_records, ty_id, year, today_str,
              extraction_file=""):
    """Load one extraction file's records into Neo4j."""
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

        tx.run(MARK_LOADED_QUERY, ty_id=ty_id, count=len(person_records),
               today=today_str, extraction_file=extraction_file)
        tx.commit()
        return True
    except Exception as e:
        tx.rollback()
        raise e


def load_person_records(driver, year_filter=None,
                        colony_filter: list[str] | None = None, force=False):
    """Discover and load extraction files into Neo4j.

    If force=True, already-loaded colony-years are cleared and reloaded
    from the current extraction files (for updating with better extractions).
    """
    # Discover files (apply filters one at a time since discover_extraction_files
    # takes single colony, not list)
    all_files = []
    if colony_filter:
        for colony in colony_filter:
            all_files.extend(discover_extraction_files(
                year_filter=year_filter, colony_filter=colony,
            ))
    else:
        all_files = discover_extraction_files(year_filter=year_filter)

    print(f"\nFound {len(all_files)} extraction file(s)")
    if not all_files:
        print("Nothing to load.")
        return

    # Group by year for display
    by_year = defaultdict(list)
    for f in all_files:
        by_year[f["year"]].append(f["canonical_name"])
    for year in sorted(by_year):
        colonies = sorted(by_year[year])
        print(f"  {year}: {len(colonies)} colonies")

    with driver.session() as session:
        loaded_tys = {r["id"] for r in session.run(
            "MATCH (ty:COL_TerritoryYear) WHERE ty.stage1_loaded = true RETURN ty.id AS id"
        )}
        existing_tys = {r["id"] for r in session.run(
            "MATCH (ty:COL_TerritoryYear) RETURN ty.id AS id"
        )}

    today_str = date.today().isoformat()
    stats = {
        "loaded": 0, "reloaded": 0, "skipped_already": 0,
        "skipped_no_scaffold": 0,
        "errors": 0, "total_officials": 0, "total_depts": 0,
    }
    force_cleared = set()

    for f in all_files:
        ty_id = f["ty_id"]
        colony = f["canonical_name"]
        year = f["year"]

        if ty_id in loaded_tys:
            if not force:
                stats["skipped_already"] += 1
                continue
            # Force reload: clear existing records first
            with driver.session() as session:
                pr_del, ii_del = clear_territory_year_records(session, ty_id)
            loaded_tys.discard(ty_id)
            force_cleared.add(ty_id)
            print(f"  CLEARED: {colony} {year} "
                  f"({pr_del} persons, {ii_del} departments)")

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
            data, f["colony_stem"], colony, year, extraction_file,
        )

        if not person_records:
            print(f"  SKIP (no officials): {colony} {year}")
            continue

        try:
            was_reload = ty_id in force_cleared
            with driver.session() as session:
                load_file(session, person_records, dept_records,
                          ty_id, year, today_str,
                          extraction_file=extraction_file)

            loaded_tys.add(ty_id)
            if was_reload:
                stats["reloaded"] += 1
            else:
                stats["loaded"] += 1
            stats["total_officials"] += len(person_records)
            stats["total_depts"] += len(dept_records)
            action = "RELOADED" if was_reload else "LOADED"
            print(f"  {action}: {colony} {year} -- "
                  f"{len(person_records)} officials, "
                  f"{len(dept_records)} departments")
        except Exception as e:
            print(f"  ERROR loading {colony} {year}: {e}")
            stats["errors"] += 1

    print("\n" + "-" * 60)
    print("LOADING SUMMARY")
    print("-" * 60)
    print(f"  Files loaded (new):          {stats['loaded']}")
    print(f"  Files reloaded (--force):    {stats['reloaded']}")
    print(f"  Skipped (already loaded):    {stats['skipped_already']}")
    print(f"  Skipped (no scaffold):       {stats['skipped_no_scaffold']}")
    print(f"  Errors:                      {stats['errors']}")
    print(f"  Total officials loaded:      {stats['total_officials']}")
    print(f"  Total departments loaded:    {stats['total_depts']}")

    return stats


# =============================================================================
# STATS / CLEAR
# =============================================================================

def print_stats(driver):
    """Report on current COL graph contents."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("COL KNOWLEDGE GRAPH STATISTICS")
        print("=" * 60)

        # Scaffold counts
        print("\n  Scaffold:")
        for label, display in [
            ("COL_Year", "COL_Year nodes"),
            ("COL_Territory", "COL_Territory nodes"),
            ("COL_TerritoryYear", "COL_TerritoryYear nodes"),
        ]:
            r = session.run(f"MATCH (n:{label}) RETURN count(n) AS c").single()
            print(f"    {display:<35} {r['c']}")

        # MAPS_TO
        r = session.run(
            "MATCH (:COL_TerritoryYear)-[r:MAPS_TO]->(:HistoricalTerritory) "
            "RETURN count(r) AS c"
        ).single()
        print(f"    {'MAPS_TO edges':<35} {r['c']}")

        r = session.run(
            "MATCH (ty:COL_TerritoryYear) WHERE NOT (ty)-[:MAPS_TO]->() "
            "RETURN count(ty) AS c"
        ).single()
        print(f"    {'TerritoryYears without MAPS_TO':<35} {r['c']}")

        # CONTINUES_AS
        r = session.run(
            "MATCH ()-[r:CONTINUES_AS]->() RETURN count(r) AS c"
        ).single()
        print(f"    {'CONTINUES_AS edges':<35} {r['c']}")

        # Stage 1 data
        r = session.run("MATCH (pr:COL_PersonRecord) RETURN count(pr) AS c").single()
        pr_count = r['c']
        print(f"\n  Person records:")
        print(f"    {'COL_PersonRecord nodes':<35} {pr_count}")
        r = session.run(
            "MATCH (ii:COL_InstitutionInstance) RETURN count(ii) AS c"
        ).single()
        print(f"    {'COL_InstitutionInstance nodes':<35} {r['c']}")

        # Edges
        for edge_label, src, dst in [
            ("SERVED_IN", "COL_PersonRecord", "COL_TerritoryYear"),
            ("IN_DEPARTMENT", "COL_PersonRecord", "COL_InstitutionInstance"),
            ("DEPARTMENT_OF", "COL_InstitutionInstance", "COL_TerritoryYear"),
        ]:
            r = session.run(
                f"MATCH (:{src})-[r:{edge_label}]->(:{dst}) RETURN count(r) AS c"
            ).single()
            print(f"    {edge_label + ' edges':<35} {r['c']}")

        # Loading progress
        r = session.run(
            "MATCH (ty:COL_TerritoryYear) WHERE ty.stage1_loaded = true "
            "RETURN count(ty) AS loaded, sum(ty.stage1_count) AS officials"
        ).single()
        loaded = r['loaded']
        officials = r['officials'] or 0
        r2 = session.run(
            "MATCH (ty:COL_TerritoryYear) RETURN count(ty) AS total"
        ).single()
        total_ty = r2['total']

        print(f"\n  Loading progress:")
        if total_ty:
            print(f"    TerritoryYears loaded: {loaded} / {total_ty} "
                  f"({100*loaded/total_ty:.1f}%)")
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


def clear_all_col(driver):
    """Remove ALL COL_ nodes and edges. Safe for shared database."""
    with driver.session() as session:
        print("Clearing all COL_ data...")

        for label in ["COL_PersonRecord", "COL_InstitutionInstance",
                       "COL_TerritoryYear", "COL_Territory", "COL_Year"]:
            r = session.run(
                f"MATCH (n:{label}) DETACH DELETE n RETURN count(n) AS c"
            ).single()
            print(f"  Deleted {r['c']} {label} nodes")

        print("All COL_ data cleared.")


# =============================================================================
# DRY RUN REPORT
# =============================================================================

def dry_run_report(corpus, inventory, crosswalk, colony_filter, year_filter):
    """Preview what would be created without connecting to Neo4j."""
    print("\n" + "=" * 60)
    print("[DRY RUN] PREVIEW")
    print("=" * 60)

    # Filter territories if needed
    territories = list(inventory["territories"].keys())
    if colony_filter:
        territories = [t for t in territories if t in colony_filter]

    # Count TerritoryYear nodes
    ty_count = 0
    maps_to_count = 0
    no_maps_to_count = 0
    no_crosswalk_count = 0

    for year, files in sorted(corpus.items()):
        if year_filter and year != year_filter:
            continue
        for filename, stem, canonical in files:
            if colony_filter and canonical not in colony_filter:
                continue
            ty_count += 1

            cw_entry = crosswalk.get(canonical)
            if not cw_entry:
                no_crosswalk_count += 1
                no_maps_to_count += 1
                continue

            mappings = resolve_mapping(cw_entry, year)
            if not mappings:
                no_maps_to_count += 1
            else:
                for m in mappings:
                    if m.get("confidence") != "no_kg_node":
                        maps_to_count += 1
                    else:
                        no_maps_to_count += 1

    print(f"\n  Scaffold:")
    print(f"    COL_Year nodes:          {len(inventory['years'])}")
    print(f"    COL_Territory nodes:     {len(territories)}")
    print(f"    COL_TerritoryYear nodes: {ty_count}")
    print(f"    MAPS_TO edges:           {maps_to_count}")
    print(f"    Without MAPS_TO:         {no_maps_to_count}")
    if no_crosswalk_count:
        print(f"    No crosswalk entry:      {no_crosswalk_count}")

    # Preview extraction files
    all_files = []
    if colony_filter:
        for colony in colony_filter:
            all_files.extend(discover_extraction_files(
                year_filter=year_filter, colony_filter=colony,
            ))
    else:
        all_files = discover_extraction_files(year_filter=year_filter)

    total_officials = 0
    total_depts = 0
    for f in all_files:
        try:
            with open(f["path"]) as fh:
                data = json.load(fh)
            total_officials += len(data.get("officials", []))
            depts = {o.get("department") for o in data.get("officials", [])
                     if o.get("department")}
            total_depts += len(depts)
        except Exception:
            pass

    print(f"\n  Person records:")
    print(f"    Extraction files:        {len(all_files)}")
    print(f"    Total officials:         {total_officials}")
    print(f"    Total departments:       {total_depts}")

    print("\n[DRY RUN] No data loaded.")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Build COL Knowledge Graph (unified scaffold + loader)"
    )
    parser.add_argument("--scaffold-only", action="store_true",
                        help="Build scaffold only, skip person records")
    parser.add_argument("--load-only", action="store_true",
                        help="Load person records only (scaffold must exist)")
    parser.add_argument("--colony", action="append", type=str,
                        help="Filter to specific colony (can repeat)")
    parser.add_argument("--year", type=int,
                        help="Filter to specific year")
    parser.add_argument("--force", action="store_true",
                        help="Reload already-loaded colony-years (clears old records first)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without touching Neo4j")
    parser.add_argument("--clear", action="store_true",
                        help="Remove all COL_ nodes and edges")
    parser.add_argument("--stats", action="store_true",
                        help="Report current COL graph state")
    args = parser.parse_args()

    print("=" * 60)
    print("COL KNOWLEDGE GRAPH BUILDER")
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

    # --- Load crosswalk ---
    print(f"\nLoading crosswalk: {CROSSWALK_PATH}")
    crosswalk = load_crosswalk()
    print(f"  {len(crosswalk)} colony entries")

    # --- Scan corpus ---
    print(f"Scanning corpus: {REPO_DIR}")
    corpus = scan_corpus(REPO_DIR)
    inventory = build_inventory(corpus)
    print(f"  {inventory['total_year_dirs']} year dirs, "
          f"{inventory['total_territories']} territories, "
          f"{inventory['total_territory_years']} territory-years")

    # --- Dry run ---
    if args.dry_run:
        dry_run_report(corpus, inventory, crosswalk, args.colony, args.year)
        return

    # --- Connect to Neo4j ---
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        # --- Clear if requested ---
        if args.clear:
            clear_all_col(driver)

        # --- Scaffold ---
        if not args.load_only:
            print("\n--- SCAFFOLD ---")
            load_scaffold(driver, corpus, inventory, crosswalk,
                          colony_filter=args.colony,
                          year_filter=args.year)

        # --- Person records ---
        if not args.scaffold_only:
            print("\n--- PERSON RECORDS ---")
            load_person_records(driver,
                                year_filter=args.year,
                                colony_filter=args.colony,
                                force=args.force)

        # --- Final stats ---
        print_stats(driver)

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()

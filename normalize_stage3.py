"""
Neo4j Stage 3: Normalization and Taxonomy
==========================================

Two-phase pipeline:
  Phase A — Generate taxonomy (read-only, no Neo4j writes)
  Phase B — Load approved taxonomy into Neo4j

Usage:
    # Phase A: Extract raw names from Neo4j and cluster with rules
    python normalize_stage3.py extract

    # Phase A: Run LLM clustering on unclustered items
    python normalize_stage3.py cluster --api-key KEY
    python normalize_stage3.py cluster --dry-run

    # Phase A: Merge rule + LLM clusters into final taxonomy files
    python normalize_stage3.py merge

    # Phase B: Load approved taxonomy into Neo4j
    python normalize_stage3.py load

    # Verify loaded data
    python normalize_stage3.py verify

    # Show current status
    python normalize_stage3.py status

Requires:
    pip install neo4j google-genai
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

from load_neo4j import slugify
from normalize_rules import (
    cluster_departments,
    cluster_positions,
)


# =============================================================================
# CONFIGURATION
# =============================================================================

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "colonial_office")

REPO_DIR = Path(__file__).parent
TAXONOMY_DIR = REPO_DIR / "taxonomy"
GENERATED_DIR = REPO_DIR / "generated"

PIPELINE_VERSION = "3.0"
BATCH_SIZE = 500

# Confidence score mapping
CONFIDENCE_SCORES = {
    ("rule", "HIGH"): 0.98,
    ("rule", "MEDIUM"): 0.85,
    ("llm_assisted", "HIGH"): 0.90,
    ("llm_assisted", "MEDIUM"): 0.75,
    ("llm_assisted", "LOW"): 0.55,
    ("human_reviewed", None): 0.99,
}


def get_confidence_score(method: str, level: str) -> float:
    """Look up numeric confidence score from method + level."""
    return CONFIDENCE_SCORES.get((method, level), 0.70)


# =============================================================================
# PHASE A: EXTRACT — Pull raw names from Neo4j
# =============================================================================

EXTRACT_DEPTS_QUERY = """
MATCH (ii:InstitutionInstance)
RETURN ii.name_raw AS raw_name, count(*) AS instance_count,
       collect(DISTINCT ii.colony) AS colonies,
       collect(DISTINCT ii.year) AS years
ORDER BY instance_count DESC
"""

EXTRACT_POSITIONS_QUERY = """
MATCH (pr:PersonRecord) WHERE pr.position_raw IS NOT NULL AND pr.position_raw <> ''
RETURN pr.position_raw AS raw_position, count(*) AS record_count,
       collect(DISTINCT pr.department_raw) AS departments,
       collect(DISTINCT pr.colony) AS colonies
ORDER BY record_count DESC
"""


def extract_from_neo4j(driver) -> tuple[dict[str, int], dict[str, int]]:
    """Extract distinct department and position names from Neo4j.

    Returns (dept_counts, pos_counts).
    """
    dept_counts = {}
    pos_counts = {}

    with driver.session() as session:
        print("Extracting department names from InstitutionInstance nodes...")
        result = session.run(EXTRACT_DEPTS_QUERY)
        for record in result:
            name = record["raw_name"]
            if name and name.strip():
                dept_counts[name.strip()] = record["instance_count"]
        print(f"  Found {len(dept_counts)} distinct department names")

        print("Extracting position titles from PersonRecord nodes...")
        result = session.run(EXTRACT_POSITIONS_QUERY)
        for record in result:
            pos = record["raw_position"]
            if pos and pos.strip():
                pos_counts[pos.strip()] = record["record_count"]
        print(f"  Found {len(pos_counts)} distinct position titles")

    return dept_counts, pos_counts


def extract_from_files() -> tuple[dict[str, int], dict[str, int]]:
    """Fallback: extract from generated JSON files if Neo4j is unavailable."""
    dept_counts = defaultdict(int)
    pos_counts = defaultdict(int)

    for f in sorted(GENERATED_DIR.glob("*_data_*.json")):
        try:
            data = json.load(open(f))
            for o in data.get("officials", []):
                d = o.get("department")
                p = o.get("position")
                if d and d.strip():
                    dept_counts[d.strip()] += 1
                if p and p.strip():
                    pos_counts[p.strip()] += 1
        except Exception:
            pass

    return dict(dept_counts), dict(pos_counts)


def cmd_extract(args):
    """Phase A Step 1: Extract and rule-cluster."""
    print("=" * 60)
    print("PHASE A: EXTRACT AND RULE-CLUSTER")
    print("=" * 60)

    # Try Neo4j first, fall back to files
    dept_counts = None
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        driver.verify_connectivity()
        dept_counts, pos_counts = extract_from_neo4j(driver)
        driver.close()
    except Exception as e:
        print(f"Neo4j unavailable ({e}), falling back to file scan...")

    if dept_counts is None:
        dept_counts, pos_counts = extract_from_files()
        print(f"Scanned files: {len(dept_counts)} departments, {len(pos_counts)} positions")

    # Apply rule-based clustering
    print("\nApplying rule-based clustering...")
    dept_clusters, dept_unclustered = cluster_departments(dept_counts)
    pos_clusters, pos_unclustered = cluster_positions(pos_counts)

    total_dept_inst = sum(dept_counts.values())
    total_pos_inst = sum(pos_counts.values())
    claimed_dept_inst = sum(m["count"] for c in dept_clusters for m in c["members"])
    claimed_pos_inst = sum(m["count"] for c in pos_clusters for m in c["members"])

    print(f"\nDepartments: {len(dept_clusters)} clusters, "
          f"{claimed_dept_inst}/{total_dept_inst} instances ({100*claimed_dept_inst/total_dept_inst:.1f}%)")
    print(f"Positions:   {len(pos_clusters)} clusters, "
          f"{claimed_pos_inst}/{total_pos_inst} instances ({100*claimed_pos_inst/total_pos_inst:.1f}%)")
    print(f"Unclustered: {len(dept_unclustered)} departments, {len(pos_unclustered)} positions")

    # Save intermediate files for LLM step
    TAXONOMY_DIR.mkdir(parents=True, exist_ok=True)

    dept_output = {
        "pre_clustered": dept_clusters,
        "unclustered": dept_unclustered,
        "stats": {
            "total_distinct": len(dept_counts),
            "total_instances": total_dept_inst,
            "rule_clusters": len(dept_clusters),
            "rule_claimed_instances": claimed_dept_inst,
        },
    }
    dept_path = TAXONOMY_DIR / "department_unclustered.json"
    with open(dept_path, "w") as f:
        json.dump(dept_output, f, indent=2)
    print(f"\nSaved: {dept_path}")

    pos_output = {
        "pre_clustered": pos_clusters,
        "unclustered": pos_unclustered,
        "stats": {
            "total_distinct": len(pos_counts),
            "total_instances": total_pos_inst,
            "rule_clusters": len(pos_clusters),
            "rule_claimed_instances": claimed_pos_inst,
        },
    }
    pos_path = TAXONOMY_DIR / "position_unclustered.json"
    with open(pos_path, "w") as f:
        json.dump(pos_output, f, indent=2)
    print(f"Saved: {pos_path}")

    # Estimate LLM token load
    dept_chars = sum(len(u["raw"]) + 20 for u in dept_unclustered)
    pos_chars = sum(len(u.get("raw", "")) + 20 for u in pos_unclustered)
    est_tokens = (dept_chars + pos_chars) // 4 + 3000
    print(f"\nEstimated LLM input: ~{est_tokens:,} tokens")
    print(f"\nNext step: python normalize_stage3.py cluster [--api-key KEY]")


# =============================================================================
# PHASE A: CLUSTER — Run LLM clustering
# =============================================================================

def cmd_cluster(args):
    """Phase A Step 2: LLM-assisted clustering."""
    print("=" * 60)
    print("PHASE A: LLM-ASSISTED CLUSTERING")
    print("=" * 60)

    # Import here to avoid requiring google-genai for non-LLM operations
    from normalize_llm import (
        cluster_departments_llm,
        cluster_positions_llm,
        save_llm_clusters,
    )
    from google import genai

    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")
    if not api_key and not args.dry_run:
        print("ERROR: No API key. Set GEMINI_API_KEY or use --api-key")
        sys.exit(1)

    client = None
    if not args.dry_run:
        client = genai.Client(api_key=api_key)

    # Process departments
    dept_path = TAXONOMY_DIR / "department_unclustered.json"
    if dept_path.exists():
        with open(dept_path) as f:
            dept_data = json.load(f)
        pre_clustered = dept_data.get("pre_clustered", [])
        unclustered = dept_data.get("unclustered", [])
        print(f"\nDepartments: {len(unclustered)} unclustered items")

        dept_clusters = cluster_departments_llm(
            client, unclustered, pre_clustered, dry_run=args.dry_run
        )
        if not args.dry_run:
            save_llm_clusters(dept_clusters,
                              TAXONOMY_DIR / "department_llm_clusters.json")
    else:
        print(f"WARNING: {dept_path} not found. Run 'extract' first.")

    # Process positions
    pos_path = TAXONOMY_DIR / "position_unclustered.json"
    if pos_path.exists():
        with open(pos_path) as f:
            pos_data = json.load(f)
        pre_clustered = pos_data.get("pre_clustered", [])
        unclustered = pos_data.get("unclustered", [])
        print(f"\nPositions: {len(unclustered)} unclustered items")

        pos_clusters = cluster_positions_llm(
            client, unclustered, pre_clustered, dry_run=args.dry_run
        )
        if not args.dry_run:
            save_llm_clusters(pos_clusters,
                              TAXONOMY_DIR / "position_llm_clusters.json")
    else:
        print(f"WARNING: {pos_path} not found. Run 'extract' first.")

    if not args.dry_run:
        print(f"\nNext step: python normalize_stage3.py merge")


# =============================================================================
# PHASE A: MERGE — Combine rule + LLM clusters into taxonomy files
# =============================================================================

def cmd_merge(args):
    """Phase A Step 3: Merge rule and LLM clusters into review-ready taxonomy."""
    print("=" * 60)
    print("PHASE A: MERGE INTO TAXONOMY")
    print("=" * 60)

    today_str = date.today().isoformat()

    # --- Department taxonomy ---
    dept_path = TAXONOMY_DIR / "department_unclustered.json"
    dept_llm_path = TAXONOMY_DIR / "department_llm_clusters.json"

    if not dept_path.exists():
        print(f"ERROR: {dept_path} not found. Run 'extract' first.")
        sys.exit(1)

    with open(dept_path) as f:
        dept_data = json.load(f)

    rule_clusters = dept_data["pre_clustered"]
    all_unclustered = dept_data["unclustered"]

    # Load LLM clusters if available
    llm_clusters = []
    if dept_llm_path.exists():
        with open(dept_llm_path) as f:
            llm_data = json.load(f)
        llm_clusters = llm_data.get("clusters", [])
        print(f"LLM department clusters: {len(llm_clusters)}")

    # Track which unclustered items got claimed by LLM
    llm_claimed = set()
    for c in llm_clusters:
        for member in c.get("members", []):
            llm_claimed.add(member)

    # Build final institution types
    institution_types = []
    for c in rule_clusters:
        itype = {
            "id": c["id"],
            "uri": f"col:itype/{slugify(c['canonical_name'])}",
            "canonical_name": c["canonical_name"],
            "members": c["members"],
            "career_track": c.get("career_track"),
            "reviewer_decision": None,
        }
        institution_types.append(itype)

    for i, c in enumerate(llm_clusters):
        itype_id = f"dept_llm_{i}"
        members = []
        for raw_name in c.get("members", []):
            # Find the count from unclustered list
            count = 0
            for u in all_unclustered:
                if u["raw"] == raw_name:
                    count = u["count"]
                    break
            members.append({
                "raw": raw_name,
                "count": count,
                "confidence": c.get("confidence", "MEDIUM"),
                "method": "llm_assisted",
            })
        itype = {
            "id": itype_id,
            "uri": f"col:itype/{slugify(c['canonical_name'])}",
            "canonical_name": c["canonical_name"],
            "members": members,
            "career_track": c.get("career_track"),
            "reviewer_decision": None,
        }
        institution_types.append(itype)

    # Remaining unclustered
    still_unclustered = [
        u for u in all_unclustered if u["raw"] not in llm_claimed
    ]

    dept_taxonomy = {
        "version": "0.1",
        "generated": today_str,
        "status": "DRAFT",
        "institution_types": institution_types,
        "unclustered": still_unclustered,
        "stats": dept_data.get("stats", {}),
    }

    dept_tax_path = TAXONOMY_DIR / "department_taxonomy.json"
    with open(dept_tax_path, "w") as f:
        json.dump(dept_taxonomy, f, indent=2)
    print(f"Saved: {dept_tax_path} ({len(institution_types)} types, "
          f"{len(still_unclustered)} unclustered)")

    # --- Position taxonomy ---
    pos_path = TAXONOMY_DIR / "position_unclustered.json"
    pos_llm_path = TAXONOMY_DIR / "position_llm_clusters.json"

    if not pos_path.exists():
        print(f"ERROR: {pos_path} not found. Run 'extract' first.")
        sys.exit(1)

    with open(pos_path) as f:
        pos_data = json.load(f)

    rule_clusters = pos_data["pre_clustered"]
    all_unclustered = pos_data["unclustered"]

    llm_clusters = []
    if pos_llm_path.exists():
        with open(pos_llm_path) as f:
            llm_data = json.load(f)
        llm_clusters = llm_data.get("clusters", [])
        print(f"LLM position clusters: {len(llm_clusters)}")

    llm_claimed = set()
    for c in llm_clusters:
        for member in c.get("members", []):
            llm_claimed.add(member)

    position_types = []
    for c in rule_clusters:
        ptype = {
            "id": c["id"],
            "uri": f"col:ptype/{slugify(c['canonical_name'])}",
            "canonical_name": c["canonical_name"],
            "members": c["members"],
            "career_track": c.get("career_track"),
            "grade_level": c.get("grade_level"),
            "reviewer_decision": None,
        }
        position_types.append(ptype)

    for i, c in enumerate(llm_clusters):
        ptype_id = f"pos_llm_{i}"
        members = []
        for raw_name in c.get("members", []):
            count = 0
            for u in all_unclustered:
                if u["raw"] == raw_name:
                    count = u["count"]
                    break
            members.append({
                "raw": raw_name,
                "count": count,
                "confidence": c.get("confidence", "MEDIUM"),
                "method": "llm_assisted",
            })
        ptype = {
            "id": ptype_id,
            "uri": f"col:ptype/{slugify(c['canonical_name'])}",
            "canonical_name": c["canonical_name"],
            "members": members,
            "career_track": c.get("career_track"),
            "grade_level": c.get("grade_level"),
            "reviewer_decision": None,
        }
        position_types.append(ptype)

    still_unclustered = [
        u for u in all_unclustered if u["raw"] not in llm_claimed
    ]

    pos_taxonomy = {
        "version": "0.1",
        "generated": today_str,
        "status": "DRAFT",
        "position_types": position_types,
        "unclustered": still_unclustered,
        "stats": pos_data.get("stats", {}),
    }

    pos_tax_path = TAXONOMY_DIR / "position_taxonomy.json"
    with open(pos_tax_path, "w") as f:
        json.dump(pos_taxonomy, f, indent=2)
    print(f"Saved: {pos_tax_path} ({len(position_types)} types, "
          f"{len(still_unclustered)} unclustered)")

    print(f"\nNext step: Graduate students review taxonomy JSON files.")
    print(f"  See: taxonomy/REVIEW_GUIDE.md")
    print(f"  Then: python normalize_stage3.py load")


# =============================================================================
# PHASE B: LOAD — Write approved taxonomy into Neo4j
# =============================================================================

STAGE3_SCHEMA = [
    "CREATE CONSTRAINT itype_uri IF NOT EXISTS FOR (it:InstitutionType) REQUIRE it.uri IS UNIQUE",
    "CREATE CONSTRAINT ptype_uri IF NOT EXISTS FOR (pt:PositionType) REQUIRE pt.uri IS UNIQUE",
    "CREATE CONSTRAINT ctrack_uri IF NOT EXISTS FOR (ct:CareerTrack) REQUIRE ct.uri IS UNIQUE",
    "CREATE INDEX itype_name IF NOT EXISTS FOR (it:InstitutionType) ON (it.canonical_name)",
    "CREATE INDEX ptype_name IF NOT EXISTS FOR (pt:PositionType) ON (pt.canonical_name)",
    "CREATE INDEX ctrack_name IF NOT EXISTS FOR (ct:CareerTrack) ON (ct.name)",
]

CAREER_TRACK_QUERY = """
UNWIND $tracks AS t
MERGE (ct:CareerTrack {uri: t.uri})
ON CREATE SET ct.name = t.name, ct.description = t.description
"""

INSTITUTION_TYPE_QUERY = """
UNWIND $batch AS it
MERGE (node:InstitutionType {uri: it.uri})
ON CREATE SET node.canonical_name = it.canonical_name
"""

POSITION_TYPE_QUERY = """
UNWIND $batch AS pt
MERGE (node:PositionType {uri: pt.uri})
ON CREATE SET node.canonical_name = pt.canonical_name,
              node.grade_level = pt.grade_level
"""

TYPE_OF_QUERY = """
UNWIND $mappings AS m
MATCH (ii:InstitutionInstance) WHERE ii.name_raw IN m.members
MATCH (it:InstitutionType {uri: m.type_uri})
MERGE (ii)-[r:TYPE_OF]->(it)
ON CREATE SET r.method = m.method, r.confidence = m.confidence,
              r.pipeline_version = $pipeline_version, r.date_created = $today
"""

HAS_POSITION_QUERY = """
UNWIND $mappings AS m
MATCH (pr:PersonRecord) WHERE pr.position_raw IN m.members
MATCH (pt:PositionType {uri: m.type_uri})
MERGE (pr)-[r:HAS_POSITION]->(pt)
ON CREATE SET r.method = m.method, r.confidence = m.confidence,
              r.pipeline_version = $pipeline_version, r.date_created = $today
"""

BELONGS_TO_TRACK_QUERY = """
UNWIND $mappings AS m
MATCH (pt:PositionType {uri: m.type_uri})
MATCH (ct:CareerTrack {uri: m.track_uri})
MERGE (pt)-[r:BELONGS_TO_TRACK]->(ct)
ON CREATE SET r.method = m.method,
              r.pipeline_version = $pipeline_version, r.date_created = $today
"""

ITYPE_BELONGS_TO_TRACK_QUERY = """
UNWIND $mappings AS m
MATCH (it:InstitutionType {uri: m.type_uri})
MATCH (ct:CareerTrack {uri: m.track_uri})
MERGE (it)-[r:BELONGS_TO_TRACK]->(ct)
ON CREATE SET r.method = m.method,
              r.pipeline_version = $pipeline_version, r.date_created = $today
"""


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def cmd_load(args):
    """Phase B: Load approved taxonomy into Neo4j."""
    print("=" * 60)
    print("PHASE B: LOAD TAXONOMY INTO NEO4J")
    print("=" * 60)

    today_str = date.today().isoformat()

    # Load taxonomy files
    career_tracks_path = TAXONOMY_DIR / "career_tracks.json"
    dept_tax_path = TAXONOMY_DIR / "department_taxonomy.json"
    pos_tax_path = TAXONOMY_DIR / "position_taxonomy.json"

    if not career_tracks_path.exists():
        print(f"ERROR: {career_tracks_path} not found")
        sys.exit(1)

    with open(career_tracks_path) as f:
        career_data = json.load(f)

    dept_taxonomy = None
    if dept_tax_path.exists():
        with open(dept_tax_path) as f:
            dept_taxonomy = json.load(f)
        status = dept_taxonomy.get("status", "UNKNOWN")
        if status != "APPROVED" and not args.force:
            print(f"WARNING: Department taxonomy status is '{status}', not 'APPROVED'.")
            print(f"  Use --force to load anyway.")
            if not args.force:
                dept_taxonomy = None

    pos_taxonomy = None
    if pos_tax_path.exists():
        with open(pos_tax_path) as f:
            pos_taxonomy = json.load(f)
        status = pos_taxonomy.get("status", "UNKNOWN")
        if status != "APPROVED" and not args.force:
            print(f"WARNING: Position taxonomy status is '{status}', not 'APPROVED'.")
            print(f"  Use --force to load anyway.")
            if not args.force:
                pos_taxonomy = None

    if dept_taxonomy is None and pos_taxonomy is None:
        print("Nothing to load. Approve taxonomy files first (set status: 'APPROVED').")
        return

    # Connect to Neo4j
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        with driver.session() as session:
            # Schema
            print("Creating Stage 3 schema...")
            for stmt in STAGE3_SCHEMA:
                try:
                    session.run(stmt)
                except Exception as e:
                    if "already exists" not in str(e).lower() and "equivalent" not in str(e).lower():
                        print(f"  WARNING: {e}")

            # 1. CareerTrack nodes
            tracks = career_data["career_tracks"]
            print(f"\nLoading {len(tracks)} CareerTrack nodes...")
            session.run(CAREER_TRACK_QUERY, tracks=tracks)

            # Build track URI lookup
            track_uris = {t["name"]: t["uri"] for t in tracks}

            # 2. InstitutionType nodes + TYPE_OF edges
            if dept_taxonomy:
                itypes = dept_taxonomy.get("institution_types", [])
                print(f"\nLoading {len(itypes)} InstitutionType nodes...")

                itype_batch = [
                    {"uri": it["uri"], "canonical_name": it["canonical_name"]}
                    for it in itypes
                ]
                for batch in chunks(itype_batch, BATCH_SIZE):
                    session.run(INSTITUTION_TYPE_QUERY, batch=batch)

                # TYPE_OF edges
                print("Creating TYPE_OF edges...")
                type_of_mappings = []
                for it in itypes:
                    members = [m["raw"] for m in it["members"]]
                    if not members:
                        continue
                    # Use the highest confidence from members
                    methods = [m.get("method", "rule") for m in it["members"]]
                    confidences = [m.get("confidence", "HIGH") for m in it["members"]]
                    # Use most common method
                    method = max(set(methods), key=methods.count)
                    confidence = min(
                        get_confidence_score(m.get("method", "rule"), m.get("confidence", "HIGH"))
                        for m in it["members"]
                    )
                    type_of_mappings.append({
                        "members": members,
                        "type_uri": it["uri"],
                        "method": method,
                        "confidence": confidence,
                    })

                for batch in chunks(type_of_mappings, 50):
                    session.run(TYPE_OF_QUERY, mappings=batch,
                                pipeline_version=PIPELINE_VERSION, today=today_str)
                print(f"  Created TYPE_OF edges for {len(type_of_mappings)} types")

                # InstitutionType -> CareerTrack
                itype_track_mappings = []
                for it in itypes:
                    ct = it.get("career_track")
                    if ct and ct in track_uris:
                        method = "rule"
                        for m in it["members"]:
                            if m.get("method") == "llm_assisted":
                                method = "llm_assisted"
                                break
                        itype_track_mappings.append({
                            "type_uri": it["uri"],
                            "track_uri": track_uris[ct],
                            "method": method,
                        })

                if itype_track_mappings:
                    for batch in chunks(itype_track_mappings, BATCH_SIZE):
                        session.run(ITYPE_BELONGS_TO_TRACK_QUERY, mappings=batch,
                                    pipeline_version=PIPELINE_VERSION, today=today_str)
                    print(f"  Created BELONGS_TO_TRACK edges for {len(itype_track_mappings)} types")

            # 3. PositionType nodes + HAS_POSITION edges
            if pos_taxonomy:
                ptypes = pos_taxonomy.get("position_types", [])
                print(f"\nLoading {len(ptypes)} PositionType nodes...")

                ptype_batch = [
                    {"uri": pt["uri"],
                     "canonical_name": pt["canonical_name"],
                     "grade_level": pt.get("grade_level")}
                    for pt in ptypes
                ]
                for batch in chunks(ptype_batch, BATCH_SIZE):
                    session.run(POSITION_TYPE_QUERY, batch=batch)

                # HAS_POSITION edges
                print("Creating HAS_POSITION edges...")
                has_pos_mappings = []
                for pt in ptypes:
                    members = [m["raw"] for m in pt["members"]]
                    if not members:
                        continue
                    methods = [m.get("method", "rule") for m in pt["members"]]
                    method = max(set(methods), key=methods.count)
                    confidence = min(
                        get_confidence_score(m.get("method", "rule"), m.get("confidence", "HIGH"))
                        for m in pt["members"]
                    )
                    has_pos_mappings.append({
                        "members": members,
                        "type_uri": pt["uri"],
                        "method": method,
                        "confidence": confidence,
                    })

                for batch in chunks(has_pos_mappings, 50):
                    session.run(HAS_POSITION_QUERY, mappings=batch,
                                pipeline_version=PIPELINE_VERSION, today=today_str)
                print(f"  Created HAS_POSITION edges for {len(has_pos_mappings)} types")

                # PositionType -> CareerTrack
                ptype_track_mappings = []
                for pt in ptypes:
                    ct = pt.get("career_track")
                    if ct and ct in track_uris:
                        method = "rule"
                        for m in pt["members"]:
                            if m.get("method") == "llm_assisted":
                                method = "llm_assisted"
                                break
                        ptype_track_mappings.append({
                            "type_uri": pt["uri"],
                            "track_uri": track_uris[ct],
                            "method": method,
                        })

                if ptype_track_mappings:
                    for batch in chunks(ptype_track_mappings, BATCH_SIZE):
                        session.run(BELONGS_TO_TRACK_QUERY, mappings=batch,
                                    pipeline_version=PIPELINE_VERSION, today=today_str)
                    print(f"  Created BELONGS_TO_TRACK edges for {len(ptype_track_mappings)} types")

        print("\nPhase B loading complete.")
        cmd_verify_inner(driver)

    finally:
        driver.close()


# =============================================================================
# VERIFY
# =============================================================================

VERIFY_QUERIES = {
    "InstitutionType count": "MATCH (it:InstitutionType) RETURN count(it) AS c",
    "PositionType count": "MATCH (pt:PositionType) RETURN count(pt) AS c",
    "CareerTrack count": "MATCH (ct:CareerTrack) RETURN count(ct) AS c",
    "TYPE_OF edges": "MATCH ()-[r:TYPE_OF]->() RETURN count(r) AS c",
    "HAS_POSITION edges": "MATCH ()-[r:HAS_POSITION]->() RETURN count(r) AS c",
    "BELONGS_TO_TRACK edges": "MATCH ()-[r:BELONGS_TO_TRACK]->() RETURN count(r) AS c",
}

TYPE_OF_COVERAGE_QUERY = """
MATCH (ii:InstitutionInstance)
OPTIONAL MATCH (ii)-[:TYPE_OF]->(it:InstitutionType)
RETURN count(ii) AS total, count(it) AS typed,
       toFloat(count(it))/count(ii)*100 AS pct
"""

HAS_POSITION_COVERAGE_QUERY = """
MATCH (pr:PersonRecord) WHERE pr.position_raw IS NOT NULL AND pr.position_raw <> ''
OPTIONAL MATCH (pr)-[:HAS_POSITION]->(pt:PositionType)
RETURN count(pr) AS total, count(pt) AS typed,
       toFloat(count(pt))/count(pr)*100 AS pct
"""

CAREER_TRACK_DIST_QUERY = """
MATCH (pt:PositionType)-[:BELONGS_TO_TRACK]->(ct:CareerTrack)
RETURN ct.name AS track, count(pt) AS types
ORDER BY types DESC
"""

ARCHDEACON_TEST_QUERY = """
MATCH (pr:PersonRecord)
WHERE pr.position_raw CONTAINS 'Archdeacon'
OPTIONAL MATCH (pr)-[:IN_DEPARTMENT]->(ii)
OPTIONAL MATCH (pr)-[:HAS_POSITION]->(pt)-[:BELONGS_TO_TRACK]->(ct)
RETURN pr.canonical_name AS name, pr.position_raw AS position,
       pr.colony AS colony, pr.year AS year,
       ii.name_raw AS dept, ct.name AS track
LIMIT 5
"""


def cmd_verify_inner(driver):
    """Run verification queries."""
    print("\n" + "=" * 60)
    print("STAGE 3 VERIFICATION")
    print("=" * 60)

    with driver.session() as session:
        for label, query in VERIFY_QUERIES.items():
            r = session.run(query).single()
            print(f"  {label}: {r['c']}")

        # Coverage
        print("\n  TYPE_OF coverage:")
        r = session.run(TYPE_OF_COVERAGE_QUERY).single()
        print(f"    {r['typed']}/{r['total']} InstitutionInstances typed ({r['pct']:.1f}%)")

        print("\n  HAS_POSITION coverage:")
        r = session.run(HAS_POSITION_COVERAGE_QUERY).single()
        print(f"    {r['typed']}/{r['total']} PersonRecords with position type ({r['pct']:.1f}%)")

        print("\n  Career track distribution:")
        result = session.run(CAREER_TRACK_DIST_QUERY)
        for record in result:
            print(f"    {record['track']:<20} {record['types']:>4} position types")

        # Epistemological constraint test
        print("\n  Archdeacon test (epistemological constraint):")
        result = session.run(ARCHDEACON_TEST_QUERY)
        records = list(result)
        if records:
            for record in records:
                dept = record['dept'] or '(none)'
                track = record['track'] or '(none)'
                print(f"    {record['name']}, {record['colony']} {record['year']}: "
                      f"dept={dept}, track={track}")
        else:
            print("    No Archdeacon records found in current data")


def cmd_verify(args):
    """Run verification queries against Neo4j."""
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        driver.verify_connectivity()
        cmd_verify_inner(driver)
    finally:
        driver.close()


# =============================================================================
# STATUS
# =============================================================================

def cmd_status(args):
    """Show current Stage 3 status."""
    print("=" * 60)
    print("STAGE 3 STATUS")
    print("=" * 60)

    # Check taxonomy files
    files = {
        "career_tracks.json": TAXONOMY_DIR / "career_tracks.json",
        "department_unclustered.json": TAXONOMY_DIR / "department_unclustered.json",
        "position_unclustered.json": TAXONOMY_DIR / "position_unclustered.json",
        "department_llm_clusters.json": TAXONOMY_DIR / "department_llm_clusters.json",
        "position_llm_clusters.json": TAXONOMY_DIR / "position_llm_clusters.json",
        "department_taxonomy.json": TAXONOMY_DIR / "department_taxonomy.json",
        "position_taxonomy.json": TAXONOMY_DIR / "position_taxonomy.json",
    }

    print("\nTaxonomy files:")
    for name, path in files.items():
        if path.exists():
            size = path.stat().st_size
            # Try to read status
            status_str = ""
            try:
                with open(path) as f:
                    data = json.load(f)
                if "status" in data:
                    status_str = f" [{data['status']}]"
                if "stats" in data:
                    stats = data["stats"]
                    status_str += f" (rule: {stats.get('rule_clusters', '?')} clusters)"
            except Exception:
                pass
            print(f"  [OK] {name} ({size:,} bytes){status_str}")
        else:
            print(f"  [  ] {name}")

    # Check Neo4j
    print("\nNeo4j Stage 3:")
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        driver.verify_connectivity()
        with driver.session() as session:
            for label, query in VERIFY_QUERIES.items():
                r = session.run(query).single()
                print(f"  {label}: {r['c']}")
        driver.close()
    except Exception as e:
        print(f"  Neo4j unavailable: {e}")

    # Workflow guidance
    print("\nWorkflow:")
    extract_done = (TAXONOMY_DIR / "department_unclustered.json").exists()
    llm_done = (TAXONOMY_DIR / "department_llm_clusters.json").exists()
    merge_done = (TAXONOMY_DIR / "department_taxonomy.json").exists()

    steps = [
        ("extract", extract_done, "Extract from Neo4j + rule-cluster"),
        ("cluster", llm_done, "LLM-assisted clustering"),
        ("merge", merge_done, "Merge into taxonomy JSON"),
        ("(review)", False, "Graduate students review taxonomy"),
        ("load", False, "Load approved taxonomy into Neo4j"),
        ("verify", False, "Run verification queries"),
    ]
    for cmd, done, desc in steps:
        marker = "x" if done else " "
        print(f"  [{marker}] {cmd:<12} — {desc}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Neo4j Stage 3: Normalization and Taxonomy"
    )
    subparsers = parser.add_subparsers(dest="command", help="Pipeline phase")

    # extract
    p_extract = subparsers.add_parser("extract",
        help="Phase A: Extract raw names and apply rule-based clustering")

    # cluster
    p_cluster = subparsers.add_parser("cluster",
        help="Phase A: Run LLM-assisted clustering")
    p_cluster.add_argument("--api-key", help="Gemini API key")
    p_cluster.add_argument("--dry-run", action="store_true",
                           help="Show prompts without calling API")

    # merge
    p_merge = subparsers.add_parser("merge",
        help="Phase A: Merge rule + LLM clusters into taxonomy files")

    # load
    p_load = subparsers.add_parser("load",
        help="Phase B: Load approved taxonomy into Neo4j")
    p_load.add_argument("--force", action="store_true",
                        help="Load even if taxonomy status is not APPROVED")

    # verify
    p_verify = subparsers.add_parser("verify",
        help="Run verification queries on loaded data")

    # status
    p_status = subparsers.add_parser("status",
        help="Show current Stage 3 status")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    commands = {
        "extract": cmd_extract,
        "cluster": cmd_cluster,
        "merge": cmd_merge,
        "load": cmd_load,
        "verify": cmd_verify,
        "status": cmd_status,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()

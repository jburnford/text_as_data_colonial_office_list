#!/usr/bin/env python3
"""
COL Stage 4b: Person Node Builder
===================================

Creates COL_Person nodes from connected components of high-confidence
POSSIBLE_MATCH edges and Wikidata-verified SAME_AS anchors.

A COL_Person represents a single identified individual whose career
spans one or more COL_Official stints. Each stint is linked via
CAREER_STINT relationships.

Strategy:
  1. Find connected components in the POSSIBLE_MATCH graph where ALL
     edges have uncertainty < threshold (default 0.20)
  2. Wikidata-verified edges (SAME_AS) are automatically included
  3. Each component becomes one COL_Person
  4. Optionally expand with medium-confidence edges (0.20-0.40) that
     connect to existing verified components

Usage:
    python col_build_persons.py                  # full run
    python col_build_persons.py --dry-run        # preview, no writes
    python col_build_persons.py --stats          # report
    python col_build_persons.py --clear          # remove COL_Person nodes
    python col_build_persons.py --threshold 0.15 # stricter
    python col_build_persons.py --expand         # add medium-confidence edges
    python col_build_persons.py --expand --expand-threshold 0.35

Requires:
    pip install neo4j
"""

import argparse
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


# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
BATCH_SIZE = 500
DEFAULT_HIGH_THRESHOLD = 0.20    # max uncertainty for core components
DEFAULT_EXPAND_THRESHOLD = 0.40  # max uncertainty for expansion edges


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
# GRAPH QUERIES
# =============================================================================

# Fetch high-confidence edges (within + cross-colony)
FETCH_HIGH_CONFIDENCE_EDGES = """
MATCH (a:COL_Official)-[r:POSSIBLE_MATCH]-(b:COL_Official)
WHERE r.uncertainty < $threshold
  AND id(a) < id(b)
RETURN a.id AS a_id, b.id AS b_id, r.uncertainty AS uncertainty,
       r.verified_by AS verified_by
"""

# Fetch Wikidata-verified edges (automatically high confidence)
FETCH_WD_VERIFIED_EDGES = """
MATCH (a:COL_Official)-[r:POSSIBLE_MATCH]-(b:COL_Official)
WHERE r.verified_by = 'wikidata_cascade'
  AND id(a) < id(b)
RETURN a.id AS a_id, b.id AS b_id, r.uncertainty AS uncertainty,
       r.verified_by AS verified_by
"""

# Fetch SAME_AS anchors (officials → WD_Person)
FETCH_SAME_AS = """
MATCH (o:COL_Official)-[r:SAME_AS]->(w:WD_Person)
RETURN o.id AS official_id, w.qid AS wd_qid, w.name AS wd_name,
       r.confidence AS confidence
"""

# Fetch official details for person building
FETCH_OFFICIAL_DETAILS = """
UNWIND $ids AS oid
MATCH (o:COL_Official {id: oid})
RETURN o.id AS id, o.name AS name, o.colony AS colony,
       o.first_year AS first_year, o.last_year AS last_year,
       o.num_editions AS num_editions, o.editions AS editions
"""

# Medium-confidence edges for expansion
FETCH_MEDIUM_EDGES = """
MATCH (a:COL_Official)-[r:POSSIBLE_MATCH]-(b:COL_Official)
WHERE r.uncertainty >= $low AND r.uncertainty < $high
  AND id(a) < id(b)
RETURN a.id AS a_id, b.id AS b_id, r.uncertainty AS uncertainty,
       r.domain_match AS domain_match, r.name_specificity AS name_specificity
"""

# Check for simultaneous service (anti-pattern)
CHECK_OVERLAP = """
MATCH (a:COL_Official {id: $a_id}), (b:COL_Official {id: $b_id})
WHERE a.colony <> b.colony
RETURN
  CASE WHEN a.first_year <= b.last_year AND b.first_year <= a.last_year
       THEN true ELSE false END AS overlaps,
  a.colony AS a_colony, b.colony AS b_colony,
  a.first_year AS a_first, a.last_year AS a_last,
  b.first_year AS b_first, b.last_year AS b_last
"""


# =============================================================================
# QUARANTINE-BASED GHOST FILTERING
# =============================================================================

# Ghost detection is primarily handled by col_detect_ghosts.py, which sets
# pr.quarantined = true on PersonRecords. We filter officials whose
# PersonRecords are ALL quarantined, plus a secondary colony-confirmed
# ghost detection using WD_Person → ASSOCIATED_WITH → COL_Territory.

FULLY_QUARANTINED_QUERY = """
MATCH (o:COL_Official)
WHERE NOT EXISTS {
    MATCH (pr:COL_PersonRecord)-[:RECORD_OF]->(o)
    WHERE pr.quarantined IS NULL OR pr.quarantined <> true
}
RETURN o.id AS id
"""

COLONY_CONFIRMED_GHOST_QUERY = """
MATCH (w:WD_Person)
WHERE w.deathYear IS NOT NULL
WITH w, split(w.name, ' ') AS parts
WITH w, parts[-1] AS wd_surname
MATCH (o:COL_Official)
WHERE o.name STARTS WITH wd_surname + ','
  AND o.first_year > w.deathYear + 5
OPTIONAL MATCH (w)-[:ASSOCIATED_WITH]->(t:COL_Territory)
RETURN o.id AS official_id, o.name AS col_name, o.colony AS colony,
       o.first_year AS first_year, o.last_year AS last_year,
       w.name AS wd_name, w.deathYear AS death_year, w.qid AS qid,
       collect(DISTINCT t.name) AS wd_colonies
"""


def _wd_initials(wd_name: str) -> list[str]:
    """Extract initials from WD given names: 'Frederick Gordon' → ['F', 'G']."""
    parts = wd_name.strip().split()
    if len(parts) < 2:
        return []
    return [p[0].upper() for p in parts[:-1] if p and p[0].isalpha()]


def _col_initials(col_name: str) -> list[str]:
    """Extract initials from COL name: 'Guggisberg, F. Gordon' → ['F', 'G']."""
    parts = col_name.split(", ", 1)
    if len(parts) < 2:
        return []
    given = parts[1].strip()
    return [p[0].upper() for p in given.replace(".", " ").split() if p and p[0].isalpha()]


def _initials_compatible_wd(wd_inits: list[str], col_inits: list[str]) -> bool:
    """Check if WD initials are compatible with COL initials."""
    if not wd_inits or not col_inits:
        return False
    if wd_inits[0] == col_inits[0]:
        return True
    if set(wd_inits) & set(col_inits):
        return True
    return False


def detect_ghosts(session) -> tuple[set[str], list[dict]]:
    """Find ghost officials using quarantine flags + colony-confirmed WD detection.

    Two-tier approach:
    1. Officials with ALL PersonRecords quarantined (from col_detect_ghosts.py)
    2. Colony-confirmed ghost detection: WD_Person has ASSOCIATED_WITH → COL_Territory
       matching the COL_Official's colony → relax thresholds for ghost detection

    Returns (set of ghost official IDs, list of ghost details for reporting).
    """
    from col_link_officials import COMMON_SURNAMES

    # Tier 1: Fully quarantined officials (already flagged by col_detect_ghosts.py)
    result = session.run(FULLY_QUARANTINED_QUERY)
    quarantined_ids = {r["id"] for r in result}

    # Tier 2: Colony-confirmed ghost detection (catches officials missed by governor chain)
    result = session.run(COLONY_CONFIRMED_GHOST_QUERY)
    candidates = [dict(r) for r in result]

    ghost_ids = set(quarantined_ids)
    ghost_details = []

    for c in candidates:
        if c["official_id"] in ghost_ids:
            continue  # already flagged

        wd_inits = _wd_initials(c["wd_name"])
        col_inits = _col_initials(c["col_name"])

        if not _initials_compatible_wd(wd_inits, col_inits):
            continue

        matching_inits = len(set(wd_inits) & set(col_inits))
        surname = c["col_name"].split(",")[0].strip().lower()
        gap = c["first_year"] - c["death_year"]
        wd_colonies = c.get("wd_colonies") or []

        # Three-tier classification based on colony evidence
        colony_match = c["colony"] in wd_colonies if wd_colonies else None

        if colony_match is True:
            # Colony confirmed: WD person served in this colony — relax thresholds
            if matching_inits >= 1 and gap >= 8:
                ghost_ids.add(c["official_id"])
                ghost_details.append(c)
        elif colony_match is False:
            # Colony rejected: WD person has territories but NONE match
            # Different person — skip
            continue
        else:
            # No WD territory data: fall back to conservative heuristic
            if matching_inits >= 2 and surname not in COMMON_SURNAMES:
                ghost_ids.add(c["official_id"])
                ghost_details.append(c)
            elif matching_inits >= 2 and gap >= 15:
                ghost_ids.add(c["official_id"])
                ghost_details.append(c)
            elif matching_inits == 1 and surname not in COMMON_SURNAMES and gap >= 15:
                ghost_ids.add(c["official_id"])
                ghost_details.append(c)

    return ghost_ids, ghost_details


def print_ghost_report(ghost_details: list[dict], ghost_ids: set[str], quarantined_count: int = 0):
    """Print details of detected ghosts."""
    if quarantined_count:
        print(f"  {quarantined_count} officials fully quarantined (col_detect_ghosts.py)")
    if not ghost_details and not quarantined_count:
        print("  No ghosts detected.")
        return

    shown = 0
    for c in ghost_details:
        if shown < 20:
            gap = c["first_year"] - c["death_year"]
            wd_cols = c.get("wd_colonies", [])
            colony_tag = " [colony-confirmed]" if c["colony"] in wd_cols else ""
            print(f"    {c['col_name']:<30} {c['colony']:<25} "
                  f"{c['first_year']}-{c['last_year']}  "
                  f"(WD: {c['wd_name']} d.{c['death_year']}, +{gap}y){colony_tag}")
            shown += 1
    extra = len(ghost_ids) - quarantined_count - shown
    if extra > 0:
        print(f"    ... and {extra} more colony-confirmed ghosts")


# =============================================================================
# CONNECTED COMPONENTS (UNION-FIND)
# =============================================================================

class UnionFind:
    """Union-Find data structure for connected components."""

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    def components(self) -> dict[str, set[str]]:
        """Return {root: set of members}."""
        comps = defaultdict(set)
        for x in self.parent:
            comps[self.find(x)].add(x)
        return dict(comps)


def build_components(
    edges: list[dict],
    same_as: dict[str, str],  # official_id → wd_qid
) -> list[set[str]]:
    """Build connected components from edges and SAME_AS anchors.

    Officials linked to the same WD_Person are in the same component.
    """
    uf = UnionFind()

    # Add all edge endpoints
    for e in edges:
        uf.union(e["a_id"], e["b_id"])

    # Group officials by WD_Person — same person = same component
    wd_groups = defaultdict(list)
    for off_id, wd_qid in same_as.items():
        wd_groups[wd_qid].append(off_id)

    for wd_qid, off_ids in wd_groups.items():
        for i in range(1, len(off_ids)):
            uf.union(off_ids[0], off_ids[i])

    comps = uf.components()
    return [members for members in comps.values() if len(members) >= 1]


# =============================================================================
# VALIDATION
# =============================================================================

# Federal pairs where simultaneous service is expected
FEDERAL_PAIRS = {
    # Caribbean — Leeward Islands federation
    frozenset({"Antigua", "Leeward Islands"}),
    frozenset({"Dominica", "Leeward Islands"}),
    frozenset({"Montserrat", "Leeward Islands"}),
    frozenset({"St Kitts-Nevis", "Leeward Islands"}),
    frozenset({"St Christopher and Nevis", "Leeward Islands"}),
    frozenset({"Virgin Islands", "Leeward Islands"}),
    # Caribbean — Windward Islands federation
    frozenset({"St Vincent", "Windward Islands"}),
    frozenset({"Barbados", "Windward Islands"}),
    frozenset({"Grenada", "Windward Islands"}),
    frozenset({"St Lucia", "Windward Islands"}),
    frozenset({"Tobago", "Windward Islands"}),
    # Caribbean — Trinidad group
    frozenset({"Trinidad", "Trinidad and Tobago"}),
    frozenset({"Tobago", "Trinidad"}),
    frozenset({"Tobago", "Trinidad and Tobago"}),
    # Caribbean — West Indies federation
    frozenset({"British Guiana", "West Indies"}),
    frozenset({"Trinidad", "West Indies"}),
    frozenset({"Trinidad and Tobago", "West Indies"}),
    frozenset({"Jamaica", "West Indies"}),
    frozenset({"British Guiana", "Windward Islands"}),
    frozenset({"Leeward Islands", "Windward Islands"}),
    # West Africa
    frozenset({"Gold Coast", "Togoland"}),
    frozenset({"Northern Nigeria", "Nigeria"}),
    frozenset({"Southern Nigeria", "Nigeria"}),
    # Southern/Central Africa
    frozenset({"Northern Rhodesia", "Central Africa"}),
    frozenset({"Southern Rhodesia", "Central Africa"}),
    frozenset({"Nyasaland", "Central Africa"}),
    frozenset({"Rhodesia", "Southern Rhodesia"}),
    frozenset({"Rhodesia", "South Africa"}),
    frozenset({"Rhodesia", "Swaziland"}),
    frozenset({"Southern Rhodesia", "Swaziland"}),
    frozenset({"South Africa", "Swaziland"}),
    frozenset({"South Africa", "Southern Rhodesia"}),
    frozenset({"Natal", "South Africa"}),
    frozenset({"Basutoland", "South Africa"}),
    # High Commission Territories
    frozenset({"Basutoland", "High Commission Territories"}),
    frozenset({"Swaziland", "High Commission Territories"}),
    frozenset({"Bechuanaland", "High Commission Territories"}),
    frozenset({"Basutoland", "Swaziland"}),
    frozenset({"Bechuanaland", "Swaziland"}),
    # Malaya / Southeast Asia
    frozenset({"Federated Malay States", "Straits Settlements"}),
    frozenset({"Johore", "Straits Settlements"}),
    frozenset({"Unfederated Malay States", "Straits Settlements"}),
    frozenset({"Federation of Malaya", "Singapore"}),
    # Pacific
    frozenset({"Fiji", "Western Pacific"}),
    frozenset({"Gilbert and Ellice Islands", "Western Pacific"}),
    # Australian federation (1901) — colony → Commonwealth
    frozenset({"New South Wales", "Australia"}),
    frozenset({"Victoria", "Australia"}),
    frozenset({"Queensland", "Australia"}),
    frozenset({"South Australia", "Australia"}),
    frozenset({"Western Australia", "Australia"}),
    frozenset({"Tasmania", "Australia"}),
    frozenset({"New South Wales", "Commonwealth Of Australia"}),
    frozenset({"Victoria", "Commonwealth Of Australia"}),
    frozenset({"Queensland", "Commonwealth Of Australia"}),
    frozenset({"South Australia", "Commonwealth Of Australia"}),
    frozenset({"Western Australia", "Commonwealth Of Australia"}),
    frozenset({"Tasmania", "Commonwealth Of Australia"}),
    frozenset({"Australia", "Papua"}),
    # East Africa
    frozenset({"Kenya", "Zanzibar"}),
    # Atlantic
    frozenset({"British Antarctic Territory", "Falkland Islands"}),
    # Horn of Africa (shared staff)
    frozenset({"British Somaliland", "Sierra Leone"}),
}


def validate_component(officials: list[dict]) -> tuple[bool, str]:
    """Validate that a component represents a plausible single person.

    Checks:
    1. No simultaneous service in different (non-federal) colonies
    2. Career span is plausible (< 60 years)
    3. Name consistency across stints
    """
    if len(officials) <= 1:
        return True, ""

    # Check for temporal overlap in different colonies
    for i in range(len(officials)):
        for j in range(i + 1, len(officials)):
            a = officials[i]
            b = officials[j]

            if a["colony"] == b["colony"]:
                continue

            # Check federal pairs
            if frozenset({a["colony"], b["colony"]}) in FEDERAL_PAIRS:
                continue

            # Check overlap
            if a["first_year"] <= b["last_year"] and b["first_year"] <= a["last_year"]:
                overlap_years = (min(a["last_year"], b["last_year"])
                                 - max(a["first_year"], b["first_year"]) + 1)
                if overlap_years > 1:  # Allow 1-year transition overlap
                    return False, (f"Simultaneous service: {a['colony']} "
                                   f"({a['first_year']}-{a['last_year']}) and "
                                   f"{b['colony']} ({b['first_year']}-{b['last_year']})")

    # Check career span
    earliest = min(o["first_year"] for o in officials)
    latest = max(o["last_year"] for o in officials)
    span = latest - earliest
    if span > 55:
        return False, f"Career span too long: {span} years ({earliest}-{latest})"

    return True, ""


# =============================================================================
# PERSON NODE BUILDER
# =============================================================================

def build_person_data(
    component: set[str],
    official_details: dict[str, dict],
    same_as: dict[str, str],
    same_as_names: dict[str, str],
) -> dict | None:
    """Build a COL_Person record from a component of officials."""
    officials = []
    for off_id in component:
        if off_id in official_details:
            officials.append(official_details[off_id])

    if not officials:
        return None

    # Validate
    valid, reason = validate_component(officials)
    if not valid:
        return None

    # Sort by first_year
    officials.sort(key=lambda o: o["first_year"])

    # Build person record
    # Best name: pick the most specific variant
    names = [o["name"] for o in officials]
    # Prefer names with more given name components
    best_name = max(names, key=lambda n: len(n.split(", ", 1)[-1]) if ", " in n else 0)

    # Colonies and years
    colonies = list(dict.fromkeys(o["colony"] for o in officials))  # preserve order, dedupe
    first_year = min(o["first_year"] for o in officials)
    last_year = max(o["last_year"] for o in officials)
    total_editions = sum(o.get("num_editions") or len(o.get("editions") or []) for o in officials)

    # WD_Person link
    wd_qids = set()
    wd_names_list = []
    for off_id in component:
        if off_id in same_as:
            qid = same_as[off_id]
            wd_qids.add(qid)
            if qid in same_as_names:
                wd_names_list.append(same_as_names[qid])

    person_id = f"person_{officials[0]['id']}"

    return {
        "person_id": person_id,
        "name": best_name,
        "colonies": colonies,
        "first_year": first_year,
        "last_year": last_year,
        "total_editions": total_editions,
        "num_stints": len(officials),
        "official_ids": [o["id"] for o in officials],
        "wd_qids": list(wd_qids),
        "wd_names": wd_names_list,
        "is_wikidata_verified": len(wd_qids) > 0,
    }


# =============================================================================
# WRITE TO NEO4J
# =============================================================================

CREATE_PERSON_QUERY = """
UNWIND $batch AS rec
MERGE (p:COL_Person {id: rec.person_id})
SET p.name = rec.name,
    p.colonies = rec.colonies,
    p.first_year = rec.first_year,
    p.last_year = rec.last_year,
    p.total_editions = rec.total_editions,
    p.num_stints = rec.num_stints,
    p.is_wikidata_verified = rec.is_wikidata_verified,
    p.date_created = $date_created
RETURN count(p) AS c
"""

CREATE_CAREER_STINT_QUERY = """
UNWIND $batch AS rec
MATCH (p:COL_Person {id: rec.person_id})
MATCH (o:COL_Official {id: rec.official_id})
MERGE (p)-[r:CAREER_STINT]->(o)
SET r.order = rec.stint_order
RETURN count(r) AS c
"""

CREATE_PERSON_SAME_AS_QUERY = """
UNWIND $batch AS rec
MATCH (p:COL_Person {id: rec.person_id})
MATCH (w:WD_Person {qid: rec.wd_qid})
MERGE (p)-[r:SAME_AS]->(w)
SET r.method = 'person_builder',
    r.date_created = $date_created
RETURN count(r) AS c
"""

SCHEMA_STMTS = [
    "CREATE CONSTRAINT col_person_id IF NOT EXISTS FOR (p:COL_Person) REQUIRE p.id IS UNIQUE",
    "CREATE INDEX col_person_name IF NOT EXISTS FOR (p:COL_Person) ON (p.name)",
]


def write_persons(driver, persons: list[dict]) -> dict[str, int]:
    """Write COL_Person nodes and relationships."""
    today = date.today().isoformat()
    counts = {"persons": 0, "stints": 0, "same_as": 0}

    with driver.session() as session:
        # Schema
        for stmt in SCHEMA_STMTS:
            try:
                session.run(stmt)
            except Exception as e:
                if "already exists" not in str(e).lower():
                    print(f"  WARNING: {e}")

        # Create person nodes
        for i in range(0, len(persons), BATCH_SIZE):
            batch = persons[i:i + BATCH_SIZE]
            r = session.run(CREATE_PERSON_QUERY, batch=batch, date_created=today)
            counts["persons"] += r.single()["c"]

        # Create CAREER_STINT relationships
        stint_batch = []
        for p in persons:
            for order, off_id in enumerate(p["official_ids"]):
                stint_batch.append({
                    "person_id": p["person_id"],
                    "official_id": off_id,
                    "stint_order": order,
                })

        for i in range(0, len(stint_batch), BATCH_SIZE):
            batch = stint_batch[i:i + BATCH_SIZE]
            r = session.run(CREATE_CAREER_STINT_QUERY, batch=batch, date_created=today)
            counts["stints"] += r.single()["c"]

        # Create SAME_AS to WD_Person
        sa_batch = []
        for p in persons:
            for qid in p["wd_qids"]:
                sa_batch.append({
                    "person_id": p["person_id"],
                    "wd_qid": qid,
                })

        if sa_batch:
            for i in range(0, len(sa_batch), BATCH_SIZE):
                batch = sa_batch[i:i + BATCH_SIZE]
                r = session.run(CREATE_PERSON_SAME_AS_QUERY, batch=batch,
                                date_created=today)
                counts["same_as"] += r.single()["c"]

    return counts


# =============================================================================
# EXPANSION
# =============================================================================

def expand_with_medium_edges(
    driver,
    existing_components: dict[str, str],  # official_id → person_id
    person_officials: dict[str, list[dict]],  # person_id → list of official details
    expand_threshold: float,
) -> list[dict]:
    """Find medium-confidence edges connecting to existing components.

    An edge is safe to add if:
    - One end is already in a verified component
    - The other end is unassigned
    - The edge uncertainty is below expand_threshold
    - Adding the new stint doesn't create temporal overlap (validated)
    """
    print(f"\n--- EXPANSION (threshold < {expand_threshold:.2f}) ---")

    with driver.session() as session:
        result = session.run(FETCH_MEDIUM_EDGES,
                             low=0.0, high=expand_threshold)
        medium_edges = [dict(r) for r in result]

    print(f"  {len(medium_edges)} medium-confidence edges found")

    # Find edges where one end is assigned and the other is not
    expansions = []
    for e in medium_edges:
        a_assigned = e["a_id"] in existing_components
        b_assigned = e["b_id"] in existing_components

        if a_assigned and not b_assigned:
            expansions.append({
                "person_id": existing_components[e["a_id"]],
                "official_id": e["b_id"],
                "uncertainty": e["uncertainty"],
                "anchor_id": e["a_id"],
            })
        elif b_assigned and not a_assigned:
            expansions.append({
                "person_id": existing_components[e["b_id"]],
                "official_id": e["a_id"],
                "uncertainty": e["uncertainty"],
                "anchor_id": e["b_id"],
            })

    # Deduplicate: if an official could join multiple components, skip
    by_official = defaultdict(list)
    for exp in expansions:
        by_official[exp["official_id"]].append(exp)

    candidates = []
    for off_id, exps in by_official.items():
        if len(exps) == 1:
            candidates.append(exps[0])

    # Fetch details for candidate officials
    candidate_ids = [c["official_id"] for c in candidates]
    candidate_details = {}
    if candidate_ids:
        with driver.session() as session:
            for i in range(0, len(candidate_ids), BATCH_SIZE):
                batch_ids = candidate_ids[i:i + BATCH_SIZE]
                result = session.run(FETCH_OFFICIAL_DETAILS, ids=batch_ids)
                for r in result:
                    candidate_details[r["id"]] = dict(r)

    # Validate each expansion: new stint must not overlap existing stints
    safe_expansions = []
    rejected = 0
    for exp in candidates:
        new_off = candidate_details.get(exp["official_id"])
        if not new_off:
            continue

        existing = person_officials.get(exp["person_id"], [])
        # Validate the expanded set
        expanded = existing + [new_off]
        valid, reason = validate_component(expanded)
        if valid:
            safe_expansions.append(exp)
        else:
            rejected += 1

    print(f"  {len(safe_expansions)} safe expansions (validated, no overlap)")
    if rejected:
        print(f"  {rejected} rejected (would create overlap)")
    return safe_expansions


def write_expansions(driver, expansions: list[dict]) -> int:
    """Add officials to existing COL_Person nodes."""
    today = date.today().isoformat()

    with driver.session() as session:
        total = 0
        for i in range(0, len(expansions), BATCH_SIZE):
            batch = expansions[i:i + BATCH_SIZE]
            r = session.run("""
                UNWIND $batch AS rec
                MATCH (p:COL_Person {id: rec.person_id})
                MATCH (o:COL_Official {id: rec.official_id})
                MERGE (p)-[r:CAREER_STINT]->(o)
                SET r.method = 'expansion',
                    r.uncertainty = rec.uncertainty,
                    r.date_created = $date_created
                WITH p, o
                SET p.num_stints = p.num_stints + 1
                RETURN count(o) AS c
            """, batch=batch, date_created=today)
            total += r.single()["c"]

    return total


# =============================================================================
# STATS
# =============================================================================

def print_stats(driver):
    """Report on COL_Person nodes."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("COL_PERSON STATISTICS")
        print("=" * 60)

        r = session.run("MATCH (p:COL_Person) RETURN count(p) AS c").single()
        total_persons = r["c"]
        print(f"\n  Total COL_Person nodes: {total_persons}")

        if total_persons == 0:
            print("  No person nodes yet.")
            return

        # Stints per person distribution
        result = session.run("""
            MATCH (p:COL_Person)
            RETURN p.num_stints AS stints, count(p) AS n
            ORDER BY stints
        """)
        print("\n  Stints per person:")
        for rec in result:
            bar = "█" * max(1, rec["n"] * 40 // total_persons)
            print(f"    {rec['stints']} stints: {rec['n']:>5}  {bar}")

        # Wikidata-verified
        result = session.run("""
            MATCH (p:COL_Person)
            RETURN p.is_wikidata_verified AS verified, count(p) AS n
        """)
        print("\n  Wikidata verification:")
        for rec in result:
            label = "verified" if rec["verified"] else "unverified"
            print(f"    {label}: {rec['n']:>5}")

        # SAME_AS to WD_Person
        r = session.run(
            "MATCH (p:COL_Person)-[:SAME_AS]->(w:WD_Person) "
            "RETURN count(DISTINCT p) AS persons, count(DISTINCT w) AS wd"
        ).single()
        print(f"\n  Persons linked to Wikidata: {r['persons']}")
        print(f"  Unique WD_Person linked: {r['wd']}")

        # Colonies per person
        result = session.run("""
            MATCH (p:COL_Person)
            RETURN size(p.colonies) AS n_colonies, count(p) AS n
            ORDER BY n_colonies
        """)
        print("\n  Colonies per person:")
        for rec in result:
            bar = "█" * max(1, rec["n"] * 40 // total_persons)
            print(f"    {rec['n_colonies']} colonies: {rec['n']:>5}  {bar}")

        # Career span
        result = session.run("""
            MATCH (p:COL_Person)
            WITH p, p.last_year - p.first_year AS span
            RETURN
              CASE
                WHEN span < 10 THEN '< 10 years'
                WHEN span < 20 THEN '10-19 years'
                WHEN span < 30 THEN '20-29 years'
                WHEN span < 40 THEN '30-39 years'
                ELSE '40+ years'
              END AS bucket, count(p) AS n
            ORDER BY bucket
        """)
        print("\n  Career span:")
        for rec in result:
            bar = "█" * max(1, rec["n"] * 40 // total_persons)
            print(f"    {rec['bucket']:<15} {rec['n']:>5}  {bar}")

        # Coverage
        r = session.run("""
            MATCH (p:COL_Person)-[:CAREER_STINT]->(o:COL_Official)
            WITH count(DISTINCT o) AS linked_officials
            MATCH (o2:COL_Official)
            RETURN linked_officials, count(o2) AS total_officials
        """).single()
        print(f"\n  Officials in person nodes: {r['linked_officials']} / {r['total_officials']} "
              f"({r['linked_officials'] * 100 / max(1, r['total_officials']):.1f}%)")

        # Sample persons
        print("\n  Sample COL_Person nodes (most stints):")
        result = session.run("""
            MATCH (p:COL_Person)
            OPTIONAL MATCH (p)-[:SAME_AS]->(w:WD_Person)
            RETURN p.name AS name, p.colonies AS colonies,
                   p.first_year AS first_year, p.last_year AS last_year,
                   p.num_stints AS stints, w.qid AS wd_qid
            ORDER BY p.num_stints DESC LIMIT 10
        """)
        for rec in result:
            wd = f" ↔ {rec['wd_qid']}" if rec["wd_qid"] else ""
            print(f"    {rec['name']:<30} {rec['stints']} stints "
                  f"({', '.join(rec['colonies'][:3])}) "
                  f"{rec['first_year']}-{rec['last_year']}{wd}")


# =============================================================================
# DRY RUN
# =============================================================================

def dry_run_report(persons: list[dict]):
    """Preview person nodes without writing."""
    print("\n" + "=" * 60)
    print("[DRY RUN] PREVIEW")
    print("=" * 60)

    print(f"\n  Total COL_Person nodes to create: {len(persons)}")

    if not persons:
        print("  No persons to create.")
        return

    total_officials = sum(len(p["official_ids"]) for p in persons)
    wd_verified = sum(1 for p in persons if p["is_wikidata_verified"])

    print(f"  Total officials covered: {total_officials}")
    print(f"  Wikidata-verified persons: {wd_verified}")

    # Stints distribution
    stints_dist = defaultdict(int)
    for p in persons:
        stints_dist[p["num_stints"]] += 1

    print("\n  Stints per person:")
    for s in sorted(stints_dist):
        n = stints_dist[s]
        bar = "█" * max(1, n * 40 // len(persons))
        print(f"    {s} stints: {n:>5}  {bar}")

    # Colonies per person
    cols_dist = defaultdict(int)
    for p in persons:
        cols_dist[len(p["colonies"])] += 1

    print("\n  Colonies per person:")
    for c in sorted(cols_dist):
        n = cols_dist[c]
        bar = "█" * max(1, n * 40 // len(persons))
        print(f"    {c} colonies: {n:>5}  {bar}")

    # Sample persons (most stints)
    sorted_p = sorted(persons, key=lambda p: p["num_stints"], reverse=True)
    n_show = min(20, len(sorted_p))
    print(f"\n  Top {n_show} persons (most stints):")
    for p in sorted_p[:n_show]:
        wd = f" ↔ {','.join(p['wd_qids'])}" if p["wd_qids"] else ""
        print(f"    {p['name']:<30} {p['num_stints']} stints "
              f"({', '.join(p['colonies'][:3])}) "
              f"{p['first_year']}-{p['last_year']}{wd}")

    print("\n[DRY RUN] No data written.")


# =============================================================================
# CLEAR
# =============================================================================

def clear_persons(driver):
    """Remove all COL_Person nodes and CAREER_STINT relationships."""
    with driver.session() as session:
        r = session.run(
            "MATCH (p:COL_Person)-[r:CAREER_STINT]->() "
            "DELETE r RETURN count(r) AS c"
        ).single()
        print(f"Deleted {r['c']} CAREER_STINT relationships.")

        r = session.run(
            "MATCH (p:COL_Person)-[r:SAME_AS]->() "
            "DELETE r RETURN count(r) AS c"
        ).single()
        print(f"Deleted {r['c']} COL_Person SAME_AS relationships.")

        r = session.run(
            "MATCH (p:COL_Person) DELETE p RETURN count(p) AS c"
        ).single()
        print(f"Deleted {r['c']} COL_Person nodes.")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Stage 4b: Build COL_Person nodes from verified components"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without writing to Neo4j")
    parser.add_argument("--stats", action="store_true",
                        help="Report COL_Person statistics")
    parser.add_argument("--clear", action="store_true",
                        help="Remove all COL_Person nodes")
    parser.add_argument("--threshold", type=float, default=DEFAULT_HIGH_THRESHOLD,
                        help=f"Max uncertainty for core edges (default {DEFAULT_HIGH_THRESHOLD})")
    parser.add_argument("--expand", action="store_true",
                        help="Expand with medium-confidence edges")
    parser.add_argument("--expand-threshold", type=float, default=DEFAULT_EXPAND_THRESHOLD,
                        help=f"Max uncertainty for expansion (default {DEFAULT_EXPAND_THRESHOLD})")
    args = parser.parse_args()

    print("=" * 60)
    print("COL STAGE 4b: PERSON NODE BUILDER")
    print("=" * 60)

    # Connect
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        if args.stats:
            print_stats(driver)
            return

        if args.clear:
            clear_persons(driver)
            return

        # --- Detect ghosts (quarantine flags + colony-confirmed WD) ---
        print("\nDetecting ghost officials...")
        with driver.session() as session:
            ghost_ids, ghost_details = detect_ghosts(session)
        # Count how many are from quarantine vs colony-confirmed
        quarantined_count = len(ghost_ids) - len(ghost_details)
        print(f"  {len(ghost_ids)} ghost officials detected")
        if ghost_ids:
            print_ghost_report(ghost_details, ghost_ids, quarantined_count)

        # --- Fetch high-confidence edges ---
        print(f"\nFetching high-confidence edges (uncertainty < {args.threshold})...")
        with driver.session() as session:
            result = session.run(FETCH_HIGH_CONFIDENCE_EDGES, threshold=args.threshold)
            high_edges = [dict(r) for r in result]

            # Also fetch WD-verified edges regardless of threshold
            result = session.run(FETCH_WD_VERIFIED_EDGES)
            wd_edges = [dict(r) for r in result]

        # Merge, deduplicating, and exclude ghost officials
        edge_keys = set()
        all_edges = []
        ghost_filtered = 0
        for e in high_edges + wd_edges:
            # Skip edges involving ghost officials
            if e["a_id"] in ghost_ids or e["b_id"] in ghost_ids:
                ghost_filtered += 1
                continue
            key = (min(e["a_id"], e["b_id"]), max(e["a_id"], e["b_id"]))
            if key not in edge_keys:
                edge_keys.add(key)
                all_edges.append(e)

        print(f"  {len(high_edges)} high-confidence edges")
        print(f"  {len(wd_edges)} Wikidata-verified edges")
        if ghost_filtered:
            print(f"  {ghost_filtered} edges filtered (ghost officials)")
        print(f"  {len(all_edges)} unique edges total")

        # --- Fetch SAME_AS anchors ---
        print("Fetching SAME_AS anchors...")
        with driver.session() as session:
            result = session.run(FETCH_SAME_AS)
            same_as_raw = [dict(r) for r in result]

        same_as = {r["official_id"]: r["wd_qid"] for r in same_as_raw}
        same_as_names = {}
        for r in same_as_raw:
            same_as_names[r["wd_qid"]] = r.get("wd_name", "")

        print(f"  {len(same_as)} officials with SAME_AS anchors")

        # --- Build connected components ---
        print("Building connected components...")
        components = build_components(all_edges, same_as)
        print(f"  {len(components)} components found")

        # Filter: only components with 2+ officials (single-official = trivial)
        multi_components = [c for c in components if len(c) >= 2]
        single_components = [c for c in components if len(c) == 1]
        # Include single officials that have SAME_AS (they're verified identities)
        single_verified = [c for c in single_components
                           if any(off_id in same_as for off_id in c)]
        active_components = multi_components + single_verified

        print(f"  {len(multi_components)} multi-official components")
        print(f"  {len(single_verified)} single-official components (Wikidata-verified)")

        # --- Fetch official details ---
        all_ids = set()
        for comp in active_components:
            all_ids.update(comp)

        print(f"Fetching details for {len(all_ids)} officials...")
        official_details = {}
        with driver.session() as session:
            id_list = list(all_ids)
            for i in range(0, len(id_list), BATCH_SIZE):
                batch_ids = id_list[i:i + BATCH_SIZE]
                result = session.run(FETCH_OFFICIAL_DETAILS, ids=batch_ids)
                for r in result:
                    official_details[r["id"]] = dict(r)

        # --- Build person records ---
        print("Building person records...")
        persons = []
        invalid = 0
        for comp in active_components:
            person = build_person_data(comp, official_details, same_as, same_as_names)
            if person:
                persons.append(person)
            else:
                invalid += 1

        print(f"  {len(persons)} valid person records")
        if invalid:
            print(f"  {invalid} invalid components (validation failed)")

        # Build maps for expansion validation
        existing_map = {}  # official_id → person_id
        person_officials_map = {}  # person_id → list of official details
        for p in persons:
            off_list = [official_details[oid] for oid in p["official_ids"]
                        if oid in official_details]
            person_officials_map[p["person_id"]] = off_list
            for off_id in p["official_ids"]:
                existing_map[off_id] = p["person_id"]

        # --- Dry run or write ---
        if args.dry_run:
            dry_run_report(persons)
            if args.expand:
                expansions = expand_with_medium_edges(
                    driver, existing_map, person_officials_map,
                    args.expand_threshold)
                print(f"\n  Would add {len(expansions)} expansion stints")
            return

        if persons:
            print(f"\nWriting {len(persons)} COL_Person nodes...")
            counts = write_persons(driver, persons)
            print(f"  Created {counts['persons']} person nodes")
            print(f"  Created {counts['stints']} CAREER_STINT relationships")
            print(f"  Created {counts['same_as']} SAME_AS relationships")

        # --- Expansion ---
        if args.expand and persons:
            expansions = expand_with_medium_edges(
                driver, existing_map, person_officials_map,
                args.expand_threshold)

            if expansions:
                n_expanded = write_expansions(driver, expansions)
                print(f"  Added {n_expanded} expansion stints")

        # --- Final stats ---
        print_stats(driver)

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()

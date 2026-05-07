"""
COL Phase 5: Career Chain Validation
======================================

Post-processes ML pair scores into career chains, enforcing temporal
consistency. A person can only be in one place at a time (with allowance
for administrative overlaps like Windward Islands sub-colonies).

Logic:
1. Build connected components from all edges with ml_probability > threshold
2. For each component, greedily build the best sequential chain:
   - Sort officials by first_year
   - Add officials to the chain if they don't violate temporal constraints
   - Prefer higher ml_probability edges when there's a conflict
3. Edges not in the validated chain get downgraded
4. Write chain_id and chain_validated properties to edges

Usage:
    python col_ml_chains.py                     # analyze only
    python col_ml_chains.py --write             # write chain properties to Neo4j
    python col_ml_chains.py --threshold 0.7     # only consider edges above 0.7

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
    print("ERROR: neo4j driver not installed")
    sys.exit(1)

# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
ML_DIR = REPO_DIR / "ml_data"

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

# Colonies that are sub-units of each other — overlapping service is expected
COLONY_GROUPS = {
    frozenset({"Windward Islands", "Grenada", "St Vincent", "St Lucia", "Dominica", "Tobago"}),
    frozenset({"Leeward Islands", "Antigua", "Montserrat", "St Kitts", "Nevis", "Virgin Islands", "Dominica"}),
    frozenset({"Nigeria", "Southern Nigeria", "Northern Nigeria", "Lagos"}),
    frozenset({"Rhodesia", "Southern Rhodesia", "Northern Rhodesia"}),
    frozenset({"Malaya", "Straits Settlements", "Federated Malay States", "Unfederated Malay States"}),
    frozenset({"South Africa", "Cape of Good Hope", "Natal", "Transvaal", "Orange River Colony"}),
    frozenset({"Australia", "New South Wales", "Victoria", "Queensland", "South Australia", "Western Australia", "Tasmania"}),
    frozenset({"Canada", "Ontario", "Quebec", "Nova Scotia", "New Brunswick", "Manitoba", "British Columbia",
               "Saskatchewan", "Alberta", "Prince Edward Island", "Northwest Territories", "Newfoundland"}),
    frozenset({"Western Pacific", "Fiji", "Tonga", "Gilbert and Ellice Islands"}),
    frozenset({"British Guiana", "British Honduras"}),
    frozenset({"Trinidad", "Trinidad and Tobago", "Tobago"}),
    frozenset({"East Africa", "Kenya", "Uganda", "Tanganyika", "Zanzibar"}),
    frozenset({"Gold Coast", "Togoland", "Ashanti", "Northern Territories of the Gold Coast"}),
    frozenset({"Palestine", "Transjordan"}),
    frozenset({"British Somaliland", "Aden"}),
    frozenset({"Sarawak", "North Borneo", "Brunei", "Labuan"}),
    frozenset({"Nyasaland", "British Central Africa"}),
    frozenset({"Gambia", "Sierra Leone"}),
}

# Build lookup: colony -> set of group-mates
_COLONY_MATES = defaultdict(set)
for group in COLONY_GROUPS:
    for colony in group:
        _COLONY_MATES[colony].update(group)


def colonies_compatible(col_a, col_b):
    """Can someone serve in both colonies simultaneously?"""
    if col_a == col_b:
        return True
    return col_b in _COLONY_MATES.get(col_a, set())


# =============================================================================
# DATA LOADING
# =============================================================================

def load_edges_and_officials(driver, threshold):
    """Load all POSSIBLE_MATCH edges above threshold with official data."""
    with driver.session() as s:
        result = s.run("""
            MATCH (a:COL_Official)-[r:POSSIBLE_MATCH]->(b:COL_Official)
            WHERE r.ml_probability >= $threshold
            RETURN a.id AS a_id, b.id AS b_id,
                   a.colony AS a_col, b.colony AS b_col,
                   a.first_year AS a_fy, a.last_year AS a_ly,
                   b.first_year AS b_fy, b.last_year AS b_ly,
                   a.name AS a_name, b.name AS b_name,
                   r.ml_probability AS prob,
                   r.method AS method
        """, threshold=threshold)
        edges = [dict(r) for r in result]

    # Build node data
    node_data = {}
    for e in edges:
        for side in ("a", "b"):
            nid = e[f"{side}_id"]
            if nid not in node_data:
                node_data[nid] = {
                    "id": nid,
                    "colony": e[f"{side}_col"],
                    "first_year": e[f"{side}_fy"] or 0,
                    "last_year": e[f"{side}_ly"] or 0,
                    "name": e[f"{side}_name"],
                }

    return edges, node_data


# =============================================================================
# CONNECTED COMPONENTS
# =============================================================================

def find_components(edges):
    """Find connected components from edge list."""
    graph = defaultdict(set)
    for e in edges:
        graph[e["a_id"]].add(e["b_id"])
        graph[e["b_id"]].add(e["a_id"])

    visited = set()
    components = []
    for node in graph:
        if node in visited:
            continue
        comp = []
        queue = [node]
        while queue:
            n = queue.pop(0)
            if n in visited:
                continue
            visited.add(n)
            comp.append(n)
            for neighbor in graph[n]:
                if neighbor not in visited:
                    queue.append(neighbor)
        components.append(comp)

    return components


# =============================================================================
# CHAIN VALIDATION
# =============================================================================

def validate_chain(component, node_data, edge_lookup, max_overlap=2):
    """Validate a connected component into a sequential career chain.

    Returns:
        validated_edges: set of (a_id, b_id) tuples that form valid chains
        rejected_edges: set of (a_id, b_id) tuples that violate constraints
        chain_info: dict with chain metadata
    """
    if len(component) <= 2:
        # Simple pair — just check temporal consistency
        if len(component) == 2:
            a_id, b_id = component
            a = node_data.get(a_id, {})
            b = node_data.get(b_id, {})
            edge_key = (a_id, b_id)
            if edge_key not in edge_lookup:
                edge_key = (b_id, a_id)
            if edge_key not in edge_lookup:
                return set(), set(), {}

            if _temporal_ok(a, b, max_overlap):
                return {edge_key}, set(), {"size": 2, "colonies": {a.get("colony"), b.get("colony")}}
            else:
                return set(), {edge_key}, {"size": 2, "violation": "temporal_overlap"}

        return set(), set(), {}

    # Sort officials chronologically
    nodes = [(nid, node_data.get(nid, {})) for nid in component]
    nodes.sort(key=lambda x: x[1].get("first_year", 9999))

    # Build edge probability lookup for this component
    comp_edges = {}
    for nid_a, _ in nodes:
        for nid_b, _ in nodes:
            key = (nid_a, nid_b)
            if key in edge_lookup:
                comp_edges[key] = edge_lookup[key]
            key_rev = (nid_b, nid_a)
            if key_rev in edge_lookup:
                comp_edges[key_rev] = edge_lookup[key_rev]

    # Greedy chain building: try to find the best sequential path
    # Strategy: for each possible starting node, build the longest
    # temporally-consistent chain, preferring highest-probability edges.
    best_chain = []
    best_score = 0

    for start_idx in range(len(nodes)):
        chain = [nodes[start_idx]]
        chain_edges = []

        for candidate_idx in range(start_idx + 1, len(nodes)):
            cand_id, cand_data = nodes[candidate_idx]

            # Check if this candidate connects to the chain's last member
            last_id = chain[-1][0]
            edge_key = (last_id, cand_id)
            prob = comp_edges.get(edge_key, comp_edges.get((cand_id, last_id)))
            if prob is None:
                # Not directly connected — check if connected to any chain member
                for chain_id, _ in chain:
                    edge_key = (chain_id, cand_id)
                    prob = comp_edges.get(edge_key, comp_edges.get((cand_id, chain_id)))
                    if prob is not None:
                        edge_key = (chain_id, cand_id) if (chain_id, cand_id) in comp_edges else (cand_id, chain_id)
                        break
                if prob is None:
                    continue

            # Check temporal consistency with ALL chain members
            ok = True
            for chain_id, chain_data in chain:
                if not _temporal_ok(chain_data, cand_data, max_overlap):
                    ok = False
                    break

            if ok:
                chain.append((cand_id, cand_data))
                chain_edges.append(edge_key)

        score = sum(comp_edges.get(e, comp_edges.get((e[1], e[0]), 0)) for e in chain_edges)
        if len(chain) > len(best_chain) or (len(chain) == len(best_chain) and score > best_score):
            best_chain = chain
            best_score = score

    # Determine validated vs rejected edges
    chain_ids = {nid for nid, _ in best_chain}
    validated = set()
    rejected = set()

    for edge_key, prob in comp_edges.items():
        a_in = edge_key[0] in chain_ids
        b_in = edge_key[1] in chain_ids
        if a_in and b_in:
            validated.add(edge_key)
        else:
            rejected.add(edge_key)

    colonies = {node_data.get(nid, {}).get("colony") for nid in chain_ids}
    colonies.discard(None)

    chain_info = {
        "size": len(best_chain),
        "total_in_component": len(component),
        "colonies": colonies,
        "rejected_count": len(rejected),
    }

    return validated, rejected, chain_info


def _temporal_ok(a_data, b_data, max_overlap):
    """Check if two officials can be the same person temporally."""
    a_col = a_data.get("colony", "")
    b_col = b_data.get("colony", "")

    # Same colony: overlaps are fine (within-colony gaps)
    if a_col == b_col:
        return True

    # Compatible colonies: allow larger overlaps (e.g., Windward Islands + Grenada)
    if colonies_compatible(a_col, b_col):
        return True

    # Different, unrelated colonies: check temporal overlap
    a_fy = a_data.get("first_year") or 0
    a_ly = a_data.get("last_year") or 0
    b_fy = b_data.get("first_year") or 0
    b_ly = b_data.get("last_year") or 0

    # Overlap = how many years they served simultaneously
    # overlap > 0 means they were in different colonies at the same time
    overlap = min(a_ly, b_ly) - max(a_fy, b_fy)

    return overlap <= max_overlap


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Phase 5: Career chain validation")
    parser.add_argument("--write", action="store_true",
                        help="Write chain properties to Neo4j")
    parser.add_argument("--threshold", type=float, default=0.5,
                        help="Minimum ml_probability to consider (default: 0.5)")
    parser.add_argument("--max-overlap", type=int, default=2,
                        help="Max allowed cross-colony overlap years (default: 2)")
    args = parser.parse_args()

    if not NEO4J_PASSWORD:
        print("ERROR: Set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    # Load data
    print(f"Loading edges (threshold={args.threshold})...")
    edges, node_data = load_edges_and_officials(driver, args.threshold)
    print(f"  {len(edges)} edges, {len(node_data)} officials")

    # Build edge lookup
    edge_lookup = {}
    for e in edges:
        edge_lookup[(e["a_id"], e["b_id"])] = e["prob"]

    # Find components
    components = find_components(edges)
    print(f"  {len(components)} connected components")

    # Validate each component
    print(f"\nValidating chains (max_overlap={args.max_overlap})...")
    all_validated = set()
    all_rejected = set()
    chain_stats = {"size_2": 0, "size_3_5": 0, "size_6_10": 0, "size_11_plus": 0}
    total_pruned_officials = 0
    rejection_reasons = defaultdict(int)

    for comp in components:
        validated, rejected, info = validate_chain(
            comp, node_data, edge_lookup, max_overlap=args.max_overlap)
        all_validated.update(validated)
        all_rejected.update(rejected)

        size = info.get("size", len(comp))
        if size <= 2:
            chain_stats["size_2"] += 1
        elif size <= 5:
            chain_stats["size_3_5"] += 1
        elif size <= 10:
            chain_stats["size_6_10"] += 1
        else:
            chain_stats["size_11_plus"] += 1

        pruned = info.get("total_in_component", len(comp)) - size
        total_pruned_officials += pruned

    print(f"\n  Validated edges: {len(all_validated)}")
    print(f"  Rejected edges: {len(all_rejected)}")
    print(f"  Officials pruned from chains: {total_pruned_officials}")
    print(f"\n  Chain sizes:")
    for k, v in chain_stats.items():
        print(f"    {k}: {v}")

    # Write to Neo4j
    if args.write:
        print(f"\nWriting chain_validated property to edges...")
        _write_chain_properties(driver, all_validated, all_rejected)
        print("  Done.")

    # Summary report
    report_path = ML_DIR / "chain_validation_report.txt"
    _write_report(report_path, edges, all_validated, all_rejected,
                  chain_stats, total_pruned_officials, node_data, components, edge_lookup, args)
    print(f"\n  Report: {report_path}")

    driver.close()
    print("\nDone.")


def _write_chain_properties(driver, validated, rejected):
    """Write chain_validated=true/false to edges."""
    BATCH_SIZE = 500

    # Validated edges
    batch = []
    for a_id, b_id in validated:
        batch.append({"a_id": a_id, "b_id": b_id})
        if len(batch) >= BATCH_SIZE:
            _write_validated_batch(driver, batch, True)
            batch = []
    if batch:
        _write_validated_batch(driver, batch, True)

    # Rejected edges
    batch = []
    for a_id, b_id in rejected:
        batch.append({"a_id": a_id, "b_id": b_id})
        if len(batch) >= BATCH_SIZE:
            _write_validated_batch(driver, batch, False)
            batch = []
    if batch:
        _write_validated_batch(driver, batch, False)


def _write_validated_batch(driver, batch, validated):
    with driver.session() as s:
        s.run("""
            UNWIND $batch AS row
            MATCH (a:COL_Official {id: row.a_id})-[r:POSSIBLE_MATCH]-(b:COL_Official {id: row.b_id})
            SET r.chain_validated = $validated
        """, batch=batch, validated=validated)


def _write_report(path, edges, validated, rejected, chain_stats,
                  pruned, node_data, components, edge_lookup, args):
    """Write analysis report."""
    lines = []
    lines.append("=" * 60)
    lines.append("PHASE 5: CAREER CHAIN VALIDATION REPORT")
    lines.append("=" * 60)
    lines.append(f"\nThreshold: {args.threshold}")
    lines.append(f"Max overlap: {args.max_overlap} years")
    lines.append(f"Total edges considered: {len(edges)}")
    lines.append(f"Connected components: {len(components)}")
    lines.append(f"\nValidated edges: {len(validated)}")
    lines.append(f"Rejected edges: {len(rejected)}")
    lines.append(f"Officials pruned: {pruned}")
    lines.append(f"\nChain sizes:")
    for k, v in chain_stats.items():
        lines.append(f"  {k}: {v}")

    # Show some rejected examples
    lines.append(f"\nSample rejected edges (temporal violations):")
    count = 0
    for a_id, b_id in sorted(rejected, key=lambda x: edge_lookup.get(x, 0), reverse=True)[:20]:
        a = node_data.get(a_id, {})
        b = node_data.get(b_id, {})
        prob = edge_lookup.get((a_id, b_id), edge_lookup.get((b_id, a_id), 0))
        lines.append(f"  prob={prob:.3f}: {a.get('name','?')} {a.get('colony','?')} "
                     f"({a.get('first_year','?')}-{a.get('last_year','?')}) -> "
                     f"{b.get('name','?')} {b.get('colony','?')} "
                     f"({b.get('first_year','?')}-{b.get('last_year','?')})")

    with open(path, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()

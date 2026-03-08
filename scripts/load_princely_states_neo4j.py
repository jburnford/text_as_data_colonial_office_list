"""
Load Princely States into British Empire Knowledge Graph (Neo4j)
================================================================

Reads princely_states_wikidata.json and creates Colony nodes + relationships
in the existing British Empire KG.

Requires:
    pip install neo4j
    NEO4J_PASSWORD environment variable set

Usage:
    python scripts/load_princely_states_neo4j.py              # load all
    python scripts/load_princely_states_neo4j.py --dry-run    # preview
    python scripts/load_princely_states_neo4j.py --clear      # remove princely state nodes
    python scripts/load_princely_states_neo4j.py --stats      # show counts
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")

DATA_FILE = Path(__file__).parent.parent / "princely_states_wikidata.json"

# Target nodes for EVOLVED_INTO edges
DOMINION_INDIA = "dominion_of_india_1947_1950"
DOMINION_PAKISTAN = "dominion_of_pakistan_1947_1956"

# The Indian Empire node for ADMINISTERED_UNDER edges
INDIAN_EMPIRE = "indian_empire_british_raj_1858_1947"

# The placeholder node to keep in KG but not duplicate edges
PLACEHOLDER = "princely_states_placeholder_1818_1947"

BATCH_SIZE = 100


def load_data():
    """Load princely states from JSON."""
    if not DATA_FILE.exists():
        print(f"ERROR: {DATA_FILE} not found. Run fetch_princely_states.py first.")
        sys.exit(1)
    with open(DATA_FILE) as f:
        return json.load(f)


def create_nodes(session, states):
    """Create Colony nodes for all princely states."""
    query = """
    UNWIND $batch AS s
    MERGE (c:Colony {colony_id: s.colony_id})
    SET c.name = s.name,
        c.established_year = s.inception,
        c.independence_year = s.dissolution,
        c.region = 'South Asia',
        c.colony_type = 'Princely State',
        c.wikidata_id = s.qid,
        c.latitude = s.lat,
        c.longitude = s.lon,
        c.capital = s.capital,
        c.population = s.population,
        c.successor_dominion = s.successor,
        c.source = 'wikidata_sparql_Q1336152'
    """
    count = 0
    for i in range(0, len(states), BATCH_SIZE):
        batch = states[i:i + BATCH_SIZE]
        # Prepare batch data
        batch_data = []
        for s in batch:
            batch_data.append({
                "colony_id": s["colony_id"],
                "name": s["name"],
                "inception": s.get("inception"),
                "dissolution": s.get("dissolution"),
                "qid": s["qid"],
                "lat": s.get("lat"),
                "lon": s.get("lon"),
                "capital": s.get("capital"),
                "population": s.get("population"),
                "successor": s.get("successor", "india"),
            })
        session.run(query, batch=batch_data)
        count += len(batch_data)
    return count


def create_administered_under_edges(session, states):
    """Create ADMINISTERED_UNDER edges from princely states to Indian Empire."""
    query = """
    UNWIND $batch AS colony_id
    MATCH (ps:Colony {colony_id: colony_id})
    MATCH (raj:Colony {colony_id: $raj_id})
    MERGE (ps)-[:ADMINISTERED_UNDER]->(raj)
    """
    colony_ids = [s["colony_id"] for s in states]
    for i in range(0, len(colony_ids), BATCH_SIZE):
        batch = colony_ids[i:i + BATCH_SIZE]
        session.run(query, batch=batch, raj_id=INDIAN_EMPIRE)
    return len(colony_ids)


def create_evolved_into_edges(session, states):
    """Create EVOLVED_INTO edges to Dominion of India or Pakistan."""
    india_ids = [s["colony_id"] for s in states if s.get("successor") == "india"]
    pakistan_ids = [s["colony_id"] for s in states if s.get("successor") == "pakistan"]

    query = """
    UNWIND $batch AS colony_id
    MATCH (ps:Colony {colony_id: colony_id})
    MATCH (dom:Colony {colony_id: $dom_id})
    MERGE (ps)-[:EVOLVED_INTO]->(dom)
    """

    for i in range(0, len(india_ids), BATCH_SIZE):
        batch = india_ids[i:i + BATCH_SIZE]
        session.run(query, batch=batch, dom_id=DOMINION_INDIA)

    for i in range(0, len(pakistan_ids), BATCH_SIZE):
        batch = pakistan_ids[i:i + BATCH_SIZE]
        session.run(query, batch=batch, dom_id=DOMINION_PAKISTAN)

    return len(india_ids), len(pakistan_ids)


def print_stats(driver):
    """Show princely state statistics."""
    with driver.session() as session:
        r = session.run(
            "MATCH (c:Colony {colony_type: 'Princely State'}) RETURN count(c) AS c"
        ).single()
        print(f"\n  Princely State nodes:          {r['c']}")

        r = session.run(
            "MATCH (c:Colony {colony_type: 'Princely State'})-[:ADMINISTERED_UNDER]->(r) "
            "RETURN count(c) AS c"
        ).single()
        print(f"  ADMINISTERED_UNDER edges:      {r['c']}")

        r = session.run(
            "MATCH (c:Colony {colony_type: 'Princely State'})-[:EVOLVED_INTO]->(d) "
            "RETURN d.name AS dom, count(c) AS c "
            "ORDER BY c DESC"
        )
        for record in r:
            print(f"  EVOLVED_INTO {record['dom']}: {record['c']}")

        r = session.run(
            "MATCH (c:Colony {colony_type: 'Princely State'}) "
            "WHERE c.wikidata_id IS NOT NULL "
            "RETURN count(c) AS c"
        ).single()
        print(f"  With Wikidata QID:             {r['c']}")

        r = session.run(
            "MATCH (c:Colony {colony_type: 'Princely State'}) "
            "WHERE c.latitude IS NOT NULL "
            "RETURN count(c) AS c"
        ).single()
        print(f"  With coordinates:              {r['c']}")


def clear_princely_states(driver):
    """Remove all princely state nodes and their edges."""
    with driver.session() as session:
        r = session.run(
            "MATCH (c:Colony {colony_type: 'Princely State'}) "
            "WHERE c.colony_id <> $placeholder "
            "DETACH DELETE c RETURN count(c) AS c",
            placeholder=PLACEHOLDER
        ).single()
        print(f"  Deleted {r['c']} Princely State Colony nodes (kept placeholder)")


def main():
    parser = argparse.ArgumentParser(
        description="Load princely states into British Empire KG"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without loading")
    parser.add_argument("--clear", action="store_true",
                        help="Remove princely state nodes")
    parser.add_argument("--stats", action="store_true",
                        help="Show current counts")
    args = parser.parse_args()

    data = load_data()
    states = data["states"]

    print(f"Loaded {len(states)} princely states from {DATA_FILE.name}")
    major = [s for s in states if s.get("is_major")]
    print(f"  Major states (for viz): {len(major)}")
    india = [s for s in states if s.get("successor") == "india"]
    pakistan = [s for s in states if s.get("successor") == "pakistan"]
    print(f"  → India: {len(india)}, → Pakistan: {len(pakistan)}")

    if args.dry_run:
        print("\n[DRY RUN] Would create:")
        print(f"  {len(states)} Colony nodes (type: Princely State)")
        print(f"  {len(states)} ADMINISTERED_UNDER edges → Indian Empire")
        print(f"  {len(india)} EVOLVED_INTO edges → Dominion of India")
        print(f"  {len(pakistan)} EVOLVED_INTO edges → Dominion of Pakistan")
        return

    if not NEO4J_PASSWORD:
        print("ERROR: Set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        driver.verify_connectivity()
        print(f"Connected to Neo4j at {NEO4J_URI}")

        if args.clear:
            clear_princely_states(driver)
            return

        if args.stats:
            print_stats(driver)
            return

        with driver.session() as session:
            # Create nodes
            n = create_nodes(session, states)
            print(f"  Created/updated {n} Colony nodes")

            # ADMINISTERED_UNDER → Indian Empire
            n = create_administered_under_edges(session, states)
            print(f"  Created {n} ADMINISTERED_UNDER edges")

            # EVOLVED_INTO → Dominion
            n_india, n_pakistan = create_evolved_into_edges(session, states)
            print(f"  Created {n_india} EVOLVED_INTO → Dominion of India")
            print(f"  Created {n_pakistan} EVOLVED_INTO → Dominion of Pakistan")

        print_stats(driver)

    finally:
        driver.close()


if __name__ == "__main__":
    main()

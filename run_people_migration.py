#!/usr/bin/env python3
"""
Master migration script: Clean up & reload people data with proper namespaces.

Execution order:
  Step 1: Delete HistoricalPerson nodes (cleanup_historical_persons.py)
  Step 2: Parser dedup is done at parse time (parse_lincs_historical_canadians.py)
  Step 3: Load DCB_Person (load_lincs_historical_canadians.py)
  Step 4: Load IIA_Agent (load_indian_affairs_agents.py)
  Step 5: Load WD_ namespace nodes (load_wikidata_people.py)
  Step 6: Cross-namespace linking (link_people_cross_namespace.py)

Usage:
  python run_people_migration.py                    # Run all steps
  python run_people_migration.py --step 1           # Run specific step
  python run_people_migration.py --step 5           # Just WD_ loading
  python run_people_migration.py --step 6           # Just cross-namespace linking
  python run_people_migration.py --skip-cleanup     # Skip step 1 (cleanup)
  python run_people_migration.py --verify           # Just verify final state
"""

import os
import sys
import subprocess


def run_step(description, cmd, cwd=None):
    """Run a step and check for success."""
    print(f"\n{'=' * 60}")
    print(f"  {description}")
    print(f"{'=' * 60}\n")

    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        print(f"\nFAILED: {description}")
        print(f"Command: {' '.join(cmd)}")
        sys.exit(1)
    print(f"\nDONE: {description}")


def verify(neo4j_password):
    """Run verification queries."""
    from neo4j import GraphDatabase

    uri = os.getenv('NEO4J_URI', 'bolt://206.12.90.118:7687')
    driver = GraphDatabase.driver(uri, auth=('neo4j', neo4j_password))

    try:
        with driver.session() as session:
            print("\n" + "=" * 60)
            print("VERIFICATION")
            print("=" * 60)

            labels = [
                'DCB_Person', 'IIA_Agent', 'WD_Person', 'WD_Position',
                'WD_Honour', 'HistoricalPerson', 'IndianAffairsAgent'
            ]
            for label in labels:
                result = session.run(f"MATCH (n:{label}) RETURN count(n) AS cnt")
                cnt = result.single()['cnt']
                suffix = " (should be 0)" if label in ('HistoricalPerson', 'IndianAffairsAgent') else ""
                print(f"  {label}: {cnt:,}{suffix}")

            # Cross-namespace links
            result = session.run("MATCH ()-[r:SAME_AS]->() RETURN count(r) AS cnt")
            print(f"\n  SAME_AS relationships: {result.single()['cnt']:,}")

            # WD relationships
            for rel in ['HELD_POSITION', 'POSITION_IN', 'ASSOCIATED_WITH', 'RECEIVED_HONOUR']:
                result = session.run(f"MATCH ()-[r:{rel}]->() RETURN count(r) AS cnt")
                print(f"  {rel}: {result.single()['cnt']:,}")

            # DCB relationships
            for rel in ['BORN_IN', 'DIED_IN', 'PARENT_OF', 'SPOUSE_OF']:
                result = session.run(f"MATCH (:DCB_Person)-[r:{rel}]-() RETURN count(r) AS cnt")
                print(f"  DCB {rel}: {result.single()['cnt']:,}")

            # IIA relationships
            result = session.run("MATCH (:IIA_Agent)-[r:WORKED_AT]->() RETURN count(r) AS cnt")
            print(f"  IIA WORKED_AT: {result.single()['cnt']:,}")

            # Sample cross-namespace
            print("\nSample cross-namespace paths:")
            result = session.run("""
                MATCH (d:DCB_Person)-[:SAME_AS]->(w:WD_Person)
                RETURN d.name AS dcb, w.name AS wd, w.qid AS qid
                LIMIT 5
            """)
            for rec in result:
                print(f"  DCB:{rec['dcb']} <-> WD:{rec['wd']} ({rec['qid']})")

            result = session.run("""
                MATCH (p:WD_Position)-[:POSITION_IN]->(t:COL_Territory)
                RETURN p.label AS position, t.name AS territory
                LIMIT 5
            """)
            print("\nSample WD_Position -> COL_Territory:")
            for rec in result:
                print(f"  {rec['position']} -> {rec['territory']}")

            print("\n" + "=" * 60)
    finally:
        driver.close()


def main():
    neo4j_password = os.getenv('NEO4J_PASSWORD', '')
    if not neo4j_password:
        print("ERROR: Set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    args = sys.argv[1:]
    specific_step = None
    skip_cleanup = False
    verify_only = False

    i = 0
    while i < len(args):
        if args[i] == '--step' and i + 1 < len(args):
            specific_step = int(args[i + 1])
            i += 2
        elif args[i] == '--skip-cleanup':
            skip_cleanup = True
            i += 1
        elif args[i] == '--verify':
            verify_only = True
            i += 1
        else:
            i += 1

    if verify_only:
        verify(neo4j_password)
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    canada_neo4j = os.path.expanduser('~/CanadaNeo4j')

    steps = {
        1: ("Step 1: Cleanup HistoricalPerson nodes",
            [sys.executable, os.path.join(canada_neo4j, 'scripts/loaders/cleanup_historical_persons.py')]),
        3: ("Step 3: Load DCB_Person nodes",
            [sys.executable, os.path.join(canada_neo4j, 'scripts/loaders/load_lincs_historical_canadians.py')]),
        4: ("Step 4: Load IIA_Agent nodes",
            [sys.executable, os.path.join(canada_neo4j, 'scripts/loaders/load_indian_affairs_agents.py')]),
        5: ("Step 5: Load WD_ namespace nodes",
            [sys.executable, os.path.join(script_dir, 'load_wikidata_people.py')]),
        6: ("Step 6: Cross-namespace linking",
            [sys.executable, os.path.join(script_dir, 'link_people_cross_namespace.py')]),
    }

    if specific_step:
        if specific_step in steps:
            run_step(steps[specific_step][0], steps[specific_step][1])
        else:
            print(f"Unknown step: {specific_step}. Valid: {sorted(steps.keys())}")
            sys.exit(1)
    else:
        # Run all steps in order
        for step_num in sorted(steps.keys()):
            if step_num == 1 and skip_cleanup:
                print(f"\nSkipping Step 1 (--skip-cleanup)")
                continue
            run_step(steps[step_num][0], steps[step_num][1])

    # Always verify at the end
    verify(neo4j_password)


if __name__ == "__main__":
    main()

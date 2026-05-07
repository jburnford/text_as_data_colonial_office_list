#!/usr/bin/env python3
"""
Cross-namespace linking via Wikidata QID matching.

Creates SAME_AS relationships between:
- DCB_Person <-> WD_Person (wikidataQid = qid)
- IIA_Agent <-> WD_Person (wikidataQid = qid)
- IIA_Agent <-> DCB_Person (wikidataQid = wikidataQid)
- WD_Person <-> Person (qid = qid, 6M Wikidata persons)
- DCB_Person <-> Person (wikidataQid = qid)

All links are confidence: 1.0 (exact QID match).
Requires Steps 3-5 to be complete.
"""

import os
import sys
from neo4j import GraphDatabase


def main():
    NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://206.12.90.118:7687')
    NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', '')

    if not NEO4J_PASSWORD:
        print("ERROR: Set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    dry_run = '--dry-run' in sys.argv

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        driver.verify_connectivity()
        print(f"Connected to {NEO4J_URI}")

        print("\n" + "=" * 60)
        print("CROSS-NAMESPACE LINKING (via Wikidata QID)")
        print("=" * 60)

        with driver.session() as session:
            # Pre-flight: check node counts
            for label in ['DCB_Person', 'IIA_Agent', 'WD_Person', 'Person']:
                result = session.run(f"MATCH (n:{label}) RETURN count(n) as cnt")
                cnt = result.single()['cnt']
                print(f"  {label}: {cnt:,}")

            links = [
                {
                    'name': 'DCB_Person <-> WD_Person',
                    'query': """
                        MATCH (d:DCB_Person)
                        WHERE d.wikidataQid IS NOT NULL
                        MATCH (w:WD_Person {qid: d.wikidataQid})
                        MERGE (d)-[r:SAME_AS]->(w)
                        SET r.method = 'qid_match', r.confidence = 1.0
                        RETURN count(r) as count
                    """,
                },
                {
                    'name': 'IIA_Agent <-> WD_Person',
                    'query': """
                        MATCH (a:IIA_Agent)
                        WHERE a.wikidataQid IS NOT NULL
                        MATCH (w:WD_Person {qid: a.wikidataQid})
                        MERGE (a)-[r:SAME_AS]->(w)
                        SET r.method = 'qid_match', r.confidence = 1.0
                        RETURN count(r) as count
                    """,
                },
                {
                    'name': 'IIA_Agent <-> DCB_Person',
                    'query': """
                        MATCH (a:IIA_Agent)
                        WHERE a.wikidataQid IS NOT NULL
                        MATCH (d:DCB_Person {wikidataQid: a.wikidataQid})
                        MERGE (a)-[r:SAME_AS]->(d)
                        SET r.method = 'qid_match', r.confidence = 1.0
                        RETURN count(r) as count
                    """,
                },
                {
                    'name': 'WD_Person <-> Person (6M Wikidata)',
                    'query': """
                        MATCH (w:WD_Person)
                        MATCH (p:Person {qid: w.qid})
                        MERGE (w)-[r:SAME_AS]->(p)
                        SET r.method = 'qid_match', r.confidence = 1.0
                        RETURN count(r) as count
                    """,
                },
                {
                    'name': 'DCB_Person <-> Person (6M Wikidata)',
                    'query': """
                        MATCH (d:DCB_Person)
                        WHERE d.wikidataQid IS NOT NULL
                        MATCH (p:Person {qid: d.wikidataQid})
                        MERGE (d)-[r:SAME_AS]->(p)
                        SET r.method = 'qid_match', r.confidence = 1.0
                        RETURN count(r) as count
                    """,
                },
            ]

            total_links = 0
            for link in links:
                print(f"\n{link['name']}...")
                if dry_run:
                    # Count potential matches
                    count_query = link['query'].replace(
                        'MERGE (d)-[r:SAME_AS]->(w)\n                        SET r.method = \'qid_match\', r.confidence = 1.0\n                        RETURN count(r) as count',
                        'RETURN count(*) as count'
                    ).replace(
                        'MERGE (a)-[r:SAME_AS]->(w)\n                        SET r.method = \'qid_match\', r.confidence = 1.0\n                        RETURN count(r) as count',
                        'RETURN count(*) as count'
                    ).replace(
                        'MERGE (a)-[r:SAME_AS]->(d)\n                        SET r.method = \'qid_match\', r.confidence = 1.0\n                        RETURN count(r) as count',
                        'RETURN count(*) as count'
                    ).replace(
                        'MERGE (w)-[r:SAME_AS]->(p)\n                        SET r.method = \'qid_match\', r.confidence = 1.0\n                        RETURN count(r) as count',
                        'RETURN count(*) as count'
                    ).replace(
                        'MERGE (d)-[r:SAME_AS]->(p)\n                        SET r.method = \'qid_match\', r.confidence = 1.0\n                        RETURN count(r) as count',
                        'RETURN count(*) as count'
                    )
                    print(f"  [DRY RUN] would create links (exact count requires execution)")
                else:
                    result = session.run(link['query'])
                    count = result.single()['count']
                    total_links += count
                    print(f"  Created {count:,} SAME_AS links")

            print(f"\n{'=' * 60}")
            print(f"Total cross-namespace links: {total_links:,}")

            # Verification: sample cross-namespace paths
            if not dry_run and total_links > 0:
                print("\nSample cross-namespace connections:")
                result = session.run("""
                    MATCH (d:DCB_Person)-[:SAME_AS]->(w:WD_Person)
                    WHERE d.name IS NOT NULL
                    RETURN d.name AS dcb_name, d.dcbId AS dcbId,
                           w.qid AS wd_qid, w.name AS wd_name
                    LIMIT 5
                """)
                for rec in result:
                    print(f"  DCB: {rec['dcb_name']} ({rec['dcbId']}) <-> WD: {rec['wd_name']} ({rec['wd_qid']})")

            print("=" * 60)

    finally:
        driver.close()


if __name__ == "__main__":
    main()

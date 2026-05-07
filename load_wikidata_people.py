#!/usr/bin/env python3
"""
Load Wikidata colonial people into Neo4j as WD_ namespace nodes.

Creates:
- WD_Person nodes (34,594 from merged_all_people.json)
- WD_Position nodes (~2,136 unique positions)
- WD_Honour nodes (6 honours)
- HELD_POSITION relationships (WD_Person -> WD_Position)
- POSITION_IN relationships (WD_Position -> COL_Territory)
- ASSOCIATED_WITH relationships (WD_Person -> COL_Territory)
- RECEIVED_HONOUR relationships (WD_Person -> WD_Honour)

Namespace: WD_ (Wikidata Colonial People)
"""

import json
import os
import re
import sys
from neo4j import GraphDatabase
from tqdm import tqdm


BATCH_SIZE = 500

# The 6 honours we track
HONOURS = {
    "Q12177423": "GCMG - Knight Grand Cross of St Michael and St George",
    "Q12177415": "KCMG - Knight Commander of St Michael and St George",
    "Q12177413": "CMG - Companion of St Michael and St George",
    "Q93710": "Order of the Indian Empire (overall)",
    "Q1330936": "Order of the Star of India (overall)",
    "Q1810753": "Imperial Service Order",
}


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def extract_birth_year(people_data):
    """Extract birth/death years from associations or description."""
    birth_year = None
    death_year = None

    # Try associations first
    for assoc in people_data.get('associations', []):
        if assoc.get('birth'):
            m = re.search(r'(\d{4})', str(assoc['birth']))
            if m:
                birth_year = int(m.group(1))
        if assoc.get('death'):
            m = re.search(r'(\d{4})', str(assoc['death']))
            if m:
                death_year = int(m.group(1))
        if birth_year:
            break

    # Fallback: parse description for year ranges like (1814-1877)
    if not birth_year and people_data.get('description'):
        m = re.search(r'\((\d{4})[–-](\d{4})\)', people_data['description'])
        if m:
            birth_year = int(m.group(1))
            death_year = int(m.group(2))

    return birth_year, death_year


def classify_era(birth_year):
    """Classify person into era based on birth year."""
    if birth_year is None:
        return None
    if birth_year < 1900:
        return "colonial"
    elif birth_year <= 1970:
        return "late_colonial"
    else:
        return "modern"


class WikidataPeopleLoader:
    def __init__(self, uri: str, user: str, password: str, database: str = "neo4j"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.database = database

    def close(self):
        self.driver.close()

    def create_indexes(self):
        """Create constraints and indexes for WD_ nodes."""
        print("\nCreating WD_ indexes...")

        with self.driver.session(database=self.database) as session:
            indexes = [
                "CREATE CONSTRAINT wd_person_qid IF NOT EXISTS FOR (p:WD_Person) REQUIRE p.qid IS UNIQUE",
                "CREATE CONSTRAINT wd_position_qid IF NOT EXISTS FOR (p:WD_Position) REQUIRE p.qid IS UNIQUE",
                "CREATE CONSTRAINT wd_honour_qid IF NOT EXISTS FOR (h:WD_Honour) REQUIRE h.qid IS UNIQUE",
                "CREATE INDEX wd_person_name IF NOT EXISTS FOR (p:WD_Person) ON (p.name)",
                "CREATE INDEX wd_person_era IF NOT EXISTS FOR (p:WD_Person) ON (p.era)",
            ]
            for idx in indexes:
                try:
                    session.run(idx)
                    print(f"  {idx.split('IF')[0].strip()[:70]}...")
                except Exception as e:
                    print(f"  WARNING: {str(e)[:100]}")

    def load_persons(self, merged_file: str):
        """Phase 1: Load WD_Person nodes from merged_all_people.json."""
        print(f"\nLoading WD_Person nodes from {merged_file}...")

        with open(merged_file, 'r', encoding='utf-8') as f:
            people = json.load(f)

        print(f"Found {len(people):,} people")

        total = 0
        with self.driver.session(database=self.database) as session:
            for batch in tqdm(list(chunks(people, BATCH_SIZE)), desc="Loading WD_Person"):
                person_batch = []
                for p in batch:
                    birth_year, death_year = extract_birth_year(p)
                    era = classify_era(birth_year)

                    person_batch.append({
                        'qid': p['qid'],
                        'name': p['name'],
                        'description': p.get('description', ''),
                        'sources': p.get('sources', []),
                        'era': era,
                        'birthYear': birth_year,
                        'deathYear': death_year,
                    })

                result = session.run("""
                    UNWIND $batch AS person
                    MERGE (p:WD_Person {qid: person.qid})
                    SET p.name = person.name,
                        p.description = person.description,
                        p.sources = person.sources,
                        p.era = person.era,
                        p.birthYear = person.birthYear,
                        p.deathYear = person.deathYear
                    RETURN count(p) as count
                """, batch=person_batch)
                total += result.single()['count']

        print(f"Created {total:,} WD_Person nodes")
        return total

    def load_positions(self, merged_file: str):
        """Phase 2: Load WD_Position nodes (unique positions from all people)."""
        print("\nExtracting unique positions...")

        with open(merged_file, 'r', encoding='utf-8') as f:
            people = json.load(f)

        positions = {}
        for p in people:
            for pos in p.get('positions', []):
                qid = pos.get('position_qid')
                if qid and qid not in positions:
                    positions[qid] = pos.get('position_label', '')

        print(f"Found {len(positions):,} unique positions")

        pos_list = [{'qid': qid, 'label': label} for qid, label in positions.items()]

        total = 0
        with self.driver.session(database=self.database) as session:
            for batch in tqdm(list(chunks(pos_list, BATCH_SIZE)), desc="Loading WD_Position"):
                result = session.run("""
                    UNWIND $batch AS pos
                    MERGE (p:WD_Position {qid: pos.qid})
                    SET p.label = pos.label
                    RETURN count(p) as count
                """, batch=batch)
                total += result.single()['count']

        print(f"Created {total:,} WD_Position nodes")
        return total

    def load_honours(self):
        """Phase 3: Load WD_Honour nodes (6 honours)."""
        print("\nLoading WD_Honour nodes...")

        honours_list = [{'qid': qid, 'label': label} for qid, label in HONOURS.items()]

        with self.driver.session(database=self.database) as session:
            result = session.run("""
                UNWIND $batch AS h
                MERGE (hon:WD_Honour {qid: h.qid})
                SET hon.label = h.label
                RETURN count(hon) as count
            """, batch=honours_list)
            total = result.single()['count']

        print(f"Created {total:,} WD_Honour nodes")
        return total

    def create_held_position_rels(self, merged_file: str):
        """Phase 4: Create HELD_POSITION relationships (WD_Person -> WD_Position)."""
        print("\nCreating HELD_POSITION relationships...")

        with open(merged_file, 'r', encoding='utf-8') as f:
            people = json.load(f)

        # Collect all person-position pairs
        held_rels = []
        for p in people:
            for pos in p.get('positions', []):
                if pos.get('position_qid'):
                    held_rels.append({
                        'person_qid': p['qid'],
                        'position_qid': pos['position_qid'],
                        'start': pos.get('start', ''),
                        'end': pos.get('end', ''),
                        'colony_qid': pos.get('colony_qid', ''),
                        'colony_name': pos.get('colony_name', ''),
                        'source': pos.get('source', ''),
                    })

        print(f"Found {len(held_rels):,} person-position records")

        total = 0
        with self.driver.session(database=self.database) as session:
            for batch in tqdm(list(chunks(held_rels, BATCH_SIZE)), desc="HELD_POSITION"):
                result = session.run("""
                    UNWIND $batch AS rel
                    MATCH (p:WD_Person {qid: rel.person_qid})
                    MATCH (pos:WD_Position {qid: rel.position_qid})
                    MERGE (p)-[r:HELD_POSITION {start: rel.start, position_qid: rel.position_qid}]->(pos)
                    SET r.end = rel.end,
                        r.colony_qid = rel.colony_qid,
                        r.colony_name = rel.colony_name,
                        r.source = rel.source
                    RETURN count(r) as count
                """, batch=batch)
                total += result.single()['count']

        print(f"Created {total:,} HELD_POSITION relationships")
        return total

    def create_position_in_territory_rels(self):
        """Phase 5: Create POSITION_IN relationships (WD_Position -> COL_Territory via wikidata_id)."""
        print("\nCreating POSITION_IN relationships...")

        with self.driver.session(database=self.database) as session:
            # Link via colony_qid on HELD_POSITION relationships
            result = session.run("""
                MATCH (p:WD_Person)-[hp:HELD_POSITION]->(pos:WD_Position)
                WHERE hp.colony_qid IS NOT NULL AND hp.colony_qid <> ''
                MATCH (t:COL_Territory {wikidata_id: hp.colony_qid})
                MERGE (pos)-[r:POSITION_IN]->(t)
                RETURN count(DISTINCT r) as count
            """)
            total = result.single()['count']

        print(f"Created {total:,} POSITION_IN relationships")
        return total

    def create_associated_with_rels(self, merged_file: str):
        """Phase 6: Create ASSOCIATED_WITH relationships (WD_Person -> COL_Territory)."""
        print("\nCreating ASSOCIATED_WITH relationships...")

        with open(merged_file, 'r', encoding='utf-8') as f:
            people = json.load(f)

        assoc_rels = []
        for p in people:
            for assoc in p.get('associations', []):
                if assoc.get('colony_qid'):
                    assoc_rels.append({
                        'person_qid': p['qid'],
                        'colony_qid': assoc['colony_qid'],
                        'association_type': assoc.get('association', ''),
                    })

        print(f"Found {len(assoc_rels):,} person-territory associations")

        total = 0
        with self.driver.session(database=self.database) as session:
            for batch in tqdm(list(chunks(assoc_rels, BATCH_SIZE)), desc="ASSOCIATED_WITH"):
                result = session.run("""
                    UNWIND $batch AS rel
                    MATCH (p:WD_Person {qid: rel.person_qid})
                    MATCH (t:COL_Territory {wikidata_id: rel.colony_qid})
                    MERGE (p)-[r:ASSOCIATED_WITH {type: rel.association_type}]->(t)
                    RETURN count(r) as count
                """, batch=batch)
                total += result.single()['count']

        print(f"Created {total:,} ASSOCIATED_WITH relationships")
        return total

    def create_honour_rels(self, honours_file: str):
        """Phase 7: Create RECEIVED_HONOUR relationships (WD_Person -> WD_Honour)."""
        print(f"\nCreating RECEIVED_HONOUR relationships from {honours_file}...")

        with open(honours_file, 'r', encoding='utf-8') as f:
            records = json.load(f)

        # Deduplicate: one person-honour pair
        seen = set()
        honour_rels = []
        for rec in records:
            key = (rec['person_qid'], rec['honour_qid'])
            if key not in seen and rec['honour_qid'] in HONOURS:
                seen.add(key)
                honour_rels.append({
                    'person_qid': rec['person_qid'],
                    'honour_qid': rec['honour_qid'],
                })

        print(f"Found {len(honour_rels):,} unique person-honour pairs")

        total = 0
        with self.driver.session(database=self.database) as session:
            for batch in tqdm(list(chunks(honour_rels, BATCH_SIZE)), desc="RECEIVED_HONOUR"):
                result = session.run("""
                    UNWIND $batch AS rel
                    MATCH (p:WD_Person {qid: rel.person_qid})
                    MATCH (h:WD_Honour {qid: rel.honour_qid})
                    MERGE (p)-[r:RECEIVED_HONOUR]->(h)
                    RETURN count(r) as count
                """, batch=batch)
                total += result.single()['count']

        print(f"Created {total:,} RECEIVED_HONOUR relationships")
        return total

    def print_statistics(self):
        """Print statistics about the WD_ import."""
        print("\n" + "=" * 60)
        print("WD_ NAMESPACE IMPORT STATISTICS")
        print("=" * 60)

        with self.driver.session(database=self.database) as session:
            for label in ['WD_Person', 'WD_Position', 'WD_Honour']:
                result = session.run(f"MATCH (n:{label}) RETURN count(n) as count")
                print(f"  {label}: {result.single()['count']:,}")

            for rel_type in ['HELD_POSITION', 'POSITION_IN', 'ASSOCIATED_WITH', 'RECEIVED_HONOUR']:
                result = session.run(f"MATCH ()-[r:{rel_type}]->() RETURN count(r) as count")
                print(f"  {rel_type}: {result.single()['count']:,}")

            # Era breakdown
            result = session.run("""
                MATCH (p:WD_Person)
                RETURN p.era AS era, count(p) AS cnt
                ORDER BY cnt DESC
            """)
            print("\nEra breakdown:")
            for rec in result:
                print(f"  {rec['era'] or 'unknown'}: {rec['cnt']:,}")

            # Top positions
            result = session.run("""
                MATCH (pos:WD_Position)<-[r:HELD_POSITION]-()
                RETURN pos.label AS position, count(r) AS holders
                ORDER BY holders DESC LIMIT 10
            """)
            print("\nTop 10 positions:")
            for rec in result:
                print(f"  {rec['position']}: {rec['holders']:,} holders")

            # Positions linked to COL_Territory
            result = session.run("""
                MATCH (pos:WD_Position)-[:POSITION_IN]->(t:COL_Territory)
                RETURN t.name AS territory, count(pos) AS positions
                ORDER BY positions DESC LIMIT 10
            """)
            print("\nTop territories by positions linked:")
            for rec in result:
                print(f"  {rec['territory']}: {rec['positions']:,} positions")

        print("=" * 60)

    def run_import(self, merged_file: str, honours_file: str):
        """Execute complete WD_ import."""
        print("=" * 60)
        print("IMPORTING WD_ NAMESPACE (Wikidata Colonial People)")
        print("=" * 60)

        self.create_indexes()
        self.load_persons(merged_file)
        self.load_positions(merged_file)
        self.load_honours()
        self.create_held_position_rels(merged_file)
        self.create_position_in_territory_rels()
        self.create_associated_with_rels(merged_file)
        self.create_honour_rels(honours_file)
        self.print_statistics()

        print("\nWD_ namespace import complete!")


def main():
    NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://206.12.90.118:7687')
    NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', '')

    if not NEO4J_PASSWORD:
        print("ERROR: Set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    # Default paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    merged_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join(script_dir, 'wikidata_harvest', 'merged_all_people.json')
    honours_file = sys.argv[2] if len(sys.argv) > 2 else os.path.join(script_dir, 'wikidata_harvest', 'honours_recipients.json')

    loader = WikidataPeopleLoader(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
    try:
        loader.run_import(merged_file, honours_file)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        loader.close()


if __name__ == "__main__":
    main()

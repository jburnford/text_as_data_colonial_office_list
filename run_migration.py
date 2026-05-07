#!/usr/bin/env python3
"""Run the KG migration against live Neo4j, phase by phase."""

from neo4j import GraphDatabase

# Load password from .env
with open('/home/jic823/textasdatacolonialofficelist/.env') as f:
    for line in f:
        if line.startswith('NEO4J_PASSWORD='):
            pw = line.split('=', 1)[1].strip()

driver = GraphDatabase.driver('bolt://206.12.90.118:7687', auth=('neo4j', pw))


def run(label, query):
    """Run a single Cypher statement and report results."""
    with driver.session() as s:
        result = s.run(query)
        summary = result.consume()
        print(f"  {label}: {summary.counters}")


def run_return(label, query):
    """Run a query and print returned rows."""
    with driver.session() as s:
        result = s.run(query)
        rows = [dict(r) for r in result]
        for row in rows[:20]:
            print(f"  {row}")
        if len(rows) > 20:
            print(f"  ... and {len(rows)-20} more")


# ── PHASE 1: Add HistoricalTerritory base label ──
print("\n=== PHASE 1: Add :HistoricalTerritory base label ===")
run("Add label", "MATCH (c:Colony) SET c:HistoricalTerritory")

# ── PHASE 2: Add specific labels ──
print("\n=== PHASE 2: Add specific labels ===")

phase2 = [
    ("PrincelyState (remove Colony)",
     "MATCH (c:Colony) WHERE c.colony_type = 'Princely State' SET c:PrincelyState REMOVE c:Colony"),
    ("CrownColony",
     "MATCH (c:Colony) WHERE c.administrative_status IN ['Crown Colony', 'Crown colony', 'Royal Colony'] SET c:CrownColony"),
    ("Protectorate",
     "MATCH (c:Colony) WHERE c.administrative_status IN ['Protectorate', 'Colony/Protectorate', 'Occupation/Protectorate'] SET c:Protectorate"),
    ("Dominion",
     "MATCH (c:Colony) WHERE c.administrative_status = 'Dominion' SET c:Dominion"),
    ("Mandate",
     "MATCH (c:Colony) WHERE c.administrative_status IN ['Mandate', 'Mandate/Trust Territory', 'Trust Territory'] SET c:Mandate"),
    ("IndependentNation (remove Colony)",
     "MATCH (c:Colony) WHERE c.administrative_status IN ['Independence', 'Unilateral Independence'] SET c:IndependentNation REMOVE c:Colony"),
    ("MinorTerritory",
     "MATCH (c:Colony) WHERE c.administrative_status IN ['Guano Island', 'Whaling Station', 'Remote Island'] SET c:MinorTerritory"),
    ("CompanyTerritory",
     "MATCH (c:Colony) WHERE c.administrative_status IN ['Company Territory', 'Trading Post', 'Company Settlement'] SET c:CompanyTerritory"),
    ("BoerRepublic (remove Colony)",
     "MATCH (c:Colony) WHERE c.administrative_status = 'Boer Republic' SET c:BoerRepublic REMOVE c:Colony"),
    ("Federation",
     "MATCH (c:Colony) WHERE c.administrative_status IN ['Federation', 'Federal Colony'] SET c:Federation"),
    ("Province",
     "MATCH (c:Colony) WHERE c.administrative_status IN ['Province', 'Presidency', 'United Province', 'Division of a Presidency'] SET c:Province"),
    ("Dependency",
     "MATCH (c:Colony) WHERE c.administrative_status = 'Dependency' SET c:Dependency"),
    ("OverseasTerritory",
     "MATCH (c:Colony) WHERE c.administrative_status = 'British Overseas Territory' SET c:OverseasTerritory"),
    ("Condominium",
     "MATCH (c:Colony) WHERE c.administrative_status IN ['Condominium', 'Anglo-French Condominium'] SET c:Condominium"),
    ("MilitaryAdministration",
     "MATCH (c:Colony) WHERE c.administrative_status = 'Military Administration' SET c:MilitaryAdministration"),
]

for label, q in phase2:
    run(label, q)

# Verify labels
print("\n  Label distribution:")
run_return("Labels", "MATCH (n:HistoricalTerritory) RETURN labels(n) AS labels, count(n) AS cnt ORDER BY cnt DESC")

# ── PHASE 3: Refactor EVOLVED_INTO relationships ──
print("\n=== PHASE 3: Refactor EVOLVED_INTO with relationship_type ===")

evolved_mappings = [
    ('BECAME_INDEPENDENT', ['BECAME_INDEPENDENT', 'INDEPENDENCE_GRANTED', 'INDEPENDENCE_RESTORED']),
    ('MERGED_INTO', ['MERGED_INTO', 'MERGED_WITH', 'BECAME_PART_OF', 'AMALGAMATED_INTO']),
    ('INCORPORATED_INTO', ['INCORPORATED_INTO']),
    ('REORGANIZED_AS', ['REORGANIZED_AS', 'RENAMED_TO', 'EXPANDED_TO', 'EXPANDED_WITH_PROTECTORATE',
                        'CONSOLIDATED_AS_PROVINCE', 'INTERNAL_SETTLEMENT']),
    ('BECAME_CROWN_COLONY', ['BECAME_CROWN_COLONY']),
    ('BECAME_COLONY', ['BECAME_COLONY', 'FORMALIZED_AS_COLONY']),
    ('BECAME_PROTECTORATE', ['BECAME_PROTECTORATE']),
    ('BECAME_MANDATE', ['BECAME_MANDATE']),
    ('BECAME_SEPARATE_COLONY', ['BECAME_SEPARATE_COLONY']),
    ('BECAME_SELF_GOVERNING', ['BECAME_SELF_GOVERNING']),
    ('FEDERATED_INTO', ['FEDERATED_INTO', 'CONFEDERATED_INTO', 'JOINED_FEDERATION',
                        'JOINED_CONFEDERATION', 'JOINED', 'FEDERATION_SUCCESSION']),
    ('PARTITIONED_INTO', ['PARTITIONED_INTO', 'PARTITIONED_TO', 'SEPARATED_INTO',
                          'CARVED_OUT', 'SEPARATED_FROM', 'SEPARATED_FROM_INDIA']),
    ('TRANSFERRED_SOVEREIGNTY', ['TRANSFERRED_TO_CROWN', 'TRANSFERRED_TO_AUSTRALIA', 'CONQUERED_BY',
                                  'CONQUERED_AND_RENAMED', 'RETURNED_TO', 'RESTORED_TO_CROWN', 'ANNEXED_BY']),
    ('REUNITED_INTO', ['REUNITED_INTO']),
]

for new_type, old_types in evolved_mappings:
    q = f"""
    MATCH (a)-[r:EVOLVED_INTO]->(b)
    WHERE r.relationship_type IN {old_types}
    CREATE (a)-[:{new_type} {{description: r.description, year: r.year, detail: r.relationship_type}}]->(b)
    DELETE r
    """
    run(f"EVOLVED_INTO → {new_type}", q)

# Handle DIRECT_SUCCESSION (keep as EVOLVED_INTO but clean property)
run("EVOLVED_INTO (DIRECT_SUCCESSION)", """
    MATCH (a)-[r:EVOLVED_INTO]->(b)
    WHERE r.relationship_type = 'DIRECT_SUCCESSION'
    CREATE (a)-[:EVOLVED_INTO {description: r.description, year: r.year, detail: 'DIRECT_SUCCESSION'}]->(b)
    DELETE r
""")

# ── PHASE 3b: Refactor SUCCESSOR_TO → SUCCEEDED ──
print("\n=== PHASE 3b: Refactor SUCCESSOR_TO → SUCCEEDED ===")

# All SUCCESSOR_TO with relationship_type
run("SUCCESSOR_TO (with props) → SUCCEEDED", """
    MATCH (a)-[r:SUCCESSOR_TO]->(b)
    WHERE r.relationship_type IS NOT NULL
    CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: r.relationship_type, succession_type: r.succession_type}]->(b)
    DELETE r
""")

# Bare SUCCESSOR_TO
run("SUCCESSOR_TO (bare) → SUCCEEDED", """
    MATCH (a)-[r:SUCCESSOR_TO]->(b)
    WHERE r.relationship_type IS NULL
    CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year}]->(b)
    DELETE r
""")

# ── PHASE 3c: Clean BORDERS_WITH and NEAR_COAST_OF ──
print("\n=== PHASE 3c: Clean spatial relationships ===")
run("BORDERS_WITH cleanup", "MATCH ()-[r:BORDERS_WITH]->() WHERE r.relationship_type IS NOT NULL REMOVE r.relationship_type")
run("NEAR_COAST_OF cleanup", "MATCH ()-[r:NEAR_COAST_OF]->() WHERE r.relationship_type IS NOT NULL REMOVE r.relationship_type")

# Verify relationships
print("\n  Relationship distribution:")
run_return("Rels", "MATCH ()-[r]->() RETURN type(r) AS type, count(r) AS cnt ORDER BY cnt DESC")

# ── PHASE 4: Data type casting ──
print("\n=== PHASE 4: Cast data types ===")

# Cast string lat/lon to float (without APOC type check — just try toFloat)
run("Cast lat/lon", """
    MATCH (c:HistoricalTerritory)
    WHERE c.latitude IS NOT NULL AND c.longitude IS NOT NULL
    SET c.latitude = toFloat(c.latitude),
        c.longitude = toFloat(c.longitude),
        c.location = point({latitude: toFloat(c.latitude), longitude: toFloat(c.longitude)})
""")

# ── PHASE 5: Princely State established_year → dynasty_founded ──
print("\n=== PHASE 5: Rename established_year → dynasty_founded for Princely States ===")
run("Rename field", """
    MATCH (c:PrincelyState)
    WHERE c.established_year IS NOT NULL
    SET c.dynasty_founded = c.established_year
    REMOVE c.established_year
""")

# ── PHASE 6: Resolve QID names ──
print("\n=== PHASE 6: Resolve QID-only names ===")

qid_names = {
    'Q101242542': 'Kadana State',
    'Q104152112': 'Surat State',
    'Q104152114': 'Yasin State',
    'Q11904734': 'Alaniawas',
    'Q11905355': 'Ammayanayakan',
    'Q11905439': 'Anakapalle',
    'Q11905698': 'Antarbella',
    'Q11908900': 'Bedam',
    'Q131080302': 'Sudasana State',
    'Q134436280': 'Bilkha',
    'Q1632695': 'Sanjeli State',
    'Q21044436': 'Edappalli',
    'Q21075438': 'Gopalpet',
    'Q21075439': 'Kaddatanad',
    'Q48838868': 'Tharad State',
    'Q48838869': 'Wao State',
    'Q48838872': 'Santalpur State',
    'Q48838989': 'Sarila State',
}

for qid, name in qid_names.items():
    run(f"{qid} → {name}", f"MATCH (c:HistoricalTerritory {{wikidata_id: '{qid}'}}) SET c.name = '{name}'")

# ── PHASE 7: Update constraints ──
print("\n=== PHASE 7: Update constraints ===")
try:
    run("Drop old constraint", "DROP CONSTRAINT colony_id_unique IF EXISTS")
except Exception as e:
    print(f"  Warning: {e}")

run("Create new constraint", "CREATE CONSTRAINT territory_id_unique IF NOT EXISTS FOR (n:HistoricalTerritory) REQUIRE n.colony_id IS UNIQUE")

# ── Final verification ──
print("\n=== FINAL VERIFICATION ===")
print("\nLabel counts:")
run_return("Labels", "MATCH (n:HistoricalTerritory) RETURN labels(n) AS labels, count(n) AS cnt ORDER BY cnt DESC")
print("\nRelationship counts:")
run_return("Rels", "MATCH ()-[r]->() RETURN type(r) AS type, count(r) AS cnt ORDER BY cnt DESC")
print("\nRemaining EVOLVED_INTO with relationship_type (should be 0):")
run_return("Check", "MATCH ()-[r:EVOLVED_INTO]->() WHERE r.relationship_type IS NOT NULL RETURN r.relationship_type, count(r) AS cnt")
print("\nRemaining SUCCESSOR_TO (should be 0):")
run_return("Check", "MATCH ()-[r:SUCCESSOR_TO]->() RETURN count(r) AS cnt")
print("\nQID-only names remaining (should be 0):")
run_return("Check", "MATCH (c:HistoricalTerritory) WHERE c.name STARTS WITH 'Q' AND c.name =~ 'Q\\\\d+' RETURN c.name, c.colony_id")

driver.close()
print("\n✓ Migration complete.")

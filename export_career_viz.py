#!/usr/bin/env python3
"""Export COL_Person career data for visualization."""

import json
import os
from pathlib import Path
from neo4j import GraphDatabase

REPO_DIR = Path(__file__).parent

def _load_dotenv():
    env_path = REPO_DIR / ".env"
    if env_path.exists():
        for line in open(env_path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip())

_load_dotenv()

driver = GraphDatabase.driver(
    os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687"),
    auth=("neo4j", os.environ["NEO4J_PASSWORD"]),
)

# Fetch all persons with their stints
with driver.session() as s:
    result = s.run("""
        MATCH (p:COL_Person)-[cs:CAREER_STINT]->(o:COL_Official)
        OPTIONAL MATCH (p)-[:SAME_AS]->(w:WD_Person)
        WITH p, o, cs, collect(DISTINCT w.qid)[0] AS wd_qid,
             collect(DISTINCT w.name)[0] AS wd_name
        ORDER BY o.first_year
        WITH p, wd_qid, wd_name,
             collect({
                id: o.id,
                colony: o.colony,
                first_year: o.first_year,
                last_year: o.last_year,
                num_editions: o.num_editions
             }) AS stints
        RETURN p.id AS person_id, p.name AS name,
               p.colonies AS colonies,
               p.first_year AS first_year, p.last_year AS last_year,
               p.num_stints AS num_stints,
               size(p.colonies) AS n_colonies,
               wd_qid, wd_name,
               stints
        ORDER BY size(p.colonies) DESC, p.num_stints DESC
    """)
    persons = [dict(r) for r in result]

# Fetch POSSIBLE_MATCH edges between officials in person nodes
with driver.session() as s:
    result = s.run("""
        MATCH (p:COL_Person)-[:CAREER_STINT]->(a:COL_Official)
        MATCH (p)-[:CAREER_STINT]->(b:COL_Official)
        MATCH (a)-[r:POSSIBLE_MATCH]-(b)
        WHERE a.id < b.id
        RETURN DISTINCT a.id AS source, b.id AS target,
               r.uncertainty AS uncertainty,
               a.colony AS source_colony, b.colony AS target_colony
    """)
    edges = [dict(r) for r in result]

# Collect unique colonies and assign colors
all_colonies = set()
for p in persons:
    for stint in p["stints"]:
        all_colonies.add(stint["colony"])

# Region-based color mapping
REGION_COLORS = {
    "west_africa": "#e6550d",
    "east_africa": "#31a354",
    "southern_africa": "#756bb1",
    "caribbean": "#3182bd",
    "pacific": "#e7298a",
    "southeast_asia": "#66a61e",
    "mediterranean": "#e7ba52",
    "canada_aus_nz": "#636363",
    "other": "#969696",
}

COLONY_REGIONS = {}
_regions = {
    "west_africa": ["Gold Coast", "Sierra Leone", "Gambia", "Nigeria", "Lagos",
                    "Northern Nigeria", "Southern Nigeria", "Togoland", "Cameroons"],
    "east_africa": ["Kenya", "Uganda", "Tanganyika", "Zanzibar", "British Somaliland",
                    "Nyasaland", "Aden", "Somaliland"],
    "southern_africa": ["South Africa", "Southern Rhodesia", "Northern Rhodesia",
                        "Rhodesia", "Swaziland", "Basutoland", "Bechuanaland",
                        "High Commission Territories", "Central Africa",
                        "Cape of Good Hope", "Natal"],
    "caribbean": ["Jamaica", "Trinidad", "Trinidad and Tobago", "Barbados",
                  "British Guiana", "British Honduras", "Bahamas", "Bermuda",
                  "Leeward Islands", "Windward Islands", "Antigua", "Dominica",
                  "Grenada", "St Lucia", "St Vincent", "St Kitts-Nevis",
                  "St Christopher and Nevis", "Montserrat", "Virgin Islands",
                  "Tobago", "Turks and Caicos Islands", "Cayman Islands",
                  "West Indies"],
    "pacific": ["Fiji", "Western Pacific", "Gilbert and Ellice Islands",
                "British Solomon Islands", "Tonga", "British New Guinea", "Papua"],
    "southeast_asia": ["Straits Settlements", "Federated Malay States",
                       "Hong Kong", "Ceylon", "North Borneo", "Sarawak",
                       "Brunei", "Labuan", "Singapore", "Federation of Malaya",
                       "Unfederated Malay States", "Johore", "Malaya"],
    "mediterranean": ["Cyprus", "Malta", "Gibraltar", "Palestine",
                      "Transjordan", "Mauritius", "Seychelles"],
    "canada_aus_nz": ["Canada", "Australia", "New Zealand", "New South Wales",
                      "Queensland", "South Australia", "Tasmania", "Victoria",
                      "Western Australia", "Newfoundland"],
}

for region, colonies in _regions.items():
    for c in colonies:
        COLONY_REGIONS[c] = region

colony_colors = {}
for colony in sorted(all_colonies):
    region = COLONY_REGIONS.get(colony, "other")
    colony_colors[colony] = REGION_COLORS[region]

data = {
    "persons": persons,
    "edges": edges,
    "colony_colors": colony_colors,
    "regions": {r: c for r, c in REGION_COLORS.items()},
}

out_path = REPO_DIR / "career_viz_data.json"
with open(out_path, "w") as f:
    json.dump(data, f, indent=1)

print(f"Exported {len(persons)} persons, {len(edges)} edges")
print(f"  {len(all_colonies)} unique colonies")
print(f"  Multi-colony: {sum(1 for p in persons if p['n_colonies'] > 1)}")
print(f"  Wikidata-linked: {sum(1 for p in persons if p['wd_qid'])}")
print(f"  Written to {out_path}")

driver.close()

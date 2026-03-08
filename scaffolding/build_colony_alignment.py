#!/usr/bin/env python3
"""
Colony Alignment Table Builder
==============================

Maps the 150 canonical extraction names (from build_corpus_inventory.py)
to the 288 Colony nodes in the British Empire Knowledge Graph (Neo4j),
including Wikidata QIDs and modern nation QIDs.

This alignment table bridges the extraction pipeline to the knowledge graph,
enabling clean data loading downstream.

Usage:
    python scaffolding/build_colony_alignment.py

Output:
    scaffolding/colony_alignment.json   — Full alignment data
    scaffolding/colony_alignment.csv    — Flat CSV for quick reference

Requires:
    pip install neo4j
"""

import json
import csv
import sys
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent


# =============================================================================
# MANUAL ALIGNMENT TABLE
# =============================================================================
# Maps extraction canonical name → KG Colony node name(s).
# Where multiple KG nodes exist for a single extraction name (e.g. different
# eras), we pick the most relevant one and note alternatives.

ALIGNMENT = {
    # ------------------------------------------------------------------
    # West Africa
    # ------------------------------------------------------------------
    "Gold Coast": {
        "kg_name": "British Gold Coast",
        "kg_alt": ["Gold Coast Colony"],
        "qid": "Q503623",
        "notes": "Also 'Gold Coast Colony' node; same QID",
    },
    "Sierra Leone": {
        "kg_name": "Sierra Leone Colony and Protectorate",
        "kg_alt": ["Sierra Leone Colony", "Sierra Leone Company Settlement"],
        "qid": "Q1044",
        "notes": "Colony and Protectorate is the main node (1808-1961)",
    },
    "Gambia": {
        "kg_name": "Gambia Colony and Protectorate",
        "kg_alt": ["Gambia Colony"],
        "qid": "Q3557236",
    },
    "Lagos": {
        "kg_name": "Lagos Protectorate",
        "qid": "Q1801433",
        "notes": "Lagos Colony merged into Southern Nigeria 1906",
    },
    "Nigeria": {
        "kg_name": "Colony and Protectorate of Nigeria",
        "qid": "Q5148517",
    },
    "Northern Nigeria": {
        "kg_name": "Northern Nigeria",
        "qid": "Q585408",
    },
    "Southern Nigeria": {
        "kg_name": "Southern Nigeria Protectorate",
        "qid": "Q2062030",
    },
    "Nigeria (Federation)": {
        "kg_name": "Colony and Protectorate of Nigeria",
        "qid": "Q5148517",
        "notes": "Same entity, later era name",
    },
    "Niger Coast Protectorate": {
        "kg_name": "Niger Coast Protectorate",
        "kg_alt": ["Oil Rivers Protectorate"],
        "qid": "Q2566427",
    },
    "Niger Territories": {
        "kg_name": "Royal Niger Company Territory",
        "qid": "Q1806380",
        "notes": "Approximate match — Niger Territories preceded formal protectorate",
    },
    "West African Settlements": {
        "kg_name": None,
        "notes": "Administrative grouping, no single KG node; contained Gold Coast, Lagos, Gambia, Sierra Leone",
    },
    "Togoland": {
        "kg_name": "British Togoland",
        "qid": "Q797527",
    },
    "Cameroons (UK Trusteeship)": {
        "kg_name": "British Cameroons",
        "qid": "Q1028835",
    },
    "Ashanti": {
        "kg_name": "Ashanti",
        "qid": "Q96372444",
        "notes": "Sub-territory of Gold Coast",
    },
    "Northern Territories (Gold Coast)": {
        "kg_name": None,
        "notes": "No separate KG node; part of British Gold Coast",
    },

    # ------------------------------------------------------------------
    # East Africa
    # ------------------------------------------------------------------
    "East Africa Protectorate": {
        "kg_name": "East Africa Protectorate",
        "qid": "Q876185",
        "notes": "Became Kenya Colony 1920",
    },
    "Kenya": {
        "kg_name": "Kenya, Colony & Protectorate of",
        "qid": "Q2538511",
    },
    "Uganda": {
        "kg_name": "Uganda Protectorate",
        "kg_alt": ["Uganda"],
        "qid": "Q1097943",
    },
    "Zanzibar": {
        "kg_name": "Zanzibar",
        "kg_alt": ["Zanzibar (Independent)"],
        "qid": "Q3574782",
    },
    "Tanganyika": {
        "kg_name": "Tanganyika",
        "kg_alt": ["Tanganyika Territory"],
        "qid": "Q158725",
    },
    "Nyasaland": {
        "kg_name": "Nyasaland",
        "kg_alt": ["Nyasaland (Post-Federation)", "British Central Africa Protectorate"],
        "qid": "Q1649306",
    },
    "Somaliland": {
        "kg_name": "British Somaliland",
        "kg_alt": ["Somaliland Protectorate"],
        "qid": "Q662653",
    },
    "East Africa High Commission": {
        "kg_name": None,
        "notes": "Inter-territorial body, no single KG node",
    },
    "Imperial British East Africa Company": {
        "kg_name": "Imperial British East Africa Company Territory",
        "qid": "Q926921",
    },

    # ------------------------------------------------------------------
    # Southern Africa
    # ------------------------------------------------------------------
    "Cape of Good Hope": {
        "kg_name": "Cape Colony (British)",
        "kg_alt": ["Cape Colony (British 1795-1803)"],
        "qid": "Q4806993",
    },
    "Natal": {
        "kg_name": "Colony of Natal",
        "qid": "Q1301901",
    },
    "South Africa": {
        "kg_name": "Union of South Africa",
        "qid": "Q193619",
    },
    "Transvaal": {
        "kg_name": "Transvaal Colony (Second British)",
        "kg_alt": ["Transvaal Colony (First British)", "South African Republic (Transvaal)"],
        "qid": "Q779805",
    },
    "Orange River Colony": {
        "kg_name": "Orange River Colony",
        "qid": "Q2005921",
    },
    "Rhodesia": {
        "kg_name": "British South Africa Company Territory",
        "qid": "Q5155572",
        "notes": "Pre-partition 'Rhodesia' = BSA Company territory",
    },
    "Southern Rhodesia": {
        "kg_name": "Southern Rhodesia Colony",
        "kg_alt": ["Southern Rhodesia", "Southern Rhodesia (Restored)"],
        "qid": "Q750583",
    },
    "Northern Rhodesia": {
        "kg_name": "Northern Rhodesia Colony",
        "kg_alt": ["Northern Rhodesia", "Northern Rhodesia (Post-Federation)"],
        "qid": "Q953903",
    },
    "Rhodesia and Nyasaland": {
        "kg_name": "Federation of Rhodesia and Nyasaland",
        "qid": "Q654342",
    },
    "British South Africa Company": {
        "kg_name": "British South Africa Company Territory",
        "qid": "Q5155572",
    },
    "Basutoland": {
        "kg_name": "Basutoland",
        "qid": "Q2340665",
    },
    "Bechuanaland": {
        "kg_name": "Bechuanaland Protectorate",
        "qid": "Q747314",
    },
    "British Bechuanaland": {
        "kg_name": "British Bechuanaland",
        "qid": "Q4530733",
    },
    "Swaziland": {
        "kg_name": "Swaziland",
        "qid": "Q1050",
    },
    "Zululand": {
        "kg_name": "Zululand",
        "qid": "Q1009306",
    },
    "Amatongaland": {
        "kg_name": None,
        "notes": "No KG node; annexed by Natal 1895. QID: Q4738091",
    },
    "Griqualand West": {
        "kg_name": "Griqualand West",
        "qid": "Q2547918",
    },
    "High Commission Territories": {
        "kg_name": None,
        "notes": "Administrative grouping of Basutoland, Bechuanaland, Swaziland",
    },

    # ------------------------------------------------------------------
    # Caribbean
    # ------------------------------------------------------------------
    "Jamaica": {
        "kg_name": "Jamaica",
        "qid": "Q2526023",
    },
    "Trinidad": {
        "kg_name": "Trinidad and Tobago Colony",
        "qid": "Q116282722",
        "notes": "Trinidad alone before merger with Tobago",
    },
    "Trinidad and Tobago": {
        "kg_name": "Trinidad and Tobago Colony",
        "qid": "Q116282722",
    },
    "Tobago": {
        "kg_name": "Trinidad and Tobago Colony",
        "qid": "Q116282722",
        "notes": "Tobago merged into Trinidad and Tobago 1889",
    },
    "Barbados": {
        "kg_name": "Barbados Colony",
        "qid": "Q63973349",
    },
    "British Guiana": {
        "kg_name": "British Guiana",
        "kg_alt": ["British Guyana"],
        "qid": "Q918126",
    },
    "British Honduras": {
        "kg_name": "British Honduras",
        "qid": "Q1643555",
    },
    "Bahamas": {
        "kg_name": "Bahamas Colony",
        "qid": "Q1060894",
    },
    "Bermuda": {
        "kg_name": "Bermuda",
        "qid": "Q23635",
    },
    "Dominica": {
        "kg_name": "Dominica Colony",
        "qid": "Q137394892",
    },
    "Antigua": {
        "kg_name": "Antigua Colony",
        "qid": "Q22007334",
    },
    "St Vincent": {
        "kg_name": "St. Vincent Colony",
        "qid": "Q757",
    },
    "St Lucia": {
        "kg_name": "Saint Lucia Colony",
        "qid": "Q760",
    },
    "Grenada": {
        "kg_name": "Grenada Colony",
        "qid": "Q3116419",
    },
    "Montserrat": {
        "kg_name": "Montserrat",
        "qid": "Q13353",
    },
    "Nevis": {
        "kg_name": "Saint Christopher-Nevis-Anguilla",
        "qid": "Q1637975",
        "notes": "Nevis part of combined colony; no separate KG node",
    },
    "Anguilla": {
        "kg_name": "Anguilla",
        "qid": "Q25228",
    },
    "Barbuda": {
        "kg_name": None,
        "notes": "Dependency of Antigua; no separate KG node",
    },
    "Virgin Islands": {
        "kg_name": "British Virgin Islands",
        "qid": "Q25305",
    },
    "Turks and Caicos Islands": {
        "kg_name": "Turks and Caicos Islands",
        "qid": "Q18221",
    },
    "Cayman Islands": {
        "kg_name": "Cayman Islands",
        "qid": "Q5785",
    },
    "St Christopher and Nevis": {
        "kg_name": "Saint Christopher-Nevis-Anguilla",
        "kg_alt": ["Colony of St. Kitts-Nevis-Anguilla"],
        "qid": "Q1637975",
    },
    "West Indies": {
        "kg_name": "West Indies Federation",
        "qid": "Q652560",
        "notes": "Late-era files referring to the Federation",
    },
    "West Indies Federation": {
        "kg_name": "West Indies Federation",
        "qid": "Q652560",
    },
    "West Indies (Cayman/Turks)": {
        "kg_name": None,
        "notes": "Sub-section of West Indies files covering Cayman + Turks and Caicos",
    },
    "West Indies (St Vincent)": {
        "kg_name": "St. Vincent Colony",
        "qid": "Q757",
        "notes": "Sub-section of West Indies files covering St Vincent",
    },

    # ------------------------------------------------------------------
    # Leeward Islands (Federated)
    # ------------------------------------------------------------------
    "Leeward Islands": {
        "kg_name": "Federal Colony of the Leeward Islands",
        "kg_alt": ["Leeward Islands Colony (1671-1816)"],
        "qid": "Q1796551",
    },
    "Leeward Islands - Antigua": {
        "kg_name": "Antigua Colony",
        "qid": "Q22007334",
        "notes": "Antigua presidency within Leeward Islands federation",
    },
    "Leeward Islands - Dominica": {
        "kg_name": "Dominica Colony",
        "qid": "Q137394892",
        "notes": "Dominica presidency; transferred to Windward Islands 1940",
    },
    "Leeward Islands - Montserrat": {
        "kg_name": "Montserrat",
        "qid": "Q13353",
    },
    "Leeward Islands - St Christopher Nevis": {
        "kg_name": "Saint Christopher-Nevis-Anguilla",
        "qid": "Q1637975",
    },
    "Leeward Islands - Virgin Islands": {
        "kg_name": "British Virgin Islands",
        "qid": "Q25305",
    },

    # ------------------------------------------------------------------
    # Windward Islands (Federated)
    # ------------------------------------------------------------------
    "Windward Islands": {
        "kg_name": "British Windward Islands",
        "qid": "Q2660774",
    },
    "Windward Islands - Grenada": {
        "kg_name": "Grenada Colony",
        "qid": "Q3116419",
    },
    "Windward Islands - St Lucia": {
        "kg_name": "Saint Lucia Colony",
        "qid": "Q760",
    },
    "Windward Islands - St Vincent": {
        "kg_name": "St. Vincent Colony",
        "qid": "Q757",
    },
    "Windward Islands - Tobago": {
        "kg_name": "Trinidad and Tobago Colony",
        "qid": "Q116282722",
        "notes": "Tobago was in Windward Islands before joining Trinidad 1889",
    },

    # ------------------------------------------------------------------
    # South / Southeast Asia
    # ------------------------------------------------------------------
    "Ceylon": {
        "kg_name": "Ceylon",
        "qid": "Q918153",
    },
    "Hong Kong": {
        "kg_name": "British Hong Kong",
        "kg_alt": ["Hong Kong"],
        "qid": "Q1054923",
    },
    "Straits Settlements": {
        "kg_name": "Straits Settlements",
        "qid": "Q376178",
    },
    "Singapore": {
        "kg_name": "Singapore Crown Colony",
        "kg_alt": ["Singapore", "Singapore Settlement"],
        "qid": "Q4373718",
    },
    "Labuan": {
        "kg_name": "Labuan",
        "qid": "Q1344",
    },
    "North Borneo": {
        "kg_name": "British North Borneo",
        "kg_alt": ["North Borneo Crown Colony"],
        "qid": "Q1147441",
    },
    "Sarawak": {
        "kg_name": "Sarawak Crown Colony",
        "kg_alt": ["Sarawak"],
        "qid": "Q1166",
    },
    "Brunei": {
        "kg_name": "Brunei Protectorate",
        "qid": "Q921",
    },
    "Federated Malay States": {
        "kg_name": "Federated Malay States",
        "qid": "Q1400154",
    },
    "Unfederated Malay States": {
        "kg_name": "Unfederated Malay States",
        "qid": "Q1973084",
    },
    "Federation of Malaya": {
        "kg_name": "Federation of Malaya",
        "qid": "Q1479726",
    },
    "Malaya": {
        "kg_name": "Malaya",
        "kg_alt": ["Malaya (Independent)", "Malayan Union"],
        "qid": "Q871091",
    },
    "Malaysia": {
        "kg_name": "Malaya (Independent)",
        "qid": "Q1479726",
        "notes": "Post-independence files",
    },
    "Johore": {
        "kg_name": "Unfederated Malay States",
        "qid": "Q1973084",
        "notes": "Johore was one of the Unfederated Malay States; no separate KG node",
    },
    "Kedah": {
        "kg_name": "Unfederated Malay States",
        "qid": "Q1973084",
        "notes": "Kedah was one of the Unfederated Malay States; no separate KG node",
    },
    "Kelantan": {
        "kg_name": "Unfederated Malay States",
        "qid": "Q1973084",
        "notes": "Kelantan was one of the Unfederated Malay States; no separate KG node",
    },
    "Perlis": {
        "kg_name": "Unfederated Malay States",
        "qid": "Q1973084",
        "notes": "Perlis was one of the Unfederated Malay States; no separate KG node",
    },
    "Trengganu": {
        "kg_name": "Unfederated Malay States",
        "qid": "Q1973084",
        "notes": "Trengganu was one of the Unfederated Malay States; no separate KG node",
    },
    "Aden": {
        "kg_name": "Aden Colony",
        "kg_alt": ["Aden Protectorate", "Aden Province"],
        "qid": "Q49910",
    },
    "Wei-hai-Wei": {
        "kg_name": "Weihaiwei",
        "qid": "Q15939896",
    },
    "British New Guinea": {
        "kg_name": "British New Guinea",
        "qid": "Q2645837",
    },
    "Papua": {
        "kg_name": "Territory of Papua",
        "kg_alt": ["Territory of Papua and New Guinea"],
        "qid": "Q530560",
    },

    # ------------------------------------------------------------------
    # Mediterranean & Atlantic
    # ------------------------------------------------------------------
    "Malta": {
        "kg_name": "Malta",
        "qid": "Q6744657",
    },
    "Gibraltar": {
        "kg_name": "Gibraltar",
        "qid": "Q1410",
    },
    "Cyprus": {
        "kg_name": "Cyprus",
        "qid": "Q15240466",
    },
    "Falkland Islands": {
        "kg_name": "Falkland Islands",
        "qid": "Q9648",
    },
    "St Helena": {
        "kg_name": "St. Helena",
        "qid": "Q34497",
        "notes": "KG also has 'Saint Helena, Ascension and Tristan da Cunha' (Q192184)",
    },
    "Heligoland": {
        "kg_name": None,
        "notes": "Not in KG. Ceded to Germany 1890. Wikidata: Q3084",
    },
    "Ascension": {
        "kg_name": "Ascension Island",
        "qid": "Q46197",
    },
    "Tristan da Cunha": {
        "kg_name": "Tristan da Cunha",
        "qid": "Q220982",
    },
    "Pitcairn Island": {
        "kg_name": "Pitcairn Islands",
        "qid": "Q35672",
    },
    "Christmas Island": {
        "kg_name": "Christmas Island",
        "qid": "Q31063",
    },
    "Rodrigues": {
        "kg_name": "Rodrigues",
        "qid": "Q1029547",
    },

    # ------------------------------------------------------------------
    # Pacific
    # ------------------------------------------------------------------
    "Fiji": {
        "kg_name": "Fiji",
        "qid": "Q5148320",
    },
    "Western Pacific": {
        "kg_name": "British Western Pacific Territories",
        "qid": "Q1545934",
    },
    "Gilbert and Ellice Islands": {
        "kg_name": "Gilbert and Ellice Islands",
        "qid": "Q1050859",
    },
    "British Solomon Islands": {
        "kg_name": "British Solomon Islands",
        "qid": "Q13410267",
    },
    "New Hebrides": {
        "kg_name": "New Hebrides",
        "qid": "Q686",
    },
    "Tonga": {
        "kg_name": "Tonga Protectorate",
        "qid": "Q17197946",
    },
    "Nauru": {
        "kg_name": "Nauru",
        "qid": "Q697",
    },
    "Territory of New Guinea": {
        "kg_name": "Territory of New Guinea",
        "qid": "Q691",
    },
    "Norfolk Island": {
        "kg_name": "Norfolk Island",
        "qid": "Q31057",
    },
    "Lord Howe Island": {
        "kg_name": None,
        "notes": "Part of New South Wales; no separate KG node. Wikidata: Q172029",
    },
    "Cook Islands": {
        "kg_name": "Cook Islands",
        "qid": "Q26988",
    },

    # ------------------------------------------------------------------
    # Settler Colonies
    # ------------------------------------------------------------------
    "Canada": {
        "kg_name": "Canada, Dominion of",
        "kg_alt": ["Province of Canada"],
        "qid": "Q16",
    },
    "New South Wales": {
        "kg_name": "New South Wales (Original)",
        "qid": "Q18348382",
    },
    "Victoria": {
        "kg_name": "Victoria (Colony)",
        "qid": "Q56850459",
    },
    "Queensland": {
        "kg_name": "Queensland",
        "qid": "Q28401203",
    },
    "South Australia": {
        "kg_name": "South Australia",
        "qid": "Q35715",
    },
    "Western Australia": {
        "kg_name": "Western Australia",
        "kg_alt": ["Swan River Colony"],
        "qid": "Q3208",
    },
    "Tasmania": {
        "kg_name": "Tasmania",
        "kg_alt": ["Van Diemen's Land"],
        "qid": "Q5148519",
    },
    "Australia": {
        "kg_name": "Commonwealth of Australia",
        "kg_alt": ["Australia"],
        "qid": "Q408",
    },
    "Australia - New South Wales": {
        "kg_name": "New South Wales (Original)",
        "qid": "Q18348382",
        "notes": "NSW section within Australia files",
    },
    "Australia - Queensland": {
        "kg_name": "Queensland",
        "qid": "Q28401203",
        "notes": "Queensland section within Australia files",
    },
    "New Zealand": {
        "kg_name": "New Zealand",
        "qid": "Q5148518",
    },
    "Newfoundland": {
        "kg_name": "Colony of Newfoundland",
        "kg_alt": ["Dominion of Newfoundland"],
        "qid": "Q2984260",
    },
    "Nova Scotia": {
        "kg_name": "Nova Scotia",
        "qid": "Q98931415",
    },
    "New Brunswick": {
        "kg_name": "New Brunswick",
        "qid": "Q107499350",
    },
    "Prince Edward Island": {
        "kg_name": "Prince Edward Island",
        "qid": "Q137324703",
    },
    "British Columbia": {
        "kg_name": "British Columbia (Colony)",
        "kg_alt": ["United Colony of British Columbia"],
        "qid": "Q2514958",
    },
    "Vancouver's Island": {
        "kg_name": "Colony of Vancouver Island",
        "qid": "Q2510000",
    },
    "Northern Territory (Australia)": {
        "kg_name": "Northern Territory",
        "qid": "Q3235",
    },
    "Ontario": {
        "kg_name": "Upper Canada",
        "qid": "Q795427",
        "notes": "Ontario = Upper Canada post-Confederation",
    },

    # ------------------------------------------------------------------
    # Indian Ocean
    # ------------------------------------------------------------------
    "Mauritius": {
        "kg_name": "Mauritius",
        "qid": "Q12053604",
    },
    "Seychelles": {
        "kg_name": "Seychelles",
        "kg_alt": ["Seychelles (Mauritius Dependency)"],
        "qid": "Q21821453",
    },

    # ------------------------------------------------------------------
    # Middle East
    # ------------------------------------------------------------------
    "Palestine": {
        "kg_name": "Mandatory Palestine",
        "kg_alt": ["Palestine"],
        "qid": "Q193714",
    },
    "Iraq": {
        "kg_name": "Mandatory Iraq",
        "kg_alt": ["Iraq"],
        "qid": "Q796",
    },
    "Transjordan": {
        "kg_name": "Transjordan",
        "qid": "Q810",
    },

    # ------------------------------------------------------------------
    # Miscellaneous
    # ------------------------------------------------------------------
    "Miscellaneous Islands": {
        "kg_name": None,
        "notes": "Omnibus category; individual islands have separate KG nodes",
    },
    "Bulama": {
        "kg_name": None,
        "notes": "Portuguese-contested territory; briefly British. No KG node. Wikidata: Q11919290",
    },
    "British Antarctic Territory": {
        "kg_name": None,
        "notes": "Established 1962 from Falkland Islands Dependencies. Wikidata: Q2888913",
    },
}


# =============================================================================
# BUILD AND VERIFY
# =============================================================================

def load_extraction_names() -> list:
    """Load canonical extraction names from corpus inventory."""
    inv_path = BASE_DIR / "scaffolding" / "corpus_inventory.json"
    if not inv_path.exists():
        print(f"ERROR: Run build_corpus_inventory.py first")
        sys.exit(1)

    with open(inv_path) as f:
        data = json.load(f)

    return sorted(data["statistics"]["colony_names"])


def load_kg_colonies() -> dict:
    """Load Colony nodes from Neo4j knowledge graph."""
    try:
        from neo4j import GraphDatabase
    except ImportError:
        print("WARNING: neo4j driver not installed; using cached data")
        return {}

    try:
        driver = GraphDatabase.driver(
            "bolt://206.12.90.118:7687",
            auth=("neo4j", os.environ.get("NEO4J_PASSWORD", ""))
        )
        colonies = {}
        with driver.session() as session:
            result = session.run("""
                MATCH (c:Colony)
                RETURN c.name AS name, c.wikidata_id AS qid,
                       c.modern_nation_qids AS modern_qids
                ORDER BY c.name
            """)
            for record in result:
                colonies[record["name"]] = {
                    "qid": record["qid"],
                    "modern_nation_qids": record["modern_qids"],
                }
        driver.close()
        return colonies
    except Exception as e:
        print(f"WARNING: Cannot connect to Neo4j: {e}")
        return {}


def build_alignment_table(extraction_names: list, kg_colonies: dict) -> list:
    """Build the alignment table with verification against live KG data."""
    kg_names_set = set(kg_colonies.keys())
    table = []

    for ext_name in extraction_names:
        entry = {
            "extraction_name": ext_name,
            "kg_name": None,
            "kg_alt": [],
            "wikidata_qid": None,
            "modern_nation_qids": None,
            "match_status": "unmatched",
            "notes": None,
        }

        if ext_name in ALIGNMENT:
            alignment = ALIGNMENT[ext_name]
            kg_name = alignment.get("kg_name")
            entry["kg_name"] = kg_name
            entry["kg_alt"] = alignment.get("kg_alt", [])
            entry["wikidata_qid"] = alignment.get("qid")
            entry["notes"] = alignment.get("notes")

            if kg_name is None:
                entry["match_status"] = "no_kg_node"
            elif kg_name in kg_names_set:
                entry["match_status"] = "verified"
                # Pull live QID and modern_nation_qids from KG
                kg_data = kg_colonies[kg_name]
                if kg_data["qid"]:
                    entry["wikidata_qid"] = kg_data["qid"]
                if kg_data["modern_nation_qids"]:
                    entry["modern_nation_qids"] = kg_data["modern_nation_qids"]
            else:
                entry["match_status"] = "kg_name_not_found"
                entry["notes"] = (entry["notes"] or "") + f" [WARNING: '{kg_name}' not found in KG]"
        else:
            entry["match_status"] = "no_alignment_entry"
            entry["notes"] = "Not in ALIGNMENT dict — needs manual mapping"

        table.append(entry)

    return table


# =============================================================================
# OUTPUT
# =============================================================================

def write_json(table: list, output_path: Path):
    """Write alignment table as JSON."""
    # Statistics
    verified = sum(1 for e in table if e["match_status"] == "verified")
    no_kg = sum(1 for e in table if e["match_status"] == "no_kg_node")
    not_found = sum(1 for e in table if e["match_status"] == "kg_name_not_found")
    unmatched = sum(1 for e in table if e["match_status"] in ("unmatched", "no_alignment_entry"))

    output = {
        "generated": "build_colony_alignment.py",
        "statistics": {
            "total_extraction_names": len(table),
            "verified_matches": verified,
            "no_kg_node": no_kg,
            "kg_name_not_found": not_found,
            "unmatched": unmatched,
        },
        "alignments": table,
    }

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)


def write_csv(table: list, output_path: Path):
    """Write alignment table as CSV."""
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "extraction_name", "kg_name", "wikidata_qid",
            "modern_nation_qids", "match_status", "notes"
        ])
        for entry in table:
            writer.writerow([
                entry["extraction_name"],
                entry["kg_name"] or "",
                entry["wikidata_qid"] or "",
                "|".join(entry["modern_nation_qids"] or []),
                entry["match_status"],
                entry["notes"] or "",
            ])


# =============================================================================
# MAIN
# =============================================================================

def main():
    output_dir = BASE_DIR / "scaffolding"

    print("=" * 70)
    print("COLONY ALIGNMENT TABLE BUILDER")
    print("=" * 70)

    # Load extraction names
    extraction_names = load_extraction_names()
    print(f"\nExtraction canonical names: {len(extraction_names)}")

    # Load KG colonies
    print("Loading Colony nodes from Neo4j...")
    kg_colonies = load_kg_colonies()
    print(f"  KG Colony nodes: {len(kg_colonies)}")

    # Build alignment
    print("\nBuilding alignment table...")
    table = build_alignment_table(extraction_names, kg_colonies)

    # Write outputs
    json_path = output_dir / "colony_alignment.json"
    csv_path = output_dir / "colony_alignment.csv"
    write_json(table, json_path)
    write_csv(table, csv_path)
    print(f"\n  Wrote: {json_path}")
    print(f"  Wrote: {csv_path}")

    # Summary
    verified = sum(1 for e in table if e["match_status"] == "verified")
    no_kg = sum(1 for e in table if e["match_status"] == "no_kg_node")
    not_found = sum(1 for e in table if e["match_status"] == "kg_name_not_found")
    unmatched = sum(1 for e in table if e["match_status"] in ("unmatched", "no_alignment_entry"))

    print(f"\n{'=' * 70}")
    print("ALIGNMENT SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Total extraction names:  {len(table)}")
    print(f"  Verified KG matches:     {verified}")
    print(f"  No KG node (expected):   {no_kg}")
    print(f"  KG name not found:       {not_found}")
    print(f"  Unmatched:               {unmatched}")

    # Show problems
    problems = [e for e in table if e["match_status"] in ("kg_name_not_found", "unmatched", "no_alignment_entry")]
    if problems:
        print(f"\n  Issues requiring attention:")
        for e in problems:
            print(f"    [{e['match_status']}] {e['extraction_name']}: {e['notes']}")

    # Show no-KG-node entries
    no_kg_entries = [e for e in table if e["match_status"] == "no_kg_node"]
    if no_kg_entries:
        print(f"\n  Extraction names with no KG counterpart ({len(no_kg_entries)}):")
        for e in no_kg_entries:
            print(f"    {e['extraction_name']}: {e['notes']}")


if __name__ == "__main__":
    main()

"""
Neo4j Stage 0: Temporal-Geographic Scaffolding
================================================

Scans all year-directories, normalizes colony filenames, and builds
the temporal-geographic skeleton in Neo4j:

- Year anchor nodes (1867–1966)
- Territory persistent nodes (~100 colonies)
- TerritoryYear slice nodes (one per colony-file per year)
- CONTINUES_AS temporal edges (same colony, consecutive years)
- IN_YEAR edges (slice → year)
- INSTANCE_OF edges (slice → persistent territory)

Usage:
    python scaffold_neo4j.py
    python scaffold_neo4j.py --dry-run     # print stats without loading
    python scaffold_neo4j.py --clear       # clear graph first

Requires:
    pip install neo4j
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)


# =============================================================================
# CONFIGURATION
# =============================================================================

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "colonial_office")

REPO_DIR = Path(__file__).parent


# =============================================================================
# COLONY NAME NORMALIZATION
# =============================================================================

# Map raw filename stems (lowercased, stripped of .txt) to canonical colony name.
# Only entries that need explicit mapping are listed. Everything else is
# auto-normalized by: lowercase → strip prefix "the_" → strip suffix
# "_ref"/"_windward"/"_colony"/"_protectorate" etc → title-case → known alias lookup.

EXPLICIT_ALIASES = {
    # ---- Bahamas variants ----
    "bahamas": "Bahamas",
    "bahama_islands": "Bahamas",
    "bahamas_islands": "Bahamas",

    # ---- Bermuda variants ----
    "bermuda": "Bermuda",
    "bermudas": "Bermuda",

    # ---- Canada variants ----
    "canada": "Canada",
    "dominion_of_canada": "Canada",

    # ---- Cape of Good Hope ----
    "cape_of_good_hope": "Cape of Good Hope",

    # ---- Ceylon ----
    "ceylon": "Ceylon",

    # ---- Cyprus ----
    "cyprus": "Cyprus",
    "republic_of_cyprus": "Cyprus",

    # ---- East Africa / Kenya ----
    "east_africa_protectorate": "Kenya",
    "british_east_africa_and_zanzibar": "British East Africa and Zanzibar",
    "british_east_africa_protectorate": "Kenya",
    "kenya": "Kenya",
    "the_kenya_colony_and_protectorate": "Kenya",

    # ---- Falkland Islands ----
    "falkland_islands": "Falkland Islands",
    "falkland_islands_and_dependencies": "Falkland Islands",

    # ---- Federation of Malaya / Malaya ----
    "federated_malay_states": "Federated Malay States",
    "federation_of_malaya": "Federation of Malaya",
    "malaya": "Federation of Malaya",
    "malaya_federated_malay_states": "Federated Malay States",
    "malaya__federated_malay_states": "Federated Malay States",
    "malaya_straits_settlements": "Straits Settlements",
    "malaya__straits_settlements": "Straits Settlements",
    "malaya_unfederated_malay_states": "Unfederated Malay States",
    "malay_states_not_included_in_the_federation": "Unfederated Malay States",
    "unfederated_malay_states": "Unfederated Malay States",
    "malaysia": "Malaysia",

    # ---- Fiji ----
    "fiji": "Fiji",
    "fiji_and_pitcairn_islands": "Fiji",
    "fiji_and_pitcairn_islands_group": "Fiji",
    "fiji_and_pitcairn": "Fiji",

    # ---- Gambia ----
    "gambia": "Gambia",
    "the_gambia": "Gambia",
    "west_africa_gambia": "Gambia",

    # ---- Gibraltar ----
    "gibraltar": "Gibraltar",

    # ---- Gold Coast / Ghana ----
    "gold_coast": "Gold Coast",
    "gold_coast_colony": "Gold Coast",
    "the_gold_coast": "Gold Coast",
    "the_gold_coast_colony": "Gold Coast",
    "gold_coast_ghana": "Gold Coast",

    # ---- Grenada ----
    "grenada": "Grenada",
    "grenade": "Grenada",
    "grenada_windward": "Grenada",
    "grena_da": "Grenada",
    "grenade_ref": "Grenada",

    # ---- Heligoland ----
    "heligoland": "Heligoland",
    "helgoland": "Heligoland",

    # ---- Honduras ----
    "honduras": "British Honduras",
    "british_honduras": "British Honduras",

    # ---- Hong Kong ----
    "hong_kong": "Hong Kong",

    # ---- Jamaica ----
    "jamaica": "Jamaica",

    # ---- Leeward Islands (federation) ----
    "leeward_islands": "Leeward Islands",
    "the_leeward_islands": "Leeward Islands",

    # ---- Leeward Islands sub-colonies ----
    "leeward_islands_antigua": "Antigua",
    "leeward_islands___antigua": "Antigua",
    "leeward_islands_dominica": "Dominica",
    "leeward_islands___dominica": "Dominica",
    "leeward_islands_montserrat": "Montserrat",
    "leeward_islands_st_christopher_nevis": "St Christopher and Nevis",
    "leeward_islands___st._christopher_and_nevis": "St Christopher and Nevis",
    "leeward_islands_virgin_islands": "Virgin Islands",
    "leeward_islands___virgin_islands": "Virgin Islands",

    # ---- Malta ----
    "malta": "Malta",
    "state_of_malta": "Malta",

    # ---- Mauritius ----
    "mauritius": "Mauritius",

    # ---- Nigeria ----
    "nigeria": "Nigeria",
    "northern_nigeria": "Northern Nigeria",
    "southern_nigeria": "Southern Nigeria",
    "federation_of_nigeria": "Nigeria",
    "the_niger_territories": "Niger Territories",
    "niger_coast_protectorate": "Niger Coast Protectorate",
    "niger_protectorate": "Niger Protectorate",

    # ---- Nyasaland ----
    "nyasaland": "Nyasaland",
    "nyasaland_protectorate": "Nyasaland",

    # ---- Palestine ----
    "palestine": "Palestine",

    # ---- Rhodesia ----
    "rhodesia": "Rhodesia",
    "northern_rhodesia": "Northern Rhodesia",
    "southern_rhodesia": "Southern Rhodesia",
    "southern_rhodesia_administration": "Southern Rhodesia",
    "rhodesia_and_nyasaland": "Federation of Rhodesia and Nyasaland",
    "federation_rhodesia_nyasaland": "Federation of Rhodesia and Nyasaland",
    "federation_of_rhodesia_and_nyasaland": "Federation of Rhodesia and Nyasaland",
    "the_federation_of_rhodesia_and_nyasaland": "Federation of Rhodesia and Nyasaland",
    "british_zambezia_and_british_central_africa": "British Central Africa",

    # ---- Seychelles ----
    "seychelles": "Seychelles",
    "seychelles_islands": "Seychelles",

    # ---- Sierra Leone ----
    "sierra_leone": "Sierra Leone",

    # ---- Singapore ----
    "singapore": "Singapore",
    "singapore_and_dependencies": "Singapore",
    "state_of_singapore": "Singapore",

    # ---- Somaliland ----
    "somaliland": "British Somaliland",
    "somaliland_protectorate": "British Somaliland",
    "british_somaliland_protectorate": "British Somaliland",

    # ---- South Africa ----
    "south_africa": "South Africa",

    # ---- St Christopher and Nevis ----
    "st_christophers_and_anguilla_and_nevis": "St Christopher and Nevis",
    "st_christopher_nevis_and_anguilla": "St Christopher and Nevis",
    "st_christopher_and_nevis": "St Christopher and Nevis",
    "st_christopher_nevis_anguilla": "St Christopher and Nevis",

    # ---- St Helena ----
    "st_helena": "St Helena",
    "st._helena": "St Helena",

    # ---- St Lucia ----
    "st_lucia": "St Lucia",

    # ---- St Vincent ----
    "st_vincent": "St Vincent",
    "saint_vincent": "St Vincent",

    # ---- Straits Settlements ----
    "straits_settlements": "Straits Settlements",

    # ---- Tanganyika ----
    "tanganyika": "Tanganyika",
    "tanganyika_territory": "Tanganyika",

    # ---- Tobago ----
    "tobago": "Tobago",
    "tobago_ref": "Tobago",
    "tobago_windward": "Tobago",

    # ---- Tonga ----
    "tonga": "Tonga",
    "kingdom_of_tonga": "Tonga",

    # ---- Trans-Jordan ----
    "transjordan": "Transjordan",
    "trans-jordan": "Transjordan",
    "trans_jordan": "Transjordan",

    # ---- Transvaal ----
    "transvaal": "Transvaal",
    "the_transvaal": "Transvaal",

    # ---- Trinidad and Tobago ----
    "trinidad": "Trinidad",
    "trinidad_and_tobago": "Trinidad and Tobago",
    "trinidad_tobago": "Trinidad and Tobago",

    # ---- Turks and Caicos ----
    "turks_and_caicos_islands": "Turks and Caicos Islands",
    "turks_and_caicos": "Turks and Caicos Islands",

    # ---- Uganda ----
    "uganda": "Uganda",

    # ---- British Columbia ----
    "british_columbia": "British Columbia",
    "british_columbia_and_vancouver_island": "British Columbia",
    "vancouvers_island": "Vancouver Island",

    # ---- Windward Islands ----
    "windward_islands": "Windward Islands",
    "the_windward_islands": "Windward Islands",
    "windward_islands_grenada": "Grenada",
    "windward_islands___grenada": "Grenada",
    "windward_islands_st_lucia": "St Lucia",
    "windward_islands___st._lucia": "St Lucia",
    "windward_islands_st_vincent": "St Vincent",
    "windward_islands___st._vincent": "St Vincent",
    "windward_islands___tobago": "Tobago",

    # ---- Western Pacific ----
    "western_pacific": "Western Pacific",
    "western_pacific_high_commission": "Western Pacific",

    # ---- Zanzibar ----
    "zanzibar": "Zanzibar",
    "zanzibar_and_high_commission_territories": "Zanzibar",

    # ---- Various ----
    "aden": "Aden",
    "aden_colony": "Aden",
    "antigua": "Antigua",
    "antigua_ref": "Antigua",
    "anguilla": "Anguilla",
    "anguilla_ref": "Anguilla",
    "ascension": "Ascension",
    "australia": "Australia",
    "barbados": "Barbados",
    "barbados_ref": "Barbados",
    "barbados_windward": "Barbados",
    "barbuda": "Barbuda",
    "basutoland": "Basutoland",
    "bechuanaland": "Bechuanaland",
    "bechuanaland_protectorate": "Bechuanaland",
    "british_bechuanaland": "British Bechuanaland",
    "the_bechuanaland_protectorate": "Bechuanaland",
    "british_guiana": "British Guiana",
    "british_new_guinea": "British New Guinea",
    "british_north_borneo": "North Borneo",
    "brunei": "Brunei",
    "bulama": "Bulama",
    "cameroons_uk_trusteeship": "Cameroons",
    "the_cameroons": "Cameroons",
    "cayman_islands": "Cayman Islands",
    "christmas_island": "Christmas Island",
    "cook_islands": "Cook Islands",
    "dominica": "Dominica",
    "dominica_ref": "Dominica",
    "east_africa_high_commission": "East Africa High Commission",
    "gilbert_and_ellice_islands": "Gilbert and Ellice Islands",
    "the_gilbert_and_ellice_islands_colony": "Gilbert and Ellice Islands",
    "griqualand_west": "Griqualand West",
    "high_commission_territories": "High Commission Territories",
    "the_high_commission_territories": "High Commission Territories",
    "imperial_british_east_african_company": "Imperial British East Africa Company",
    "iraq": "Iraq",
    "johore": "Johore",
    "kedah": "Kedah",
    "kelantan": "Kelantan",
    "labuan": "Labuan",
    "lagos": "Lagos",
    "mesopotamia": "Mesopotamia",
    "miscellaneous_islands": "Miscellaneous Islands",
    "montserrat": "Montserrat",
    "natal": "Natal",
    "nauru": "Nauru",
    "nevis": "Nevis",
    "nevis_ref": "Nevis",
    "new_brunswick": "New Brunswick",
    "newfoundland": "Newfoundland",
    "new_hebrides": "New Hebrides",
    "new_south_wales": "New South Wales",
    "new_zealand": "New Zealand",
    "norfolk_island": "Norfolk Island",
    "north_borneo": "North Borneo",
    "nova_scotia": "Nova Scotia",
    "orange_river_colony": "Orange River Colony",
    "papua": "Papua",
    "perlis": "Perlis",
    "pitcairn_island": "Pitcairn Island",
    "pitcairn_islands": "Pitcairn Island",
    "pitcairn_islands_group": "Pitcairn Island",
    "prince_edward_island": "Prince Edward Island",
    "queensland": "Queensland",
    "rodrigues": "Rodrigues",
    "sarawak": "Sarawak",
    "south_australia": "South Australia",
    "swaziland": "Swaziland",
    "tasmania": "Tasmania",
    "the_british_sphere_of_togoland": "Togoland",
    "togoland": "Togoland",
    "trengganu": "Trengganu",
    "tristan_d_acunha": "Tristan da Cunha",
    "tristan_da_cunha": "Tristan da Cunha",
    "victoria": "Victoria",
    "virgin_islands": "Virgin Islands",
    "wei_hai_wei": "Weihaiwei",
    "weihaiwei": "Weihaiwei",
    "west_africa": "West Africa",
    "west_african_settlements": "West Africa Settlements",
    "west_africa_settlements": "West Africa Settlements",
    "western_australia": "Western Australia",
    "west_indies": "West Indies",
    "west_indies_federation": "West Indies Federation",
    "the_west_indies_federation": "West Indies Federation",
    "west_indies_cayman_turks_caicos": "West Indies - Cayman, Turks and Caicos",
    "west_indies_jamaica": "Jamaica",
    "west_indies_st_vincent": "St Vincent",
    "the_west_indies_-_barbados": "Barbados",
    "the_west_indies_-_trinidad_and_tobago": "Trinidad and Tobago",
    "the_west_indies_federation": "West Indies Federation",
    "british_antarctic_territory": "British Antarctic Territory",
    "british_solomon_islands_protectorate": "British Solomon Islands",
    "the_british_solomon_islands_protectorate": "British Solomon Islands",
    "the_territory_of_new_guinea": "Territory of New Guinea",
    "zululand": "Zululand",
}


def normalize_colony_name(filename_stem: str) -> str:
    """Normalize a colony filename stem to a canonical colony name."""
    key = filename_stem.lower().strip()

    # Direct lookup
    if key in EXPLICIT_ALIASES:
        return EXPLICIT_ALIASES[key]

    # Try stripping common prefixes/suffixes
    stripped = key
    for prefix in ["the_"]:
        if stripped.startswith(prefix):
            stripped = stripped[len(prefix):]
    for suffix in ["_ref", "_colony", "_protectorate"]:
        if stripped.endswith(suffix):
            stripped = stripped[:-len(suffix)]

    if stripped in EXPLICIT_ALIASES:
        return EXPLICIT_ALIASES[stripped]

    # Fallback: title-case the stem
    return stripped.replace("_", " ").title()


# =============================================================================
# CORPUS SCANNING
# =============================================================================

def scan_corpus(repo_dir: Path) -> dict[int, list[tuple[str, str, str]]]:
    """Scan year-directories and return {year: [(filename, stem, canonical_name), ...]}."""
    corpus = {}

    for entry in sorted(repo_dir.iterdir()):
        if not entry.is_dir() or not entry.name.endswith("_manual_parsed"):
            continue

        year_str = entry.name.replace("_manual_parsed", "")
        try:
            year = int(year_str)
        except ValueError:
            continue

        files = []
        for txt_file in sorted(entry.glob("*.txt")):
            stem = txt_file.stem
            canonical = normalize_colony_name(stem)
            files.append((txt_file.name, stem, canonical))

        corpus[year] = files

    return corpus


def build_inventory(corpus: dict) -> dict:
    """Build territory inventory from corpus scan."""
    # Collect all canonical names and their appearances
    territory_years = defaultdict(list)  # canonical_name -> [year, ...]
    all_years = sorted(corpus.keys())

    for year, files in sorted(corpus.items()):
        for filename, stem, canonical in files:
            territory_years[canonical].append(year)

    return {
        "years": all_years,
        "territories": dict(sorted(territory_years.items())),
        "total_year_dirs": len(all_years),
        "total_territories": len(territory_years),
        "total_territory_years": sum(len(years) for years in territory_years.values()),
    }


# =============================================================================
# NEO4J LOADING
# =============================================================================

def load_scaffolding(driver, corpus: dict, inventory: dict):
    """Load the temporal-geographic scaffolding into Neo4j."""

    with driver.session() as session:
        # --- Create constraints/indexes ---
        print("Creating constraints and indexes...")
        session.run("CREATE CONSTRAINT year_value IF NOT EXISTS FOR (y:Year) REQUIRE y.value IS UNIQUE")
        session.run("CREATE CONSTRAINT territory_name IF NOT EXISTS FOR (t:Territory) REQUIRE t.name IS UNIQUE")
        session.run("CREATE CONSTRAINT territory_year_id IF NOT EXISTS FOR (ty:TerritoryYear) REQUIRE ty.id IS UNIQUE")

        # --- Year nodes ---
        years = inventory["years"]
        print(f"Creating {len(years)} Year nodes ({years[0]}–{years[-1]})...")
        session.run(
            "UNWIND $years AS y "
            "MERGE (n:Year {value: y})",
            years=years
        )

        # --- Territory persistent nodes ---
        territories = list(inventory["territories"].keys())
        print(f"Creating {len(territories)} Territory nodes...")
        session.run(
            "UNWIND $names AS name "
            "MERGE (t:Territory {name: name})",
            names=territories
        )

        # --- TerritoryYear slice nodes + edges ---
        print("Creating TerritoryYear slices and edges...")
        batch = []
        for year, files in sorted(corpus.items()):
            for filename, stem, canonical in files:
                ty_id = f"{canonical}_{year}"
                batch.append({
                    "id": ty_id,
                    "territory": canonical,
                    "year": year,
                    "source_file": f"{year}_manual_parsed/{filename}",
                })

        # Process in chunks to avoid memory issues
        chunk_size = 500
        for i in range(0, len(batch), chunk_size):
            chunk = batch[i:i + chunk_size]
            session.run(
                "UNWIND $records AS r "
                "MERGE (ty:TerritoryYear {id: r.id}) "
                "SET ty.territory = r.territory, "
                "    ty.year = r.year, "
                "    ty.source_file = r.source_file "
                "WITH ty, r "
                "MATCH (y:Year {value: r.year}) "
                "MERGE (ty)-[:IN_YEAR]->(y) "
                "WITH ty, r "
                "MATCH (t:Territory {name: r.territory}) "
                "MERGE (ty)-[:INSTANCE_OF]->(t)",
                records=chunk
            )

        print(f"Created {len(batch)} TerritoryYear nodes")

        # --- CONTINUES_AS temporal edges ---
        print("Creating CONTINUES_AS temporal chains...")
        continues_count = 0
        for territory, appearances in inventory["territories"].items():
            sorted_years = sorted(appearances)
            if len(sorted_years) < 2:
                continue

            pairs = []
            for i in range(len(sorted_years) - 1):
                from_id = f"{territory}_{sorted_years[i]}"
                to_id = f"{territory}_{sorted_years[i + 1]}"
                pairs.append({"from_id": from_id, "to_id": to_id})

            if pairs:
                session.run(
                    "UNWIND $pairs AS p "
                    "MATCH (a:TerritoryYear {id: p.from_id}) "
                    "MATCH (b:TerritoryYear {id: p.to_id}) "
                    "MERGE (a)-[:CONTINUES_AS]->(b)",
                    pairs=pairs
                )
                continues_count += len(pairs)

        print(f"Created {continues_count} CONTINUES_AS edges")


def clear_graph(driver):
    """Remove all nodes and edges."""
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    print("Graph cleared.")


# =============================================================================
# REPORTING
# =============================================================================

def print_report(inventory: dict):
    """Print corpus inventory report."""
    print("\n" + "=" * 60)
    print("CORPUS INVENTORY")
    print("=" * 60)
    print(f"Year directories: {inventory['total_year_dirs']}")
    print(f"Years span: {inventory['years'][0]}–{inventory['years'][-1]}")
    print(f"Unique territories: {inventory['total_territories']}")
    print(f"Total territory-years: {inventory['total_territory_years']}")

    print(f"\n--- Territories by coverage ({inventory['total_year_dirs']} years available) ---")
    # Sort by number of appearances (descending)
    sorted_territories = sorted(
        inventory["territories"].items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    for territory, appearances in sorted_territories[:30]:
        bar = "#" * (len(appearances) * 40 // inventory["total_year_dirs"])
        print(f"  {territory:<45} {len(appearances):>3} years  {bar}")

    if len(sorted_territories) > 30:
        print(f"  ... and {len(sorted_territories) - 30} more territories")

    # Year gap analysis
    all_possible = set(range(inventory["years"][0], inventory["years"][-1] + 1))
    actual_years = set(inventory["years"])
    gaps = sorted(all_possible - actual_years)
    if gaps:
        print(f"\n--- Missing years ({len(gaps)}) ---")
        # Group consecutive gaps
        ranges = []
        start = gaps[0]
        prev = gaps[0]
        for g in gaps[1:]:
            if g == prev + 1:
                prev = g
            else:
                ranges.append((start, prev))
                start = g
                prev = g
        ranges.append((start, prev))

        for s, e in ranges:
            if s == e:
                print(f"  {s}")
            else:
                print(f"  {s}–{e}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Build Neo4j temporal-geographic scaffolding")
    parser.add_argument("--dry-run", action="store_true", help="Print stats without loading into Neo4j")
    parser.add_argument("--clear", action="store_true", help="Clear existing graph data first")
    args = parser.parse_args()

    print("=" * 60)
    print("NEO4J STAGE 0: TEMPORAL-GEOGRAPHIC SCAFFOLDING")
    print("=" * 60)

    # Scan corpus
    print(f"\nScanning: {REPO_DIR}")
    corpus = scan_corpus(REPO_DIR)
    inventory = build_inventory(corpus)

    print_report(inventory)

    if args.dry_run:
        print("\n[DRY RUN] Skipping Neo4j loading.")
        return

    # Connect to Neo4j
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        if args.clear:
            clear_graph(driver)

        load_scaffolding(driver, corpus, inventory)

        # Verify
        with driver.session() as session:
            result = session.run(
                "MATCH (y:Year) RETURN count(y) AS years "
            ).single()
            print(f"\nVerification: {result['years']} Year nodes")

            result = session.run(
                "MATCH (t:Territory) RETURN count(t) AS territories "
            ).single()
            print(f"Verification: {result['territories']} Territory nodes")

            result = session.run(
                "MATCH (ty:TerritoryYear) RETURN count(ty) AS slices "
            ).single()
            print(f"Verification: {result['slices']} TerritoryYear slices")

            result = session.run(
                "MATCH ()-[r:CONTINUES_AS]->() RETURN count(r) AS edges "
            ).single()
            print(f"Verification: {result['edges']} CONTINUES_AS edges")

        print("\nScaffolding complete!")

    finally:
        driver.close()


if __name__ == "__main__":
    main()

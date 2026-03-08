#!/usr/bin/env python3
"""
Colonial Office List Corpus Inventory Builder
==============================================

Walks all *_manual_parsed/ directories and produces:
  1. corpus_inventory.json   — per-file metadata with canonical colony names
  2. coverage_matrix.csv     — colony × year presence matrix
  3. anomalies.txt           — flagged issues requiring attention

Usage:
    python scaffolding/build_corpus_inventory.py
    python scaffolding/build_corpus_inventory.py --base-dir /path/to/repo
"""

import os
import re
import json
import csv
import argparse
from pathlib import Path
from collections import defaultdict


BASE_DIR = Path(__file__).resolve().parent.parent

# =============================================================================
# CANONICAL COLONY NAME MAPPING
# =============================================================================
# Maps normalized filename stems (lowercase, no extension, no 'the_' prefix)
# to canonical colony names. Handles the three naming eras:
#   - 1867-~1890: lowercase (gold_coast.txt)
#   - 1900-~1936: UPPERCASE (THE_GOLD_COAST.txt)
#   - 1950s-1966: mixed case (Gold_Coast.txt, gold_coast.txt)

CANONICAL_MAP = {
    # --- West Africa ---
    "gold_coast": "Gold Coast",
    "gold_coast_colony": "Gold Coast",
    "gold_coast_ghana": "Gold Coast",
    "gambia": "Gambia",
    "the_gambia": "Gambia",
    "west_africa_gambia": "Gambia",
    "sierra_leone": "Sierra Leone",
    "lagos": "Lagos",
    "nigeria": "Nigeria",
    "northern_nigeria": "Northern Nigeria",
    "southern_nigeria": "Southern Nigeria",
    "federation_of_nigeria": "Nigeria (Federation)",
    "niger_coast_protectorate": "Niger Coast Protectorate",
    "niger_protectorate": "Niger Coast Protectorate",
    "the_niger_territories": "Niger Territories",
    "west_african_settlements": "West African Settlements",
    "west_africa_settlements": "West African Settlements",
    "west_africa": "West African Settlements",
    "togoland": "Togoland",
    "the_british_sphere_of_togoland": "Togoland",
    "cameroons_uk_trusteeship": "Cameroons (UK Trusteeship)",
    "the_cameroons": "Cameroons (UK Trusteeship)",

    # --- East Africa ---
    "east_africa_protectorate": "East Africa Protectorate",
    "british_east_africa_protectorate": "East Africa Protectorate",
    "british_east_africa_and_zanzibar": "East Africa Protectorate",
    "british_east_africa_zanzibar_uganda": "East Africa Protectorate",
    "the_kenya_colony_and_protectorate": "Kenya",
    "kenya": "Kenya",
    "uganda": "Uganda",
    "zanzibar": "Zanzibar",
    "zanzibar_and_high_commission_territories": "Zanzibar",
    "tanganyika": "Tanganyika",
    "tanganyika_territory": "Tanganyika",
    "nyasaland": "Nyasaland",
    "nyasaland_protectorate": "Nyasaland",
    "british_central_africa": "Nyasaland",
    "british_central_africa_protectorate": "Nyasaland",
    "british_zambezia_and_british_central_africa": "Nyasaland",
    "somaliland": "Somaliland",
    "somaliland_protectorate": "Somaliland",
    "british_somaliland_protectorate": "Somaliland",
    "east_africa_high_commission": "East Africa High Commission",
    "imperial_british_east_african_company": "Imperial British East Africa Company",

    # --- Southern Africa ---
    "cape_of_good_hope": "Cape of Good Hope",
    "natal": "Natal",
    "south_africa": "South Africa",
    "transvaal": "Transvaal",
    "the_transvaal": "Transvaal",
    "orange_river_colony": "Orange River Colony",
    "rhodesia": "Rhodesia",
    "southern_rhodesia": "Southern Rhodesia",
    "southern_rhodesia_administration": "Southern Rhodesia",
    "northern_rhodesia": "Northern Rhodesia",
    "rhodesia_and_nyasaland": "Rhodesia and Nyasaland",
    "federation_of_rhodesia_and_nyasaland": "Rhodesia and Nyasaland",
    "the_federation_of_rhodesia_and_nyasaland": "Rhodesia and Nyasaland",
    "federation_rhodesia_nyasaland": "Rhodesia and Nyasaland",
    "british_south_africa_company": "British South Africa Company",
    "basutoland": "Basutoland",
    "bechuanaland": "Bechuanaland",
    "bechuanaland_protectorate": "Bechuanaland",
    "the_bechuanaland_protectorate": "Bechuanaland",
    "british_bechuanaland": "British Bechuanaland",
    "swaziland": "Swaziland",
    "zululand": "Zululand",
    "amatongaland": "Amatongaland",
    "griqualand_west": "Griqualand West",
    "high_commission_territories": "High Commission Territories",
    "the_high_commission_territories": "High Commission Territories",

    # --- Caribbean ---
    "jamaica": "Jamaica",
    "west_indies_jamaica": "Jamaica",
    "trinidad": "Trinidad",
    "trinidad_and_tobago": "Trinidad and Tobago",
    "trinidad_tobago": "Trinidad and Tobago",
    "tobago": "Tobago",
    "tobago_windward": "Tobago",
    "tobago_ref": "Tobago",
    "barbados": "Barbados",
    "barbados_windward": "Barbados",
    "barbados_ref": "Barbados",
    "the_west_indies___barbados": "Barbados",
    "the_west_indies_-_barbados": "Barbados",
    "the_west_indies___trinidad_and_tobago": "Trinidad and Tobago",
    "the_west_indies_-_trinidad_and_tobago": "Trinidad and Tobago",
    "british_guiana": "British Guiana",
    "honduras": "British Honduras",
    "british_honduras": "British Honduras",
    "bahamas": "Bahamas",
    "bahama_islands": "Bahamas",
    "bahamas_islands": "Bahamas",
    "bermuda": "Bermuda",
    "bermudas": "Bermuda",
    "dominica": "Dominica",
    "dominica_ref": "Dominica",
    "antigua": "Antigua",
    "antigua_ref": "Antigua",
    "saint_vincent": "St Vincent",
    "st_vincent": "St Vincent",
    "st_lucia": "St Lucia",
    "st_helena": "St Helena",
    "st._helena": "St Helena",
    "nevis": "Nevis",
    "nevis_ref": "Nevis",
    "montserrat": "Montserrat",
    "anguilla": "Anguilla",
    "anguilla_ref": "Anguilla",
    "barbuda": "Barbuda",
    "grenada": "Grenada",
    "grenade": "Grenada",
    "grena_da": "Grenada",
    "grenade_ref": "Grenada",
    "grenada_windward": "Grenada",
    "turks_and_caicos_islands": "Turks and Caicos Islands",
    "turks_and_caicos": "Turks and Caicos Islands",
    "cayman_islands": "Cayman Islands",
    "virgin_islands": "Virgin Islands",
    "st_christophers_and_anguilla_and_nevis": "St Christopher and Nevis",
    "st_christopher_and_nevis": "St Christopher and Nevis",
    "st_christopher_nevis_and_anguilla": "St Christopher and Nevis",
    "st_christopher_nevis_anguilla": "St Christopher and Nevis",
    "west_indies": "West Indies",
    "west_indies_federation": "West Indies Federation",
    "the_west_indies_federation": "West Indies Federation",
    "west_indies_cayman_turks_caicos": "West Indies (Cayman/Turks)",
    "west_indies_st_vincent": "West Indies (St Vincent)",

    # --- Leeward Islands (federated territory) ---
    "leeward_islands": "Leeward Islands",
    "the_leeward_islands": "Leeward Islands",
    "leeward_islands_antigua": "Leeward Islands - Antigua",
    "leeward_islands___antigua": "Leeward Islands - Antigua",
    "leeward_islands_dominica": "Leeward Islands - Dominica",
    "leeward_islands___dominica": "Leeward Islands - Dominica",
    "leeward_islands_montserrat": "Leeward Islands - Montserrat",
    "leeward_islands_st_christopher_nevis": "Leeward Islands - St Christopher Nevis",
    "leeward_islands___st._christopher_and_nevis": "Leeward Islands - St Christopher Nevis",
    "leeward_islands_st._christopher_and_nevis": "Leeward Islands - St Christopher Nevis",
    "leeward_islands_virgin_islands": "Leeward Islands - Virgin Islands",
    "leeward_islands___virgin_islands": "Leeward Islands - Virgin Islands",

    # --- Windward Islands (federated territory) ---
    "windward_islands": "Windward Islands",
    "the_windward_islands": "Windward Islands",
    "windward_islands_grenada": "Windward Islands - Grenada",
    "windward_islands___grenada": "Windward Islands - Grenada",
    "windward_islands_st_lucia": "Windward Islands - St Lucia",
    "windward_islands___st._lucia": "Windward Islands - St Lucia",
    "windward_islands_st_vincent": "Windward Islands - St Vincent",
    "windward_islands___st._vincent": "Windward Islands - St Vincent",
    "windward_islands___st_lucia": "Windward Islands - St Lucia",
    "windward_islands___st_vincent": "Windward Islands - St Vincent",
    "windward_islands___tobago": "Windward Islands - Tobago",
    "windward_islands_tobago": "Windward Islands - Tobago",
    "windward_islands_st._lucia": "Windward Islands - St Lucia",
    "windward_islands_st._vincent": "Windward Islands - St Vincent",

    # --- St. variants with dots ---
    "st._lucia": "St Lucia",
    "st._vincent": "St Vincent",

    # --- South/Southeast Asia ---
    "ceylon": "Ceylon",
    "hong_kong": "Hong Kong",
    "straits_settlements": "Straits Settlements",
    "malaya_straits_settlements": "Straits Settlements",
    "malaya__straits_settlements": "Straits Settlements",
    "singapore": "Singapore",
    "singapore_and_dependencies": "Singapore",
    "state_of_singapore": "Singapore",
    "labuan": "Labuan",
    "north_borneo": "North Borneo",
    "british_north_borneo": "North Borneo",
    "sarawak": "Sarawak",
    "brunei": "Brunei",
    "federated_malay_states": "Federated Malay States",
    "the_federated_malay_states": "Federated Malay States",
    "malaya_federated_malay_states": "Federated Malay States",
    "malaya__federated_malay_states": "Federated Malay States",
    "unfederated_malay_states": "Unfederated Malay States",
    "malay_states_unfederated": "Unfederated Malay States",
    "malay_states_not_included_in_the_federation": "Unfederated Malay States",
    "malaya_unfederated_malay_states": "Unfederated Malay States",
    "federation_of_malaya": "Federation of Malaya",
    "malaya": "Malaya",
    "malaysia": "Malaysia",
    "johore": "Johore",
    "kedah": "Kedah",
    "kelantan": "Kelantan",
    "perlis": "Perlis",
    "trengganu": "Trengganu",
    "aden": "Aden",
    "aden_colony": "Aden",
    "british_new_guinea": "British New Guinea",
    "papua": "Papua",
    "weihaiwei": "Wei-hai-Wei",
    "wei_hai_wei": "Wei-hai-Wei",

    # --- Mediterranean & Atlantic Islands ---
    "malta": "Malta",
    "state_of_malta": "Malta",
    "gibraltar": "Gibraltar",
    "cyprus": "Cyprus",
    "republic_of_cyprus": "Cyprus",
    "falkland_islands": "Falkland Islands",
    "falkland_islands_and_dependencies": "Falkland Islands",
    "ascension": "Ascension",
    "heligoland": "Heligoland",
    "helgoland": "Heligoland",
    "tristan_da_cunha": "Tristan da Cunha",
    "tristan_d_acunha": "Tristan da Cunha",
    "pitcairn_island": "Pitcairn Island",
    "pitcairn_islands": "Pitcairn Island",
    "pitcairn_islands_group": "Pitcairn Island",
    "rodrigues": "Rodrigues",
    "christmas_island": "Christmas Island",
    "norfolk_island": "Norfolk Island",

    # --- Pacific ---
    "fiji": "Fiji",
    "fiji_and_pitcairn": "Fiji",
    "fiji_and_pitcairn_islands": "Fiji",
    "fiji_and_pitcairn_islands_group": "Fiji",
    "western_pacific": "Western Pacific",
    "western_pacific_high_commission": "Western Pacific",
    "gilbert_and_ellice_islands": "Gilbert and Ellice Islands",
    "the_gilbert_and_ellice_islands_colony": "Gilbert and Ellice Islands",
    "the_british_solomon_islands_protectorate": "British Solomon Islands",
    "new_hebrides": "New Hebrides",
    "tonga": "Tonga",
    "kingdom_of_tonga": "Tonga",
    "nauru": "Nauru",
    "the_territory_of_new_guinea": "Territory of New Guinea",
    "cook_islands": "Cook Islands",
    "lord_howe_island": "Lord Howe Island",

    # --- Settler Colonies ---
    "canada": "Canada",
    "dominion_of_canada": "Canada",
    "new_south_wales": "New South Wales",
    "victoria": "Victoria",
    "queensland": "Queensland",
    "south_australia": "South Australia",
    "western_australia": "Western Australia",
    "tasmania": "Tasmania",
    "australia": "Australia",
    "the_commonwealth_of_australia": "Australia",
    "the_commonwealth": "Australia",
    "commonwealth_control": "Australia",
    "australia_new_south_wales": "Australia - New South Wales",
    "australia-new_south_wales": "Australia - New South Wales",
    "australia_queensland": "Australia - Queensland",
    "australia-queensland": "Australia - Queensland",
    "new_zealand": "New Zealand",
    "new_zealand_dependencies": "New Zealand",
    "newfoundland": "Newfoundland",
    "nova_scotia": "Nova Scotia",
    "new_brunswick": "New Brunswick",
    "prince_edward_island": "Prince Edward Island",
    "british_columbia": "British Columbia",
    "british_columbia_and_vancouver_island": "British Columbia",
    "vancouvers_island": "Vancouver's Island",
    "the_northern_territory": "Northern Territory (Australia)",
    "northern_territory": "Northern Territory (Australia)",
    "ontario": "Ontario",

    # --- Indian Ocean ---
    "mauritius": "Mauritius",
    "seychelles": "Seychelles",
    "seychelles_islands": "Seychelles",

    # --- Miscellaneous ---
    "miscellaneous_islands": "Miscellaneous Islands",
    "other_miscellaneous_possessions": "Miscellaneous Islands",
    "bulama": "Bulama",

    # --- Middle East (mandate era) ---
    "palestine": "Palestine",
    "iraq": "Iraq",
    "trans_jordan": "Transjordan",
    "transjordan": "Transjordan",
    "trans-jordan": "Transjordan",
    "mesopotamia": "Iraq",

    # --- Polar ---
    "british_antarctic_territory": "British Antarctic Territory",

    # --- Ashanti (sub-territory of Gold Coast) ---
    "ashanti": "Ashanti",
    "the_northern_territories": "Northern Territories (Gold Coast)",
}


# =============================================================================
# COLONY CLASSIFICATION
# =============================================================================

COLONY_CLASSIFICATIONS = {
    # Crown Colonies
    "Gold Coast": "Crown Colony",
    "Sierra Leone": "Crown Colony",
    "Gambia": "Crown Colony",
    "Lagos": "Crown Colony",
    "Nigeria": "Crown Colony",
    "Northern Nigeria": "Crown Colony",
    "Southern Nigeria": "Crown Colony",
    "Nigeria (Federation)": "Crown Colony",
    "Niger Coast Protectorate": "Protectorate",
    "Niger Territories": "Protectorate",
    "Ceylon": "Crown Colony",
    "Hong Kong": "Crown Colony",
    "Straits Settlements": "Crown Colony",
    "Jamaica": "Crown Colony",
    "Trinidad": "Crown Colony",
    "Trinidad and Tobago": "Crown Colony",
    "Barbados": "Crown Colony",
    "British Guiana": "Crown Colony",
    "British Honduras": "Crown Colony",
    "Bahamas": "Crown Colony",
    "Bermuda": "Crown Colony",
    "Malta": "Crown Colony",
    "Gibraltar": "Crown Colony",
    "Cyprus": "Crown Colony",
    "Falkland Islands": "Crown Colony",
    "St Helena": "Crown Colony",
    "Mauritius": "Crown Colony",
    "Seychelles": "Crown Colony",
    "Fiji": "Crown Colony",
    "Grenada": "Crown Colony",
    "St Lucia": "Crown Colony",
    "St Vincent": "Crown Colony",
    "Dominica": "Crown Colony",
    "Antigua": "Crown Colony",
    "Montserrat": "Crown Colony",
    "Nevis": "Crown Colony",
    "Anguilla": "Crown Colony",
    "Barbuda": "Crown Colony",
    "Tobago": "Crown Colony",
    "Virgin Islands": "Crown Colony",
    "Turks and Caicos Islands": "Crown Colony",
    "Cayman Islands": "Crown Colony",
    "Aden": "Crown Colony",
    "Singapore": "Crown Colony",
    "Labuan": "Crown Colony",
    "Wei-hai-Wei": "Crown Colony",
    "Heligoland": "Crown Colony",
    "Ascension": "Small Island",
    "Tristan da Cunha": "Small Island",
    "Pitcairn Island": "Small Island",
    "Christmas Island": "Small Island",
    "Norfolk Island": "Small Island",
    "Rodrigues": "Small Island",
    "Lord Howe Island": "Small Island",
    "Cook Islands": "Small Island",
    "Nauru": "Small Island",
    "Miscellaneous Islands": "Miscellaneous",
    "St Christopher and Nevis": "Crown Colony",

    # Protectorates
    "East Africa Protectorate": "Protectorate",
    "Kenya": "Protectorate",
    "Uganda": "Protectorate",
    "Zanzibar": "Protectorate",
    "Tanganyika": "Mandated Territory",
    "Nyasaland": "Protectorate",
    "Somaliland": "Protectorate",
    "North Borneo": "Protectorate",
    "Sarawak": "Protectorate",
    "Brunei": "Protectorate",
    "Swaziland": "Protectorate",
    "Basutoland": "Protectorate",
    "Bechuanaland": "Protectorate",
    "British Bechuanaland": "Crown Colony",
    "Zululand": "Crown Colony",
    "Amatongaland": "Crown Colony",
    "Griqualand West": "Crown Colony",
    "Tonga": "Protectorate",
    "Gilbert and Ellice Islands": "Protectorate",
    "British Solomon Islands": "Protectorate",
    "New Hebrides": "Protectorate",
    "Western Pacific": "Protectorate",
    "British New Guinea": "Protectorate",
    "Papua": "Protectorate",
    "Territory of New Guinea": "Mandated Territory",
    "Bulama": "Crown Colony",

    # Federated Territories
    "Leeward Islands": "Federated Territory",
    "Leeward Islands - Antigua": "Federated Territory",
    "Leeward Islands - Dominica": "Federated Territory",
    "Leeward Islands - Montserrat": "Federated Territory",
    "Leeward Islands - St Christopher Nevis": "Federated Territory",
    "Leeward Islands - Virgin Islands": "Federated Territory",
    "Windward Islands": "Federated Territory",
    "Windward Islands - Grenada": "Federated Territory",
    "Windward Islands - St Lucia": "Federated Territory",
    "Windward Islands - St Vincent": "Federated Territory",
    "Windward Islands - Tobago": "Federated Territory",
    "Federated Malay States": "Federated Territory",
    "Unfederated Malay States": "Federated Territory",
    "Federation of Malaya": "Federated Territory",
    "Malaya": "Federated Territory",
    "Malaysia": "Federated Territory",
    "Rhodesia and Nyasaland": "Federated Territory",
    "West Indies Federation": "Federated Territory",
    "West Indies": "Federated Territory",
    "West Indies (Cayman/Turks)": "Federated Territory",
    "West Indies (St Vincent)": "Federated Territory",

    # Settler Colonies
    "Canada": "Settler Colony",
    "New South Wales": "Settler Colony",
    "Victoria": "Settler Colony",
    "Queensland": "Settler Colony",
    "South Australia": "Settler Colony",
    "Western Australia": "Settler Colony",
    "Tasmania": "Settler Colony",
    "Australia": "Settler Colony",
    "Australia - New South Wales": "Settler Colony",
    "Australia - Queensland": "Settler Colony",
    "New Zealand": "Settler Colony",
    "Newfoundland": "Settler Colony",
    "Nova Scotia": "Settler Colony",
    "New Brunswick": "Settler Colony",
    "Prince Edward Island": "Settler Colony",
    "British Columbia": "Settler Colony",
    "Vancouver's Island": "Settler Colony",
    "Cape of Good Hope": "Settler Colony",
    "Natal": "Settler Colony",
    "South Africa": "Settler Colony",
    "Transvaal": "Settler Colony",
    "Orange River Colony": "Settler Colony",
    "Rhodesia": "Settler Colony",
    "Southern Rhodesia": "Settler Colony",
    "Northern Rhodesia": "Protectorate",
    "Northern Territory (Australia)": "Settler Colony",
    "Ontario": "Settler Colony",

    # Chartered Companies
    "British South Africa Company": "Chartered Company",
    "Imperial British East Africa Company": "Chartered Company",

    # High Commission / Administrative
    "East Africa High Commission": "Administrative",
    "High Commission Territories": "Administrative",
    "West African Settlements": "Administrative",

    # Polar/Dependencies
    "British Antarctic Territory": "Crown Colony",

    # Mandated Territories
    "Togoland": "Mandated Territory",
    "Cameroons (UK Trusteeship)": "Mandated Territory",
    "Palestine": "Mandated Territory",
    "Iraq": "Mandated Territory",
    "Transjordan": "Mandated Territory",

    # Malay sub-states
    "Johore": "Federated Territory",
    "Kedah": "Federated Territory",
    "Kelantan": "Federated Territory",
    "Perlis": "Federated Territory",
    "Trengganu": "Federated Territory",

    # Gold Coast sub-territories
    "Ashanti": "Crown Colony",
    "Northern Territories (Gold Coast)": "Crown Colony",
}

# Colony groupings for guide assignment
COLONY_GROUPS = {
    "West Africa": [
        "Gold Coast", "Sierra Leone", "Gambia", "Lagos", "Nigeria",
        "Northern Nigeria", "Southern Nigeria", "Nigeria (Federation)",
        "Niger Coast Protectorate", "Niger Territories",
        "West African Settlements", "Togoland",
        "Cameroons (UK Trusteeship)", "Ashanti",
        "Northern Territories (Gold Coast)",
    ],
    "East Africa": [
        "East Africa Protectorate", "Kenya", "Uganda", "Zanzibar",
        "Tanganyika", "Nyasaland", "Somaliland",
        "East Africa High Commission",
        "Imperial British East Africa Company",
    ],
    "Caribbean": [
        "Jamaica", "Trinidad", "Trinidad and Tobago", "Tobago",
        "Barbados", "British Guiana", "British Honduras", "Bahamas",
        "Bermuda", "Dominica", "Antigua", "Montserrat", "Nevis",
        "Anguilla", "Barbuda", "Grenada", "St Lucia", "St Vincent",
        "Virgin Islands", "Turks and Caicos Islands", "Cayman Islands",
        "St Christopher and Nevis", "West Indies", "West Indies Federation",
        "West Indies (Cayman/Turks)", "West Indies (St Vincent)",
    ],
    "South/Southeast Asia": [
        "Ceylon", "Hong Kong", "Straits Settlements", "Singapore",
        "Labuan", "North Borneo", "Sarawak", "Brunei",
        "Federated Malay States", "Unfederated Malay States",
        "Federation of Malaya", "Malaya", "Malaysia",
        "Johore", "Kedah", "Kelantan", "Perlis", "Trengganu",
        "Aden", "Wei-hai-Wei",
    ],
    "Mediterranean & Atlantic": [
        "Malta", "Gibraltar", "Cyprus", "Falkland Islands",
        "St Helena", "Heligoland", "Ascension", "Tristan da Cunha",
        "Pitcairn Island", "Christmas Island", "Rodrigues",
    ],
    "Pacific": [
        "Fiji", "Western Pacific", "Gilbert and Ellice Islands",
        "British Solomon Islands", "New Hebrides", "Tonga",
        "Nauru", "Territory of New Guinea", "British New Guinea",
        "Papua", "Norfolk Island", "Lord Howe Island", "Cook Islands",
    ],
    "Settler Colonies": [
        "Canada", "New South Wales", "Victoria", "Queensland",
        "South Australia", "Western Australia", "Tasmania", "Australia",
        "Australia - New South Wales", "Australia - Queensland",
        "New Zealand", "Newfoundland", "Nova Scotia", "New Brunswick",
        "Prince Edward Island", "British Columbia", "Vancouver's Island",
        "Cape of Good Hope", "Natal", "South Africa", "Transvaal",
        "Orange River Colony", "Rhodesia", "Southern Rhodesia",
        "Northern Rhodesia", "Northern Territory (Australia)", "Ontario",
    ],
    "Federated Territories": [
        "Leeward Islands", "Leeward Islands - Antigua",
        "Leeward Islands - Dominica", "Leeward Islands - Montserrat",
        "Leeward Islands - St Christopher Nevis",
        "Leeward Islands - Virgin Islands",
        "Windward Islands", "Windward Islands - Grenada",
        "Windward Islands - St Lucia", "Windward Islands - St Vincent",
        "Windward Islands - Tobago",
        "Rhodesia and Nyasaland",
    ],
    "Southern Africa": [
        "Basutoland", "Bechuanaland", "British Bechuanaland",
        "Swaziland", "Zululand", "Amatongaland", "Griqualand West",
        "High Commission Territories",
        "British South Africa Company", "Northern Rhodesia",
    ],
    "Middle East": [
        "Palestine", "Iraq", "Transjordan",
    ],
    "Miscellaneous": [
        "Miscellaneous Islands", "Bulama", "Mauritius", "Seychelles",
        "British Antarctic Territory",
    ],
}

# Federated territories that contain multiple sub-colonies in a single file
FEDERATED_MULTI_COLONY_FILES = {
    "Leeward Islands",
    "Windward Islands",
    "West Indies",
    "West Indies Federation",
    "High Commission Territories",
    "Miscellaneous Islands",
}


# =============================================================================
# FILENAME NORMALIZATION
# =============================================================================

def normalize_filename(filename: str) -> str:
    """Normalize a filename to a canonical lookup key.

    Strips extension, lowercases, collapses multiple underscores,
    strips leading/trailing underscores. Preserves dots and hyphens
    that appear in the original filename (e.g. st._helena, trans-jordan)
    since these are part of the canonical key.
    """
    stem = Path(filename).stem
    key = stem.lower()
    key = key.strip("_")
    # Collapse double/triple underscores
    key = re.sub(r'_+', '_', key)
    return key


def resolve_canonical_name(filename: str) -> str:
    """Resolve a filename to its canonical colony name."""
    key = normalize_filename(filename)

    # Direct lookup
    if key in CANONICAL_MAP:
        return CANONICAL_MAP[key]

    # Try with 'the_' prefix stripped
    if key.startswith("the_"):
        stripped = key[4:]
        if stripped in CANONICAL_MAP:
            return CANONICAL_MAP[stripped]

    # Try adding 'the_' prefix
    with_the = "the_" + key
    if with_the in CANONICAL_MAP:
        return CANONICAL_MAP[with_the]

    # Return normalized key as fallback (flag as unmapped)
    return f"UNMAPPED: {key}"


# =============================================================================
# CORPUS SCANNING
# =============================================================================

def scan_corpus(base_dir: Path) -> list:
    """Walk all *_manual_parsed/ directories and collect file metadata."""
    inventory = []

    for year_dir in sorted(base_dir.glob("*_manual_parsed")):
        year_match = re.match(r"(\d{4})_manual_parsed", year_dir.name)
        if not year_match:
            continue
        year = int(year_match.group(1))

        for filepath in sorted(year_dir.iterdir()):
            # Skip Zone.Identifier files
            if "Zone.Identifier" in filepath.name:
                continue
            if not filepath.is_file():
                continue

            stat = filepath.stat()
            file_size = stat.st_size

            # Count lines
            try:
                with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                line_count = content.count('\n') + (1 if content and not content.endswith('\n') else 0)
            except Exception:
                line_count = 0
                content = ""

            canonical_name = resolve_canonical_name(filepath.name)
            normalized_key = normalize_filename(filepath.name)

            # Determine size tier
            if file_size == 0:
                size_tier = "empty"
            elif file_size < 5000:
                size_tier = "tiny"
            elif file_size < 20000:
                size_tier = "small"
            elif file_size < 50000:
                size_tier = "medium"
            elif file_size < 100000:
                size_tier = "large"
            elif file_size < 200000:
                size_tier = "very_large"
            else:
                size_tier = "enormous"

            classification = COLONY_CLASSIFICATIONS.get(canonical_name, "Unknown")

            # Determine colony group
            colony_group = "Unknown"
            for group, members in COLONY_GROUPS.items():
                if canonical_name in members:
                    colony_group = group
                    break

            # Detect if this is a federated multi-colony file
            is_federated_multi = canonical_name in FEDERATED_MULTI_COLONY_FILES

            # Detect file extension
            extension = filepath.suffix.lower()

            entry = {
                "year": year,
                "filename": filepath.name,
                "filepath": str(filepath.relative_to(base_dir)),
                "canonical_name": canonical_name,
                "normalized_key": normalized_key,
                "classification": classification,
                "colony_group": colony_group,
                "file_size": file_size,
                "line_count": line_count,
                "size_tier": size_tier,
                "extension": extension,
                "is_federated_multi": is_federated_multi,
            }
            inventory.append(entry)

    return inventory


# =============================================================================
# ANOMALY DETECTION
# =============================================================================

def detect_anomalies(inventory: list) -> list:
    """Flag files that need manual review."""
    anomalies = []

    # Group by canonical name to detect naming inconsistencies
    by_colony = defaultdict(list)
    for entry in inventory:
        by_colony[entry["canonical_name"]].append(entry)

    for entry in inventory:
        # Empty files
        if entry["file_size"] == 0:
            anomalies.append({
                "type": "EMPTY_FILE",
                "severity": "HIGH",
                "filepath": entry["filepath"],
                "message": f"Empty file: {entry['filepath']}"
            })

        # Unmapped filenames
        if entry["canonical_name"].startswith("UNMAPPED:"):
            anomalies.append({
                "type": "UNMAPPED_FILENAME",
                "severity": "HIGH",
                "filepath": entry["filepath"],
                "message": f"Cannot map '{entry['filename']}' to canonical colony name"
            })

        # Enormous files (>200KB) — likely need special handling
        if entry["size_tier"] == "enormous":
            anomalies.append({
                "type": "ENORMOUS_FILE",
                "severity": "MEDIUM",
                "filepath": entry["filepath"],
                "message": f"Very large file ({entry['file_size']:,} bytes): {entry['filepath']} — may need section-by-section extraction"
            })

        # Suspiciously large for colony type (>300KB for non-settler colonies)
        if (entry["file_size"] > 300000
                and entry["classification"] not in ("Settler Colony", "Federated Territory", "Administrative", "Miscellaneous")):
            anomalies.append({
                "type": "SUSPICIOUS_SIZE",
                "severity": "HIGH",
                "filepath": entry["filepath"],
                "message": f"Suspiciously large for {entry['classification']}: {entry['file_size']:,} bytes — possible parsing artifact"
            })

        # Unknown classification
        if entry["classification"] == "Unknown":
            anomalies.append({
                "type": "UNKNOWN_CLASSIFICATION",
                "severity": "MEDIUM",
                "filepath": entry["filepath"],
                "message": f"Unknown colony classification for '{entry['canonical_name']}'"
            })

    # Check for naming inconsistencies within a colony
    for colony, entries in by_colony.items():
        filenames = set(e["filename"] for e in entries)
        if len(filenames) > 3:
            anomalies.append({
                "type": "NAMING_INCONSISTENCY",
                "severity": "LOW",
                "filepath": entries[0]["filepath"],
                "message": f"Colony '{colony}' has {len(filenames)} distinct filenames: {sorted(filenames)[:5]}..."
            })

    return anomalies


# =============================================================================
# COVERAGE MATRIX
# =============================================================================

def build_coverage_matrix(inventory: list) -> tuple:
    """Build colony × year coverage matrix.

    Returns (headers, rows) where headers = ["Colony", year1, year2, ...]
    and rows = [["Colony Name", 1/0, 1/0, ...], ...]
    """
    # Collect all years and colonies
    years = sorted(set(e["year"] for e in inventory))
    colonies = sorted(set(e["canonical_name"] for e in inventory
                          if not e["canonical_name"].startswith("UNMAPPED:")))

    # Build presence set
    presence = set()
    for e in inventory:
        presence.add((e["canonical_name"], e["year"]))

    headers = ["Colony"] + [str(y) for y in years]
    rows = []
    for colony in colonies:
        row = [colony]
        for year in years:
            row.append(1 if (colony, year) in presence else 0)
        rows.append(row)

    return headers, rows


# =============================================================================
# STATISTICS
# =============================================================================

def compute_statistics(inventory: list) -> dict:
    """Compute corpus-wide statistics."""
    total_files = len(inventory)
    non_empty = [e for e in inventory if e["file_size"] > 0]
    total_bytes = sum(e["file_size"] for e in inventory)
    total_lines = sum(e["line_count"] for e in inventory)

    # Size distribution
    size_dist = defaultdict(int)
    for e in inventory:
        size_dist[e["size_tier"]] += 1

    # Classification distribution
    class_dist = defaultdict(int)
    for e in inventory:
        class_dist[e["classification"]] += 1

    # Group distribution
    group_dist = defaultdict(int)
    for e in inventory:
        group_dist[e["colony_group"]] += 1

    # Extension distribution
    ext_dist = defaultdict(int)
    for e in inventory:
        ext_dist[e["extension"]] += 1

    # Year range
    years = sorted(set(e["year"] for e in inventory))

    # Unique colonies
    colonies = set(e["canonical_name"] for e in inventory
                   if not e["canonical_name"].startswith("UNMAPPED:"))

    # Federated multi-colony files
    federated_count = sum(1 for e in inventory if e["is_federated_multi"])

    return {
        "total_files": total_files,
        "non_empty_files": len(non_empty),
        "total_bytes": total_bytes,
        "total_lines": total_lines,
        "year_range": [min(years), max(years)] if years else [],
        "year_count": len(years),
        "unique_colonies": len(colonies),
        "colony_names": sorted(colonies),
        "size_distribution": dict(sorted(size_dist.items())),
        "classification_distribution": dict(sorted(class_dist.items())),
        "group_distribution": dict(sorted(group_dist.items())),
        "extension_distribution": dict(sorted(ext_dist.items())),
        "federated_multi_colony_files": federated_count,
        "largest_files": sorted(
            [{"filepath": e["filepath"], "size": e["file_size"], "colony": e["canonical_name"]}
             for e in inventory],
            key=lambda x: x["size"],
            reverse=True
        )[:20],
    }


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Build Colonial Office List corpus inventory")
    parser.add_argument("--base-dir", type=Path, default=BASE_DIR,
                        help="Base directory containing *_manual_parsed/ directories")
    args = parser.parse_args()

    base_dir = args.base_dir.resolve()
    output_dir = base_dir / "scaffolding"
    output_dir.mkdir(exist_ok=True)

    print("=" * 70)
    print("COLONIAL OFFICE LIST - CORPUS INVENTORY BUILDER")
    print("=" * 70)
    print(f"Base directory: {base_dir}")

    # Scan corpus
    print("\nScanning corpus...")
    inventory = scan_corpus(base_dir)
    print(f"  Found {len(inventory)} files")

    # Detect anomalies
    print("\nDetecting anomalies...")
    anomalies = detect_anomalies(inventory)
    print(f"  Found {len(anomalies)} anomalies")

    # Compute statistics
    print("\nComputing statistics...")
    stats = compute_statistics(inventory)

    # Build coverage matrix
    print("\nBuilding coverage matrix...")
    headers, matrix_rows = build_coverage_matrix(inventory)

    # --- Write outputs ---

    # 1. corpus_inventory.json
    inventory_path = output_dir / "corpus_inventory.json"
    output_data = {
        "generated": "build_corpus_inventory.py",
        "statistics": stats,
        "files": inventory,
    }
    with open(inventory_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    print(f"\n  Wrote: {inventory_path}")

    # 2. coverage_matrix.csv
    matrix_path = output_dir / "coverage_matrix.csv"
    with open(matrix_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in matrix_rows:
            writer.writerow(row)
    print(f"  Wrote: {matrix_path}")

    # 3. anomalies.txt
    anomalies_path = output_dir / "anomalies.txt"
    with open(anomalies_path, 'w') as f:
        f.write("COLONIAL OFFICE LIST - CORPUS ANOMALIES\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total anomalies: {len(anomalies)}\n\n")

        # Group by type
        by_type = defaultdict(list)
        for a in anomalies:
            by_type[a["type"]].append(a)

        for atype in sorted(by_type.keys()):
            items = by_type[atype]
            f.write(f"\n{'─' * 50}\n")
            f.write(f"{atype} ({len(items)} issues)\n")
            f.write(f"{'─' * 50}\n\n")
            for item in sorted(items, key=lambda x: x["filepath"]):
                f.write(f"  [{item['severity']}] {item['message']}\n")
    print(f"  Wrote: {anomalies_path}")

    # --- Print summary ---
    print(f"\n{'=' * 70}")
    print("CORPUS SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Total files:        {stats['total_files']:,}")
    print(f"  Non-empty files:    {stats['non_empty_files']:,}")
    print(f"  Total size:         {stats['total_bytes']:,} bytes ({stats['total_bytes'] / 1024 / 1024:.1f} MB)")
    print(f"  Total lines:        {stats['total_lines']:,}")
    print(f"  Year range:         {stats['year_range'][0]}-{stats['year_range'][1]} ({stats['year_count']} years)")
    print(f"  Unique colonies:    {stats['unique_colonies']}")
    print(f"  Federated multi:    {stats['federated_multi_colony_files']} files")

    print(f"\n  Size distribution:")
    for tier, count in sorted(stats['size_distribution'].items()):
        print(f"    {tier:12s}: {count:4d} files")

    print(f"\n  Classification distribution:")
    for cls, count in sorted(stats['classification_distribution'].items(), key=lambda x: -x[1]):
        print(f"    {cls:25s}: {count:4d} files")

    print(f"\n  Colony group distribution:")
    for group, count in sorted(stats['group_distribution'].items(), key=lambda x: -x[1]):
        print(f"    {group:25s}: {count:4d} files")

    print(f"\n  Extension distribution:")
    for ext, count in sorted(stats['extension_distribution'].items(), key=lambda x: -x[1]):
        print(f"    {ext:10s}: {count:4d} files")

    print(f"\n  Anomalies by type:")
    by_type = defaultdict(int)
    for a in anomalies:
        by_type[a["type"]] += 1
    for atype, count in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"    {atype:30s}: {count:4d}")

    print(f"\n{'=' * 70}")
    print("Done. Review anomalies.txt for issues requiring attention.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
COL Governor Chain Parser & Ghost Detector
===========================================

Parses historical governor/administrator chain sections from the raw Colonial
Office List text files and uses them to identify ghost PersonRecords in Neo4j.

The COL includes sections listing ALL past governors of each colony (e.g.
"## Governors", "### Administrators", "### Governors since the Union...").
Our extraction pipeline treated these as current officials, creating ~6,000+
ghost PersonRecords. This script parses those sections and flags the ghosts.

Usage:
    python col_parse_governor_chains.py                         # parse chains, write JSON
    python col_parse_governor_chains.py --detect                # parse + query Neo4j
    python col_parse_governor_chains.py --detect --quarantine   # mark ghosts
    python col_parse_governor_chains.py --detect --dry-run      # detect, no writes (default)
    python col_parse_governor_chains.py --detect --report       # write markdown report
    python col_parse_governor_chains.py --stats                 # show current quarantine counts

Requires:
    pip install neo4j
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
CROSSWALK_PATH = REPO_DIR / "scaffolding" / "col_kg_crosswalk.json"
OUTPUT_JSON = REPO_DIR / "governor_chains_parsed.json"
REPORT_PATH = REPO_DIR / "GOVERNOR_CHAIN_GHOST_REPORT.md"

# Governor-class position keywords (same as col_detect_ghosts.py)
GOVERNOR_POSITION_KEYWORDS = [
    "governor", "administrator", "high commissioner",
    "governor-general", "governor general",
    "officer administering", "acting governor",
    "lieutenant-governor", "lieutenant governor",
    "captain-general", "captain general",
    "commander-in-chief", "commander in chief",
    "commissioners since",  # for entries like "Commissioners since 1910"
]

# Section headers that introduce governor chains (regex patterns, case-insensitive)
# Two families:
#   (A) Markdown headers: start with one or more '#' characters
#   (B) Plain-text headers: no '#', stand alone on their line, often followed by
#       a blank line then the chain entries.  These appear in many older COL
#       editions whose raw text was not fully converted to markdown.
CHAIN_HEADER_PATTERNS = [
    # ── (A) Markdown headers ──────────────────────────────────────────────────
    r"^#{1,3}\s+Governors?\b",
    r"^#{1,3}\s+Administrators?\b",
    r"^#{1,3}\s+High\s+Commissioners?\b",
    r"^#{1,3}\s+Lieutenant-Governors?\b",
    r"^#{1,3}\s+Lieutenant\s+Governors?\b",
    r"^#{1,3}\s+Governors?-General\b",
    r"^#{1,3}\s+Governor-Generals?\b",
    r"^#{1,3}\s+Resident\s+Commissioners?\b",
    # Markdown with qualifiers
    r"^#{1,3}\s+Governors?\s+since\b",
    r"^#{1,3}\s+Governors?\s+from\b",
    r"^#{1,3}\s+Governors?\s+of\b",
    r"^#{1,3}\s+Administrators?\s+of\b",
    r"^#{1,3}\s+Administrators?\s+since\b",
    r"^#{1,3}\s+Commissioners?\s+since\b",
    r"^#{1,3}\s+Commissioners?\s+and\b",
    r"^#{1,3}\s+List\s+of\s+Governors?\b",
    r"^#{1,3}\s+List\s+of\s+Commissioners?\b",
    r"^#{1,3}\s+French\s+Governors?\b",
    r"^#{1,3}\s+Governors?-in-Chief\b",
    r"^#{1,3}\s+GOVERNOR\b",
    r"^#{1,3}\s+GOVERNORS?\b",
    r"^#{1,3}\s+ADMINISTRATORS?\b",
    r"^#{1,3}\s+COMMISSIONERS?\b",
    r"^#{1,3}\s+Governors?\s+and\s+(Administrators?|Commanders?)\b",
    r"^#{1,3}\s+ADMINISTRATORS?\s+AND\s+GOVERNORS?\b",
    r"^#{1,3}\s+Succession\s+of\s+(Governors?|Lieutenant-Governors?)\b",
    r"^#{1,3}\s+Lieutenant-Governors?\s+since\b",
    r"^#{1,3}\s+Lieutenant-Governors?\s+of\b",
    r"^#{1,3}\s+Governors?-General\s+since\b",
    r"^#{1,3}\s+Governors?-General\s+of\b",
    r"^#{1,3}\s+High\s+Commissioners?\s+and\b",

    # ── (B) Plain-text headers (no '#') ──────────────────────────────────────
    # These lines appear alone on a line, possibly with trailing ".", "*", "†", "§"
    # The trailing punctuation pattern is: [.\*†§‡¶]?  at end of line.
    # We anchor with ^ and $ (MULTILINE implied by the scanner).

    # "Governors." / "Governors.*" / "Governors.†" / "GOVERNORS."
    # Trailing punctuation may be ".", ".*", ".†", ".*†", etc.
    r"^Governors?\s*(?:[.*†§‡¶]{0,3})?\s*$",
    r"^GOVERNORS?\s*(?:[.*†§‡¶]{0,3})?\s*$",

    # "Governors since 1855." / "Governors since Confederation." etc.
    r"^Governors?\s+since\b[^()]*[.*†§‡¶]?\s*$",

    # "Governors from 1900."
    r"^Governors?\s+from\s+\d{4}[^()]*[.*†§‡¶]?\s*$",

    # "Governors of Queensland." / "Governors of Tasmania since 1881."
    r"^Governors?\s+of\s+\w[^()]*[.*†§‡¶]?\s*$",

    # "Governors-General of the Commonwealth." / "Governors-General since Confederation."
    r"^Governors?-General\b[^()]*[.*†§‡¶]?\s*$",
    r"^Governors?-General\s+(?:of|since|from)\b[^()]*[.*†§‡¶]?\s*$",

    # "Governors and Administrators" / "Governors and Commanders-in-Chief..."
    r"^Governors?\s+and\s+(?:Administrators?|Commanders?)[^()]*[.*†§‡¶]?\s*$",
    r"^ADMINISTRATORS?\s+AND\s+GOVERNORS?\s*[.*†§‡¶]?\s*$",

    # "Governors-in-Chief, West Africa Settlements."
    r"^Governors?-in-Chief\b[^()]*[.*†§‡¶]?\s*$",

    # "Administrators." / "Administrators.*" / "Administrators since ..."
    r"^Administrators?\s*(?:[.*†§‡¶]{0,3})?\s*$",
    r"^ADMINISTRATORS?\s*(?:[.*†§‡¶]{0,3})?\s*$",
    r"^Administrators?\s+since\b[^()]*[.*†§‡¶]?\s*$",
    # "Administrators of St. Vincent since 1888." but NOT "Administrator of the Govt."
    r"^Administrators?\s+of\s+(?!the\s+Govt|the\s+Government)[A-Z][^()]*[.*†§‡¶]?\s*$",

    # "High Commissioners." / "High Commissioners and Governors."
    r"^High\s+Commissioners?\s*[.*†§‡¶]?\s*$",
    r"^High\s+Commissioners?\s+(?:and|since|of)\b[^()]*[.*†§‡¶]?\s*$",

    # "Lieutenant-Governors." / "Lieutenant-Governors since Confederation."
    r"^Lieutenant-Governors?\s*[.*†§‡¶]?\s*$",
    r"^Lieutenant-Governors?\s+(?:since|of|from|before)\b[^()]*[.*†§‡¶]?\s*$",
    r"^Lieutenant-Governors?\s+and\b[^()]*[.*†§‡¶]?\s*$",

    # "Commissioners since 1910."
    r"^Commissioners?\s+since\b[^()]*[.*†§‡¶]?\s*$",

    # "List of Governors." / "List of Governors since 1880." / "List of Governors of ..."
    r"^List\s+of\s+Governors?\b[^()]*[.*†§‡¶]?\s*$",
    r"^List\s+of\s+(?:Lieutenant-Governors?|High\s+Commissioners?)\b[^()]*[.*†§‡¶]?\s*$",

    # "Succession of Governors & Lieutenant-Governors of Tasmania since 1813:"
    r"^Succession\s+of\s+(?:Governors?|Lieutenant-Governors?)\b[^()]*[.*†§‡¶:]?\s*$",

    # "Governors, Lieutenant-Governors, and Commandants of the Fortress of Gibraltar..."
    r"^Governors?,\s+Lieutenant-Governors?\b[^()]*[.*†§‡¶]?\s*$",

    # "Governors for Great Britain." (Mauritius etc.)
    r"^Governors?\s+for\s+Great\s+Britain\b[^()]*[.*†§‡¶]?\s*$",
    r"^French\s+Governors?\b[^()]*[.*†§‡¶]?\s*$",
]

# Patterns that look like chain entries: year followed by a name
# We need to handle:
#   - **1660** G. D'Oyley.
#   - **1661** Lord Windsor.
#   1808 Duke of Manchester.
#   1892. Sir Walter Joseph Sendall, K.C.M.G.
#   | 1831 | Maj.-Gen. Sir Benjamin D'Urban. |   (table row)
#   **2 June 1897** Sir H. E. H. Jerningham, K.C.M.G.   (date with month)
#   **Jan. 1722** M. de Nyon.

# Regex to extract year from various year formats
YEAR_PATTERN = re.compile(
    r"""
    (?:
        \*{0,2}                         # optional bold markers
        (?:                             # optional day+month prefix
            \d{1,2}\.?\s+              # day
            (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept?|Oct|Nov|Dec)[a-z]*\.?\s+  # month
        )?
        (\d{4})                         # THE YEAR (group 1)
        \.?                             # optional trailing dot
        \*{0,2}                         # optional bold markers
    )
    """,
    re.VERBOSE | re.IGNORECASE,
)

# Honours and post-nominal letters to strip
HONOURS_PATTERN = re.compile(
    r"""
    ,?\s+                               # comma + space before honours
    (?:
        [A-Z]\.(?:[A-Z]\.){1,5}        # e.g. K.C.M.G., G.C.B.
        |[A-Z]{2,6}(?:\.[A-Z]{1,4})*  # e.g. CB, DSO, etc.
        |Bart\.?
        |Esq\.?
        |LL\.D\.?
        |Q\.C\.?
        |K\.C\.
    )
    (?=\s*(?:,\s*[A-Z]\.|\s*\(|\s*$|\.?\s*$))  # lookahead
    """,
    re.VERBOSE,
)

# Titles and military ranks to recognise (but keep for surname extraction)
TITLE_PREFIXES = re.compile(
    r"""^
    (?:
        Sir\s+ | Lord\s+ | Lady\s+ | Dame\s+ |
        The\s+(?:Rt\.?\s+)?(?:Hon(?:ourable)?\.?\s+)? |
        Earl\s+(?:of\s+)? |
        Duke\s+(?:of\s+)? |
        Baron\s+(?:of\s+)? |
        Viscount\s+(?:[A-Za-z\s]+\s+of\s+)? |
        Marquis\s+(?:of\s+)? |
        Marquess\s+(?:of\s+)? |
        Major-Gen(?:eral)?\.?\s+ |
        Major\s+Gen(?:eral)?\.?\s+ |
        Maj\.?-?Gen\.?\s+ |
        Lieut\.?-?Gen(?:eral)?\.?\s+ |
        Lieut\.?-?Col(?:onel)?\.?\s+ |
        Lt\.?-?Gen(?:eral)?\.?\s+ |
        Lt\.?-?Col(?:onel)?\.?\s+ |
        Col(?:onel)?\.?\s+ |
        Brig(?:adier)?\.?-?Gen(?:eral)?\.?\s+ |
        Brig(?:adier)?\.?\s+ |
        Capt(?:ain)?\.?\s+ |
        Major\s+ |
        Admiral\s+ |
        Gen(?:eral)?\.?\s+ |
        Rear-Admiral\s+ |
        Captain\s+ |
        Rev(?:erend)?\.?\s+ |
        M\.?\s+ |  # French titles: "M. de Nyon"
        Le\s+(?:Chevalier|Vicomte|Comte|Sieur)\s+ |
        Hon(?:ourable)?\.?\s+(?:Sir\s+)?
    )+
    """,
    re.VERBOSE | re.IGNORECASE,
)

# Suffixes that indicate role (not the name itself)
ROLE_SUFFIXES = re.compile(
    r"""
    \s*
    (?:
        \((?:afterwards?|later|now|acting|Lieutenant[-\s]Governor|
             Lieut\.?-?Governor|Administrator|Consul-General|
             Commandant|Lieutenant|acting\s+Governor|par\s+int[ée]rim)[^)]*\)
        |\s+\(afterwards?[^)]*\)
        |,\s+(?:Lieutenant[-\s]Governor|Lieut\.?-?Governor|
               Administrator|Consulat[-\s]General|
               Governor(?:\s+of[^,.]+)?)
    )
    """,
    re.VERBOSE | re.IGNORECASE,
)

# Patterns that indicate this is NOT a chain entry (false positives)
NOT_A_CHAIN_LINE = re.compile(
    r"""
    ^\s*(?:
        \|.*\|.*\|   |  # markdown table with multiple columns
        \#           |  # another section header
        \*\*(?![\d])    # bold non-year content at start
    )
    """,
    re.VERBOSE,
)


# =============================================================================
# .ENV LOADING (same pattern as col_detect_ghosts.py)
# =============================================================================

def _load_dotenv():
    """Load .env file from repo root."""
    env_path = REPO_DIR / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())


_load_dotenv()

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")


# =============================================================================
# COLONY NAME MAPPING
# =============================================================================

def build_filename_to_colony_map():
    """
    Build a mapping from text file stem (e.g. 'sierra_leone') → COL colony name
    (e.g. 'Sierra Leone').

    Strategy:
    1. Load crosswalk for canonical COL names.
    2. Generate lowercase underscored versions of each name.
    3. Supplement with hardcoded exceptions.
    """
    if not CROSSWALK_PATH.exists():
        print(f"WARNING: Crosswalk not found at {CROSSWALK_PATH}")
        return {}

    with open(CROSSWALK_PATH) as f:
        crosswalk = json.load(f)

    col_names = list(crosswalk.keys())

    def to_slug(name: str) -> str:
        """Convert 'British Guiana' → 'british_guiana'."""
        return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")

    slug_to_col = {}
    for name in col_names:
        slug_to_col[to_slug(name)] = name

    # Hardcoded overrides for difficult cases
    overrides = {
        "the_gambia": "Gambia",
        "gambia": "Gambia",
        "dominion_of_canada": "Canada",
        "canada": "Canada",
        "victoria": "Victoria",
        "federation_of_malaya": "Federation of Malaya",
        "bahama_islands": "Bahamas",
        "bahamas": "Bahamas",
        "st_christopher_nevis_anguilla": "St Christopher and Nevis",
        "st_christopher_and_nevis": "St Christopher and Nevis",
        "pitcairn_islands": "Pitcairn Island",
        "miscellaneous_islands": "Miscellaneous Islands",
        "west_africa_settlements": "West Africa Settlements",
        "nigeria": "Nigeria",
        "northern_nigeria": "Northern Nigeria",
        "southern_nigeria": "Southern Nigeria",
        "gold_coast": "Gold Coast",
        "trinidad_and_tobago": "Trinidad and Tobago",
        "trinidad": "Trinidad",
        "tobago": "Tobago",
        "british_zambezia_and_british_central_africa": "British Central Africa",
        "windward_islands": "Windward Islands",
        "leeward_islands": "Leeward Islands",
        "kenya": "Kenya",
        "tanganyika": "Tanganyika",
        "uganda": "Uganda",
        "zanzibar": "Zanzibar",
        "rhodesia": "Rhodesia",
        "nyasaland": "Nyasaland",
        "northern_rhodesia": "Northern Rhodesia",
        "southern_rhodesia": "Southern Rhodesia",
        "somaliland_protectorate": "British Somaliland",
        "somaliland": "British Somaliland",
        "ceylon": "Ceylon",
        "straits_settlements": "Straits Settlements",
        "hong_kong": "Hong Kong",
        "north_borneo": "North Borneo",
        "sarawak": "Sarawak",
        "brunei": "Brunei",
        "federated_malay_states": "Federated Malay States",
        "unfederated_malay_states": "Unfederated Malay States",
        "weihaiwei": "Weihaiwei",
        "gilbert_and_ellice_islands": "Gilbert and Ellice Islands",
        "western_pacific": "Western Pacific",
        "papua": "Papua",
        "territory_of_new_guinea": "Territory of New Guinea",
        "nauru": "Nauru",
        "cook_islands": "Cook Islands",
        "tonga": "Tonga",
        "new_south_wales": "New South Wales",
        "victoria": "Victoria",
        "south_australia": "South Australia",
        "western_australia": "Western Australia",
        "queensland": "Queensland",
        "tasmania": "Tasmania",
        "new_zealand": "New Zealand",
        "cape_of_good_hope": "Cape of Good Hope",
        "natal": "Natal",
        "transvaal": "Transvaal",
        "orange_river_colony": "Orange River Colony",
        "zululand": "Zululand",
        "griqualand_west": "Griqualand West",
        "basutoland": "Basutoland",
        "bechuanaland": "Bechuanaland",
        "swaziland": "Swaziland",
        "high_commission_territories": "High Commission Territories",
        "east_africa_high_commission": "East Africa High Commission",
        "federation_of_rhodesia_and_nyasaland": "Federation of Rhodesia and Nyasaland",
        "iraq": "Iraq",
        "palestine": "Palestine",
        "transjordan": "Transjordan",
        "mesopotamia": "Mesopotamia",
        "nigeria": "Nigeria",
        "the_windward_islands": "Windward Islands",
        "windward_islands": "Windward Islands",

        # AUSTRALIA.txt is a combined Commonwealth + States file.
        # Map the filename itself to New South Wales (the "Governors since 1855"
        # chain with no colony hint is the NSW chain).  Sub-state chains
        # (Queensland, Tasmania, etc.) are extracted via colony_hint.
        "australia": "New South Wales",
        "AUSTRALIA": "New South Wales",
        "australia-new_south_wales": "New South Wales",
        "australia-queensland": "Queensland",

        # Colony hints from plain-text headers
        "commonwealth_of_australia": "New South Wales",  # GG chain — no separate colony node
        "New South Wales": "New South Wales",
        "new_south_wales": "New South Wales",
        "queensland": "Queensland",
        "tasmania": "Tasmania",
        "victoria": "Victoria",
        "south_australia": "South Australia",
        "western_australia": "Western Australia",

        # Alternate / historical filename variants
        "BERMUDAS": "Bermuda",
        "bermudas": "Bermuda",
        "BECHUANALAND_PROTECTORATE": "Bechuanaland",
        "bechuanaland_protectorate": "Bechuanaland",
        "The_Bechuanaland_Protectorate": "Bechuanaland",
        "BRITISH_CENTRAL_AFRICA_PROTECTORATE": "British Central Africa",
        "BRITISH_EAST_AFRICA_PROTECTORATE": "Kenya",
        "EAST_AFRICA_PROTECTORATE": "Kenya",
        "east_africa_protectorate": "Kenya",
        "THE_KENYA_COLONY_AND_PROTECTORATE": "Kenya",
        "BRITISH_EAST_AFRICA_ZANZIBAR_UGANDA": "Kenya",
        "THE_GOLD_COAST": "Gold Coast",
        "the_gold_coast": "Gold Coast",
        "THE_GOLD_COAST_COLONY": "Gold Coast",
        "the_gold_coast_colony": "Gold Coast",
        "GOLD_COAST_COLONY": "Gold Coast",
        "gold_coast_colony": "Gold Coast",
        "GOLD_COAST_GHANA": "Gold Coast",
        "ashanti": "Gold Coast",
        "the_niger_territories": "Northern Nigeria",
        "THE_LEEWARD_ISLANDS": "Leeward Islands",
        "the_leeward_islands": "Leeward Islands",
        "LEEWARD_ISLANDS_ANTIGUA": "Antigua",
        "LEEWARD_ISLANDS___ANTIGUA": "Antigua",
        "WINDWARD_ISLANDS_GRENADA": "Grenada",
        "WINDWARD_ISLANDS___GRENADA": "Grenada",
        "WINDWARD_ISLANDS_ST_LUCIA": "St Lucia",
        "WINDWARD_ISLANDS___ST._LUCIA": "St Lucia",
        "WINDWARD_ISLANDS_ST_VINCENT": "St Vincent",
        "WINDWARD_ISLANDS___ST._VINCENT": "St Vincent",
        "WINDWARD_ISLANDS___TOBAGO": "Tobago",
        "grenada_windward": "Grenada",
        "GRENADE": "Grenada",
        "grenade_ref": "Grenada",
        "tobago_windward": "Tobago",
        "tobago_ref": "Tobago",
        "barbados_windward": "Barbados",
        "THE_TRANSVAAL": "Transvaal",
        "the_transvaal": "Transvaal",
        "TANGANYIKA_TERRITORY": "Tanganyika",
        "tanganyika_territory": "Tanganyika",
        "NYASALAND_PROTECTORATE": "Nyasaland",
        "nyasaland_protectorate": "Nyasaland",
        "Nyasaland_Protectorate": "Nyasaland",
        "SOMALILAND": "British Somaliland",
        "British_Somaliland_Protectorate": "British Somaliland",
        "FEDERATION_OF_NIGERIA": "Nigeria",
        "federation_of_nigeria": "Nigeria",
        "TRANS-JORDAN": "Transjordan",
        "TRANS_JORDAN": "Transjordan",
        "WEI_HAI_WEI": "Weihaiwei",
        "THE_COMMONWEALTH_OF_AUSTRALIA": "New South Wales",
        "THE_COMMONWEALTH": "New South Wales",
        "THE_TERRITORY_OF_NEW_GUINEA": "Territory of New Guinea",
        "THE_FEDERATED_MALAY_STATES": "Federated Malay States",
        "MALAYA_FEDERATED_MALAY_STATES": "Federated Malay States",
        "MALAYA__FEDERATED_MALAY_STATES": "Federated Malay States",
        "MALAYA_STRAITS_SETTLEMENTS": "Straits Settlements",
        "MALAYA__STRAITS_SETTLEMENTS": "Straits Settlements",
        "MALAYA_UNFEDERATED_MALAY_STATES": "Unfederated Malay States",
        "MALAY_STATES_UNFEDERATED": "Unfederated Malay States",
        "MALAY_STATES_NOT_INCLUDED_IN_THE_FEDERATION": "Unfederated Malay States",
        "FEDERATION_OF_RHODESIA_AND_NYASALAND": "Federation of Rhodesia and Nyasaland",
        "THE_FEDERATION_OF_RHODESIA_AND_NYASALAND": "Federation of Rhodesia and Nyasaland",
        "RHODESIA_AND_NYASALAND": "Federation of Rhodesia and Nyasaland",
        "federation_rhodesia_nyasaland": "Federation of Rhodesia and Nyasaland",
        "Rhodesia_and_Nyasaland": "Federation of Rhodesia and Nyasaland",
        "FALKLAND_ISLANDS_AND_DEPENDENCIES": "Falkland Islands",
        "falkland_islands_and_dependencies": "Falkland Islands",
        "Falkland_Islands_and_Dependencies": "Falkland Islands",
        "FIJI_AND_PITCAIRN": "Fiji",
        "fiji_and_pitcairn_islands": "Fiji",
        "fiji_and_pitcairn_islands_group": "Fiji",
        "Fiji_and_Pitcairn_Islands_Group": "Fiji",
        "THE_GILBERT_AND_ELLICE_ISLANDS_COLONY": "Gilbert and Ellice Islands",
        "WEST_AFRICA_GAMBIA": "Gambia",
        "Aden_Colony": "Aden",
        "aden_colony": "Aden",
        "seychelles_islands": "Seychelles",
        "singapore_and_dependencies": "Singapore",
        "State_of_Singapore": "Singapore",
        "state_of_singapore": "Singapore",
        "british_north_borneo": "North Borneo",
        "BRITISH_COLUMBIA_AND_VANCOUVER_ISLAND": "British Columbia",
        "NORTHERN_RHODESIA": "Northern Rhodesia",
        "SOUTHERN_RHODESIA": "Southern Rhodesia",
        "southern_rhodesia_administration": "Southern Rhodesia",
        "trinidad_tobago": "Trinidad and Tobago",
        "KINGDOM_OF_TONGA": "Tonga",
        "kingdom_of_tonga": "Tonga",
        "WESTERN_PACIFIC_HIGH_COMMISSION": "Western Pacific",
        "western_pacific_high_commission": "Western Pacific",
        "Western_Pacific_High_Commission": "Western Pacific",
        "helgoland": "Heligoland",
        "GRENA_DA": "Grenada",
        "grena_da": "Grenada",
        "helgoland": "Heligoland",
        "ontario": "Canada",
        "west_africa": "West Africa Settlements",
        "west_african_settlements": "West Africa Settlements",
        "MALAYA": "Federation of Malaya",
    }
    slug_to_col.update(overrides)

    # Also map ALL_CAPS filename variants (e.g. JAMAICA → Jamaica)
    for name in col_names:
        slug_to_col[name.upper().replace(" ", "_")] = name
        slug_to_col[name.lower().replace(" ", "_")] = name

    return slug_to_col


# =============================================================================
# CHAIN SECTION DETECTION
# =============================================================================

_CHAIN_HEADER_RE = re.compile(
    "|".join(CHAIN_HEADER_PATTERNS),
    re.IGNORECASE,
)

# Headers that are NOT chains despite looking similar
_FALSE_POSITIVE_HEADERS = re.compile(
    r"""
    Governor(?:'s)?\s+(?:Establishment|Office|Staff|and\s+Staff)\b  |
    Governor-General\s+(?:and\s+Staff|Conference|and\s+Commander)\b |
    Governors?['']s\s+Executive\s+Council\b                         |
    East\s+African\s+Governors['']?\s+Conference\b                  |
    Board\s+of\s+Sanitary\s+Commissioners\b                         |
    Commissioner\s+of\s+(?:Police|Lands|Works)\b                    |
    Deputy\s+Commissioner\s+of\b                                     |
    Native\s+Commissioners?\b                                        |
    District\s+Commissioners?\b                                      |
    Assistant\s+Commissioner\b                                       |
    Resident\s+Commissioner's\s+Department\b                        |
    Administrator\s+General\b                                        |
    Administrator's\s+Department\b                                   |
    Administrator\s+of\s+(?:the\s+Govt|the\s+Government)\b         |
    First\s+Magistrate\s+and\s+Commissioner\b                       |
    Administrators,\s+Dominion\b                                     |
    The\s+Governor\b                                                  |
    THE\s+GOVERNOR\b                                                  |
    Governor[-\s]General\s+and\s+Commander\b                        |
    Governor\s+and\s+Commander-in-Chief\s+of\b                      |
    Governors?\s+of\s+(?:Gaols?|Prisons?|Schools?|the\s+Newfoundland\s+Savings)\b |
    Governors?\s+Pension\b                                           |
    Governors?'\s+Pension\b
    """,
    re.VERBOSE | re.IGNORECASE,
)


def is_chain_header(line: str) -> bool:
    """Return True if this line (markdown or plain-text) introduces a historical
    governor chain section.

    Handles:
    - Markdown headers: '## Governors', '### Administrators since 1880', etc.
    - Plain-text headers: 'Governors since 1855.*', 'GOVERNORS.', etc.
    """
    stripped = line.strip()
    if not stripped:
        return False
    # Extract the meaningful text (strip leading '#' markers for markdown)
    if stripped.startswith("#"):
        header_text = re.sub(r"^#+\s*", "", stripped)
    else:
        header_text = stripped
    # Check against false-positives first
    if _FALSE_POSITIVE_HEADERS.search(header_text):
        return False
    return bool(_CHAIN_HEADER_RE.match(stripped))


# =============================================================================
# LINE PARSING
# =============================================================================

def _strip_table_row(line: str) -> str:
    """Convert '| 1831 | Name |' to '1831 Name'."""
    if "|" in line:
        # Extract cell contents, skip empty cells and header separators
        cells = [c.strip() for c in line.split("|")]
        cells = [c for c in cells if c and not re.match(r"^[-:]+$", c)]
        if len(cells) >= 2:
            # First cell should be the year, rest is the name
            year_cell = cells[0]
            name_parts = cells[1:]
            # Some tables have a third "Title" column, join them
            name_cell = " ".join(name_parts).strip()
            return f"{year_cell} {name_cell}"
        elif len(cells) == 1:
            return cells[0]
    return line


def _strip_list_marker(line: str) -> str:
    """Remove leading '- ' or '* ' from list items."""
    return re.sub(r"^\s*[-*]\s+", "", line)


def _clean_honours(name: str) -> str:
    """
    Iteratively strip post-nominal honours like K.C.M.G., G.C.B., D.S.O., etc.
    from the end of a name string.
    """
    # Remove parenthetical notes like "(afterwards Sir X, G.C.M.G.)"
    name = re.sub(r"\s*\([^)]*\)", "", name)
    # Remove trailing role qualifiers
    name = ROLE_SUFFIXES.sub("", name)
    # Remove trailing honours clusters: ", K.C.M.G., G.C.B., C.I.E."
    # Pattern: comma followed by abbreviated honours
    honour_block = re.compile(
        r"""
        ,\s*
        (?:
            [A-Z]{1,2}\.(?:[A-Z]{1,2}\.){0,5}  # dotted abbrev
            |[A-Z]{2,6}                          # solid abbrev
            |Bart\.?|Esq\.?|LL\.D\.?|K\.C\.|P\.C\.|V\.D\.|Q\.C\.
        )
        (?:
            (?:,?\s*
                (?:[A-Z]{1,2}\.(?:[A-Z]{1,2}\.){0,5}|[A-Z]{2,6}|Bart\.?|Esq\.?|LL\.D\.?|K\.C\.|P\.C\.|V\.D\.)
            )*
        )
        \s*\.?\s*$
        """,
        re.VERBOSE,
    )
    prev = None
    while prev != name:
        prev = name
        name = honour_block.sub("", name).strip()
    return name.strip(" ,.")


def extract_surname(raw_name: str) -> str:
    """
    Extract a clean surname from a raw governor name string.

    E.g.:
    'Sir Thomas Modyford'         → 'Modyford'
    'Lord Windsor'                 → 'Windsor'
    'Earl of Carlisle'             → 'Carlisle'
    'Duke of Manchester'           → 'Manchester'
    'G. D'Oyley'                   → "D'Oyley"
    'Major-Gen. Dalling'           → 'Dalling'
    'Sir H. E. H. Jerningham'      → 'Jerningham'
    'A Triumvirate: Sale, Paynter' → skip
    'M. de Nyon'                   → 'Nyon'
    """
    name = _clean_honours(raw_name).strip()

    # Strip trailing period
    name = name.rstrip(".")

    # Skip obvious non-person entries or descriptive text
    if re.search(
        r"Triumvirate|Interregnum|Vacancy|Unknown|[Ss]everal|Council\s+of"
        r"|will\s+be\s+found|Edition\s+for"
        r"|annually|elected\s+|Magistrate|previous\s+to|to\s+\d{4}\s+by"
        r"|\bper\s+cent\b|\bpounds?\b|\bsterling\b",
        name, re.IGNORECASE
    ):
        return ""

    # Strip leading title/rank prefixes
    name_no_title = TITLE_PREFIXES.sub("", name).strip()

    if not name_no_title:
        # Might be a title-only name like "Earl of Carlisle"
        # Extract the place/family name after "of"
        m = re.search(r"\bof\s+([A-Z][A-Za-z'-]+)", name)
        if m:
            return m.group(1)
        # Or just return the last word of the original
        words = name.split()
        return words[-1].strip(".,") if words else ""

    # Now extract surname from the remaining string
    # Initials pattern: "H. E. H. Jerningham" → "Jerningham"
    # Full name pattern: "Thomas Modyford" → "Modyford"
    # Single name: "Jerningham" → "Jerningham"
    # Compound: "D'Urban", "de Nyon", "de la Brillianne"

    # Remove leading initials like "G. " or "H. E. H. "
    no_initials = re.sub(r"^(?:[A-Z]\.(?:\s+[A-Z]\.)*\s+)", "", name_no_title).strip()
    if not no_initials:
        no_initials = name_no_title

    # If there's "de/du/von/van" compound, keep from there
    m = re.search(r"\b((?:de\s+la\s+|de\s+|du\s+|von\s+|van\s+)?[A-Z][A-Za-z'-]+)\s*$", no_initials)
    if m:
        return m.group(1)

    # Fall back: last word
    words = no_initials.split()
    if words:
        return words[-1].strip(".,")

    return ""


def parse_chain_line(line: str, in_table: bool = False) -> tuple[int | None, str, str]:
    """
    Parse a single line from a governor chain section.

    Returns (year, raw_name, surname) or (None, "", "") if not a valid entry.
    """
    original = line

    # Clean up the line
    if in_table or "|" in line:
        line = _strip_table_row(line)
    line = _strip_list_marker(line)
    line = line.strip()

    if not line:
        return None, "", ""

    # Skip section dividers, headers, and non-chain content
    if line.startswith("#") or re.match(r"^[-*]{3,}\s*$", line):
        return None, "", ""

    # Skip lines that are purely footnotes or metadata
    if re.match(r"^\*\s", line) or re.match(r"^[†‡§¶]", line):
        return None, "", ""

    # Must contain a year
    year_match = YEAR_PATTERN.search(line)
    if not year_match:
        return None, "", ""

    year = int(year_match.group(1))

    # Sanity check: COL covers 1660–1966
    if year < 1600 or year > 1970:
        return None, "", ""

    # Extract the name: everything after the year (and its bold markers / dot)
    year_end = year_match.end()
    raw_after = line[year_end:].strip()

    # Remove leading separators that may remain: ".", ",", "-", "|"
    raw_after = re.sub(r"^[.,\-|]\s*", "", raw_after).strip()

    if not raw_after:
        # Check if this is a "Name .. Year" reverse format (Bahamas early editions)
        # e.g. "- Halkett, John .. Governor .. 1801"
        #      "Sir C. C. Lees, K.C.M.G. .... 1882"
        # In this case, the year is at the END, name at the beginning
        raw_before = line[:year_match.start()].strip()
        raw_before = _strip_list_marker(raw_before)
        # Strip trailing " .... " separators
        raw_before = re.sub(r"\s*\.{2,}\s*$", "", raw_before).strip()
        # Strip trailing role title (e.g. ".. Governor", '.. "')
        raw_before = re.sub(r"\s*\.\.\s+(?:Governor|Lieutenant-Governor|Lieut\.-Governor|"
                            r"Acting Governor|Administrator|Lieut\.?\s+Gov\.|"
                            r"Commander|Captain-General|High Commissioner|"
                            r'["\'])\s*$', "", raw_before, flags=re.IGNORECASE)
        # Strip trailing honours (e.g. ", K.C.M.G., C.B.")
        # These appear between name and ".... year" in this format
        raw_before = _clean_honours(raw_before)
        raw_before = raw_before.strip(" .,-")
        # Handle "Surname, Given" format → convert to "Given Surname"
        if re.match(r"^[A-Z][a-zA-Z'-]+,\s*[A-Z]", raw_before):
            parts = raw_before.split(",", 1)
            raw_name = f"{parts[1].strip()} {parts[0].strip()}"
        else:
            raw_name = raw_before
        if not raw_name or len(raw_name) < 3:
            return None, "", ""
    else:
        raw_name = raw_after

    # The name ends at the first occurrence of a multi-honour block,
    # or a period that clearly ends the entry (not part of an abbreviation)
    # We'll clean honours from the full raw name

    surname = extract_surname(raw_name)

    if not surname or len(surname) < 2:
        return None, "", ""

    return year, raw_name, surname


# =============================================================================
# SECTION PARSING
# =============================================================================

def _colony_hint_from_header(header: str) -> str | None:
    """
    Try to extract a colony / state name from a plain-text governor chain header.

    Examples:
      "Governors of Queensland.*"          → "Queensland"
      "Governors of Tasmania since 1881.*" → "Tasmania"
      "Governors since 1855.*"             → None  (no colony name embedded)
      "Governors-General of the Commonwealth." → "Commonwealth of Australia"
      "Lieutenant-Governors since Confederation." → None
      "List of Governors of South Australia." → "South Australia"

    Returns a raw string that the caller can look up in slug_to_col, or None.
    """
    # Strip trailing footnote markers and punctuation
    h = re.sub(r"\s*[.*†§‡¶:]+\s*$", "", header).strip()

    # "Governors of <Name>" / "List of Governors of <Name>"
    m = re.search(r"(?:Governors?|Administrators?)\s+of\s+([A-Z][A-Za-z\s'()&-]+?)(?:\s+since\s+\d{4}|\s+from\s+\d{4}|\s*$)", h)
    if m:
        cname = m.group(1).strip()
        # Skip generic phrases
        if re.search(r"^the\s+(Colony|Province|Island|Settlement|Federation|Commonwealth)\b", cname, re.I):
            return None
        return cname

    # "Governors-General of the Commonwealth"
    m = re.search(r"Governors?-General\s+of\s+the\s+(Commonwealth\s+of\s+Australia|Commonwealth)", h, re.I)
    if m:
        return "Commonwealth of Australia"

    # "Governors and Administrators of Lagos"
    m = re.search(r"Governors?\s+and\s+Administrators?\s+of\s+([A-Z][A-Za-z\s'&-]+?)(?:\s+since|\s+from|\s*$)", h)
    if m:
        return m.group(1).strip()

    return None


def extract_chains_from_file(filepath: Path) -> list[dict]:
    """
    Extract all governor chain sections from a single .txt or .md file.

    Returns a list of chain dicts:
    {
        "header": "## Governors",
        "colony_hint": "Queensland",   # optional, extracted from plain-text header
        "entries": [{"year": 1660, "raw_name": "G. D'Oyley", "surname": "D'Oyley"}, ...]
    }
    """
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  WARNING: Could not read {filepath}: {e}")
        return []

    lines = text.splitlines()
    chains = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        if is_chain_header(line):
            header = line.strip()
            is_plaintext_header = not header.startswith("#")
            colony_hint = _colony_hint_from_header(header) if is_plaintext_header else None
            entries = []
            in_table = False
            i += 1

            # Consume lines until we hit a new section header or run dry.
            # For plain-text headers we need stricter termination because there
            # is no structural '#' marker to rely on.
            #
            # Heuristic for plain-text sections:
            #   - Stop after N consecutive non-entry lines (paragraph text)
            #   - Stop when another chain header is encountered
            consecutive_non_entry = 0
            MAX_NON_ENTRY = 6  # allow a few blank/footnote lines between entries

            while i < n:
                cur = lines[i]

                # A markdown section header always ends any chain section
                if re.match(r"^#{1,4}\s+\S", cur) and cur.strip() != header:
                    break

                # Another plain-text chain header ends the current section
                if is_plaintext_header and is_chain_header(cur) and cur.strip() != header:
                    break

                # ALL CAPS paragraph headers (e.g. "PRIVY COUNCIL", "EXECUTIVE COUNCIL")
                # indicate end of chain section.  But be careful: "GOVERNORS." is a
                # valid chain header (handled above).
                if (
                    re.match(r"^[A-Z][A-Z\s]{4,}$", cur.strip())
                    and not re.search(r"\d", cur)
                    and not is_chain_header(cur)
                ):
                    break

                # Known Title-Case section dividers that follow governor lists
                # (e.g. "Former Ministries.", "Ministries.", "Ministers.",
                #  "Note.", "Staff.", "Legislature.", "Executive Council.", etc.)
                if re.match(
                    r"^(?:Former\s+)?(?:Ministr(?:y|ies)|Ministers?|Staff|Legislature"
                    r"|Executive\s+Council|Legislative\s+Council|House\s+of|Parliament"
                    r"|Note|Note\.|Land\s+Revenue|Revenue|Public\s+Debt|Railways?)\b",
                    cur.strip(), re.IGNORECASE
                ) and re.match(r"^[A-Z]", cur.strip()) and len(cur.strip()) < 80:
                    # Only act as terminator if this line doesn't also contain a year
                    # (to avoid cutting off chains that have "Note — since 1880" type lines)
                    if not re.search(r"\b\d{4}\b", cur):
                        break

                # A horizontal rule often follows the chain section
                if re.match(r"^-{3,}\s*$", cur.strip()):
                    break

                # Detect table mode
                if re.match(r"^\s*\|", cur):
                    in_table = True
                    # Skip table header separator rows like |---|---|
                    if re.match(r"^\s*\|[-:|]+\|", cur):
                        i += 1
                        continue
                elif in_table and not cur.strip():
                    # Blank line after table ends table mode
                    in_table = False

                year, raw_name, surname = parse_chain_line(cur, in_table=in_table)
                if year is not None and raw_name:
                    entries.append({
                        "year": year,
                        "raw_name": raw_name.strip(" .,"),
                        "surname": surname,
                    })
                    consecutive_non_entry = 0
                else:
                    # For plain-text sections, bail out if we're deep into
                    # non-entry prose (prevents bleeding into body text).
                    # Don't count blank lines or short lines (footnotes).
                    if is_plaintext_header and cur.strip() and len(cur.strip()) > 20:
                        consecutive_non_entry += 1
                        if consecutive_non_entry >= MAX_NON_ENTRY and entries:
                            break

                i += 1

            if len(entries) >= 2:
                chains.append({
                    "header": header,
                    "colony_hint": colony_hint,
                    "entries": entries,
                })
            # Don't increment i again – we already moved past this block
        else:
            i += 1

    return chains


def pick_best_chain(chains_list: list[dict]) -> dict | None:
    """
    From multiple chain sections in a file (e.g. "French Governors" + "Governors for
    Great Britain"), pick the one that is most likely the primary/complete governor chain.

    Preference order:
    1. Chain with most entries
    2. Chain with latest final year
    """
    if not chains_list:
        return None

    # Score: length + recency of last entry
    def score(chain):
        entries = chain["entries"]
        n = len(entries)
        last_year = max(e["year"] for e in entries) if entries else 0
        return n * 10 + (last_year - 1600)

    return max(chains_list, key=score)


def merge_chains(chains_list: list[dict]) -> list[dict]:
    """
    Merge multiple chain sections from the same file into one combined chain,
    sorted by year. This handles colonies like Mauritius that have "French
    Governors (1722-1810)" + "Governors for Great Britain".
    """
    all_entries = []
    seen = set()
    for chain in chains_list:
        for e in chain["entries"]:
            key = (e["year"], e["surname"].lower())
            if key not in seen:
                seen.add(key)
                all_entries.append(e)
    all_entries.sort(key=lambda e: e["year"])
    return all_entries


# =============================================================================
# CORPUS SCANNER
# =============================================================================

def _resolve_col_name(stem: str, slug_to_col: dict) -> str | None:
    """Map a file stem (possibly ALL-CAPS, mixed-case, or hyphenated) to a COL colony name."""
    return (
        slug_to_col.get(stem)
        or slug_to_col.get(stem.lower())
        or slug_to_col.get(stem.lower().replace("-", "_"))
        or slug_to_col.get(stem.upper())
        or slug_to_col.get(re.sub(r"[^a-z0-9]+", "_", stem.lower()).strip("_"))
    )


def scan_corpus(base_dir: Path, slug_to_col: dict, verbose: bool = False) -> dict:
    """
    Scan all *_manual_parsed/*.txt and *.md files and extract governor chains.

    For each colony, keep the most complete chain across all editions.

    Special handling for files like AUSTRALIA.txt that embed sub-chains for
    individual states (Queensland, Tasmania, etc.) — each sub-chain is mapped
    to its own colony via the colony_hint extracted from the plain-text header.

    Returns {col_name: {source_file, edition_year, chain: [...]}}
    """
    # Gather all year directories
    year_dirs = sorted(
        [d for d in base_dir.iterdir() if d.is_dir() and re.match(r"\d{4}_manual_parsed$", d.name)],
        key=lambda d: int(d.name[:4]),
    )

    if not year_dirs:
        print(f"ERROR: No *_manual_parsed directories found in {base_dir}")
        return {}

    # colony → list of (edition_year, file_path, chain_entries)
    colony_candidates: dict[str, list] = defaultdict(list)
    unmatched_files: list[str] = []

    total_files = 0
    total_chains = 0

    for year_dir in year_dirs:
        edition_year = int(year_dir.name[:4])
        # Collect both .txt and .md files (excluding Zone.Identifier artefacts)
        all_files = [
            f for ext in ("*.txt", "*.md")
            for f in year_dir.glob(ext)
            if not f.name.endswith("Zone.Identifier")
        ]

        for txt_path in sorted(all_files):
            total_files += 1
            stem = txt_path.stem  # e.g. "sierra_leone", "JAMAICA", "AUSTRALIA"

            # Map filename to COL colony name
            col_name = _resolve_col_name(stem, slug_to_col)

            if col_name is None:
                unmatched_files.append(f"{edition_year}/{stem}")
                continue

            # Extract chains from this file
            chains = extract_chains_from_file(txt_path)
            if not chains:
                continue

            # ----------------------------------------------------------------
            # Separate chains into:
            #   (a) Sub-colony chains — have a colony_hint pointing to a
            #       DIFFERENT colony than the file's own col_name (e.g. the
            #       "Governors of Queensland" chain inside AUSTRALIA.txt).
            #   (b) Own-colony chains — belong to the file's colony.
            # ----------------------------------------------------------------
            sub_colony_chains: dict[str, list] = defaultdict(list)
            own_chains = []

            for ch in chains:
                hint = ch.get("colony_hint")
                if hint:
                    # Try to resolve the hint to a canonical COL name
                    hint_slug = re.sub(r"[^a-z0-9]+", "_", hint.lower()).strip("_")
                    resolved = (
                        slug_to_col.get(hint)
                        or slug_to_col.get(hint_slug)
                        or slug_to_col.get(hint.lower())
                    )
                    if resolved and resolved != col_name:
                        sub_colony_chains[resolved].append(ch)
                        continue
                own_chains.append(ch)

            # Record sub-colony chains separately
            for sub_col, sub_chains in sub_colony_chains.items():
                merged = merge_chains(sub_chains)
                if merged:
                    total_chains += 1
                    colony_candidates[sub_col].append(
                        (edition_year, txt_path, merged, sub_chains)
                    )

            # Merge all own-colony chains and record
            merged_entries = merge_chains(own_chains)
            if merged_entries:
                total_chains += 1
                colony_candidates[col_name].append(
                    (edition_year, txt_path, merged_entries, own_chains)
                )

    if verbose:
        print(f"  Scanned {total_files} files across {len(year_dirs)} editions")
        print(f"  Found chain sections in {total_chains} file-colony combinations")
        if unmatched_files:
            print(f"  Unmatched filenames ({len(unmatched_files)}): {unmatched_files[:10]}")

    # For each colony, select the best candidate
    # Strategy: use the edition with the MOST entries (most complete chain)
    # Tie-break: latest edition year (more up-to-date)
    result = {}
    for col_name, candidates in colony_candidates.items():
        best = max(candidates, key=lambda c: (len(c[2]), c[0]))
        edition_year, txt_path, entries, all_chains = best
        result[col_name] = {
            "source_file": str(txt_path.relative_to(base_dir)),
            "edition_year": edition_year,
            "num_editions_with_chain": len(candidates),
            "chain": entries,
        }

    return result


# =============================================================================
# SURNAME NORMALISATION
# =============================================================================

# Common OCR/historical variants
SURNAME_NORMALISATION = {
    "d'oyley": "d'oyley",  # keep apostrophe variants
    "d'urban": "d'urban",
}


def _normalise_mac(s: str) -> str:
    """Collapse Mac/Mc/M' prefixes to a single form for comparison.

    M'Gregor, McGregor, MacGregor → macgregor
    """
    return re.sub(r"^m[ac']{1,2}", "mac", s, flags=re.IGNORECASE)


def normalise_surname(s: str) -> str:
    """Normalise a surname for fuzzy matching."""
    s = s.lower().strip(" .,")
    s = SURNAME_NORMALISATION.get(s, s)
    # Collapse Mac/Mc/M' variants
    s = _normalise_mac(s)
    # Remove hyphens for matching (e.g. "Goold-Adams" matches "Goold Adams")
    return s


def is_junk_surname(surname: str) -> bool:
    """Return True if surname is junk (currency amounts, OCR noise, etc.)."""
    s = surname.strip()
    if len(s) < 2:
        return True
    # Currency amounts like "$274", "1906", "94"
    if re.match(r"^\$?\d", s):
        return True
    # Pure numbers
    if re.match(r"^\d+[-/]?\d*$", s):
        return True
    # Common OCR noise words
    if s.lower() in {"of", "the", "and", "for", "see", "also", "no", "vol", "act"}:
        return True
    return False


# =============================================================================
# NEO4J GHOST DETECTION
# =============================================================================

def _is_governor_position(pos: str) -> bool:
    """Check if a position_raw string is governor-class."""
    if not pos:
        return False
    pos_lower = pos.lower()
    return any(kw in pos_lower for kw in GOVERNOR_POSITION_KEYWORDS)


def detect_ghosts_from_parsed_chains(
    driver,
    governor_chains: dict,
    dry_run: bool = True,
    verbose: bool = True,
) -> dict:
    """
    For each colony in governor_chains, find PersonRecords in Neo4j that match
    historical governors (i.e. those who appear in the chain but are NOT the
    last/current entry for their edition year).

    Logic:
    - Load all governor-class PersonRecords for each colony.
    - For each PersonRecord, check if its surname matches any historical chain
      entry (year < edition_year) where there is a LATER chain entry.
    - A chain entry is "historical" if it is not the last entry in the chain for
      a given edition (i.e. the edition year >= a subsequent entry's year).

    Returns {
        "ghosts": [...PersonRecord URIs...],
        "details": [{uri, colony, year, surname, position_raw, chain_year, chain_name}, ...],
        "stats": {...}
    }
    """
    ghosts_uris = []
    details = []
    per_colony_counts = defaultdict(int)

    with driver.session() as session:
        for col_name, chain_data in governor_chains.items():
            chain = chain_data["chain"]
            if not chain:
                continue

            edition_year = chain_data["edition_year"]

            # Build lookup: surname → list of chain years
            # An entry is "historical" if there exists a later entry
            chain_by_surname: dict[str, list[dict]] = defaultdict(list)
            for entry in chain:
                if not isinstance(entry.get("year"), int) or entry["year"] < 1500:
                    continue
                sn = normalise_surname(entry["surname"])
                if is_junk_surname(sn):
                    continue
                chain_by_surname[sn].append(entry)
            # Pre-compute the set of all normalised chain surnames for fuzzy fallback
            all_chain_surnames = set(chain_by_surname.keys())

            # Determine which entries are "historical" for each edition year
            # A chain entry at year Y is historical if there's another entry at year Y' > Y
            # and the edition year >= Y' (i.e. that later person was already in post)
            all_chain_years = sorted(set(e["year"] for e in chain))

            def is_historical_entry(entry_year: int, record_edition_year: int) -> bool:
                """
                An entry is historical if there's a later entry in the chain
                that had already started (entry_year' <= record_edition_year).
                In other words: is this person's tenure clearly over by the
                record's edition year?
                """
                later_entries = [y for y in all_chain_years if y > entry_year]
                if not later_entries:
                    # This is the last/only entry — not historical
                    return False
                # If the next successor started on or before the edition year,
                # this person's tenure is over
                next_entry_year = min(later_entries)
                return next_entry_year <= record_edition_year

            # Query Neo4j for all governor-class PersonRecords in this colony
            query = """
            MATCH (pr:COL_PersonRecord {colony: $colony})
            WHERE pr.position_raw IS NOT NULL
              AND toLower(pr.position_raw) =~ $gov_pattern
            RETURN pr.uri AS uri,
                   pr.surname AS surname,
                   pr.given_names AS given_names,
                   pr.canonical_name AS canonical_name,
                   pr.year AS year,
                   pr.position_raw AS position_raw,
                   COALESCE(pr.quarantined, false) AS quarantined
            ORDER BY pr.year, pr.surname
            """

            # Build a regex that matches any governor keyword
            gov_pattern = ".*(" + "|".join(re.escape(kw) for kw in GOVERNOR_POSITION_KEYWORDS) + ").*"

            try:
                records = session.run(
                    query,
                    colony=col_name,
                    gov_pattern=gov_pattern,
                ).data()
            except Exception as e:
                if verbose:
                    print(f"  WARNING: Query failed for {col_name}: {e}")
                continue

            for rec in records:
                pr_surname = normalise_surname(rec.get("surname") or "")
                pr_year = rec.get("year")  # edition year of the PersonRecord
                pr_uri = rec.get("uri")
                already_quarantined = rec.get("quarantined", False)

                if not pr_surname or not pr_year or already_quarantined:
                    continue

                if is_junk_surname(pr_surname):
                    continue

                # Check if this surname matches any historical chain entry
                matched_entries = chain_by_surname.get(pr_surname, [])

                # Levenshtein fallback: if no exact match, check edit distance ≤ 1
                if not matched_entries and len(pr_surname) >= 4:
                    for chain_sn in all_chain_surnames:
                        if abs(len(chain_sn) - len(pr_surname)) > 1:
                            continue
                        # SequenceMatcher ratio > threshold ≈ edit distance ≤ 1
                        # For strings of length ~7, ratio > 0.8 ≈ 1 edit
                        ratio = SequenceMatcher(None, pr_surname, chain_sn).ratio()
                        min_len = min(len(pr_surname), len(chain_sn))
                        threshold = 1 - (1.0 / min_len) if min_len > 2 else 0.6
                        if ratio >= threshold:
                            matched_entries = chain_by_surname[chain_sn]
                            break

                if not matched_entries:
                    continue

                # IMPORTANT: If any chain entry with this surname is CURRENT
                # (not historical) for this PersonRecord's edition year, the
                # PersonRecord is the current governor and should NOT be flagged.
                # This prevents false positives when two different people share
                # the same surname (e.g. Edward Hay 1772 vs James Shaw Hay 1891).
                has_current_match = any(
                    not is_historical_entry(e["year"], pr_year)
                    for e in matched_entries
                )
                if has_current_match:
                    continue

                # All matches are historical — flag as ghost
                # Pick the best chain match: the one closest to the PersonRecord year
                best_match = min(
                    [e for e in matched_entries if is_historical_entry(e["year"], pr_year)],
                    key=lambda e: abs(e["year"] - pr_year),
                    default=None,
                )
                if best_match is None:
                    continue

                chain_year = best_match["year"]
                ghosts_uris.append(pr_uri)
                details.append({
                    "uri": pr_uri,
                    "colony": col_name,
                    "edition_year": pr_year,
                    "surname": rec.get("canonical_name") or pr_surname,
                    "position_raw": rec.get("position_raw"),
                    "chain_year": chain_year,
                    "chain_name": best_match["raw_name"],
                    "chain_source": chain_data["source_file"],
                })
                per_colony_counts[col_name] += 1

    # Deduplicate
    seen_uris = set()
    unique_details = []
    for d in details:
        if d["uri"] not in seen_uris:
            seen_uris.add(d["uri"])
            unique_details.append(d)

    stats = {
        "total_ghost_candidates": len(unique_details),
        "colonies_with_ghosts": len(per_colony_counts),
        "per_colony": dict(sorted(per_colony_counts.items(), key=lambda x: -x[1])),
    }

    return {
        "ghosts": list(seen_uris),
        "details": unique_details,
        "stats": stats,
    }


def quarantine_ghosts(driver, ghost_uris: list[str], dry_run: bool = True) -> int:
    """
    Set `quarantined = true` on PersonRecord nodes for the given URIs.

    Returns the number of nodes updated.
    """
    if dry_run or not ghost_uris:
        return 0

    updated = 0
    batch_size = 500
    with driver.session() as session:
        for i in range(0, len(ghost_uris), batch_size):
            batch = ghost_uris[i : i + batch_size]
            result = session.run(
                """
                UNWIND $uris AS uri
                MATCH (pr:COL_PersonRecord {uri: uri})
                SET pr.quarantined = true,
                    pr.quarantine_reason = 'governor_chain_ghost',
                    pr.quarantine_date = date()
                RETURN count(pr) AS n
                """,
                uris=batch,
            )
            updated += result.single()["n"]
    return updated


def get_quarantine_stats(driver) -> dict:
    """Get current quarantine statistics from Neo4j."""
    with driver.session() as session:
        total = session.run("MATCH (pr:COL_PersonRecord) RETURN count(pr) AS n").single()["n"]
        quarantined = session.run(
            "MATCH (pr:COL_PersonRecord {quarantined: true}) RETURN count(pr) AS n"
        ).single()["n"]
        chain_quarantined = session.run(
            """
            MATCH (pr:COL_PersonRecord {quarantined: true, quarantine_reason: 'governor_chain_ghost'})
            RETURN count(pr) AS n
            """
        ).single()["n"]

    return {
        "total_person_records": total,
        "total_quarantined": quarantined,
        "chain_ghost_quarantined": chain_quarantined,
    }


# =============================================================================
# REPORT GENERATION
# =============================================================================

def write_report(
    governor_chains: dict,
    detection_results: dict | None,
    output_path: Path,
) -> None:
    """Write a markdown report of parsing results and ghost detection."""
    today = date.today().isoformat()
    lines = [
        f"# Governor Chain Ghost Detection Report",
        f"",
        f"Generated: {today}",
        f"",
        f"## Summary",
        f"",
    ]

    # Parsing stats
    total_colonies = len(governor_chains)
    total_entries = sum(len(d["chain"]) for d in governor_chains.values())
    lines += [
        f"### Parsing Results",
        f"",
        f"- **Colonies with parsed chains**: {total_colonies}",
        f"- **Total governor entries**: {total_entries}",
        f"- **Output file**: `governor_chains_parsed.json`",
        f"",
    ]

    # Detection stats
    if detection_results:
        stats = detection_results["stats"]
        lines += [
            f"### Ghost Detection Results",
            f"",
            f"- **Ghost candidates identified**: {stats['total_ghost_candidates']}",
            f"- **Colonies with ghosts**: {stats['colonies_with_ghosts']}",
            f"",
            f"#### Top colonies by ghost count",
            f"",
            f"| Colony | Ghost Count |",
            f"|--------|-------------|",
        ]
        for colony, count in list(stats["per_colony"].items())[:20]:
            lines.append(f"| {colony} | {count} |")
        lines.append("")

        # Per-colony details
        lines += [
            f"## Detailed Ghost Candidates",
            f"",
        ]
        by_colony: dict[str, list] = defaultdict(list)
        for d in detection_results["details"]:
            by_colony[d["colony"]].append(d)

        for colony in sorted(by_colony.keys()):
            ghost_list = sorted(by_colony[colony], key=lambda x: x["edition_year"])
            chain_info = governor_chains.get(colony, {})
            lines += [
                f"### {colony} ({len(ghost_list)} ghosts)",
                f"",
                f"Chain source: `{chain_info.get('source_file', 'unknown')}`  ",
                f"Chain length: {len(chain_info.get('chain', []))} entries",
                f"",
                f"| Edition Year | Surname | Position | Chain Year | Chain Name |",
                f"|--------------|---------|----------|------------|------------|",
            ]
            for g in ghost_list:
                pos = (g["position_raw"] or "")[:50]
                cname = g["chain_name"][:40]
                lines.append(
                    f"| {g['edition_year']} | {g['surname']} | {pos} | {g['chain_year']} | {cname} |"
                )
            lines.append("")

    # Colony chain summary
    lines += [
        f"## Parsed Chains by Colony",
        f"",
        f"| Colony | Source File | Entries | First Year | Last Year |",
        f"|--------|------------|---------|------------|-----------|",
    ]
    for col_name in sorted(governor_chains.keys()):
        data = governor_chains[col_name]
        chain = data["chain"]
        if chain:
            first_year = chain[0]["year"]
            last_year = chain[-1]["year"]
        else:
            first_year = last_year = "—"
        lines.append(
            f"| {col_name} | `{data['source_file']}` | {len(chain)} | {first_year} | {last_year} |"
        )
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written to: {output_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Parse governor chains from COL text files and detect ghost PersonRecords."
    )
    parser.add_argument(
        "--detect",
        action="store_true",
        help="Query Neo4j to find ghost PersonRecords matching parsed chains.",
    )
    parser.add_argument(
        "--quarantine",
        action="store_true",
        help="Mark detected ghosts as quarantined in Neo4j (requires --detect).",
    )
    parser.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        default=True,
        help="Detect and report without writing to Neo4j (default).",
    )
    parser.add_argument(
        "--no-dry-run",
        dest="dry_run",
        action="store_false",
        help="Disable dry-run mode.",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Write a markdown report to GOVERNOR_CHAIN_GHOST_REPORT.md.",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show current quarantine statistics from Neo4j and exit.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_JSON,
        help=f"Output JSON file path (default: {OUTPUT_JSON})",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print verbose progress information.",
    )
    parser.add_argument(
        "--test-colony",
        metavar="COLONY",
        help="Test-parse a specific colony file and show results (e.g. 'Jamaica').",
    )
    parser.add_argument(
        "--no-parse",
        dest="no_parse",
        action="store_true",
        help="Skip re-parsing; load existing governor_chains_parsed.json for detection.",
    )

    args = parser.parse_args()

    # --stats shortcut
    if args.stats:
        if not NEO4J_PASSWORD:
            print("ERROR: NEO4J_PASSWORD not set. Check .env file.")
            sys.exit(1)
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        stats = get_quarantine_stats(driver)
        driver.close()
        print("\nQuarantine Statistics:")
        for k, v in stats.items():
            print(f"  {k}: {v:,}")
        return

    # --test-colony: show parsed chain for a single colony
    if args.test_colony:
        slug_to_col = build_filename_to_colony_map()
        target = args.test_colony
        print(f"\nSearching for governor chain for colony: {target}")
        found = False
        for year_dir in sorted(
            [d for d in REPO_DIR.iterdir() if d.is_dir() and re.match(r"\d{4}_manual_parsed$", d.name)],
            key=lambda d: int(d.name[:4]),
            reverse=True,
        ):
            # Scan both .txt and .md files
            all_files = [
                f for ext in ("*.txt", "*.md")
                for f in year_dir.glob(ext)
                if not f.name.endswith("Zone.Identifier")
            ]
            for txt_path in sorted(all_files):
                col_name = _resolve_col_name(txt_path.stem, slug_to_col)
                if col_name and col_name.lower() == target.lower():
                    chains = extract_chains_from_file(txt_path)
                    if chains:
                        print(f"\nFile: {txt_path.relative_to(REPO_DIR)}")
                        merged = merge_chains(chains)
                        print(f"Merged chain ({len(merged)} entries):")
                        for e in merged:
                            print(f"  {e['year']:4d}  {e['raw_name'][:60]!s:60s}  → surname: {e['surname']}")
                        found = True
                        break
            if found:
                break
        if not found:
            print(f"  No chain found for '{target}'")
        return

    # =========================================================================
    # PHASE 1: PARSE GOVERNOR CHAINS (or load existing)
    # =========================================================================
    if args.no_parse:
        print("=" * 60)
        print("Phase 1: Loading existing governor chains (--no-parse)")
        print("=" * 60)
        if not args.output.exists():
            print(f"ERROR: {args.output} not found. Run without --no-parse first.")
            sys.exit(1)
        with open(args.output, "r", encoding="utf-8") as f:
            governor_chains = json.load(f)
        total_entries = sum(len(d['chain']) for d in governor_chains.values())
        print(f"  Loaded {len(governor_chains)} colonies, {total_entries} entries from {args.output}")
    else:
        print("=" * 60)
        print("Phase 1: Parsing governor chains from corpus")
        print("=" * 60)

        slug_to_col = build_filename_to_colony_map()
        print(f"  Colony name mappings loaded: {len(slug_to_col)} slugs")

        governor_chains = scan_corpus(REPO_DIR, slug_to_col, verbose=True)

        print(f"\nResults:")
        print(f"  Colonies with chains: {len(governor_chains)}")
        total_entries = sum(len(d['chain']) for d in governor_chains.values())
        print(f"  Total governor entries: {total_entries}")

        # Write JSON output
        output_data = {}
        for col_name in sorted(governor_chains.keys()):
            output_data[col_name] = governor_chains[col_name]

        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"\nChains written to: {args.output}")

        # Show sample
        if args.verbose:
            print("\nSample (Jamaica):")
            if "Jamaica" in governor_chains:
                jm = governor_chains["Jamaica"]
                print(f"  Source: {jm['source_file']}")
                for e in jm["chain"][:5]:
                    print(f"  {e['year']}  {e['raw_name']!s:50s} → {e['surname']}")
                print(f"  ... ({len(jm['chain'])} total entries)")

    # =========================================================================
    # PHASE 1b: MERGE AGENT-EXTRACTED CHAINS
    # =========================================================================
    agent_batch_files = sorted(REPO_DIR.glob("governor_chains_agent_batch*.json"))
    if agent_batch_files:
        print("\n" + "=" * 60)
        print("Phase 1b: Merging agent-extracted chains")
        print("=" * 60)
        for abf in agent_batch_files:
            print(f"  Loading {abf.name}...")
            with open(abf, "r", encoding="utf-8") as f:
                agent_data = json.load(f)

            merged_count = 0
            new_count = 0
            for key, adata in agent_data.items():
                colony = adata.get("colony", key.split(":")[0] if ":" in key else key)

                # Normalise agent entries: they use "name" not "raw_name"/"surname"
                agent_chain = []
                for entry in adata.get("chain", []):
                    year = entry.get("year")
                    if not year or not isinstance(year, int):
                        continue
                    raw_name = entry.get("name") or entry.get("raw_name", "")
                    surname = entry.get("surname") or extract_surname(raw_name)
                    if not surname or is_junk_surname(surname):
                        continue
                    agent_chain.append({
                        "year": year,
                        "raw_name": raw_name,
                        "surname": surname,
                    })

                if not agent_chain:
                    continue

                if colony in governor_chains:
                    # Merge: add new entries not already present
                    existing = governor_chains[colony]["chain"]
                    existing_keys = {
                        (e["year"], normalise_surname(e["surname"]))
                        for e in existing
                    }
                    added = 0
                    for ae in agent_chain:
                        akey = (ae["year"], normalise_surname(ae["surname"]))
                        if akey not in existing_keys:
                            existing.append(ae)
                            existing_keys.add(akey)
                            added += 1
                    if added:
                        existing.sort(key=lambda e: e["year"])
                        merged_count += 1
                else:
                    # New colony entry
                    governor_chains[colony] = {
                        "source_file": adata.get("source", abf.name),
                        "edition_year": max(e["year"] for e in agent_chain),
                        "num_editions_with_chain": 1,
                        "chain": agent_chain,
                    }
                    new_count += 1

            print(f"    Merged into {merged_count} existing colonies, added {new_count} new")

        # Re-write merged chains
        output_data = {}
        for col_name in sorted(governor_chains.keys()):
            output_data[col_name] = governor_chains[col_name]
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        total_entries = sum(len(d['chain']) for d in governor_chains.values())
        print(f"  Total after merge: {len(governor_chains)} colonies, {total_entries} entries")

    # =========================================================================
    # PHASE 2: GHOST DETECTION (optional)
    # =========================================================================
    detection_results = None

    if args.detect:
        if not NEO4J_PASSWORD:
            print("\nERROR: NEO4J_PASSWORD not set. Check .env file.")
            sys.exit(1)

        print("\n" + "=" * 60)
        print("Phase 2: Detecting ghost PersonRecords in Neo4j")
        print("=" * 60)
        print(f"  Connection: {NEO4J_URI}")
        print(f"  Dry-run: {args.dry_run}")

        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

        try:
            detection_results = detect_ghosts_from_parsed_chains(
                driver,
                governor_chains,
                dry_run=args.dry_run,
                verbose=args.verbose,
            )
        finally:
            if not args.quarantine:
                driver.close()

        stats = detection_results["stats"]
        print(f"\nDetection Results:")
        print(f"  Ghost candidates: {stats['total_ghost_candidates']}")
        print(f"  Colonies affected: {stats['colonies_with_ghosts']}")

        if stats["per_colony"]:
            print("\n  Top colonies:")
            for colony, count in list(stats["per_colony"].items())[:10]:
                print(f"    {colony}: {count}")

        # =====================================================================
        # PHASE 3: QUARANTINE (optional)
        # =====================================================================
        if args.quarantine and not args.dry_run:
            print("\n" + "=" * 60)
            print("Phase 3: Quarantining ghost PersonRecords")
            print("=" * 60)

            ghost_uris = detection_results["ghosts"]
            print(f"  Marking {len(ghost_uris)} nodes as quarantined...")
            updated = quarantine_ghosts(driver, ghost_uris, dry_run=False)
            print(f"  Updated: {updated} nodes")
            driver.close()

        elif args.quarantine and args.dry_run:
            print("\nNOTE: --quarantine specified but --dry-run is active.")
            print("      Use --quarantine --no-dry-run to actually quarantine.")

        if "driver" in locals():
            try:
                driver.close()
            except Exception:
                pass

    # =========================================================================
    # REPORT
    # =========================================================================
    if args.report:
        write_report(governor_chains, detection_results, REPORT_PATH)

    print("\nDone.")


if __name__ == "__main__":
    main()

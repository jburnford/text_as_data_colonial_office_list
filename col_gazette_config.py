#!/usr/bin/env python3
"""
London Gazette LOD Configuration
==================================

Colony name → Gazette search term mapping, SPARQL helpers, and rate limiting.

Maps COL colonies (from scaffold_neo4j.py EXPLICIT_ALIASES) and IOL places
to search terms for the Gazette's longitudinal dataset SPARQL endpoint.

Usage:
    from col_gazette_config import (
        GAZETTE_COL_TERMS, GAZETTE_IOL_TERMS,
        sparql_query, build_colony_search_query,
    )
"""

import re
import time
import urllib.parse
import urllib.request
import json
from collections import defaultdict

# Import colony aliases from scaffold
from scaffold_neo4j import EXPLICIT_ALIASES


# =============================================================================
# SPARQL ENDPOINT
# =============================================================================

SPARQL_ENDPOINT = "https://www.thegazette.co.uk/longitudinal-dataset/sparql"

# Rate limiting
_last_request_time = 0.0
MIN_REQUEST_INTERVAL = 5.0  # seconds between queries — be polite


# =============================================================================
# RDF PREDICATES (from endpoint exploration)
# =============================================================================

NS = "https://www.thegazette.co.uk/def/index#"
RDFS_LABEL = "http://www.w3.org/2000/01/rdf-schema#label"

PRED_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
PRED_ENTRY_TEXT = f"{NS}entryText"
PRED_SURNAME = f"{NS}hasSurname"
PRED_FORENAMES = f"{NS}hasForenames"
PRED_TITLE = f"{NS}title"
PRED_HONOUR = f"{NS}hasHonour"
PRED_PAGE_NO = f"{NS}pageNo"
PRED_GROUPING0 = f"{NS}grouping0"  # year/volume URI
PRED_SECTION = f"{NS}isInSection"
ITEM_TYPE = f"{NS}Item"


# =============================================================================
# COLONY → GAZETTE SEARCH TERMS
# =============================================================================

def _build_col_terms():
    """Invert EXPLICIT_ALIASES to build canonical colony → search terms map.

    Each canonical colony name maps to a list of lowercase search terms
    that might appear in Gazette entry text or titles.
    """
    # Invert: canonical name → set of raw alias strings
    canonical_to_aliases = defaultdict(set)

    # Filename suffixes that are artifacts, not real search terms
    # "ref" is a filename marker; "windward" without context is a file grouping
    _JUNK_SUFFIXES = {"ref"}
    # Compound prefixed terms where the real colony is the suffix part
    _JUNK_PREFIXES = {"west indies ", "leeward islands ",
                      "windward islands ", "malaya "}

    for raw, canonical in EXPLICIT_ALIASES.items():
        # Convert underscore-based raw names to space-separated search terms
        term = raw.replace("_", " ").replace("  ", " ").strip()

        # Skip very short terms
        if len(term) < 4:
            continue

        # Skip terms that are just the canonical with a junk suffix
        term_lower = term.lower()
        # Skip "antigua ref", "barbados windward" etc — these are filename artifacts
        skip = False
        for suffix in _JUNK_SUFFIXES:
            if term_lower.endswith(f" {suffix}") and term_lower != canonical.lower():
                skip = True
                break
        if skip:
            continue

        # Skip compound prefixed terms like "leeward islands  antigua"
        # — the canonical name alone is a better search term
        has_prefix = False
        for prefix in _JUNK_PREFIXES:
            if term_lower.startswith(prefix):
                has_prefix = True
                break
        if has_prefix:
            continue

        canonical_to_aliases[canonical].add(term_lower)

        # Also add the canonical name itself
        canonical_to_aliases[canonical].add(canonical.lower())

    # Convert to sorted lists for determinism
    return {k: sorted(v) for k, v in canonical_to_aliases.items()}


GAZETTE_COL_TERMS = _build_col_terms()

# IOL places — Indian administrative divisions that appear in Gazette
# These are manually curated since IOL uses different naming from COL
GAZETTE_IOL_TERMS = {
    "Bengal": ["bengal", "fort william"],
    "Bombay": ["bombay", "bombay presidency"],
    "Madras": ["madras", "madras presidency"],
    "Burma": ["burma"],
    "United Provinces": ["united provinces", "agra and oudh"],
    "Punjab": ["punjab"],
    "Central Provinces": ["central provinces"],
    "Assam": ["assam"],
    "Bihar and Orissa": ["bihar", "orissa"],
    "North-West Frontier Province": ["north-west frontier", "north west frontier"],
    "Sind": ["sind", "sindh"],
    "Baluchistan": ["baluchistan", "balochistan"],
    "Coorg": ["coorg"],
    "Ajmer-Merwara": ["ajmer", "merwara"],
    "India (Viceroy)": ["viceroy", "governor-general of india"],
    "India (Secretary of State)": ["secretary of state for india"],
    "Hyderabad": ["hyderabad"],
    "Mysore": ["mysore"],
    "Baroda": ["baroda"],
    "Travancore": ["travancore"],
    "Ceylon": ["ceylon"],  # overlaps with COL — handled in both
}


# =============================================================================
# SPARQL HELPERS
# =============================================================================

def _rate_limit():
    """Enforce minimum interval between SPARQL requests."""
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < MIN_REQUEST_INTERVAL:
        time.sleep(MIN_REQUEST_INTERVAL - elapsed)
    _last_request_time = time.time()


def sparql_query(query: str, max_retries: int = 3) -> dict:
    """Execute a SPARQL query against the Gazette endpoint.

    Returns parsed JSON results. Handles rate limiting and retries with backoff.
    """
    _rate_limit()

    params = urllib.parse.urlencode({"query": query})
    url = f"{SPARQL_ENDPOINT}?{params}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/sparql-results+json",
        "User-Agent": "ColonialOfficeList-Research/1.0",
    })

    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < max_retries - 1:
                wait = (attempt + 1) * 5
                print(f"  HTTP {e.code}, retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
        except urllib.error.URLError as e:
            if attempt < max_retries - 1:
                wait = (attempt + 1) * 5
                print(f"  URL error: {e.reason}, retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise

    return {"results": {"bindings": []}}


def build_colony_search_query(search_terms: list[str], limit: int = 2000) -> str:
    """Build a SPARQL query to find all Gazette entries mentioning a colony.

    Searches both entryText and title fields for any of the search terms.
    Uses subqueries to avoid cross-product explosion from multiple OPTIONAL
    multi-valued properties (honours, titles).
    """
    # Build FILTER clause: OR of CONTAINS for each term on both text and title
    conditions = []
    for term in search_terms:
        escaped = term.replace('"', '\\"')
        conditions.append(f'CONTAINS(LCASE(?text), "{escaped}")')
        conditions.append(f'CONTAINS(LCASE(?title), "{escaped}")')

    filter_clause = " || ".join(conditions)

    # Two-phase: first get distinct entries via text/title filter,
    # then enrich with honour data. This avoids the cross-product
    # between text, title, and honour OPTIONAL joins.
    return f"""
SELECT ?entry ?surname ?forenames ?title ?honour ?text WHERE {{
  ?entry a <{ITEM_TYPE}> .
  ?entry <{PRED_SURNAME}> ?suri .
  ?suri <{RDFS_LABEL}> ?surname .
  OPTIONAL {{ ?entry <{PRED_FORENAMES}> ?forenames }}
  OPTIONAL {{ ?entry <{PRED_TITLE}> ?title }}
  OPTIONAL {{ ?entry <{PRED_HONOUR}> ?honour }}
  OPTIONAL {{ ?entry <{PRED_ENTRY_TEXT}> ?text }}
  FILTER({filter_clause})
}} LIMIT {limit}
"""


def build_entry_query(search_terms: list[str], limit: int = 2000) -> str:
    """Build a lightweight SPARQL query — entries + surnames only, no cross-product.

    Returns entries with surname, forenames, and text. Honours are fetched
    separately per-entry if needed.
    """
    conditions = []
    for term in search_terms:
        escaped = term.replace('"', '\\"')
        conditions.append(f'CONTAINS(LCASE(?text), "{escaped}")')
        conditions.append(f'CONTAINS(LCASE(?title), "{escaped}")')

    filter_clause = " || ".join(conditions)

    return f"""
SELECT DISTINCT ?entry ?surname ?forenames ?title ?text WHERE {{
  ?entry a <{ITEM_TYPE}> .
  ?entry <{PRED_SURNAME}> ?suri .
  ?suri <{RDFS_LABEL}> ?surname .
  OPTIONAL {{ ?entry <{PRED_FORENAMES}> ?forenames }}
  OPTIONAL {{ ?entry <{PRED_TITLE}> ?title }}
  OPTIONAL {{ ?entry <{PRED_ENTRY_TEXT}> ?text }}
  FILTER({filter_clause})
}} LIMIT {limit}
"""


def build_honours_query(entry_uris: list[str]) -> str:
    """Build SPARQL query to fetch honours for a set of entry URIs."""
    values = " ".join(f"<{uri}>" for uri in entry_uris)
    return f"""
SELECT ?entry ?honour WHERE {{
  VALUES ?entry {{ {values} }}
  ?entry <{PRED_HONOUR}> ?honour .
}}
"""


def build_surname_forenames_query(surname_lower: str, limit: int = 200) -> str:
    """Query all entries for a given surname to find forenames.

    Used to enrich entries that matched by colony but lack forenames.
    The surname URI is deterministic: /id/surname/{lowercase_surname}
    """
    surname_uri = f"https://www.thegazette.co.uk/id/surname/{surname_lower}"
    return f"""
SELECT DISTINCT ?entry ?forenames WHERE {{
  ?entry <{PRED_SURNAME}> <{surname_uri}> .
  ?entry <{PRED_FORENAMES}> ?forenames .
}} LIMIT {limit}
"""


# =============================================================================
# ENTRY PARSING
# =============================================================================

# Extract year from Gazette entry URI
# e.g. https://www.thegazette.co.uk/id/London/index/year/1922/volume/1/page/118/item/0041
_YEAR_FROM_URI = re.compile(r"/year/(\d{4})/")


def parse_entry_uri(uri: str) -> dict:
    """Extract structured data from a Gazette entry URI."""
    m = _YEAR_FROM_URI.search(uri)
    year = int(m.group(1)) if m else None
    return {"uri": uri, "year": year}


def aggregate_bindings(bindings: list[dict]) -> dict[str, dict]:
    """Aggregate SPARQL result rows by entry URI.

    Multiple rows for the same entry arise from multiple title/text values.
    Returns {uri: {surname, forenames, year, titles: set, honours: set, texts: set}}.
    """
    entries = {}
    for row in bindings:
        uri = row["entry"]["value"]
        if uri not in entries:
            parsed = parse_entry_uri(uri)
            entries[uri] = {
                "uri": uri,
                "year": parsed["year"],
                "surname": row.get("surname", {}).get("value", ""),
                "forenames": row.get("forenames", {}).get("value", ""),
                "titles": set(),
                "honours": set(),
                "texts": set(),
            }

        entry = entries[uri]

        # Accumulate multi-valued fields
        title_val = row.get("title", {}).get("value", "")
        if title_val:
            entry["titles"].add(title_val)

        honour_val = row.get("honour", {}).get("value", "")
        if honour_val:
            entry["honours"].add(honour_val)

        text_val = row.get("text", {}).get("value", "")
        if text_val:
            entry["texts"].add(text_val)

        # Update forenames if we got a more specific value
        forenames_val = row.get("forenames", {}).get("value", "")
        if forenames_val and len(forenames_val) > len(entry["forenames"]):
            entry["forenames"] = forenames_val

    # Convert sets to sorted lists for JSON serialization
    for entry in entries.values():
        entry["titles"] = sorted(entry["titles"])
        entry["honours"] = sorted(entry["honours"])
        entry["texts"] = sorted(entry["texts"])

    return entries


def add_honours_to_entries(entries: dict[str, dict]) -> None:
    """Fetch and add honours for entries that don't have them yet.

    Makes a separate SPARQL query for honours to avoid cross-product issues.
    """
    uris_needing_honours = [
        uri for uri, e in entries.items()
        if not e.get("honours")
    ]
    if not uris_needing_honours:
        return

    # Batch honours queries (VALUES clause has limits)
    batch_size = 50
    for i in range(0, len(uris_needing_honours), batch_size):
        batch_uris = uris_needing_honours[i:i+batch_size]
        query = build_honours_query(batch_uris)
        try:
            result = sparql_query(query)
            for row in result.get("results", {}).get("bindings", []):
                uri = row["entry"]["value"]
                honour = row.get("honour", {}).get("value", "")
                if uri in entries and honour:
                    if isinstance(entries[uri]["honours"], list):
                        entries[uri]["honours"] = set(entries[uri]["honours"])
                    entries[uri]["honours"].add(honour)
        except Exception:
            pass  # honours are supplementary, don't fail on them

    # Re-convert sets to lists
    for entry in entries.values():
        if isinstance(entry["honours"], set):
            entry["honours"] = sorted(entry["honours"])


def fetch_surname_forenames(entries: dict[str, dict]) -> dict[str, list[str]]:
    """For entries missing forenames, fetch all known forenames for that surname.

    Returns {entry_uri: [candidate_forenames]} — deduplicated list of all
    forenames seen for sibling entries sharing the same surname URI.
    The matching logic scores each candidate and picks the best.
    """
    # Find entries missing forenames
    missing = [(uri, e) for uri, e in entries.items() if not e.get("forenames")]
    if not missing:
        return {}

    # Group by surname to avoid duplicate queries
    surname_groups = defaultdict(list)
    for uri, entry in missing:
        surname = entry.get("surname", "").lower().strip()
        if surname:
            surname_groups[surname].append(uri)

    candidates = {}
    for surname, uris in surname_groups.items():
        query = build_surname_forenames_query(surname)
        try:
            result = sparql_query(query)
        except Exception:
            continue

        # Collect all distinct forenames seen for this surname
        all_forenames = set()
        for row in result.get("results", {}).get("bindings", []):
            fore = row.get("forenames", {}).get("value", "")
            if fore:
                all_forenames.add(fore)

        if all_forenames:
            forenames_list = sorted(all_forenames)
            for uri in uris:
                candidates[uri] = forenames_list

    return candidates


def extract_role_from_entry(entry: dict) -> str:
    """Extract the role/position from an entry's text or title fields."""
    # Prefer entryText (more detailed)
    for text in entry.get("texts", []):
        if text:
            return text

    # Fall back to title (often contains rank + role)
    for title in entry.get("titles", []):
        if title:
            return title

    return ""


def colony_slug(colony_name: str) -> str:
    """Convert colony name to filesystem-safe slug."""
    s = colony_name.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


if __name__ == "__main__":
    print(f"COL colonies: {len(GAZETTE_COL_TERMS)}")
    print(f"IOL places: {len(GAZETTE_IOL_TERMS)}")
    print(f"\nSample COL terms:")
    for colony in sorted(GAZETTE_COL_TERMS)[:10]:
        print(f"  {colony}: {GAZETTE_COL_TERMS[colony]}")
    print(f"\nSample IOL terms:")
    for place in sorted(GAZETTE_IOL_TERMS)[:5]:
        print(f"  {place}: {GAZETTE_IOL_TERMS[place]}")

#!/usr/bin/env python3
"""
Harvest people associated with British colonies from Wikidata.

Casts a wide net: colonial officials, governors, indigenous leaders, civil society
figures — anyone with a Wikidata entry connected to our colony entities.

Strategies:
  1. positions    — Find position items linked to our colonies (via P1001/P642/P17)
  2. holders      — Find all holders (P39) of positions discovered in strategy 1
  3. colonial-office — People employed by / holding positions in the Colonial Office
  4. governor-tree — Find ALL subclasses of Governor (Q132050) and harvest holders
  5. direct-p39   — People with P39 qualified by colony QIDs
  6. associated    — Broader: anyone born in, died in, citizen of, or active in colonies
  7. snowball     — Start from known officials, follow replaces/replaced-by chains
  8. merge        — Combine all results into unified dataset
  9. cypher       — Generate Neo4j load script

Usage:
  python3 wikidata_harvest_officials.py --strategy all
  python3 wikidata_harvest_officials.py --inspect Q2577822
  python3 wikidata_harvest_officials.py --strategy snowball --seeds Q2577822 Q1583232
  python3 wikidata_harvest_officials.py --strategy associated
"""

import json
import time
import csv
import argparse
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import quote
from urllib.error import HTTPError, URLError

# ── Config ──────────────────────────────────────────────────────────────────

SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"
WIKIDATA_API = "https://www.wikidata.org/w/api.php"
USER_AGENT = "ColonialOfficeListBot/1.0 (historical-research; mailto:jic823@usask.ca)"
CROSSWALK_PATH = Path(__file__).parent / "scaffolding" / "col_kg_crosswalk.json"
OUTPUT_DIR = Path(__file__).parent / "wikidata_harvest"

# Rate limiting
SPARQL_DELAY = 2.0   # seconds between SPARQL queries
API_DELAY = 0.5      # seconds between REST API calls

# Known Wikidata items
COLONIAL_OFFICE_QID = "Q1201542"       # Colonial Office
COLONIAL_SECRETARY_QID = "Q3295079"    # Secretary of State for the Colonies
GOVERNOR_QID = "Q132050"               # Governor (generic)
GOVERNOR_GENERAL_QID = "Q382844"       # Governor-General

# ── Helpers ─────────────────────────────────────────────────────────────────

def sparql_query(query: str, retries: int = 3) -> dict:
    """Execute a SPARQL query against Wikidata."""
    url = f"{SPARQL_ENDPOINT}?format=json&query={quote(query)}"
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    for attempt in range(retries):
        try:
            with urlopen(req, timeout=120) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except HTTPError as e:
            if e.code == 429 or e.code == 503:
                wait = SPARQL_DELAY * (2 ** attempt)
                print(f"  Rate limited ({e.code}), waiting {wait}s...")
                time.sleep(wait)
            else:
                raise
        except URLError as e:
            wait = SPARQL_DELAY * (2 ** attempt)
            print(f"  Connection error: {e}, retrying in {wait}s...")
            time.sleep(wait)
    raise RuntimeError(f"SPARQL query failed after {retries} retries")


def wikidata_entity(qid: str) -> dict:
    """Fetch a single Wikidata entity via the REST API."""
    url = f"{WIKIDATA_API}?action=wbgetentities&ids={qid}&format=json&props=labels|descriptions|claims"
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data.get("entities", {}).get(qid, {})


def get_label(entity: dict, lang: str = "en") -> str:
    return entity.get("labels", {}).get(lang, {}).get("value", "")


def get_description(entity: dict, lang: str = "en") -> str:
    return entity.get("descriptions", {}).get(lang, {}).get("value", "")


def extract_qid(uri: str) -> str:
    return uri.rsplit("/", 1)[-1] if "/" in uri else uri


def load_colony_qids() -> dict:
    """Load colony QIDs from crosswalk JSON. Returns {qid: {colony_id, canonical_name, col_name, ...}}"""
    with open(CROSSWALK_PATH) as f:
        crosswalk = json.load(f)

    qid_map = {}
    for col_name, info in crosswalk.items():
        for m in info.get("mappings", []):
            qid = m.get("wikidata_id", "")
            if qid and qid.startswith("Q"):
                qid_map[qid] = {
                    "colony_id": m.get("colony_id", ""),
                    "canonical_name": m.get("canonical_name", ""),
                    "col_name": col_name,
                    "year_start": m.get("year_start"),
                    "year_end": m.get("year_end"),
                }
    return qid_map


def save_json(data, filename: str):
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / filename
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    n = len(data) if isinstance(data, (list, dict)) else "?"
    print(f"  Saved {path} ({n} items)")
    return path


def parse_year(timestr: str) -> str:
    """Extract year from Wikidata time string like '+1914-06-15T00:00:00Z'."""
    if not timestr:
        return ""
    # Handle both full timestamps and just years
    timestr = timestr.lstrip("+")
    if "T" in timestr:
        return timestr.split("T")[0]
    return timestr[:10]


# ── Inspect ─────────────────────────────────────────────────────────────────

def inspect_entity(qid: str):
    """Inspect a Wikidata entity to understand its structure."""
    print(f"\n=== Inspecting {qid} ===")
    entity = wikidata_entity(qid)
    name = get_label(entity)
    desc = get_description(entity)
    print(f"  Name: {name}")
    print(f"  Description: {desc}")

    claims = entity.get("claims", {})

    # Key properties to display
    prop_names = {
        "P39": "position held", "P108": "employer", "P106": "occupation",
        "P27": "citizenship", "P19": "birth place", "P20": "death place",
        "P569": "birth date", "P570": "death date",
        "P1001": "jurisdiction", "P17": "country", "P131": "located in",
        "P279": "subclass of", "P31": "instance of", "P361": "part of",
        "P642": "of", "P1365": "replaces", "P1366": "replaced by",
    }

    for prop, prop_label in prop_names.items():
        if prop not in claims:
            continue
        print(f"\n  {prop} ({prop_label}): {len(claims[prop])} values")
        for i, claim in enumerate(claims[prop]):
            mainsnak = claim.get("mainsnak", {})
            dv = mainsnak.get("datavalue", {})

            if dv.get("type") == "wikibase-entityid":
                val = dv.get("value", {}).get("id", "?")
            elif dv.get("type") == "time":
                val = dv.get("value", {}).get("time", "?")
            elif dv.get("type") == "string":
                val = dv.get("value", "?")
            else:
                val = str(dv)

            # Show qualifiers for P39
            quals_str = ""
            if prop == "P39":
                quals = claim.get("qualifiers", {})
                parts = []
                for qprop in ["P580", "P582", "P1001", "P642", "P1365", "P1366"]:
                    if qprop in quals:
                        qval = quals[qprop][0].get("datavalue", {}).get("value", {})
                        if isinstance(qval, dict) and "id" in qval:
                            parts.append(f"{qprop}={qval['id']}")
                        elif isinstance(qval, dict) and "time" in qval:
                            parts.append(f"{qprop}={qval['time'][:10]}")
                if parts:
                    quals_str = f"  [{', '.join(parts)}]"

            print(f"    [{i+1}] {val}{quals_str}")

    return entity


# ── Strategy 1: Find position items for colonies ───────────────────────────

def harvest_positions_all_colonies():
    """
    Find all position items linked to our colonies via P1001/P642/P17.
    Also finds positions that are subclasses of Governor for our colony's modern countries.
    """
    colony_qids = load_colony_qids()
    unique_qids = list(set(colony_qids.keys()))

    print(f"\n=== Strategy 1: Finding positions for {len(unique_qids)} colony QIDs ===")

    # Single SPARQL query for all colonies at once (batched)
    all_positions = []
    batch_size = 30

    for batch_start in range(0, len(unique_qids), batch_size):
        batch = unique_qids[batch_start:batch_start + batch_size]
        values = " ".join(f"wd:{qid}" for qid in batch)

        query = f"""
        SELECT DISTINCT ?position ?positionLabel ?positionDescription
               ?colony ?colonyLabel ?linkProp WHERE {{
          VALUES ?colony {{ {values} }}
          {{
            ?position wdt:P1001 ?colony .
            BIND("P1001" AS ?linkProp)
          }} UNION {{
            ?position wdt:P642 ?colony .
            BIND("P642" AS ?linkProp)
          }} UNION {{
            ?position wdt:P17 ?colony .
            BIND("P17" AS ?linkProp)
          }}
          # Position must have at least one holder (P39) to be a real position
          FILTER EXISTS {{ ?someone wdt:P39 ?position }}
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" }}
        }}
        """

        batch_num = batch_start // batch_size + 1
        total_batches = (len(unique_qids) + batch_size - 1) // batch_size
        print(f"  Batch {batch_num}/{total_batches}...", end=" ", flush=True)

        try:
            result = sparql_query(query)
            rows = result.get("results", {}).get("bindings", [])
            print(f"{len(rows)} positions")

            for row in rows:
                colony_qid = extract_qid(row["colony"]["value"])
                colony_info = colony_qids.get(colony_qid, {})
                all_positions.append({
                    "position_qid": extract_qid(row["position"]["value"]),
                    "position_label": row.get("positionLabel", {}).get("value", ""),
                    "position_desc": row.get("positionDescription", {}).get("value", ""),
                    "colony_qid": colony_qid,
                    "colony_name": colony_info.get("canonical_name", ""),
                    "col_name": colony_info.get("col_name", ""),
                    "link_property": row.get("linkProp", {}).get("value", ""),
                })
        except Exception as e:
            print(f"ERROR: {e}")

        time.sleep(SPARQL_DELAY)

    # Deduplicate
    unique = {}
    for p in all_positions:
        key = (p["position_qid"], p["colony_qid"])
        unique[key] = p
    all_positions = list(unique.values())

    print(f"\n  Total unique (position, colony) pairs: {len(all_positions)}")
    print(f"  Unique position items: {len(set(p['position_qid'] for p in all_positions))}")
    save_json(all_positions, "colony_positions.json")
    return all_positions


# ── Strategy 2: Find holders of discovered positions ───────────────────────

def harvest_holders(positions_file: str = "colony_positions.json"):
    """For each discovered position, find all people who held it (P39)."""
    positions_path = OUTPUT_DIR / positions_file
    if not positions_path.exists():
        print(f"  Run 'positions' strategy first to generate {positions_path}")
        return []

    with open(positions_path) as f:
        positions = json.load(f)

    # Get unique positions with their colony info
    unique_positions = {}
    for p in positions:
        pqid = p["position_qid"]
        if pqid not in unique_positions:
            unique_positions[pqid] = p
        # Keep colony info as list
        if "colonies" not in unique_positions[pqid]:
            unique_positions[pqid]["colonies"] = []
        unique_positions[pqid]["colonies"].append({
            "colony_qid": p["colony_qid"],
            "colony_name": p.get("colony_name", ""),
            "col_name": p.get("col_name", ""),
        })

    print(f"\n=== Strategy 2: Finding holders for {len(unique_positions)} unique positions ===")

    # Batch query: all holders of all positions at once (batched)
    pos_list = list(unique_positions.keys())
    all_holders = []
    batch_size = 50

    for batch_start in range(0, len(pos_list), batch_size):
        batch = pos_list[batch_start:batch_start + batch_size]
        values = " ".join(f"wd:{qid}" for qid in batch)

        query = f"""
        SELECT ?person ?personLabel ?personDescription
               ?position ?positionLabel ?start ?end
               ?replaces ?replacesLabel ?replacedBy ?replacedByLabel WHERE {{
          VALUES ?position {{ {values} }}
          ?person p:P39 ?stmt .
          ?stmt ps:P39 ?position .
          OPTIONAL {{ ?stmt pq:P580 ?start }}
          OPTIONAL {{ ?stmt pq:P582 ?end }}
          OPTIONAL {{ ?stmt pq:P1365 ?replaces }}
          OPTIONAL {{ ?stmt pq:P1366 ?replacedBy }}
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" }}
        }}
        """

        batch_num = batch_start // batch_size + 1
        total_batches = (len(pos_list) + batch_size - 1) // batch_size
        print(f"  Batch {batch_num}/{total_batches}...", end=" ", flush=True)

        try:
            result = sparql_query(query)
            rows = result.get("results", {}).get("bindings", [])
            print(f"{len(rows)} holders")

            for row in rows:
                pos_qid = extract_qid(row["position"]["value"])
                pos_info = unique_positions.get(pos_qid, {})
                colony_name = pos_info.get("colony_name", "")
                col_name = pos_info.get("col_name", "")
                colony_qid = pos_info.get("colony_qid", "")

                all_holders.append({
                    "person_qid": extract_qid(row["person"]["value"]),
                    "person_label": row.get("personLabel", {}).get("value", ""),
                    "person_desc": row.get("personDescription", {}).get("value", ""),
                    "position_qid": pos_qid,
                    "position_label": row.get("positionLabel", {}).get("value", ""),
                    "colony_qid": colony_qid,
                    "colony_name": colony_name,
                    "col_name": col_name,
                    "start": parse_year(row.get("start", {}).get("value", "")),
                    "end": parse_year(row.get("end", {}).get("value", "")),
                    "replaces_qid": extract_qid(row["replaces"]["value"]) if "replaces" in row else "",
                    "replaced_by_qid": extract_qid(row["replacedBy"]["value"]) if "replacedBy" in row else "",
                    "source": "position_holders",
                })
        except Exception as e:
            print(f"ERROR: {e}")

        time.sleep(SPARQL_DELAY)

    # Deduplicate
    unique = {}
    for h in all_holders:
        key = (h["person_qid"], h["position_qid"])
        unique[key] = h
    all_holders = list(unique.values())

    unique_people = set(h["person_qid"] for h in all_holders)
    print(f"\n  Total person-position records: {len(all_holders)}")
    print(f"  Unique people: {len(unique_people)}")
    save_json(all_holders, "colony_position_holders.json")
    return all_holders


# ── Strategy 3: Colonial Office people ──────────────────────────────────────

def harvest_colonial_office_employees():
    """Find people employed by or holding positions in the Colonial Office."""
    print(f"\n=== Strategy 3: Colonial Office employees ===")

    queries = {
        "employer_P108": f"""
            SELECT ?person ?personLabel ?personDescription WHERE {{
              ?person wdt:P108 wd:{COLONIAL_OFFICE_QID} .
              SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" }}
            }}
        """,
        "sec_of_state": f"""
            SELECT ?person ?personLabel ?personDescription ?start ?end WHERE {{
              ?person p:P39 ?stmt .
              ?stmt ps:P39 wd:{COLONIAL_SECRETARY_QID} .
              OPTIONAL {{ ?stmt pq:P580 ?start }}
              OPTIONAL {{ ?stmt pq:P582 ?end }}
              SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" }}
            }}
        """,
        # Under-Secretary of State for the Colonies
        "under_sec": """
            SELECT ?person ?personLabel ?personDescription ?pos ?posLabel ?start ?end WHERE {
              ?person p:P39 ?stmt .
              ?stmt ps:P39 ?pos .
              ?pos rdfs:label ?posLabel .
              FILTER(LANG(?posLabel) = "en")
              FILTER(CONTAINS(LCASE(?posLabel), "colonial") || CONTAINS(LCASE(?posLabel), "colonies"))
              OPTIONAL { ?stmt pq:P580 ?start }
              OPTIONAL { ?stmt pq:P582 ?end }
              SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
            }
        """,
    }

    all_people = []
    for label, query in queries.items():
        print(f"  Query: {label}...", end=" ", flush=True)
        try:
            result = sparql_query(query)
            rows = result.get("results", {}).get("bindings", [])
            print(f"{len(rows)} results")
            for row in rows:
                all_people.append({
                    "person_qid": extract_qid(row["person"]["value"]),
                    "person_label": row.get("personLabel", {}).get("value", ""),
                    "person_desc": row.get("personDescription", {}).get("value", ""),
                    "source": f"colonial_office_{label}",
                    "position_label": row.get("posLabel", {}).get("value", ""),
                    "start": parse_year(row.get("start", {}).get("value", "")),
                    "end": parse_year(row.get("end", {}).get("value", "")),
                })
        except Exception as e:
            print(f"ERROR: {e}")
        time.sleep(SPARQL_DELAY)

    unique = {}
    for p in all_people:
        if p["person_qid"] not in unique:
            unique[p["person_qid"]] = p
    all_people = list(unique.values())

    print(f"  Unique Colonial Office people: {len(all_people)}")
    save_json(all_people, "colonial_office_people.json")
    return all_people


# ── Strategy 4: Governor tree — all subclasses of Governor ──────────────────

def harvest_governor_tree():
    """
    Find ALL position items that are subclasses of Governor (Q132050) or
    Governor-General (Q382844), then find all holders.
    This catches positions that aren't linked to our colony QIDs but ARE
    governor/lieutenant-governor roles in British territories.
    """
    print(f"\n=== Strategy 4: Governor type hierarchy ===")

    # First find all governor-type positions
    query = """
    SELECT DISTINCT ?position ?positionLabel ?positionDescription
           ?jurisdiction ?jurisdictionLabel WHERE {
      {
        ?position wdt:P279+ wd:Q132050 .  # subclass of Governor
      } UNION {
        ?position wdt:P279+ wd:Q382844 .  # subclass of Governor-General
      } UNION {
        ?position wdt:P279+ wd:Q1970061 . # subclass of Lieutenant Governor
      } UNION {
        ?position wdt:P279+ wd:Q123695 .  # subclass of High Commissioner
      }
      OPTIONAL { ?position wdt:P1001 ?jurisdiction }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
    }
    """

    print("  Finding all governor-type positions...", end=" ", flush=True)
    try:
        result = sparql_query(query)
        rows = result.get("results", {}).get("bindings", [])
        print(f"{len(rows)} positions found")
    except Exception as e:
        print(f"ERROR: {e}")
        return []

    # Filter for positions related to British territories
    # Keep all of them but tag which ones match our colonies
    colony_qids = load_colony_qids()
    colony_qid_set = set(colony_qids.keys())

    positions = []
    for row in rows:
        pos_qid = extract_qid(row["position"]["value"])
        label = row.get("positionLabel", {}).get("value", "")
        desc = row.get("positionDescription", {}).get("value", "")
        jurisdiction = extract_qid(row["jurisdiction"]["value"]) if "jurisdiction" in row else ""

        # Check if this is a British colonial position
        is_colony_match = jurisdiction in colony_qid_set

        # Also check label for British-related keywords
        label_lower = label.lower()
        is_british = any(kw in label_lower for kw in [
            "british", "colonial", "crown colony", "protectorate",
        ])
        # Check if any of our colony names appear in the label
        is_colony_name = any(
            colony_qids[qid]["canonical_name"].lower() in label_lower or
            colony_qids[qid]["col_name"].lower() in label_lower
            for qid in colony_qid_set
        )

        positions.append({
            "position_qid": pos_qid,
            "position_label": label,
            "position_desc": desc,
            "jurisdiction_qid": jurisdiction,
            "jurisdiction_label": row.get("jurisdictionLabel", {}).get("value", ""),
            "is_colony_match": is_colony_match,
            "is_british_keyword": is_british,
            "is_colony_name_match": is_colony_name,
        })

    # Separate matched vs unmatched
    matched = [p for p in positions if p["is_colony_match"] or p["is_colony_name_match"]]
    british = [p for p in positions if p["is_british_keyword"] and not p["is_colony_match"]]

    print(f"  Direct colony QID matches: {len(matched)}")
    print(f"  British keyword matches: {len(british)}")
    print(f"  Total positions (including non-British): {len(positions)}")

    save_json(positions, "governor_tree_all.json")
    save_json(matched + british, "governor_tree_british.json")

    return matched + british


# ── Strategy 5: Direct P39 with colony qualifiers ──────────────────────────

def harvest_direct_p39_colony():
    """
    Find all people who held any position where the P39 statement has a qualifier
    (P1001, P642) pointing to one of our colony QIDs.
    """
    colony_qids = load_colony_qids()
    unique_qids = list(set(colony_qids.keys()))

    print(f"\n=== Strategy 5: Direct P39 with colony qualifiers ({len(unique_qids)} QIDs) ===")

    all_results = []
    batch_size = 20

    for batch_start in range(0, len(unique_qids), batch_size):
        batch = unique_qids[batch_start:batch_start + batch_size]
        values = " ".join(f"wd:{qid}" for qid in batch)

        query = f"""
        SELECT ?person ?personLabel ?personDescription
               ?pos ?posLabel ?colony ?colonyLabel ?start ?end WHERE {{
          VALUES ?colony {{ {values} }}
          ?person p:P39 ?stmt .
          ?stmt ps:P39 ?pos .
          {{
            ?stmt pq:P1001 ?colony .
          }} UNION {{
            ?stmt pq:P642 ?colony .
          }}
          OPTIONAL {{ ?stmt pq:P580 ?start }}
          OPTIONAL {{ ?stmt pq:P582 ?end }}
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" }}
        }}
        """

        batch_num = batch_start // batch_size + 1
        total_batches = (len(unique_qids) + batch_size - 1) // batch_size
        print(f"  Batch {batch_num}/{total_batches}...", end=" ", flush=True)

        try:
            result = sparql_query(query)
            rows = result.get("results", {}).get("bindings", [])
            print(f"{len(rows)} results")

            for row in rows:
                colony_qid = extract_qid(row["colony"]["value"])
                colony_info = colony_qids.get(colony_qid, {})
                all_results.append({
                    "person_qid": extract_qid(row["person"]["value"]),
                    "person_label": row.get("personLabel", {}).get("value", ""),
                    "person_desc": row.get("personDescription", {}).get("value", ""),
                    "position_qid": extract_qid(row["pos"]["value"]),
                    "position_label": row.get("posLabel", {}).get("value", ""),
                    "colony_qid": colony_qid,
                    "colony_name": colony_info.get("canonical_name", ""),
                    "col_name": colony_info.get("col_name", ""),
                    "start": parse_year(row.get("start", {}).get("value", "")),
                    "end": parse_year(row.get("end", {}).get("value", "")),
                    "source": "direct_p39_qualifier",
                })
        except Exception as e:
            print(f"ERROR: {e}")

        time.sleep(SPARQL_DELAY)

    unique = {}
    for r in all_results:
        key = (r["person_qid"], r["position_qid"], r["colony_qid"])
        unique[key] = r
    all_results = list(unique.values())

    unique_people = set(r["person_qid"] for r in all_results)
    print(f"\n  Total records: {len(all_results)}, unique people: {len(unique_people)}")
    save_json(all_results, "direct_p39_colony_holders.json")
    return all_results


# ── Strategy 6: Associated people (broad net) ──────────────────────────────

def harvest_associated_people():
    """
    Broad strategy: find anyone associated with our colonies via:
    - P19 (place of birth) in colony
    - P20 (place of death) in colony
    - P27 (country of citizenship) = colony
    - P937 (work location) in colony
    - P551 (residence) in colony

    This catches indigenous leaders, civil society figures, etc. who may not
    have held formal positions but are notable enough for Wikidata.

    We filter for people active during the colonial period.
    """
    colony_qids = load_colony_qids()
    unique_qids = list(set(colony_qids.keys()))

    print(f"\n=== Strategy 6: Associated people (broad net) ===")

    # Properties to search
    properties = {
        "P19": "born in",
        "P20": "died in",
        "P27": "citizen of",
        "P937": "work location",
        "P551": "residence",
    }

    all_results = []
    batch_size = 20

    for prop, prop_label in properties.items():
        print(f"\n  Property: {prop} ({prop_label})")

        for batch_start in range(0, len(unique_qids), batch_size):
            batch = unique_qids[batch_start:batch_start + batch_size]
            values = " ".join(f"wd:{qid}" for qid in batch)

            query = f"""
            SELECT ?person ?personLabel ?personDescription
                   ?colony ?colonyLabel ?birth ?death WHERE {{
              VALUES ?colony {{ {values} }}
              ?person wdt:{prop} ?colony .
              OPTIONAL {{ ?person wdt:P569 ?birth }}
              OPTIONAL {{ ?person wdt:P570 ?death }}
              # Only humans
              ?person wdt:P31 wd:Q5 .
              SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" }}
            }} LIMIT 5000
            """

            batch_num = batch_start // batch_size + 1
            total_batches = (len(unique_qids) + batch_size - 1) // batch_size
            print(f"    Batch {batch_num}/{total_batches}...", end=" ", flush=True)

            try:
                result = sparql_query(query)
                rows = result.get("results", {}).get("bindings", [])
                print(f"{len(rows)} people")

                for row in rows:
                    colony_qid = extract_qid(row["colony"]["value"])
                    colony_info = colony_qids.get(colony_qid, {})
                    all_results.append({
                        "person_qid": extract_qid(row["person"]["value"]),
                        "person_label": row.get("personLabel", {}).get("value", ""),
                        "person_desc": row.get("personDescription", {}).get("value", ""),
                        "colony_qid": colony_qid,
                        "colony_name": colony_info.get("canonical_name", ""),
                        "col_name": colony_info.get("col_name", ""),
                        "association": prop_label,
                        "association_property": prop,
                        "birth": parse_year(row.get("birth", {}).get("value", "")),
                        "death": parse_year(row.get("death", {}).get("value", "")),
                        "source": f"associated_{prop}",
                    })
            except Exception as e:
                print(f"ERROR: {e}")

            time.sleep(SPARQL_DELAY)

    # Deduplicate by (person, colony, property)
    unique = {}
    for r in all_results:
        key = (r["person_qid"], r["colony_qid"], r["association_property"])
        unique[key] = r
    all_results = list(unique.values())

    unique_people = set(r["person_qid"] for r in all_results)
    print(f"\n  Total records: {len(all_results)}, unique people: {len(unique_people)}")
    save_json(all_results, "associated_people.json")
    return all_results


# ── Strategy 7: Snowball from known officials ───────────────────────────────

def harvest_snowball(seed_qids: list = None):
    """
    Start from known officials, inspect their P39 positions, then follow
    replaces/replaced-by chains to discover more people and positions.

    This is the most organic discovery method — it follows career linkages.
    """
    if seed_qids is None:
        seed_qids = ["Q2577822"]  # William Allardyce

    print(f"\n=== Strategy 7: Snowball from {len(seed_qids)} seeds ===")

    colony_qids = load_colony_qids()
    colony_qid_set = set(colony_qids.keys())

    discovered_people = {}   # qid -> {name, desc, positions}
    discovered_positions = {}  # pos_qid -> {label, jurisdiction}
    queue = list(seed_qids)
    visited = set()

    max_people = 500  # Safety limit
    iteration = 0

    while queue and len(discovered_people) < max_people:
        person_qid = queue.pop(0)
        if person_qid in visited:
            continue
        visited.add(person_qid)
        iteration += 1

        print(f"  [{iteration}] Inspecting {person_qid}...", end=" ", flush=True)

        try:
            entity = wikidata_entity(person_qid)
            name = get_label(entity)
            desc = get_description(entity)
            print(f"{name}")

            claims = entity.get("claims", {})

            # Check it's a human (P31 = Q5)
            is_human = False
            for c in claims.get("P31", []):
                if c.get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id") == "Q5":
                    is_human = True
                    break

            if not is_human:
                print(f"    (not a human, skipping)")
                time.sleep(API_DELAY)
                continue

            person_info = {
                "qid": person_qid,
                "name": name,
                "description": desc,
                "positions": [],
                "source": "snowball",
            }

            for claim in claims.get("P39", []):
                mainsnak = claim.get("mainsnak", {})
                pos_qid = mainsnak.get("datavalue", {}).get("value", {}).get("id", "")
                if not pos_qid:
                    continue

                quals = claim.get("qualifiers", {})
                start = end = ""
                replaces = replaced_by = ""

                if "P580" in quals:
                    start = quals["P580"][0].get("datavalue", {}).get("value", {}).get("time", "")
                if "P582" in quals:
                    end = quals["P582"][0].get("datavalue", {}).get("value", {}).get("time", "")
                if "P1365" in quals:
                    replaces = quals["P1365"][0].get("datavalue", {}).get("value", {}).get("id", "")
                    if replaces and replaces not in visited:
                        queue.append(replaces)
                if "P1366" in quals:
                    replaced_by = quals["P1366"][0].get("datavalue", {}).get("value", {}).get("id", "")
                    if replaced_by and replaced_by not in visited:
                        queue.append(replaced_by)

                person_info["positions"].append({
                    "position_qid": pos_qid,
                    "start": parse_year(start),
                    "end": parse_year(end),
                    "replaces_qid": replaces,
                    "replaced_by_qid": replaced_by,
                })

                if pos_qid not in discovered_positions:
                    discovered_positions[pos_qid] = {"position_qid": pos_qid}

            discovered_people[person_qid] = person_info

        except Exception as e:
            print(f"ERROR: {e}")

        time.sleep(API_DELAY)

    print(f"\n  Discovered {len(discovered_people)} people, {len(discovered_positions)} positions")
    print(f"  Queue remaining: {len(queue)} (visited: {len(visited)})")

    # Resolve position labels
    print("  Resolving position labels...")
    for pos_qid in list(discovered_positions.keys()):
        try:
            pos_entity = wikidata_entity(pos_qid)
            discovered_positions[pos_qid]["position_label"] = get_label(pos_entity)
            discovered_positions[pos_qid]["position_desc"] = get_description(pos_entity)

            # Check jurisdiction
            for prop in ["P1001", "P17"]:
                for c in pos_entity.get("claims", {}).get(prop, []):
                    jur_qid = c.get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", "")
                    if jur_qid:
                        discovered_positions[pos_qid][f"jurisdiction_{prop}"] = jur_qid
                        if jur_qid in colony_qid_set:
                            discovered_positions[pos_qid]["colony_match"] = True
                            discovered_positions[pos_qid]["colony_qid"] = jur_qid

            time.sleep(API_DELAY)
        except Exception as e:
            print(f"    {pos_qid}: ERROR {e}")

    # Enrich people with position labels
    for person in discovered_people.values():
        for pos in person["positions"]:
            pos_info = discovered_positions.get(pos["position_qid"], {})
            pos["position_label"] = pos_info.get("position_label", "")
            pos["colony_qid"] = pos_info.get("colony_qid", "")

    save_json(list(discovered_people.values()), "snowball_people.json")
    save_json(list(discovered_positions.values()), "snowball_positions.json")

    return discovered_people


# ── Strategy 8: Colonial honours recipients ─────────────────────────────────

# Order of St Michael and St George — THE colonial service order
HONOURS_QIDS = {
    # Order of St Michael and St George (colonial service)
    "Q12177423": "GCMG - Knight Grand Cross of St Michael and St George",
    "Q12177415": "KCMG - Knight Commander of St Michael and St George",
    "Q12177413": "CMG - Companion of St Michael and St George",
    # Order of the Indian Empire (India & dependencies)
    "Q93710": "Order of the Indian Empire (overall)",
    # Order of the Star of India
    "Q1330936": "Order of the Star of India (overall)",
    # Imperial Service Order (colonial civil servants on retirement)
    "Q1810753": "Imperial Service Order",
}


def harvest_honours():
    """
    Strategy 8: Find all recipients of colonial-service honours.
    The Order of St Michael and St George was specifically for colonial service.
    Also harvests their P39 (positions held) to link them to colonies.
    """
    print(f"\n=== Strategy 8: Colonial honours recipients ===")

    all_results = []

    for honour_qid, honour_label in HONOURS_QIDS.items():
        print(f"\n  {honour_label} ({honour_qid})...")

        # Get all recipients with their positions
        query = f"""
        SELECT ?person ?personLabel ?personDescription
               ?pos ?posLabel ?start ?end WHERE {{
          ?person wdt:P166 wd:{honour_qid} .
          ?person wdt:P31 wd:Q5 .
          OPTIONAL {{
            ?person p:P39 ?stmt .
            ?stmt ps:P39 ?pos .
            OPTIONAL {{ ?stmt pq:P580 ?start }}
            OPTIONAL {{ ?stmt pq:P582 ?end }}
          }}
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" }}
        }}
        """

        try:
            result = sparql_query(query)
            rows = result.get("results", {}).get("bindings", [])
            print(f"    {len(rows)} person-position records")

            for row in rows:
                all_results.append({
                    "person_qid": extract_qid(row["person"]["value"]),
                    "person_label": row.get("personLabel", {}).get("value", ""),
                    "person_desc": row.get("personDescription", {}).get("value", ""),
                    "honour_qid": honour_qid,
                    "honour_label": honour_label,
                    "position_qid": extract_qid(row["pos"]["value"]) if "pos" in row else "",
                    "position_label": row.get("posLabel", {}).get("value", ""),
                    "start": parse_year(row.get("start", {}).get("value", "")),
                    "end": parse_year(row.get("end", {}).get("value", "")),
                    "source": "honours",
                })
        except Exception as e:
            print(f"    ERROR: {e}")

        time.sleep(SPARQL_DELAY)

    # Deduplicate by (person, honour, position)
    unique = {}
    for r in all_results:
        key = (r["person_qid"], r["honour_qid"], r.get("position_qid", ""))
        unique[key] = r
    all_results = list(unique.values())

    unique_people = set(r["person_qid"] for r in all_results)
    print(f"\n  Total records: {len(all_results)}")
    print(f"  Unique people: {len(unique_people)}")

    # Summary by honour
    from collections import Counter
    honour_counts = Counter()
    for r in all_results:
        honour_counts[r["honour_label"]] += 1
    for h, c in honour_counts.most_common():
        print(f"    {h}: {c} records")

    save_json(all_results, "honours_recipients.json")
    return all_results


# ── Merge ───────────────────────────────────────────────────────────────────

def merge_all_results():
    """Merge all harvested data into a single deduplicated dataset."""
    print("\n=== Merging all results ===")

    people = {}  # person_qid -> merged info

    # Load structured results
    structured_files = [
        ("colony_position_holders.json", "position_holders"),
        ("direct_p39_colony_holders.json", "direct_p39"),
        ("colonial_office_people.json", "colonial_office"),
        ("honours_recipients.json", "honours"),
        ("colonial_administrators.json", "colonial_admin"),
    ]

    for filename, source in structured_files:
        path = OUTPUT_DIR / filename
        if not path.exists():
            continue

        with open(path) as f:
            records = json.load(f)
        print(f"  Loading {filename}: {len(records)} records")

        for rec in records:
            qid = rec["person_qid"]
            if qid not in people:
                people[qid] = {
                    "qid": qid,
                    "name": rec.get("person_label", ""),
                    "description": rec.get("person_desc", rec.get("person_description", "")),
                    "positions": [],
                    "associations": [],
                    "sources": set(),
                }
            people[qid]["sources"].add(source)

            if rec.get("position_qid"):
                people[qid]["positions"].append({
                    "position_qid": rec.get("position_qid", ""),
                    "position_label": rec.get("position_label", ""),
                    "colony_qid": rec.get("colony_qid", ""),
                    "colony_name": rec.get("colony_name", rec.get("col_name", "")),
                    "start": rec.get("start", ""),
                    "end": rec.get("end", ""),
                    "source": source,
                })

    # Load snowball results
    snowball_path = OUTPUT_DIR / "snowball_people.json"
    if snowball_path.exists():
        with open(snowball_path) as f:
            snowball = json.load(f)
        print(f"  Loading snowball_people.json: {len(snowball)} records")
        for rec in snowball:
            qid = rec["qid"]
            if qid not in people:
                people[qid] = {
                    "qid": qid,
                    "name": rec.get("name", ""),
                    "description": rec.get("description", ""),
                    "positions": [],
                    "associations": [],
                    "sources": set(),
                }
            people[qid]["sources"].add("snowball")
            for pos in rec.get("positions", []):
                people[qid]["positions"].append({
                    "position_qid": pos.get("position_qid", ""),
                    "position_label": pos.get("position_label", ""),
                    "colony_qid": pos.get("colony_qid", ""),
                    "colony_name": "",
                    "start": pos.get("start", ""),
                    "end": pos.get("end", ""),
                    "source": "snowball",
                })

    # Load associated people
    assoc_path = OUTPUT_DIR / "associated_people.json"
    if assoc_path.exists():
        with open(assoc_path) as f:
            associated = json.load(f)
        print(f"  Loading associated_people.json: {len(associated)} records")
        for rec in associated:
            qid = rec["person_qid"]
            if qid not in people:
                people[qid] = {
                    "qid": qid,
                    "name": rec.get("person_label", ""),
                    "description": rec.get("person_desc", ""),
                    "positions": [],
                    "associations": [],
                    "sources": set(),
                }
            people[qid]["sources"].add("associated")
            people[qid]["associations"].append({
                "colony_qid": rec.get("colony_qid", ""),
                "colony_name": rec.get("colony_name", ""),
                "association": rec.get("association", ""),
                "birth": rec.get("birth", ""),
                "death": rec.get("death", ""),
            })

    # Clean up for serialization
    for p in people.values():
        p["sources"] = sorted(p["sources"])
        # Deduplicate positions
        seen = set()
        unique_pos = []
        for pos in p["positions"]:
            key = (pos.get("position_qid", ""), pos.get("colony_qid", ""), pos.get("start", ""))
            if key not in seen:
                seen.add(key)
                unique_pos.append(pos)
        p["positions"] = unique_pos

    merged = list(people.values())
    print(f"\n  Total unique people: {len(merged)}")
    print(f"  Total position records: {sum(len(p['positions']) for p in merged)}")
    print(f"  Total association records: {sum(len(p['associations']) for p in merged)}")

    save_json(merged, "merged_all_people.json")

    # CSV export
    csv_path = OUTPUT_DIR / "merged_all_people.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["person_qid", "person_name", "description", "type",
                         "position_qid", "position_label", "colony_qid", "colony_name",
                         "start", "end", "association", "sources"])
        for p in merged:
            sources = ";".join(p["sources"])
            if p["positions"]:
                for pos in p["positions"]:
                    writer.writerow([
                        p["qid"], p["name"], p.get("description", ""), "position",
                        pos.get("position_qid", ""), pos.get("position_label", ""),
                        pos.get("colony_qid", ""), pos.get("colony_name", ""),
                        pos.get("start", ""), pos.get("end", ""), "", sources,
                    ])
            if p["associations"]:
                for assoc in p["associations"]:
                    writer.writerow([
                        p["qid"], p["name"], p.get("description", ""), "association",
                        "", "", assoc.get("colony_qid", ""), assoc.get("colony_name", ""),
                        assoc.get("birth", ""), assoc.get("death", ""),
                        assoc.get("association", ""), sources,
                    ])
            if not p["positions"] and not p["associations"]:
                writer.writerow([p["qid"], p["name"], p.get("description", ""), "other",
                                 "", "", "", "", "", "", "", sources])

    print(f"  Saved {csv_path}")
    return merged


# ── Generate Cypher ─────────────────────────────────────────────────────────

def generate_cypher():
    """Generate Cypher statements to load all harvested people into Neo4j."""
    merged_path = OUTPUT_DIR / "merged_all_people.json"
    if not merged_path.exists():
        print("  Run merge first")
        return

    with open(merged_path) as f:
        people = json.load(f)

    cypher_path = OUTPUT_DIR / "load_wikidata_people.cypher"

    def esc(s):
        return s.replace("\\", "\\\\").replace('"', '\\"') if s else ""

    with open(cypher_path, "w") as f:
        f.write("// Wikidata people associated with British colonies — auto-generated\n")
        f.write("// Run after col_build_kg.py has created COL_Territory nodes\n\n")

        f.write("CREATE CONSTRAINT wd_person_qid IF NOT EXISTS FOR (p:WD_Person) REQUIRE p.qid IS UNIQUE;\n")
        f.write("CREATE CONSTRAINT wd_position_qid IF NOT EXISTS FOR (p:WD_Position) REQUIRE p.qid IS UNIQUE;\n\n")

        for person in people:
            qid = person["qid"]
            name = esc(person.get("name", ""))
            desc = esc(person.get("description", ""))
            sources = ";".join(person.get("sources", []))

            f.write(f'MERGE (p:WD_Person {{qid: "{qid}"}})\n')
            f.write(f'SET p.name = "{name}", p.description = "{desc}", p.sources = "{sources}";\n\n')

            for pos in person.get("positions", []):
                pos_qid = pos.get("position_qid", "")
                if not pos_qid:
                    continue
                pos_label = esc(pos.get("position_label", ""))
                colony_qid = pos.get("colony_qid", "")
                start = pos.get("start", "")
                end = pos.get("end", "")

                f.write(f'MERGE (pos:WD_Position {{qid: "{pos_qid}"}})\n')
                f.write(f'SET pos.label = "{pos_label}";\n')
                f.write(f'MERGE (p:WD_Person {{qid: "{qid}"}})\n')
                f.write(f'MERGE (pos:WD_Position {{qid: "{pos_qid}"}})\n')
                f.write(f'MERGE (p)-[r:HELD_POSITION]->(pos)\n')
                props = []
                if start: props.append(f'start: "{start}"')
                if end: props.append(f'end: "{end}"')
                if colony_qid: props.append(f'colony_qid: "{colony_qid}"')
                if props:
                    f.write(f'SET r += {{{", ".join(props)}}};\n')
                f.write("\n")

                if colony_qid:
                    f.write(f'MATCH (t:COL_Territory {{wikidata_id: "{colony_qid}"}})\n')
                    f.write(f'MATCH (pos:WD_Position {{qid: "{pos_qid}"}})\n')
                    f.write(f'MERGE (pos)-[:POSITION_IN]->(t);\n\n')

            for assoc in person.get("associations", []):
                colony_qid = assoc.get("colony_qid", "")
                if not colony_qid:
                    continue
                assoc_type = esc(assoc.get("association", "unknown"))

                f.write(f'MATCH (t:COL_Territory {{wikidata_id: "{colony_qid}"}})\n')
                f.write(f'MATCH (p:WD_Person {{qid: "{qid}"}})\n')
                f.write(f'MERGE (p)-[r:ASSOCIATED_WITH]->(t)\n')
                f.write(f'SET r.type = "{assoc_type}";\n\n')

    print(f"  Generated {cypher_path}")


# ── Main ────────────────────────────────────────────────────────────────────

STRATEGIES = {
    "positions": harvest_positions_all_colonies,
    "holders": harvest_holders,
    "colonial-office": harvest_colonial_office_employees,
    "governor-tree": harvest_governor_tree,
    "direct-p39": harvest_direct_p39_colony,
    "associated": harvest_associated_people,
    "honours": harvest_honours,
    "merge": merge_all_results,
    "cypher": generate_cypher,
}


def main():
    parser = argparse.ArgumentParser(description="Harvest colonial-era people from Wikidata")
    parser.add_argument("--strategy", default="all",
                        choices=list(STRATEGIES.keys()) + ["all", "snowball", "quick"],
                        help="Which strategy to run")
    parser.add_argument("--inspect", metavar="QID", help="Inspect a single Wikidata entity")
    parser.add_argument("--seeds", nargs="+", default=["Q2577822"],
                        help="Seed QIDs for snowball strategy")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)

    if args.inspect:
        inspect_entity(args.inspect)
        return

    if args.strategy == "snowball":
        harvest_snowball(args.seeds)
        return

    if args.strategy == "quick":
        # Quick run: just colonial office + direct P39 + merge
        harvest_colonial_office_employees()
        harvest_direct_p39_colony()
        merge_all_results()
        return

    if args.strategy == "all":
        harvest_colonial_office_employees()
        harvest_direct_p39_colony()
        harvest_positions_all_colonies()
        harvest_holders()
        harvest_governor_tree()
        harvest_honours()
        harvest_associated_people()
        harvest_snowball(args.seeds)
        merge_all_results()
        generate_cypher()
        return

    # Run single strategy
    STRATEGIES[args.strategy]()


if __name__ == "__main__":
    main()

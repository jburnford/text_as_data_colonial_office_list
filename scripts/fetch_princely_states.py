"""
Fetch Princely States of British India from Wikidata
=====================================================

Queries Wikidata SPARQL for instances of Q1336152 (princely state of India)
and supplements with major states that Wikidata classifies differently
(e.g. as "historical country").

Outputs: princely_states_wikidata.json

Usage:
    python scripts/fetch_princely_states.py
"""

import json
import re
import time
import urllib.request
import urllib.parse
from pathlib import Path

SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"

SPARQL_QUERY = """
SELECT ?item ?itemLabel ?inception ?dissolution ?lat ?lon
       ?replacedByLabel ?replacedBy ?capital ?capitalLabel
       ?population ?countryLabel
WHERE {
  ?item wdt:P31 wd:Q1336152 .   # instance of: princely state of India

  OPTIONAL { ?item wdt:P571 ?inception . }
  OPTIONAL { ?item wdt:P576 ?dissolution . }
  OPTIONAL {
    ?item p:P625 ?coordStmt .
    ?coordStmt ps:P625 ?coord .
    BIND(geof:latitude(?coord) AS ?lat)
    BIND(geof:longitude(?coord) AS ?lon)
  }
  OPTIONAL { ?item wdt:P1366 ?replacedBy . }
  OPTIONAL { ?item wdt:P36 ?capital . }
  OPTIONAL { ?item wdt:P1082 ?population . }
  OPTIONAL { ?item wdt:P17 ?country . }

  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
}
"""

# Major princely states that Wikidata may classify as "historical country" (Q3024240)
# or other types instead of Q1336152. We add them manually.
MANUAL_SUPPLEMENTS = [
    # QIDs verified via Wikidata API (wbgetentities) or SPARQL label lookup.
    # Only states NOT returned by the Q1336152 SPARQL query are listed here.
    #
    # VERIFIED: Q1240096 = "Hyderabad State" (P31: princely state, historical country)
    {"qid": "Q1240096", "name": "Hyderabad State", "inception": 1724, "dissolution": 1948,
     "agency": "Deccan", "successor": "india"},
    # VERIFIED: Q266923 = "Kingdom of Mysore" (P31: kingdom, princely state, vassal state, historical country)
    {"qid": "Q266923", "name": "Kingdom of Mysore", "inception": 1399, "dissolution": 1950,
     "agency": "Madras", "successor": "india"},
    # VERIFIED: Q808575 = "Baroda State" (P31: princely state, historical country)
    {"qid": "Q808575", "name": "Baroda State", "inception": 1721, "dissolution": 1949,
     "agency": "Western India", "successor": "india"},
    # VERIFIED: Q2571484 = "Jammu and Kashmir" princely state (P31: princely state)
    {"qid": "Q2571484", "name": "Jammu and Kashmir", "inception": 1846, "dissolution": 1952,
     "agency": "Punjab", "successor": "india"},
    # VERIFIED: Q1557792 = "Gwalior State" (P31: princely state, historical country)
    {"qid": "Q1557792", "name": "Gwalior State", "inception": 1731, "dissolution": 1948,
     "agency": "Central India", "successor": "india"},
    # VERIFIED: Q716890 = "Indore State" (P31: princely state, historical country)
    {"qid": "Q716890", "name": "Indore State", "inception": 1731, "dissolution": 1948,
     "agency": "Central India", "successor": "india"},
    # VERIFIED: Q150058 = "Kingdom of Thiruvithamkoor" / Travancore (P31: Q3024240, Q1336152)
    {"qid": "Q150058", "name": "Travancore", "inception": 1729, "dissolution": 1949,
     "agency": "Madras", "successor": "india"},
    # VERIFIED: Q150056 = "Kingdom of Cochin" (P31: princely state, historical country)
    {"qid": "Q150056", "name": "Kingdom of Cochin", "inception": 1503, "dissolution": 1949,
     "agency": "Madras", "successor": "india"},
    # VERIFIED: Q6124144 = "Jaipur State" (P31: Q1336152, Q417175, Q3024240)
    {"qid": "Q6124144", "name": "Jaipur State", "inception": 1727, "dissolution": 1949,
     "agency": "Rajputana", "successor": "india"},
    # VERIFIED: Q6207845 = "Jodhpur State" (P31: Q3624078, Q1371288, Q3024240, Q1336152)
    {"qid": "Q6207845", "name": "Jodhpur State", "inception": 1226, "dissolution": 1949,
     "agency": "Rajputana", "successor": "india"},
    # VERIFIED: Q3960459 = "Kingdom of Sikkim" (P31: protectorate, historical country)
    {"qid": "Q3960459", "name": "Kingdom of Sikkim", "inception": 1642, "dissolution": 1975,
     "agency": "Bengal", "successor": "india"},
]

# Well-known salute states for scoring (salute guns → list of QIDs)
# Salute gun ranks — QIDs verified via Wikidata API
SALUTE_GUNS = {
    21: ["Q1240096", "Q266923", "Q808575", "Q2571484", "Q1557792"],
    19: ["Q716890", "Q150058"],
    17: ["Q150056", "Q855044", "Q657946", "Q6124144", "Q6207845"],
    15: ["Q3960459", "Q917553"],
}

# Major states to include in visualization (by QID)
# ~25-30 states covering all agencies
# Major states for visualization — QIDs verified via Wikidata API or SPARQL
MAJOR_STATES_QIDS = {
    # 21-gun salute (verified manual supplements)
    "Q1240096",  # Hyderabad State
    "Q266923",   # Kingdom of Mysore
    "Q808575",   # Baroda State
    "Q2571484",  # Jammu and Kashmir (princely state)
    "Q1557792",  # Gwalior State
    # 19-gun (verified)
    "Q716890",   # Indore State
    "Q150058",   # Travancore (Kingdom of Thiruvithamkoor)
    # Rajputana Agency (verified via SPARQL label + API)
    "Q6124144",  # Jaipur State (verified via API)
    "Q6207845",  # Jodhpur State (verified via API)
    "Q1457519",  # Udaipur State (in SPARQL results)
    "Q859966",   # Bikaner State (in SPARQL results)
    # Central India (in SPARQL results)
    "Q855044",   # Bhopal State
    # Western India (in SPARQL results)
    "Q1720882",  # Cutch State
    "Q14491604", # Junagadh State
    # Southern (verified)
    "Q150056",   # Kingdom of Cochin
    # Punjab (in SPARQL results)
    "Q917553",   # Patiala State
    "Q1728782",  # Kapurthala State
    # Eastern (in SPARQL results)
    "Q17342164", # Tripura
    "Q509572",   # Cooch Behar
    # Sikkim (verified)
    "Q3960459",  # Kingdom of Sikkim
    # Pakistan (in SPARQL results)
    "Q800236",   # Bahawalpur State
    "Q3249587",  # Khairpur State
    "Q139948",   # Khanate of Kalat
    # Others (in SPARQL results)
    "Q657946",   # Kolhapur State
    "Q176466",   # Rewa State
}


def sparql_query(query):
    """Execute a SPARQL query against Wikidata."""
    params = urllib.parse.urlencode({
        "query": query,
        "format": "json",
    })
    url = f"{SPARQL_ENDPOINT}?{params}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "BritishEmpireKG/1.0 (research project; mailto:jic823@usask.ca)",
        "Accept": "application/sparql-results+json",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def extract_year(date_str):
    """Extract year from an ISO date or datetime string."""
    if not date_str:
        return None
    m = re.match(r'[-]?(\d{4})', date_str)
    if m:
        year = int(m.group(1))
        if date_str.startswith('-'):
            year = -year
        return year
    return None


def extract_qid(uri):
    """Extract QID from a Wikidata URI."""
    if not uri:
        return None
    m = re.search(r'(Q\d+)$', uri)
    return m.group(1) if m else None


def slugify(name):
    """Convert name to snake_case slug."""
    s = name.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '_', s)
    return s.strip('_')


def make_colony_id(name, inception, dissolution):
    """Generate colony_id in the same format as existing KG nodes."""
    slug = slugify(name)
    parts = [slug]
    if inception:
        parts.append(str(inception))
    if dissolution:
        parts.append(str(dissolution))
    return '_'.join(parts)


def main():
    output_path = Path(__file__).parent.parent / "princely_states_wikidata.json"

    print("Querying Wikidata for princely states (Q1336152)...")
    result = sparql_query(SPARQL_QUERY)
    bindings = result["results"]["bindings"]
    print(f"  Got {len(bindings)} result rows")

    # Deduplicate by QID (multiple rows per state due to OPTIONAL joins)
    states = {}
    for row in bindings:
        qid = extract_qid(row.get("item", {}).get("value", ""))
        if not qid:
            continue

        if qid not in states:
            states[qid] = {
                "qid": qid,
                "name": row.get("itemLabel", {}).get("value", ""),
                "inception": None,
                "dissolution": None,
                "lat": None,
                "lon": None,
                "capital": None,
                "replaced_by": [],
                "population": None,
                "country": None,
            }

        s = states[qid]
        inception = extract_year(row.get("inception", {}).get("value"))
        if inception and (s["inception"] is None or inception < s["inception"]):
            s["inception"] = inception

        dissolution = extract_year(row.get("dissolution", {}).get("value"))
        if dissolution and (s["dissolution"] is None or dissolution > s["dissolution"]):
            s["dissolution"] = dissolution

        lat = row.get("lat", {}).get("value")
        if lat and s["lat"] is None:
            s["lat"] = float(lat)
        lon = row.get("lon", {}).get("value")
        if lon and s["lon"] is None:
            s["lon"] = float(lon)

        cap = row.get("capitalLabel", {}).get("value")
        if cap and s["capital"] is None:
            s["capital"] = cap

        pop = row.get("population", {}).get("value")
        if pop:
            try:
                p = int(float(pop))
                if s["population"] is None or p > s["population"]:
                    s["population"] = p
            except ValueError:
                pass

        replaced_by_qid = extract_qid(row.get("replacedBy", {}).get("value"))
        replaced_by_label = row.get("replacedByLabel", {}).get("value")
        if replaced_by_qid and replaced_by_qid not in [r["qid"] for r in s["replaced_by"]]:
            s["replaced_by"].append({"qid": replaced_by_qid, "name": replaced_by_label})

        country = row.get("countryLabel", {}).get("value")
        if country and s["country"] is None:
            s["country"] = country

    print(f"  Deduplicated to {len(states)} unique states")

    # Add manual supplements or merge into incomplete SPARQL entries
    added = 0
    for ms in MANUAL_SUPPLEMENTS:
        if ms["qid"] not in states:
            states[ms["qid"]] = {
                "qid": ms["qid"],
                "name": ms["name"],
                "inception": ms.get("inception"),
                "dissolution": ms.get("dissolution"),
                "lat": ms.get("lat"),
                "lon": ms.get("lon"),
                "capital": ms.get("capital"),
                "replaced_by": [],
                "population": None,
                "country": "British Raj",
                "source": "manual_supplement",
            }
            added += 1
            print(f"  Added manual supplement: {ms['name']} ({ms['qid']})")
        else:
            # Merge manual data into incomplete SPARQL entries
            s = states[ms["qid"]]
            merged = []
            if s["inception"] is None and ms.get("inception"):
                s["inception"] = ms["inception"]; merged.append("inception")
            if s["dissolution"] is None and ms.get("dissolution"):
                s["dissolution"] = ms["dissolution"]; merged.append("dissolution")
            if s["lat"] is None and ms.get("lat"):
                s["lat"] = ms["lat"]; merged.append("lat")
            if s["lon"] is None and ms.get("lon"):
                s["lon"] = ms["lon"]; merged.append("lon")
            if s["capital"] is None and ms.get("capital"):
                s["capital"] = ms["capital"]; merged.append("capital")
            # Prefer manual name if SPARQL name is generic
            if ms.get("name") and "state" in ms["name"].lower():
                s["name"] = ms["name"]; merged.append("name")
            if merged:
                print(f"  Merged manual data into SPARQL entry: {ms['name']} ({ms['qid']}) [{', '.join(merged)}]")
            else:
                print(f"  Already complete in SPARQL results: {ms['name']} ({ms['qid']})")

    if added:
        print(f"  Added {added} manual supplements")

    # Generate colony_id and classify successor state
    for qid, s in states.items():
        name = s["name"]
        inception = s["inception"]
        dissolution = s["dissolution"]
        s["colony_id"] = make_colony_id(name, inception, dissolution)
        s["is_major"] = qid in MAJOR_STATES_QIDS
        s["type"] = "Princely State"
        s["region"] = "South Asia"

        # Determine successor: India or Pakistan
        # Default to India; a few went to Pakistan
        PAKISTAN_QIDS = {
            "Q800236",   # Bahawalpur (verified in SPARQL)
            "Q3249587",  # Khairpur (verified in SPARQL)
            "Q139948",   # Kalat (verified in SPARQL)
        }
        # Also match by name for states that may have different QIDs
        PAKISTAN_NAMES = {"las bela", "makran", "kharan", "amb", "dir", "swat", "chitral"}
        name_slug = slugify(name).replace('_state', '').replace('_', ' ').strip()
        if name_slug in PAKISTAN_NAMES:
            s["successor"] = "pakistan"
        s["successor"] = "pakistan" if qid in PAKISTAN_QIDS else "india"

    # Summary stats
    major = [s for s in states.values() if s["is_major"]]
    with_coords = [s for s in states.values() if s["lat"] is not None]
    with_dates = [s for s in states.values() if s["inception"] is not None]
    india = [s for s in states.values() if s["successor"] == "india"]
    pakistan = [s for s in states.values() if s["successor"] == "pakistan"]

    print(f"\nSummary:")
    print(f"  Total states:       {len(states)}")
    print(f"  Major (for viz):    {len(major)}")
    print(f"  With coordinates:   {len(with_coords)}")
    print(f"  With inception:     {len(with_dates)}")
    print(f"  → India:            {len(india)}")
    print(f"  → Pakistan:         {len(pakistan)}")

    # Save
    output = {
        "metadata": {
            "source": "Wikidata SPARQL + manual supplements",
            "query_class": "Q1336152 (princely state of India)",
            "total_states": len(states),
            "major_states": len(major),
        },
        "states": list(states.values()),
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nSaved to {output_path}")

    # Print major states for viz reference
    print(f"\n{'='*60}")
    print("Major states for visualization:")
    print(f"{'='*60}")
    for s in sorted(major, key=lambda x: x["name"]):
        guns = ""
        for g, qids in SALUTE_GUNS.items():
            if s["qid"] in qids:
                guns = f" ({g}-gun)"
                break
        print(f"  {s['name']:<30} {s['colony_id']:<45} {s['qid']}{guns}")


if __name__ == "__main__":
    main()

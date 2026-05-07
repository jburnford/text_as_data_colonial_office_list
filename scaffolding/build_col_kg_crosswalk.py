#!/usr/bin/env python3
"""
Build a crosswalk mapping COL extraction colony names to KG HistoricalTerritory nodes.

Reads:
  - britishempire_kg_export.cypher (source of truth for territory nodes and QIDs)
  - scaffolding/colony_alignment.csv (verified mappings)
  - generated/*_data_*.json (source of COL colony names + years)

Writes:
  - scaffolding/col_kg_crosswalk.json
  - scaffolding/col_kg_crosswalk.csv
"""

import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KG_EXPORT = ROOT / "britishempire_kg_export.cypher"
ALIGNMENT_CSV = ROOT / "scaffolding" / "colony_alignment.csv"
GENERATED_DIR = ROOT / "generated"
OUT_JSON = ROOT / "scaffolding" / "col_kg_crosswalk.json"
OUT_CSV = ROOT / "scaffolding" / "col_kg_crosswalk.csv"


# ── Step 1: Parse KG export ──────────────────────────────────────────────────

def parse_kg_export(path: Path) -> dict:
    """Extract all territory nodes from the cypher file.
    Returns dict keyed by colony_id with fields:
      canonical_name, wikidata_id, established_year, independence_year,
      administrative_status
    """
    territories = {}
    # Also build a reverse index: wikidata_id → [colony_id, ...]
    qid_to_ids = defaultdict(list)

    text = path.read_text()
    # Each node block starts with MERGE ... {colony_id: '...'})
    # and is followed by SET c += { ... };
    # Parse SET blocks
    blocks = re.split(r"MERGE \(c:HistoricalTerritory[^{]*\{colony_id: '([^']+)'\}\)", text)
    # blocks[0] is preamble, then alternating: colony_id, rest_until_next_merge
    for i in range(1, len(blocks), 2):
        colony_id = blocks[i]
        body = blocks[i + 1] if i + 1 < len(blocks) else ""

        def extract(field):
            m = re.search(rf"{field}: '([^']*)'", body)
            return m.group(1) if m else None

        def extract_int(field):
            m = re.search(rf"{field}: (\d+)", body)
            return int(m.group(1)) if m else None

        t = {
            "colony_id": colony_id,
            "canonical_name": extract("canonical_name") or extract("name"),
            "wikidata_id": extract("wikidata_id"),
            "established_year": extract_int("established_year"),
            "independence_year": extract_int("independence_year"),
            "administrative_status": extract("administrative_status"),
        }
        territories[colony_id] = t
        if t["wikidata_id"]:
            qid_to_ids[t["wikidata_id"]].append(colony_id)

    # Build name-based index: canonical_name → [colony_id, ...]
    name_to_ids = defaultdict(list)
    for cid, t in territories.items():
        if t["canonical_name"]:
            name_to_ids[t["canonical_name"]].append(cid)

    return territories, qid_to_ids, name_to_ids


# ── Step 2: Parse extraction files ───────────────────────────────────────────

def get_col_names_and_years(generated_dir: Path) -> dict:
    """Scan generated/*_data_*.json files.
    Returns dict: col_name → sorted list of years.
    The col_name is derived from the JSON 'colony' field.
    """
    col_years = defaultdict(set)
    for f in generated_dir.glob("*_data_*.json"):
        # Extract from filename: {colony}_{year}_data_{model}.json
        stem = f.stem  # e.g. "aden_1922_data_gpt-oss_120b"
        m = re.match(r"(.+?)_(\d{4})_data_", stem)
        if not m:
            continue
        year = int(m.group(2))
        # Get colony name from inside the JSON for accuracy
        try:
            with open(f) as fh:
                data = json.load(fh)
            col_name = data.get("colony", m.group(1))
        except (json.JSONDecodeError, KeyError):
            col_name = m.group(1)
        col_years[col_name].add(year)

    return {k: sorted(v) for k, v in col_years.items()}


# ── Step 3: Load alignment CSV ───────────────────────────────────────────────

def load_alignment_csv(path: Path) -> dict:
    """Read colony_alignment.csv.
    Returns dict: extraction_name → {kg_name, wikidata_qid, match_status, notes}
    """
    rows = {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["extraction_name"].strip()
            if not name:
                continue
            rows[name] = {
                "kg_name": row.get("kg_name", "").strip(),
                "wikidata_qid": row.get("wikidata_qid", "").strip(),
                "match_status": row.get("match_status", "").strip(),
                "notes": row.get("notes", "").strip(),
            }
    return rows


# ── Step 4 & 5: Build crosswalk ──────────────────────────────────────────────

# Tier 2: Alias resolution — COL names not in CSV but with clear KG equivalents
ALIASES = {
    "British Somaliland": "Somaliland",
    "Federation of Rhodesia and Nyasaland": "Rhodesia and Nyasaland",
    "Weihaiwei": "Wei-hai-Wei",
    "West Africa Settlements": "West African Settlements",
}

# When CSV kg_name differs from KG canonical_name, map to the correct KG name
KG_NAME_FIXES = {
    "Lagos Protectorate": "Lagos Colony",      # KG node colony_id='lagos_protectorate_1887_1906' has canonical_name='Lagos Colony'
    "New Zealand": "New Zealand Colony",        # CSV 'New Zealand' should map to colony, not independent nation
}

# Tier 2 special: British Central Africa maps directly to KG node
DIRECT_KG_MATCHES = {
    "British Central Africa": {
        "colony_id": "british_central_africa_protectorate_1891_1907",
        "qid": "Q2642989",
    },
}

# Tier 3: Resolved ambiguous cases (dual mappings)
DUAL_MAPPINGS = {
    "Niger Protectorate": [
        {
            "colony_id": "oil_rivers_protectorate_1885_1893",
            "qid": "Q2566427",
            "note": "Oil Rivers Protectorate — part of combined COL heading",
        },
        {
            "colony_id": "royal_niger_company_territory_1886_1900",
            "qid": "Q1806380",
            "note": "Royal Niger Company Territory — part of combined COL heading",
        },
    ],
    "British East Africa and Zanzibar": [
        {
            "colony_id": "east_africa_protectorate_1895_1920",
            "qid": "Q876185",
            "note": "East Africa Protectorate — part of combined COL heading",
        },
        {
            "colony_id": "zanzibar_1890_1963",
            "qid": "Q3574782",
            "note": "Zanzibar — part of combined COL heading",
        },
    ],
    "Mesopotamia": [
        {
            "colony_id": "mandatory_iraq_1920_1932",
            "qid": "Q146720",
            "note": "COL year 1921 falls within Mandatory Iraq period (1920-1932)",
        },
    ],
}

# Step 5: Temporal splits — COL names spanning multiple KG entities
TEMPORAL_SPLITS = {
    "Aden": [
        {
            "colony_id": "aden_1839_1963",
            "qid": "Q17509767",
            "year_start": 1922,
            "year_end": 1936,
            "note": "Aden Province (pre-separation)",
        },
        {
            "colony_id": "aden_colony_1937_1967",
            "qid": "Q49910",
            "year_start": 1937,
            "year_end": 9999,
            "note": "Aden Colony (post-separation)",
        },
    ],
    "Newfoundland": [
        {
            "colony_id": "colony_of_newfoundland_1610_1949",
            "qid": "Q2984260",
            "year_start": 1867,
            "year_end": 1906,
            "note": "Colony of Newfoundland",
        },
        {
            "colony_id": "dominion_of_newfoundland_1907_1934",
            "qid": "Q38610",
            "year_start": 1907,
            "year_end": 9999,
            "note": "Dominion of Newfoundland",
        },
    ],
    "Kenya": [
        {
            "colony_id": "east_africa_protectorate_1895_1920",
            "qid": "Q876185",
            "year_start": 1908,
            "year_end": 1919,
            "note": "East Africa Protectorate (pre-1920)",
        },
        {
            "colony_id": "kenya_colony_and_protectorate_of_1920_1963",
            "qid": "Q2538511",
            "year_start": 1920,
            "year_end": 9999,
            "note": "Kenya Colony and Protectorate",
        },
    ],
    "North Borneo": [
        {
            "colony_id": "british_north_borneo_1882_1946",
            "qid": "Q1147441",
            "year_start": 1890,
            "year_end": 1945,
            "note": "British North Borneo (Company territory)",
        },
        {
            "colony_id": "north_borneo_crown_colony_1946_1963",
            "qid": "Q16933920",
            "year_start": 1946,
            "year_end": 9999,
            "note": "North Borneo Crown Colony",
        },
    ],
    "Sarawak": [
        {
            "colony_id": "sarawak_1841_1946",
            "qid": "Q1658411",
            "year_start": 1890,
            "year_end": 1945,
            "note": "Sarawak (Brooke family rule)",
        },
        {
            "colony_id": "sarawak_crown_colony_1946_1963",
            "qid": "Q5589708",
            "year_start": 1946,
            "year_end": 9999,
            "note": "Sarawak Crown Colony",
        },
    ],
}


def find_colony_id_by_qid(qid: str, qid_to_ids: dict, territories: dict) -> str | None:
    """Find the colony_id for a given QID. If multiple, prefer the one
    whose canonical_name best matches."""
    ids = qid_to_ids.get(qid, [])
    if len(ids) == 1:
        return ids[0]
    if len(ids) == 0:
        return None
    # Multiple — return the first one (they should be disambiguated by caller)
    return ids[0]


def build_crosswalk(territories, qid_to_ids, name_to_ids, col_years, alignment):
    """Build the crosswalk entries."""
    crosswalk = {}
    errors = []
    warnings = []

    for col_name, years in sorted(col_years.items()):
        year_min, year_max = min(years), max(years)

        # ── Check temporal splits first (Step 5) ──
        if col_name in TEMPORAL_SPLITS:
            mappings = []
            for split in TEMPORAL_SPLITS[col_name]:
                # Verify QID exists in KG
                if split["colony_id"] not in territories:
                    errors.append(f"TEMPORAL SPLIT: colony_id '{split['colony_id']}' not in KG for '{col_name}'")
                    continue
                kg_node = territories[split["colony_id"]]
                if kg_node["wikidata_id"] != split["qid"]:
                    errors.append(
                        f"TEMPORAL SPLIT QID MISMATCH: '{col_name}' split to '{split['colony_id']}' "
                        f"has QID {kg_node['wikidata_id']} in KG but {split['qid']} in config"
                    )
                    continue
                # Determine actual year range from COL data
                split_years = [y for y in years if split["year_start"] <= y <= split["year_end"]]
                if not split_years:
                    continue  # No COL data in this split period
                mappings.append({
                    "colony_id": split["colony_id"],
                    "canonical_name": kg_node["canonical_name"],
                    "wikidata_id": split["qid"],
                    "year_start": min(split_years),
                    "year_end": max(split_years),
                    "confidence": "verified",
                    "note": split["note"],
                })
            crosswalk[col_name] = {
                "col_name": col_name,
                "col_year_min": year_min,
                "col_year_max": year_max,
                "col_year_count": len(years),
                "mappings": mappings,
                "has_temporal_split": True,
            }
            continue

        # ── Check dual mappings (Tier 3) ──
        if col_name in DUAL_MAPPINGS:
            mappings = []
            for dm in DUAL_MAPPINGS[col_name]:
                if dm["colony_id"] not in territories:
                    errors.append(f"DUAL MAPPING: colony_id '{dm['colony_id']}' not in KG for '{col_name}'")
                    continue
                kg_node = territories[dm["colony_id"]]
                if kg_node["wikidata_id"] != dm["qid"]:
                    errors.append(
                        f"DUAL MAPPING QID MISMATCH: '{col_name}' → '{dm['colony_id']}' "
                        f"has QID {kg_node['wikidata_id']} in KG but {dm['qid']} in config"
                    )
                    continue
                mappings.append({
                    "colony_id": dm["colony_id"],
                    "canonical_name": kg_node["canonical_name"],
                    "wikidata_id": dm["qid"],
                    "year_start": year_min,
                    "year_end": year_max,
                    "confidence": "verified",
                    "note": dm["note"],
                })
            crosswalk[col_name] = {
                "col_name": col_name,
                "col_year_min": year_min,
                "col_year_max": year_max,
                "col_year_count": len(years),
                "mappings": mappings,
                "has_temporal_split": False,
            }
            continue

        # ── Check direct KG matches (Tier 2 special) ──
        if col_name in DIRECT_KG_MATCHES:
            dkm = DIRECT_KG_MATCHES[col_name]
            if dkm["colony_id"] not in territories:
                errors.append(f"DIRECT KG MATCH: colony_id '{dkm['colony_id']}' not in KG for '{col_name}'")
                continue
            kg_node = territories[dkm["colony_id"]]
            if kg_node["wikidata_id"] != dkm["qid"]:
                errors.append(
                    f"DIRECT KG QID MISMATCH: '{col_name}' → '{dkm['colony_id']}' "
                    f"has QID {kg_node['wikidata_id']} in KG but {dkm['qid']} in config"
                )
                continue
            crosswalk[col_name] = {
                "col_name": col_name,
                "col_year_min": year_min,
                "col_year_max": year_max,
                "col_year_count": len(years),
                "mappings": [{
                    "colony_id": dkm["colony_id"],
                    "canonical_name": kg_node["canonical_name"],
                    "wikidata_id": dkm["qid"],
                    "year_start": year_min,
                    "year_end": year_max,
                    "confidence": "verified",
                    "note": "Direct KG match (Tier 2)",
                }],
                "has_temporal_split": False,
            }
            continue

        # ── Resolve aliases (Tier 2) ──
        lookup_name = ALIASES.get(col_name, col_name)

        # ── CSV lookup (Tier 1) ──
        if lookup_name in alignment:
            aln = alignment[lookup_name]
            if aln["match_status"] == "no_kg_node":
                crosswalk[col_name] = {
                    "col_name": col_name,
                    "col_year_min": year_min,
                    "col_year_max": year_max,
                    "col_year_count": len(years),
                    "mappings": [{
                        "colony_id": None,
                        "canonical_name": None,
                        "wikidata_id": None,
                        "year_start": year_min,
                        "year_end": year_max,
                        "confidence": "no_kg_node",
                        "note": aln["notes"] or f"No KG node for {col_name}",
                    }],
                    "has_temporal_split": False,
                }
                continue

            csv_qid = aln["wikidata_qid"]
            kg_name = aln["kg_name"]
            # Find colony_id from KG by QID first, then by name
            candidate_ids = qid_to_ids.get(csv_qid, [])

            colony_id = None
            if candidate_ids:
                # Pick the best candidate — prefer one whose canonical_name matches CSV kg_name
                for cid in candidate_ids:
                    if territories[cid]["canonical_name"] == kg_name:
                        colony_id = cid
                        break
                if colony_id is None:
                    colony_id = candidate_ids[0]
            else:
                # QID from CSV not in KG — fallback to name matching
                # CSV often has modern-nation QIDs; KG has historical-territory QIDs
                lookup_kg_name = KG_NAME_FIXES.get(kg_name, kg_name)
                name_candidates = name_to_ids.get(lookup_kg_name, [])
                if name_candidates:
                    colony_id = name_candidates[0]
                    warnings.append(
                        f"CSV QID {csv_qid} for '{col_name}' not in KG; "
                        f"matched by name '{lookup_kg_name}' → '{colony_id}' "
                        f"(KG QID: {territories[colony_id]['wikidata_id']})"
                    )
                else:
                    errors.append(
                        f"'{col_name}': CSV QID {csv_qid} not in KG and "
                        f"name '{kg_name}' (fixed: '{lookup_kg_name}') not found either"
                    )
                    continue

            kg_node = territories[colony_id]

            alias_note = f"Alias: '{col_name}' → '{lookup_name}'" if col_name != lookup_name else ""

            crosswalk[col_name] = {
                "col_name": col_name,
                "col_year_min": year_min,
                "col_year_max": year_max,
                "col_year_count": len(years),
                "mappings": [{
                    "colony_id": colony_id,
                    "canonical_name": kg_node["canonical_name"],
                    "wikidata_id": kg_node["wikidata_id"],
                    "year_start": year_min,
                    "year_end": year_max,
                    "confidence": "verified",
                    "note": alias_note,
                }],
                "has_temporal_split": False,
            }
        else:
            errors.append(f"UNMATCHED: '{col_name}' (alias lookup: '{lookup_name}') not in alignment CSV")

    return crosswalk, errors, warnings


# ── Step 6: Verification ─────────────────────────────────────────────────────

def verify_crosswalk(crosswalk, territories, col_years, alignment, qid_to_ids):
    """Run verification checks."""
    errors = []

    # Check 1: Every QID in output exists in the parsed KG export
    all_kg_qids = {t["wikidata_id"] for t in territories.values() if t["wikidata_id"]}
    for col_name, entry in crosswalk.items():
        for m in entry["mappings"]:
            if m["wikidata_id"] and m["wikidata_id"] not in all_kg_qids:
                errors.append(f"VERIFY: QID {m['wikidata_id']} for '{col_name}' not in KG export")

    # Check 2: Every (col_name, year) pair is covered by exactly one mapping
    for col_name, years in col_years.items():
        if col_name not in crosswalk:
            errors.append(f"VERIFY: COL name '{col_name}' has no crosswalk entry")
            continue
        entry = crosswalk[col_name]
        for year in years:
            covering = [
                m for m in entry["mappings"]
                if m["year_start"] <= year <= m["year_end"]
            ]
            if len(covering) == 0:
                errors.append(f"VERIFY: ({col_name}, {year}) not covered by any mapping")
            elif len(covering) > 1 and entry["has_temporal_split"]:
                errors.append(f"VERIFY: ({col_name}, {year}) covered by {len(covering)} temporal split mappings (overlap)")

    # Check 3: No temporal split has overlapping year ranges
    for col_name, entry in crosswalk.items():
        if entry["has_temporal_split"] and len(entry["mappings"]) > 1:
            sorted_maps = sorted(entry["mappings"], key=lambda m: m["year_start"])
            for i in range(len(sorted_maps) - 1):
                if sorted_maps[i]["year_end"] >= sorted_maps[i + 1]["year_start"]:
                    errors.append(
                        f"VERIFY: Temporal split overlap for '{col_name}': "
                        f"{sorted_maps[i]['year_end']} >= {sorted_maps[i+1]['year_start']}"
                    )

    # Check 4: Cross-check verified CSV matches — output QID matches CSV QID
    # Note: CSV often has modern-nation QIDs while KG has historical-territory QIDs.
    # When name-matched, the QID difference is expected — only flag as info, not error.
    for col_name, entry in crosswalk.items():
        lookup_name = ALIASES.get(col_name, col_name)
        if lookup_name in alignment:
            aln = alignment[lookup_name]
            if aln["match_status"] == "verified" and aln["wikidata_qid"]:
                # Only check non-split, non-dual entries
                if not entry["has_temporal_split"] and col_name not in DUAL_MAPPINGS:
                    csv_qid = aln["wikidata_qid"]
                    for m in entry["mappings"]:
                        if m["wikidata_id"] and m["wikidata_id"] != csv_qid:
                            # Check if this was a name-matched entry (CSV QID not in KG)
                            if csv_qid not in {t["wikidata_id"] for t in territories.values() if t["wikidata_id"]}:
                                pass  # Expected: CSV used modern-nation QID
                            else:
                                errors.append(
                                    f"VERIFY: CSV QID mismatch for '{col_name}': "
                                    f"CSV={csv_qid}, output={m['wikidata_id']}"
                                )

    return errors


# ── Step 7: Write outputs ────────────────────────────────────────────────────

def write_json(crosswalk, path):
    with open(path, "w") as f:
        json.dump(crosswalk, f, indent=2, ensure_ascii=False)
    print(f"  Written: {path}")


def write_csv(crosswalk, path):
    rows = []
    for col_name, entry in sorted(crosswalk.items()):
        for m in entry["mappings"]:
            rows.append({
                "col_name": col_name,
                "col_year_min": entry["col_year_min"],
                "col_year_max": entry["col_year_max"],
                "col_year_count": entry["col_year_count"],
                "colony_id": m["colony_id"] or "",
                "canonical_name": m["canonical_name"] or "",
                "wikidata_id": m["wikidata_id"] or "",
                "year_start": m["year_start"],
                "year_end": m["year_end"],
                "confidence": m["confidence"],
                "has_temporal_split": entry["has_temporal_split"],
                "note": m["note"],
            })

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "col_name", "col_year_min", "col_year_max", "col_year_count",
            "colony_id", "canonical_name", "wikidata_id",
            "year_start", "year_end", "confidence", "has_temporal_split", "note",
        ])
        writer.writeheader()
        writer.writerows(rows)
    print(f"  Written: {path}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=== COL-to-KG Colony Crosswalk Builder ===\n")

    # Step 1
    print("Step 1: Parsing KG export...")
    territories, qid_to_ids, name_to_ids = parse_kg_export(KG_EXPORT)
    print(f"  {len(territories)} territory nodes parsed")
    print(f"  {len(qid_to_ids)} unique QIDs")

    # Step 2
    print("\nStep 2: Scanning extraction files...")
    col_years = get_col_names_and_years(GENERATED_DIR)
    print(f"  {len(col_years)} unique COL colony names")
    total_files = sum(len(v) for v in col_years.values())
    print(f"  {total_files} total extraction files")

    # Step 3
    print("\nStep 3: Loading alignment CSV...")
    alignment = load_alignment_csv(ALIGNMENT_CSV)
    print(f"  {len(alignment)} entries loaded")

    # Step 4 & 5
    print("\nStep 4-5: Building crosswalk...")
    crosswalk, build_errors, build_warnings = build_crosswalk(
        territories, qid_to_ids, name_to_ids, col_years, alignment
    )

    if build_warnings:
        print(f"\n  WARNINGS ({len(build_warnings)}):")
        for w in build_warnings:
            print(f"    ⚠ {w}")

    if build_errors:
        print(f"\n  BUILD ERRORS ({len(build_errors)}):")
        for e in build_errors:
            print(f"    ✗ {e}")

    # Step 6
    print("\nStep 6: Verification...")
    verify_errors = verify_crosswalk(crosswalk, territories, col_years, alignment, qid_to_ids)
    if verify_errors:
        print(f"\n  VERIFICATION ERRORS ({len(verify_errors)}):")
        for e in verify_errors:
            print(f"    ✗ {e}")

    # Summary
    n_verified = sum(
        1 for e in crosswalk.values()
        if any(m["confidence"] == "verified" for m in e["mappings"])
    )
    n_no_kg = sum(
        1 for e in crosswalk.values()
        if any(m["confidence"] == "no_kg_node" for m in e["mappings"])
    )
    n_split = sum(1 for e in crosswalk.values() if e["has_temporal_split"])
    n_dual = sum(1 for name in crosswalk if name in DUAL_MAPPINGS)
    total_mappings = sum(len(e["mappings"]) for e in crosswalk.values())

    print(f"\n=== Summary ===")
    print(f"  COL names processed: {len(crosswalk)}")
    print(f"  Verified:            {n_verified}")
    print(f"  No KG node:          {n_no_kg}")
    print(f"  Temporal splits:     {n_split}")
    print(f"  Dual mappings:       {n_dual}")
    print(f"  Total mappings:      {total_mappings}")

    all_errors = build_errors + verify_errors
    if all_errors:
        print(f"\n  TOTAL ERRORS: {len(all_errors)}")

    # Step 7
    print("\nStep 7: Writing outputs...")
    write_json(crosswalk, OUT_JSON)
    write_csv(crosswalk, OUT_CSV)

    if all_errors:
        print(f"\nCompleted with {len(all_errors)} error(s).")
        return 1
    else:
        print("\nCompleted with 0 errors.")
        return 0


if __name__ == "__main__":
    sys.exit(main())

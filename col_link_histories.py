#!/usr/bin/env python3
"""
COL History Track (Phase D, local slice): Governor bridge + place grounding
===========================================================================

Grounds the deterministic history entity candidates (col_frame_histories.py)
WITHOUT needing Neo4j, a gold set, or an LLM — using data already on disk:

  1. **Governor bridge.** Match each history PERSON candidate against the
     personnel extraction files (generated/<colony>_<year>_data_*.json, the
     COL_Official source) for the SAME colony. A strong match (compatible given
     name) means a person *narrated about* in the history is the same individual
     *rostered* in the personnel graph — the COL_HistoricalEntity ↔ COL_Person
     bridge (`IS_HISTORICAL_SELF_OF`). Reuses col_link_wikidata's
     name parser + initials matcher, so scoring is consistent with the official
     Wikidata-linking pipeline.

  2. **Place grounding.** History PLACE candidates are gazetteer references to
     other colonies; ground each to its canonical territory slug and emit the
     cross-colony reference network (colony -> territories its history names).

  3. **To-ground queue.** Frequent PERSON candidates with NO personnel match are
     the historical figures outside the colonial service (explorers, monarchs,
     rival-empire actors) — ranked for a later Wikidata pass.

Everything stays a *claim*: a bridge is "the CO List's history of colony X names a
person matching a rostered official", recorded with the name-match strength, never
asserted as identity without review.

Outputs:
    generated/histories_grounded/<colony>.json     (candidates + bridge/ground info)
    generated/histories_grounding_report.json       (corpus summary)

Usage:
    python col_link_histories.py            # ground all, write report
    python col_link_histories.py --stats    # summary only, no write
"""

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import col_canonicalize_reports as canon
import col_link_wikidata as wd

PIPELINE_VERSION = "col_link_histories/0.1"
FRAMED_DIR = "generated/histories_framed"
OUT_DIR = "generated/histories_grounded"

RE_PERS_FILE = re.compile(r"^(?P<colony>.+?)_(?P<year>\d{4})_(?:data|quarantined)_")
RE_GOVERNOR = re.compile(
    r"governor|administrator|high\s+commissioner|commander-in-chief|"
    r"lieutenant[- ]governor|colonial\s+secretary|chief\s+commissioner", re.I)
STRONG = {"exact", "initial_compatible"}
# A name match is only a real bridge if the personnel record is temporally
# plausible for the era the history is talking about. Without this, a 19th-c.
# governor (Sir Philip Wodehouse, 1850s) spuriously matches a same-surname 1948
# official. The personnel corpus starts ~1862, so a mention dated earlier cannot
# legitimately bridge at all.
TEMPORAL_WINDOW = 15      # personnel year within +/- this of the mention's year
PERSONNEL_START = 1862


def load_personnel_index(root):
    """{colony_slug: {norm_surname: [ {surname, given, position, year} ]}}.

    Dedups across the multiple model variants per colony-year."""
    idx = defaultdict(lambda: defaultdict(list))
    seen = set()
    for f in (root / "generated").glob("*_data_*.json"):
        m = RE_PERS_FILE.match(f.name)
        if not m:
            continue
        colony, year = m.group("colony"), int(m.group("year"))
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        officials = []
        if isinstance(data, dict):
            if isinstance(data.get("officials"), list):
                officials = data["officials"]
            elif isinstance(data.get("departments"), list):
                for dep in data["departments"]:
                    officials += dep.get("officials", []) or []
        for o in officials:
            sur = (o.get("surname") or "").strip()
            if not sur:
                continue
            given = (o.get("given_names") or "").strip()
            pos = (o.get("position") or "").strip()
            k = (colony, year, o.get("canonical_name", ""), pos)
            if k in seen:
                continue
            seen.add(k)
            idx[colony][wd.normalize_surname(sur)].append(
                {"surname": sur, "given": given, "position": pos, "year": year})
    return idx


def bridge_person(surface, colony_officials, year_ref=None):
    """Best personnel match for a history person surface form, or None."""
    sur, given = wd.parse_wd_name(surface)
    if not sur:
        return None
    cands = colony_officials.get(wd.normalize_surname(sur), [])
    best, best_rank = None, -1
    grouped = defaultdict(lambda: {"years": set(), "positions": set()})
    for c in cands:
        nm = wd.initials_match(c["given"], given)
        if nm == "mismatch":
            continue
        rank = {"exact": 3, "initial_compatible": 2, "bare": 1, "partial": 1}.get(nm, 0)
        key = (c["surname"], c["given"])
        g = grouped[key]
        g["years"].add(c["year"])
        g["positions"].add(c["position"])
        g["_nm"] = nm
        g["_rank"] = max(g.get("_rank", 0), rank)
    for (sur_m, given_m), g in grouped.items():
        if g["_rank"] > best_rank:
            best_rank = g["_rank"]
            gov = any(RE_GOVERNOR.search(p) for p in g["positions"])
            best = {
                "matched_canonical": f"{sur_m}, {given_m}".strip(", "),
                "name_match": g["_nm"],
                "strong": g["_nm"] in STRONG,
                "is_governor": gov,
                "personnel_years": sorted(g["years"]),
                "positions": sorted(g["positions"])[:3],
            }
    if best is not None:
        # Temporal gate: is the personnel record plausible for the era the
        # history is describing? Anachronistic name-twins are demoted.
        if year_ref:
            delta = min(abs(y - year_ref) for y in best["personnel_years"])
            best["mention_year"] = year_ref
            best["temporal_delta"] = delta
            if year_ref < PERSONNEL_START:
                best["temporal"] = "pre_records"   # person served before COL data
            elif delta <= TEMPORAL_WINDOW:
                best["temporal"] = "consistent"
            else:
                best["temporal"] = "anachronistic"
        else:
            best["mention_year"] = None
            best["temporal_delta"] = None
            best["temporal"] = "undated"
        # A CONFIRMED bridge is strong AND temporally consistent (or, when the
        # mention is undated, left as a candidate — not asserted).
        best["confirmed"] = best["strong"] and best["temporal"] == "consistent"
    return best


def ground_colony(data, personnel_idx):
    colony = data["colony"]
    officials = personnel_idx.get(colony, {})
    place_refs = set()
    for v in data["versions"]:
        for e in v.get("entity_candidates", []):
            if e["entity_type"] == "person":
                b = bridge_person(e["surface_text"], officials,
                                  e.get("year_reference"))
                e["bridge"] = b
            elif e["entity_type"] == "place":
                slug = canon._norm(e["surface_text"])
                e["grounded_territory"] = slug
                place_refs.add(slug)
    data["referenced_territories"] = sorted(place_refs)
    return data


def main():
    ap = argparse.ArgumentParser(description="Governor bridge + place grounding")
    ap.add_argument("--stats", action="store_true", help="summary only, no write")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    framed = sorted((root / FRAMED_DIR).glob("*.json"))
    if not framed:
        print(f"no framed files in {FRAMED_DIR}/ — run col_frame_histories.py first")
        return
    print("indexing personnel extraction files ...")
    personnel_idx = load_personnel_index(root)
    n_off = sum(len(v) for d in personnel_idx.values() for v in d.values())
    print(f"  {len(personnel_idx)} colonies, {n_off} official-year records indexed")

    n_person = n_strong = n_confirmed = n_anachro = n_undated = n_pre = 0
    n_weak = n_gov_conf = 0
    n_place = 0
    place_edges = Counter()
    ungrounded = Counter()        # frequent non-matches (to-ground queue)
    gov_examples = []
    seen_gov = set()
    out_dir = root / OUT_DIR

    for f in framed:
        data = json.loads(f.read_text(encoding="utf-8"))
        data = ground_colony(data, personnel_idx)
        colony = data["colony"]
        for v in data["versions"]:
            for e in v.get("entity_candidates", []):
                if e["entity_type"] == "person":
                    n_person += 1
                    b = e.get("bridge")
                    if b and b["strong"]:
                        n_strong += 1
                        t = b["temporal"]
                        if t == "consistent":
                            n_confirmed += 1
                            if b["is_governor"]:
                                n_gov_conf += 1
                                key = (colony, b["matched_canonical"])
                                if key not in seen_gov and len(gov_examples) < 12:
                                    seen_gov.add(key)
                                    gov_examples.append(
                                        f"{colony}: {e['surface_text']!r} -> "
                                        f"{b['matched_canonical']} "
                                        f"(Δ{b['temporal_delta']}y, {b['positions'][0]})")
                        elif t == "anachronistic":
                            n_anachro += 1
                        elif t == "pre_records":
                            n_pre += 1
                        else:
                            n_undated += 1
                    elif b:
                        n_weak += 1
                    else:
                        ungrounded[e["surface_text"]] += 1
                elif e["entity_type"] == "place":
                    n_place += 1
                    place_edges[(colony, e.get("grounded_territory"))] += 1
        if not args.stats:
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / f.name).write_text(
                json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== Governor bridge (history person candidates -> personnel graph) ===")
    print(f"person candidates                      : {n_person}")
    print(f"  strong name match (same colony)      : {n_strong}")
    print(f"    CONFIRMED (temporally consistent)  : {n_confirmed} "
          f"({100*n_confirmed//n_person if n_person else 0}%)  "
          f"-- of which governors/admins: {n_gov_conf}")
    print(f"    undated mention (candidate)        : {n_undated}")
    print(f"    anachronistic name-twin (rejected) : {n_anachro}")
    print(f"    pre-1862, before records (rejected): {n_pre}")
    print(f"  weak (surname-only)                  : {n_weak}")
    print(f"  no personnel match (to-ground)       : {sum(ungrounded.values())}")
    print("  sample CONFIRMED governor bridges:")
    for ex in gov_examples:
        print(f"    {ex}")
    print(f"\n=== Place grounding ===")
    print(f"place references grounded to a territory : {n_place}")
    print(f"distinct (colony -> territory) edges     : {len(place_edges)}")
    top_ref = Counter()
    for (_, terr), n in place_edges.items():
        top_ref[terr] += 1
    print("  most-referenced territories across histories:")
    for terr, n in top_ref.most_common(8):
        print(f"    {terr:24s} referenced by {n} colonies")
    print(f"\n=== To-ground queue (frequent figures with no personnel match) ===")
    for name, n in ungrounded.most_common(15):
        print(f"  {n:3d}  {name}")

    if not args.stats:
        report = {
            "pipeline_version": PIPELINE_VERSION,
            "date_created": date.today().isoformat(),
            "person_candidates": n_person,
            "strong_name_match": n_strong,
            "confirmed_bridge": n_confirmed,
            "confirmed_governors": n_gov_conf,
            "undated_candidate": n_undated,
            "rejected_anachronistic": n_anachro,
            "rejected_pre_records": n_pre,
            "weak_bridge": n_weak,
            "unmatched": sum(ungrounded.values()),
            "place_references": n_place,
            "colony_territory_edges": len(place_edges),
            "to_ground_top": dict(ungrounded.most_common(100)),
        }
        (root / "generated" / "histories_grounding_report.json").write_text(
            json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nwrote {len(framed)} grounded colony files + grounding report")


if __name__ == "__main__":
    main()

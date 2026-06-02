#!/usr/bin/env python3
"""
COL History Track: Framing analysis by region x era (+ self-contained viz)
==========================================================================

Aggregates the deterministic framing annotations (col_frame_histories.py) into a
critical read of HOW the Colonial Office narrated its colonies — by region, by
era, and per colony over time. These are the SOURCE's framing patterns, not
historical fact (every count is "share of published histories using frame F").

Observation unit = one (colony, edition_year): each distinct history version is
expanded to the editions it was printed in, so prevalence reflects what a reader
of a given year's volume would actually encounter.

Outputs:
    generated/framing_analysis.json   (aggregates: region x frame, era x frame, per-colony timelines)
    framing_viz.html                  (self-contained; region heatmap, era trends, per-colony evolution)

Usage:
    python col_analyze_framing.py            # write JSON + HTML
    python col_analyze_framing.py --stats    # print summary only
"""

import argparse
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

FRAMED_DIR = "generated/histories_framed"
FRAMES = ["discovery", "cession_acquisition", "conflict", "civilising", "sovereignty"]

# Era buckets (edition year -> era label).
ERAS = [(1862, 1899, "1862-99 High Imperial"),
        (1900, 1918, "1900-18 Edwardian-WWI"),
        (1919, 1945, "1919-45 Interwar-WWII"),
        (1946, 1970, "1946-66 Late/Decolonisation")]


def era_of(year):
    for lo, hi, label in ERAS:
        if lo <= year <= hi:
            return label
    return "other"


# Curated colony-slug -> region map for the 116 history colonies. Region groupings
# follow the project's guides/*_guide.md. Settler colonies are split from
# non-settler Africa so the "civilising"-framing contrast is visible.
REGION = {}
def _r(region, slugs):
    for s in slugs:
        REGION[s] = region

_r("Caribbean", [
    "bahamas", "bahama_islands", "barbados", "british_guiana", "british_honduras",
    "grenada", "grena_da", "grenade", "jamaica", "leeward_islands",
    "the_leeward_islands", "montserrat", "st_lucia", "st_vincent",
    "windward_islands", "the_windward_islands", "windward_islands_grenada",
    "windward_islands_st_lucia", "windward_islands_st_vincent",
    "windward_islands_tobago", "tobago", "trinidad", "trinidad_and_tobago",
    "trinidad_tobago", "turks_and_caicos_islands", "west_indies_cayman_turks_caicos"])
_r("West Africa", [
    "gambia", "the_gambia", "gold_coast", "the_gold_coast", "gold_coast_colony",
    "the_gold_coast_colony", "lagos", "nigeria", "northern_nigeria",
    "southern_nigeria", "federation_of_nigeria", "sierra_leone"])
_r("East & Central Africa", [
    "british_central_africa_protectorate", "british_zambezia_and_british_central_africa",
    "kenya", "nyasaland", "nyasaland_protectorate", "northern_rhodesia", "rhodesia",
    "southern_rhodesia", "tanganyika", "tanganyika_territory", "uganda", "zanzibar",
    "somaliland_protectorate", "british_somaliland_protectorate", "amatongaland"])
_r("Southern Africa (settler)", [
    "basutoland", "bechuanaland", "bechuanaland_protectorate", "british_bechuanaland",
    "cape_of_good_hope", "natal", "orange_river_colony", "south_africa", "swaziland",
    "transvaal", "the_transvaal", "zululand"])
_r("South & Southeast Asia", [
    "aden", "brunei", "ceylon", "federated_malay_states", "federation_of_malaya",
    "hong_kong", "johore", "kedah", "malay_states_unfederated",
    "malaya_straits_settlements", "malaya_unfederated_malay_states",
    "unfederated_malay_states", "north_borneo", "british_north_borneo", "sarawak",
    "singapore", "singapore_and_dependencies", "straits_settlements", "weihaiwei"])
_r("Pacific", [
    "british_new_guinea", "fiji", "gilbert_and_ellice_islands", "kingdom_of_tonga",
    "tonga", "nauru", "papua", "western_pacific", "western_pacific_high_commission"])
_r("Settler Dominions", [
    "british_columbia", "canada", "dominion_of_canada", "new_brunswick",
    "new_south_wales", "newfoundland", "nova_scotia", "queensland", "south_australia",
    "tasmania", "victoria", "western_australia", "new_zealand"])
_r("Islands & Mediterranean", [
    "bermuda", "cyprus", "falkland_islands", "falkland_islands_and_dependencies",
    "gibraltar", "heligoland", "malta", "st_helena", "mauritius", "seychelles"])


def main():
    ap = argparse.ArgumentParser(description="Framing analysis by region x era + viz")
    ap.add_argument("--stats", action="store_true", help="print summary, do not write")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    framed = sorted((root / FRAMED_DIR).glob("*.json"))
    # observations: list of (region, era, colony, year, frozenset(frames))
    obs = []
    per_colony = defaultdict(dict)   # colony -> {year -> set(frames)}
    unmapped = set()
    for f in framed:
        data = json.loads(f.read_text(encoding="utf-8"))
        colony = data["colony"]
        region = REGION.get(colony)
        if region is None:
            unmapped.add(colony)
        for v in data["versions"]:
            if v.get("quarantined"):
                continue
            frames = {a["framing_type"] for a in v.get("framings", [])}
            for y in v["edition_years"]:
                obs.append((region, era_of(y), colony, y, frames))
                per_colony[colony][y] = sorted(frames)

    def prevalence(filter_key):
        """frame -> % of observations matching filter_key that carry the frame."""
        groups = defaultdict(lambda: [0, defaultdict(int)])  # key -> [n, {frame:count}]
        for region, era, colony, year, frames in obs:
            k = filter_key(region, era)
            if k is None:
                continue
            groups[k][0] += 1
            for fr in frames:
                groups[k][1][fr] += 1
        return {k: {"n": n, "pct": {fr: round(100 * c.get(fr, 0) / n) for fr in FRAMES}}
                for k, (n, c) in groups.items()}

    by_region = prevalence(lambda region, era: region)
    by_era = prevalence(lambda region, era: era)
    by_region_era = prevalence(lambda region, era: f"{region} || {era}"
                               if region else None)

    # per-colony timelines (>=5 editions) for the evolution view
    timelines = {c: {str(y): fr for y, fr in sorted(d.items())}
                 for c, d in per_colony.items() if len(d) >= 5}

    analysis = {
        "pipeline_version": "col_analyze_framing/0.1",
        "date_created": date.today().isoformat(),
        "note": ("Share of published colony-year histories using each imperial "
                 "framing category. These describe the Colonial Office's "
                 "perspective, not historical fact."),
        "frames": FRAMES,
        "eras": [e[2] for e in ERAS],
        "n_observations": len(obs),
        "by_region": by_region,
        "by_era": by_era,
        "by_region_era": by_region_era,
        "timelines": timelines,
    }

    # ---- console summary ----
    print(f"\n=== Framing by region (% of published colony-year histories, n={len(obs)}) ===")
    order = sorted(by_region, key=lambda r: -by_region[r]["pct"]["civilising"])
    hdr = "region".ljust(28) + "".join(fr[:9].rjust(10) for fr in FRAMES) + "    n"
    print(hdr)
    for r in order:
        row = by_region[r]
        print(r.ljust(28) + "".join(f'{row["pct"][fr]:9d}%' for fr in FRAMES)
              + f'{row["n"]:6d}')
    print(f"\n=== Framing by era ===")
    print("era".ljust(28) + "".join(fr[:9].rjust(10) for fr in FRAMES))
    for _, _, label in ERAS:
        if label in by_era:
            row = by_era[label]
            print(label.ljust(28) + "".join(f'{row["pct"][fr]:9d}%' for fr in FRAMES))
    if unmapped:
        print(f"\n(unmapped colonies, excluded from region view: {sorted(unmapped)})")

    if not args.stats:
        (root / "generated" / "framing_analysis.json").write_text(
            json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8")
        html = HTML_TEMPLATE.replace("/*DATA*/", json.dumps(analysis, ensure_ascii=False))
        (root / "framing_viz.html").write_text(html, encoding="utf-8")
        print("\nwrote generated/framing_analysis.json and framing_viz.html")


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Colonial Office List — Framing of Colony Histories</title>
<style>
 body{font:14px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;margin:0;background:#faf8f4;color:#222}
 header{background:#3a2f25;color:#f3ead9;padding:18px 28px}
 header h1{margin:0 0 4px;font-size:20px} header p{margin:0;font-size:13px;opacity:.85;max-width:900px}
 main{padding:22px 28px;max-width:1100px} h2{font-size:16px;margin:30px 0 8px;color:#3a2f25}
 .note{font-size:12px;color:#6b5d4c;margin:0 0 12px}
 table{border-collapse:collapse;font-size:13px} td,th{padding:5px 8px;text-align:center}
 th.l,td.l{text-align:left;white-space:nowrap;font-weight:600;color:#3a2f25}
 .cell{color:#1a1a1a;font-variant-numeric:tabular-nums;border:1px solid #fff;min-width:48px}
 .leg{font-size:11px;color:#6b5d4c;margin-top:6px}
 select{font-size:13px;padding:4px}
 svg text{font-size:11px;fill:#444}
 .frbox{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:4px;vertical-align:middle}
</style></head><body>
<header>
 <h1>How the Colonial Office Narrated Its Colonies</h1>
 <p>Prevalence of imperial framing in the <b>History</b> sections of the Colonial Office List (1862–1966),
 by region, era, and over time. Each value is the share of published colony-year histories using that
 framing. <b>These are the source's claims and perspective, not objective history.</b></p>
</header>
<main>
 <h2>Framing by region</h2>
 <p class="note">Rows sorted by "civilising" framing (natives / tribes / savage / protection). Darker = more prevalent.</p>
 <div id="region"></div>
 <h2>Framing by era</h2>
 <p class="note">Did the narration shift over time? Each line is one framing category's prevalence across eras.</p>
 <svg id="era" width="760" height="300"></svg>
 <div id="eralegend" class="leg"></div>
 <h2>Per-colony framing over time</h2>
 <p class="note">Frames present in each edition's history. Watch a single colony's narration evolve
 (e.g. Sierra Leone's shift to scare-quoted "King").</p>
 <select id="colsel"></select>
 <div id="timeline" style="margin-top:10px"></div>
</main>
<script>
const A = /*DATA*/;
const FRAMES = A.frames;
const FCOLOR = {discovery:"#2b7bba",cession_acquisition:"#8c510a",conflict:"#b2182b",
                civilising:"#762a83",sovereignty:"#1b7837"};
const FLABEL = {discovery:"discovery",cession_acquisition:"cession/acquisition",
                conflict:"conflict",civilising:"civilising",sovereignty:"sovereignty"};
function heat(v){const t=v/100;const r=Math.round(250-160*t),g=Math.round(245-150*t),b=Math.round(235-180*t);
  return `rgb(${r},${g},${b})`;}

// region heatmap
(function(){
 const regions=Object.keys(A.by_region).sort((a,b)=>A.by_region[b].pct.civilising-A.by_region[a].pct.civilising);
 let h='<table><tr><th class="l">region</th>'+FRAMES.map(f=>`<th>${FLABEL[f]}</th>`).join('')+'<th>n</th></tr>';
 for(const r of regions){const row=A.by_region[r];
   h+=`<tr><td class="l">${r}</td>`+FRAMES.map(f=>{const v=row.pct[f];
     return `<td class="cell" style="background:${heat(v)}">${v}%</td>`;}).join('')+`<td>${row.n}</td></tr>`;}
 h+='</table>';document.getElementById('region').innerHTML=h;
})();

// era line chart
(function(){
 const eras=A.eras.filter(e=>A.by_era[e]);const W=760,H=300,P=46;
 const x=i=>P+i*((W-2*P)/(eras.length-1||1));const y=v=>H-P-(v/100)*(H-2*P);
 let s=`<line x1="${P}" y1="${H-P}" x2="${W-P}" y2="${H-P}" stroke="#ccc"/>`;
 for(let v=0;v<=100;v+=25){s+=`<line x1="${P}" y1="${y(v)}" x2="${W-P}" y2="${y(v)}" stroke="#eee"/>`+
   `<text x="${P-8}" y="${y(v)+3}" text-anchor="end">${v}%</text>`;}
 eras.forEach((e,i)=>s+=`<text x="${x(i)}" y="${H-P+16}" text-anchor="middle">${e.split(' ')[0]}</text>`);
 for(const f of FRAMES){const pts=eras.map((e,i)=>`${x(i)},${y(A.by_era[e].pct[f])}`).join(' ');
   s+=`<polyline points="${pts}" fill="none" stroke="${FCOLOR[f]}" stroke-width="2.5"/>`;
   eras.forEach((e,i)=>s+=`<circle cx="${x(i)}" cy="${y(A.by_era[e].pct[f])}" r="3" fill="${FCOLOR[f]}"/>`);}
 document.getElementById('era').innerHTML=s;
 document.getElementById('eralegend').innerHTML=FRAMES.map(f=>
   `<span class="frbox" style="background:${FCOLOR[f]}"></span>${FLABEL[f]}`).join('&nbsp;&nbsp;');
})();

// per-colony timeline
(function(){
 const cols=Object.keys(A.timelines).sort();const sel=document.getElementById('colsel');
 const pref=cols.includes('sierra_leone')?'sierra_leone':cols[0];
 for(const c of cols){const o=document.createElement('option');o.value=c;o.textContent=c;
   if(c===pref)o.selected=true;sel.appendChild(o);}
 function draw(c){const tl=A.timelines[c];const years=Object.keys(tl).sort();
   let h='<table><tr><th class="l">frame \\ year</th>'+years.map(y=>`<th style="font-size:10px">${y.slice(2)}</th>`).join('')+'</tr>';
   for(const f of FRAMES){h+=`<tr><td class="l" style="color:${FCOLOR[f]}">${FLABEL[f]}</td>`+
     years.map(y=>{const on=tl[y].includes(f);
       return `<td class="cell" style="background:${on?FCOLOR[f]:'#f0ece4'};min-width:20px">${on?'':''}</td>`;}).join('')+'</tr>';}
   h+='</table>';document.getElementById('timeline').innerHTML=h;}
 sel.onchange=()=>draw(sel.value);draw(pref);
})();
</script></body></html>"""


if __name__ == "__main__":
    main()

"""
COL Phase 4: Corpus-Wide ML Scoring
=====================================

Scores all existing POSSIBLE_MATCH edges with the trained ML model, then
discovers new candidate pairs via blocking rules. Generates a disagreement
report (ML vs hand-tuned linker) and an HTML review page for active learning.

Modes:
  --score-edges     Score existing POSSIBLE_MATCH edges with ML model
  --discover        Find new candidate pairs not in the hand-tuned linker
  --write           Write ml_uncertainty to Neo4j (requires --score-edges)
  --compare         Generate disagreement report + HTML review page

Usage:
    python col_ml_score.py --score-edges                  # score + report
    python col_ml_score.py --score-edges --write          # score + write to Neo4j
    python col_ml_score.py --score-edges --compare        # score + disagreement report
    python col_ml_score.py --discover                     # find new candidates
    python col_ml_score.py --discover --compare           # new candidates + review HTML
    python col_ml_score.py --score-edges --discover --compare  # everything

Requires:
    pip install neo4j scikit-learn joblib numpy
"""

import argparse
import csv
import json
import math
import os
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed")
    sys.exit(1)

try:
    import joblib
except ImportError:
    print("ERROR: joblib not installed. Run: pip install joblib")
    sys.exit(1)

from col_ml_features import (
    FEATURE_COLS, compute_features, load_official_data,
    _is_bare_member,
)
from col_link_officials import is_bare_member_position
from col_normalize_names import initials_compatible, clean_given_names

# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
ML_DIR = REPO_DIR / "ml_data"
MODEL_FILE = ML_DIR / "model.joblib"
BATCH_SIZE = 500

# Load .env
_env_file = REPO_DIR / ".env"
if _env_file.exists():
    with open(_env_file) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _key, _val = _line.split("=", 1)
                os.environ.setdefault(_key.strip(), _val.strip())

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")


# =============================================================================
# MODEL LOADING
# =============================================================================

def load_model():
    """Load the trained GradientBoosting model."""
    if not MODEL_FILE.exists():
        print(f"ERROR: Model not found: {MODEL_FILE}")
        print("  Run col_ml_train.py first")
        sys.exit(1)
    model = joblib.load(MODEL_FILE)
    print(f"  Loaded model: {MODEL_FILE}")
    return model


# =============================================================================
# SCORE EXISTING EDGES
# =============================================================================

def fetch_possible_match_edges(session):
    """Fetch all POSSIBLE_MATCH edges with their properties."""
    result = session.run("""
        MATCH (a:COL_Official)-[r:POSSIBLE_MATCH]->(b:COL_Official)
        RETURN a.id AS a_id, b.id AS b_id,
               r.uncertainty AS uncertainty,
               r.method AS method,
               r.gap_years AS gap_years,
               r.domain_match AS domain_match
    """)
    return [dict(r) for r in result]


def score_pairs(model, pairs_data, officials):
    """Score pairs using the ML model.

    pairs_data: list of dicts with at least a_id, b_id
    officials: dict from load_official_data

    Returns list of result dicts.
    """
    results = []
    skipped = 0
    excluded_member = 0

    for pair in pairs_data:
        a_id = pair["a_id"]
        b_id = pair["b_id"]
        a_data = officials.get(a_id)
        b_data = officials.get(b_id)

        if not a_data or not b_data:
            skipped += 1
            continue

        if _is_bare_member(a_data) or _is_bare_member(b_data):
            excluded_member += 1
            continue

        # Ensure chronological order
        if (a_data.get("first_year") or 0) > (b_data.get("first_year") or 0):
            a_data, b_data = b_data, a_data
            a_id, b_id = b_id, a_id

        features = compute_features(a_data, b_data)

        # Build feature vector
        X = np.zeros((1, len(FEATURE_COLS)))
        for j, col in enumerate(FEATURE_COLS):
            try:
                X[0, j] = float(features.get(col, 0))
            except (ValueError, TypeError):
                X[0, j] = 0.0

        prob = model.predict_proba(X)[0, 1]

        results.append({
            "a_id": a_id,
            "b_id": b_id,
            "a_name": a_data.get("name", ""),
            "b_name": b_data.get("name", ""),
            "a_colony": a_data.get("colony", ""),
            "b_colony": b_data.get("colony", ""),
            "ml_probability": round(prob, 4),
            "ml_uncertainty": round(1.0 - prob, 4),
            "hand_tuned_uncertainty": pair.get("uncertainty"),
            "method": pair.get("method", ""),
            "a_first_pos": a_data.get("first_position", ""),
            "a_last_pos": a_data.get("last_position", ""),
            "b_first_pos": b_data.get("first_position", ""),
            "b_last_pos": b_data.get("last_position", ""),
            "a_first_year": a_data.get("first_year"),
            "a_last_year": a_data.get("last_year"),
            "b_first_year": b_data.get("first_year"),
            "b_last_year": b_data.get("last_year"),
            "source": pair.get("source", "ml_discovery"),
        })

    if skipped:
        print(f"  Skipped {skipped} (missing official data)")
    if excluded_member:
        print(f"  Excluded {excluded_member} (bare legislative member)")

    return results


def write_ml_scores(session, results):
    """Write ml_uncertainty and ml_confidence to POSSIBLE_MATCH edges."""
    batch = []
    written = 0

    for r in results:
        batch.append({
            "a_id": r["a_id"],
            "b_id": r["b_id"],
            "ml_unc": r["ml_uncertainty"],
            "ml_prob": r["ml_probability"],
        })
        if len(batch) >= BATCH_SIZE:
            _write_score_batch(session, batch)
            written += len(batch)
            batch = []

    if batch:
        _write_score_batch(session, batch)
        written += len(batch)

    return written


def _write_score_batch(session, batch):
    session.run("""
        UNWIND $batch AS row
        MATCH (a:COL_Official {id: row.a_id})-[r:POSSIBLE_MATCH]-(b:COL_Official {id: row.b_id})
        SET r.ml_uncertainty = row.ml_unc,
            r.ml_probability = row.ml_prob
    """, batch=batch)


# =============================================================================
# NEW CANDIDATE DISCOVERY (BLOCKING)
# =============================================================================

def fetch_all_officials_for_discovery(session):
    """Fetch all COL_Officials with boundary PersonRecord data."""
    result = session.run("""
        MATCH (o:COL_Official)
        WHERE EXISTS {
            MATCH (pr:COL_PersonRecord)-[:RECORD_OF]->(o)
            WHERE pr.quarantined IS NULL OR pr.quarantined = false
        }
        OPTIONAL MATCH (pr_first:COL_PersonRecord)-[:RECORD_OF]->(o)
        WHERE pr_first.year = o.first_year
          AND (pr_first.quarantined IS NULL OR pr_first.quarantined = false)
        OPTIONAL MATCH (pr_last:COL_PersonRecord)-[:RECORD_OF]->(o)
        WHERE pr_last.year = o.last_year
          AND (pr_last.quarantined IS NULL OR pr_last.quarantined = false)
        RETURN
            o.id AS id,
            o.name AS name,
            o.colony AS colony,
            o.first_year AS first_year,
            o.last_year AS last_year,
            o.num_editions AS num_editions,
            pr_first.position_raw AS first_position,
            pr_first.department_raw AS first_department,
            pr_first.honors AS first_honours,
            pr_last.position_raw AS last_position,
            pr_last.department_raw AS last_department,
            pr_last.honors AS last_honours
    """)
    return {r["id"]: dict(r) for r in result}


def fetch_existing_edges(session):
    """Fetch all existing POSSIBLE_MATCH edge pairs as a set."""
    result = session.run("""
        MATCH (a:COL_Official)-[:POSSIBLE_MATCH]-(b:COL_Official)
        RETURN a.id AS a_id, b.id AS b_id
    """)
    edges = set()
    for r in result:
        pair = tuple(sorted([r["a_id"], r["b_id"]]))
        edges.add(pair)
    return edges


def discover_new_candidates(officials, existing_edges, max_gap=30):
    """Find new candidate pairs via surname blocking.

    Blocking rules:
    - Same surname
    - Compatible initials (fuzzy name matching)
    - Gap <= max_gap years (no overlap > 5 years)
    - Not already a POSSIBLE_MATCH edge
    - Neither side is a bare legislative member
    - At least one side has a position

    Returns list of candidate pair dicts.
    """
    # Group by surname
    by_surname = defaultdict(list)
    for oid, data in officials.items():
        name = data.get("name", "")
        if "," not in name:
            continue
        surname = name.split(",", 1)[0].strip()
        by_surname[surname].append(data)

    candidates = []
    skipped_large = 0

    for surname, stints in by_surname.items():
        if len(stints) > 200:
            skipped_large += 1
            continue

        for i, a in enumerate(stints):
            for b in stints[i + 1:]:
                a_id = a["id"]
                b_id = b["id"]

                # Skip existing edges
                pair_key = tuple(sorted([a_id, b_id]))
                if pair_key in existing_edges:
                    continue

                # Skip bare members
                if _is_bare_member(a) or _is_bare_member(b):
                    continue

                # Need at least one position on each side
                a_has_pos = bool((a.get("first_position") or "").strip() or
                                 (a.get("last_position") or "").strip())
                b_has_pos = bool((b.get("first_position") or "").strip() or
                                 (b.get("last_position") or "").strip())
                if not a_has_pos or not b_has_pos:
                    continue

                # Check name compatibility (initials)
                a_name = a.get("name", "")
                b_name = b.get("name", "")
                if a_name != b_name:
                    # Different full names — check initials
                    a_given = a_name.split(",", 1)[1].strip() if "," in a_name else ""
                    b_given = b_name.split(",", 1)[1].strip() if "," in b_name else ""
                    a_clean = clean_given_names(a_given)
                    b_clean = clean_given_names(b_given)
                    if not initials_compatible(a_clean, b_clean):
                        continue

                # Chronological order
                a_first = a.get("first_year") or 9999
                b_first = b.get("first_year") or 9999
                if a_first > b_first:
                    a, b = b, a
                    a_id, b_id = b_id, a_id

                # Gap check
                a_last = a.get("last_year") or 0
                b_first_yr = b.get("first_year") or 0
                gap = b_first_yr - a_last
                if gap > max_gap:
                    continue
                # Skip heavy overlaps (> 5 years simultaneous service unlikely)
                if gap < -5:
                    continue

                candidates.append({
                    "a_id": a_id,
                    "b_id": b_id,
                    "source": "ml_discovery",
                })

    if skipped_large:
        print(f"  Skipped {skipped_large} large surname groups (>200)")

    return candidates


# =============================================================================
# COMPARISON REPORT
# =============================================================================

def generate_comparison_report(results, threshold=0.20):
    """Generate disagreement report between ML and hand-tuned scores."""
    # Separate scored edges (have hand-tuned) from discoveries (don't)
    scored_edges = [r for r in results if r.get("hand_tuned_uncertainty") is not None]
    discoveries = [r for r in results if r.get("hand_tuned_uncertainty") is None]

    # Find disagreements in scored edges
    disagreements = []
    for r in scored_edges:
        ht = r["hand_tuned_uncertainty"]
        ml = r["ml_uncertainty"]
        diff = ht - ml  # positive = ML more confident than linker
        if abs(diff) > threshold:
            r["diff"] = round(diff, 4)
            r["direction"] = "ML_more_confident" if diff > 0 else "ML_less_confident"
            disagreements.append(r)

    disagreements.sort(key=lambda x: abs(x["diff"]), reverse=True)

    # High-confidence new discoveries
    high_conf_discoveries = [r for r in discoveries if r["ml_probability"] > 0.5]
    high_conf_discoveries.sort(key=lambda x: x["ml_probability"], reverse=True)

    # Write CSV reports
    _write_disagreement_csv(disagreements)
    _write_discovery_csv(high_conf_discoveries)

    # Print summary
    lines = []
    lines.append("=" * 60)
    lines.append("PHASE 4: ML SCORING COMPARISON REPORT")
    lines.append("=" * 60)

    if scored_edges:
        lines.append(f"\nScored existing edges: {len(scored_edges)}")
        ml_match = sum(1 for r in scored_edges if r["ml_probability"] > 0.5)
        ml_reject = len(scored_edges) - ml_match
        lines.append(f"  ML says match (prob > 0.5): {ml_match}")
        lines.append(f"  ML says no match: {ml_reject}")
        lines.append(f"\nDisagreements (|diff| > {threshold}): {len(disagreements)}")
        ml_more = sum(1 for d in disagreements if d["direction"] == "ML_more_confident")
        ml_less = sum(1 for d in disagreements if d["direction"] == "ML_less_confident")
        lines.append(f"  ML more confident than linker: {ml_more}")
        lines.append(f"  ML less confident than linker: {ml_less}")

        # Correlation
        ht_vals = [r["hand_tuned_uncertainty"] for r in scored_edges]
        ml_vals = [r["ml_uncertainty"] for r in scored_edges]
        corr = np.corrcoef(ht_vals, ml_vals)[0, 1]
        lines.append(f"\nCorrelation (hand-tuned vs ML uncertainty): {corr:.4f}")
        lines.append(f"Hand-tuned: mean={np.mean(ht_vals):.3f} median={np.median(ht_vals):.3f}")
        lines.append(f"ML:         mean={np.mean(ml_vals):.3f} median={np.median(ml_vals):.3f}")

    if discoveries:
        lines.append(f"\nNew discovery candidates: {len(discoveries)}")
        lines.append(f"  High confidence (prob > 0.5): {len(high_conf_discoveries)}")
        if high_conf_discoveries:
            lines.append(f"  Top probability: {high_conf_discoveries[0]['ml_probability']:.4f}")

    # Top disagreements
    if disagreements:
        lines.append(f"\nTop 20 disagreements:")
        for d in disagreements[:20]:
            lines.append(f"  {d['a_name']} ({d['a_colony']}) -> "
                        f"{d['b_name']} ({d['b_colony']})")
            lines.append(f"    linker={d['hand_tuned_uncertainty']:.3f}  "
                        f"ML={d['ml_uncertainty']:.3f}  "
                        f"diff={d['diff']:+.3f} ({d['direction']})")

    # Top discoveries
    if high_conf_discoveries:
        lines.append(f"\nTop 20 new discoveries:")
        for d in high_conf_discoveries[:20]:
            lines.append(f"  {d['a_name']} ({d['a_colony']}) -> "
                        f"{d['b_name']} ({d['b_colony']})")
            lines.append(f"    prob={d['ml_probability']:.4f}  "
                        f"positions: {d.get('a_last_pos', '?')} -> {d.get('b_first_pos', '?')}")

    report = "\n".join(lines)
    report_path = ML_DIR / "phase4_report.txt"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"\n  Report: {report_path}")
    print(report)

    # Generate HTML review pages
    _generate_review_html(disagreements, high_conf_discoveries)

    return disagreements, high_conf_discoveries


def _write_disagreement_csv(disagreements):
    """Write disagreements to CSV."""
    path = ML_DIR / "phase4_disagreements.csv"
    if not disagreements:
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "a_id", "b_id", "a_name", "b_name", "a_colony", "b_colony",
            "hand_tuned_uncertainty", "ml_uncertainty", "ml_probability",
            "diff", "direction", "method",
            "a_last_pos", "b_first_pos",
        ])
        writer.writeheader()
        for d in disagreements:
            writer.writerow({k: d.get(k) for k in writer.fieldnames})
    print(f"  Disagreements CSV: {path} ({len(disagreements)} rows)")


def _write_discovery_csv(discoveries):
    """Write new discoveries to CSV."""
    path = ML_DIR / "phase4_discoveries.csv"
    if not discoveries:
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "a_id", "b_id", "a_name", "b_name", "a_colony", "b_colony",
            "ml_probability", "ml_uncertainty",
            "a_last_pos", "b_first_pos",
            "a_first_year", "a_last_year", "b_first_year", "b_last_year",
        ])
        writer.writeheader()
        for d in discoveries:
            writer.writerow({k: d.get(k) for k in writer.fieldnames})
    print(f"  Discoveries CSV: {path} ({len(discoveries)} rows)")


def _generate_review_html(disagreements, discoveries):
    """Generate HTML review page for active learning."""
    # Combine both into one review page, tagged by source
    items = []

    for d in disagreements:
        items.append({
            "verdict": "?",
            "verified": False,
            "source": "disagreement",
            "direction": d.get("direction", ""),
            "a_name": d.get("a_name", ""),
            "b_name": d.get("b_name", ""),
            "a_colony": d.get("a_colony", ""),
            "b_colony": d.get("b_colony", ""),
            "a_pos": d.get("a_last_pos", ""),
            "b_pos": d.get("b_first_pos", ""),
            "a_years": f"{d.get('a_first_year', '?')}-{d.get('a_last_year', '?')}",
            "b_years": f"{d.get('b_first_year', '?')}-{d.get('b_last_year', '?')}",
            "ml_prob": f"{d.get('ml_probability', 0):.3f}",
            "ht_unc": f"{d.get('hand_tuned_uncertainty', ''):.3f}" if d.get('hand_tuned_uncertainty') is not None else "",
            "a_id": d.get("a_id", ""),
            "b_id": d.get("b_id", ""),
        })

    for d in discoveries:
        items.append({
            "verdict": "?",
            "verified": False,
            "source": "discovery",
            "direction": "",
            "a_name": d.get("a_name", ""),
            "b_name": d.get("b_name", ""),
            "a_colony": d.get("a_colony", ""),
            "b_colony": d.get("b_colony", ""),
            "a_pos": d.get("a_last_pos", ""),
            "b_pos": d.get("b_first_pos", ""),
            "a_years": f"{d.get('a_first_year', '?')}-{d.get('a_last_year', '?')}",
            "b_years": f"{d.get('b_first_year', '?')}-{d.get('b_last_year', '?')}",
            "ml_prob": f"{d.get('ml_probability', 0):.3f}",
            "ht_unc": "",
            "a_id": d.get("a_id", ""),
            "b_id": d.get("b_id", ""),
        })

    if not items:
        return

    html = _build_review_html(items)
    path = ML_DIR / "review_phase4.html"
    with open(path, "w") as f:
        f.write(html)
    print(f"  Review HTML: {path} ({len(items)} pairs)")


def _build_review_html(items):
    """Build the Phase 4 review HTML page."""
    data_json = json.dumps(items, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Phase 4: ML Scoring Review</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:'Segoe UI',system-ui,sans-serif;background:#f5f5f5;padding:20px}}
  h1{{margin-bottom:5px}} p.sub{{margin-bottom:15px;color:#555}}
  .stats{{background:#fff;padding:15px;border-radius:8px;margin-bottom:20px;box-shadow:0 1px 3px rgba(0,0,0,.1)}}
  .stats span{{margin-right:20px;font-weight:bold}}
  .filters{{margin-bottom:15px}}
  .filters button{{padding:6px 14px;margin-right:6px;border:1px solid #ccc;border-radius:4px;cursor:pointer;background:#fff}}
  .filters button.active{{background:#333;color:#fff}}
  table{{width:100%;border-collapse:collapse;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.1)}}
  th{{background:#333;color:#fff;padding:8px 5px;text-align:left;font-size:11px;position:sticky;top:0}}
  td{{padding:5px;border-bottom:1px solid #eee;font-size:11px;vertical-align:top}}
  tr:hover{{background:#f0f7ff}}
  tr.label-Y{{border-left:4px solid #4caf50}}
  tr.label-N{{border-left:4px solid #f44336}}
  tr.label-Q{{border-left:4px solid #ff9800}}
  tr.verified{{background:#e8f5e9 !important}}
  .name{{font-weight:600}} .pos{{color:#1565c0;font-size:10px}}
  .colony{{color:#555}} .prob{{font-weight:bold}}
  .src-disagreement{{color:#e65100}} .src-discovery{{color:#1565c0}}
  select.verdict{{padding:3px;border-radius:4px;font-size:11px}}
  .vcheck{{width:18px;height:18px;cursor:pointer}}
  #export-btn{{padding:10px 20px;background:#1565c0;color:#fff;border:none;border-radius:6px;cursor:pointer;font-size:14px;margin-top:15px}}
  #export-btn:hover{{background:#0d47a1}}
</style>
</head>
<body>
<h1>Phase 4: ML Scoring Review</h1>
<p class="sub">Disagreements between ML and hand-tuned linker + new ML discoveries. Review for active learning.</p>
<div class="stats" id="stats"></div>
<div class="filters">
  <strong>Show:</strong>
  <button onclick="filter('all')" class="active" id="btn-all">All</button>
  <button onclick="filter('Y')" id="btn-Y">Y</button>
  <button onclick="filter('N')" id="btn-N">N</button>
  <button onclick="filter('?')" id="btn-Q">?</button>
  <button onclick="filter('disagreement')" id="btn-disagreement">Disagreements</button>
  <button onclick="filter('discovery')" id="btn-discovery">Discoveries</button>
  <button onclick="filter('verified')" id="btn-verified">Verified</button>
  <button onclick="filter('unverified')" id="btn-unverified">Unverified</button>
</div>
<table>
<thead><tr>
  <th><input type="checkbox" onclick="toggleAllVerified(this)" title="Verify all visible"></th>
  <th>V</th>
  <th>Source</th><th>Name A</th><th>Name B</th><th>Colony A</th><th>Colony B</th>
  <th>A Years</th><th>A Position</th><th>B Years</th><th>B Position</th>
  <th>ML Prob</th><th>Linker Unc</th>
</tr></thead>
<tbody id="tbody"></tbody>
</table>
<button id="export-btn" onclick="exportCSV()">Export Verified Rows as CSV</button>
<script>
const DATA = {data_json};
let currentFilter='all';
function render(){{
  const tbody=document.getElementById('tbody');tbody.innerHTML='';
  let shown=0,yC=0,nC=0,qC=0,vC=0,disC=0,discC=0;
  DATA.forEach((d,i)=>{{
    const v=d.verdict;
    if(v==='Y')yC++;else if(v==='N')nC++;else qC++;
    if(d.verified)vC++;
    if(d.source==='disagreement')disC++;else discC++;
    if(currentFilter==='Y'&&v!=='Y')return;
    if(currentFilter==='N'&&v!=='N')return;
    if(currentFilter==='?'&&v!=='?')return;
    if(currentFilter==='disagreement'&&d.source!=='disagreement')return;
    if(currentFilter==='discovery'&&d.source!=='discovery')return;
    if(currentFilter==='verified'&&!d.verified)return;
    if(currentFilter==='unverified'&&d.verified)return;
    shown++;
    const cls=(v==='Y'?'label-Y':v==='N'?'label-N':'label-Q')+(d.verified?' verified':'');
    const srcCls=d.source==='disagreement'?'src-disagreement':'src-discovery';
    const tr=document.createElement('tr');tr.className=cls;
    tr.innerHTML=`
      <td><input type="checkbox" class="vcheck" data-idx="${{i}}" ${{d.verified?'checked':''}} onchange="toggleVerified(this)"></td>
      <td><select class="verdict" data-idx="${{i}}" onchange="cv(this)">
        <option value="Y" ${{v==='Y'?'selected':''}}>Y</option>
        <option value="N" ${{v==='N'?'selected':''}}>N</option>
        <option value="?" ${{v==='?'?'selected':''}}>?</option>
      </select></td>
      <td class="${{srcCls}}">${{esc(d.source)}}</td>
      <td class="name">${{esc(d.a_name)}}</td><td class="name">${{esc(d.b_name)}}</td>
      <td class="colony">${{esc(d.a_colony)}}</td><td class="colony">${{esc(d.b_colony)}}</td>
      <td>${{esc(d.a_years)}}</td><td class="pos">${{esc(d.a_pos)}}</td>
      <td>${{esc(d.b_years)}}</td><td class="pos">${{esc(d.b_pos)}}</td>
      <td class="prob">${{esc(d.ml_prob)}}</td><td>${{esc(d.ht_unc)}}</td>`;
    tbody.appendChild(tr);
  }});
  document.getElementById('stats').innerHTML=
    `<span>Total: ${{DATA.length}}</span><span style="color:#2e7d32">Y: ${{yC}}</span>`+
    `<span style="color:#c62828">N: ${{nC}}</span><span style="color:#e65100">?: ${{qC}}</span>`+
    `<span>Showing: ${{shown}}</span><span style="color:#1565c0">Verified: ${{vC}}</span>`+
    `<span class="src-disagreement">Disagree: ${{disC}}</span>`+
    `<span class="src-discovery">Discover: ${{discC}}</span>`;
}}
function filter(f){{currentFilter=f;document.querySelectorAll('.filters button').forEach(b=>b.classList.remove('active'));
  const btnId=f==='?'?'Q':f;const btn=document.getElementById('btn-'+btnId);if(btn)btn.classList.add('active');render();}}
function cv(sel){{const i=parseInt(sel.dataset.idx);DATA[i].verdict=sel.value;DATA[i].verified=true;render();}}
function toggleVerified(cb){{DATA[parseInt(cb.dataset.idx)].verified=cb.checked;render();}}
function toggleAllVerified(cb){{
  const visible=[];DATA.forEach((d,i)=>{{
    const v=d.verdict;
    if(currentFilter==='Y'&&v!=='Y')return;if(currentFilter==='N'&&v!=='N')return;
    if(currentFilter==='?'&&v!=='?')return;
    if(currentFilter==='disagreement'&&d.source!=='disagreement')return;
    if(currentFilter==='discovery'&&d.source!=='discovery')return;
    if(currentFilter==='verified'&&!d.verified)return;
    if(currentFilter==='unverified'&&d.verified)return;visible.push(i);
  }});
  visible.forEach(i=>{{DATA[i].verified=cb.checked;}});render();}}
function esc(s){{return s?String(s).replace(/</g,'&lt;').replace(/>/g,'&gt;'):''}}
function exportCSV(){{
  const ver=DATA.filter(d=>d.verified);
  if(!ver.length){{alert('No verified rows');return;}}
  let csv='a_id,b_id,verdict,source\\n';
  ver.forEach(d=>{{csv+=`"${{d.a_id}}","${{d.b_id}}","${{d.verdict}}","${{d.source}}"\\n`;}});
  const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([csv],{{type:'text/csv'}}));
  a.download='review_phase4_verified.csv';a.click();
}}
render();
</script>
</body>
</html>"""


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Phase 4: Corpus-wide ML scoring and new candidate discovery")
    parser.add_argument("--score-edges", action="store_true",
                        help="Score existing POSSIBLE_MATCH edges")
    parser.add_argument("--discover", action="store_true",
                        help="Discover new candidate pairs via blocking")
    parser.add_argument("--write", action="store_true",
                        help="Write ml_uncertainty to Neo4j edges")
    parser.add_argument("--compare", action="store_true",
                        help="Generate comparison report + HTML review")
    parser.add_argument("--threshold", type=float, default=0.20,
                        help="Disagreement threshold (default: 0.20)")
    parser.add_argument("--max-gap", type=int, default=30,
                        help="Max gap years for discovery blocking (default: 30)")
    args = parser.parse_args()

    if not args.score_edges and not args.discover:
        print("Specify --score-edges and/or --discover. Use --help for details.")
        sys.exit(1)

    if not NEO4J_PASSWORD:
        print("ERROR: Set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    # Load model
    print("Loading model...")
    model = load_model()

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    all_results = []

    try:
        # --- Score existing edges ---
        if args.score_edges:
            print("\n--- SCORING EXISTING EDGES ---")
            with driver.session() as session:
                edges = fetch_possible_match_edges(session)
            print(f"  Found {len(edges)} POSSIBLE_MATCH edges")

            # Collect all official IDs
            edge_ids = set()
            for e in edges:
                edge_ids.add(e["a_id"])
                edge_ids.add(e["b_id"])

            print(f"  Loading {len(edge_ids)} officials...")
            officials = load_official_data(driver, edge_ids)

            print("  Scoring...")
            edge_results = score_pairs(model, edges, officials)
            print(f"  Scored {len(edge_results)} edges")
            all_results.extend(edge_results)

            if args.write:
                print("\n  Writing ML scores to Neo4j...")
                with driver.session() as session:
                    written = write_ml_scores(session, edge_results)
                print(f"  Written to {written} edges")

            # Quick summary
            ml_match = sum(1 for r in edge_results if r["ml_probability"] > 0.5)
            print(f"\n  ML match (prob > 0.5): {ml_match}/{len(edge_results)}")

        # --- Discover new candidates ---
        if args.discover:
            print("\n--- DISCOVERING NEW CANDIDATES ---")
            with driver.session() as session:
                print("  Fetching all officials...")
                all_officials = fetch_all_officials_for_discovery(session)
                print(f"  Loaded {len(all_officials)} officials")

                print("  Fetching existing edges...")
                existing = fetch_existing_edges(session)
                print(f"  {len(existing)} existing edge pairs")

            print(f"  Generating candidates (max_gap={args.max_gap})...")
            candidates = discover_new_candidates(
                all_officials, existing, max_gap=args.max_gap)
            print(f"  {len(candidates)} new candidate pairs found")

            if candidates:
                # Collect IDs
                disc_ids = set()
                for c in candidates:
                    disc_ids.add(c["a_id"])
                    disc_ids.add(c["b_id"])

                # Load official data (reuse if already loaded)
                print(f"  Loading {len(disc_ids)} officials for scoring...")
                disc_officials = load_official_data(driver, disc_ids)

                print("  Scoring new candidates...")
                disc_results = score_pairs(model, candidates, disc_officials)
                print(f"  Scored {len(disc_results)} candidates")

                # Only keep high-probability discoveries
                high_prob = [r for r in disc_results if r["ml_probability"] > 0.3]
                high_prob.sort(key=lambda x: x["ml_probability"], reverse=True)
                print(f"  High probability (> 0.3): {len(high_prob)}")
                print(f"  Very high (> 0.8): {sum(1 for r in high_prob if r['ml_probability'] > 0.8)}")

                all_results.extend(high_prob)

        # --- Comparison report ---
        if args.compare and all_results:
            print("\n--- GENERATING REPORT ---")
            generate_comparison_report(all_results, threshold=args.threshold)

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()

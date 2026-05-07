# ML Career Discovery — Status Report March 22, 2026

## Overview

Building an ML pipeline to discover career chains among 68,335 COL_Official nodes
extracted from ~300,000 Colonial Office List person records. The model predicts whether
two officials are the same person based on 19 features computed from node properties.

**Key principle:** Conservative over recall. False positives corrupt the graph silently;
missed links can be found later with external sources.

---

## Model Performance

**Current model:** GradientBoosting (sklearn), trained on 2,459 verified pairs.

```
5-fold stratified CV:
  Precision: 0.818   Recall: 0.871   F1: 0.843   AUC: 0.970
  Career recovery rate: 87%

Per-source recall:
  human_cross:            93.8%
  human_cross_discovery:  95.0%
  human_gap:             100.0%
  human_phase4:           84.5%
  human_sanity:          100.0%
  human_variant:          74.8%
```

### Feature Importance
1. `domain_match` — 39% (career domain continuity)
2. `name_exact_match` — 21%
3. `time_decay` — 9%
4. `gap_years` — 7%
5. `a_editions` — 7%
6. `same_colony` — 4.5% (reduced after cross-colony training)

### Training Data (2,459 pairs)

| Source | Positive | Negative | Total |
|--------|----------|----------|-------|
| gemini_hard_negative | 0 | 1,069 | 1,069 |
| wd_hard_negative | 0 | 376 | 376 |
| human_variant | 142 | 155 | 297 |
| human_phase4 | 73 | 94 | 167 |
| human_gap | 119 | 2 | 121 |
| curated | 99 | 0 | 99 |
| human_cross_discovery | 9 | 88 | 97 |
| human_cross | 46 | 46 | 92 |
| gemini | 63 | 0 | 63 |
| human_sanity | 36 | 4 | 40 |
| wikidata | 38 | 0 | 38 |
| **Total** | **625** | **1,834** | **2,459** |

---

## Corpus-Wide Results

### Scored Edges

All 25,538 POSSIBLE_MATCH edges scored with ML model. Breakdown:

| Method | Total | ML match (>0.5) | ML reject (<0.5) |
|--------|-------|------------------|-------------------|
| Within-colony (automated_linking) | 7,012 | 4,914 | 2,098 |
| Cross-colony (cross_colony_linking) | 9,391 | 6,374 | 3,017 |
| ML discovery (new edges) | 8,639 | 2,488 | 6,151 |
| **Total** | **25,042** | **13,776** | **11,266** |

### ML vs Hand-Tuned Linker Agreement

| | Count | % |
|---|---|---|
| Both agree match | 9,958 | 61% |
| Both agree no match | 2,831 | 17% |
| Linker YES, ML NO (potential false positives) | 911 | 6% |
| Linker NO, ML YES (linker too cautious) | 2,703 | 16% |

Sanity check of linker-NO-ML-YES: 72% confirmed correct (36 Y, 4 N, 10 ? out of 50).

### Chain Validation (Phase 5)

Career chain validation enforces temporal consistency — a person can only serve in
one unrelated colony at a time (with allowances for administrative sub-units like
Windward Islands/Grenada, Nigeria/Northern Nigeria, Gold Coast/Togoland, etc.).

| | Validated | Rejected |
|---|---|---|
| Within-colony | 4,823 | 104 |
| Cross-colony | 9,896 | 856 |
| **Total** | **14,719** | **960** |

960 edges rejected for temporal violations (simultaneous service in unrelated colonies).

---

## Exclusion Rules

1. **Bare legislative members** — "Member", "Member of Parliament", "Senator" positions
   excluded from linking pipeline. Data stays in graph, just not matched. 496 pairs affected.

2. **No matching without job titles** — Name variant pairs where either side lacks a
   position are excluded. Data too thin for reliable linking.

3. **Cross-colony overlap >2 years** — Flagged and zeroed in ML scoring. 2,383 edges
   affected. Compatible colony groups (e.g., Windward Islands sub-colonies) exempted.

### Compatible Colony Groups
Colonies where overlapping service is expected (administrative sub-units):
- Windward Islands ↔ Grenada, St Vincent, St Lucia, Dominica, Tobago
- Leeward Islands ↔ Antigua, Montserrat, St Kitts, Nevis, Virgin Islands
- Nigeria ↔ Southern Nigeria, Northern Nigeria, Lagos
- Gold Coast ↔ Togoland, Ashanti
- Malaya ↔ Straits Settlements, Federated/Unfederated Malay States
- Australia ↔ all state colonies; Canada ↔ all province colonies
- East Africa ↔ Kenya, Uganda, Tanganyika, Zanzibar
- And others (see col_ml_chains.py COLONY_GROUPS)

---

## Validation Against Known Careers

| Person | Expected Career | Result |
|--------|----------------|--------|
| **Lugard** | N.Nigeria → Hong Kong → Nigeria | ✅ All 3 linked, chain validated |
| **Guggisberg** | S.Nigeria → Togoland → Gold Coast | ✅ Togoland↔Gold Coast validated (compatible colonies). S.Nigeria links rejected by chain (ghost data at 1946-1948 confuses component) |
| **Alexander** | Fiji → Tanganyika | ✅ Linked at 0.992, chain validated |
| **Grimble** | Gilbert & Ellice → St Vincent → Seychelles → Windward Islands | ⚠️ Only 2 of 4 stints in database. G&E→Windward link found but scored 0.050 (name format change "A.F" → "Arthur Francis", domain change, long gap) |
| **Bradley** | N.Rhodesia → Falklands → Gold Coast | ❌ Only N.Rhodesia stint in database |

---

## Scripts

| Script | Purpose | Status |
|--------|---------|--------|
| `col_build_ground_truth.py` | Match external careers to COL_Officials | Phase 1 ✅ |
| `col_ml_features.py` | Compute 19 pairwise features | Phase 2 ✅ |
| `col_ml_train.py` | GradientBoosting CV + career recovery | Phase 3 ✅ |
| `col_ml_score.py` | Corpus-wide scoring + discovery | Phase 4 ✅ |
| `col_ml_chains.py` | Career chain validation (temporal consistency) | Phase 5 ✅ |

---

## Known Limitations

1. **Name format changes** — "A. F. Grimble" → "Arthur Francis Grimble" scores very low.
   The model relies heavily on `name_exact_match` (21% importance). Rare surnames should
   carry more weight but adding this risks false positives on common surnames.

2. **Cross-colony ratio** — 9,896 validated cross-colony edges vs 4,823 within-colony
   seems high. Partially explained by the cross-colony linker + ML discovery generating
   more candidates, but may indicate over-linking. Needs further validation.

3. **Ghost data** — Unquarantined ghost officials (e.g., Guggisberg Gold Coast 1946-1948)
   confuse the chain validator by appearing in components where they don't belong.

4. **Extraction gaps** — 719 .md files skipped by extraction pipeline. Some colonies/years
   have missing data, causing incomplete careers (Bradley, Grimble).

5. **Domain match is fragile** — `domain_match=0` (unknown) and `domain_match=1` (unknown)
   are treated similarly, but "unknown" covers both genuinely different careers and cases
   where positions are too different to classify. More granular domain taxonomy would help.

---

## Next Steps

### Immediate
1. **London Gazette integration** — SPARQL endpoint at `thegazette.co.uk/longitudinal-dataset/sparql`
   contains gazetted colonial appointments (name + role + colony). Can confirm career
   transitions with authoritative source. Tested successfully with Guggisberg query.

2. **Wikidata SAME_AS rebuild** — Stage 5 edges (COL_Official → WD_Person) not in current
   Neo4j session. Re-running `col_link_wikidata.py` would provide external confirmation
   for ~947 officials.

### Medium Term
3. **Ghost cleanup** — Quarantine remaining ghost officials that confuse chain validation.

4. **Extraction gap fix** — Process the 719 skipped .md files to complete the corpus.

5. **Cross-colony validation** — Targeted review of the 9,896 validated cross-colony
   edges to verify the ratio is genuine, not over-linking.

### Future
6. **London Gazette harvester** — Systematic querying of all colonial appointments from
   the Gazette SPARQL endpoint. Parse `entryText` for person+role+colony triples.
   Use as ground truth to supplement ML edges.

7. **Entourage/cohort detection** — Officials who move together between colonies are
   likely correctly linked. Network-level signal, deferred from original plan.

8. **Phonetic surname blocking** — For Phase 4 discovery, use phonetic matching
   (Soundex/Metaphone) to find surname variants the current exact-surname blocking misses.

---

## Data Files

| File | Purpose |
|------|---------|
| `ml_data/ground_truth_pairs.csv` | 2,459 labeled pairs |
| `ml_data/feature_matrix.csv` | 2,395 rows × 19 features (64 bare-member excluded) |
| `ml_data/model.joblib` | Trained GradientBoosting model |
| `ml_data/training_report.txt` | Latest CV results |
| `ml_data/phase4_report.txt` | Scoring comparison report |
| `ml_data/phase4_disagreements.csv` | ML vs linker disagreements |
| `ml_data/phase4_discoveries.csv` | New ML-discovered candidates |
| `ml_data/chain_validation_report.txt` | Chain validation results |
| `ml_data/curated_cross_colony_careers.json` | 20 hand-curated careers |
| `ml_data/known_careers.json` | 543 matched careers (WD + Gemini + curated) |

## Neo4j Properties on POSSIBLE_MATCH Edges

| Property | Source | Description |
|----------|--------|-------------|
| `uncertainty` | Hand-tuned linker | Original uncertainty score (0-1) |
| `ml_probability` | ML model | P(same person) from GradientBoosting |
| `ml_uncertainty` | ML model | 1 - ml_probability |
| `ml_overlap_flag` | Overlap filter | Years of cross-colony overlap (if >2) |
| `chain_validated` | Chain validator | true/false — temporal consistency check |
| `method` | Various | `automated_linking`, `cross_colony_linking`, or `ml_discovery` |
| `score_version` | Various | Version tracking |

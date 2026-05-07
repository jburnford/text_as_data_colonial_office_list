# ML Career Discovery — Status & Progress

**Last updated:** 2026-03-19
**Plan:** `PLAN_ML_CAREER_DISCOVERY_2026-03-17.md`

---

## Overview

Building an ML model to discover career chains among 68,335 COL_Official nodes.
The model predicts whether two officials are the same person based on 19 features
computed directly from node properties (not from the hand-tuned linker's edges).

**Key principle:** Prefer false negatives over false positives. A missed link can
be found later; a false link corrupts the graph silently.

---

## Phase Status

| Phase | Status | Script | Notes |
|-------|--------|--------|-------|
| **1. Ground Truth** | DONE | `col_build_ground_truth.py` | 543 careers from WD + Gemini + curated |
| **2. Features** | DONE | `col_ml_features.py` | 19 features, computed from COL_Official + PersonRecord properties |
| **3. Training** | IN PROGRESS | `col_ml_train.py` | 90% recovery, awaiting more human-verified data |
| **4. Scoring** | NOT STARTED | `col_ml_score.py` | Corpus-wide discovery + comparison with linker |
| **5. Network re-scoring** | FUTURE | — | Entourage/cohort detection (deferred) |

---

## Current Model Performance (2026-03-19)

```
5-fold stratified CV:
  Precision: 0.832   Recall: 0.879   F1: 0.854   AUC: 0.978
  Career recovery rate: 90% (target was >80%)

Per-source recall:
  human_cross:   93%  (cross-colony transfers)
  human_gap:    100%  (within-colony gaps)
  human_variant:  62%  (name recording variations — deliberately conservative)
```

### Feature Importance (top 6)
1. `name_exact_match` — 45% (whether official names are identical)
2. `same_colony` — 14% (within vs cross-colony)
3. `domain_match` — 13% (career domain continuity)
4. `time_decay` — 6% (gap penalty)
5. `a_editions` — 6% (how long person A served)
6. `gap_years` — 6% (years between stints)

---

## Training Data

### Ground Truth Sources (1,994 total pairs)

| Source | Positive | Negative | Notes |
|--------|----------|----------|-------|
| Gemini careers (400 across 7 colonies) | ~67 | ~1,445 | Within-colony; best negative data |
| Wikidata (358 dated colonial service) | ~34 | — | Within + cross colony |
| Curated cross-colony (19 careers) | 99 | — | Historically verified governors etc. |
| **Human-verified gap pairs** | 121 | 4 | From `review_gap_pairs.html` |
| **Human-verified name variants** | 56 | 81 | From `review_name_variants.html` |
| **Human-verified cross-colony** | 46 | 46 | From `review_cross_colony.html` |
| **Total** | **421** | **1,573** | |

### Human Review Pipeline

Three HTML review pages in `ml_data/` with verified checkbox:

| File | Total | Y | N | ? | Purpose |
|------|-------|---|---|---|---------|
| `review_gap_pairs.html` | 2,322 | 2,041 | 14 | 267 | Same name, same colony, gap in records |
| `review_name_variants.html` | 2,617 | 1,321 | 1,095 | 201 | Different names, same colony |
| `review_cross_colony.html` | 2,000 | 1,019 | 588 | 393 | Different colonies |

**Workflow:** Review in browser → tick verified checkbox → Export → place in Dropbox →
re-run integration + features + training.

**Export locations:** `C:\Users\jic823\Dropbox\2026\review_*_verified.csv`

**Re-training command sequence:**
```bash
# After exporting new verified CSVs from HTML reviews:
python3 col_ml_features.py    # recompute features for new pairs
python3 col_ml_train.py       # retrain model
```

---

## Key Decisions & Lessons

### Data Quality
- **Multi-year consistent name differences are NOT OCR errors.** If "Brown, W. A" appears
  in 6 editions and "Brown, W. H" in 9, they are different people (A ≠ H). Only flag as
  possible OCR if one side has 1-2 editions.
- **Hong Kong WWII gap ≠ Bermuda WWII gap.** Japanese occupation caused major staff
  turnover. Each HK case needs individual review. Bermuda/Gibraltar gaps are reliable
  (same officials returned).
- **Explosion groups** (same name matching multiple officials, e.g., 3×3 = 9 pairs for
  "Maingot, André" in Trinidad) must be individually reviewed. At most one A→B chain
  per person is correct.
- **Cadet demotions = father-son pairs.** Senior official → Cadet with same name is
  almost certainly the son entering colonial service, not a demotion.

### Model Design
- **GradientBoosting** (sklearn) — right choice for 421 positive pairs. Deep learning
  would overfit.
- **Features computed from node properties, not POSSIBLE_MATCH edges** — avoids circular
  training from the hand-tuned linker.
- **Career recovery rate** is the key metric, not pair-level accuracy.
- **Plan amendments from Gemini review (2026-03-17):**
  1. Phonetic surname blocking (Block 4) — for Phase 4 discovery
  2. Acting appointment features — implemented but rare in current data
  3. Entourage/cohort detection — deferred to Phase 5
  4. Hard negative sampling quotas — implemented via Gemini same-colony negatives

### Curated Cross-Colony Careers
`ml_data/curated_cross_colony_careers.json` — 19 historically verified careers
including Hugh Clifford (8 colonies), D. T. Tudor (6 colonies), Ralph Grey (5 colonies).
Extensible: add more careers with verified official IDs and re-run.

---

## Files

### Scripts
| File | Purpose |
|------|---------|
| `col_build_ground_truth.py` | Match WD + Gemini + curated careers to COL_Officials |
| `col_ml_features.py` | Compute 19 pairwise features from Neo4j node properties |
| `col_ml_train.py` | GradientBoosting CV + career recovery evaluation |
| `col_ml_score.py` | Phase 4: corpus-wide scoring (not yet rewritten) |

### Data
| File | Purpose |
|------|---------|
| `ml_data/known_careers.json` | 543 matched careers (WD + Gemini + curated) |
| `ml_data/ground_truth_pairs.csv` | 1,994 labeled pairs for training |
| `ml_data/feature_matrix.csv` | 1,994 rows × 19 features |
| `ml_data/model.joblib` | Trained GradientBoosting model |
| `ml_data/training_report.txt` | Latest CV results + feature importance |
| `ml_data/curated_cross_colony_careers.json` | 19 hand-curated careers |
| `ml_data/within_colony_gap_reviewed.csv` | Sonnet-reviewed gap pairs |
| `ml_data/name_variant_reviewed.csv` | Sonnet-reviewed name variant pairs |
| `ml_data/cross_colony_reviewed.csv` | Sonnet-reviewed cross-colony pairs |

---

## Next Steps

1. **More human verification** — user reviewing HTML pages, exporting verified CSVs
2. **Retrain** when sufficient new verified data available
3. **Phase 4** — corpus-wide scoring with blocking rules, comparison with hand-tuned linker
4. **Iterate** — review ML vs linker disagreements, add to training data

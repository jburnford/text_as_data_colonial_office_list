# Plan: ML Career Discovery from External Ground Truth

## Context

We have **two independent sources of known careers** that were NOT produced by our linking pipeline:

1. **Wikidata harvest** (`wikidata_harvest/merged_all_people.json`) — 34,594 people with structured position data (position title, colony QID, start/end dates). ~4,000+ have colonial positions with dates and colony links.

2. **Gemini-read careers** (`llm_careers/*.json`) — 408 careers across 7 colonies where Gemini read the raw OCR and identified the same person across editions.

We have **68,335 COL_Official nodes** in Neo4j (time-sliced career stints extracted from Colonial Office Lists) and **16,259 POSSIBLE_MATCH edges** created by our hand-tuned linker.

**The problem with the previous approach:** It tried to train an ML model on labels derived from the pipeline's own POSSIBLE_MATCH edges and SAME_AS links. That's circular — the model just learns to replicate the linker's biases. Worse, using high-uncertainty edges as negatives is unreliable (some are genuine matches the hand-tuned scorer got wrong).

**The correct approach:** Use externally-verified careers as ground truth. Build a model that independently discovers career chains from raw features. Evaluate by checking how many known careers the model recovers — a **retrieval/recall** problem, not a scoring problem.

---

## Architecture: Ground Truth → Features → Discovery → Evaluation

```
Step 1: Build Ground Truth Dataset
  Wikidata positions + Gemini careers
  → Match to COL_Official nodes (Python, spot-checked by human)
  → known_careers.json: [{person_id, officials: [id1, id2, ...], source}]

Step 2: Build Pairwise Feature Matrix
  For every pair of COL_Officials that COULD be the same person
  (same surname, compatible initials):
  → Compute features (gap, domain, honours, embeddings, etc.)
  → Label: 1 if both officials appear in same known career, 0 otherwise

Step 3: Train Binary Classifier
  → "Are these two officials the same person?"
  → Trained ONLY on pairs where we have ground truth labels
  → Evaluated on held-out ground truth careers

Step 4: Apply to All Pairs
  → Score every candidate pair in the corpus
  → Report: which careers does it find? Which does it miss?
  → Compare recall against hand-tuned linker
```

**Key principle:** The Python matching script in Step 1 is NOT creating training labels for the ML model. It's matching external knowledge (WD person X held position Y in colony Z from 1890-1895) to our data (COL_Official "Smith, J." in colony Z from 1890-1896). The label comes from Wikidata/Gemini, not from our pipeline. Human spot-check catches script matching errors.

---

## Step 1: Build Ground Truth (`col_build_ground_truth.py`)

### 1a: Wikidata Career Matching

**Input:** `wikidata_harvest/merged_all_people.json` — each person has:
- `qid`, `name`, `positions[]` with `position_label`, `colony_qid`, `colony_name`, `start`, `end`

**Algorithm:**
1. Load ALL WD people who have 1+ colonial positions mapped to our colonies (2,305 people, 1,543 with dates)
2. For each WD person, for each position:
   - Map `colony_qid` → COL_Territory name (via crosswalk)
   - Extract surname from WD name (handle "FirstName LastName" → "LastName")
   - Find COL_Officials: `WHERE surname = $wd_surname AND colony = $mapped_colony`
   - Filter by initials compatibility (if WD has given names)
   - Filter by year overlap: COL_Official's [first_year, last_year] overlaps WD position's [start, end] within ±3 years
   - Score: year overlap + name specificity → pick best match(es)
3. **Key insight:** A WD person with a SINGLE position (e.g., "Inspector of Police, Ceylon, 1885-1910") may match MULTIPLE COL_Official nodes if the normalization pipeline failed to unify name variants ("J. Smith" / "Jas. Smith" / "James Smith"). These multi-match cases are the most valuable training pairs — they represent exactly the hard within-colony linking problem.
4. A WD person matching 2+ COL_Officials (whether from multiple positions OR from one position split across name variants) = **one known career** with positive pairs.
5. A WD person matching exactly 1 COL_Official = **an anchor** (useful for hard negatives: we know this official is NOT the same as other same-surname officials in that colony).
6. Output match confidence: HIGH (exact name + year overlap), MEDIUM (initial match + year proximity), LOW (surname only)

**Safeguards against false positives:**
- Only accept HIGH and MEDIUM matches for training
- Flag LOW matches for human review
- If WD person matches 5+ officials, flag as suspicious (common name)
- If COL_Official matches 2+ WD persons, flag as conflict
- Export `wd_matching_review.csv` with 100 random HIGH matches for human spot-check

**Expected yield:** ~2,000-4,000 anchored COL_Officials from 2,305 WD people + 400 Gemini careers

### 1b: Gemini Career Matching (re-match from raw careers)

**Input:** `llm_careers/*.json` — 400 careers across 7 colonies (150 with 2+ stints)

The existing `col_llm_verify.py` only confirmed 30 pairs — too conservative. Re-match ALL 400 Gemini careers directly to COL_Officials using the same matching logic as 1a. Even single-stint Gemini careers provide anchors (known identity for a COL_Official), and multi-stint careers provide positive pairs.

**Key difference from WD:** Gemini careers are within-colony (same person across time in one colony), providing training signal for the most common career pattern (slow promotion within one colony). WD careers are often cross-colony (governor of X then governor of Y). Together they cover both linking problems.

### 1c: Combine into Ground Truth File

```json
// known_careers.json
[
  {
    "career_id": "wd_Q12345",
    "source": "wikidata",
    "person_name": "Smith, John Frederick",
    "officials": ["Smith, J. F.___Ceylon___1890", "Smith, J. F.___Gold Coast___1896"],
    "confidence": "HIGH",
    "match_details": {...}
  },
  {
    "career_id": "gemini_ceylon_001",
    "source": "gemini",
    "person_name": "Twynam, W. C.",
    "officials": ["Twynam, W. C.___Ceylon___1867", "Twynam, W. C.___Ceylon___1879"],
    "confidence": "HIGH",
    "match_details": {...}
  }
]
```

**From this, derive pairwise labels:**
- Officials in the same career → positive pair (label=1)
- Officials with same surname but in DIFFERENT known careers (or one known, one unmatched) → hard negative (label=0)
- Random same-surname pairs where neither is in a known career → unlabeled (excluded from training)

---

## Step 2: Build Pairwise Features (`col_ml_features.py`, rewrite)

For each candidate pair (same surname, compatible initials), compute:

### Structural features (from COL_Official properties):
- `gap_years`: years between a.last_year and b.first_year
- `overlap_years`: temporal overlap
- `a_editions`, `b_editions`: how many editions each appears in
- `same_colony`: binary (1 if same colony, 0 if cross-colony)

### Name features:
- `name_specificity`: high/medium/low → ordinal (from COMMON_SURNAMES set)
- `initials_count`: how many initials/given names available
- `name_exact_match`: binary (canonical names identical)

### Career features (computed fresh, NOT from POSSIBLE_MATCH edges):
- `domain_match`: classify_domain(a_last_position) vs classify_domain(b_first_position)
- `position_cosine_sim`: sentence-transformer similarity on position_raw text
- `department_cosine_sim`: same for department text
- `honours_match`: compare honours lists
- `military_rank_match`: compare ranks
- `seniority_direction`: promotion/lateral/demotion
- `is_acting_a`, `is_acting_b`: boolean — extracted from `acting_status` field (already in PersonRecord) plus position text patterns ("Acting", "Ag.", "Officiating", "Temporary"). **When either is True, compute a parallel `seniority_direction_no_acting` feature** that strips the acting stint and compares the substantive positions on either side. This prevents the model from penalizing common "Acting Colonial Secretary → Chief Clerk" sequences that are actually the same person returning from furlough cover.
- `acting_pair`: boolean — True if either official in the pair has an acting appointment. Lets the model learn to discount salary/seniority fluctuations for acting stints without hard-coding the logic.

### Geographic features (cross-colony only):
- `regional_proximity`: transfer circuit analysis
- `colony_count`: how many colonies share this name

**Critical:** Features are computed from COL_Official/PersonRecord properties directly — NOT read from POSSIBLE_MATCH edge properties. This ensures the ML model works independently of the hand-tuned linker.

### Directional features (Gemini refinement: "Honours Ratchet" + "Salary Vectors"):
- `honours_ratchet`: If official A (earlier) has honours that official B (later) lacks, this is a **strong negative signal** — honours accumulate, they don't disappear. Not just "mismatch" but a directional penalty.
- `salary_progression`: If both have salary data, is B's salary >= A's (or within a reasonable range for lateral moves)? A massive unexplained drop is a negative signal.
- `honours_upgrade`: Did honours progress in the expected direction (C.M.G. → K.C.M.G. → G.C.M.G.)? This is a strong positive signal.

### Temporal decay (Gemini refinement):
- `time_decay`: Exponential penalty for gaps > 3 years. A 34-year gap should require overwhelming evidence. Computed as `exp(-gap_years / 10)` or similar — the model can learn the right decay from the data, but the raw feature should encode the gap magnitude.

### Feature leakage prevention (Gemini refinement):
- Since positive labels were selected partly on year overlap, hard negatives MUST include **temporally-overlapping same-surname pairs from different known careers**. This forces the model to learn features beyond temporal proximity.

---

## Step 3: Train Classifier (`col_ml_train.py`, rewrite)

### Training data construction:
1. For each known career with 2+ matched officials, generate all positive pairs
2. For hard negatives: same-surname pairs where officials are in DIFFERENT known careers
3. Additional negatives: career-span impossibles (>55 years combined span)
4. **Do NOT use high-uncertainty POSSIBLE_MATCH edges as negatives** (they may be correct matches the hand-tuned scorer missed)

### Hard negative sampling quotas (prevents temporal shortcut learning):
The model must not learn a trivial classifier where `gap_years < 10` → match. Force difficult negatives:
- **≥30% of negatives** must have `gap_years < 5` or `overlap_years > 0` (temporally close)
- **≥20% of negatives** must be same-colony pairs (geographically close)
- **Hardest tier:** same decade + same colony + different known career — these force the model to rely on `department_cosine_sim`, `salary_progression`, `honours_ratchet` rather than temporal/geographic separation
- If insufficient natural hard negatives exist from known careers, supplement with synthetic negatives: pairs of officials with the same surname and overlapping tenures in the same colony where we are confident they are different people (e.g., both appear in the same edition simultaneously in different roles)

### Model:
- GradientBoostingClassifier (sklearn) — handles mixed feature types, captures interactions
- class_weight='balanced' to handle imbalance
- Stratified 5-fold cross-validation

### Evaluation (the key metric):
**Career recovery rate** — for each known career in the test set:
1. Does the model predict P(same_person) > 0.5 for at least one pair of officials in that career?
2. If the career has 3+ officials, does the model find the full chain?

Compare against hand-tuned linker:
- For each test career, check if POSSIBLE_MATCH edges exist between the officials
- Report: careers found by ML only, by hand-tuned only, by both, by neither

### Anti-overfitting checks:
- Per-source recall: WD careers vs Gemini careers (should be similar)
- Per-seniority recall: senior vs mid-level careers
- Cross-colony vs within-colony recall

---

## Step 4: Apply & Report (`col_ml_score.py`, rewrite)

### Discovery mode (primary):
- Generate all candidate pairs (same surname, compatible initials) across the corpus
- Use blocking rules to manage scale (Gemini refinement):
  - Block 1: exact surname + same colony (within-colony careers)
  - Block 2: exact canonical_name across all colonies (cross-colony transfers)
  - Block 3: first 3 chars of surname + same department (catches OCR name variants)
  - Block 4: **phonetic surname match** — Double Metaphone on surnames, allowing pairs where the primary metaphone code matches even if the string doesn't. Catches MacDonald/McDonald, Smyth/Smythe, Thomson/Thompson, etc. Also allow Levenshtein distance ≤ 1 for surnames > 5 characters. This expands recall beyond the OCR/LLM extraction error ceiling without polluting the training data (applied only in discovery, not training).
- Score each pair with the trained model
- Build connected components from high-confidence pairs (P > 0.7)
- **Transitivity trap prevention (Gemini refinement):** Before finalizing components, validate that no component contains temporal impossibilities (two full-time posts in different non-federal colonies in the same year, or career span > 55 years). Sever the weakest edge that creates the impossibility.
- Report: how many careers discovered? How many match known ground truth?
- Export discovered careers for human review

### Comparison mode:
- For existing POSSIBLE_MATCH edges: compute ML score alongside hand-tuned uncertainty
- Report disagreements: edges where ML says "yes" but hand-tuned says "no" and vice versa
- These disagreements are the interesting cases to review

---

## Files to Create/Rewrite

| File | Purpose |
|------|---------|
| `col_build_ground_truth.py` | **NEW**: Match WD+Gemini careers to COL_Officials, export known_careers.json |
| `col_ml_features.py` | **REWRITE**: Compute features from COL_Official properties directly (not from POSSIBLE_MATCH edges) |
| `col_ml_train.py` | **REWRITE**: Train on ground truth pairs, evaluate by career recovery rate |
| `col_ml_score.py` | **REWRITE**: Discovery mode + comparison mode |

| File | Status |
|------|--------|
| `col_llm_verify.py` | **KEEP**: Already built, verified 408 Gemini careers |
| `llm_careers/*.json` | **KEEP**: 408 careers across 7 colonies |
| `llm_output/*_confirmed.csv` | **KEEP**: 26 confirmed pairs from verification |

## Files to Read (not modify)

| File | What we use |
|------|-------------|
| `wikidata_harvest/merged_all_people.json` | WD people with positions, dates, colonies |
| `col_link_officials.py` | `classify_domain()`, `compute_name_specificity()`, `COMMON_SURNAMES` |
| `col_normalize_names.py` | `initials_compatible()`, `clean_given_names()` |
| `col_link_cross_colony.py` | `compute_regional_proximity()`, `compute_honours_match()`, transfer circuits |

---

## Execution Order

### Phase 1: Ground Truth Construction
1. Build `col_build_ground_truth.py`
2. Run: maps WD people → COL_Officials, combines with Gemini careers
3. Human spot-checks 100 random WD matches from `wd_matching_review.csv`
4. Fix any matching errors found in spot-check
5. **Expected output:** 1,000-2,000 known career pairs (positive labels)

### Phase 2: Feature Engineering
6. Rewrite `col_ml_features.py` to compute features from COL_Official properties
7. Generate pairwise feature matrix for all ground-truth pairs + hard negatives

### Phase 3: Training & Evaluation
8. Rewrite `col_ml_train.py` with career-recovery evaluation
9. Train, evaluate, iterate on features
10. **Key metric:** What % of known careers does the model recover?

### Phase 4: Corpus-Wide Discovery
11. Rewrite `col_ml_score.py` for discovery mode
12. Run on full corpus, compare against hand-tuned linker
13. Review disagreements — these are the new discoveries

### Phase 5: Network-Based Re-scoring (future enhancement)
14. **Entourage/cohort detection:** Senior officials (Governors, Chief Secretaries) frequently brought Private Secretaries, ADCs, and trusted administrators when transferring between colonies. After Phase 4 produces high-confidence career chains, re-score low-confidence cross-colony pairs by checking if other officials make the same geographic jump in the same year. A `shared_cohort_transfer` feature (count of co-transferring officials, weighted by their link confidence) can bootstrap identity for otherwise ambiguous names. This requires a multi-pass approach: first build confident chains, then use those chains as context for uncertain ones. Deferred because it creates a chicken-and-egg dependency and the number of cases where this is the deciding (not merely confirmatory) signal is likely small.

---

## Alternative: Splink (Probabilistic Record Linkage)

Gemini suggested using **Splink** (UK Ministry of Justice's probabilistic linkage library) which uses Fellegi-Sunter models with Expectation-Maximization — it can train match weights WITHOUT labeled data. This is worth considering as a complement or alternative to sklearn:

**Pros:** Handles scale (millions of records), learns feature weights automatically, designed for messy administrative data, handles blocking natively.

**Cons:** Less control over feature engineering, may not capture the domain-specific signals (honours ratchet, transfer circuits) as well as a custom model.

**Decision:** Start with the sklearn approach (Step 3) since we have ground truth and want interpretable features. If sklearn career recovery rate is <70%, try Splink as a fallback. The ground truth dataset (Step 1) works for evaluating either approach.

---

## Verification

1. **Ground truth quality**: Human reviews 100 random WD→COL_Official matches. Target: >95% correct.
2. **Training data size**: Expect 1,000-2,000 positive pairs, 2,000-4,000 negative pairs.
3. **Career recovery rate**: What % of held-out known careers does the model find? Target: >80%.
4. **Comparison with hand-tuned linker**: How many careers does ML find that the linker missed? Vice versa?
5. **False positive rate**: Of ML-discovered careers NOT in ground truth, how many are real? (sample review)
6. **Elite bias check**: Recovery rate for mid-level Gemini careers vs elite WD careers should be within 10%.

---

## Amendments (2026-03-17, post-Gemini review)

Four issues identified by external review, three incorporated immediately:

| # | Issue | Verdict | Action taken |
|---|-------|---------|--------------|
| 1 | **Surname blocking recall ceiling** — exact string match caps recall at OCR/LLM error rate | Valid | Added Block 4 (Double Metaphone + Levenshtein ≤1) to Step 4 discovery phase. Not applied to training to keep labels clean. |
| 2 | **Acting appointment volatility** — "Acting Colonial Secretary → Chief Clerk" penalized as extreme demotion | Valid, important | Added `is_acting_a/b`, `acting_pair`, and `seniority_direction_no_acting` features to Step 2. Acting status already extracted in PersonRecord data. |
| 3 | **Entourage/cohort effect** — co-transferring officials as identity signal | Valid but premature | Deferred to Phase 5 as network re-scoring pass. Requires high-confidence chains first (chicken-and-egg). |
| 4 | **Hard negative sampling bias** — easy negatives let model rely on temporal separation | Critical | Added explicit sampling quotas to Step 3: ≥30% temporally close, ≥20% same-colony, with hardest-tier mandate for same-decade-same-colony pairs. |

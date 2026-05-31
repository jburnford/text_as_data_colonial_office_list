# Session Report — May 30, 2026

**Branch:** `claude/repo-file-structure-w7jxq`
**Focus:** Phase 0 of the colony-reports extraction plan — source canonicalization and colonial-structure discovery
**Outcome:** Three new deliverables built, validated against all 2,946 corpus files, committed and pushed. No LLM was available in this environment, so all work is deterministic/statistical — and that turned out to be the point.

---

## TL;DR

We built the foundation layer for extracting structured data from the Colonial Office List "report" sections, and in the process reframed what that layer is *for*. Three artifacts:

1. **`col_canonicalize_reports.py`** — a deterministic canonicalizer that turns every parsed `.txt` (Markdown *or* plain text) into one block representation, with a content-based **boundary-integrity detector** that distinguishes legitimate federation mega-entries from misfiled/contaminated files.
2. **`col_mine_corpus_patterns.py`** — a corpus-scale pattern miner that *derives* the colonial federation structure, the floating-appendix set, and the empirical section/indicator vocabularies — with no hand map — then uses an iterative decontamination loop and acts as a ruler for the curated map.
3. **`taxonomy/colony_families.json`** — a historically-curated, era-annotated authoritative map of 20 colonial federations/groupings, closing the gaps the corpus can't resolve on its own.

The intellectual arc: **boundary integrity matters more than heading normalization → derive structure from scale, don't train on a gold set → but derivation is fragile in the long tail, so reconcile with curated history.**

---

## The work, in sequence

### 1. Phase 0 canonicalizer (`col_canonicalize_reports.py`)

Grounded in a close read of representative files across eras, the canonicalizer segments each file into typed blocks — `colony_header`, `heading`, `prose`, `table`, `dot_leader` — each carrying line/char back-pointers to the source for auditability. Key realities it handles:

- **Headings are dominated by bare `Title.` lines and inline `Subheading.—text`** (e.g. `Railways.—There are four lines…`), *not* Markdown `###` — even in 1930s files. 4,221 inline em-dash subheadings exist corpus-wide.
- **Pipe tables are ragged** — header column counts rarely match data rows, and "Total" rows lose their leading pipe. The parser keeps all rows with a `ragged` flag rather than forcing a rectangle.
- **Dot-leader lines** (`Rainfall in 1898 …… 47-76 ins.`, where `-` is OCR for a decimal point) are captured as a distinct kind.
- **Degenerate-file triage**: empty / very_short / short / no_tables / garbled-or-lowercase filename / possible_truncation (vs the colony's own median) / size_outlier.

Heading→section-slug mapping is the one part that genuinely needs meaning; a conservative keyword fallback already covers **85% of files**, and the rest is stubbed (`needs_model=true`) for a later LLM pass.

### 2. Boundary-integrity detector — the first reframe

The first triage flag (`anomalous_giant`, size-based) conflated three situations needing **opposite** handling, and dangerously false-flagged the federation mega-entries that are the report track's prime recovery targets:

| File | Size | Truth | Old flag |
|---|---|---|---|
| Ascension 1888 | 212k | volume dump | flagged, wrong reason |
| British Honduras 1910 | 53k | **wrong colony** (Canada section misfiled) | flagged, mislabelled |
| Australia 1919 | 82k | **legitimate federation** (recovery target) | **false-flagged** |
| Aden 1922 | 6.9k | honours-list bleed | **missed** |

Replaced it with a **content-based classifier** using a colony-name gazetteer (built free from the 2,946 filenames) and a federation→sub-unit allow-list:

- `federation_nested` — the entry's *own* sub-units appear inside it → recovery target, stamp sub-units.
- `multi_colony_misparse` — *unrelated* colonies concatenated → quarantine. Corroboration-gated (≥4 unrelated headers or a size outlier) so incidental prose mentions don't false-trigger.
- `appendix_contamination` — honours / cross-colony markers (reuses the personnel pipeline's detector).
- `volume_dump` — absolute-size backstop (header detection undercounts OCR-mangled dumps).

### 3. "Use scale, not a gold set" — the methodology pivot

A key steer landed mid-session: *the data is too irregular for a 15–20 file gold standard to train on — use it only to validate, and derive the patterns from the full corpus.* **Gold standard = a ruler, not a teacher.**

Built `col_mine_corpus_patterns.py` to prove it. With **no hand map**, pure colony-name co-occurrence across 2,946 files:

- **Recovered and extended** the federation families (Canada gained Quebec/Alberta/Saskatchewan; Gold Coast gained Ashanti/Togoland; discovered Gambia/Gold Coast families never hand-coded), merging parent **name-drift** automatically (FMS/UMS/Straits/"Malaya" → one family).
- **Surfaced the floating-appendix set** (Miscellaneous Islands, Ascension, Tristan da Cunha, Aden, Other Miscellaneous Possessions) as the promiscuous hub nodes that bleed across files.
- **Produced the empirical taxonomies** by frequency-ranking headings (civil establishment, executive/legislative council, education, history, constitution, population, finances, imports/exports…) and table columns (year, revenue, expenditure, total tonnage, from/to U.K., males/females, value…).

Two hard lessons fell out, both illustrating that the irregularity is the crux:
- **Naive clustering over-merges** — appendix hubs bridge unrelated families (one run fused Windward+Pacific+random hosts into a 21-member blob). Fix: only low-promiscuity children count as merge evidence.
- **Misparses contaminate the derived structure** — the British Honduras→Canada misparse makes `british_honduras` look like a Canada parent-variant.

### 4. Iterative decontamination — and the limit of derivation

Built a **detect → exclude → re-mine** loop: seed exclusions from the validated boundary detector, *exclude before mining* (breaking the chicken-and-egg), re-detect with the derived families, iterate to a fixed point (converges in one round). It removed the contamination — `british_honduras` stopped masquerading as a Canada parent; `saskatchewan` (whose only header evidence lived *inside* the misparse) dropped out.

But the loop then false-flagged `UNFEDERATED_MALAY_STATES` — a *sparse* federation whose own members looked foreign once neighbours were excluded. **That is the honest boundary of pure derivation: where the corpus is thin, it can't confirm what curated knowledge knows.** Resolution: **reconcile, don't replace** — a nesting is allowed if *either* the derived family *or* curated knowledge permits it.

### 5. Historical curation — closing the gaps (`taxonomy/colony_families.json`)

Encoded the administrative history of the Empire into an authoritative, era-annotated map of 20 families, cross-checked against the project's regional guides. It is now the single source of truth (the boundary detector loads it; the inline dict is a fallback). History resolved what the data couldn't:

- **Ascension + Tristan da Cunha → St Helena**, not Aden — the *List* prints these Atlantic islands in the same "miscellaneous" appendix region as Aden, so co-occurrence had fused them.
- **Gibraltar is standalone**, not part of the Gambia (a derived leak).
- **The Rhodesias form their own federation** and the **High Commission Territories are separate** from the Union of South Africa — but they appear under the SA High Commissioner in early editions, so encoded as strict `members` (for stamping) vs `associated_territories` (administered-with, for the allow-list).
- Added under-evidenced families: Nigeria, East Africa High Commission, Gold Coast, West African Settlements, Falklands + dependencies, British Borneo, plus dependency notes.

The miner then stopped computing a competing map and instead became a **ruler for the curated one** (`curated_map_coverage`): it found real variant gaps (Kingdom of Tonga, Nyasaland Protectorate, Pitcairn Islands Group), which were closed. The 7 names still unexplained are correctly non-members (appendix containers; NZ's Cook Islands; the OCR misspelling `grenade`; standalone Somaliland/Bahamas).

---

## Validation (all 2,946 files, ~20–25s, zero errors)

| Metric | Value |
|---|---|
| Files with ≥1 parsed table block | 2,653 (90%) |
| Files with a heading candidate | 2,751 (93%) |
| Files with ≥1 keyword-mapped section slug | 2,510 (85%) |
| `federation_nested` | **250** (was 65 under the hand map) |
| `multi_colony_misparse` | **21** (all manually confirmed genuine) |
| `appendix_contamination` | 7 |
| `volume_dump` | 2 (Ascension 1888 = 212k w; Tristan da Cunha 1898 = 200k w) |
| `possible_truncation` | 178 |
| `very_short` / `empty` | 103 / 1 |
| Curated families | 20 |

Spot-checks confirmed: British Honduras/Weihaiwei stay flagged misparse; Australia/Canada/South Africa/Straits/Leeward nest correctly; incidental mentions (Queensland naming St Lucia) are not flagged.

---

## Methodological takeaway

**Scale-derivation and curated knowledge are complementary, not competing.** Derive where evidence is dense; lean on curation in the long tail; reconcile by union; reserve the gold standard for *measuring* and for *adjudicating* the handful of genuinely ambiguous cases — never for training rules. This now sits in the plan's design principles.

---

## Open questions / next steps

1. **Gold validation set** — still none. Per the steer, this is the one thing a gold set is genuinely for: *measuring* recall/precision of the canonicalizer and boundary detector (not deriving them).
2. **Misparse handling** — quarantine the 21 `multi_colony_misparse` files, or build a splitter that carves the misfiled foreign sections into their own canonical docs?
3. **Sub-unit stamping (Track A)** — use the curated strict `members` with edition-year disambiguation for the era-overlap cases (Dominica Leeward↔Windward 1940; Tobago→Trinidad 1889; Seychelles→separate 1903; Newfoundland→Canada 1949; Lagos across West Africa Settlements/Gold Coast/Nigeria).
4. **Schema freeze** — lock the canonical block schema before bulk-generating `generated/reports_canonical/*.json` (currently regenerable, not committed).
5. **`british_borneo`** has no umbrella file, so its members read as "unconfirmed" (inert in the allow-list; kept for documentation) — confirm in review.

---

## Files changed this session

| File | Status | Purpose |
|---|---|---|
| `col_canonicalize_reports.py` | new | Phase-0 canonicalizer + boundary-integrity detector |
| `col_mine_corpus_patterns.py` | new | corpus-scale family/appendix/taxonomy miner + decontamination loop + curated cross-check |
| `taxonomy/colony_families.json` | new | historically-curated authoritative family map (20 families) |
| `generated/corpus_patterns.json` | new | derived patterns + coverage report (regenerable artifact) |
| `COLONY_REPORTS_EXTRACTION_PLAN.md` | updated | Phase-0 status, design principles, methodology |
| `COLONY_REPORTS_SESSION_HANDOFF.md` | updated | full session trail + design notes for the next session |

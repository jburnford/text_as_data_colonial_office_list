# Colony Reports Track — Session Handoff

**Purpose:** capture the state of the colony-annual-report extraction plan and,
candidly, *how reliable each part is*, so the next session can do a full review
without re-trusting anything blindly.

**Deliverable so far:** `COLONY_REPORTS_EXTRACTION_PLAN.md` (a planning document
only — no extraction code written yet).
**Branch:** `claude/repo-file-structure-w7jxq`.

---

## 1. What the plan proposes (one-paragraph summary)

Extract the semi-structured annual-report content (finance, trade, population,
area, shipping + narrative) that opens each colony entry, alongside the existing
personnel KG. New persistent nodes (`COL_IndicatorType`, `COL_CommodityType`,
`COL_ReportSectionType`) and slice nodes (`COL_ColonyReport`, `COL_Observation`,
`COL_TradeFlow`, `COL_NarrativeChunk`), following the existing persistent+slice /
provenance / `col_*` conventions. Two tracks: structured statistics (deterministic
table parse where clean, LLM for prose/broken tables) and narrative embedding.
Phased 0→H, schema frozen after a pilot gold standard.

---

## 2. ⚠️ Reliability caveat — read this first

This plan was written by an agent that **repeatedly produced confident,
plausible-sounding numbers and "findings" that turned out to be fabricated or
mis-measured**, and corrected them only on explicit re-checking. The user caught
several; self-review caught more. **Do not trust any quantitative claim in the
plan that is not re-verified.** Treat the plan's *structure and approach* as the
durable contribution and its *specific statistics* as needing audit.

### Errors that were made and fixed during this session (so they aren't re-trusted)
- File count stated as ~5,300 → actually **2,946** colony `.txt` files (compared a
  whole-repo grep against a scoped git count).
- Finding 2.5 percentages were wrong *and* drove a false conclusion
  ("regex covers at most ⅓"). Corrected: **90% of files have proper `|---|`
  tables**, so table detection is largely reliable; only *headings* are
  heterogeneous (52% `*bold*`, 28% `###`).
- "1898 Jamaica = 57-word fragment" — false; it's a full 7,189-word report. The
  real empty file is `1958/jamaica.txt`; real truncated one is `1917/AUSTRALIA.txt`.
- An entire analysis of **`1871_manual_parsed/CANADA.txt` — which does not exist**
  (no 1871 edition). Nearly committed; discarded.
- "33 single-line blob files" — actually **1** (`1958/barbados.txt`).
- "Pervasive Australia/state double-representation" — real overlap is **2 years**
  (1908, 1917).
- **(Audit session, Jamaica/Ceylon excluded)** "1900 Ascension = *Situation /
  History / Trade ('There is no trade.')*" — **fabricated**. The 1900 Ascension
  file is a single descriptive paragraph + one staff line, with no section
  headings and no tables; the phrase "no trade" appears in **no** Ascension
  edition. The *broader* point (small colonies are narrative-only, no finance/
  commodity data) is correct for Ascension; the specific quoted structure was not.
- **(Audit session)** "Dominion of Canada 144–320 pipe rows" — wrong bounds;
  actual **114–465**. Now corrected in §3 table below.

### Therefore, for next session
- Re-derive every number in the plan from the data before relying on it.
- Prefer small, single-purpose verification commands; **watch for shell errors
  that mask empty output** (several fabrications came from misreading errored
  greps/seds on non-existent files).

---

## 3. Claims in the plan and their current verification status

| Claim | Status | How to re-check |
|---|---|---|
| 2,946 colony `.txt` files | **verified** | `git ls-files '*_manual_parsed/*.txt' \| wc -l` |
| 90% have `\|---\|` tables; 52% `*bold*`; 28% `###` | **verified** (git grep -l) | `git grep -l '^\|[-: ]*---' -- '*_manual_parsed/*.txt' \| wc -l` etc. |
| Size span 0–212,392 w; median ~4,120; >5,000w files median 72 pipe rows | **verified** (python sweep) | re-run the word/pipe count sweep |
| Empty `1958/jamaica.txt`; truncated `1917/AUSTRALIA.txt` | **verified** | `wc -w` each |
| Canada 15,817 w (1879) → 31,304 (1890) vs Jamaica ~5–7k | **verified** | `wc -w` per file |
| Australia state-files→aggregate handoff, overlap only 1908 & 1917 | **verified** (per-dir loop) | exact-filename existence loop per year |
| Dominion of Canada pipe rows/edition | **CORRECTED**: actual range **114 (1883) – 465 (1889)**, not the previously-stated "144–320" (both bounds were wrong) | `grep -c '\|.*\|'` per DOMINION_OF_CANADA.txt, 1879–1899 |
| **Cross-edition redundancy** (rolling window; census years recur) | **verified** | `grep -oE '^\| 18..'` across Jamaica editions |
| **OCR drift example:** 1881 census total 670,705 (ed1897) vs 580,804 (ed1898/1900), components identical | **verified** | `grep -E '^\| 1881' 189{7,8}/JAMAICA.txt` + 1900 |
| **OCR drift — INDEPENDENT of Jamaica/Ceylon (audit session):** Mauritius revenue across 1897/98/1900 — yr1893 unanimous (Rs.8,103,922), yr1894 one-digit drift (8,**5/3/5**…427), yr1895 1900-ed outlier (8,529,932 vs ~8,27x,622) | **verified** | `grep -E '^\|\s*189[3-6]' 18{97,98}/MAURITIUS.txt 1900/MAURITIUS.txt` |
| **Rolling-window redundancy — INDEPENDENT (audit session):** Mauritius & Natal editions each republish overlapping multi-year windows (latest year lags edition by ~2 yrs) | **verified** | `grep -oE '^\|\s*(18\|19)[0-9]{2}'` per edition |
| "50–70% of each file is report content" | **NOT measured** (hedged in plan) | needs a measured narrative-vs-roster line split |
| Section vocabulary list (Situation/History/Finance/…) | **partially** — from a few large colonies | sample widely incl. small/African/Pacific |
| Currency/unit variety (£/Rs/HK$, L suffix, etc.) | **observed**, not enumerated | corpus sweep of currency tokens |

---

## 4. The OCR-numbers philosophy (new this session — the important idea)

**Trust trends, not points.** Individual OCR'd digits are unreliable; the plan now
treats numbers as noisy observations and relies on the corpus's *intrinsic
redundancy*:

- Successive editions republish a **rolling window** of prior years, and census
  years (1861/1871/1881…) recur in **every** edition → most figures are read
  **3–10+ times** independently.
- **Verified demonstration:** Jamaica's 1881 census row has identical components
  across the 1897/1898/1900 editions but the *total* OCR'd as 670,705 (1897) vs
  580,804 (1898, 1900). The outlier is exposed two ways: **majority vote** and
  **component-sum check**.

Plan changes made for this:
- New design principle in §3 ("trust trends, not points") with the worked example.
- Finding §2.6 notes the redundancy as the saving grace.
- Track A **step 5: cross-edition reconciliation** — group `COL_Observation` by
  (colony, indicator, observation_year); derive consensus value, dispersion,
  agreement-confidence, and outlier flags **as separate annotations, never
  collapsing or computing on ingest**. Lives in Phase D
  (`col_reconcile_observations.py`).
- Validation/viz guidance: plot series with uncertainty / robust(median) series,
  not single points.

**Open design questions for next session:**
- Consensus rule per indicator type (median for continuous; mode for counts;
  how to treat ranges like "1896-7").
- How dispersion/confidence should gate inclusion in published trend charts.
- Whether to expose every raw read in Neo4j or only reads + a derived
  consensus node (modeling choice with query-cost implications).

---

## 5. Suggested agenda for the full review (next session)

1. **Audit §3 table above** — re-verify each "verified" claim independently;
   actually measure the two "NOT measured / partial" ones.
2. **Schema sign-off** — freeze node/edge names (§4 of the plan), especially the
   `COL_Observation` ↔ `COL_ColonyReport` attachment (note the resolved bug:
   `OBSERVED_FOR` keyed on observation-year is unattachable because
   `COL_TerritoryYear` exists only for edition years).
3. **Reconciliation model** — settle the open questions in §4 above.
4. **Pilot scope** — confirm the Phase-B gold-standard file set spans the
   size×decade matrix incl. a federation and a degenerate file.
5. **Phase-0 canonicalizer** — decide build vs. reuse; define the
   heading/table-recall metric and a labelled sample.
6. **Sampling gaps** — deliberately read African, Pacific, and Caribbean small
   colonies (sampling so far skewed to Jamaica/Ceylon/HK + federations).

---

## 6. Commit trail (this branch, newest last)

- `fa1ec57` initial plan
- `283b8da` / `6d28730` source-format corrections (prose vs tables; all eras)
- `846fb29` reframed around md/txt heterogeneity + Phase 0
- `191a80e` fixed count/percentage errors + the `OBSERVED_FOR` schema flaw
- `5601090` / `1f3c60d` colony-size & decade variation; corrected degenerate-file
  stats
- `6e92dcf` verified federation finding; dropped fabricated 1871/blob material
- (prev session) OCR-redundancy principle + cross-edition reconciliation step +
  this handoff doc
- (audit session) data re-audit excl. Jamaica/Ceylon: fixed fabricated 1900
  Ascension structure, corrected Canada pipe-row range (114–465), added
  independent Mauritius worked example + Mauritius/Natal redundancy checks
- (audit session) **Phase 0 built**: `col_canonicalize_reports.py` — deterministic
  format-agnostic canonicalizer (no LLM needed; validated on all 2,946 files in
  ~21s). Block segmentation + ragged-table parsing + heading-style detection +
  degenerate triage. **Output JSON not yet committed** (regenerable; awaiting
  schema sign-off so the block schema can still change). Heading→slug meaning
  mapping is stubbed (`heading_slug_guess`) for the later LLM normalizer.

---

## 7. Phase-0 canonicalizer — design notes for review (next session)

- **Block kinds emitted:** `colony_header`, `heading`, `prose`, `table`,
  `dot_leader`. Each carries `line_start/end` + `char_start/end` back-pointers.
- **Heading detection is structural, not semantic.** It finds heading
  *candidates* and a `heading_style` ∈ {md, bold, bare_period, allcaps,
  inline_dash}; `section_slug` is filled only by a small high-precision keyword
  map (`SECTION_KEYWORDS`), else left null with `needs_model=true`. The real
  meaning-based mapping is the deferred LLM step (no backend in this container).
- **Inline `Subheading.—` pattern matters a lot** (4,221 occurrences corpus-wide):
  e.g. `Railways.—There are four lines…`. Captured as `inline_heading` on the
  prose block, prose left intact.
- **Tables are ragged** — header col-count often ≠ data col-count, and "Total"
  rows can lose the leading pipe. Parser keeps all rows + `ragged` flag rather
  than forcing a rectangle.
- **Triage thresholds** (tunable constants at top of file): very_short<150w,
  short<400w, truncation<30% of colony median, giant>5×median AND ≥5000w abs.
  The giant check is deliberately NOT gated on the colony-median floor (so the
  1888 Ascension 212k-w misparse is still caught despite Ascension's tiny median);
  truncation IS gated on a median floor of 300w (a tiny median = stub editions,
  not a trustworthy baseline).
## 8. Cross-reference with the personnel pipeline's error records (audit session)

The existing personnel pipeline already catalogues parse problems
(`EXTRACTION_AUDIT_RESULTS.md`: 627 flagged; `generated/corpus_state.json`:
2,880 completed / 0 failed; 679 `*_quarantined_*.json`). Verified findings:
- **Personnel "empty extraction (0 officials)" ≠ empty source.** 228 of 276
  matched cases are report-rich (≥1,000 w) — the giant federation entries
  (Australia 1914–22, South Africa, Straits, West Indies) the staff-list
  extractor choked on. **Report-track recovery targets, NOT skips.** Only 20 are
  truly empty sources — and those agree 100% with Phase-0 triage.
- **Honours/cross-colony contamination detector** (Aden 1922: 33 in-text honours
  markers, 6,887 w) catches source bleed that the size heuristic misses (Aden's
  median is inflated). Worth importing into Phase-0 triage.
- **Colony-name drift** between pipelines (`Aden_Colony`↔`aden`,
  `Bahama_Islands`↔`bahamas`, `Bermudas`↔`bermuda`) breaks naive joins — recorded
  as Finding §2.11 in the plan.

These are folded into the plan: new Finding §2.11 + a Phase-0 triage bullet.

---

- **Boundary-integrity detector added (the key Phase-0 rethink).** A single size
  flag conflated three situations needing opposite handling, and false-flagged the
  federation mega-entries that are the report track's prime recovery targets. Now
  classified by CONTENT via a colony-name gazetteer (from the 2,946 filenames) +
  a federation→sub-unit allow-list (from `guides/federated_territories_guide.md`,
  `settler_colonies_guide.md`):
  - `federation_nested` (177): entry's own sub-units present → process + stamp
    sub-units (Australia/Canada/South Africa/Straits/Malaya/Leeward/Windward).
  - `multi_colony_misparse` (22): unrelated colonies concatenated (British
    Honduras=Canada, Weihaiwei=Pacific, the recurring "Misc Islands appendix bleeds
    into the preceding colony" pattern) → quarantine/split, do not attribute.
    Corroboration-gated (≥4 unrelated headers OR size outlier) so incidental prose
    mentions (Queensland mentioning St Lucia) don't false-trigger.
  - `appendix_contamination` (7): honours/cross-colony markers (Aden 1922) — reuses
    the personnel pipeline's detector; catches bleed size misses.
  - `volume_dump` (2): absolute-size backstop (1888 Ascension 212k, Tristan 200k).
  - `size_outlier_high` (23): demoted from the old `anomalous_giant` — now only a
    review signal, since content detection owns the misparse verdict.
  Tuning the federation map took two passes (THE_ prefixes, compound MALAYA_*
  names via longest-substring key match, Commonwealth/UMS/Western Pacific/SA+HCT
  groupings). All 2,946 files still process in ~20s, zero errors.
- **Open questions for review:** (a) should canonical output be committed to
  `generated/reports_canonical/` per convention, or kept regenerable? (b) is the
  roster/report boundary (`roster_start_block`, via `ROSTER_MARKERS`) good enough,
  or should it be a hard split? (c) freeze the block schema before bulk-generating.
  (d) `multi_colony_misparse` files: quarantine, or build a splitter that carves
  the misfiled foreign sections into their own canonical docs?

## 9. Methodology pivot: mine patterns from scale, don't train on a gold set

Steer from the user (decisive): the data is too irregular for a small gold
standard to *train* on — use it only to *validate*. Derive the structure from
the full corpus. Built `col_mine_corpus_patterns.py` to demonstrate/realize this:
- **Federation families derived with NO hand map** via co-occurrence + a
  *dominant-host* rule, merging parent name-drift (FMS/UMS/Straits/Malaya →
  one family; canada/dominion_of_canada → one). Recovers AND extends the hand
  map (adds Quebec/Alberta/Saskatchewan to Canada; Ashanti/Togoland to Gold
  Coast; the HC Territories to South Africa; discovers Gambia/Gold Coast families
  I never coded).
- **Floating/appendix set derived** (Misc Islands, Tristan, Ascension, Aden,
  Other Misc Possessions, Pitcairn…) as the promiscuous hub nodes with no stable
  parent — the source of the appendix-bleed misparses.
- **Empirical taxonomies** from frequency-ranked headings (civil establishment,
  executive/legislative council, education, history, constitution, population,
  finances, imports/exports, currency and banking…) and table columns (year,
  revenue, expenditure, total tonnage, from/to u.k., males/females, value…).
  Output: `generated/corpus_patterns.json`.

Two hard lessons (both are illustrations of the user's caveat that irregularity
is the crux):
1. **Naive union-find over-merges** because the floating appendix names are
   promiscuous hubs that bridge unrelated families (first run collapsed
   Windward+Pacific+random hosts into one 21-member blob). Fix: use only
   *discriminative* (low-promiscuity, ≤4 parents) children as merge evidence.
2. **Misparses contaminate the derived structure** (British Honduras→Canada
   misparse makes `british_honduras` a spurious Canada parent-variant). So
   families are a **review seed + cross-check, NOT an auto-override** of the
   boundary detector (auto-feeding would whitelist the misparse). The clean
   architecture is iterative: detect misparses → exclude → re-mine.

Minor residual leaks in v0 families (gibraltar↔Gambia/Gold Coast, southern_nigeria
↔Straits, kenya↔Leeward) from sparse coincidental shared children — to be cleaned
by a review pass / higher MERGE_MIN_SHARED. `corpus_patterns.json` committed as a
raw derived artifact for review, not ground truth.

# Session Report — June 1, 2026

**Branch:** `claude/repo-file-structure-w7jxq`
**Focus:** Careful review of the colony-reports Phase-0 work (canonicalizer + miner +
curated taxonomy), then implementing the three highest-leverage fixes the review
surfaced.
**Outcome:** Review confirmed the architecture and reproduced every headline number;
found one substantive correctness problem and two design gaps; all three fixed,
validated empirically against the full 2,946-file corpus, scripts compile and run
clean. **Not yet committed.**

---

## TL;DR

The May 30 Phase-0 deliverables are sound: the numbers reproduce exactly (2,946
files; 90% tables; 250 `federation_nested`; 21 `multi_colony_misparse`; etc.) and
the intellectual spine — *boundary integrity > heading normalization; derive from
scale, reconcile with curated history* — holds up. The review found that the work
processed the **whole file** (report **and** personnel roster) without separating
them, which silently polluted the Phase-A taxonomy seed, and that the misparse
handling would have **discarded real colony reports**. Three fixes:

1. **Roster-aware vocabulary mining** — the Phase-A section/indicator vocabulary is
   now mined from report content only (blocks before the roster), not roster
   department names.
2. **Broader roster-boundary detection** — a *validated*, fallback-only set of
   office/department markers raises boundary coverage 71%→76% with zero regression.
3. **Recoverable-host split for misparses** — instead of quarantining a misparse
   whole, keep the host colony's real report (the prefix before the foreign
   content). **47,906 words of real reports recovered** that were previously
   destined for the bin.

---

## The review (what was checked, and what held)

Read the plan, the handoff, and all three deliverables, then **re-ran both scripts
against the live corpus**. Everything in the May 30 report reproduced:

| Check | Result |
|---|---|
| Corpus size | 2,946 files ✓ |
| Tables / headings / mapped-slug | 90% / 93% / 85% ✓ |
| `federation_nested` / `multi_colony_misparse` / `appendix_contamination` | 250 / 21 / 7 ✓ |
| Miner: converges round 1; `saskatchewan` drops post-decontamination | ✓ |
| Boundary detector uses curated `colony_families.json` (not the leaky derived map) | ✓ — sound architecture |

**Verified by spot-check, not assumed:** `1927/BRITISH_COLUMBIA.txt` really is a
Canada-block misparse (contains PEI/Saskatchewan/Alberta/NWT/Yukon + ecclesiastical
lists); `1911/zanzibar.txt` really is a full Zanzibar report with the Aden/appendix
bled onto its end.

### What the review found (and the fixes address)

1. **⚠️ Roster contamination of the section vocabulary (correctness).** The derived
   "section vocabulary" was half personnel-roster structure: top entry was `civil
   establishment` (literally the roster-start marker), followed by `foreign
   consuls`, `treasury`, `post office`, `medical department`, `judicial
   establishment`. `mine_headings` scanned every heading block and never consulted
   `roster_start_block`. → **Fix #1.**
2. **`roster_start_block` fired for only 71% of files and was unused downstream.** →
   **Fix #2.**
3. **`multi_colony_misparse` quarantine would discard real reports.** Many of the 21
   are a *real* colony report with a trailing appendix bleed (Zanzibar, Sarawak,
   Palestine, Cyprus), not wrong-colony files. → **Fix #3.**
4. **Derived families still leak** (aden+St Helena, gibraltar, kenya↔Leeward) — but
   harmless because the curated map is authoritative. Left as a documentation note.
5. Minor: `british_borneo` has no umbrella file; sub-unit *stamping* (Track A) still
   needs edition-year disambiguation for era-overlap cases.

---

## The three fixes (each validated empirically)

### Fix #1 — Roster-aware vocabulary mining (`col_mine_corpus_patterns.py`)

`mine_headings` now stops at `roster_start_block`, so the Phase-A taxonomy seed
reflects report content. Added a `no_boundary` tally and a `vocab_scope` field in
the output JSON so the coverage gap stays visible.

| Term | Before | After #1 | After #2 |
|---|---|---|---|
| `civil establishment` | 2256 (#1) | filtered out | — |
| `treasury` | 540 | 65 | 30 |
| `post office` | 525 | 84 | 49 |
| `medical department` | 506 | 70 | 32 |
| `judicial establishment` | 454 | 55 | 32 |

The top of the list is now genuine report sections (history, education,
constitution, currency and banking, situation and area, population, climate,
imports/exports, finances). `governors` stayed flat (578→578), confirming it sits
*before* the roster — a real report heading, correctly kept.

### Fix #2 — Broader roster-boundary detection (`col_canonicalize_reports.py`)

**Method matters here.** Rather than guessing markers, every candidate was
**validated against the 1,840 files that already have a primary-marker boundary**:
a safe marker, when present, must fall *at/after* the true boundary (it's roster),
not before (which would truncate the report). Results:

- **Safe (≥90% at/after)** → added as fallback markers: `treasury` (94%), `audit
  office/dept` (94%), `medical department` (92%), `public works department` (91%),
  `judicial establishment` (91%), `ecclesiastical` (91%), plus `colonial secretary`
  / `post office` (88%).
- **Rejected (mostly report content)**: `executive council` (87% FP), `legislative
  council` (84% FP), `governors` (90% FP), `customs` (22% FP). These are
  genuinely meaning-ambiguous and left to the model.
- **Also tested and rejected a content-density detector**: post-nominal honorifics
  (C.M.G., K.C.M.G., Esq…) are spread evenly through report *and* roster — only 47%
  fall after the boundary — because the report's governor lists and council
  membership carry just as many. Confirms the plan's claim that this boundary is
  genuinely meaning-based.

Fallback markers are applied **only when no primary marker exists**, so they can
never pull an already-detected boundary earlier — **zero regression** (primary
detections unchanged at 2,116). Coverage 71%→76% (+149 files); substantial (>4,000w)
files lacking a boundary cut 258→152. Added a `roster_detection` field
(`primary`/`department_fallback`/`None`). The remaining 152 open with
`governors`/`executive council` — the ambiguous tail correctly deferred to the model
(e.g. Nigeria 1950 stays `None` rather than mis-cut).

### Fix #3 — Recoverable-host split for misparses (`col_canonicalize_reports.py`)

A misparse is **not** a write-off. In every case the host colony's own report is the
prefix *before* the first foreign colony header; only the foreign tail (a misfiled
colony block, or a bled-in appendix) must be kept off the host. Verified:

- `1910/BRITISH_HONDURAS.txt`: a complete **4,001-word** British Honduras report
  (Situation and Area, History…) before the Canada block at L349.
- `1911/zanzibar.txt`: full Zanzibar report before the Aden/appendix bleed.

So `apply_corpus_triage` now annotates each misparse with `host_split_block`,
`host_recoverable_words`, and a `misparse_subtype` review hint
(`appendix_bleed` vs `wrong_colony`). **Annotates rather than dropping blocks**, so
the audit trail is preserved. Result: **19/21 files salvage a host report (≥300w);
47,906 words recovered** (median 1,568/file) that were previously all quarantined.
The 2 non-salvageable are correct (1888 Ascension is a 212k volume dump whose real
report genuinely is tiny; `OTHER_MISCELLANEOUS_POSSESSIONS` is an appendix
container with no single host).

**Bug caught and fixed along the way (entity drift, Finding 2.11):**
`SOMALILAND PROTECTORATE` was misread as a foreign header under `SOMALILAND`,
collapsing the split to line 0 and discarding the whole report. Fixed with a
word-core comparison (`_core_words`) that strips generic admin qualifiers
(protectorate/colony/settlement…) so a self-variant is recognized — while keeping
true compound sub-units like `Western Australia` as foreign. This also corrected
`federation_nested` from a too-aggressive intermediate (a raw-substring guard had
wrongly dropped Australia's states); final count **247** (was 250; the −3 is the
*correct* direction — host self-variants no longer miscount as sub-units present).

---

## Validation (all 2,946 files, zero errors)

| Metric | Value |
|---|---|
| `federation_nested` | 247 |
| `multi_colony_misparse` | 21 (6 `appendix_bleed`, 15 `wrong_colony`) |
| misparse host words **recovered** vs discarded | **47,906** (median 1,568/file; was 0) |
| roster-boundary coverage | 76% (was 71%), zero regression |
| section-vocab roster contamination | down ~85–90% vs the original |

---

## Files changed this session (uncommitted)

| File | Change |
|---|---|
| `col_canonicalize_reports.py` | +88: fallback roster markers + validation-derived; `roster_detection` field; host-split + `misparse_subtype`; `_core_words` self-variant guard |
| `col_mine_corpus_patterns.py` | +28/−14: roster-aware `mine_headings`; `vocab_scope` output |
| `generated/corpus_patterns.json` | regenerated (clean vocabulary) |
| `June1.md` | this report |

---

## Open / next steps

1. **Commit** this session's work (not yet done).
2. **Schema freeze + commit `generated/reports_canonical/`** (plan open question a).
3. **"Derived ≠ authoritative" guard** on `corpus_patterns.json` (the leaky derived
   families/floating list should not read as ground truth).
4. **Phase-B gold set** — for *measuring* (per the steer), not training.
5. **Sub-unit stamping (Track A)** — edition-year disambiguation for era-overlap
   cases (Dominica Leeward↔Windward 1940; Tobago→Trinidad 1889; Seychelles 1903;
   Newfoundland→Canada 1949).
6. **Consume `host_split_block`** in the eventual report extractor so host reports
   are salvaged and foreign tails segmented/quarantined separately.

---

## Next analysis (this session, starting now)

Preliminary look at the **History sections**: do they evolve year to year, or are
they republished verbatim across editions? This bears directly on the cross-edition
redundancy principle (§3 of the plan) for *narrative* (Track B), the way the OCR
worked example established it for *numbers* (Track A).

### Findings

- **History sections are ~81% repeated verbatim** across consecutive editions (12%
  incremental, ~6% rewrite-or-artifact). Each colony has only ~3–15 *distinct*
  versions across 30–68 editions. Two regimes: some histories are essentially fixed
  for 60+ years (Barbados, Fiji), others progressively rewritten (Cyprus, Hong Kong,
  Sierra Leone). ~6% of "rewrites" are actually section-boundary extraction
  artifacts (spike-then-revert) — a prerequisite to fix before version-clustering.
- **They are dense with groundable entities** (~4.6 titled persons/colony lower
  bound; ~14 datable years/colony) — historical figures (explorers, monarchs,
  colonial secretaries, indigenous leaders) largely distinct from the personnel
  roster, plus places and datable events. Past governors named in histories bridge
  back to the personnel `COL_Person` graph.
- **They are heavily framed** — 79% acquisition, 71% conflict, 66% sovereignty, 52%
  civilising, 51% discovery. These are *imperial self-narratives, not objective
  history* (Sierra Leone's scare-quoted `"King" Naimbana`; NZ "discovered by
  Tasman"; Rhodesia from the Chartered Company's view).

## Track C built this session — History-narrative extraction (deterministic foundation)

On the user's direction (first-class framing nodes; deterministic foundation first;
History across all colonies), built the no-LLM foundation for a new History track
(see `HISTORY_NARRATIVE_EXTRACTION_PLAN.md`):

| File | Purpose |
|---|---|
| `col_segment_histories.py` | Robust History bounding (capped at roster/host-split) + cross-edition version dedup → `generated/histories_segmented/` |
| `col_frame_histories.py` | First-class framing baseline (5 categories) + entity-candidate sweep → `generated/histories_framed/`, `taxonomy/framing_taxonomy.json` |
| `guides/history_entity_schema.py` | Frozen pydantic schema + Neo4j node/edge projection (attribution-first: `asserted_by`/`asserted_as_claim`) |

**Validated:** 116 colonies, 1,491 bounded histories → **385 distinct versions
(3.9× dedup)**; all 385 end at a heading boundary; framing prevalence reproduces the
finding (cession 76% / conflict 68% / sovereignty 67% / discovery 58% / civilising
48% per version); 1,331 person + 709 place candidates; idempotent. Spot-checks pass
(Sierra Leone `"King" Nembanu` + cession; NZ Tasman discovery). LLM NER, Wikidata
grounding (+ governor bridge), and Neo4j load are designed and staged for next.

## Geography Track built this session — place-name extraction (deterministic foundation)

`col_extract_places.py` (+ `PLACE_EXTRACTION_PLAN.md`): extract place-name mentions
across the corpus to flesh out the KG geography, bounded to report content. Per-
(place,colony) **role** (local / trading_partner / external_reference) from four
signals — home-share, family/self, section, cross-colony ubiquity — because no
single one works (Galle is a Ceylon town yet appears in 22 colonies as a coaling
port). Full named toponyms captured incl. feature words (`Cape Coast`, `Cape of
Good Hope`, `Port Louis`, `Gambia River`) while standalone generics (`hill`,
`field`, `cape`) are dropped. **3,821 places**; London/Great Britain/England =
external hubs; Colombo/Singapore/Port Louis local in their home colonies; **KWIC**
concordance per (place,colony) for grounding; temporal index shows 274 places first
appearing ≥1946 (Belize City, Brunei Town, Hong Kong Island). Wikidata/GeoNames
grounding + `COL_Place` KG load staged.

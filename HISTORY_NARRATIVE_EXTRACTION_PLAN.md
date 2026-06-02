# History-Narrative Extraction & Framing (Track C)

**Status:** Phase 0 (deterministic foundation) **built & validated**; LLM/grounding
phases designed and staged.
**Relationship to existing tracks:** Extends `COLONY_REPORTS_EXTRACTION_PLAN.md`
(Track B, narrative). Consumes the Phase-0 canonicalizer
(`col_canonicalize_reports.py`) and reuses the personnel track's extraction,
Wikidata-grounding, normalization, and Neo4j conventions.

---

## 1. Motivation

Every colony entry opens with a narrative **History** section. Two measured facts
make these worth a dedicated track:

- **They are highly redundant.** ~81% of consecutive editions are verbatim
  republications (12% incremental, ~6% rewrite-or-artifact); each colony has only
  ~3–15 *distinct* versions across 30–68 editions. The narrative analogue of the
  numeric rolling-window redundancy in `COLONY_REPORTS_EXTRACTION_PLAN.md` §3 —
  so entities/framing are extracted **once per distinct version**, not 60×.
- **They are dense with groundable entities and heavy framing.** ~4.6 titled
  persons/colony (a lower bound), ~14 datable year-refs/colony; and across 125
  colonies the prose carries imperial framing — 79% acquisition, 71% conflict,
  66% sovereignty, 52% civilising, 51% discovery.

## 2. Non-negotiable stance: claims, not facts

These histories are **claims asserted by the Colonial Office**, not objective
history. They are imperial self-narratives with loaded framing — Sierra Leone's
scare-quoted `"King" Naimbana`/`"King" Tom`; New Zealand "discovered in 1642 by
Tasman" (erasing Māori); Southern Rhodesia narrated from the British South Africa
Company's view; "ceded by the native chiefs", "punitive expedition", "pacified".

The schema therefore **attributes every record** (`asserted_by="Colonial Office
List"` + the `edition_years` it was printed in), **flags it a claim, never a fact**
(`asserted_as_claim=True`), **preserves the verbatim surface form** (incl.
scare-quotes — they are the signal), and **promotes the framing to a first-class,
queryable object**. No edge ever asserts objective truth — only "the CO List
claimed X in editions Y." This guards against laundering colonial claims into
apparent facts.

## 3. Schema

### Persistent nodes
- `COL_HistoricalEntity` — `col:hentity/<type>/<slug>`; `entity_type ∈
  {person,place,event}`, `canonical_label`, `aliases[]` (raw surface forms incl.
  scare-quotes, preserved not privileged), `entity_subtype`, `wikidata_qid`+
  `wd_confidence` (Phase D), provenance.
- `COL_FramingType` — `col:framing/<slug>`; the five seeded categories.

### Slice nodes
- `COL_HistoryVersion` — `col:hversion/<colony>/history/<hash>`; the dedup anchor.
  Verbatim `text`, `edition_years[]`, span, `intra_cluster_min_sim`, `source_flags`.
- `COL_EntityMention` — `col:hmention/<tail>/<idx>`; `surface_text` (verbatim),
  `source_span`, `asserted_by`, `asserted_as_claim`, `edition_years[]`,
  `year_reference`, `confidence`, `extractor`.
- `COL_FramingAnnotation` — `col:hframing/<tail>/<idx>`; `framing_type`,
  `loaded_terms[]` (verbatim), `verbatim_span`, span, `asserted_by`,
  `edition_years[]`, `confidence`.

Relationships, constraints, and indexes are specified in
`guides/history_entity_schema.py` (`NODE_SCHEMA`, `EDGE_SCHEMA`,
`CONSTRAINTS_CYPHER`). Key edges: `VERSION_IN`→`COL_TerritoryYear`,
`MENTIONS`→`COL_HistoricalEntity`, `OF_FRAMING`→`COL_FramingType`,
`SAME_AS`→`WD_Person`, and the **governor bridge** `IS_HISTORICAL_SELF_OF`→
`COL_Person` (a past governor named in a history is often already in the personnel
graph).

## 4. Phases

| Phase | Status | Deliverable |
|---|---|---|
| **0a. Section bounding + version dedup** | ✅ built | `col_segment_histories.py` → `generated/histories_segmented/<colony>.json` |
| **0b. Framing baseline + entity candidates** | ✅ built | `col_frame_histories.py` → `generated/histories_framed/<colony>.json`; `taxonomy/framing_taxonomy.json` |
| **A. Schema freeze** | ✅ built | `guides/history_entity_schema.py` (pydantic + Neo4j projection) |
| **B. Pilot gold set** (for *measuring*) | staged | `test_data/history_gold/*` — region×era spanning |
| **C. LLM NER + framing refinement** | staged | `col_extract_histories.py` (reuse `extraction_corpus.py` checkpointing, `extraction_instructor.py` pydantic `response_model`, `extraction_ollama.py`; era/region prompts from `guides/*_guide.md`) |
| **D. Entity normalize + Wikidata ground + governor bridge** | ⚙️ local slice built; WD grounding staged | `col_link_histories.py` (governor bridge + place grounding, no Neo4j/LLM); staged: `col_normalize_histories.py`, `col_link_histories_wikidata.py` (reuse `normalize_rules.py`/`normalize_llm.py`, `col_link_wikidata.py` `compute_match_confidence`/`compute_temporal_overlap`, `load_wikidata_people.py`, `wikidata-mcp`) |
| **E. Neo4j load** | staged | `col_load_histories_neo4j.py` (reuse `col_load_neo4j.py` loaders, `col_scaffold_neo4j.py` constraints) |
| **F. Validation + critical-analysis viz** | ⚙️ framing analysis built | `col_analyze_framing.py` (framing by region × era + self-contained `framing_viz.html`); staged: `col_audit_histories.py` (entity networks, gold scoring) |

### Phase 0 method (built)
- **Bounding** (`col_segment_histories.py`): from canonical blocks, take prose
  after the `history` heading until the next heading, hard-capped at
  `roster_start_block` and `host_split_block`; quarantine `volume_dump`, drop
  sections falling after a misparse boundary (`after_boundary`). This removes the
  ~6% boundary-artifact "rewrites".
- **Version dedup**: chain consecutive editions by `SequenceMatcher` ≥ 0.90 into
  one `COL_HistoryVersion`; representative = longest member; record
  `intra_cluster_min_sim` so drift stays visible.
- **Framing** (`col_frame_histories.py`): a curated lexicon (5 categories, 74
  terms) → `COL_FramingAnnotation` with verbatim loaded terms + enclosing
  sentence. A transparent baseline the LLM refines.
- **Entity candidates**: titled persons (scare-quote-aware), gazetteer place
  references (cross-colony links), datable year-refs — a high-precision recall
  floor + taxonomy seed (`extractor="deterministic_baseline"`).

## 5. Validation (Phase 0, all corpus)

| Metric | Value |
|---|---|
| Colonies with a bounded History | 116 |
| Editions with a bounded History | 1,491 |
| Distinct versions (dedup) | 385 (**3.9× collapse**) |
| Versions/colony min/median/max | 1 / 3 / 15 (matches per-colony measures: jamaica 7, hong_kong 13, fiji 8) |
| Section end-reason | 385/385 end at a heading boundary; 2/385 roster-leak |
| Framing prevalence (per version) | cession 76% · conflict 68% · sovereignty 67% · discovery 58% · civilising 48% |
| Entity candidates | 1,331 person · 709 place |
| Idempotent re-run | stable `version_hash` ⇒ identical output |

Spot-checks pass: Sierra Leone → `cession` framing + scare-quoted `"King" Nembanu`
(verbatim, `asserted_as_claim=True`); New Zealand → `discovered in 1642 by Tasman`
discovery frame.

### Governor bridge + place grounding (Phase-D local slice, built)

`col_link_histories.py` matches the 1,251 history person candidates against the
3,103 local personnel extraction files (the `COL_Official` source), reusing
`col_link_wikidata`'s name parser + initials matcher. **Temporal gating is
essential and applied**: of 108 strong same-colony name matches, only **26 are
CONFIRMED** (personnel year within ±15y of the mention) — 10 governors/admins —
while **47 pre-1862 and 14 anachronistic name-twins are rejected** (e.g. 19th-c.
Sir Philip Wodehouse spuriously matched a 1948 same-surname official). Confirmed
examples are correct: Sir Harry Johnston→Johnston (Uganda Commissioner, Δ0y); Sir
Gilbert Carter→Carter (Bahamas Governor, Δ3y); Sir Garnet Wolseley→Wolseley (Gold
Coast, Δ12y). 709 place references ground to 337 colony→territory edges (most-
referenced: malacca, australia, victoria, penang, singapore). 1,007 unmatched
figures (Raleigh, Queen Elizabeth, Cook, Abercrombie) form the Wikidata to-ground
queue. Outputs: `generated/histories_grounded/<colony>.json`,
`generated/histories_grounding_report.json`.

## 6. Risks & mitigations

1. **Epistemological laundering (headline)** → attribution-first schema
   (`asserted_by`+`asserted_as_claim`), verbatim spans, framing as first-class
   nodes; no edge asserts truth.
2. **Boundary artifacts (~6%)** → Phase 0 caps at next-heading + `roster_start_block`
   + `host_split_block` *before* version clustering.
3. **OCR-garbled / scare-quoted names** → keep all surface forms in `aliases[]`;
   never normalize away scare-quotes; under-extract on illegible names.
4. **NER over-extraction / anachronistic WD matches** (Phases C/D) → under-extract;
   temporal gate via `compute_temporal_overlap`; 0.70/0.90 thresholds; dry-run
   review before writing `SAME_AS`.

### Framing analysis by region × era (Phase-F slice, built)

`col_analyze_framing.py` aggregates the framing annotations over 1,491 published
colony-year histories (each version expanded to its editions) by an 8-region
curated map × 4 eras, emitting `generated/framing_analysis.json` and a
self-contained `framing_viz.html` (region heatmap, era trend lines, per-colony
evolution). Headline critical findings:

- **"Civilising" framing concentrates in Africa, not the Pacific.** Southern Africa
  (settler) 100%, West Africa 88%, East & Central Africa 82% — vs Caribbean 41%,
  Settler Dominions 22%, **Pacific 20%**.
- **Settler-dominion histories erase frontier conflict.** Conflict framing: Canada/
  Australia/NZ = **2%**, vs Southern Africa 100%, East & Central Africa 95%, Pacific
  92%, West Africa 84%. The violence of settler colonisation is narratively absent
  while African colonies are narrated through conquest.
- **"Discovery" tracks terra-nullius colonies.** Pacific 90%, Settler Dominions 89%,
  Caribbean 86% — vs East & Central Africa 27%, South/SE Asia 25% (conquered/ceded,
  not "discovered").
- **Era drift (mostly republication-stable):** conflict 56%→75%, civilising 44%→57%,
  sovereignty 52%→77% across 1862-99 → 1946-66; discovery falls 69%→60%.

These are properties of the SOURCE's narration (claims), not historical fact.

## 7. Next steps

1. Phase B gold set (region×era) for measuring C/D precision/recall.
2. Phase C LLM NER over the 385 versions (not 1,491 editions).
3. Phase D grounding + the governor bridge to `COL_Person`.
4. Phase F: framing-by-region/era analysis — e.g. does "civilising" framing
   concentrate in African vs settler colonies; does framing shift across eras
   (Sierra Leone's "native chiefs" → scare-quoted `"King"` after 1925).

# Colony Annual Reports → Knowledge Graph: Extraction Plan

**Status:** Proposed (planning document)
**Relationship to existing stages:** New parallel track. Consumes Stage 1
segmentation, reuses the persistent+slice modeling pattern, and dovetails with
Stage 3 (normalization), Stage 5 (narrative embedding), and Stage 6 (external
linking).

---

## 1. Motivation

So far the pipeline has mined **people** out of the Colonial Office List
(`COL_PersonRecord → COL_Official → COL_Person`). But each colony entry in every
volume (1867–1966, ~5,300 colony-year `.txt` files) opens with a
**semi-structured annual report** on the colony itself, *before* the staff lists
begin. By line count this descriptive/statistical material is roughly **50–70% of
each file** and is currently unextracted.

This is a century-long, ~50-colony **panel dataset** of public finance, trade,
population, area, shipping, communications, and production — plus rich narrative
on geography, history, and constitution. Extracting it turns the KG from a
prosopography into a quantitative + textual atlas of the empire, enabling queries
the personnel graph cannot answer (e.g. "plot Ceylon revenue vs. number of
officials, 1870–1950", "which colonies' export base was >80% one commodity",
"retrieve the constitutional history of Natal").

---

## 2. What the source actually looks like (extraction-relevant findings)

A cross-decade read of Jamaica, Ceylon, Hong Kong, and smaller colonies, plus
corpus-wide counts, shows:

1. **Section vocabulary is consistent**, but **its formatting is not.** Sections
   are introduced by a heading that may be a bare line ending in `.`
   (`Trade.`, `Revenue.`, `Situation and Area.`), a Markdown `### Finances`, or a
   `*bold*` title — inconsistently, even for the same colony across years.
2. **Statistics appear in two presentations, often in the same entry:**
   - *Prose-embedded figures* (all eras), e.g. 1900 `JAMAICA.txt`:
     ```
     Industry.
     ... sugar (export 284,875 cwt., value 120,958L); coffee (export 85,410
     cwt., value 165,494L); ginger (export 12,572 cwt., value 34,884L) ...
     ```
   - *Pipe/Markdown tables* (also all eras; 1867 `JAMAICA.txt` already has them):
     ```
     | Year | Revenue (£) | Expenditure (£) |
     | 1856 | 221,768     | 213,612         |
     | 1862 | 291,087     | 292,402         |
     ```
3. **Figures are retrospective.** A 1930 volume reports 1928–29 figures; a 1900
   volume reports 1894–98. **The year a statistic describes (`observation_year`)
   is almost never the volume's `edition_year`**, and it is stated in the
   prose/row ("for 1928", "1862"). This is the single most important *modeling*
   consequence.
4. **Units/currencies vary** by colony and era: £ vs Rupees (Ceylon, Straits,
   Mauritius) vs HK$ (Hong Kong); a trailing `L`/`l.` for pounds; area in square
   miles; crops in tons / cwt / lbs / stems / acres. Currency regimes also change
   mid-century for a colony.
5. **The files are an inconsistent md/txt mix — the dominant *practical*
   problem.** The upstream OCR/parsing step emitted Markdown for some
   files/sections and plain text for others, with no consistency. Measured over
   5,325 parsed files: ~98% contain at least one pipe row, but only **31% have
   proper `|---|` table separators**, **28% have `*bold*` titles**, **18% have
   `###` headings** — and some volumes (e.g. parts of 1960) have none of these
   markers at all. The *same colony* swings between conventions year to year.
   **A regex keyed on any single marker (`###`, `|---|`, bare `Heading.`) covers
   at most ~⅓ of the corpus and silently drops the rest.** Hard-coded parsing
   will fail; structure detection must be model-based and format-agnostic.
6. **OCR is noisy on structure and digits.** Tables have placeholder headers
   (`| 1 | 2 | 3 |`), header rows split from data, ragged columns; headings are
   garbled; digits are the least reliable tokens of all
   (`GRAPHRAG_PIPELINE_DESIGN.md`). Numeric extraction needs transcription
   discipline and confidence flagging, not silent computation.

---

## 3. Design principles (inherited from the existing KG)

Non-negotiable, because they are what makes the current graph trustworthy:

- **Persistent + slice separation.** Persistent identity nodes (time-invariant)
  vs. slice nodes (one observation, tied to a colony-year). Mirrors
  `Territory/TerritoryYear`, `InstitutionType/InstitutionInstance`,
  `Person/PersonRecord`.
- **Slice fidelity — never infer or compute.** Record exactly what the page
  prints. Keep the **raw string** alongside any parsed value. Do not sum
  components to fill a missing total; do not convert currencies/units in the
  slice layer. Derivations live in the persistent/analytic layer only.
- **Provenance + confidence on every node and edge** (`method`, `confidence`,
  `pipeline_version`, `date_created`) with a `quarantined` boolean for
  low-confidence numerics — exactly as `COL_PersonRecord` already does.
- **Under-extract rather than over-assert.** A flagged gap is recoverable; a
  confidently wrong revenue figure poisons downstream analysis.
- **Conventions:** `col_*.py` script names, `col:...` URI scheme, taxonomy JSON in
  `taxonomy/`, canonical schema in `guides/`, incremental & re-runnable Neo4j
  loaders, human-in-the-loop review tooling.

---

## 4. Proposed schema extension

### 4.1 New persistent nodes (canonical, deduplicated, reviewed)

| Label | Key | Purpose | Example |
|---|---|---|---|
| `COL_IndicatorType` | `uri` (`col:indicator/<slug>`) | A canonical metric | `revenue`, `imports_value`, `population_total`, `area_sq_mi`, `shipping_tonnage`, `public_debt` |
| `COL_CommodityType` | `uri` (`col:commodity/<slug>`) | A traded/produced good | `sugar`, `coffee`, `bananas`, `pimento` |
| `COL_ReportSectionType` | `uri` (`col:section/<slug>`) | A canonical report section | `history`, `finance`, `constitution`, `trade` |

Properties carry normalization metadata: `IndicatorType` →
`canonical_unit`, `dimension` (currency/count/area/mass/volume/tonnage),
`category` (finance/trade/demography/geography/infrastructure);
`CommodityType` → `category`, optional `wikidata_id` (Stage 6 hook).

### 4.2 New slice nodes (one per observation, tied to a colony-year)

- **`COL_ColonyReport`** — anchor for one colony-year's report.
  `uri = col:report/<colony>/<edition_year>`; holds `source_file`, `edition_year`,
  `sections_present`, provenance. A convenient hub even though observations also
  link directly to the `TerritoryYear`.
- **`COL_Observation`** — a single scalar statistic. Properties: `uri`,
  `indicator_slug`, `value_raw` (string as printed), `value_num` (parsed
  float|null), `unit_raw`, `currency_raw`, **`observation_year_start/end`** (the
  period the figure describes; e.g. row "1896-7" → 1896/1897), `edition_year`,
  `colony`, `source_span`, `confidence`, `quarantined`.
- **`COL_TradeFlow`** — a commodity-level import/export line. Properties:
  `direction` (import/export), `commodity_slug`, `quantity_raw`, `quantity_num`,
  `quantity_unit`, `value_raw`, `value_num`, `currency_raw`,
  `observation_year_start/end`, provenance. (Optional `partner` when trade-by-
  country is given.)
- **`COL_NarrativeChunk`** — a section-typed prose chunk for embedding.
  Properties: `uri`, `section_slug`, `text`, `char_start/end`, `edition_year`,
  `embedding` (or external vector-store id). **Concretely realizes Stage 5's
  "narrative → vectors" for report sections.**

### 4.3 Relationships

```
(COL_ColonyReport)-[:REPORT_FOR]->(COL_TerritoryYear)
(COL_Observation)-[:MEASURES]->(COL_IndicatorType)
(COL_Observation)-[:REPORTED_IN]->(COL_ColonyReport)
(COL_Observation)-[:OBSERVED_FOR]->(COL_TerritoryYear)   // by observation_year, not edition
(COL_TradeFlow)-[:OF_COMMODITY]->(COL_CommodityType)
(COL_TradeFlow)-[:REPORTED_IN]->(COL_ColonyReport)
(COL_NarrativeChunk)-[:DESCRIBES]->(COL_TerritoryYear)
(COL_NarrativeChunk)-[:OF_SECTION]->(COL_ReportSectionType)
```

Because `COL_TerritoryYear-[:INSTANCE_OF]->COL_Territory` and the `CONTINUES_AS`
temporal chain already exist, longitudinal series fall out for free: collect
`COL_Observation` across a `Territory`'s year-slices, order by `observation_year`.
That field is what makes the panel correct rather than off-by-several-years.

### 4.4 Constraints / indexes (Neo4j)

```cypher
CREATE CONSTRAINT col_indicator_uri IF NOT EXISTS FOR (i:COL_IndicatorType)     REQUIRE i.uri IS UNIQUE;
CREATE CONSTRAINT col_commodity_uri IF NOT EXISTS FOR (c:COL_CommodityType)     REQUIRE c.uri IS UNIQUE;
CREATE CONSTRAINT col_section_uri    IF NOT EXISTS FOR (s:COL_ReportSectionType) REQUIRE s.uri IS UNIQUE;
CREATE CONSTRAINT col_report_uri     IF NOT EXISTS FOR (r:COL_ColonyReport)      REQUIRE r.uri IS UNIQUE;
CREATE CONSTRAINT col_obs_uri        IF NOT EXISTS FOR (o:COL_Observation)       REQUIRE o.uri IS UNIQUE;
CREATE CONSTRAINT col_trade_uri      IF NOT EXISTS FOR (t:COL_TradeFlow)         REQUIRE t.uri IS UNIQUE;
CREATE INDEX col_obs_ind_year        IF NOT EXISTS FOR (o:COL_Observation)       ON (o.indicator_slug, o.observation_year_start);
CREATE INDEX col_obs_colony          IF NOT EXISTS FOR (o:COL_Observation)       ON (o.colony);
```

---

## 5. Extraction approach — format-agnostic, LLM-first

The corpus is too inconsistent (Finding §2.5) for a parser that keys on Markdown
markers or fixed layouts. The approach is therefore **structure-detection by
model, not by regex**, with cheap deterministic steps used only where they are
reliable, and regex used only as a *recall booster/cross-check*, never as the
primary extractor.

Backends reuse the existing stack: local **Ollama gpt-oss:120b** primary;
**OpenRouter**/**Gemini** and **instructor + pydantic** for validation/fallback;
plus the project's code-generation review option.

### Phase 0 — Source canonicalization (new, addresses the md/txt mix)

Before extraction, run a light **normalizer that maps every file into one
internal representation** regardless of whether it arrived as Markdown or plain
text. This is the single highest-leverage step:

- Detect headings by *meaning* (fuzzy match against the section taxonomy),
  whether they appear as `### Finances`, `**Trade**`, `Trade.`, or `TRADE`.
- Detect table-ish regions structurally (lines of mostly digits/separators,
  pipe-aligned or whitespace-aligned) rather than by requiring `|---|`.
- Emit a uniform JSON: `{section, kind: prose|table|mixed, raw_text, table_cells?}`.
- Keep a back-pointer (`source_span`) to the original file for audit.

This converts "5,325 files in N formats" into "5,325 files in one format," so the
downstream extractor sees consistent input and the **md/txt heterogeneity is
solved once, centrally**, instead of being re-fought in every regex.

> Note: this also retroactively fixes a known pipeline gap — earlier extraction
> skipped `.md` source files entirely; canonicalization removes that class of bug
> by making format irrelevant.

### Track A — Structured statistics (the hard, high-value part)

1. **Segment** each entry into section blocks using the Phase-0 canonical form
   (no raw-format regex), tagging each block with a `COL_ReportSectionType`.
2. **Extract with the LLM + pydantic schema** (`ColonyReportExtraction`) over
   each block, handling prose and table cells uniformly. The model reads
   *"The revenue and expenditure for the financial year 1928-29 were £2,663,924
   and £2,659,895 respectively"* (or the equivalent table row) and emits two
   `COL_Observation` records with `observation_year_start=1928,
   observation_year_end=1929`. Prompt rules, encoded tersely (gpt-oss responds
   better to rules than examples):
   - *Transcribe digits exactly; never add, sum, round, or convert.*
   - *Extract the period each figure describes from the surrounding sentence/row.*
   - *Record `unit_raw`/`currency_raw` exactly as written (`£`, trailing `L`,
     `Rs.`, `tons`, `cwt.`, `acres`); leave normalization to a later stage.*
   - *Keep `value_raw` as the verbatim substring and a `source_span` offset so
     every number is auditable back to the page.*
   - *If illegible/ambiguous, emit with `confidence<0.5` rather than guessing.*
3. **Regex only as a recall cross-check.** A few high-precision patterns
   (currency-prefixed number near a year) run alongside the LLM purely to flag
   figures the model may have missed — discrepancies are surfaced for review, not
   trusted blindly. Regex never owns an extraction.
4. **Verify numerics (cheap, deterministic):** cross-check stated total vs. sum
   of printed components when both appear (**flag mismatches, do not
   auto-correct**), magnitude plausibility, and year-over-year continuity against
   neighbouring editions. Anomalies set `quarantined=true`.

### Track B — Narrative chunking + embedding

1. Chunk narrative sections (from Phase-0 output) by heading + paragraph
   (≤1,500 words, ≥200), tag with `section_slug` and `edition_year`.
2. Embed (open-source or API embedder, consistent with the Stage 5 decision);
   store `COL_NarrativeChunk` with `DESCRIBES`/`OF_SECTION` edges.
3. GraphRAG-ready: graph queries select colony-years, vectors retrieve prose.

---

## 6. Normalization (Stage-3-style, after extraction)

Produce reviewed taxonomy JSON in `taxonomy/`, bootstrapped by a corpus sweep,
clustered rule-first then LLM-assisted, then human-approved:

- `taxonomy/indicator_taxonomy.json` — raw labels ("Revenue", "Total revenue",
  "Revenue.") → `COL_IndicatorType` with `canonical_unit`/`dimension`.
- `taxonomy/commodity_taxonomy.json` — raw commodity strings → `COL_CommodityType`.
- `taxonomy/report_section_taxonomy.json` — heading variants → `COL_ReportSectionType`.
- **Unit/currency conversion lives here, not in the slice.** Add derived
  `value_canonical`/`unit_canonical` (and optional GBP-equivalent with documented,
  versioned rates) as *additional* fields, always preserving `*_raw`.

---

## 7. Phasing & deliverables

| Phase | Work | Output |
|---|---|---|
| **0. Canonicalization** | Format-agnostic normalizer (md/txt → one internal JSON); measure heading/table recall on a labelled sample | `col_canonicalize_reports.py`, `generated/reports_canonical/*.json` |
| **A. Schema + taxonomy seed** | Freeze labels; sweep ~40 files across eras/regions to seed indicator/commodity/section taxonomies | `guides/colony_report_schema.py`, three `taxonomy/*_taxonomy.json` |
| **B. Segmenter + pilot** | Build a gold standard for ~5 colonies spanning eras (Jamaica, Ceylon, Hong Kong, a settler colony, a small island) | `col_segment_reports.py`, `test_data/report_gold/*` |
| **C. Structured extraction** | Run Track A over the corpus with checkpointing/auto-push (reuse `extraction_corpus.py` patterns) | `col_extract_reports.py`, `generated/reports/*.json` |
| **D. Normalization** | Cluster + review indicators/commodities/sections; add canonical units/currencies | populated taxonomies, `col_normalize_reports.py` |
| **E. Neo4j load** | Constraints/indexes; load reports, observations, trade flows | `col_load_reports_neo4j.py` |
| **F. Narrative embedding** | Track B chunking + embedding (aligns with Stage 5) | `col_embed_reports.py`, `COL_NarrativeChunk` nodes |
| **G. Validation + viz** | Gold-standard accuracy, panel QA (continuity, totals), demo charts | `col_audit_reports.py`, sample notebooks/HTML |
| **H. External linking (opt.)** | Commodities → Wikidata; indicators → a standard vocab | Stage-6-style `SAME_AS`/`EXTERNAL_LINK` edges |

Phase 0 should be validated (heading/table recall on a labelled sample) and
Phases A→B reviewed, with the schema frozen, before C runs at corpus scale.

---

## 8. Risks & mitigations

- **Inconsistent md/txt formatting (the headline risk)** → Phase-0
  canonicalization solves it once, centrally; model-based structure detection;
  regex only as a cross-check, never primary.
- **OCR digit/table errors** → raw + parsed values, confidence scores,
  quarantine, cross-edition continuity checks; never auto-compute.
- **observation-year vs edition-year confusion** → first-class
  `observation_year_start/end`; loaders link `OBSERVED_FOR` by observation year.
- **Unit/currency heterogeneity** → preserve `*_raw`; convert only in a versioned
  normalization layer with documented rates.
- **Format drift across a century** → era-aware prompts; extend the regional
  `guides/*` (which already encode colony-specific patterns) with report-format
  notes.
- **Federations / sub-colony tables** (Leeward/Windward, Straits, Canada) → reuse
  existing federation handling; attach observations to the correct member
  `TerritoryYear`.
- **Scope creep** → Track A priorities are finance/trade/population/area/shipping;
  deep tables (detailed education/medical breakdowns) are a later pass.

---

## 9. Teaching value (this is also a course project)

The colony-report track is a strong HIST 496 extension: the *same* document
yields a second, quantitatively different extraction problem (noisy, multi-format
tables vs. clean rosters). Students see firsthand why upstream format
inconsistency defeats regex and motivates a canonicalization step, practice
schema design for panel data, and confront the observation-year subtlety and
OCR-confidence trade-offs. The Phase-B gold standard can double as a lab.

---

## 10. Immediate next steps

1. Review/approve the schema (§4) and freeze node/edge names.
2. Prototype the Phase-0 canonicalizer and measure heading/table recall on a
   labelled sample spanning markdown-heavy and plain-text files.
3. Run the Phase-A corpus sweep to seed the three taxonomies; stand up the
   Phase-B gold standard for 5 colonies before any corpus-scale run.

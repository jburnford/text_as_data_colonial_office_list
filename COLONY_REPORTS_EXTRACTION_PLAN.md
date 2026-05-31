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
volume (1867–1966, 2,946 colony-year `.txt` files) opens with a
**semi-structured annual report** on the colony itself, *before* the staff lists
begin. By line count this descriptive/statistical material is a large share of
each file (a substantial fraction sampled at ~½, though this is an eyeball
estimate, not a measured corpus statistic) and is currently unextracted.

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
5. **Inconsistent Markdown formatting inside the `.txt` files — a residue of an
   upstream md/txt mix, and the dominant *practical* problem for *headings*.**
   The parsing that produced these files applied Markdown unevenly. Measured over
   all **2,946** parsed colony files:
   - **tables are fairly consistent:** 90% of files contain ≥1 pipe row and
     **90% contain a proper `|---|` separator** — so most numeric tables *are*
     well-delimited Markdown and are reliably machine-detectable.
   - **headings are not:** **52% use `*bold*` titles, 28% use `###` headings**,
     and the remainder use a bare `Heading.` line or ALL-CAPS (`FINANCES.`).
     The *same colony* swings between these conventions year to year, and the
     same section appears as `FINANCES.`, `Finances.`, `### Finances`, `Finance.`,
     `## Finances`, …
   So the honest split is: **table *detection* can lean on regex/deterministic
   parsing (≈90% well-formed), but heading/section detection cannot** — no single
   marker identifies sections corpus-wide. Section segmentation must be
   meaning-based (model/fuzzy), even though table parsing need not be.
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
  `colony`, `source_span`, `confidence`, `quarantined`. The temporal info lives
  in these **properties**; an observation always attaches to its
  `COL_ColonyReport` (which always exists), *not* to a year-slice that may not
  (see §4.3).
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
(COL_ColonyReport)-[:REPORT_FOR]->(COL_TerritoryYear)        // edition year — always exists
(COL_Observation)-[:MEASURES]->(COL_IndicatorType)
(COL_Observation)-[:REPORTED_IN]->(COL_ColonyReport)         // primary attachment, always present
(COL_Observation)-[:OBSERVED_FOR]->(COL_TerritoryYear)       // OPTIONAL: only if a slice exists for that obs. year
(COL_TradeFlow)-[:OF_COMMODITY]->(COL_CommodityType)
(COL_TradeFlow)-[:REPORTED_IN]->(COL_ColonyReport)
(COL_NarrativeChunk)-[:DESCRIBES]->(COL_TerritoryYear)
(COL_NarrativeChunk)-[:OF_SECTION]->(COL_ReportSectionType)
```

**Why observations attach to the report, not to an observation-year slice.**
`COL_TerritoryYear` nodes exist only for the ~69 *edition* years (1862, 1867,
1877, …). But reports cite figures for **non-edition years** — e.g. 1867
Jamaica's revenue table lists 1856, 1859, 1860, none of which has a slice. So an
`OBSERVED_FOR` edge keyed on observation year would be unattachable for a large
fraction of observations. The fix: every observation attaches to its
`COL_ColonyReport` (which exists by construction) and carries
`observation_year_start/end` as **properties**; `OBSERVED_FOR` is created only
opportunistically when a matching slice happens to exist (e.g. for
cross-referencing personnel in that same year).

Longitudinal series are therefore built from the **property**, not from
year-slices: gather a `Territory`'s observations via its `COL_ColonyReport`s and
order by `observation_year_start`. (Optionally, de-duplicate the overlap where
successive editions republish the same year's figure — keep the earliest-printed
or highest-confidence copy.) That property is what makes the panel correct rather
than off-by-several-years.

### 4.4 Constraints / indexes (Neo4j)

```cypher
CREATE CONSTRAINT col_indicator_uri IF NOT EXISTS FOR (i:COL_IndicatorType)     REQUIRE i.uri IS UNIQUE;
CREATE CONSTRAINT col_commodity_uri IF NOT EXISTS FOR (c:COL_CommodityType)     REQUIRE c.uri IS UNIQUE;
CREATE CONSTRAINT col_section_uri    IF NOT EXISTS FOR (s:COL_ReportSectionType) REQUIRE s.uri IS UNIQUE;
CREATE CONSTRAINT col_report_uri     IF NOT EXISTS FOR (r:COL_ColonyReport)      REQUIRE r.uri IS UNIQUE;
CREATE CONSTRAINT col_obs_uri        IF NOT EXISTS FOR (o:COL_Observation)       REQUIRE o.uri IS UNIQUE;
CREATE CONSTRAINT col_trade_uri      IF NOT EXISTS FOR (t:COL_TradeFlow)         REQUIRE t.uri IS UNIQUE;
CREATE INDEX col_obs_ind_year        IF NOT EXISTS FOR (o:COL_Observation)       ON (o.indicator_slug, o.observation_year_start);
CREATE INDEX col_obs_colony_year     IF NOT EXISTS FOR (o:COL_Observation)       ON (o.colony, o.observation_year_start);
```

---

## 5. Extraction approach — deterministic where reliable, model where not

Finding §2.5 dictates a split, not a blanket choice: **table structure is ~90%
well-formed Markdown** (so deterministic parsing earns its keep on the bulk of
the numeric data), while **heading/section detection is heterogeneous** (so it
must be meaning-based). The LLM also carries the genuinely hard cases:
OCR-broken table fragments and figures embedded in prose. Net: use cheap
deterministic parsing where the data is regular, the model where it is not, and
regex never as the *sole* owner of a numeric extraction.

Backends reuse the existing stack: local **Ollama gpt-oss:120b** primary;
**OpenRouter**/**Gemini** and **instructor + pydantic** for validation/fallback;
plus the project's code-generation review option.

### Phase 0 — Source canonicalization (new, addresses heading heterogeneity)

Before extraction, run a light **normalizer that maps every file into one
internal representation** regardless of whether it arrived as Markdown or plain
text. This is the single highest-leverage step:

- Detect headings by *meaning* (fuzzy match against the section taxonomy),
  whether they appear as `### Finances`, `**Trade**`, `Trade.`, or `TRADE`. This
  is the part that genuinely *needs* the model, since no single marker works
  corpus-wide (Finding §2.5).
- Detect tables: the ~90% with `|---|` parse deterministically; for the rest,
  fall back to structural detection (lines of mostly digits/separators, pipe- or
  whitespace-aligned).
- Emit a uniform JSON: `{section, kind: prose|table|mixed, raw_text, table_cells?}`.
- Keep a back-pointer (`source_span`) to the original file for audit.

This converts "2,946 files with inconsistent heading markup" into "2,946 files in
one internal format," so the downstream extractor sees consistent input and the
**heading heterogeneity is normalized once, centrally**, instead of being
re-fought in every consumer.

> Note: this also retroactively fixes a known pipeline gap — earlier extraction
> skipped `.md` source files entirely; canonicalization removes that class of bug
> by making format irrelevant.

### Track A — Structured statistics (the hard, high-value part)

1. **Segment** each entry into section blocks using the Phase-0 canonical form,
   tagging each block with a `COL_ReportSectionType`.
2. **Well-formed tables (~90%): parse deterministically, LLM labels columns.**
   Read cells directly, capture each cell's `value_raw`, parse `value_num` +
   `currency_raw`, and pull the period per row into `observation_year_start/end`.
   The LLM's job here is *only* to map column headers → `indicator_slug` and
   confirm units — it does not re-transcribe digits it might hallucinate. This is
   the cheapest, highest-precision path and covers the bulk of the numeric data.
3. **Prose figures and broken tables: LLM + pydantic schema**
   (`ColonyReportExtraction`). The model reads *"The revenue and expenditure for
   the financial year 1928-29 were £2,663,924 and £2,659,895 respectively"* (or a
   mangled table fragment) and emits two `COL_Observation` records with
   `observation_year_start=1928, observation_year_end=1929`. Prompt rules,
   encoded tersely (gpt-oss responds better to rules than examples):
   - *Transcribe digits exactly; never add, sum, round, or convert.*
   - *Extract the period each figure describes from the surrounding sentence/row.*
   - *Record `unit_raw`/`currency_raw` exactly as written (`£`, trailing `L`,
     `Rs.`, `tons`, `cwt.`, `acres`); leave normalization to a later stage.*
   - *Keep `value_raw` as the verbatim substring and a `source_span` offset so
     every number is auditable back to the page.*
   - *If illegible/ambiguous, emit with `confidence<0.5` rather than guessing.*
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

- **Inconsistent heading markup (the headline *heading* risk)** → Phase-0
  canonicalization normalizes headings once, centrally, via meaning-based
  detection. (Tables are mostly well-formed and are *not* the headline risk.)
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
yields a second, quantitatively different extraction problem (statistics in
mostly-clean tables plus prose, under inconsistent headings, vs. clean personnel
rosters). Students see firsthand why inconsistent heading markup defeats naive
regex and motivates a canonicalization step, practice schema design for panel
data, and confront the observation-year subtlety (figures predating any edition!)
and OCR-confidence trade-offs. The Phase-B gold standard can double as a lab.

---

## 10. Immediate next steps

1. Review/approve the schema (§4) and freeze node/edge names.
2. Prototype the Phase-0 canonicalizer and measure heading/table recall on a
   labelled sample spanning markdown-heavy and plain-text files.
3. Run the Phase-A corpus sweep to seed the three taxonomies; stand up the
   Phase-B gold standard for 5 colonies before any corpus-scale run.

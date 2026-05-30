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
volume (1867–1966, ~2,228 colony-year `.txt` files) opens with a **semi-structured
annual report** on the colony itself, *before* the staff lists begin. By line
count this descriptive/statistical material is roughly **50–70% of each file** and
is currently unextracted.

The actual on-disk format. The manual parsing renders each section as a **bare
heading line ending in `.`** followed by prose; **statistics are embedded in the
sentences, not in tables** (there are *no* delimited tables anywhere in the
corpus). The period each figure describes is stated *in the sentence*. Verbatim,
1930 `JAMAICA.txt`:

```
Trade.
The total value of the imports for 1928 was £6,007,624 and of the domestic
exports £6,217,628.

Revenue.
The revenue and expenditure for the financial year 1928-29 were £2,663,924 and
£2,659,895 respectively.

Public Debt.
The public debt on the 31st March, 1929, amounted to £9,847,103.
```

And the richer narrative-with-embedded-numbers style of 1900 `JAMAICA.txt`:

```
Situation and Area.
Jamaica is an island in the Caribbean Sea ... containing about 4,207 square
miles ... It is estimated that Jamaica contains 2,692,480 acres ...

Industry.
... sugar (export 284,875 cwt., value 120,958L); coffee (export 85,410 cwt.,
value 165,494L); ginger (export 12,572 cwt., value 34,884L) ...
```

This is a century-long, ~50-colony **panel dataset** of public finance, trade,
population, area, shipping, communications, and production — plus rich narrative
on geography, history, and constitution. Extracting it turns the KG from a
prosopography into a quantitative + textual atlas of the empire, enabling queries
the personnel graph cannot answer (e.g. "plot Ceylon revenue vs. number of
officials, 1870–1950", "which colonies' export base was >80% one commodity",
"retrieve the constitutional history of Natal").

---

## 2. What the source actually looks like (extraction-relevant findings)

A cross-decade read of Jamaica, Ceylon, Hong Kong, and smaller colonies shows:

1. **One reliable surface pattern, one hard one:**
   - *Easy:* section boundaries — a **short line ending in `.`** acts as a
     heading (`Trade.`, `Revenue.`, `Public Debt.`, `Situation and Area.`,
     `Constitution.`, `Industry.`, `Shipping.`). These segment the entry cheaply.
   - *Hard:* **every statistic is embedded in a prose sentence**, with its period
     stated in words ("for 1928", "for the financial year 1928-29", "at the
     census taken in 1921"). There are **no delimited tables** to parse — so
     Track A is fundamentally an **LLM/regex-over-prose extraction**, not table
     reading. Currency markers vary even within a file (`£6,007,624`, `120,958L`,
     `Rs.`).
2. **Consistent section vocabulary:** Situation/Area, History, Climate &
   Inhabitants, Constitution/Government, Finance (Revenue & Expenditure, Debt),
   Population, Trade (Imports/Exports), Shipping & Tonnage, Communications
   (post/telegraph/rail/roads), Industry/Products, Education, Medical, Judicial,
   Ecclesiastical, Banking/Currency — then Governors list and Civil Establishment
   (personnel, already extracted).
3. **Figures are retrospective.** A 1930 volume reports 1928–29 figures; a 1900
   volume reports 1894–98. **The year a statistic describes (`observation_year`)
   is almost never the volume's `edition_year`**, and it is stated in the prose
   ("for 1928", "for the financial year 1928-29"). This is the single most
   important modeling consequence.
4. **Units/currencies vary** by colony and era: £ vs Rupees (Ceylon, Straits,
   Mauritius) vs HK$ (Hong Kong); area in square miles; crops in tons / cwt /
   lbs / stems / acres. Currency regimes also change mid-century for a colony.
5. **Format drifts across decades:** early volumes (1867–1880s) are heavily
   narrative/constitutional with sparse statistics (1867 Jamaica devotes pages to
   the Morant Bay rebellion); mid-period (1900–1930s) carry the densest embedded
   statistics; late volumes (1950s–60s) are condensed; war-era editions (1946–48)
   are thin. **OCR also garbles headings** (`Government.` → `Gcoernment.`,
   `CEYLON` dir entry `CceyYLON.txt`), so heading detection must be fuzzy.
6. **OCR reliability is lower on digits than text** — a documented risk
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

## 5. Extraction approach

Two tracks, both fed by an extended Stage 1 segmenter, both reusing existing
backends (local **Ollama gpt-oss:120b** primary; **OpenRouter**/**Gemini** and
**instructor + pydantic** for validation/fallback) and the project's
code-generation review option.

### Track A — Structured statistics (the hard, high-value part)

1. **Segment cheaply.** Extend the Stage 1 segmenter to split each entry at the
   bare `Heading.` lines (fuzzy-matched against the section taxonomy to tolerate
   OCR garbling), tagging each block with a `COL_ReportSectionType`. This is the
   one deterministic step; everything below operates on prose.
2. **Extract embedded figures with the LLM + pydantic schema**
   (`ColonyReportExtraction`). Because there are no tables, the model reads
   sentences like *"The revenue and expenditure for the financial year 1928-29
   were £2,663,924 and £2,659,895 respectively"* and emits two `COL_Observation`
   records (revenue, expenditure) with `observation_year_start=1928,
   observation_year_end=1929`. Prompt rules, encoded tersely (gpt-oss responds
   better to rules than examples):
   - *Transcribe digits exactly; never add, sum, round, or convert.*
   - *Extract the period each figure describes from the surrounding sentence.*
   - *Record `unit_raw`/`currency_raw` exactly as written (`£`, trailing `L`,
     `Rs.`, `tons`, `cwt.`, `acres`); leave normalization to a later stage.*
   - *Keep `value_raw` as the verbatim substring and a `source_span` offset so
     every number is auditable back to the page.*
   - *If illegible/ambiguous, emit with `confidence<0.5` rather than guessing.*
3. **(Optional) deterministic regex pre-pass** for high-frequency, low-ambiguity
   patterns (a currency-prefixed number adjacent to a year) to seed candidates
   and cross-check the LLM — but the LLM remains primary because period and
   indicator live in the surrounding prose, not in fixed columns.
4. **Verify numerics (cheap, deterministic):** a second pass cross-checks stated
   total vs. sum of printed components when both appear (**flag mismatches, do not
   auto-correct**), magnitude plausibility, and year-over-year continuity against
   neighbouring editions. Anomalies set `quarantined=true`.

### Track B — Narrative chunking + embedding

1. Chunk narrative sections by heading + paragraph (≤1,500 words, ≥200), tag with
   `section_slug` and `edition_year`.
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
| **A. Schema + taxonomy seed** | Freeze labels; sweep ~40 files across eras/regions to seed indicator/commodity/section taxonomies | `guides/colony_report_schema.py`, three `taxonomy/*_taxonomy.json` |
| **B. Segmenter + pilot** | Extend segmenter; build a gold standard for ~5 colonies spanning eras (Jamaica, Ceylon, Hong Kong, a settler colony, a small island) | `col_segment_reports.py`, `test_data/report_gold/*` |
| **C. Structured extraction** | Run Track A over the corpus with checkpointing/auto-push (reuse `extraction_corpus.py` patterns) | `col_extract_reports.py`, `generated/reports/*.json` |
| **D. Normalization** | Cluster + review indicators/commodities/sections; add canonical units/currencies | populated taxonomies, `col_normalize_reports.py` |
| **E. Neo4j load** | Constraints/indexes; load reports, observations, trade flows | `col_load_reports_neo4j.py` |
| **F. Narrative embedding** | Track B chunking + embedding (aligns with Stage 5) | `col_embed_reports.py`, `COL_NarrativeChunk` nodes |
| **G. Validation + viz** | Gold-standard accuracy, panel QA (continuity, totals), demo charts | `col_audit_reports.py`, sample notebooks/HTML |
| **H. External linking (opt.)** | Commodities → Wikidata; indicators → a standard vocab | Stage-6-style `SAME_AS`/`EXTERNAL_LINK` edges |

Phases A→B should be reviewed and the schema frozen before C runs at corpus scale.

---

## 8. Risks & mitigations

- **OCR digit errors** → raw + parsed values, confidence scores, quarantine,
  cross-edition continuity checks; never auto-compute.
- **observation-year vs edition-year confusion** → first-class
  `observation_year_start/end`; loaders link `OBSERVED_FOR` by observation year.
- **Unit/currency heterogeneity** → preserve `*_raw`; convert only in a versioned
  normalization layer with documented rates.
- **Format drift across a century** → era-aware prompts/segmentation; extend the
  regional `guides/*` (which already encode colony-specific patterns) with
  report-format notes.
- **Federations / sub-colony tables** (Leeward/Windward, Straits, Canada) → reuse
  existing federation handling; attach observations to the correct member
  `TerritoryYear`.
- **Scope creep** → Track A priorities are finance/trade/population/area/shipping;
  deep tables (detailed education/medical breakdowns) are a later pass.

---

## 9. Teaching value (this is also a course project)

The colony-report track is a strong HIST 496 extension: the *same* document
yields a second, quantitatively different extraction problem (noisy tables vs.
clean rosters). Students practice schema design for panel data and confront the
observation-year subtlety and OCR-confidence trade-offs first-hand. The Phase-B
gold standard can double as a lab exercise.

---

## 10. Immediate next steps

1. Review/approve the schema (Section 4) and freeze node/edge names.
2. Run the Phase-A corpus sweep to seed the three taxonomies.
3. Draft `guides/colony_report_schema.py` and stand up the Phase-B gold standard
   for 5 colonies before any corpus-scale run.

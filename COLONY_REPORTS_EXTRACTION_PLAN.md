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

This is a century-long **panel dataset** of public finance, trade, population,
area, shipping, communications, and production — plus rich narrative on geography,
history, and constitution. Extracting it turns the KG from a prosopography into a
quantitative + textual atlas of the empire, enabling queries the personnel graph
cannot answer (e.g. "plot Ceylon revenue vs. number of officials, 1870–1950",
"which colonies' export base was >80% one commodity", "retrieve the
constitutional history of Natal").

**Caveat on density (see Finding §2.7):** the quantitative payoff is concentrated
in the ~50 large colonies (Ceylon, Jamaica, the Australasian colonies, India-
adjacent territories, etc.). Most of the long tail of small colonies and most
pre-1900 editions are narrative-dominant with few or no statistics, so the
"panel" is dense for big colonies and sparse-to-empty for small ones. The
narrative track (Track B) is the universally valuable output; the statistical
track (Track A) is high-value but unevenly populated.

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
   discipline and confidence flagging, not silent computation. **But the corpus is
   intrinsically redundant, which is the saving grace:** successive editions
   republish a *rolling window* of prior years and census years recur in every
   edition — e.g. the 1894–1900 Jamaica volumes each carry ~1888–1895 revenue
   rows, and 1861/1871/1881 census figures appear in all of them. So most
   underlying figures are independently re-OCR'd 3–10+ times, enabling
   majority-vote and component-sum cross-checks (see §3, "trust trends, not
   points"). This redundancy is what makes trend analysis trustworthy even though
   no individual datapoint is.
7. **Enormous variation by colony size — the richness assumption only holds for
   large colonies.** Measured over all 2,946 files, words/file span 0–212,392
   (p10 900, median 4,120, p90 11,350; the few giants are multi-state entries
   like AUSTRALIA at ~85k and an anomalous 1888 ASCENSION). Crucially,
   **statistical density scales with size as a tendency, not a law**: files <800
   words have a *median of 0* pipe-table rows, while files >5,000 words have a
   *median of ~70–80* — but the federation mega-entries are table-rich
   (Dominion of Canada runs 114–465 pipe rows per edition, 1879–1899), so size
   predicts *volume* of data, not its structuredness, reliably. Small colonies are
   qualitatively different, not just shorter — 1900 Ascension's *entire* report is
   a single descriptive paragraph (geography, garrison, turtles, ~166 population,
   "all expenses charged to naval funds") followed by one line of staff, with **no
   section headings and no tables at all** — no finance, trade, or commodity data.
   So `COL_Observation`/`COL_TradeFlow` output will be **rich for ~50 large
   colonies and near-empty for the long tail of small ones** — which is correct
   behaviour, not extraction failure, and the pipeline/validation must not flag it
   as such.
8. **Size and decade interact, non-monotonically.** Jamaica grows steadily
   (4,805 w in 1867 → 11,779 w in 1940); Falkland holds ~2,000–3,200 w with
   tables in every era *except* its broken 1940 file (291 w, 0 tables). So neither
   "later = bigger" nor "small colony = always sparse" holds reliably. Expectations
   must be set per (colony, year) from the file's own size/table profile, with
   sharp drops vs. neighbouring editions flagged as likely parse failures (§2.9).
9. **A long tail of degenerate/broken files needs triage before extraction.**
   **104 files are <150 words and 172 are <400**, including a genuinely empty
   one (`1958/jamaica.txt`, 0 bytes) and a truncated parse (`1917/AUSTRALIA.txt`,
   1 word — while Australia is 80,000+ words in 1919–1927). A missing report can
   *masquerade as a small colony*: 1940 Falkland is 291 words / 0 tables, far
   below its own 1900/1920 ~2,300-word reports. Filenames are also OCR-/parse-
   garbled (`_REF` suffixes, split entries) and case-inconsistent
   (`JAMAICA.txt` vs `jamaica.txt`). All of this must be detected and quarantined
   up front — and crucially **distinguished from genuinely small colonies** — or
   broken files will be silently scored as "colonies with no data."
10. **Federations are a distinct mega-entry regime with a self-cross-cutting
    representation that must be reconciled.** The dominions dwarf ordinary
    colonies and are handled inconsistently across the run:
    - **Scale (verified):** *Dominion of Canada* runs 15,817 w (1879) → 31,304 w
      (1890), against a contemporaneous Jamaica of ~5,100–7,000 w — i.e. 3–6× a
      large ordinary colony. The Commonwealth `AUSTRALIA.txt` reaches ~85k w
      (1920). So a single "colony report" can be an order of magnitude larger and
      internally nests many sub-units (states/provinces).
    - **Representation switches over time, with brief overlap.** Australia's
      states appear as their *own* files (`NEW_SOUTH_WALES.txt`, `VICTORIA.txt`, …)
      from 1867 up to ~1906, then a single aggregate `AUSTRALIA.txt` takes over
      from 1908 onward — but the two coexist in **1908 and 1917** (both the
      aggregate *and* a `NEW_SOUTH_WALES.txt` exist those years). Canada appears
      as `canada.txt` (1867) then `dominion_of_canada.txt` (1879–1899) and drops
      out thereafter as it gained autonomy.
    - **Consequences for extraction:** (a) reconcile entity-name drift
      (`canada`↔`dominion_of_canada`; states↔`AUSTRALIA`) onto stable
      `COL_Territory`/sub-territory identities; (b) in the overlap years,
      de-duplicate state figures that appear in both the aggregate and the
      own-file; (c) segment the aggregate's nested per-state/province sections and
      stamp each observation with the correct sub-unit, not just "Australia".
    (These are *measured* facts from the file inventory, not assumptions — the
    exact-year coexistence was checked per directory.)
11. **The existing personnel pipeline already located many parse problems — and
    its failures map to *report-track opportunities* (verified cross-reference).**
    `EXTRACTION_AUDIT_RESULTS.md` flags 627 colony-years (317 "empty extraction",
    72 missing-governor, 93 dual-discrepancy, 144 Neo4j-mismatch, 1 honours
    contamination). Cross-referencing these against the source files
    (`col_canonicalize_reports.py` word/table counts) shows:
    - **"Empty extraction (0 officials)" is a personnel-extractor failure, not an
      empty source.** Of 276 matched cases, only **20 have a truly empty source
      (<150 w); 228 are report-rich (≥1,000 w)** — and they are exactly the giant
      table-dense mega-entries the staff-list extractor could not segment:
      Australia 1914–1922 (~77–85k w, 60–80 table-blocks each), South Africa
      1913–1919, Straits Settlements 1928–29, West Indies 1959. **These are the
      report track's prime recovery targets**: a century of finance/trade/
      population tables the personnel pass dropped on the floor.
    - **Source-level contamination is real and the personnel honours-marker
      detector catches it better than a size heuristic.** Aden 1922 has an
      appendix honours list bled into its entry (6,887 w vs neighbours' 336/1,087;
      33 in-text honours markers), but is *not* flagged as size-anomalous because
      Aden's own median is inflated by other large editions. Reuse that detector
      for section-boundary bleed (Track A step 0).
    - **Entity-name drift between pipelines** must be reconciled before any join:
      personnel keys (`Aden_Colony`, `Bahama_Islands`, `Bermudas`) differ from the
      filenames (`ADEN`, `BAHAMAS`, `BERMUDA`) — same problem as the federation
      name drift in §2.10, now also a cross-pipeline concern.

---

## 3. Design principles (inherited from the existing KG)

Non-negotiable, because they are what makes the current graph trustworthy:

- **Treat numbers as noisy observations, not facts — trust trends, not points.**
  OCR on digits is unreliable enough that **no single extracted figure should be
  trusted on its own**; the value is in aggregates and trajectories over many
  redundant reads. This is feasible here because the source is *intrinsically
  redundant* (see box below): successive editions republish a rolling window of
  the same years, and census years recur in every edition, so most underlying
  figures are read 3–10+ times. The data model and downstream use must reflect
  this: keep every individual read with its provenance and confidence, never
  silently pick one, and compute trends/consensus rather than relying on any
  lone datapoint.

  > **Worked example (verified in the corpus).** Jamaica's 1881 census population
  > row appears in the 1897, 1898, and 1900 editions with components *identical*
  > (14,433 / 109,946 / 444,186 / 12,240) but the **total** OCR'd as **670,705**
  > in 1897 vs **580,804** in 1898 and 1900. Three independent reads expose the
  > 1897 figure as the outlier two ways at once — by **majority vote** (2 agree)
  > and by **internal check** (the components sum to ~580,804, not 670,705).
  > Neither signal exists if you extract the number once and trust it.

  > **Second, independent example (Mauritius, verified).** Mauritius revenue is
  > reprinted across the 1897/1898/1900 editions. For observation-year **1893** all
  > three editions agree exactly (Rs. 8,103,922) → unanimous, high confidence. For
  > **1894** the same figure is OCR'd three different ways — 8,**5**84,427 (1897),
  > 8,**5**34,427 (1898), 8,**5**54,427 (1900) — drift confined to one digit, so a
  > robust/median estimate (~8.55M) is trustworthy though no single read is. For
  > **1895** two editions cluster (~8,27x,622) and the 1900 read (8,529,932) is an
  > exposed outlier. This corroborates the principle on a *second colony and a
  > different currency regime* (note the £→Rs. and 4-col→2-col drift across the
  > same three editions, also illustrating Findings §2.4/§2.6).

  Practical implications, threaded through the plan:
  - **Never compute or "repair" a value into the slice layer** (already a
    principle below) — but *do* record, separately, the cross-read consensus and
    the component-sum check as derived, provenance-stamped annotations.
  - **Store every occurrence.** The same (colony, indicator, observation_year)
    seen in N editions becomes N `COL_Observation` nodes, each with its
    `edition_year` and `value_raw`; a later reconciliation step derives a
    consensus value + dispersion, it does **not** collapse them on ingest.
  - **Confidence reflects agreement.** A figure corroborated across editions
    and passing its component-sum check is high-confidence; a lone or
    disagreeing read is flagged/quarantined.
  - **Analysis-layer guidance.** Downstream queries and visualizations should
    plot series with uncertainty (or robust/median series), not single values,
    and should be honest that point estimates are unreliable.

- **Discover structure from corpus scale, not from a small gold standard.**
  The data is too irregular for a 15–20 file hand-labelled sample to *train* on;
  used that way it overfits, and hand-authored maps (the federation→sub-unit list
  the boundary detector first used) are brittle and need endless maintenance.
  Instead, mine the regularities from the **full 2,946-file corpus** and let two
  scale properties carry the work: (1) **redundancy** — names, sections and
  figures recur thousands of times, so patterns are *countable*, not guessed;
  (2) **self-consistency** — cross-edition repetition lets the data check itself
  (majority vote / component-sum for values; *dominant-host* for structure). A
  gold standard is then a **ruler (for measuring the result), not a teacher (for
  deriving it).** `col_mine_corpus_patterns.py` realizes this: with no hand map
  it derives the federation families (merging the §2.10 name-drift automatically),
  the floating-appendix set, and the empirical section/indicator vocabularies
  (frequency-ranked headings & table columns).
  - *Caveats, kept in view:* scale also amplifies **systematic** errors (a
    recurring OCR garbling looks like a pattern by frequency alone) — so trust
    self-consistency, not raw frequency; and the **long tail is real signal**
    (Finding §2.7), so "rare" must not be auto-pruned as "noise". Also, **misparses
    contaminate the derived structure** (the British Honduras→Canada misparse makes
    `british_honduras` look like a Canada parent-variant), so structure discovery
    and boundary triage are **iterative**: detect misparses → exclude → re-mine;
    and derived-vs-hand discrepancies are themselves misparse signals, not an
    automatic override of the boundary detector.
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
- **Triage degenerate files (Finding §2.9):** flag empty, suspiciously short
  (e.g. <150 words), and OCR-garbled-filename files; cross-check each file's size
  against its colony's neighbouring editions to catch truncated parses (the 1898
  Jamaica fragment). Route these to a quarantine/review queue rather than the
  extractor, so they are not silently mistaken for genuinely small colonies.
- **Reuse the personnel pipeline's error signals — but invert their meaning
  (Finding §2.11).** `EXTRACTION_AUDIT_RESULTS.md` already catalogues 627 flagged
  colony-years. Two of its signals transfer to the report track: (a) the
  **honours / cross-colony-directory contamination** detector (section-boundary
  bleed) catches source corruption that a size heuristic misses — e.g. Aden 1922
  carries 33 honours-list markers in-text but is not size-anomalous against
  Aden's own (inflated) median; import this marker check into triage. (b) The
  small subset of *truly* empty sources corroborates Phase-0 triage (20/20 agree).
  **Do NOT, however, treat the personnel "empty extraction (0 officials)" list as
  a skip-list:** 228 of 276 such cases are report-rich (≥1,000 w) — they are the
  mega-entries the staff-list extractor choked on, and are the report track's
  highest-value *recovery* targets, not failures (see §2.11).
- **Record a per-file expectation profile (Finding §2.7–2.8):** word count and
  table count, used downstream to set realistic yield expectations per
  (colony, year) — a near-empty extraction from Ascension is success; a
  near-empty extraction from a 12,000-word Ceylon file is a bug.

- **Boundary-integrity classification (the highest-stakes triage, Finding §2.11).**
  The most important thing Phase 0 protects is not heading recall but *attribution
  correctness* — never letting one colony's figures be filed under another. A
  single size heuristic cannot do this: it conflates a whole-volume dump, a
  wrong-colony concatenation, and a legitimate federation mega-entry, which need
  opposite handling. The canonicalizer therefore classifies by **content**, using
  a colony-name gazetteer (built from the 2,946 filenames) and a federation→
  sub-unit allow-list (from `guides/federated_territories_guide.md` and
  `settler_colonies_guide.md`):
  - `federation_nested` — the entry's *own* sub-units appear inside it (Australia→
    its states, Dominion of Canada→provinces, Straits/Malaya→Malay states, Union
    of South Africa→provinces+HC territories). **Not an error — a recovery target**;
    each observation must be stamped with the correct sub-unit (§2.10).
  - `multi_colony_misparse` — *unrelated* colonies are concatenated into the file
    (British Honduras 1910 actually holds the Canada section; Weihaiwei holds
    Pacific territories). Corroborated by either ≥4 unrelated colony headers or a
    size outlier, so incidental prose mentions don't false-trigger. **Do not
    attribute — quarantine/split.**
  - `appendix_contamination` — honours-list / "General Colonial Service List"
    markers bled in (Aden 1922); reuses the personnel pipeline's detector and
    catches bleed a size heuristic misses.
  - `volume_dump` — extreme absolute size as a backstop, since header detection
    undercounts dumps whose colony headers are OCR-mangled (1888 Ascension).

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
5. **Cross-edition reconciliation (the trust mechanism — separate step, never on
   ingest).** Because the same (colony, indicator, observation_year) is printed in
   several editions (§2.6), group the resulting `COL_Observation` nodes by that
   key and derive — as *new, provenance-stamped* annotations, leaving the raw
   reads untouched:
   - a **consensus value** (majority vote across reads; median for continuous
     quantities) and a **dispersion** measure;
   - an **agreement-based confidence** (corroborated + component-sum-consistent →
     high; lone or conflicting → low/quarantined);
   - an **outlier flag** on reads that disagree with both the consensus and any
     internal component-sum (the 1881 "670,705 vs 580,804" case, §3).
   This is what turns individually-untrustworthy OCR figures into trustworthy
   trends. It belongs in the normalization/analytic layer (Phase D), not the
   extractor.

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
| **0. Canonicalization** | ✅ **Built & validated** (deterministic, no LLM): `col_canonicalize_reports.py` segments every file into typed blocks (prose / table / heading / dot_leader / colony_header), parses ragged pipe tables, detects heading *candidates* + style (md/bold/bare-period/inline-dash/ALL-CAPS), and runs degenerate-file triage. Ran clean over all 2,946 files in ~21s: 90% have ≥1 parsed table block; conservative keyword fallback maps a section slug for 85% of files (residual deferred to the meaning-based normalizer); triage flags 1 empty, 103 very-short, 178 possible-truncation, 23 anomalous-giant misparses (e.g. 1888 Ascension 212k w, 1898 Tristan da Cunha 200k w). Heading→slug *meaning* mapping (the part that needs the model) is stubbed behind `heading_slug_guess`. Still TODO: labelled heading/table recall sample | `col_canonicalize_reports.py` (done), `generated/reports_canonical/*.json` (regenerable: one command) |
| **A. Schema + taxonomy seed** | Freeze labels; **seed taxonomies from the FULL corpus, not a 40-file sample** (`col_mine_corpus_patterns.py`): frequency-ranked headings → section taxonomy, frequency-ranked table columns → indicator taxonomy, co-occurrence → federation families + floating-appendix set. Human review reconciles, the gold set only measures. | `guides/colony_report_schema.py`, three `taxonomy/*_taxonomy.json`, `generated/corpus_patterns.json` (done, v0) |
| **B. Segmenter + pilot** | Build a gold standard deliberately spanning the size×decade matrix — a large colony early & late (Jamaica 1867/1940), a statistics-dense one (Ceylon), a small colony across eras (Falkland 1867/1920), a near-empty real one (1900 Ascension, 134 w — pure prose, no tables), and a degenerate file (1958 Jamaica, empty; or 1940 Falkland, truncated) — so accuracy is measured across the real variation, not just on big colonies | `col_segment_reports.py`, `test_data/report_gold/*` |
| **C. Structured extraction** | Run Track A over the corpus with checkpointing/auto-push (reuse `extraction_corpus.py` patterns) | `col_extract_reports.py`, `generated/reports/*.json` |
| **D. Normalization + reconciliation** | Cluster/review indicators/commodities/sections; add canonical units/currencies; **cross-edition reconciliation → consensus value, dispersion, agreement-confidence, outlier flags** (Track A step 5) | populated taxonomies, `col_normalize_reports.py`, `col_reconcile_observations.py` |
| **E. Neo4j load** | Constraints/indexes; load reports, observations, trade flows | `col_load_reports_neo4j.py` |
| **F. Narrative embedding** | Track B chunking + embedding (aligns with Stage 5) | `col_embed_reports.py`, `COL_NarrativeChunk` nodes |
| **G. Validation + viz** | Gold-standard accuracy; panel QA (continuity, totals, cross-edition agreement rate); **trend/series charts with uncertainty, not point values** | `col_audit_reports.py`, sample notebooks/HTML |
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
- **Federations / mega-entries (Finding §2.10)** (Canada, Australia,
  Leeward/Windward, Straits) → decompose the aggregate into per-state/province
  blocks and stamp each observation with the sub-unit; in the 1908/1917 overlap
  years de-duplicate state figures present in both aggregate and own-file;
  reconcile name drift (`canada`↔`dominion_of_canada`, states↔`AUSTRALIA`) to
  stable `COL_Territory` identities.
- **Scope creep** → Track A priorities are finance/trade/population/area/shipping;
  deep tables (detailed education/medical breakdowns) are a later pass.
- **Mistaking sparse small-colony output for failure (Finding §2.7–2.9)** →
  size/table expectation profile per file; validate yield *relative to* a file's
  size and its colony's neighbours, not against a flat threshold; up-front triage
  of empty/truncated/garbled files so they don't pollute the "small colony" bucket.
- **Over-investing the statistical track on thin material** → prioritize Track A
  on the large colonies and the table-bearing later editions where the data
  actually is; rely on Track B (narrative embedding) for the small/early long
  tail, where prose is the only content.

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

# GraphRAG Pipeline Design: Colonial Office List 1867–1966

## Purpose

This document specifies a data pipeline to transform 2,228 manually parsed Colonial Office List text files into a knowledge graph with integrated vector search (GraphRAG). The design prioritizes historical fidelity over computational convenience. It preserves complexity rather than reducing it, and is intended as foundational infrastructure for a decade of scholarship.

---

## 1. Architecture Overview

### 1.1 Three Spines

The graph is organized around three independent structural dimensions:

- **Geography** — colonies, protectorates, dominions, federated territories, provinces, and their sub-divisions
- **Institution** — departments, offices, and position-types that recur across the empire
- **Time** — year-anchored slices forming a left-to-right timeline through which the graph progresses

Any entity in the graph can be located at the intersection of these three dimensions. "Colonial Secretary's Department, Sierra Leone, 1896" is a specific instantiation — a point in geography × institution × time space.

### 1.2 Two-Tier Entity Model

Every major entity class uses a **persistent node + temporal slice** pattern:

```
Persistent Node (identity)          Slice Node (evidence)
──────────────────────────          ─────────────────────
Ceylon                              Ceylon_1899
  - wikidata: Q35600                  - source_file: 1899_manual_parsed/ceylon.txt
  - geonames: ...                     - narrative_chunks: [...]
  - fromans: ...                      - institutional_structure: [...]
  - modern_successor: Sri Lanka       - links_to: Ceylon_1898, Ceylon_1900
```

**Persistent nodes** carry time-invariant properties and external linkages. They are identity claims — assertions that a set of slices refer to the same real-world entity.

**Slice nodes** carry what the source actually attests for a given year. They are evidence. The graph's temporal structure lives at this layer.

### 1.3 Data Layers

The pipeline produces four integrated layers:

| Layer | Content | Storage |
|-------|---------|---------|
| **Knowledge Graph** | Entities, relationships, temporal structure | Graph database (Neo4j or equivalent) |
| **Vector Store** | Embedded narrative text chunks | Vector database (linked to graph nodes) |
| **Research Queue** | Candidate identity matches requiring human review | Structured output (JSON/CSV) |
| **Provenance Log** | Extraction metadata, confidence scores, pipeline version | Attached to all graph edges |

---

## 2. Graph Schema

### 2.1 Node Types

#### Geography

| Node Type | Tier | Description | Example |
|-----------|------|-------------|---------|
| `Territory` | Persistent | Enduring identity of a colony/protectorate/dominion | Ceylon, Sierra Leone, Canada |
| `TerritoryYear` | Slice | A territory as recorded in a specific year's CO List | Ceylon_1899 |
| `SubTerritory` | Persistent | Province, district, or constituent of a federation | Province of Uva, British Columbia |
| `SubTerritoryYear` | Slice | A sub-territory in a specific year | BritishColumbia_1872 |
| `Year` | Anchor | A first-class year node anchoring all slices for that year | 1899 |

#### Institution

| Node Type | Tier | Description | Example |
|-----------|------|-------------|---------|
| `InstitutionType` | Persistent | A recurring institutional template across the empire | Medical Department, Treasury |
| `InstitutionInstance` | Slice | A specific department in a specific colony-year | MedicalDepartment_SierraLeone_1896 |
| `PositionType` | Persistent | A functional role that recurs across colonies | Colonial Secretary, Colonial Surgeon |
| `PositionInstance` | Slice | A specific post in a specific colony-year | ColonialSecretary_SierraLeone_1896 |

#### Person

| Node Type | Tier | Description | Example |
|-----------|------|-------------|---------|
| `Person` | Persistent | Identity claim — created only when threshold is met | Sir Frederick Cardew |
| `PersonRecord` | Slice | An individual as recorded in one colony-year | Cardew_SierraLeone_1896 |

#### Career

| Node Type | Tier | Description | Example |
|-----------|------|-------------|---------|
| `CareerTrack` | Persistent | A professional domain (see §4.2) | Medical, Legal, Administrative |

### 2.2 Edge Types

#### Temporal Edges (the timeline)

| Edge | Connects | Meaning |
|------|----------|---------|
| `CONTINUES_AS` | Slice → Slice | Same entity, next year. The default temporal link |
| `MERGES_INTO` | Slice → Slice | Two entities combine (Northern Nigeria 1913 → Nigeria 1914) |
| `SPLITS_INTO` | Slice → Slice | One entity divides |
| `SUCCEEDS` | Slice → Slice | Replacement with discontinuity (name change, constitutional reorganization) |
| `IN_YEAR` | Slice → Year | Anchors a slice to its year node |

#### Structural Edges

| Edge | Connects | Meaning |
|------|----------|---------|
| `INSTANCE_OF` | Slice → Persistent | Links a temporal slice to its enduring identity |
| `CONTAINS` | TerritoryYear → SubTerritoryYear | Geographic nesting (Canada_1872 → BC_1872) |
| `HAS_DEPARTMENT` | TerritoryYear → InstitutionInstance | A colony-year's institutional structure |
| `HAS_POSITION` | InstitutionInstance → PositionInstance | A department contains positions |
| `OCCUPIED_BY` | PositionInstance → PersonRecord | A person holds a post |
| `BELONGS_TO_TRACK` | PositionType → CareerTrack | Career track classification |
| `TYPE_OF` | InstitutionInstance → InstitutionType | Department family membership |
| `TYPE_OF` | PositionInstance → PositionType | Position family membership |

#### Identity Edges

| Edge | Connects | Meaning | Properties |
|------|----------|---------|------------|
| `SAME_AS` | PersonRecord → Person | Links a record to a persistent identity | confidence, method, confirmed_by |
| `CANDIDATE_MATCH` | Person → Person | Two persistent person nodes that may be the same individual | confidence, evidence, status |
| `EXTERNAL_LINK` | Persistent → External | Link to Wikidata, ODNB, VIAF, etc. | uri, source, date_linked |

#### Cross-Colony Edges (discovered from narrative and personnel data)

| Edge | Connects | Meaning |
|------|----------|---------|
| `TRADE_WITH` | TerritoryYear → TerritoryYear | Trade relationship mentioned in narrative |
| `TELEGRAPH_TO` | TerritoryYear → TerritoryYear | Communication link |
| `SHIPPING_ROUTE` | TerritoryYear → TerritoryYear | Regular shipping service |
| `SHARED_JURISDICTION` | InstitutionInstance → InstitutionInstance | E.g., a bishop whose diocese spans colonies |
| `CONSUL_OF` | PersonRecord → External Entity | Foreign consul representing another nation |

### 2.3 Properties

#### On All Edges

Every edge in the graph carries:

```
provenance: {
  method: "automated_extraction" | "manual_annotation" | "external_match",
  pipeline_version: "1.0",
  confidence: 0.0–1.0,
  date_created: "2026-02-06",
  confirmed_by: null | "scholar_id",
  notes: null | "free text"
}
```

#### On PersonRecord Nodes

```
name_raw: "Lt.-Col. J. O. Gore"           # exactly as it appears in source
surname: "Gore"
given_names: "J. O."
position_raw: "Colonial Secretary"          # as it appears
department_raw: "Colonial Secretary's Department"
salary_min: 710                             # nullable
salary_max: 800                             # nullable
salary_currency: "GBP"                      # GBP | Rs | dollars
allowances_raw: "quarters"                  # nullable, unparsed string
honors: ["C.M.G."]                          # list, only those attested this year
qualifications: ["M.D.", "L.R.C.P."]        # list
military_rank: "Lt.-Col."                   # nullable
location: "Freetown"                        # nullable, where attested
source_file: "1896_manual_parsed/sierra_leone.txt"
source_line: 16                             # nullable, line reference
```

#### On Person (Persistent) Nodes

```
canonical_name: "Gore, James O."            # best-known full name
surname: "Gore"
given_names: "James O."                     # expanded where known
birth_year: null                            # from external sources
death_year: null
wikidata_qid: null                          # e.g. "Q12345678"
odnb_id: null
viaf_id: null
persistence_reason: "longevity"             # longevity | seniority | cross_colony | external_match
first_appearance: 1892
last_appearance: 1903
career_tracks: ["administrative"]
```

---

## 3. Pipeline Stages

### Stage 0: Corpus Inventory and Temporal Scaffolding

**Input:** The 60 year-directories and their file listings.

**Process:**
1. Enumerate all year-directories, build the `Year` anchor nodes (1867, 1868, ..., 1966)
2. For each year, list all colony files. Create `TerritoryYear` slice nodes
3. Match colony filenames across years to establish `CONTINUES_AS` chains (e.g., `sierra_leone.txt` appears in 42 of 60 years)
4. Flag naming variations for manual review (e.g., `cape_of_good_hope` vs. `cape_colony`; `dominion_of_canada` vs. `canada`)
5. Integrate with existing colony knowledge graph to create or link `Territory` persistent nodes
6. Build the geographic containment hierarchy for federated territories (Leeward Islands → Antigua, etc.) using known historical dates of federation/dissolution

**Output:** The temporal-geographic skeleton of the graph. Every colony-year has a node, every colony has a persistent anchor, and the timeline edges connect them.

**Open questions to resolve empirically:**
- Full inventory of colony name variations across the 100-year span
- Which colonies appear in which years (coverage matrix)
- Which federated/nested structures exist and when they change

### Stage 1: Document Segmentation

**Input:** Raw text files (2,228 files).

**Process:**

Each file contains a mix of narrative prose and structured personnel data. These require different extraction strategies and must be segmented before processing.

Segment each file into typed sections:

| Section Type | Identification Signal | Downstream |
|-------------|----------------------|------------|
| **Narrative** | Prose paragraphs: history, geography, climate, trade, law, education, religion, infrastructure | → Vector embedding (Stage 5) |
| **Personnel Roster** | Department headers followed by position/name/salary lines | → Structured extraction (Stage 2) |
| **Statistical Table** | Tabular data with columns of numbers (revenue, population, trade) | → Lower priority, flag for future |
| **Governor List** | Chronological list of governors with dates | → Structured extraction (Stage 2) |
| **Council Membership** | Executive/Legislative Council listings | → Structured extraction (Stage 2) |
| **Foreign Consuls** | Consul listings for other nations | → Structured extraction (Stage 2) |

**Segmentation approach:**
- Use section headings as primary delimiters ("Civil Establishment.", "Medical Department.", "History.", "Climate.", etc.)
- Build a heading taxonomy from the full corpus (headings are highly regular across colonies)
- Classify each section by type using heading + content heuristics
- Handle the settler colony exception: these have different section patterns (responsible government structures, provincial sub-sections)

**Output:** Each file decomposed into typed, labeled sections with byte offsets back to the source.

### Stage 2: Personnel Extraction

**Input:** Segmented personnel roster sections.

**Process:**

Extract structured records from the personnel data. This is the most technically challenging stage due to the formatting conventions of the CO List.

#### Key extraction challenges:

**Ditto marks:** "2nd ditto" means "2nd [whatever the previous position was]". Requires stateful parsing — each line depends on context from preceding lines.

**Multiple people per line:** "Assistant ditto, Wm. Renner, M.R.C.S., 300l. to 350l.; M. L. Jarrett, M.R.C.S., 250l.; I. N. Paris, M.B., 200l." — three people, one line, semicolon-separated.

**Abbreviated names:** First names almost always appear as initials only. Occasionally full first names appear (Jacob W. Lewis, Bruce Faulkner).

**Position/name ambiguity:** "Kent, 40l., and quarters." — is Kent a person or a place? (It's a place — this is a dispenser posting with no name, meaning the post is vacant or the occupant unnamed.)

**Salary notation variation across time and colony:**
- British pounds: "200l.", "2,000l.", "300l. to 350l."
- Rupees: "Rs. 12,000", "Rs. 3,000 to Rs. 4,000"
- Other: dollars, local currencies
- Allowances in many forms: "and quarters", "travelling allowance, 91l. 5s.", "and 50l. personal"

**The settler colony problem:** Dominions with responsible government have fundamentally different administrative structures. Provincial sub-sections. Ministers rather than department heads. The extraction logic must branch on colony type.

#### Extraction strategy:

Use LLM-based extraction (as demonstrated in `extraction_instructor.py`) as the primary method, with regex patterns (as in `extraction_regex.py`) as validation cross-checks.

For each personnel section:
1. Identify the department/institutional context from the section heading
2. Parse line-by-line with ditto-state tracking
3. For each person-line, extract: name components, position, salary, honors, qualifications, military rank, location
4. Create `PersonRecord` slice nodes and `PositionInstance` slice nodes
5. Link them: `PositionInstance -[OCCUPIED_BY]-> PersonRecord`
6. Link positions to departments: `InstitutionInstance -[HAS_POSITION]-> PositionInstance`
7. Link departments to colony-year: `TerritoryYear -[HAS_DEPARTMENT]-> InstitutionInstance`

**Output:** Structured person records linked into the institutional hierarchy for each colony-year.

### Stage 3: Institution and Position Normalization

**Input:** Extracted institution instances and position instances from Stage 2.

**Process:**

The same institutional template appears across dozens of colonies with minor naming variations. This stage builds the persistent institution and position layers.

#### Institution type normalization:

Cluster institution instances across the full corpus:
- "Medical Department", "Medical Dept.", "Medical and Sanitary Department" → `InstitutionType: Medical Department`
- "Colonial Secretary's Department", "Colonial Secretary's Office" → `InstitutionType: Colonial Secretary's Department`
- "Treasury Department", "Treasury", "Treasurer's Department" → `InstitutionType: Treasury`

Build `InstitutionType` persistent nodes and link instances to them via `TYPE_OF` edges.

#### Position type normalization:

Similarly cluster position titles:
- "Colonial Secretary", "Col. Secretary", "Col. Sec." → `PositionType: Colonial Secretary`
- "Colonial Surgeon", "Col. Surgeon" → `PositionType: Colonial Surgeon`

Note: **variability is expected and should be preserved, not forced into false uniformity.** A "Government Agent" in Ceylon (provincial administrator) is not the same role as a "Government Agent" elsewhere. Position type normalization should be conservative — only cluster when the functional equivalence is clear. Ambiguous cases remain as separate types until a scholar resolves them.

#### Career track classification:

Assign each `PositionType` to one or more `CareerTrack` nodes:

| Career Track | Example Positions |
|-------------|-------------------|
| **Executive/Administrative** | Governor, Colonial Secretary, Assistant Colonial Secretary, Government Agent, District Commissioner, Cadet |
| **Legal/Judicial** | Chief Justice, Attorney-General, Solicitor-General, Crown Counsel, District Judge, Police Magistrate |
| **Medical** | Colonial Surgeon, Assistant Colonial Surgeon, Medical Officer, Dispenser |
| **Financial** | Treasurer, Auditor-General, Collector of Customs |
| **Engineering/Public Works** | Director of Public Works, Provincial Engineer, District Engineer |
| **Survey/Lands** | Surveyor-General, Superintendent of Survey |
| **Police/Prisons** | Inspector-General of Police, Superintendent of Police |
| **Ecclesiastical** | Bishop, Chaplain, Archdeacon |
| **Education** | Director of Public Instruction, Inspector of Schools |
| **Military** | Officer Commanding, Brigadier-General (where part of colonial establishment) |
| **Postal/Telegraph** | Postmaster-General, Superintendent of Telegraphs |
| **Agricultural/Scientific** | Director of Botanic Garden, Conservator of Forests |

This list is a starting point. The actual taxonomy should be derived empirically from the corpus by clustering positions by department co-occurrence and cross-colony patterns. Some positions belong to multiple tracks (a medical officer who becomes a colonial administrator).

**Output:** Persistent institution type and position type nodes with cross-colony linkages. Career track taxonomy.

### Stage 4: Person Linking

**Input:** All `PersonRecord` slice nodes from Stage 2, career track classifications from Stage 3.

**Process:**

This is the most intellectually demanding stage. It operates in three phases.

#### Phase 4a: Within-colony career chains

Link person records across years within the same colony. This is the easiest case.

Matching signals:
- Exact surname match
- Compatible initials (initials may expand across years as someone becomes more prominent)
- Same or plausibly successive position
- Compatible honors (honors only accumulate)
- Compatible qualifications (permanent)
- Compatible military rank (only increases)

This produces **career chains** — sequences of PersonRecord nodes linked within one colony. Most chains will be unambiguous. Flag ambiguous cases (common surnames, e.g., multiple "Smith" entries in the same colony).

#### Phase 4b: Earned persistence

Apply threshold criteria to promote career chains to persistent `Person` nodes:

| Criterion | Threshold | Rationale |
|-----------|-----------|-----------|
| **Longevity** | To be determined empirically from career-length distribution | Long-serving officials are trackable and significant |
| **Seniority** | Head of department or above | Senior officials are more likely to appear in external sources |
| **Cross-colony match** | Candidate match identified in Phase 4c | The cross-colony move itself is significant |
| **External match** | Confirmed Wikidata/ODNB/VIAF match | External confirmation resolves identity |

Create `Person` persistent nodes for those meeting any criterion. Link all their `PersonRecord` slices via `SAME_AS` edges.

Everyone else remains as slice-only records — fully present in the data, queryable within their colony-year context, but without an identity claim above the slice layer.

#### Phase 4c: Cross-colony candidate matching

For each persistent `Person` node, search for plausible matches in other colonies.

Matching features (each contributes to a composite confidence score):

| Feature | Signal Strength | Logic |
|---------|----------------|-------|
| Surname match | Strong | Required for candidacy |
| Initial compatibility | Medium | Initials must be compatible (not contradictory) |
| Vacancy correspondence | Strong | Did the person leave colony A the year before appearing in colony B? |
| Career track continuity | Strong | Medical → Medical is likely; Medical → Police is extremely unlikely |
| Rank plausibility | Medium | Is the new post a lateral move or promotion? Demotions are rare |
| Honors consistency | Strong | All previously held honors must still be present |
| Qualification consistency | Strong | Qualifications are permanent — contradictions disprove a match |
| Military rank consistency | Medium | Can only increase or stay the same |
| Geographic plausibility | Weak | Some transfer patterns are more common (West Africa ↔ West Africa) |

**When a cross-colony candidate match is found:**

1. Do NOT merge. Create two separate `Person` persistent nodes (one per colony career)
2. Create a `CANDIDATE_MATCH` edge between them
3. Attach the composite confidence score and the individual feature scores as edge properties
4. Add the pair to the **Research Queue** for human review

**Output:** Persistent person nodes, within-colony career chains, cross-colony candidate matches with confidence scores, and a prioritized research queue.

### Stage 5: Narrative Processing and Vector Embedding

**Input:** Narrative sections segmented in Stage 1.

**Process:**

#### 5a: Chunking strategy

The narrative sections vary enormously in length. The Ceylon 1899 entry runs to thousands of words covering dozens of topics. A small colony might have two paragraphs.

Chunking approach:
- **Primary split:** by section heading (History, Climate, Constitution, Trade, Education, etc.)
- **Secondary split:** by paragraph within long sections, preserving paragraph boundaries
- **Minimum chunk size:** ~200 words (avoid fragments that lose context)
- **Maximum chunk size:** ~1500 words (keep within embedding model sweet spot)
- **Overlap:** include the section heading and colony-year identifier as prefix in every chunk for context

Each chunk carries metadata:
```
{
  colony: "Ceylon",
  year: 1899,
  section: "History",
  chunk_index: 2,
  source_file: "1899_manual_parsed/ceylon.txt",
  byte_offset_start: 4521,
  byte_offset_end: 6103
}
```

#### 5b: Embedding

Embed each chunk using a suitable model (e.g., `text-embedding-3-large` or an open-source equivalent for reproducibility).

Store embeddings in a vector database with the metadata above as filterable fields. This enables:
- Semantic search across the full corpus ("What do the sources say about Buddhist education?")
- Filtered search within a colony or time range ("Trade relationships in West African colonies 1900-1914")
- Colony-year scoped retrieval for RAG (attach relevant narrative to any graph query)

#### 5c: Graph linkage

Each chunk is linked to the graph:
- `NarrativeChunk -[DESCRIBES]-> TerritoryYear` (primary link)
- `NarrativeChunk -[MENTIONS]-> Territory` (when other colonies are mentioned in the text)
- `NarrativeChunk -[TOPIC]-> TopicNode` (optional: extracted topic tags)

The `MENTIONS` edges are particularly valuable — they capture the implicit cross-colony relationships in the narrative (trade partners, telegraph connections, shipping routes, shared ecclesiastical hierarchies, references to other colonial administrations).

**Output:** Vector database of embedded narrative chunks, linked to the knowledge graph via colony-year slice nodes.

### Stage 6: External Linkage

**Input:** Persistent nodes (Territory, Person, InstitutionType).

**Process:**

Automated matching against external databases. Focus effort where the return is highest.

#### Geography (high automation, high confidence):

| Database | Matching Strategy | Expected Coverage |
|----------|-------------------|-------------------|
| **Wikidata** | Colony names → Wikidata SPARQL lookup | Near-complete for territories |
| **Froman's** | Integration with existing colony knowledge graph | As available |
| **GeoNames** | For sub-territory locations (towns, districts) mentioned in personnel data | Partial |
| **World Historical Gazetteer** | Historical place-name resolution | Partial |
| **UK National Archives** | CO record series mapping (CO 54 = Ceylon, CO 267 = Sierra Leone, etc.) | Complete for major colonies |

#### Persons (selective automation, requires validation):

| Database | Matching Strategy | Expected Coverage |
|----------|-------------------|-------------------|
| **Wikidata** | SPARQL query: name + "colonial administrator" + approximate dates | Governors, senior officials |
| **ODNB** | Name + date range matching | Senior British officials |
| **VIAF** | Authority file lookup for disambiguated names | Selective |
| **WikiTree / FamilySearch** | For genealogical connections | Selective, manual |

For persons: only attempt automated matching for persistent nodes at Governor/Head of Department level. Lower-ranked matches go on the Research Queue for manual verification.

#### Institutions:

| Database | Matching Strategy | Expected Coverage |
|----------|-------------------|-------------------|
| **Wikidata** | Institutional names + colony context | Partial |
| **UK National Archives** | CO series sub-classifications | Partial |

**Output:** `EXTERNAL_LINK` edges on persistent nodes with URIs and provenance.

---

## 4. Key Design Decisions

### 4.1 Why Not Merge Prematurely

The greatest risk in historical prosopography is false identity matches. Two "J. Smith" entries in different colonies are likely different people. The graph must represent uncertainty honestly.

The design enforces this through:
- Persistent person nodes are created conservatively (earned persistence)
- Cross-colony matches produce candidate edges, not merges
- Every identity link carries provenance and confidence
- The Research Queue makes uncertain matches visible and actionable

A scholar in 2030 who discovers from archival research that two person nodes are actually the same individual can merge them. A scholar who discovers a false merge has a much harder time untangling it. **The asymmetry of error costs favors under-linking.**

### 4.2 Career Track Logic as Domain Knowledge

The probabilistic person-linking system encodes real knowledge about how the colonial service worked:

- **Professional specialization was the norm.** Medical officers trained in medicine and served in medical departments throughout their careers. Legal officers had legal training and moved through legal posts. Administrative generalists (cadets → assistant secretaries → colonial secretaries → governors) were the most mobile across tracks, but even they followed recognizable patterns.

- **Rank only increases.** An Assistant Colonial Secretary may become Colonial Secretary. The reverse does not happen except in extraordinary circumstances. A K.C.M.G. was always previously a C.M.G.

- **Honors accumulate.** If someone held C.M.G. in 1896, they still hold it in 1900. They may additionally hold K.C.M.G. New honors are added; old ones are never removed.

- **Qualifications are permanent.** M.D. does not expire. F.R.C.S. is for life. These are strong identity signals.

- **Some transfers are more common than others.** West African colonies exchanged officials frequently. Caribbean colonies formed another circuit. These patterns are statistical, not absolute, and should inform but not determine matching.

### 4.3 Handling Structural Variability

The Colonial Office List is highly regular with major exceptions. The design handles this through:

**Colony type classification:** Each territory is classified by administrative type, which determines extraction strategy:

| Type | Characteristics | Examples |
|------|----------------|----------|
| **Crown Colony** | Governor appointed by Crown, standard departmental structure | Sierra Leone, Ceylon, Hong Kong |
| **Protectorate** | Similar to Crown Colony but different legal status | Uganda, Nyasaland |
| **Settler Colony / Dominion** | Responsible government, ministers, provincial sub-structure | Canada, Cape of Good Hope, Australia |
| **Federated Territory** | Umbrella entity containing sub-territories with their own administrations | Leeward Islands, Windward Islands, pre-1914 Nigeria |
| **Mandated / Trust Territory** | Post-WWI territories administered on behalf of League/UN | Tanganyika, Togoland |
| **Miscellaneous** | Sui generis arrangements | Anglo-Egyptian Sudan, Trucial States |

Extraction and graph-building logic branches on colony type where necessary. The schema itself is uniform — the same node and edge types apply everywhere — but the *expected patterns* differ.

**Temporal variability:** A colony may change type over time (British Columbia goes from Crown Colony to Canadian province). The colony-type classification is a property of the `TerritoryYear` slice, not the persistent `Territory` node.

### 4.4 Fiscal and Numerical Data

OCR reliability on numbers is lower than on text. Revenue tables, trade statistics, and population figures are present in the narrative sections but are **deprioritized for structured extraction**.

They are still captured:
- As raw text within narrative chunks (available for RAG queries)
- As section-typed segments (labeled "statistical table" in Stage 1) that can be extracted later when a validated approach is available

The pipeline does not discard them — it defers their structured extraction.

---

## 5. Vector Database Design

### 5.1 Purpose

The narrative sections of the Colonial Office List contain extraordinarily dense contextual knowledge that resists tabular extraction. A vector database enables scholars to query this material semantically without requiring anticipation of every possible research question.

Example queries the vector store should support:
- "What was the relationship between Ceylon and the Maldive Islands?"
- "How did medical education change in West African colonies?"
- "Which colonies had telegraph connections to India?"
- "What does the Colonial Office List say about slavery abolition in different territories?"
- "How was land tenure organized in East African protectorates?"

### 5.2 Retrieval Strategy (RAG)

When a query arrives:
1. Embed the query
2. Retrieve top-k chunks from the vector store, optionally filtered by colony, year range, or section type
3. Use the chunk metadata to locate the corresponding graph nodes
4. Traverse the graph to provide structured context alongside the narrative retrieval
5. Return both: relevant text passages and their graph context (what colony, what year, what institutional structure existed, who was in post)

This is the "Graph" in GraphRAG — the vector retrieval is enriched by graph structure. A passage about medical education in Gold Coast 1920 is more useful when accompanied by the extracted Medical Department staff list from the same colony-year.

---

## 6. Open Empirical Questions

These must be answered from the data before pipeline parameters can be finalized.

### 6.1 Career Length Distribution

**Question:** How many years does a typical named individual appear in a given colony?

**Method:** For each colony, extract surname + initials across all years. Count the number of consecutive (and non-consecutive) years each name appears. Plot the distribution.

**Purpose:** Informs the longevity threshold for earned persistence. If the distribution is bimodal (many 1-2 year appearances, a second peak at 10-15 years), the threshold should sit in the valley between the modes.

### 6.2 Colony Coverage Matrix

**Question:** Which colonies appear in which years?

**Method:** Cross-tabulate year-directories against colony filenames. Identify entries, exits, name changes, and structural reorganizations.

**Purpose:** Informs Stage 0 (temporal scaffolding) and identifies colonies that change names or merge/split.

### 6.3 Department Inventory

**Question:** How many distinct department/institution types exist across the corpus?

**Method:** Extract all section headings from personnel roster sections across all files. Cluster by string similarity and manual review.

**Purpose:** Informs Stage 3 (institution normalization) and the career track taxonomy.

### 6.4 Position Title Variation

**Question:** How much do position titles vary across colonies for the same functional role?

**Method:** For each department type, extract all position titles. Cluster and examine variation.

**Purpose:** Informs Stage 3 (position normalization). Determines how aggressive normalization can be.

### 6.5 Settler Colony Structural Patterns

**Question:** How do settler colonies and federated territories differ structurally from Crown colonies?

**Method:** Sample files from each colony type. Document the structural patterns, section types, and personnel formats that differ from the standard Crown colony template.

**Purpose:** Informs colony-type branching in Stages 1 and 2.

---

## 7. Technology Recommendations

### 7.1 Graph Database

**Neo4j** is the natural choice given:
- The existing `.cypher` file in the repository suggests familiarity
- Native support for temporal queries via Cypher
- Mature ecosystem for graph data science (GDS library for community detection, similarity, pathfinding)
- APOC procedures for data import/transformation

Alternative: **Memgraph** for higher write throughput during ingestion, or **RDF/SPARQL** if deep Wikidata integration is prioritized over query ergonomics.

### 7.2 Vector Database

Options:
- **Qdrant** or **Weaviate** — purpose-built vector databases with metadata filtering
- **Neo4j Vector Index** — if keeping everything in one system is preferred (Neo4j 5.x supports native vector search)
- **pgvector** — if a relational backbone is desired alongside the graph

For a research project, keeping the vector store close to the graph (Neo4j native, or a separate store with explicit graph links) reduces integration friction.

### 7.3 LLM for Extraction

The existing codebase demonstrates Gemini 3.0 Flash for extraction with strong results (100% recall, 98% precision on test data). This is a reasonable choice for batch extraction of 2,228 files. Claude or GPT-4 class models may be used for harder cases (settler colonies, unusual formats).

Key principle: **extraction should be deterministic and reproducible.** Log the model, prompt, and version used for every extraction. Store the raw LLM output alongside the parsed result.

### 7.4 Embedding Model

For the vector database, use a model with:
- Strong performance on historical English text (the prose uses 19th/20th century vocabulary and constructions)
- Sufficient dimensionality for nuanced retrieval across a 100-year, multi-topic corpus
- Open-source availability preferred for reproducibility and long-term access

---

## 8. Implementation Sequence

The pipeline should be built incrementally, with each stage producing usable output.

### Phase I: Scaffold (Stages 0 + 1)
Build the temporal-geographic skeleton. Segment all 2,228 files. This produces no extracted data but creates the framework everything else attaches to. **Can begin immediately.**

### Phase II: Extract (Stage 2)
Begin with a well-understood subset: Crown colonies in a single decade (e.g., 1890-1900). Validate extraction quality against the existing gold standard (Sierra Leone 1896) and expand. **Depends on Stage 1.**

### Phase III: Normalize (Stage 3)
Build the institution and position type taxonomy from Phase II extractions. Expand as more decades are extracted. **Depends on Stage 2.**

### Phase IV: Link People (Stage 4)
Run within-colony career chains first. Compute the career length distribution (§6.1). Set persistence thresholds. Then run cross-colony matching. **Depends on Stages 2 and 3, and empirical analysis in §6.**

### Phase V: Embed Narratives (Stage 5)
Chunk and embed all narrative sections. Link to graph. This can proceed partly in parallel with Phases II–IV since it operates on the narrative sections, not the personnel data. **Depends on Stage 1.**

### Phase VI: External Links (Stage 6)
Run automated external matching on persistent nodes. **Depends on Stages 0 and 4.**

### Ongoing: Research Queue
The Research Queue begins accumulating in Phase IV and grows through Phase VI. It is a permanent output — a structured list of identity questions for the scholarly community.

---

## 9. What This Design Does Not Attempt

- **Full OCR correction.** The pipeline works from the manually parsed text files as they are. OCR errors are present and will propagate. The design mitigates this through probabilistic matching (which tolerates minor name variations) and provenance tracking (which allows corrections to be applied later).

- **Structured extraction of all fiscal/numerical data.** Deferred, not discarded. The narrative chunks preserve the raw text.

- **Automated resolution of all person identity questions.** The design explicitly creates a Research Queue rather than forcing resolution. Some identity questions will require archival research that no algorithm can perform.

- **Coverage of the Colonial Office itself.** The CO List records the colonial establishments, not the metropolitan side. The CO's own staff, the correspondence system, and the policy-making apparatus in London are not captured in this source. Integration with CO records at the National Archives would be a separate project linking to this graph.

- **Definitive historical claims.** The graph represents what the Colonial Office List records. The CO List is itself a bureaucratic document with its own biases, omissions, and errors. The graph should be understood as a representation of this source, not of historical reality.

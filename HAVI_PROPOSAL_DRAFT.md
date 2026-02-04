# HAVI 2026 Proposal Draft

## Administrative Information

**Title**: From Colonial Office Lists to Knowledge Graph: AI-Enabled Prosopography of British Imperial Administration, 1867-1966

**Level**: Level II ($300,000–$800,000, 1–3 years) — *or Level I if budget constraints*

**Lead Institution**: University of Saskatchewan

**PI**: [Your name]

**Co-PI (AI)**: Beatrice Alex, University of Edinburgh / Alan Turing Institute

**Collaborators**: Susan Brown (University of Guelph / LINCS)

---

## Abstract (1,000 characters max)

*Current: ~950 characters*

The Colonial Office Lists (1867-1966) document every British imperial official across 50+ colonies — an estimated 100,000 careers with positions, salaries, and institutional affiliations. This prosopographical goldmine remains locked in semi-structured text. We propose to build a replicable AI pipeline that extracts structured data from these administrative records, resolves entities across 68 years of name variations, and constructs a knowledge graph enabling research questions impossible with manual methods. Our approach combines LLM-based extraction with schema validation, probabilistic record linkage at scale, and GraphRAG for historical inquiry. The PI and Co-PI previously collaborated on Trading Consequences, which pioneered similar methods for historical text. Building on that foundation and leveraging LINCS infrastructure for Linked Open Data, we will create both a transformative research resource and a methodological template for semi-structured historical document processing.

---

## Humanities Research Question (1,000 characters max)

*Current: ~920 characters*

How did British imperial administration function as a networked system across space and time? The Colonial Office Lists enable prosopographical analysis at unprecedented scale: tracking career trajectories across colonies, mapping patronage networks through appointment patterns, analyzing salary structures by race and region, and identifying institutional evolution through departmental changes. Specific research questions include: (1) What career paths led to gubernatorial appointments, and how did these change after 1900? (2) How did the "unofficial" members of Legislative Councils relate to commercial interests? (3) What was the relationship between railway expansion and administrative infrastructure? (4) How did the transition from Crown Colony to self-governance affect staffing patterns? These questions require linking individuals across decades of records with varying name forms — currently impossible without computational methods.

---

## AI Research Question (1,000 characters max)

*Current: ~980 characters*

How can we reliably extract structured data from semi-structured historical documents at scale? The Colonial Office Lists present a distinct challenge: highly regular formatting conventions but with historical abbreviations, inconsistent OCR, and evolving schemas across 100 years. We will develop methods for: (1) LLM-based extraction with Pydantic schema validation and automatic retry on failure; (2) Section classification to route text to appropriate extraction pipelines (staff lists vs. tables vs. narrative); (3) Probabilistic entity resolution using Splink to match person records across years despite name variations and accumulating honors; (4) GraphRAG integration connecting extracted entities to embedded text passages for contextual retrieval. Our pipeline will be evaluated against manually-annotated gold standard data and designed for reproducibility on similar administrative corpora (e.g., India Office Lists, Foreign Office Lists).

---

## Narrative (8 pages max)

### 1. Problem Statement (1-1.5 pages)

#### The Corpus

The Colonial Office Lists were published annually from 1862 to 1966, documenting British imperial administration across Africa, the Caribbean, Asia, and the Pacific. Each volume contains:

- **Staff directories**: Every official from Governor to junior clerk, with position, salary, honors, and qualifications
- **Financial tables**: Revenue, expenditure, trade statistics by year
- **Institutional structure**: Departments, councils, boards with membership
- **Narrative descriptions**: Climate, geography, history, infrastructure

Our digitized corpus spans 68 years (1867-1966, with gaps), comprising:
- 2,227 text files
- 1.25 million lines of text
- ~33-48 colonies per year
- Estimated 50,000-100,000 unique individuals

#### The Research Bottleneck

Despite digitization, this data remains inaccessible for systematic research. A single colony entry (e.g., Sierra Leone 1896) contains ~150 named individuals with positions and salaries. Manual extraction is prohibitive: 150 people × 48 colonies × 68 years = ~490,000 person-position records.

Current approaches fail because:

1. **Standard NER doesn't fit**: This is semi-structured administrative text, not free prose. Pattern-based extraction is more appropriate than statistical NER.

2. **Entity resolution is critical**: "Samuel Rowe" (1881) must be linked to "Sir Saml. Rowe, K.C.M.G." (1888). Across 68 years, name variations multiply.

3. **Schema evolves**: Departments are created, colonies merge, position titles change. The extraction system must handle temporal variation.

4. **Scale requires automation**: Manual approaches cannot achieve the coverage needed for network analysis or statistical research.

#### Why Now?

Recent advances make this tractable:

- **LLM structured extraction**: Libraries like Instructor enable schema-validated JSON extraction with automatic retry
- **Probabilistic record linkage**: Splink can deduplicate millions of records in minutes
- **GraphRAG**: Knowledge graphs with vector embeddings enable new query paradigms
- **LOD infrastructure**: LINCS provides sustainable Canadian infrastructure for linked cultural data

### 2. Technical Approach (2-2.5 pages)

#### Overview

Our pipeline transforms semi-structured text into a queryable knowledge graph:

```
RAW TEXT → SECTION CLASSIFIER → EXTRACTION PIPELINES → ENTITY RESOLUTION → KNOWLEDGE GRAPH + RAG
```

#### 2.1 Section Classification

Colonial Office List entries contain distinct section types requiring different extraction strategies:

| Section Type | Example | Extraction Method |
|--------------|---------|-------------------|
| Staff lists | "Colonial Secretary, Lt.-Col. J. O. Gore, 710l. to 800l." | LLM + Pydantic schema |
| Financial tables | Revenue/Expenditure by year | Regex + LLM parsing |
| Governor lists | Name, Rank, Date tabular data | Table extraction |
| Narrative | "The climate of Sierra Leone is unhealthy..." | Chunking + embedding |

We will train a classifier to route sections to appropriate pipelines, using a modest set of manually-labeled examples (~200 sections across 10 colonies).

#### 2.2 LLM-Based Structured Extraction

For staff lists, we define Pydantic schemas:

```python
class OfficialPosition(BaseModel):
    name: str
    titles: list[str]  # Military ranks, honorifics
    honors: list[str]  # C.M.G., K.C.M.G., etc.
    position: str
    department: str
    salary_pounds: int | None
    allowances_pounds: int | None
    qualifications: list[str]  # M.D., B.A., C.E.
```

Using Instructor with GPT-4/Claude, we extract to this schema with:
- Automatic validation against constraints
- Retry with error feedback on validation failure
- Confidence scoring for human review routing

We will evaluate multiple LLMs (GPT-4, Claude, open-source alternatives) for accuracy and cost-effectiveness.

#### 2.3 Table Extraction

Financial and statistical tables require different handling:
- Detect table boundaries via formatting patterns
- Parse column structure
- Extract to normalized schema with year, colony, metric, value
- Validate against expected ranges

#### 2.4 Entity Resolution

The core challenge: matching person records across years.

**Blocking strategy**: Reduce comparison space using:
- Colony + decade
- First name + surname initial
- Department type

**Matching features** (Splink):
- Fuzzy name similarity (Jaro-Winkler)
- Honor accumulation patterns (honors only increase)
- Position trajectory plausibility
- Temporal constraints

**Training**: ~500 manually-linked person pairs across 5 colonies

**Evaluation**: Precision/recall on held-out linked pairs

#### 2.5 Knowledge Graph Construction

Target schema (extending existing territorial backbone):

**Nodes**:
- Person (name, birth_year, death_year, wikidata_id)
- Position (title, department_type)
- Department (name, colony, year_established)
- Colony (existing ~300 nodes)
- Honor (name, abbreviation, precedence)

**Relationships**:
- (Person)-[HELD_POSITION {year, salary, allowances}]->(Position)
- (Position)-[PART_OF]->(Department)
- (Department)-[PART_OF {year}]->(Colony)
- (Person)-[AWARDED {year}]->(Honor)
- (Person)-[SAME_AS]->(Person) — cross-year links

#### 2.6 GraphRAG Integration

Beyond structured extraction, narrative passages contain valuable context. We will:
- Chunk narrative sections (~500 tokens)
- Generate embeddings (OpenAI/open-source)
- Store in Neo4j vector index
- Enable hybrid queries: graph traversal + semantic retrieval

Example query: "What did colonial administrators say about public health in West African colonies?"
→ Graph identifies West African colonies and medical officers
→ Vector search retrieves relevant narrative passages
→ LLM synthesizes response grounded in sources

### 3. Environmental Scan (1 page)

#### Prior Art

**Trading Consequences** (Digging into Data II, 2012-2014): The PI and Co-PI collaborated on this project, which transformed 19th-century commodity trading documents into structured linked data. Methods included NER, relation extraction, and geo-grounding. This proposal extends that work with modern LLM-based extraction and GraphRAG.

**Clergy of the Church of England Database (CCEd)**: 130,000 clergy careers (1540-1835) extracted from administrative records. Demonstrates feasibility of large-scale prosopography from similar sources. Our approach differs in automation level and knowledge graph integration.

**Living with Machines** (Turing/British Library): Developed T-Res for toponym resolution and DeezyMatch for fuzzy string matching in historical newspapers. These tools inform our entity resolution approach.

**BiographySampo** (Finland): National biography as semantic web with GraphRAG capabilities. Demonstrates the query paradigm we aim to enable.

#### Technical Landscape

- **Instructor/Pydantic**: Mature library for LLM structured extraction (3M+ monthly downloads)
- **Splink**: Production-proven record linkage (Australian Census, German Federal Statistics)
- **Neo4j**: Industry-standard graph database with vector search
- **LINCS**: Canadian LOD infrastructure for sustainability

#### Gap We Fill

No existing project combines:
1. Semi-structured historical document extraction at this scale
2. Probabilistic entity resolution across 100 years
3. GraphRAG for historical research
4. Replicable pipeline for similar corpora

### 4. Impact (1.5 pages)

#### 4.1 Humanities Impact

**Immediate research enablement**:

- **Prosopographical analysis**: Track 100,000 careers across the British Empire
- **Network analysis**: Map patronage, professional, and institutional networks
- **Comparative colonial studies**: Systematic comparison across regions and periods
- **Economic history**: Salary structures, trade patterns, fiscal evolution

**Research questions now answerable**:

1. What career backgrounds predicted gubernatorial appointment? How did this change over time?
2. How did salary differentials between white and "coloured" officials vary by colony and period?
3. What was the relationship between railway companies and colonial administration?
4. How did institutional structures diffuse across colonies?

**Methodological contribution**: Demonstrating that semi-structured historical documents can be processed at scale, opening similar corpora (India Office Lists, Foreign Office Lists, Army Lists) to systematic research.

#### 4.2 AI Impact

**Datasets**:
- Gold-standard extraction annotations (~5,000 person-position records)
- Entity resolution training data (~2,000 linked pairs)
- Historical administrative text with structured labels

**Technical contributions**:
- Evaluation of LLM extraction on historical administrative text
- Blocking and matching strategies for historical name resolution
- GraphRAG patterns for prosopographical research

**Reproducible pipeline**: Open-source code for semi-structured document → knowledge graph transformation.

#### 4.3 Broader Impact

**Research infrastructure**: Data deposited in LINCS triple store, accessible via SPARQL and API.

**Pedagogical resource**: Corpus and tools usable for digital humanities teaching.

**Template for similar projects**: Methodology applicable to India Office Lists, Foreign Office Lists, Army Lists, colonial newspapers, and other administrative series.

### 5. Team (0.5-1 page)

**[PI Name]** (University of Saskatchewan) — *Humanities Lead*
- Domain expertise in [your area]
- Prior collaboration with Co-PI on Trading Consequences
- Experience with historical data modeling

**Beatrice Alex** (University of Edinburgh / Alan Turing Institute) — *AI Lead*
- Chancellor's Fellow, Edinburgh Futures Institute
- Turing Fellow, Alan Turing Institute
- Led text mining on Trading Consequences
- Developer of Edinburgh Geoparser
- Expertise: historical NLP, entity extraction, geoparsing

**Susan Brown** (University of Guelph) — *Collaborator, LOD Infrastructure*
- Canada Research Chair in Collaborative Digital Scholarship
- Director, LINCS and CWRC
- Roberto Busa Prize 2024
- Expertise: linked open data, ontology design, digital humanities infrastructure

**LINCS Team** — *Infrastructure Support*
- Conversion toolkit for LOD transformation
- National triple store hosting
- Sustainability beyond grant period

#### Team Justification

This team combines:
- **Proven collaboration**: PI and Co-PI worked together on Trading Consequences
- **Complementary expertise**: Historical research + NLP/extraction + LOD infrastructure
- **Institutional strength**: Saskatchewan + Edinburgh/Turing + Guelph/LINCS
- **International scope**: Canada-UK collaboration

### 6. Dissemination (0.5 page)

**Code and data**:
- GitHub repository with extraction pipeline (MIT license)
- Gold-standard annotations deposited in Zenodo
- Knowledge graph accessible via LINCS SPARQL endpoint

**Publications**:
- Methods paper targeting Journal of Cultural Analytics or Digital Scholarship in the Humanities
- Historical research paper(s) demonstrating corpus value
- Dataset paper in Journal of Open Humanities Data

**Presentations**:
- DH2027 (if timeline permits)
- Computational Humanities Research (CHR)
- NLP4DH workshop

**Community engagement**:
- Tutorial at DH Summer Institute or similar
- Blog posts documenting methodology
- Collaboration with related projects (e.g., India Office List digitization)

---

## Timeline (Summary)

| Phase | Months | Activities |
|-------|--------|------------|
| **1. Setup & Pilot** | 1-6 | Finalize schema, annotate gold standard, pilot extraction on 1896 data |
| **2. Extraction Pipeline** | 7-18 | Process full corpus, refine classifiers, evaluate accuracy |
| **3. Entity Resolution** | 12-24 | Train Splink model, cluster persons, manual review |
| **4. Graph & RAG** | 18-30 | Build knowledge graph, integrate embeddings, query interface |
| **5. Research & Dissemination** | 24-36 | Historical analysis, publications, sustainability handoff to LINCS |

*Note: Phases overlap; entity resolution development parallels extraction work.*

---

## Budget Notes (to be developed)

**Level II target**: $500,000-$600,000 over 3 years

| Category | Estimate | Notes |
|----------|----------|-------|
| PI salary/buyout | TBD | Course release or summer salary |
| Co-PI salary | TBD | Edinburgh rates |
| Postdoc/RA | ~$150,000 | 1 FTE for 2 years, based at Edinburgh or Saskatchewan |
| LLM API costs | ~$30,000 | GPT-4/Claude for extraction |
| Computing | ~$20,000 | Or use Schmidt Sciences allocation |
| Travel | ~$15,000 | Team meetings, conferences |
| LINCS contribution | TBD | In-kind or direct support |
| Indirect | 10% cap | Per RFP |

---

## Appendices (to be prepared)

- [ ] Sample extraction: Sierra Leone 1896 staff list → JSON
- [ ] Schema diagrams
- [ ] Corpus statistics table
- [ ] Timeline Gantt chart


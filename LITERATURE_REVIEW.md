# Literature Review: Tools and Approaches for Colonial Office List Extraction

## Executive Summary

The Colonial Office Lists present a **semi-structured document extraction** problem, not an NER problem. The data is highly regular (positions, salaries, hierarchies) but requires understanding document layout and handling cross-document entity resolution. This review focuses on enterprise-grade and scholarly tools that address these specific challenges.

---

## Part 1: Document AI and Intelligent Document Processing (IDP)

### The Problem Space

The Colonial Office Lists are **semi-structured administrative documents** with:
- Repeating hierarchical patterns (Department → Position → Person → Salary)
- Tables (financial data, trade statistics, governors lists)
- Consistent formatting conventions (abbreviations, honors, currency)
- Cross-references between sections and years

This is NOT a free-text NER problem. Standard NER tools expect unstructured prose. Instead, we need **pattern-based extraction** from structured layouts.

### Enterprise IDP Platforms

Modern Intelligent Document Processing combines OCR, layout analysis, and LLM reasoning:

| Platform | Strength | Relevance |
|----------|----------|-----------|
| [UiPath Document Understanding](https://www.uipath.com/blog/ai/improved-document-processing) | Proprietary DocPath LLMs, human-in-the-loop | High for production scale |
| [Microsoft Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/choosing-right-ai-tool) | Layout-aware OCR, table extraction | High for Azure integration |
| [AWS Amazon Textract](https://aws.amazon.com/ai/generative-ai/use-cases/document-processing/) | Forms, tables, key-value pairs | Good for AWS shops |
| [Google Document AI](https://cloud.google.com/document-ai) | Custom processors, Layout Parser | Good for GCP integration |
| [ABBYY Vantage](https://www.abbyy.com/vantage/) | Multi-format, NLP + structure analysis | Established enterprise tool |
| [H2O Document AI](https://h2o.ai/platform/ai-cloud/make/document-ai/) | ML-driven, cross-format | Open-source friendly |

**Key insight**: These platforms are designed for **invoices, forms, contracts**—documents with similar structure to Colonial Office Lists. The challenge is adapting them to historical conventions.

### Recommended Approach: Hybrid Rule + Model

> "Rule-based data extraction targets structured documents, while model-based data extraction is used for semi-structured and unstructured documents... We want users to be able to easily combine different approaches."
> — [UiPath](https://www.uipath.com/blog/ai/improved-document-processing)

For Colonial Office Lists:
1. **Rules/Templates** for predictable sections (salary tables, governor lists)
2. **LLM-based extraction** for narrative sections and edge cases
3. **Human-in-the-loop** for validation and training data creation

---

## Part 2: Wrapper Induction and Pattern-Based Extraction

### Classical Approach: STALKER Algorithm

The [STALKER algorithm](https://link.springer.com/article/10.1023/A:1010022931168) introduced **hierarchical wrapper induction** specifically for semi-structured documents:

> "The novel approach is based on hierarchical information extraction, which turns the hard problem of extracting data from an arbitrarily complex document into a series of simpler extraction tasks."

Key features:
- Learns extraction rules from labeled examples
- Handles **nested/hierarchical data** (Department → Position → Person)
- Works with variable ordering and missing items
- Requires **far fewer training examples** than other approaches

**Directly applicable**: Colonial Office Lists have a clear hierarchical structure (Colony → Department → Position → Person with attributes).

### Record-Level Extraction

Research on [record-level wrapper induction](https://dl.acm.org/doi/10.1145/1645953.1645962) addresses exactly our problem:

> "The task of extracting records from web pages... wrapper induction is one of the most popular methods and is extensively used by many commercial information systems."

The [IEPAD algorithm](https://www.semanticscholar.org/paper/IEPAD:-information-extraction-based-on-pattern-Chang-Lui/c22e82083b78e4022d5b9d2cd4c2a2f42f73151a) uses pattern discovery to generate extraction rules **without labeled examples**:
- Builds a pattern-tree of hierarchical relationships
- Discovers repeating structures automatically
- Particularly effective for list-like data

---

## Part 3: LLM-Based Structured Extraction

### The 2024-2025 Revolution

> "Structured data extraction is a killer app for LLMs... The single most commercially valuable application of LLMs is turning unstructured content into structured data."
> — [Simon Willison](https://simonw.substack.com/p/structured-data-extraction-from-unstructured)

Modern LLMs with **structured output modes** can extract to JSON schemas:

### Key Libraries

| Library | Description | Link |
|---------|-------------|------|
| **Instructor** | Most popular Python library for LLM structured extraction; Pydantic-based validation, retries, streaming | [python.useinstructor.com](https://python.useinstructor.com/) |
| **Outlines** | Grammar-constrained generation; guarantees valid JSON/Pydantic output | [GitHub](https://github.com/outlines-dev/outlines) |
| **Formatron** | Efficient constrained decoding; f-string templates | [GitHub](https://github.com/Dan-wanna-M/formatron) |
| **LangChain** | Pydantic structured outputs via `with_structured_output()` | [LangChain Docs](https://python.langchain.com/docs/how_to/structured_output/) |

### Instructor Example for Colonial Data

```python
from pydantic import BaseModel
from instructor import patch
import openai

class OfficialPosition(BaseModel):
    name: str
    title: str
    honors: list[str]
    salary_pounds: int
    allowances_pounds: int | None
    qualifications: list[str]

class Department(BaseModel):
    name: str
    positions: list[OfficialPosition]

# Patch OpenAI client
client = patch(openai.OpenAI())

# Extract structured data
result = client.chat.completions.create(
    model="gpt-4",
    response_model=Department,
    messages=[{"role": "user", "content": raw_text}]
)
```

### Validation and Self-Correction

[Pydantic validators can minimize LLM hallucinations](https://pydantic.dev/articles/llm-validation):

> "Instructor leverages Pydantic's validation framework to provide a uniform developer experience for both code-based and LLM-based validation, as well as a reasking mechanism for correcting LLM outputs based on validation errors."

This is critical for Colonial Office Lists where:
- Salary values must be numeric
- Years must be in valid ranges (1800-1966)
- Honors (C.M.G., K.C.M.G.) must be from a known set

---

## Part 4: Table Extraction

### The Challenge

Colonial Office Lists contain extensive tabular data:
- Financial statistics (Revenue, Expenditure, Tonnage)
- Trade tables (Imports/Exports by origin/destination)
- Population tables (by year, sex, race)
- Governor succession lists

### Deep Learning Models

| Model | Source | Capability |
|-------|--------|------------|
| [Microsoft Table Transformer (TATR)](https://github.com/microsoft/table-transformer) | Microsoft Research | DETR-based detection from images; PubTables-1M dataset |
| [TableFormer](https://arxiv.org/abs/2203.01017) | IBM Research | Transformer-based structure recognition; 98.5% TEDS on simple tables |
| [DocTR](https://github.com/mindee/doctr) | Mindee | Open-source OCR with layout detection; PyTorch ecosystem |

### For Pre-OCR'd Text

Since your Colonial Office Lists are already parsed to text, you may not need image-based table extraction. Instead:

1. **Regex patterns** for detecting table boundaries
2. **LLM parsing** of tabular text into structured data
3. **Pandas** for validation and normalization

---

## Part 5: Record Linkage and Entity Resolution

### The Core Problem

> "Is 'Samuel Rowe' in 1881 the same as 'Sir Saml. Rowe, K.C.M.G.' in 1888?"

This is **entity resolution at scale**: 50,000-100,000 unique individuals across 68 years with name variations, accumulating honors, and career transitions.

### Production-Ready Tools

#### Splink (UK Ministry of Justice)

[Splink](https://github.com/moj-analytical-services/splink) is the leading open-source probabilistic record linkage tool:

> "Splink is capable of linking a million records on a laptop in approximately one minute... the fastest free tool for accurately deduplicating large datasets."

Notable users:
- **Australian Bureau of Statistics**: 2024 National Linkage Spine
- **German Federal Statistical Office**: Register-based census linking
- **US Defense Health Agency**: 200 million hospital records

**Highly recommended** for Colonial Office List person matching.

#### Dedupe.io

[Dedupe](https://github.com/dedupeio/dedupe) uses machine learning for fuzzy matching:

> "Dedupe takes in human training data and comes up with the best rules for your dataset to quickly and automatically find similar records."

Based on Mikhail Bilenko's PhD research on learnable similarity functions.

### Blocking Strategies for Colonial Data

Efficient record linkage requires **blocking** to avoid O(n²) comparisons:

| Blocking Key | Example |
|--------------|---------|
| Colony + Year range | "Sierra Leone, 1890-1900" |
| First name + Surname initial | "Samuel R*" |
| Department type | "Medical Department" |
| Honor pattern | "*C.M.G.*" |

---

## Part 6: Linked Open Data and Ontologies

### CIDOC-CRM for Cultural Heritage

[CIDOC-CRM](https://cidoc-crm.org/) is the ISO standard (ISO 21127) for cultural heritage data:

> "CIDOC CRM can help researchers explore complex questions with regards to our past across diverse and dispersed datasets by providing definitions and a formal structure."

### Bio CRM for Prosopography

[Bio CRM](https://ceur-ws.org/Vol-2119/paper10.pdf) extends CIDOC-CRM for biographical data:

> "Bio CRM provides a semantic data model for harmonizing and interlinking heterogeneous data from different biographical data sources. The model includes structures for basic data of people, personal relations, professions, and events."

Key modeling distinctions:
- **Enduring unary roles** (being a Governor)
- **Enduring binary relationships** (employed by Colony)
- **Perduring events** (appointment, death, transfer)

### BiographySampo (Finland)

[Semantic National Biography of Finland](https://seco.cs.aalto.fi/projects/biographies/) demonstrates GraphRAG for prosopography:

> "BiographySampo aims to make a paradigm shift in publishing biographical dictionaries on the web and includes versatile tooling for biographical research."

### SNAP: Standards for Networking Ancient Prosopographies

[SNAP:DRGN](https://snapdrgn.net/) provides interchange standards for person data:

> "SNAP is building a virtual authority list for ancient people through Linked Data collection from many collaborating projects."

While focused on ancient history, their [ontology](https://snapdrgn.net/ontology.html) and [cookbook](https://snapdrgn.net/cookbook.html) are directly applicable.

---

## Part 7: Existing Prosopographical Projects

### Clergy of the Church of England Database (CCEd)

[CCEd](https://theclergydatabase.org.uk/) (1540-1835) is structurally similar to Colonial Office Lists:

> "The database contains the key career events for over 130,000 individual clerics... Rather than containing prose biographies, the database records information about clerical careers in interlinked tables."

**Data model elements**:
- Person records with biographical data
- Position records (curacies, livings, preferments)
- Institution records (parishes, dioceses)
- Temporal links (ordination dates, appointments)

**Directly applicable patterns** for Colonial Office official careers.

### Dictionary of Canadian Biography (DCB)

[DCB](https://www.biographi.ca/) has 9,000+ biographies with structured metadata:

> "The volumes are arranged according to death dates of subjects... indexes by occupation and geography."

Your cypher file already references `dcb_id` for person linking.

### People of Medieval Scotland

Database of 21,000+ individuals from Scottish medieval records—similar administrative source material.

---

## Part 8: Data Cleaning and Reconciliation

### OpenRefine

[OpenRefine](https://openrefine.org/) excels at semi-automated entity matching:

> "Reconciliation is the process of matching your dataset with that of an external source... OpenRefine's Reconciliation service is used to semi-automate the process."

Key features:
- [Wikidata reconciliation](https://wikidata.reconci.link/) for places, people
- Fuzzy string matching with manual review
- Clustering for variant detection
- GREL expressions for transformation

### Workflow for Colonial Data

1. Extract raw person-position records
2. Cluster on name variants in OpenRefine
3. Reconcile against Wikidata for known individuals
4. Export reconciled data with QIDs
5. Load to Neo4j with external links

---

## Part 9: Neo4j Knowledge Graph Construction

### LLM Graph Builder

[Neo4j LLM Knowledge Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/) automates extraction:

> "The extraction turns [documents] into a lexical graph of documents and chunks (with embeddings) and an entity graph with nodes and their relationships."

### Pipeline Components

From [Neo4j GraphRAG Python](https://neo4j.com/docs/neo4j-graphrag-python/current/user_guide_kg_builder.html):

1. **Data loader**: Extract text from files
2. **Text splitter**: Chunk by section/department
3. **Schema builder**: Define node/relationship types
4. **Entity extractor**: LLM-based extraction
5. **Graph pruner**: Clean based on schema
6. **Entity resolver**: Merge duplicate nodes

### Schema-Grounded Extraction

> "Provide a schema to ground LLM extracted node and relationship types—can be provided manually or extracted automatically using LLMs."

For Colonial Office Lists, **manual schema definition** is essential:
- Node types: Person, Position, Department, Colony, Year, Honor, Qualification
- Relationship types: HELD_POSITION, PART_OF, AWARDED, QUALIFIED_AS

---

## Part 10: Annotation and Training Workflows

### Prodigy + spaCy

[Prodigy](https://prodi.gy/) enables rapid annotation with active learning:

> "Prodigy is an annotation tool so efficient that data scientists can do the annotation themselves."

For custom entity types in Colonial Office Lists:
- **ner.correct**: Use existing model, correct mistakes
- **ner.manual**: Fully manual annotation for new entity types
- **Active learning**: Model suggests most informative examples

### Annotation Strategy

1. Start with **rules/patterns** for high-confidence extractions
2. Use **LLM zero-shot** for moderate-confidence
3. **Prodigy annotation** for edge cases and training data
4. Train **spaCy model** for production deployment

---

## Part 11: Historical Document Processing

### Transkribus

[Transkribus](https://www.transkribus.org/) is the standard for historical text recognition:

> "Handwritten Text Recognition (HTR) technology is now a mature machine learning tool, becoming integrated in the digitisation processes of libraries and archives."

While your Colonial Office Lists are already OCR'd, Transkribus offers:
- **Field Models**: Custom layout recognition for registers, forms
- **Table Models**: Structured extraction from tabular layouts
- Over 140 public AI models for various scripts/languages

---

## Part 12: Recommended Technology Stack

### For Colonial Office List Extraction

| Layer | Recommended Tool | Alternative |
|-------|------------------|-------------|
| **Schema Definition** | Pydantic models | JSON Schema |
| **LLM Extraction** | Instructor + GPT-4/Claude | LangChain structured output |
| **Table Parsing** | Custom regex + LLM | TableFormer |
| **Entity Resolution** | Splink | Dedupe.io |
| **Data Cleaning** | OpenRefine | Pandas |
| **Reconciliation** | Wikidata via OpenRefine | Manual matching |
| **Graph Database** | Neo4j | — |
| **Ontology** | Bio CRM / CIDOC-CRM | Custom |
| **Annotation** | Prodigy | Label Studio |
| **Vector Search** | Neo4j + embeddings | Pinecone |

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     RAW TEXT FILES                              │
│                  (68 years × ~48 colonies)                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   SECTION CLASSIFIER                            │
│     (Identify: Staff list, Financial table, Narrative, etc.)   │
└─────────────────────────────────────────────────────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            ▼                 ▼                 ▼
    ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
    │ STAFF LISTS   │ │ TABLES        │ │ NARRATIVE     │
    │               │ │               │ │               │
    │ Pattern-based │ │ Regex + LLM   │ │ LLM chunking  │
    │ + LLM         │ │ parsing       │ │ + embeddings  │
    │ (Instructor)  │ │               │ │               │
    └───────────────┘ └───────────────┘ └───────────────┘
            │                 │                 │
            └─────────────────┼─────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ENTITY RESOLUTION                             │
│                (Splink / Dedupe.io)                             │
│     Match persons across years, handle name variations          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   RECONCILIATION                                │
│             (OpenRefine + Wikidata)                             │
│     Link to external identifiers (QIDs, GeoNames, DCB)          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   NEO4J KNOWLEDGE GRAPH                         │
│     Nodes: Person, Position, Department, Colony, Event          │
│     + Vector embeddings for narrative passages                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Part 13: Key Papers and Resources

### Must-Read Papers

1. **Hierarchical Wrapper Induction** - [Muslea, Minton, Knoblock (2001)](https://link.springer.com/article/10.1023/A:1010022931168)
2. **Bio CRM for Prosopography** - [Tuominen & Hyvönen (2018)](https://ceur-ws.org/Vol-2119/paper10.pdf)
3. **Knowledge Base Population** - [Ji & Grishman (2011)](https://www.researchgate.net/publication/220873715_Knowledge_Base_Population_Successful_Approaches_and_Challenges)
4. **Splink: Probabilistic Linking at Scale** - [UK MoJ](https://moj-analytical-services.github.io/splink/)
5. **Structured Outputs from LLMs** - [Multiple authors (2024)](https://mbrenndoerfer.com/writing/structured-outputs-schema-validated-data-extraction-language-models)

### Tool Documentation

- [Instructor Documentation](https://python.useinstructor.com/)
- [Splink Documentation](https://moj-analytical-services.github.io/splink/index.html)
- [OpenRefine Reconciliation](https://openrefine.org/docs/manual/reconciling)
- [Neo4j GraphRAG Python](https://neo4j.com/docs/neo4j-graphrag-python/current/user_guide_kg_builder.html)
- [CIDOC-CRM](https://cidoc-crm.org/)
- [SNAP Cookbook](https://snapdrgn.net/cookbook.html)

### Similar Projects

- [Clergy of the Church of England Database](https://theclergydatabase.org.uk/)
- [Dictionary of Canadian Biography](https://www.biographi.ca/)
- [BiographySampo (Finland)](https://seco.cs.aalto.fi/projects/biographies/)
- [SNAP:DRGN](https://snapdrgn.net/)

---

## Part 14: Recommended Next Steps

### Phase 1: Pilot Extraction (1-2 weeks)

1. **Define Pydantic schema** for person-position records
2. **Test Instructor** on 5 colony files from 1896
3. **Evaluate extraction accuracy** manually
4. **Identify failure modes** and edge cases

### Phase 2: Entity Resolution (2-3 weeks)

1. **Export extracted persons** to CSV
2. **Configure Splink** for name matching
3. **Train on manually-linked examples** (100-200 pairs)
4. **Run clustering** across all 1896 data
5. **Evaluate precision/recall**

### Phase 3: Scale and Reconciliation (2-4 weeks)

1. **Process all 68 years** with refined pipeline
2. **Reconcile with Wikidata** via OpenRefine
3. **Link to existing graph** (DCB IDs, GeoNames)
4. **Load to Neo4j**

### Phase 4: GraphRAG (ongoing)

1. **Add passage embeddings** for narrative sections
2. **Build query interface**
3. **Evaluate on research questions**

---

## Conclusion

The Colonial Office List extraction problem is **well-suited to modern tools**:

- **Semi-structured data** → Pattern-based + LLM hybrid extraction
- **Entity resolution at scale** → Splink (proven on 200M+ records)
- **Linked Data** → Bio CRM ontology + Wikidata reconciliation
- **GraphRAG** → Neo4j with vector embeddings

The CCEd (130,000 clergy, 1540-1835) demonstrates this is achievable for similar administrative records. The key is combining:

1. **Explicit schemas** (not free-form NER)
2. **LLM extraction with validation** (Instructor + Pydantic)
3. **Probabilistic record linkage** (Splink)
4. **Semantic grounding** (Wikidata, GeoNames, DCB)

---

*Literature review prepared for HIST 496: Text as Data*
*February 2026*

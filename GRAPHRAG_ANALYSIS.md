# Colonial Office List Knowledge Graph: Potential and Challenges

## Executive Summary

This corpus represents **100 years of British imperial administration** (1867-1966) with extraordinary potential for historical research—and equally extraordinary challenges for computational extraction.

**Current Status**: Territorial backbone complete; prosopographical data awaits extraction.

---

## Corpus Statistics

| Metric | Value |
|--------|-------|
| Years covered | 68 (1867-1966, with gaps) |
| Text files | 2,227 |
| Total lines | 1,254,448 |
| Total size | 184 MB |
| Colonies per year | ~33-48 |
| Estimated named individuals | 50,000-100,000+ unique |

---

## Current Knowledge Graph (`britishempire_clean.cypher`)

The existing cypher file provides the **territorial scaffold**:

### Node Types
- **Colony** (~300+ entries): Temporal territories with start/end dates
- **Region** (21): Geographic groupings (West Africa, Caribbean, etc.)
- **Place** (~54): GeoNames-linked locations with coordinates
- **State**: Post-independence nations
- **Empire**: Top-level container

### Relationship Types
| Relationship | Count | Description |
|--------------|-------|-------------|
| `SUCCESSOR_TO` | 9 | Independence transitions |
| `PART_OF` | 9 | Hierarchical containment |
| `EVOLVED_INTO` | 7 | Administrative changes |
| `IN_REGION` | 1 | Geographic grouping |
| `FEDERATED_INTO` | - | Union formations |
| `PARTITIONED_INTO` | 1 | Territory divisions |
| `BORDERS_WITH` | 3 | Geographic adjacency |

### Colony Type Taxonomy (50+ types)
```
Crown Colony (89), Independence (35), Protectorate (33),
Guano Island (14), Province (12), Dependency (10),
Trading Post (9), Mandate (8), Royal Colony (7),
Dominion (7), Presidency (6), Whaling Station (5)...
```

### What's Missing
The cypher file contains **territorial structure** but NOT:
- Named officials (Governors, Colonial Secretaries, Clerks)
- Positions and departments
- Salaries and allowances
- Institutional hierarchies
- Economic statistics
- Narrative descriptions

---

## Extractable Data Types from Colonial Office Lists

### 1. Prosopographical (People)

**Example from Sierra Leone 1896:**
```
Governor, Commander-in-Chief; and Vice-Admiral,
Colonel F. Cardew, C.M.G., 2,000l. and 500l. allowances.
```

**Extractable fields:**
- Name (Colonel F. Cardew)
- Titles/Honors (C.M.G.)
- Military rank (Colonel)
- Position(s) (Governor, Commander-in-Chief, Vice-Admiral)
- Salary (2,000l.)
- Allowances (500l.)
- Qualifications (M.D., M.R.C.S., B.L., B.A., C.E.)

**Scale challenge**: ~150 people per colony per year × 48 colonies × 68 years = **~490,000 person-position records**

---

### 2. Organizational (Institutions)

**Departments found in Sierra Leone 1896:**
- Executive Council
- Legislative Council
- Colonial Secretary's Department
- Treasury Department
- Customs Department
- Post Office Department
- Medical Department
- Police Department
- Prison Department
- Education Department
- Surveyor's Department
- Audit Department
- Native Affairs Department
- Printing Department
- Ecclesiastical Department

**Relationships:**
```
(Person)-[HELD_POSITION {salary, year}]->(Position)
(Position)-[PART_OF]->(Department)
(Department)-[PART_OF]->(Colony)
```

---

### 3. Economic (Quantitative Data)

**Time series tables (Sierra Leone 1896):**
```
| Year | Revenue | Expenditure | British Tonnage | Total Tonnage |
|------|---------|-------------|-----------------|---------------|
| 1885 | 64,751  | 67,917      | 379,465         | 434,163       |
...
| 1894 | 98,838  | 98,100      | 828,718         | 962,046       |
```

**Trade flows:**
```
| Year | From U.K. | From Colonies | From Elsewhere | Total |
|------|-----------|---------------|----------------|-------|
| 1894 | 381,248   | 11,012        | 85,764         | 478,024|
```

**Products:** Palm oil, kernels, boni seed, ground nuts, cola nuts, rubber, copal, hides, ginger (exports); spirits, tobacco, cotton goods, furniture, hardware (imports)

---

### 4. Temporal (Events and Transitions)

**Charter/Treaty dates:**
- 1787: Peninsula ceded by native chiefs
- 1807: Colony transferred to Crown (slave trade abolition)
- 1821: West Africa Settlements unified
- 1843: Gambia separated
- 1862: Sherbro annexed
- 1866: Central Government established
- 1874: Gold Coast separated
- 1888: Gambia re-separated

**Governor succession tables:**
```
| Name | Rank | Assumed Government |
|------|------|--------------------|
| A. E. Kennedy | Govr.-in-Chief | 12 Oct., 1852 |
| S. J. Hill | Govr.-in-Chief | 18 Sept., 1855 |
...
```

---

### 5. Geographic (Spatial Data)

**Explicit coordinates:**
```
Cape lies in 8° 30' N. lat., 13° 18' W. long.
```

**Measurements:**
```
Peninsula is 26 miles in length by 12 in breadth
Area of 300 square miles (4,000 sq mi total colony)
```

**Named places:**
- Islands: Sherbro, Isles de Los, Banana, Turtle, Leopard, Plantain
- Rivers: Sierra Leone, Mannah, Skarcius, Sherbro, Roquelle
- Towns: Freetown (80,033 pop.), Waterloo, Bonton

---

### 6. Infrastructure Networks

**Shipping routes:**
```
Liverpool → Madeira: 7 days (every Saturday + every 2nd Wednesday)
Madeira → Freetown: 8-9 days
Also: Hamburg, Havre, Marseilles, Lisbon, Algiers
```

**Telegraph cables:**
```
Freetown → Bathurst (direct)
Freetown → Conakry (direct)
Freetown → Accra (direct)
Established: 1886
```

**Rivers as transport:**
```
Sherbro River: navigable 20 miles (to Yorktown)
Sierra Leone River: navigable 40 miles (to Magbellie)
```

---

### 7. Qualitative Assessments (Colonial Knowledge)

**Climate evaluations:**
```
"The climate of Sierra Leone is unhealthy, especially for Europeans."
"The beginning and ending of the wet season are the most sickly periods."
```

**Comparative statements:**
```
"possesses the best harbour in West Africa"
"a little over half the size of Wales"
"The inhabitants are born traders"
```

These encode **colonial knowledge production**—subjective but historically significant.

---

## GraphRAG Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                     KNOWLEDGE GRAPH LAYER                      │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │ Person  │───▶│Position │───▶│  Dept   │───▶│ Colony  │     │
│  │         │    │{salary} │    │         │    │{dates}  │     │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘     │
│       │              │              │              │           │
│       ▼              ▼              ▼              ▼           │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │  Honor  │    │  Event  │    │ Product │    │ Region  │     │
│  │ (C.M.G.)│    │{date}   │    │{trade}  │    │         │     │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘     │
└────────────────────────────────────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ PASSAGE INDEX   │ │ VECTOR STORE    │ │ EXTERNAL LINKS  │
│                 │ │                 │ │                 │
│ "The climate of │ │ Embeddings for  │ │ Wikidata QIDs   │
│ Sierra Leone is │ │ semantic search │ │ GeoNames IDs    │
│ unhealthy..."   │ │                 │ │ DCB IDs         │
│                 │ │                 │ │                 │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

---

## Query Types Enabled by GraphRAG

### Factual Queries (Graph Traversal)
```cypher
// Who governed Sierra Leone in 1888?
MATCH (p:Person)-[h:HELD_POSITION]->(pos:Position {title: 'Governor'})
      -[:IN]->(c:Colony {name: 'Sierra Leone'})
WHERE h.year = 1888
RETURN p.name, h.start_date
```

### Comparative Queries (Multi-Colony)
```cypher
// How did Governor salaries compare across West African colonies in 1896?
MATCH (p:Person)-[h:HELD_POSITION {year: 1896}]->(pos:Position {title: 'Governor'})
      -[:IN]->(c:Colony)-[:IN_REGION]->(r:Region {name: 'West Africa'})
RETURN c.name, p.name, h.salary ORDER BY h.salary DESC
```

### Career Tracking (Prosopographical)
```cypher
// Track Sir Samuel Rowe's career across colonies
MATCH (p:Person {name: 'Samuel Rowe'})-[h:HELD_POSITION]->(pos)-[:IN]->(c:Colony)
RETURN c.name, pos.title, h.start_date ORDER BY h.start_date
```

### Semantic Queries (Vector Search + Graph)
```
"What did colonial officials say about tropical climates and European health?"
→ Vector search finds relevant passages
→ Graph grounds them in specific colonies and time periods
→ LLM synthesizes comparative analysis
```

### Network Queries (Infrastructure)
```cypher
// Fastest route from London to Lagos in 1896
MATCH path = shortestPath(
  (london:Place {name: 'London'})-[:SHIP_ROUTE|TELEGRAPH*]-(lagos:Colony {name: 'Lagos'})
)
RETURN path, reduce(t = 0, r in relationships(path) | t + r.travel_days)
```

---

## Scale Challenges (Teaching Points)

### 1. Entity Resolution
```
"Samuel Rowe" = "Sir Saml. Rowe" = "Sir Samuel Rowe, K.C.M.G." ?
```
- Same person, different name forms across years
- Accumulating honors (C.M.G. → K.C.M.G.)
- Abbreviations ("ditto", "do.", "Govr.")

### 2. Schema Evolution
- Departments created/abolished over time
- Colony boundaries change (mergers, partitions)
- Position titles evolve ("Govr.-in-Chief" → "Governor")

### 3. OCR Quality
- 100+ years of documents with varying print quality
- Tables with complex alignment
- Mixed fonts (italic for names, different sizes)

### 4. Coreference Resolution
```
"The Colony" → which colony?
"ditto" → same as previous entry
"the same" → same year/amount?
```

### 5. Implicit Knowledge
- "l." = pounds sterling
- "C.M.G." = Companion of the Order of St Michael and St George
- Geographic comparisons assume reader knows size of Wales

### 6. Cross-Document References
```
"For Governors previous to 1850, see Edition for 1893"
"see under Gold Coast"
```
Documents form an intertextual network.

---

## Estimated Extraction Effort

| Data Type | Complexity | Estimated Records |
|-----------|------------|-------------------|
| Person names | Medium | 50,000-100,000 |
| Position assignments | High | 500,000+ |
| Salary figures | Medium | 300,000+ |
| Departments | Low | 2,000-3,000 |
| Economic time series | Medium | 50,000+ data points |
| Geographic entities | Low | 5,000-10,000 |
| Events/dates | High | 100,000+ |
| Narrative passages | Low (chunking) | 50,000+ |

---

## Comparison: Current State vs. Potential

| Aspect | Current Cypher | Full Extraction |
|--------|----------------|-----------------|
| Colonies | ~300 | ~300 (complete) |
| Regions | 21 | 21 (complete) |
| People | 0 | 50,000-100,000 |
| Positions | 0 | 10,000-20,000 |
| Position-Holds | 0 | 500,000+ |
| Departments | 0 | 2,000-3,000 |
| Economic Data | 0 | 50,000+ rows |
| Events | 0 | 100,000+ |
| Passages (RAG) | 0 | 50,000+ |

The territorial scaffold is **<1%** of the potential knowledge graph.

---

## Recommended Next Steps

1. **Schema Design**: Finalize node/relationship types for prosopographical data
2. **Pilot Extraction**: Manual + semi-automated extraction for 1 colony × 5 years
3. **NER Training**: Train named entity recognizer on colonial administrative text
4. **Evaluation**: Measure precision/recall on pilot data
5. **Scale**: Apply to full corpus with human-in-the-loop correction
6. **RAG Integration**: Add passage embeddings and retrieval layer
7. **Query Interface**: Build research query tools for historians

---

## Value Proposition

**For Imperial History**: Track careers, networks, and institutional evolution across the entire British Empire over 100 years.

**For Prosopography**: Identify ~100,000 individuals with positions, salaries, and career trajectories.

**For Digital Humanities**: Demonstrate GraphRAG on a challenging historical corpus with rich metadata.

**For Data Science Education**: Perfect case study of "huge potential, significant challenges" at scale.

---

*Analysis prepared for HIST 496: Text as Data*
*Jo Guldi, University of Saskatchewan*
*February 2026*

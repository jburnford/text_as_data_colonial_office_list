# Plan: Neo4j Stage 1 — Load PersonRecords into Knowledge Graph

## Context

We have 239+ colony-year extractions (32,400+ officials, growing hourly) from the Colonial Office List corpus. The Neo4j Stage 0 scaffold is loaded (68 Year nodes, 133 Territory nodes, 2,220 TerritoryYear slices). We now need to load extracted personnel data as Stage 1, creating the foundation of a knowledge graph designed for a decade of scholarship.

**Key design decisions (confirmed with user):**
- **Hybrid schema**: Property graph core (persistent + slice nodes) with event nodes for career transitions. Natively queryable in Cypher, CIDOC-CRM-exportable via neosemantics (n10s) later.
- **Scope**: Stage 1 only — PersonRecord nodes linked to TerritoryYear. No normalization (Stage 3) or person linking (Stage 4) yet. But the schema must accommodate future stages.

**LOD principles guiding the schema:**
- Provenance on all edges (method, confidence, pipeline_version, date_created)
- URI scheme for all entities (stable, resolvable)
- Preserve raw source data alongside any normalization
- Model uncertainty explicitly (confidence scores, not forced merges)
- CIDOC-CRM alignment: PersonRecord ≈ E21_Person temporal slice; events ≈ E5_Event subclasses
- Plan for Wikidata/VIAF/GeoNames grounding on persistent nodes (Stage 6)

---

## Schema Design

### Node labels (Stage 1)

```
Existing (Stage 0):
  (:Year {year: 1896})
  (:Territory {name: "Sierra Leone", ...})
  (:TerritoryYear {name: "Sierra Leone", year: 1896, source_file: "..."})

New (Stage 1):
  (:PersonRecord {
    uri: "col:pr/sierra_leone/1896/cardew_f",     -- stable identifier
    name_raw: "Colonel F. Cardew",                 -- exactly as in source
    canonical_name: "Cardew, F.",                   -- surname-first normalized
    surname: "Cardew",
    given_names: "F.",
    position_raw: "Governor, Commander-in-Chief",
    department_raw: "Civil Establishment",
    salary_min: 2000,                               -- nullable
    salary_max: 2000,                               -- nullable
    salary_currency: "GBP",                         -- inferred from colony
    allowances_raw: "500l. allowances",             -- nullable, unparsed
    honors: ["C.M.G."],                             -- list
    qualifications: [],                             -- list
    military_rank: "Colonel",                       -- nullable
    location: null,                                 -- nullable
    source_file: "1896_manual_parsed/sierra_leone.txt",
    extraction_file: "generated/sierra_leone_1896_data_gpt-oss_120b.json",
    record_index: 0,                                -- position within extraction file
    colony: "Sierra Leone",                         -- denormalized for queries
    year: 1896                                      -- denormalized for queries
  })

  (:InstitutionInstance {
    uri: "col:inst/sierra_leone/1896/civil_establishment",
    name_raw: "Civil Establishment",
    colony: "Sierra Leone",
    year: 1896
  })

Placeholder for future stages (NOT created in Stage 1):
  (:Person)              -- persistent identity, earned in Stage 4
  (:InstitutionType)     -- normalized dept family, Stage 3
  (:PositionType)        -- normalized position family, Stage 3
  (:PositionInstance)    -- specific post, Stage 3
  (:CareerEvent)         -- appointment/transfer/promotion, Stage 4
```

### Edge types (Stage 1)

```
(pr:PersonRecord)-[:SERVED_IN]->(ty:TerritoryYear)
  {method: "automated_extraction", confidence: 0.95, pipeline_version: "1.0",
   date_created: "2026-02-22"}

(pr:PersonRecord)-[:IN_DEPARTMENT]->(ii:InstitutionInstance)
  {method: "automated_extraction", ...}

(ii:InstitutionInstance)-[:DEPARTMENT_OF]->(ty:TerritoryYear)
  {method: "automated_extraction", ...}

(pr:PersonRecord)-[:IN_YEAR]->(y:Year)
  -- lightweight temporal anchor, no provenance needed

(ii:InstitutionInstance)-[:IN_YEAR]->(y:Year)
```

### Indexes and constraints

```cypher
-- Uniqueness
CREATE CONSTRAINT pr_uri IF NOT EXISTS FOR (pr:PersonRecord) REQUIRE pr.uri IS UNIQUE;
CREATE CONSTRAINT ii_uri IF NOT EXISTS FOR (ii:InstitutionInstance) REQUIRE ii.uri IS UNIQUE;

-- Lookup indexes
CREATE INDEX pr_colony_year IF NOT EXISTS FOR (pr:PersonRecord) ON (pr.colony, pr.year);
CREATE INDEX pr_surname IF NOT EXISTS FOR (pr:PersonRecord) ON (pr.surname);
CREATE INDEX pr_canonical IF NOT EXISTS FOR (pr:PersonRecord) ON (pr.canonical_name);
CREATE INDEX ii_colony_year IF NOT EXISTS FOR (ii:InstitutionInstance) ON (ii.colony, ii.year);

-- Full-text search for names (fuzzy matching in Stage 4)
CREATE FULLTEXT INDEX pr_name_ft IF NOT EXISTS FOR (n:PersonRecord) ON EACH [n.name_raw, n.canonical_name, n.surname];
```

---

## URI Scheme

Base namespace: `col:` (short prefix, expanded to full URL when exporting RDF)

```
Pattern:                         Example:
col:yr/{year}                    col:yr/1896
col:territory/{slug}             col:territory/sierra_leone
col:ty/{slug}/{year}             col:ty/sierra_leone/1896
col:pr/{slug}/{year}/{name_key}  col:pr/sierra_leone/1896/cardew_f
col:inst/{slug}/{year}/{dept}    col:inst/sierra_leone/1896/civil_establishment
col:person/{id}                  col:person/00001  (Stage 4, auto-increment)
col:event/{type}/{id}            col:event/appointment/00001  (Stage 4)
```

The `name_key` for PersonRecord URIs is generated as: `surname_initials` lowercased, deduplicated with numeric suffix if needed (e.g., `smith_j`, `smith_j_2`).

---

## Currency Inference

Map colony → currency based on historical knowledge:

```python
RUPEE_COLONIES = {
    "Ceylon", "Straits Settlements", "Hong Kong",       # pre-1900 used various
    "Mauritius",                                          # Mauritian rupee
}
# Most colonies used British pounds (GBP)
# Some used local dollars (Hong Kong after certain dates)
# Default: "GBP" — the CO List predominantly reports in pounds
# Store as property; can be corrected later without schema change
```

This is a simplification. The `salary_currency` field is a best guess, stored alongside the raw salary figures. Scholars can correct individual records.

---

## Implementation: `load_neo4j.py`

### CLI

```bash
python load_neo4j.py                          # load all available extractions
python load_neo4j.py --year 1896              # load one year
python load_neo4j.py --colony "Sierra Leone"  # load one colony
python load_neo4j.py --dry-run                # preview what would be loaded
python load_neo4j.py --clear                  # remove all Stage 1 nodes (careful!)
python load_neo4j.py --stats                  # report on current graph contents
```

### Loading logic (pseudocode)

```
1. Connect to Neo4j (bolt://localhost:7687)
2. Create constraints and indexes (idempotent)
3. Discover extraction JSON files in generated/
4. For each file:
   a. Skip if already loaded (check TerritoryYear.stage1_loaded flag)
   b. Read JSON, parse officials list
   c. Find matching TerritoryYear node (by colony + year)
   d. If no TerritoryYear match, warn and skip (extraction for a colony not in scaffold)
   e. Infer source_file from colony + year
   f. Infer salary_currency from colony
   g. Create InstitutionInstance nodes (one per unique department in this file)
   h. Create PersonRecord nodes (one per official)
   i. Create edges: SERVED_IN, IN_DEPARTMENT, DEPARTMENT_OF, IN_YEAR
   j. Set TerritoryYear.stage1_loaded = true, stage1_count = N
   k. Log: colony, year, N officials loaded, N departments
5. Print summary: total loaded, skipped, errors
```

### Batch loading strategy

Use `UNWIND` with batches of ~500 records for performance:

```cypher
UNWIND $batch AS rec
MATCH (ty:TerritoryYear {name: rec.colony, year: rec.year})
MATCH (y:Year {year: rec.year})
MERGE (ii:InstitutionInstance {uri: rec.inst_uri})
  ON CREATE SET ii.name_raw = rec.department, ii.colony = rec.colony, ii.year = rec.year
CREATE (pr:PersonRecord {
  uri: rec.uri,
  name_raw: rec.name_raw,
  canonical_name: rec.canonical_name,
  ...all fields...
})
CREATE (pr)-[:SERVED_IN {method: "automated_extraction", confidence: rec.confidence,
  pipeline_version: "1.0", date_created: $today}]->(ty)
CREATE (pr)-[:IN_DEPARTMENT {method: "automated_extraction", pipeline_version: "1.0",
  date_created: $today}]->(ii)
CREATE (pr)-[:IN_YEAR]->(y)
MERGE (ii)-[:DEPARTMENT_OF]->(ty)
MERGE (ii)-[:IN_YEAR]->(y)
```

### Incremental loading

The extraction is still running (239/2164 done). The loader must:
- Check `TerritoryYear.stage1_loaded` before loading a file
- Be safe to re-run: new files get loaded, already-loaded files get skipped
- Auto-push script pushes new JSONs to GitHub hourly; loader reads from local disk

We can re-run `load_neo4j.py` periodically (or even daily via cron) to keep the graph current with extraction progress.

---

## Provenance Strategy

Every edge created by the loader carries:

| Property | Value | Purpose |
|----------|-------|---------|
| `method` | `"automated_extraction"` | Distinguishes from manual annotation or external match |
| `pipeline_version` | `"1.0"` | Tracks which code version created the edge |
| `confidence` | 0.0–1.0 | From validation (HIGH=0.95, MEDIUM=0.7, LOW=0.3) |
| `date_created` | ISO date | When the edge was created |

PersonRecord nodes also carry `extraction_file` and `record_index` for full traceability back to the extraction output.

---

## Files

| File | Action |
|------|--------|
| `load_neo4j.py` | **NEW** — Stage 1 Neo4j loader |
| `scaffold_neo4j.py` | Read only — reuse `normalize_colony_name()`, `EXPLICIT_ALIASES` |

---

## Verification

1. **Schema test**: Run `load_neo4j.py --dry-run` — confirm it discovers extraction files, matches to TerritoryYear nodes, reports counts
2. **Single colony test**: Run `load_neo4j.py --colony "Sierra Leone" --year 1896` — load 183 officials, verify in Neo4j Browser:
   ```cypher
   MATCH (pr:PersonRecord)-[:SERVED_IN]->(ty:TerritoryYear {name: "Sierra Leone", year: 1896})
   RETURN pr.canonical_name, pr.position_raw, pr.department_raw, pr.salary_min
   ORDER BY pr.department_raw, pr.canonical_name
   LIMIT 20
   ```
3. **Provenance check**: Verify edges carry provenance properties:
   ```cypher
   MATCH ()-[r:SERVED_IN]->() RETURN r.method, r.confidence, r.pipeline_version LIMIT 5
   ```
4. **Department check**: Verify InstitutionInstance nodes are created and linked:
   ```cypher
   MATCH (ii:InstitutionInstance)-[:DEPARTMENT_OF]->(ty:TerritoryYear {year: 1896})
   RETURN ty.name, ii.name_raw, size(()-[:IN_DEPARTMENT]->(ii)) AS officials
   ORDER BY officials DESC LIMIT 20
   ```
5. **Full load**: Run `load_neo4j.py` to load all available extractions. Check total node/edge counts:
   ```cypher
   MATCH (pr:PersonRecord) RETURN count(pr)
   MATCH ()-[r:SERVED_IN]->() RETURN count(r)
   ```
6. **Idempotency**: Re-run `load_neo4j.py` — confirm no duplicates created

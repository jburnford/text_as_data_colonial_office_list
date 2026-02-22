# Plan: Neo4j Stage 3 — Normalization and Taxonomy

## Context

Stage 1 loaded 34,806 PersonRecords and 4,345 InstitutionInstances into Neo4j. Analysis reveals:
- **1,256 distinct department names** need clustering into ~50-80 InstitutionType nodes
- **5,953 distinct position titles** need clustering into ~500-1000 PositionType nodes
- 12 predefined CareerTrack categories provide the professional domain taxonomy

The user's developer team (assessing Cursor/Cline) will implement this. Graduate students in the SSHRC PAST partnership will review the generated taxonomy. This plan must be detailed enough for both audiences.

### Critical Epistemological Constraint

**Two-tier evidence model** — never violated:
- **Slice layer** (PersonRecord, InstitutionInstance): records what the SOURCE said. Never infer or add missing data.
- **Persistent layer** (InstitutionType, PositionType, CareerTrack): records what we KNOW. Normalization lives here.

Example: If a text didn't place "Archdeacon" under an "Ecclesiastical Department" header, do NOT add an `IN_DEPARTMENT` edge. Instead, link `PositionType("Archdeacon") -[BELONGS_TO_TRACK]-> CareerTrack("Ecclesiastical")`. Scholars query the career track to find all ecclesiastical officials without falsely claiming the source contained a department header.

---

## Schema Additions (Stage 3)

### New nodes

```
(:InstitutionType {uri, canonical_name})          — persistent department family
(:PositionType {uri, canonical_name, grade_level}) — persistent normalized role
(:CareerTrack {uri, name})                         — persistent professional domain (12+)
```

### New edges

```
(ii:InstitutionInstance)-[:TYPE_OF]->(it:InstitutionType)
  {method, confidence, pipeline_version, date_created}

(pr:PersonRecord)-[:HAS_POSITION]->(pt:PositionType)
  {method, confidence, pipeline_version, date_created}

(pt:PositionType)-[:BELONGS_TO_TRACK]->(ct:CareerTrack)
  {method, pipeline_version, date_created}
```

### No PositionInstance nodes in Stage 3

The post-level specificity ("2nd Clerk in Treasury, Sierra Leone 1896") is already captured by `PersonRecord.position_raw` + `IN_DEPARTMENT` + `SERVED_IN`. PositionInstance nodes can be created in Stage 4 if needed for vacancy tracking. This keeps the graph lean.

### URI scheme

```
col:itype/{slug}     e.g. col:itype/medical_department
col:ptype/{slug}     e.g. col:ptype/clerk_2nd
col:ctrack/{slug}    e.g. col:ctrack/administrative
```

---

## Architecture: Two-Phase Pipeline

### Phase A: Generate Taxonomy (read-only, no Neo4j writes)

Produces human-reviewable JSON files. Graduate students review before anything enters the graph.

### Phase B: Load Taxonomy (after human review)

Reads approved JSON, creates persistent nodes and edges in Neo4j.

---

## Phase A: Taxonomy Generation

### Step 1: Extract from Neo4j

```cypher
-- All distinct department names with context
MATCH (ii:InstitutionInstance)
RETURN ii.name_raw AS raw_name, count(*) AS instance_count,
       collect(DISTINCT ii.colony) AS colonies, collect(DISTINCT ii.year) AS years
ORDER BY instance_count DESC

-- All distinct position titles with context
MATCH (pr:PersonRecord) WHERE pr.position_raw IS NOT NULL
RETURN pr.position_raw AS raw_position, count(*) AS record_count,
       collect(DISTINCT pr.department_raw) AS departments,
       collect(DISTINCT pr.colony) AS colonies
ORDER BY record_count DESC
```

### Step 2: Rule-based pre-clustering (`normalize_rules.py`)

Deterministic regex rules handle the easy cases (~60% of departments, ~40% of positions). This is auditable, reproducible, and free.

**Department rules** — dictionary of `{cluster_id: {canonical_name, patterns[]}}`:

| Cluster | Canonical Name | Example Patterns |
|---------|---------------|-----------------|
| medical | Medical Department | `^medical(\s+department)?$`, `^medical and sanitary` |
| treasury | Treasury | `^treasury(\s+department)?$`, `^treasurer.s department$` |
| police | Police Department | `^police(\s+department)?$`, `^police and gaols?$` |
| ecclesiastical | Ecclesiastical | `^ecclesiastic(al)?(\s+department\|establishment)?$` |
| postal | Post Office | `^post.?office`, `^postal department$`, `^post and telegraph` |
| ... | ... | ~27 total rules covering Civil Est., Judicial, Audit, Customs, Public Works, Prisons, Colonial Sec., Survey, Registrar, Education, Harbour, Printing, Railways, Health, Immigration, Crown Lands, Botanic Gardens, Executive/Legislative Council, Attorney-General, Telegraph, Consuls |

**Position rules** — pre-normalization transforms + family matching:

1. **Normalize**: lowercase, expand abbreviations (Col.→Colonial, Asst.→Assistant, Supt.→Superintendent, Govt.→Government, Dept.→Department), strip trailing periods, normalize quotes/dashes
2. **Extract grade**: "2nd Clerk" → base="Clerk", grade=2; "Clerks, 1st Class" → base="Clerk", grade=1; ordinal standardization (first→1st, second→2nd)
3. **Singular/plural**: "Clerks"→"Clerk", "Inspectors"→"Inspector"
4. **Family match**: ~50 high-confidence position families with career track hints

### Step 3: LLM-assisted clustering (`normalize_llm.py`)

**LLM**: Claude API (Sonnet) — runs remotely, zero GPU impact while extraction continues on Ollama.

**Department prompt** (sent as a single batch, ~500 unclustered names):

```
You are a historian specializing in British colonial administration. Given the
following list of department/institution names extracted from Colonial Office
Lists (1867-1966), cluster them into groups where each group represents the
same type of institution appearing in different colonies or eras.

RULES:
1. Only group names when you are CONFIDENT they refer to the same institutional
   function. When in doubt, keep them separate.
2. "Medical Department" and "Medical and Sanitary Department" → same type.
3. "Provincial Administration" ≠ "Civil Establishment" — distinct institutional
   contexts.
4. Colony-specific qualifiers (e.g. "Sierra Leone Battalion, WAFF") → group by
   function (Military), not by colony name.
5. Use the most common variant as the canonical name.
6. Assign confidence: HIGH (obvious synonyms), MEDIUM (probable, needs reviewer
   confirmation), LOW (possible, needs scholar decision).

Previously clustered (HIGH confidence, do not re-cluster):
{pre_clustered_json}

Unclustered names to process (with instance counts):
{unclustered_names}

Return JSON array:
[{"canonical_name": "...", "members": ["raw1", "raw2"],
  "confidence": "HIGH|MEDIUM|LOW", "reasoning": "..."}]
```

**Position prompt** (batched by frequency, ~6-10 API calls):

```
You are a historian specializing in British colonial administration. Given the
following position titles from Colonial Office Lists (1867-1966), group them
into clusters where each cluster represents the same functional role.

RULES:
1. "Colonial Surgeon" and "Col. Surgeon" → same. "Colonial Surgeon" and
   "Senior Medical Officer" → may NOT be same (different grades).
2. Graded positions: "Clerk", "2nd Clerk", "Chief Clerk" are DIFFERENT types.
3. "Clerks, 1st Class" and "1st Class Clerk" → same.
4. Department-qualified positions: "Clerk" in Treasury and "Clerk" in Post
   Office → same PositionType "Clerk" (department comes from the graph edge).
5. Assign each to one CareerTrack: Administrative, Legal, Medical, Financial,
   Engineering, Survey, Police, Ecclesiastical, Education, Military, Postal,
   Agricultural. Use null if track depends on department context.

Return JSON array:
[{"canonical_name": "...", "members": ["raw1", "raw2"],
  "confidence": "HIGH|MEDIUM|LOW", "career_track": "..." or null,
  "grade_level": int or null, "reasoning": "..."}]
```

**Cost**: ~10 API calls, ~80K tokens total. Under $1 at Sonnet pricing.

### Step 4: Output taxonomy JSON

Two files: `taxonomy/department_taxonomy.json` and `taxonomy/position_taxonomy.json`.

**Department taxonomy format**:
```json
{
  "version": "0.1", "generated": "...", "status": "DRAFT",
  "institution_types": [
    {
      "id": "dept_medical", "uri": "col:itype/medical_department",
      "canonical_name": "Medical Department",
      "members": [
        {"raw": "Medical Department", "count": 150, "confidence": "HIGH", "method": "rule"},
        {"raw": "Medical", "count": 89, "confidence": "HIGH", "method": "rule"},
        {"raw": "Health Department", "count": 8, "confidence": "MEDIUM", "method": "llm"}
      ],
      "career_track": "Medical",
      "reviewer_decision": null
    }
  ],
  "unclustered": [{"raw": "...", "count": N, "reason": "..."}]
}
```

**Position taxonomy format** — same structure, plus `grade_level` field.

---

## Human Review Workflow

Graduate students review taxonomy JSON files before Phase B loading.

**Decision categories** per cluster:
- **APPROVE** — grouping correct, canonical name good
- **SPLIT** — over-merged, should become 2+ clusters
- **MERGE** — under-merged, combine with another cluster
- **RENAME** — change canonical name
- **RECLASSIFY** — wrong career track
- **FLAG** — needs domain expert opinion

**Review priority**: highest-count clusters first (they affect the most records).

**Special attention areas**:
- "Civil Establishment" is a catch-all, not a real department — keep as InstitutionType but no CareerTrack
- "Foreign Consuls" is a section header — either create a 13th CareerTrack("Consular") or leave career_track null
- "Sanitary Department" ≠ "Medical Department" — historically distinct functions
- Colony-specific institutions (WAFF, Jamaica Constabulary) → cluster by function

**Tool**: Extend `review_extraction.py` pattern (APPROVE/REJECT/FLAG CLI) or build minimal review CLI that loads taxonomy JSON, presents clusters, records decisions.

---

## Phase B: Load Taxonomy into Neo4j

### Pre-conditions
- Taxonomy JSON has `status: "APPROVED"`
- All high-count clusters (>100 records) reviewed

### Loading order

1. **CareerTrack nodes** (12 nodes from `taxonomy/career_tracks.json`)
2. **InstitutionType nodes** (from reviewed department taxonomy)
3. **PositionType nodes** (from reviewed position taxonomy)
4. **TYPE_OF edges**: `InstitutionInstance → InstitutionType` (match on `name_raw IN members`)
5. **HAS_POSITION edges**: `PersonRecord → PositionType` (match on `position_raw IN members`)
6. **BELONGS_TO_TRACK edges**: `PositionType → CareerTrack`

### Key Cypher patterns

```cypher
-- TYPE_OF edges (batch by InstitutionType)
UNWIND $mappings AS m
MATCH (ii:InstitutionInstance) WHERE ii.name_raw IN m.members
MATCH (it:InstitutionType {uri: m.type_uri})
MERGE (ii)-[r:TYPE_OF]->(it)
ON CREATE SET r.method = m.method, r.confidence = m.confidence,
              r.pipeline_version = $pipeline_version, r.date_created = $today

-- HAS_POSITION edges (batch by PositionType)
UNWIND $mappings AS m
MATCH (pr:PersonRecord) WHERE pr.position_raw IN m.members
MATCH (pt:PositionType {uri: m.type_uri})
MERGE (pr)-[r:HAS_POSITION]->(pt)
ON CREATE SET r.method = m.method, r.confidence = m.confidence,
              r.pipeline_version = $pipeline_version, r.date_created = $today
```

All uses MERGE for idempotency. Provenance on every edge.

### Confidence score mapping

| Method | Level | Score |
|--------|-------|-------|
| rule | HIGH | 0.98 |
| rule | MEDIUM | 0.85 |
| llm_assisted | HIGH | 0.90 |
| llm_assisted | MEDIUM | 0.75 |
| llm_assisted | LOW | 0.55 |
| human_reviewed | — | 0.99 |

---

## Files

| File | Action |
|------|--------|
| `normalize_stage3.py` | **NEW** — main CLI orchestrator |
| `normalize_rules.py` | **NEW** — rule-based pre-clustering (regex dict) |
| `normalize_llm.py` | **NEW** — Claude API prompting for clustering |
| `taxonomy/career_tracks.json` | **NEW** — 12 CareerTrack seed definitions |
| `taxonomy/department_taxonomy.json` | **GENERATED** — Phase A output |
| `taxonomy/position_taxonomy.json` | **GENERATED** — Phase A output |
| `taxonomy/REVIEW_GUIDE.md` | **NEW** — instructions for graduate student reviewers |
| `load_neo4j.py` | Read only — reuse `slugify()`, URI patterns, Neo4j config |
| `scaffold_neo4j.py` | Read only — reuse `normalize_colony_name()` |
| `review_extraction.py` | Read only — pattern for review CLI |

---

## Verification (Phase B)

```cypher
-- Node counts
MATCH (it:InstitutionType) RETURN count(it);
MATCH (pt:PositionType) RETURN count(pt);
MATCH (ct:CareerTrack) RETURN count(ct);

-- TYPE_OF coverage
MATCH (ii:InstitutionInstance)
OPTIONAL MATCH (ii)-[:TYPE_OF]->(it:InstitutionType)
RETURN count(ii) AS total, count(it) AS typed,
       toFloat(count(it))/count(ii)*100 AS pct;

-- HAS_POSITION coverage
MATCH (pr:PersonRecord) WHERE pr.position_raw IS NOT NULL
OPTIONAL MATCH (pr)-[:HAS_POSITION]->(pt:PositionType)
RETURN count(pr) AS total, count(pt) AS typed,
       toFloat(count(pt))/count(pr)*100 AS pct;

-- Career track distribution
MATCH (pt:PositionType)-[:BELONGS_TO_TRACK]->(ct:CareerTrack)
RETURN ct.name, count(pt) AS types ORDER BY types DESC;

-- The 1867 Falkland Archdeacon test (epistemological constraint)
MATCH (pr:PersonRecord {colony: "Falkland Islands", year: 1867})
WHERE pr.position_raw CONTAINS "Archdeacon"
OPTIONAL MATCH (pr)-[:IN_DEPARTMENT]->(ii)
OPTIONAL MATCH (pr)-[:HAS_POSITION]->(pt)-[:BELONGS_TO_TRACK]->(ct)
RETURN pr.canonical_name, pr.position_raw, ii.name_raw AS dept, ct.name AS track
-- Expected: dept=null, track="Ecclesiastical"
```

---

## Implementation Sequence

1. Create `normalize_rules.py` — rule dictionary + regex clustering (pure Python)
2. Create `taxonomy/career_tracks.json` — seed file
3. Create `normalize_llm.py` — Claude API caller with prompt templates
4. Create `normalize_stage3.py` — CLI orchestrator (Phase A: generate taxonomy)
5. **Human review** — graduate students review taxonomy JSON
6. Add Phase B loading to `normalize_stage3.py` — Neo4j writes
7. Create `taxonomy/REVIEW_GUIDE.md`
8. Verify with Cypher queries

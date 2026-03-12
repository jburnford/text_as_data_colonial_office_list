# Taxonomy Review Guide

## For Graduate Student Reviewers (SSHRC PAST Partnership)

This guide explains how to review the machine-generated taxonomy files
before they are loaded into the knowledge graph.

---

## What You Are Reviewing

Two JSON files containing clusters of department names and position titles
extracted from Colonial Office Lists (1867-1966):

- `department_taxonomy.json` — groups of department/institution names
- `position_taxonomy.json` — groups of position/role titles

Each cluster proposes that several raw strings from the source texts refer
to the **same institutional type** or **same functional role**.

### Why This Matters

These clusters become persistent nodes in the knowledge graph. If "Medical
Department" and "Health Department" are correctly grouped, scholars can
query all medical officials across the empire with a single query. If they
are incorrectly grouped, the graph produces misleading results.

**Precision matters more than recall.** It is better to leave two names
unclustered (a scholar can find them manually) than to incorrectly merge
them (creating false associations that propagate silently).

---

## Taxonomy File Structure

Each cluster looks like this:

```json
{
  "id": "dept_medical",
  "uri": "col:itype/medical_department",
  "canonical_name": "Medical Department",
  "members": [
    {"raw": "Medical Department", "count": 1002, "confidence": "HIGH", "method": "rule"},
    {"raw": "Medical", "count": 489, "confidence": "HIGH", "method": "rule"},
    {"raw": "Health Department", "count": 8, "confidence": "MEDIUM", "method": "llm_assisted"}
  ],
  "career_track": "Medical",
  "reviewer_decision": null
}
```

Key fields:
- **canonical_name**: the label that will appear in the graph
- **members**: raw strings that map to this type, with occurrence counts
- **confidence**: HIGH / MEDIUM / LOW — how certain the grouping is
- **method**: "rule" (regex match) or "llm_assisted" (Gemini suggested)
- **career_track**: which professional domain (12 options, or null)
- **reviewer_decision**: your decision (starts as null)

---

## Review Decisions

For each cluster, record one of these decisions:

| Decision | When to Use |
|----------|------------|
| **APPROVE** | Grouping is correct, canonical name is appropriate |
| **SPLIT** | Cluster contains items that should be separate types |
| **MERGE** | This cluster should be combined with another cluster |
| **RENAME** | Grouping is correct but canonical name should change |
| **RECLASSIFY** | Wrong career track assigned |
| **FLAG** | Needs domain expert opinion — you are unsure |

### How to Record

Edit the `reviewer_decision` field in the JSON:

```json
"reviewer_decision": "APPROVE"
```

For SPLIT, MERGE, RENAME, or RECLASSIFY, add a `reviewer_notes` field:

```json
"reviewer_decision": "SPLIT",
"reviewer_notes": "Separate 'Health Department' — historically distinct from Medical in some colonies"
```

---

## Review Priority

Review clusters in this order:

1. **HIGH-count clusters first** — clusters where `count` sums to >100
   affect the most records in the graph. Get these right.
2. **MEDIUM confidence items** — rule-based HIGH confidence items are
   almost always correct. Focus your attention on MEDIUM and LOW.
3. **LLM-assisted clusters** — the LLM sometimes over-merges or assigns
   wrong career tracks. Check these more carefully than rule-based ones.

---

## Special Attention Areas

### Departments

- **"Civil Establishment"** is a section header, not a real department.
  It remains as an InstitutionType but has no career track (null).
  Do NOT merge it with other departments.

- **"Sanitary Department" vs "Medical Department"** — historically distinct
  functions in many colonies. The sanitary department handled public health
  infrastructure (drains, quarantine) while the medical department handled
  clinical care. Keep them separate unless the source text treats them as one.

- **"Foreign Consuls"** is a section listing foreign diplomatic
  representatives, not a colonial department. It has career_track: null.

- **Colony-specific institutions** like "Jamaica Constabulary" or "Sierra
  Leone Battalion, WAFF" should be grouped by function (Police, Military),
  not kept as colony-specific types.

- **Compound departments** like "Customs and Treasury" or "Post and
  Telegraph" — these are real institutional forms, not errors. Keep them
  as distinct types.

### Positions

- **Graded positions are distinct types**: "Clerk", "2nd Clerk", "Chief
  Clerk", and "Senior Clerk" are FOUR separate PositionTypes. Do NOT merge
  grades.

- **"Clerk, 1st Class" = "1st Class Clerk"** — these ARE the same.

- **Department-qualified clerks**: "Clerk" in Treasury and "Clerk" in Post
  Office are the SAME PositionType "Clerk". The department relationship
  comes from the graph edge (`IN_DEPARTMENT`), not from the position type.

- **career_track = null** is correct for positions like "Clerk" or "Member"
  whose track depends entirely on which department they serve in.

### Career Tracks

The 12 career tracks are:

| Track | Description |
|-------|------------|
| Administrative | Governors, secretaries, district officers, cadets |
| Legal | Judges, attorneys, magistrates, registrars |
| Medical | Surgeons, medical officers, dispensers |
| Financial | Treasurers, auditors, collectors, customs |
| Engineering | Public works, railways, harbours |
| Survey | Surveyors, land commissioners |
| Police | Police, prisons, constabulary |
| Ecclesiastical | Bishops, chaplains, clergy |
| Education | Directors of education, schoolmasters |
| Military | Garrison, WAFF/KAR, commandants |
| Postal | Postmasters, telegraph operators |
| Agricultural | Agriculture, forestry, veterinary, botanic |

If a position or department doesn't fit any track, use null.

---

## The Two-Tier Evidence Rule

**Never violated.** The source text is sacred.

- **Slice layer** (PersonRecord, InstitutionInstance): records what the
  SOURCE SAID. We never add or infer missing data at this layer.

- **Persistent layer** (InstitutionType, PositionType, CareerTrack):
  records what we KNOW from normalization. This is where clustering lives.

**Example**: If a source text listed "Archdeacon" under no department
header, the PersonRecord has `department_raw = null` and no `IN_DEPARTMENT`
edge. The normalization layer links `PositionType("Archdeacon")` to
`CareerTrack("Ecclesiastical")`. A scholar queries the career track to find
all ecclesiastical officials without falsely claiming the source placed
the archdeacon in a specific department.

---

## When You Are Done

1. Set `reviewer_decision` on every cluster
2. Change the top-level `"status"` field from `"DRAFT"` to `"APPROVED"`:

```json
{
  "version": "0.1",
  "status": "APPROVED",
  ...
}
```

3. Notify the pipeline operator to run Phase B loading:
   ```
   python normalize_stage3.py load
   ```

---

## Questions?

If you encounter a cluster you cannot resolve, set `reviewer_decision` to
`"FLAG"` with notes explaining the ambiguity. Domain experts will review
flagged items before loading.

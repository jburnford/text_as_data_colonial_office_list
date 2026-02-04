# Text as Data: Colonial Office List Workshop

**Course**: HIST 496 - Text as Data
**Instructor**: Jo Guldi (guest: Jim Clifford)
**Duration**: 80 minutes
**Students**: 30 data science students

---

## Learning Objectives

By the end of this session, students will be able to:
1. Identify extractable data types in semi-structured historical documents
2. Understand why standard NER fails on administrative records
3. Conceptualize a knowledge graph schema for prosopographical data
4. Appreciate the entity resolution challenge across temporal documents
5. Experiment with extraction approaches (regex, LLM-based)

---

## Materials Needed

- Whiteboard/markers
- Projector for code demo
- Students need laptops with Python 3.10+
- Sample data files (provided)
- Optional: OpenAI/Anthropic API key for LLM demo

---

## Session Outline

### Part 1: The Corpus (10 minutes)

**Show Sierra Leone 1896 on screen**

Key points to make:
- 68 years of British imperial administration (1867-1966)
- ~50 colonies per year, each with similar structure
- 2,227 text files, 1.25 million lines
- Already OCR'd and parsed — the hard part is extraction

**Ask students**: What kinds of data do you see here?

Expected answers:
- Names
- Positions/titles
- Salaries
- Departments
- Honors (C.M.G., etc.)

**Reveal the scale**:
- ~150 people per colony per year
- 150 × 48 colonies × 68 years = **~490,000 person-position records**
- Estimated 50,000-100,000 unique individuals

---

### Part 2: Research Questions (10 minutes)

**Why would anyone care?**

Prosopography = collective biography. With this data we could answer:

1. **Career trajectories**: What paths led to becoming a Governor?
2. **Networks**: Who worked together? Who promoted whom?
3. **Salary inequality**: How did pay differ by colony, race, position?
4. **Institutional evolution**: How did departments change over time?
5. **Imperial connections**: How did officials move between colonies?

**Show the challenge**:
- "Samuel Rowe" (1881) = "Sir Saml. Rowe, K.C.M.G." (1888)?
- Same person, accumulated honors, different name forms
- Manual linking is impossible at this scale

---

### Part 3: Knowledge Graph Design (15 minutes) — WHITEBOARD

**Draw the basic schema**:

```
         ┌─────────┐
         │ Colony  │
         └────┬────┘
              │ PART_OF
              ▼
         ┌─────────┐        ┌─────────┐
         │  Dept   │◄───────│ Position│
         └─────────┘ PART_OF└────┬────┘
                                 │ HELD_POSITION
                                 │ {year, salary}
                                 ▼
                            ┌─────────┐
                            │ Person  │
                            └────┬────┘
                                 │ AWARDED
                                 ▼
                            ┌─────────┐
                            │  Honor  │
                            └─────────┘
```

**Key design decisions**:
1. Positions are nodes (not just relationship properties) — WHY?
   - Same position held by different people over time
   - Positions have attributes (salary range, department)

2. Year is on the relationship, not a separate node — WHY?
   - Query efficiency: "Who was Colonial Secretary in 1896?"
   - Temporal reasoning without explosion of nodes

3. Person nodes span years — WHY?
   - Entity resolution: link "Samuel Rowe" across all appearances
   - Career tracking requires persistent identity

**GraphRAG addition**:
- Narrative passages get chunked and embedded
- Passages link to entities they mention
- Query: "What did officials say about climate?"
  → Graph finds officials → retrieves their passages → LLM synthesizes

---

### Part 4: Why Standard NER Fails (10 minutes)

**Show a staff list entry**:
```
Colonial Secretary, Fred. Evans, C.M.G., 1,300l.
```

**Ask**: What's wrong with running spaCy NER on this?

Problems:
1. **Not prose**: NER expects sentences, not structured lists
2. **Domain-specific entities**: "C.M.G." is an honor, not recognized
3. **Implicit structure**: Position comes before name (or does it?)
4. **Abbreviations**: "l." = pounds, "ditto" = same as above
5. **No context**: Each line is independent, not a paragraph

**The real approach**: This is **pattern extraction** from semi-structured data, not NER.

**Show the pattern**:
```
[Position], [Name], [Honors], [Salary]l.
```

But patterns vary:
```
Assistant ditto, J. Allwood, 700l.                    # "ditto" = previous position type
Clerks, 1st Class, F. S. Sanguinetti, T. L. Roxburgh, and J. B. Lucie Smith, 300l. to 400l.  # Multiple people!
Superintendent, E. L. Du Quesnay, 200l. to 250l.     # Salary range
```

---

### Part 5: Hands-On Code (25 minutes)

**Option A: Students run locally** (if they have Python + optional API key)

**Option B: Live demo with discussion**

Walk through the provided notebook/script:

1. **Load and explore** the data (5 min)
2. **Naive regex** extraction — partial success (10 min)
3. **LLM-based extraction** with Pydantic schema (10 min)
4. **Discuss**: What broke? What worked?

**Key teaching moments**:
- Regex handles simple cases, fails on complexity
- LLM handles complexity but costs money and needs validation
- The "80/20 problem": 80% is easy, 20% is really hard
- Human-in-the-loop: you still need to check the output

---

### Part 6: The Entity Resolution Problem (5 minutes)

Even if extraction is perfect, you still have:

| Year | Name | Position |
|------|------|----------|
| 1881 | Samuel Rowe | Governor |
| 1885 | Sir Samuel Rowe, K.C.M.G. | Governor |
| 1888 | Sir Saml. Rowe, K.C.M.G. | Administrator |

**Is this one person or three?**

Signals:
- Same colony
- Name similarity (fuzzy match)
- Honors only accumulate (never lose a K.C.M.G.)
- Plausible career trajectory

Tools: **Splink** (probabilistic record linkage at scale)

---

### Part 7: Discussion & Wrap-up (5 minutes)

**Discussion questions**:
1. What other historical sources have this structure?
2. How would you validate extraction quality?
3. What's the minimum viable dataset to prove this works?
4. Who else should be working on this?

**The meta-lesson**:
- Historical data science isn't just "apply algorithm"
- Domain knowledge shapes every technical decision
- Scale changes what's possible (and what's hard)

---

## Appendix: The Prompt Approach

**Share Jim's current workflow** (token-heavy but effective):

The key insight: Rather than building a complex extraction pipeline, use an LLM with:
1. A detailed **extraction guide** (domain knowledge encoded)
2. A defined **schema** (what to extract)
3. **Incremental processing** (4-10 small scripts, not one giant one)
4. **Entity resolution hints** (check for returning officials)
5. **Human oversight** (verify counts, update tracking)

This is "prompt engineering as software architecture" — the prompt IS the program.

**Example prompt structure**:
```
Read [extraction_guide.md] for context.
Process the [YEAR] [COLONY] Colonial Office List:
1. Read source file
2. Extract all personnel following schema
3. Create loading scripts (NOT one large script)
4. Handle identity: Names are NOT unique, prioritize local matches
5. Load to Neo4j with colony-specific properties
6. Process geographic entities
7. Verify counts
8. Create prompt for next session
```

**Why this works**:
- LLM has full context of extraction rules
- Small scripts are easier to debug
- Explicit instructions prevent common errors
- Self-documenting workflow

---

## Files for Students

1. `extraction_demo.py` — Hands-on code
2. `sample_data/sierra_leone_1896.txt` — Full colony entry
3. `sample_data/jamaica_1896_staff.txt` — Just staff lists
4. `GRAPHRAG_ANALYSIS.md` — Full analysis document (optional reading)

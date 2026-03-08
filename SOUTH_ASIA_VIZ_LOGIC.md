# Empire Evolution Visualization: Change-Over-Time Logic

This document captures the patterns, rules, and lessons learned from building the territorial evolution visualization. South Asia was the hardest case and established the patterns; Southern Africa added new ones. Apply these consistently across all regions.

---

## 1. Change-Over-Time Patterns

### Pattern A: Simple Succession (EVOLVED_INTO)
Parent ends, child begins. One-to-one. No temporal overlap.
```
Fort William (1696-1757) ──EVOLVED_INTO──> Bengal Presidency Co. (1757-1858)
```

### Pattern B: Administrative Upgrade (EVOLVED_INTO, same entity)
Same entity transitions from one administrative form to another.
```
Bengal Presidency Co. (1757-1858) ──EVOLVED_INTO──> Bengal Presidency Crown (1858-1912)
Madras Presidency Co. (1640-1858) ──EVOLVED_INTO──> Madras Presidency Crown (1858-1947)
```
**Rule**: Parent's `ind` should equal child's `est`.

### Pattern C: Carve-Out (PARTITIONED_INTO, parent continues)
A piece is carved off but the parent entity continues operating.
```
Bengal Presidency Crown (1858-1912) ──PARTITIONED_INTO──> Assam Province (1874-1905)
Punjab Province (1849-1947) ──PARTITIONED_INTO──> NW Frontier Province (1901-1947)
Bombay Presidency Crown (1858-1947) ──PARTITIONED_INTO──> Sind (1936-1947)
```
**Rule**: The child's `est` should be the formal separation date, NOT the original conquest/discovery date. Sind was conquered in 1843 but became a separate province in 1936 — use 1936.

### Pattern D: Merger (multiple parents -> one child)
Two or more entities combine into one.
```
Eastern Bengal & Assam (1905-1912) + Bengal Partitioned (1905-1912)
    ──EVOLVED_INTO──> Bengal Province Reunited (1912-1947)
```
**Rule**: All parents' `ind` should match (or nearly match) the child's `est`.

### Pattern E: Partition (one parent -> multiple children, parent ends)
An entity is divided between successors. The parent ceases to exist.
```
Bengal Reunited (1912-1947) ──PARTITIONED_INTO──> Dominion of India + Dominion of Pakistan
BSAC Territory (1889-1923) ──PARTITIONED_INTO──> Southern Rhodesia Colony + Northern Rhodesia Colony
```
**Rule**: Use PARTITIONED_INTO when the parent is divided between successors. Use EVOLVED_INTO when the entire parent goes to one successor.

### Pattern F: Temporary Split-and-Rejoin (Bengal 1905-1912)
An entity splits and then the pieces recombine:
```
Bengal Crown ──> Bengal Partitioned (1905-1912) ──> Bengal Reunited (1912-1947)
Bengal Crown ──> E.B.&A. (1905-1912) ────────────> Bengal Reunited (1912-1947)
```
The intermediate entities have short lifespans (7 years).

### Pattern G: Absorption (smaller entity merges into ongoing larger entity)
A smaller entity is annexed or incorporated into a larger entity that predates it. The larger entity does NOT end — it continues with expanded territory.
```
Griqualand West (1871-1880) ──EVOLVED_INTO──> Cape Colony (British, 1806-1910)
British Bechuanaland (1885-1895) ──EVOLVED_INTO──> Cape Colony (British, 1806-1910)
Zululand (1887-1897) ──EVOLVED_INTO──> Colony of Natal (1843-1910)
```
**Key difference from Pattern D (Merger)**: In a merger, all parents end and a new child begins. In an absorption, the target entity already exists and continues — the absorbed entity simply disappears into it.

**Visual rule**: The flow curve connects at `x = source.ind` on BOTH sides (a short vertical drop/rise to the target bar at the absorption year), not at `target.est` which would create a backwards-flowing curve. The code detects this automatically: `isAbsorption = !isPartition && tgtStart < srcEnd`.

**Do NOT split the target entity into phases** to avoid backwards flow. This was tried with Cape Colony (splitting into 1806-1880, 1880-1895, 1895-1910) but it breaks visual continuity — the colony jumps across rows and gets lost. Keep the absorbing entity as one bar.

### Pattern H: Federation Cycle (join -> federate -> dissolve -> independence)
Entities join a federation, the federation dissolves, and the entities re-emerge. This creates graph cycles.
```
S. Rhodesia Colony (1923-1953) ──> Federation (1953-1963) ──> S. Rhodesia post-Fed (1963-1965)
N. Rhodesia Colony (1924-1953) ──> Federation (1953-1963) ──> N. Rhodesia post-Fed (1963-1964)
Nyasaland (1891-1953) ──────────> Federation (1953-1963) ──> Nyasaland post-Fed (1963-1964)
```
**Rule**: Break the cycle by creating post-federation nodes. The pre-federation entity "ends" when it enters the federation (`ind = federation.est`). The federation uses PARTITIONED_INTO to flow into post-federation nodes. Post-federation nodes then EVOLVED_INTO their independent successors.

**Do NOT extend pre-federation entities through the federation period** (e.g., setting NR Colony `ind: 1964`). This creates temporal overlaps with the Federation bar. Simpler to show: colony ends → federation → post-federation node → independence.

---

## 2. Non-British Entities

### Boer Republics and Dutch/French Colonies
Entities that appear in the lineage but were never British possessions:
- **Boer Republics**: Orange Free State, South African Republic (Transvaal), SAR Restored, Natalia Republic
- **Dutch Colonies**: Cape Colony (Dutch), Cape Colony (Dutch Restored)
- **French Colonies**: New France, Acadia

**Visual rule**: Render with dashed outline + transparent fill (CSS class `nonbritish`). They are part of the succession story but must be visually distinct from British territories.

**Edge rule**: These entities are standalone origins or endpoints in their lineage — they were not "created by" British entities. The ORS was proclaimed by the Cape governor but over territory north of the Orange River that was never part of the Cape Colony. The Natalia Republic was founded by Boer trekkers. Do not create false PARTITIONED_INTO edges from British colonies to non-British entities just because a British official was involved.

### The Orange Free State / Cape Colony question
The Orange River Sovereignty (1848-1854) was proclaimed by the Cape Colony governor over trans-Orange territory. But this was NOT Cape Colony territory — the Orange River was the Cape's border. The ORS is a standalone British entity. The chain is:
```
ORS (1848-1854) ──EVOLVED_INTO──> OFS (1854-1900) ──EVOLVED_INTO──> ORC (1900-1910) ──> Union of SA
```
No edge connects the Cape Colony to this lineage. They are independent streams that converge at the Union of South Africa (1910).

---

## 3. Avoiding Teleological Framing

**Problem**: An "East India Company (Pre-Territorial) 1612-1757" bar implies the Company was destined to become the Raj.

**Solution**: Remove umbrella/envelope entities. Show actual historical entities:
- Factory at Surat (1612-1687) -> Bombay Presidency Co.
- Fort William (1696-1757) -> Bengal Presidency Co.
- Madras Presidency Co. starts at 1640 directly (Fort St. George IS Madras -- same entity, removed as duplicate)

**General rule**: If an entity exists only to group successors and wasn't a real administrative unit, remove it.

**Southern Africa examples**:
- Southern Rhodesia (1901-1980): envelope bar overlapping with Southern Rhodesia Colony (1923-1953). Removed; edges redirected through the Colony node.
- Northern Rhodesia (1911-1964): same issue. Removed; edges redirected through NR Colony.

---

## 4. Date Fixing Rules

### End dates (`ind`)
- `ind: null` means "ongoing" -- bar extends to YEAR_MAX. Only for entities that truly persist (Gibraltar, Falklands).
- For entities entering a federation: set `ind` to the federation start year (e.g., Nyasaland `ind: 1953`).

### Start dates (`est`)
- Use the formal establishment date, not conquest/discovery.
- Sind: conquered 1843, `est: 1936` (separated as province from Bombay).

### Fort/Factory end dates
- End when the successor entity is established.

---

## 5. Edge Rules

### Direction
Edges must flow forward in time. Backwards edges create visual artifacts (curves flowing left).

### Edge type selection
| Scenario | Edge Type |
|----------|-----------|
| Parent ends, child begins | EVOLVED_INTO |
| Parent continues, child carved out | PARTITIONED_INTO |
| Parent divided between successors | PARTITIONED_INTO |
| Multiple parents merge into child | EVOLVED_INTO |
| Smaller entity absorbed into ongoing larger entity | EVOLVED_INTO |
| Federation dissolves into constituent parts | PARTITIONED_INTO |

### Bad edge patterns to remove
- **Membership edges**: WIF -> Jamaica is membership, not succession
- **Annexation edges**: Cape Colony -> Natalia Republic was an annexation, not a partition or evolution
- **Authority-proclamation edges**: Cape Colony -> ORS — the Cape governor proclaimed it, but no territory was transferred
- **Concurrent parallel entities**: Southern Nigeria -> Northern Nigeria — these were parallel protectorates (both 1900-1914), not succession
- **Wrong node variant**: `assam_province_1874_1905 -> dominion_of_india` (wrong — the *restored* version has this edge)
- **Historically wrong**: `assam_province_restored -> dominion_of_pakistan` (Assam went to India; only Sylhet district went to Pakistan)

---

## 6. The Southern Africa Edge Graph (Final)

```
Cape Colony (Dutch, 1652-1795)
  └─> Cape Colony (Br. 1st, 1795-1803)
        └─> Cape Colony (Dutch Restored, 1803-1806)
              └─> Cape Colony (British, 1806-1910)
                    ├─ <── Griqualand West (1871-1880) absorbed 1880 [Pattern G]
                    ├─ <── British Bechuanaland (1885-1895) absorbed 1895 [Pattern G]
                    └─EVOLVED_INTO─> Union of South Africa (1910-1961)

Natalia Republic (1839-1843) [Boer, standalone origin]
  └─> Colony of Natal (1843-1910)
        ├─ <── Zululand (1887-1897) absorbed 1897 [Pattern G]
        └─EVOLVED_INTO─> Union of South Africa (1910-1961)

Orange River Sovereignty (1848-1854) [standalone British origin]
  └─> Orange Free State (1854-1900) [Boer Republic]
        └─> Orange River Colony (1900-1910)
              └─EVOLVED_INTO─> Union of South Africa (1910-1961)

S.A. Republic / Transvaal (1852-1877) [Boer Republic]
  └─> Transvaal Colony (1st British, 1877-1881)
        └─> S.A. Republic Restored (1881-1900) [Boer Republic]
              └─> Transvaal Colony (2nd British, 1900-1910)
                    └─EVOLVED_INTO─> Union of South Africa (1910-1961)

British Central Africa Protectorate (1891-1907)
  └─> Nyasaland (1891-1953)
        └─EVOLVED_INTO─> Federation of Rhodesia & Nyasaland (1953-1963)

BSAC Territory (1889-1923) ──PARTITIONED_INTO──┐
  ├─> S. Rhodesia Colony (1923-1953) ──────────> Federation (1953-1963) [Pattern H]
  └─> N. Rhodesia Colony (1924-1953) ──────────> Federation (1953-1963)
                                                   ├─PARTITIONED_INTO─> S. Rhodesia post-Fed (1963-1965) ──> Rhodesia (UDI) ──> Zimbabwe Rhodesia ──> S. Rhodesia (Restored)
                                                   ├─PARTITIONED_INTO─> N. Rhodesia post-Fed (1963-1964)
                                                   └─PARTITIONED_INTO─> Nyasaland post-Fed (1963-1964)

[Standalone — High Commission Territories, no succession edges]
  Basutoland (1868-1966) ──> Lesotho
  Bechuanaland Protectorate (1884-1966) ──> Botswana
  Swaziland (1903-1968) ──> Eswatini
```

---

## 7. The South Asia Edge Graph (Final)

```
Factory at Surat (1612-1687)
  └─EVOLVED_INTO─> Bombay Presidency Co. (1687-1858)
                     └─EVOLVED_INTO─> Bombay Presidency Crown (1858-1947)
                                        ├─PARTITIONED_INTO─> Sind (1936-1947) ─> Pakistan
                                        └─EVOLVED_INTO─> India

Fort William (1696-1757)
  └─EVOLVED_INTO─> Bengal Presidency Co. (1757-1858)
                     ├─PARTITIONED_INTO─> Assam (Bengal Pres.) (1826-1874)
                     │                     └─EVOLVED_INTO─> Assam Province (1874-1905)
                     │                                        └─EVOLVED_INTO─> E.B.&A. (1905-1912)
                     │                                                           ├─> Assam Restored (1912-1947) ─> India
                     │                                                           └─> Bengal Reunited (1912-1947)
                     └─EVOLVED_INTO─> Bengal Presidency Crown (1858-1912)
                                        ├─PARTITIONED_INTO─> Assam Province (see above)
                                        ├─EVOLVED_INTO─> E.B.&A. (see above)
                                        ├─EVOLVED_INTO─> Bengal Partitioned (1905-1912)
                                        │                  └─> Bengal Reunited (1912-1947) ─> India + Pakistan
                                        └─EVOLVED_INTO─> Bihar & Orissa (1912-1947) ─> India

Madras Presidency Co. (1640-1858)
  └─EVOLVED_INTO─> Madras Presidency Crown (1858-1947) ─> India

Punjab Province (1849-1947)
  ├─PARTITIONED_INTO─> NW Frontier Province (1901-1947) ─> Pakistan
  └─PARTITIONED_INTO─> India + Pakistan

[Standalone provinces: United Provinces, Central Provinces, Baluchistan, Coorg, Ajmer-Merwara, Andaman & Nicobar]
  └─EVOLVED_INTO─> India or Pakistan

[Standalone: Lower Burma ─> Burma (Br. India) ─> Burma (Colony)]
[Standalone: Ceylon, Maldives, Chagos Islands]
```

---

## 8. Layout Algorithm: DFS Lineage Layout

### Why one-row-per-entity

We tried three approaches before finding one that works:

**Attempt 1 -- Containment model** (children stacked inside parent bar):
Failed. Parallel entities overlap.

**Attempt 2 -- Weighted containment** (parent height = sum of children):
Fixed overlap but made parent bars unreasonably tall. Merge nodes got lost.

**Attempt 3 -- One-row-per-entity with DFS ordering** (what we use):
Every node gets UNIT (14px) height on its own row. Flow curves show connections. DFS from sources keeps parent->child on adjacent rows.

### The algorithm

```javascript
function layoutNode(id) {
  if (placed.has(id)) return;

  // CRITICAL: Defer merge nodes until ALL parents placed
  const parents = localParents[id].filter(p => comp.includes(p));
  if (parents.some(p => !placed.has(p))) return;

  placed.add(id);
  layout[id] = { y: yPos, h: UNIT };
  yPos += UNIT + GAP;

  // Immediately follow children (sorted by est date)
  const children = localChildren[id].filter(c => comp.includes(c));
  children.sort((a, b) => nodeById[a].est - nodeById[b].est);
  children.forEach(c => layoutNode(c));
}

sourceOrder.forEach(id => layoutNode(id));
```

### Flow rendering

Flow bands connect source bars to target bars with cubic Bezier curves:
- **Standard (EVOLVED_INTO)**: x1 = source.ind, x2 = target.est
- **Partition (PARTITIONED_INTO)**: x1 = target.est (connect at partition year within source bar), x2 = target.est
- **Absorption (source ends, target already existed)**: x1 = source.ind, x2 = source.ind (short vertical curve at absorption year on target bar)
- **Band height**: Source bar height divided by number of outbound edges
- **Gap warning**: Dashed stroke if temporal gap > 2 years (not for partitions or absorptions)

---

## 9. Visual Styling for Entity Types

| Entity Type | CSS Class | Visual |
|-------------|-----------|--------|
| Crown Colony, Protectorate, Province, etc. | (default) | Solid fill |
| Dominion, Independence, Federation, Transitional | `postimperial` | Dashed outline, 25% fill, 70% opacity |
| Boer Republic, Dutch Colony, French Colony | `nonbritish` | Dashed outline, 25% fill, 70% opacity |
| Standalone (no edges) | `standalone` | Smaller text (7px) |

---

## 10. Applying This to Other Regions

### West Africa (Nigeria)
Oil Rivers -> Niger Coast -> Southern/Northern Nigeria (parallel) -> Colony and Protectorate.

**Key issue**: Southern and Northern Nigeria were parallel protectorates (both 1900-1914), NOT a succession. The edge between them was removed. Both merge into Colony of Nigeria in 1914 (Pattern D: Merger).

### Southeast Asia (Malaya)
Penang + Singapore + Malacca -> Straits Settlements. FMS + UMS -> Malayan Union -> Federation -> Malaysia. Singapore separates.

**Same patterns**: Merger (Pattern D), then partition (Pattern E, Singapore separates).

### Caribbean
Leeward/Windward Islands federations. West Indies Federation (1958-1962).

**Key rule**: Federation membership is NOT succession. Don't create EVOLVED_INTO from WIF to member colonies that existed centuries before it.

### General checklist for each region
1. Identify envelope/umbrella bars -> remove, redirect edges
2. Identify non-British entities -> mark type, apply `nonbritish` styling
3. Check for backwards-flowing edges -> fix with correct pattern or remove
4. Check for absorption merges (Pattern G) -> ensure target is one continuous bar
5. Check for federation cycles (Pattern H) -> create post-federation nodes to break cycles
6. Verify all `est`/`ind` dates match edge endpoints
7. Add SHORT_NAMES for long entity names
8. Assign correct sub-region in AFRICA_SUBREGIONS (or equivalent)

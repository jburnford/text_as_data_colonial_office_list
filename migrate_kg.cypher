// ============================================================
// British Empire Knowledge Graph — Migration Script
// Run against live Neo4j at bolt://206.12.90.118:7687
// Date: 2026-03-09
// ============================================================
// This script fixes issues identified in the Gemini review:
//   1. Overloaded :Colony label → multi-label taxonomy
//   2. Meta-relationship anti-pattern → typed relationships
//   3. Data type inconsistencies → cast lat/lon, normalize dates
//   4. Princely State established_year → dynasty_founded
// ============================================================

// ── PHASE 1: Add :HistoricalTerritory base label to all Colony nodes ──

MATCH (c:Colony)
SET c:HistoricalTerritory;

// ── PHASE 2: Add specific labels based on colony_type / administrative_status ──

// Princely States
MATCH (c:Colony)
WHERE c.colony_type = 'Princely State'
SET c:PrincelyState
REMOVE c:Colony;

// Crown Colonies
MATCH (c:Colony)
WHERE c.administrative_status IN ['Crown Colony', 'Crown colony', 'Royal Colony']
SET c:CrownColony;

// Protectorates
MATCH (c:Colony)
WHERE c.administrative_status IN ['Protectorate', 'Colony/Protectorate', 'Occupation/Protectorate']
SET c:Protectorate;

// Dominions
MATCH (c:Colony)
WHERE c.administrative_status = 'Dominion'
SET c:Dominion;

// Mandates
MATCH (c:Colony)
WHERE c.administrative_status IN ['Mandate', 'Mandate/Trust Territory', 'Trust Territory']
SET c:Mandate;

// Independent Nations (post-independence successor states)
MATCH (c:Colony)
WHERE c.administrative_status IN ['Independence', 'Unilateral Independence']
SET c:IndependentNation
REMOVE c:Colony;

// Minor Territories
MATCH (c:Colony)
WHERE c.administrative_status IN ['Guano Island', 'Whaling Station', 'Remote Island']
SET c:MinorTerritory;

// Company Territories
MATCH (c:Colony)
WHERE c.administrative_status IN ['Company Territory', 'Trading Post', 'Company Settlement']
SET c:CompanyTerritory;

// Boer Republics
MATCH (c:Colony)
WHERE c.administrative_status = 'Boer Republic'
SET c:BoerRepublic
REMOVE c:Colony;

// Federations
MATCH (c:Colony)
WHERE c.administrative_status IN ['Federation', 'Federal Colony']
SET c:Federation;

// Provinces / Presidencies
MATCH (c:Colony)
WHERE c.administrative_status IN ['Province', 'Presidency', 'United Province', 'Division of a Presidency']
SET c:Province;

// Dependencies
MATCH (c:Colony)
WHERE c.administrative_status = 'Dependency'
SET c:Dependency;

// British Overseas Territories (modern)
MATCH (c:Colony)
WHERE c.administrative_status = 'British Overseas Territory'
SET c:OverseasTerritory;

// Condominiums
MATCH (c:Colony)
WHERE c.administrative_status IN ['Condominium', 'Anglo-French Condominium']
SET c:Condominium;

// Military Administrations
MATCH (c:Colony)
WHERE c.administrative_status = 'Military Administration'
SET c:MilitaryAdministration;

// ── PHASE 3: Refactor EVOLVED_INTO relationships with relationship_type ──
// Convert parameterized EVOLVED_INTO into properly typed relationships,
// preserving description and year as properties.

// BECAME_INDEPENDENT
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'BECAME_INDEPENDENT'
CREATE (a)-[:BECAME_INDEPENDENT {description: r.description, year: r.year, detail: 'BECAME_INDEPENDENT'}]->(b)
DELETE r;

// MERGED_INTO (absorbs MERGED_WITH)
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type IN ['MERGED_INTO', 'MERGED_WITH']
CREATE (a)-[:MERGED_INTO {description: r.description, year: r.year, detail: r.relationship_type}]->(b)
DELETE r;

// INCORPORATED_INTO
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'INCORPORATED_INTO'
CREATE (a)-[:INCORPORATED_INTO {description: r.description, year: r.year, detail: 'INCORPORATED_INTO'}]->(b)
DELETE r;

// REORGANIZED_AS (absorbs RENAMED_TO)
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type IN ['REORGANIZED_AS', 'RENAMED_TO']
CREATE (a)-[:REORGANIZED_AS {description: r.description, year: r.year, detail: r.relationship_type}]->(b)
DELETE r;

// BECAME_CROWN_COLONY
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'BECAME_CROWN_COLONY'
CREATE (a)-[:BECAME_CROWN_COLONY {description: r.description, year: r.year, detail: 'BECAME_CROWN_COLONY'}]->(b)
DELETE r;

// BECAME_COLONY
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type IN ['BECAME_COLONY', 'FORMALIZED_AS_COLONY']
CREATE (a)-[:BECAME_COLONY {description: r.description, year: r.year, detail: r.relationship_type}]->(b)
DELETE r;

// BECAME_PROTECTORATE
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'BECAME_PROTECTORATE'
CREATE (a)-[:BECAME_PROTECTORATE {description: r.description, year: r.year, detail: 'BECAME_PROTECTORATE'}]->(b)
DELETE r;

// BECAME_MANDATE
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'BECAME_MANDATE'
CREATE (a)-[:BECAME_MANDATE {description: r.description, year: r.year, detail: 'BECAME_MANDATE'}]->(b)
DELETE r;

// BECAME_SEPARATE_COLONY
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'BECAME_SEPARATE_COLONY'
CREATE (a)-[:BECAME_SEPARATE_COLONY {description: r.description, year: r.year, detail: 'BECAME_SEPARATE_COLONY'}]->(b)
DELETE r;

// BECAME_SELF_GOVERNING
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'BECAME_SELF_GOVERNING'
CREATE (a)-[:BECAME_SELF_GOVERNING {description: r.description, year: r.year, detail: 'BECAME_SELF_GOVERNING'}]->(b)
DELETE r;

// FEDERATED_INTO (absorbs CONFEDERATED_INTO, JOINED_FEDERATION, JOINED_CONFEDERATION, JOINED)
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type IN ['FEDERATED_INTO', 'CONFEDERATED_INTO', 'JOINED_FEDERATION', 'JOINED_CONFEDERATION', 'JOINED']
CREATE (a)-[:FEDERATED_INTO {description: r.description, year: r.year, detail: r.relationship_type}]->(b)
DELETE r;

// PARTITIONED_INTO (absorbs PARTITIONED_TO, SEPARATED_INTO, CARVED_OUT, SEPARATED_FROM, SEPARATED_FROM_INDIA)
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type IN ['PARTITIONED_INTO', 'PARTITIONED_TO', 'SEPARATED_INTO', 'CARVED_OUT', 'SEPARATED_FROM', 'SEPARATED_FROM_INDIA']
CREATE (a)-[:PARTITIONED_INTO {description: r.description, year: r.year, detail: r.relationship_type}]->(b)
DELETE r;

// TRANSFERRED_SOVEREIGNTY (absorbs TRANSFERRED_TO_CROWN, TRANSFERRED_TO_AUSTRALIA, CONQUERED_BY, CONQUERED_AND_RENAMED, RETURNED_TO, RESTORED_TO_CROWN, ANNEXED_BY)
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type IN ['TRANSFERRED_TO_CROWN', 'TRANSFERRED_TO_AUSTRALIA', 'CONQUERED_BY', 'CONQUERED_AND_RENAMED', 'RETURNED_TO', 'RESTORED_TO_CROWN', 'ANNEXED_BY']
CREATE (a)-[:TRANSFERRED_SOVEREIGNTY {description: r.description, year: r.year, detail: r.relationship_type}]->(b)
DELETE r;

// REUNITED_INTO
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'REUNITED_INTO'
CREATE (a)-[:REUNITED_INTO {description: r.description, year: r.year, detail: 'REUNITED_INTO'}]->(b)
DELETE r;

// Catch remaining rare types on EVOLVED_INTO
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type IS NOT NULL
  AND r.relationship_type NOT IN ['land_border', 'coastal_proximity', 'DIRECT_SUCCESSION',
    'INDEPENDENCE_GRANTED', 'INDEPENDENCE_RESTORED', 'INTERNAL_SETTLEMENT',
    'EXPANDED_TO', 'EXPANDED_WITH_PROTECTORATE', 'CONSOLIDATED_AS_PROVINCE',
    'BECAME_PART_OF', 'FEDERATION_SUCCESSION']
CREATE (a)-[:EVOLVED_INTO {description: r.description, year: r.year, detail: r.relationship_type}]->(b)
DELETE r;

// Handle remaining edge cases individually
MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'INDEPENDENCE_GRANTED'
CREATE (a)-[:BECAME_INDEPENDENT {description: r.description, year: r.year, detail: 'INDEPENDENCE_GRANTED'}]->(b)
DELETE r;

MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'INDEPENDENCE_RESTORED'
CREATE (a)-[:BECAME_INDEPENDENT {description: r.description, year: r.year, detail: 'INDEPENDENCE_RESTORED'}]->(b)
DELETE r;

MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'FEDERATION_SUCCESSION'
CREATE (a)-[:FEDERATED_INTO {description: r.description, year: r.year, detail: 'FEDERATION_SUCCESSION'}]->(b)
DELETE r;

MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'EXPANDED_TO'
CREATE (a)-[:REORGANIZED_AS {description: r.description, year: r.year, detail: 'EXPANDED_TO'}]->(b)
DELETE r;

MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'EXPANDED_WITH_PROTECTORATE'
CREATE (a)-[:REORGANIZED_AS {description: r.description, year: r.year, detail: 'EXPANDED_WITH_PROTECTORATE'}]->(b)
DELETE r;

MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'CONSOLIDATED_AS_PROVINCE'
CREATE (a)-[:REORGANIZED_AS {description: r.description, year: r.year, detail: 'CONSOLIDATED_AS_PROVINCE'}]->(b)
DELETE r;

MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'BECAME_PART_OF'
CREATE (a)-[:MERGED_INTO {description: r.description, year: r.year, detail: 'BECAME_PART_OF'}]->(b)
DELETE r;

MATCH (a)-[r:EVOLVED_INTO]->(b)
WHERE r.relationship_type = 'INTERNAL_SETTLEMENT'
CREATE (a)-[:REORGANIZED_AS {description: r.description, year: r.year, detail: 'INTERNAL_SETTLEMENT'}]->(b)
DELETE r;

// ── PHASE 3b: Refactor SUCCESSOR_TO relationships ──
// These mirror EVOLVED_INTO but in reverse direction. Same treatment.

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type = 'BECAME_INDEPENDENT'
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: 'BECAME_INDEPENDENT', succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type IN ['MERGED_INTO', 'MERGED_WITH', 'AMALGAMATED_INTO']
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: r.relationship_type, succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type = 'INCORPORATED_INTO'
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: 'INCORPORATED_INTO', succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type IN ['REORGANIZED_AS', 'RENAMED_TO']
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: r.relationship_type, succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type = 'BECAME_CROWN_COLONY'
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: 'BECAME_CROWN_COLONY', succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type IN ['BECAME_COLONY', 'FORMALIZED_AS_COLONY']
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: r.relationship_type, succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type = 'BECAME_PROTECTORATE'
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: 'BECAME_PROTECTORATE', succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type = 'BECAME_MANDATE'
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: 'BECAME_MANDATE', succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type = 'BECAME_SEPARATE_COLONY'
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: 'BECAME_SEPARATE_COLONY', succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type = 'BECAME_SELF_GOVERNING'
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: 'BECAME_SELF_GOVERNING', succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type IN ['FEDERATED_INTO', 'CONFEDERATED_INTO', 'JOINED_FEDERATION', 'JOINED_CONFEDERATION', 'JOINED', 'FEDERATION_SUCCESSION']
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: r.relationship_type, succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type IN ['PARTITIONED_INTO', 'PARTITIONED_TO', 'SEPARATED_INTO', 'CARVED_OUT', 'SEPARATED_FROM', 'SEPARATED_FROM_INDIA']
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: r.relationship_type, succession_type: r.succession_type}]->(b)
DELETE r;

MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type IN ['TRANSFERRED_TO_CROWN', 'TRANSFERRED_TO_AUSTRALIA', 'CONQUERED_BY', 'CONQUERED_AND_RENAMED', 'RETURNED_TO', 'RESTORED_TO_CROWN', 'ANNEXED_BY']
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: r.relationship_type, succession_type: r.succession_type}]->(b)
DELETE r;

// Catch any remaining SUCCESSOR_TO with relationship_type
MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type IS NOT NULL
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year, detail: r.relationship_type, succession_type: r.succession_type}]->(b)
DELETE r;

// Clean remaining bare SUCCESSOR_TO (no relationship_type property)
MATCH (a)-[r:SUCCESSOR_TO]->(b)
WHERE r.relationship_type IS NULL
CREATE (a)-[:SUCCEEDED {description: r.description, year: r.year}]->(b)
DELETE r;

// ── PHASE 3c: Clean up BORDERS_WITH and NEAR_COAST_OF ──
// Remove the redundant relationship_type property

MATCH ()-[r:BORDERS_WITH]->()
WHERE r.relationship_type IS NOT NULL
REMOVE r.relationship_type;

MATCH ()-[r:NEAR_COAST_OF]->()
WHERE r.relationship_type IS NOT NULL
REMOVE r.relationship_type;

// ── PHASE 4: Data type casting ──

// Cast string latitudes to float
MATCH (c:HistoricalTerritory)
WHERE c.latitude IS NOT NULL AND apoc.meta.cypher.type(c.latitude) = 'STRING'
SET c.latitude = toFloat(c.latitude);

// Cast string longitudes to float
MATCH (c:HistoricalTerritory)
WHERE c.longitude IS NOT NULL AND apoc.meta.cypher.type(c.longitude) = 'STRING'
SET c.longitude = toFloat(c.longitude);

// Add native spatial point (requires both lat/lon as floats)
MATCH (c:HistoricalTerritory)
WHERE c.latitude IS NOT NULL AND c.longitude IS NOT NULL
SET c.location = point({latitude: toFloat(c.latitude), longitude: toFloat(c.longitude)});

// ── PHASE 5: Princely State established_year → dynasty_founded ──

MATCH (c:PrincelyState)
WHERE c.established_year IS NOT NULL
SET c.dynasty_founded = c.established_year
REMOVE c.established_year;

// ── PHASE 6: Resolve QID-only node names ──
// These 18 nodes had only Wikidata QIDs as names. Resolved via Wikipedia.

MATCH (c:HistoricalTerritory {wikidata_id: 'Q101242542'}) SET c.name = 'Kadana State';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q104152112'}) SET c.name = 'Surat State';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q104152114'}) SET c.name = 'Yasin State';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q11904734'}) SET c.name = 'Alaniawas';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q11905355'}) SET c.name = 'Ammayanayakan';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q11905439'}) SET c.name = 'Anakapalle';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q11905698'}) SET c.name = 'Antarbella';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q11908900'}) SET c.name = 'Bedam';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q131080302'}) SET c.name = 'Sudasana State';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q134436280'}) SET c.name = 'Bilkha';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q1632695'}) SET c.name = 'Sanjeli State';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q21044436'}) SET c.name = 'Edappalli';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q21075438'}) SET c.name = 'Gopalpet';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q21075439'}) SET c.name = 'Kaddatanad';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q48838868'}) SET c.name = 'Tharad State';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q48838869'}) SET c.name = 'Wao State';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q48838872'}) SET c.name = 'Santalpur State';
MATCH (c:HistoricalTerritory {wikidata_id: 'Q48838989'}) SET c.name = 'Sarila State';

// ── PHASE 7: Update constraints for new label structure ──

// Drop old constraint
DROP CONSTRAINT colony_id_unique IF EXISTS;

// Create new constraint on base label
CREATE CONSTRAINT territory_id_unique IF NOT EXISTS
FOR (n:HistoricalTerritory) REQUIRE n.colony_id IS UNIQUE;

// ── PHASE 7: Remove redundant colony_type property for Princely States ──
// (The label :PrincelyState now carries this information)
// Keep administrative_status as-is for other nodes since it has more variety.

// Done. Verify with:
// MATCH (n) RETURN labels(n), count(n) ORDER BY count(n) DESC;
// MATCH ()-[r]->() RETURN type(r), count(r) ORDER BY count(r) DESC;

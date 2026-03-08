# Knowledge Graph Data Fixes

Issues identified via the empire timeline visualization. To be addressed in a future pass.

## Missing Edges (fixed 2026-03-06)
- Newfoundland (1497) -> Colony of Newfoundland (1610) -> Dominion of Newfoundland (1907): added EVOLVED_INTO chain
- Saint Lucia Colony: added WAS_MEMBER_OF -> British Windward Islands
- 13 American colonies: added EVOLVED_INTO -> United States of America (new node created, QID Q30)

## Deleted Nodes (fixed 2026-03-06)
- "Australia" (1901-1942): duplicate of "Commonwealth of Australia" (1901-ongoing), same QID Q408. Deleted.

## Deleted Edges (fixed 2026-03-06)
- Fiji <-> Western Australia (NEAR_COAST_OF): bogus geographic edge, Fiji is not near WA

## Date Corrections (fixed 2026-03-06)
- Indian Empire (British Raj): established_year was 1613, corrected to 1858 (Crown takeover from EIC)

## Hierarchy (PART_OF) Edges Added (fixed 2026-03-06)
- 15 Indian provinces/presidencies PART_OF Indian Empire (British Raj)
- Manitoba (1870), Northwest Territories (1870) PART_OF Dominion of Canada
- EIC -> Raj -> Dominion of India / Dominion of Pakistan (EVOLVED_INTO)

## Pending: North America Lineage (identified 2026-03-06)
- DELETE "Canada (French Colony)" (1608-1763, Q2569593): duplicate of New France, same dates, no edges
- ADD EDGE: New France (1608-1763) EVOLVED_INTO Province of Quebec (British) (1763-1791) — Treaty of Paris 1763
- ADD EDGE: Acadia (1604-1713) EVOLVED_INTO Nova Scotia (1713-1867) — Treaty of Utrecht 1713
- ADD EDGE: Nova Scotia PARTITIONED_INTO New Brunswick (1784) — carved out of Nova Scotia
- ADD NODE: Nova Scotia (Scottish Charter) (1621-1632, Q1854755) — Sir William Alexander's grant
- ADD EDGE: Nova Scotia (Scottish Charter) EVOLVED_INTO Nova Scotia
- FIX: Nova Scotia established_year 1621 -> 1713 (1621 is the Scottish charter, not British colony)
- MERGE "America" region into "North America" across all affected nodes
- RENAME "Canada, Dominion of" → "Dominion of Canada"
- FIX: Dominion of Canada ind = 1931 (Statute of Westminster); add successor node "Canada" (1931-ongoing, type=Independence)
- ADD NODE: Red River Colony (1811-1870, Q1143638) — Selkirk Settlement
- ADD EDGE: Rupert's Land PARTITIONED_INTO Red River Colony
- ADD EDGE: Rupert's Land PARTITIONED_INTO North-Western Territory (shared HBC administration)
- ADD EDGE: Rupert's Land EVOLVED_INTO Dominion of Canada (absorbed 1870)
- ADD EDGE: Red River Colony EVOLVED_INTO Dominion of Canada
- ADD EDGE: North-Western Territory EVOLVED_INTO Dominion of Canada
- SPLIT Nova Scotia into pre-partition (1713-1784) and post-partition (1784-1867) nodes
- ADD EDGE: Nova Scotia (pre) PARTITIONED_INTO Nova Scotia (post) + New Brunswick
- ADD EDGE: Île Royale EVOLVED_INTO Nova Scotia (pre) — Treaty of Paris 1763
- Newfoundland chain edges missing from export: Newfoundland → Colony of Newfoundland → Dominion of Newfoundland → Canada

## Pending: Caribbean Data Issues (identified 2026-03-06)
- FIX: Leeward Islands Colony ind = 1816 (was 1956 in data, reorganized into sub-units in 1816)
- FIX: British Leeward Islands (federal_colony_leeward_islands_1833-1960) ind = 1960, type = 'Federal Colony' (was null/empty)
- FIX: Antigua Colony ind = 1981 (independence as Antigua and Barbuda; was null)
- FIX: Saint Kitts and Nevis Colony node ID says 1958 but est=1624; ID should be regenerated
- FIX: Trinidad and Tobago Colony (1797-1962) → rename to "Trinidad Colony", set ind=1888 (pre-unification)
- FIX: Trinidad and Tobago (1889-1962) → rename to "Colony of Trinidad and Tobago" (unified Crown Colony)
- DELETE EDGE: West Indies Federation → Trinidad and Tobago (membership, not succession; T&T was a WIF member but the federation didn't evolve into T&T)
- DELETE EDGE: West Indies Federation → Jamaica (membership, not succession; Jamaica existed 307 years before WIF)
- NOTE: Newfoundland (1497-1949) removed from viz — 1497 is Cabot's arrival, not a colony. Colony of Newfoundland (1610) is the true start.
- NOTE: Louisiana (French, 1682-1762) removed from viz — never British territory

## Pending: Caribbean Edge Fixes (identified 2026-03-07)
- FIX EDGE TYPE: Leeward Islands Colony → Antigua-Barbuda-Montserrat: PARTITIONED_INTO (colony split into two sub-groupings, not simple succession)
- FIX EDGE TYPE: Leeward Islands Colony → St Kitts-Nevis-Anguilla: PARTITIONED_INTO (same reason)
- FIX ID: settlement_of_belize_1798_1862 — DATA_FIXES was referencing wrong ID (english_settlement_of_belize_1798), corrected
- NOTE: WIF (1958-1962) and British Windward Islands (1833-1959) are administrative groupings — membership, not succession. No outbound edges appropriate.
- NOTE: Most individual Caribbean colonies (Antigua, Barbados, Jamaica, Grenada, etc.) are standalone — no succession relationships. This is historically correct.

## Pending: Caribbean QID Issues (identified 2026-03-06)
- DUPLICATE QID Q1796551: shared by Leeward Islands Colony (1671-1816) and British Leeward Islands (1833-1960) — distinct entities, earlier one needs own QID
- DUPLICATE QID Q116282722: shared by Trinidad Colony (1797-1888) and Colony of Trinidad and Tobago (1889-1962) — pre-union Trinidad needs separate QID
- WRONG QID: St. Vincent Colony uses Q757 (modern nation SVG, independent 1979) — colonial entity needs different QID
- STALE ID: saint_christopher_nevis_anguilla_1958_1983 encodes 1958 but est=1624 — regenerate ID
- MISSING TYPE: British Leeward Islands (federal_colony_leeward_islands_1833-1960) has empty type field — should be "Federal Colony"

## Deleted Nodes — Africa Duplicates (fixed 2026-03-06)
- Uganda Protectorate (1894-1962): exact duplicate of Uganda (Q1097943), same dates — deleted
- Somaliland Protectorate (1884-1960): exact duplicate of British Somaliland (Q662653), same dates — deleted
- Anglo-Egyptian Sudan (1899-1956): exact duplicate of Sudan, Anglo-Egyptian (Q541455), same dates — deleted
- James Island (Gambia) (1661-1779): duplicate of James Island Trading Post (1661-1816), shorter dates, no edges — deleted

## Deleted Nodes — Africa Envelope Bars (fixed 2026-03-06)
- Southern Rhodesia (1901-1980): overlapping envelope bar, edges redirected through Southern Rhodesia Colony (1923-1953)
- Northern Rhodesia (1911-1964): overlapping envelope bar, edges redirected through Northern Rhodesia Colony (1924-1953)

## Deleted Edges — Africa (fixed 2026-03-06)
- Cape Colony (British) → Natalia Republic: backwards flow (1910→1839), Cape annexed Natalia, not evolved into it
- Cape Colony (British) → Orange River Sovereignty: backwards flow (1910→1848), same issue
- Federation of Rhodesia and Nyasaland → Rhodesia (UDI): should flow through Southern Rhodesia Colony

## Deleted Edges — West Africa Nigeria Cluster (fixed 2026-03-06)
- Lagos Protectorate → Southern Nigeria Protectorate: duplicate edge (×2 in data), deleted one copy
- Southern Nigeria Protectorate → Colony and Protectorate of Nigeria: duplicate edge (×2 in data), deleted one copy
- Southern Nigeria Protectorate → Northern Nigeria: wrong edge — these were concurrent parallel protectorates (both 1900-1914), not succession; both merged into Colony of Nigeria in 1914

## Missing Edges — Africa (fixed 2026-03-06)
- Ashanti (1901-1957) EVOLVED_INTO Gold Coast Colony (1874-1957) — merged into Ghana at independence
- British Togoland (1919-1957) EVOLVED_INTO Gold Coast Colony (1874-1957) — UN plebiscite, joined Gold Coast for Ghana independence

## Added Edges — Africa (fixed 2026-03-06)
- Federation → Northern Rhodesia Colony (PARTITIONED_INTO)
- Federation → Nyasaland post-federation (PARTITIONED_INTO)
- Federation → Southern Rhodesia Colony (PARTITIONED_INTO)
- Southern Rhodesia Colony → Rhodesia (UDI) (EVOLVED_INTO)

## Date Fixes — Africa (fixed 2026-03-06)
- Northern Rhodesia Colony: ind 1953 → 1964 (continued to independence, not just federation end)
- Southern Rhodesia Colony: ind 1953 → 1965 (continued as self-governing until UDI)

## Region Split — Africa (fixed 2026-03-06)
- Monolithic "Africa" region (81 nodes) split into 5 sub-regions:
  - Southern Africa (30), West Africa (22), East Africa (13), North-East Africa (5), Africa (Islands) (11)

## Possible Duplicates
- Newfoundland (1497-1949) vs Colony of Newfoundland (1610-1949): overlapping, may need merge or clearer delineation

## Missing End Dates (fixed 2026-03-06)
- Canada (French Colony): was null, set to 1763
- Acadia: was null, set to 1713
- United Colony of British Columbia: was null, set to 1871
- English settlement of Belize: was null, set to 1862

## Region Corrections (fixed 2026-03-06)
- 13 American colonies: moved from "America" to "North America"
- Bermuda: moved to "Atlantic"
- British Guiana: moved to "South America"
- Belize/British Honduras: moved to "Caribbean"

## Null Data (fixed 2026-03-06)
- Colony of Antigua-Barbuda-Montserrat: had null canonical_name and established_year
- Colony of St. Kitts-Nevis-Anguilla: had null canonical_name and established_year

## Pending: Southern Africa (identified 2026-03-07)
- REMOVE EDGE: Cape Colony (British) → Natalia Republic (Cape didn't partition into Natalia; Natalia was a Boer republic, Cape annexed it)
- REMOVE EDGE: Cape Colony (British) → Orange River Sovereignty (ORS was proclaimed over trans-Orange territory, not Cape territory)
- ADD EDGE: Cape Colony (British) → Orange River Sovereignty (PARTITIONED_INTO) — REMOVED, historically wrong: ORS was not Cape territory
- FIX TYPE: BSAC Territory → Southern Rhodesia Colony: PARTITIONED_INTO (not EVOLVED_INTO) — territory was split
- FIX TYPE: BSAC Territory → Northern Rhodesia Colony: PARTITIONED_INTO (not EVOLVED_INTO) — territory was split
- FIX: Nyasaland ind = 1953 (joined Federation; post-federation node covers 1963-1964)
- FIX: Nyasaland post-federation est = 1963 (was 1964; Federation dissolved 1963)
- MOVE: Nyasaland, British Central Africa Protectorate, Nyasaland post-federation → Southern Africa (were East Africa; part of Rhodesia/Federation lineage)
- NOTE: Boer Republics (OFS, SAR, Natalia) and Dutch Colonies should have distinct visual type to differentiate from British entities
- NOTE: Griqualand West, British Bechuanaland, Zululand are absorptions into Cape Colony / Colony of Natal — flow renders at absorption year, not target est

## Pending: West Africa (identified 2026-03-07)
- FIX: Sierra Leone Colony and Protectorate est = 1896 (was 1787; 1787 is Province of Freedom date, protectorate declared 1896)
- FIX EDGE TYPE: Gold Coast Colony → Ashanti should be PARTITIONED_INTO (Ashanti administered under Gold Coast, not predecessor)
- FIX EDGE TYPE: Gold Coast Colony → British Togoland should be PARTITIONED_INTO (mandate administered under Gold Coast)
- REMOVE OLD EDGES: Ashanti → Gold Coast Colony and British Togoland → Gold Coast Colony (were EVOLVED_INTO; direction was wrong)

## Pending: North America (identified 2026-03-07)
- ADD NODE: United States of America (1776-ongoing, Q30, type=Independence)
- ADD EDGES: 13 colonies EVOLVED_INTO United States
- ADD NODE: Newfoundland Commission of Government (1934-1949, Q48378, type=Crown Colony)
- FIX: Colony of Newfoundland ind = 1907 (was 1949; became Dominion in 1907)
- ADD EDGE: Dominion of Newfoundland → Newfoundland Commission → Canada (was Dominion → Canada directly)
- FIX: Mainland British Columbia ind = 1866 (was 1871; merged with Vancouver Island in 1866)
- REMOVE EDGE: Vancouver Island → Mainland BC (concurrent colonies that merged, not succession)
- REMOVE EDGE: Mainland BC → Dominion of Canada (United Colony joined Confederation, not Mainland)
- DELETE: Canada (French Colony) — duplicate of New France, same dates
- FIX: New Hampshire Colony est = 1629 (was 1623; 1623 is Pannaway fishing settlement, 1629 is John Mason's province grant from Council for New England)

## Pending: Pacific / Australia (identified 2026-03-07)
- DELETE: Northern Territory (1911-ongoing) — internal Australian territory, not a British colony
- DELETE: Australian Capital Territory (1911-ongoing) — internal federal territory, not a British colony
- DELETE: Australia (1901-1942) — duplicate of Commonwealth of Australia (same QID Q408)
- REMOVE EDGE: South Australia → Northern Territory (federal admin transfer, not colonial succession)
- FIX EDGE TYPE: NSW → Van Diemen's Land: PARTITIONED_INTO (NSW continued after carving out VDL)
- FIX EDGE TYPE: NSW → Victoria: PARTITIONED_INTO (NSW continued)
- FIX EDGE TYPE: NSW → Queensland: PARTITIONED_INTO (NSW continued)
- FIX: Commonwealth of Australia ind = 1942 (Statute of Westminster Adoption Act; Dominion status ended)
- ADD NODE: Australia (1942-ongoing, Q408, type=Independence) — fully independent
- ADD EDGE: Commonwealth of Australia → Australia (EVOLVED_INTO)
- ADD NODE: New Zealand (1947-ongoing, Q664, type=Independence) — adopted Statute of Westminster
- ADD EDGE: New Zealand Colony/Dominion → New Zealand independent (EVOLVED_INTO)
- RENAME: New South Wales (Original) → New South Wales (drop "(Original)" — it's just NSW)
- NOTE: 23 Guano Island / Whaling Station / Remote Island nodes with no edges clutter the Pacific view — consider filtering or grouping
- NOTE: French predecessor colonies (New France, Acadia, Île Royale) should have distinct visual type as non-British entities

## Pending: Southeast Asia (identified 2026-03-07)
- DELETE: Singapore (1824-1965) — envelope bar overlapping Singapore Settlement (1819) + Singapore Crown Colony (1946)
- DELETE: Malaya (1824-1963) — envelope bar overlapping Straits Settlements + Malayan Union + Federation of Malaya
- ADD NODE: Malaysia (1963-ongoing, Q833, type=Independence) — formed from Malaya + Singapore + North Borneo + Sarawak + Labuan
- ADD NODE: Singapore (1965-ongoing, Q334, type=Independence) — separated from Malaysia
- ADD EDGES: Malaya (Independent) + Singapore Crown Colony + North Borneo Crown Colony + Sarawak Crown Colony + Labuan → Malaysia (all EVOLVED_INTO)
- ADD EDGE: Malaysia → Singapore (PARTITIONED_INTO) — Singapore expelled/separated 1965
- FIX EDGE TYPE: Straits Settlements → Singapore Crown Colony: PARTITIONED_INTO (Straits dissolved 1946; peninsular parts → Malayan Union, Singapore → Crown Colony)
- NOTE: Brunei declined to join Malaysia in 1963; remains standalone protectorate → independence (1984)

## Pending: East Africa (identified 2026-03-07)
- REMOVE EDGE: Tanganyika Territory → Zanzibar (EVOLVED_INTO): wrong — Zanzibar (1890) predates Tanganyika (1922); they are independent lineages that merge in 1964
- ADD NODE: Tanzania (1964-ongoing, Q924, type=Independence) — merger of Tanganyika + Zanzibar
- ADD EDGES: Tanganyika (independent, 1961-1964) + Zanzibar (independent, 1963-1964) → Tanzania (both EVOLVED_INTO)
- NOTE: German East Africa (Military Administration, 1916-1922) should be styled as non-British entity (foreign territory under military occupation)

## Deleted Nodes — South America (fixed 2026-03-07)
- British Guyana (british_guyana_1831_1966, est=1763): duplicate of British Guiana (british_guiana_1831_1966, est=1831). Wrong spelling ("Guyana" vs "Guiana"), wrong est (1763 is Dutch cession date, not colony establishment).

## Pending: Middle East (identified 2026-03-07)
- NOTE: Aden Province (1839-1937) → Aden Colony (1937-1967) edge already added (EVOLVED_INTO, admin upgrade)
- NOTE: Aden Protectorate (1869-1967) is a separate entity (hinterland tribal areas), not a partition of Aden Province
- NOTE: Mesopotamia (Br. Occupied, Military Administration) styled as non-British — correct for temporary military occupation of Ottoman territory
- NOTE: Kuwait Protectorate and Mandatory Palestine already removed as duplicates

## Added Nodes — Europe (fixed 2026-03-07)
- ADD NODE: Minorca (1st British, 1708-1756, Q173095) — captured in War of Spanish Succession, lost to France
- ADD NODE: Minorca (2nd British, 1763-1782, Q173095) — restored by Treaty of Paris, lost to Spain in siege
- ADD NODE: Minorca (3rd British, 1798-1802, Q173095) — recaptured, returned by Treaty of Amiens
- ADD EDGES: Minorca 1st → 2nd → 3rd (EVOLVED_INTO) — same island recaptured
- ADD NODE: Anglo-Corsican Kingdom (1794-1796, Q2259576) — brief British protectorate under George III
- ADD NODE: Heligoland (1807-1890, Q3104) — captured from Denmark, ceded to Germany (Heligoland-Zanzibar Treaty)
- ADD NODE: Kingdom of Ireland (1541-1801, Q179876) — Henry VIII declared King; ended with Acts of Union
- ADD NODE: Ireland (UK, 1801-1922, Q174193) — United Kingdom of GB&I; ended with partition
- ADD NODE: Irish Free State (1922-1937, Q31747, type=Dominion) — Anglo-Irish Treaty; became Republic
- ADD NODE: Northern Ireland (1920-ongoing, Q26) — remained in UK after partition
- ADD EDGES: Kingdom of Ireland → Ireland (UK) (EVOLVED_INTO); Ireland (UK) → Irish Free State + Northern Ireland (PARTITIONED_INTO)

## Confirmed OK: Africa (Islands), Atlantic, Antarctica (reviewed 2026-03-07)
- Isle de France → Mauritius → Seychelles chain: correct
- All Antarctic whaling stations and remote islands: standalone, no succession — correct
- Falklands and St Helena group: ongoing BOTs, standalone — correct

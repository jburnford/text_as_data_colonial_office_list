// British Empire Knowledge Graph — Territory nodes and relationships
// Exported from Neo4j, cleaned on 2026-03-09
//
// Node labels: HistoricalTerritory (base), Colony, CrownColony, Protectorate,
//   Dominion, Mandate, PrincelyState, IndependentNation, Federation,
//   Province, CompanyTerritory, MinorTerritory, BoerRepublic, etc.
//
// To import: run this file in Neo4j Browser or cypher-shell

// ── Constraints ──
CREATE CONSTRAINT territory_id_unique IF NOT EXISTS FOR (n:HistoricalTerritory) REQUIRE n.colony_id IS UNIQUE;

// ── Territory Nodes ──

MERGE (c:HistoricalTerritory:Colony {colony_id: 'acadia_french_1604_1713'})
SET c += {
  administrative_status: 'Colonial Territory',
  canonical_name: 'Acadia',
  colony_id: 'acadia_french_1604_1713',
  colony_type: 'Colonial Territory',
  comments: 'French colony in Maritime provinces, ceded to Britain 1713. End date: Treaty of Utrecht 1713.',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T16:50:25',
  end_date: '1713-04-11',
  established_year: 1604,
  independence_year: 1713,
  latitude: 46.81666667,
  link_status: 'verified',
  longitude: -71.2,
  modern_nation_qids: ['Q16'],
  name: 'Acadia (French)',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'French Colonial System',
  spatial_updated: '2025-07-21T10:19:47',
  start_date: '1604-06-26',
  verified: true,
  verified_date: '2025-08-05T20:04:03.412000000+00:00',
  whg_aat_types: ['300387506'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q207353'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'aden_1839_1963'})
SET c += {
  administrative_status: 'Colony/Protectorate',
  canonical_name: 'Aden Province',
  colony_id: 'aden_1839_1963',
  colony_type: 'Colony/Protectorate',
  comments: '',
  created_date: '2025-07-19T18:39:07.944245',
  end_date: '1937-03-31',
  established_year: 1839,
  independence_year: 1937,
  latitude: 12.8,
  longitude: 45.0333,
  modern_nation_qids: ['Q805'],
  name: 'Aden Province',
  region: 'Middle East',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1839-01-01',
  transition_type: 'federation',
  verified: true,
  verified_date: '2025-08-05T20:18:40.536000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['YE'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q17509767'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'aden_colony_1937_1967'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Aden Colony',
  colony_id: 'aden_colony_1937_1967',
  colony_type: 'Crown Colony',
  comments: 'Strategic port at entrance to Red Sea, key refueling station',
  created_date: '2025-07-19T22:11:19',
  end_date: '1967-11-30',
  established_year: 1937,
  independence_year: 1967,
  latitude: 12.8,
  longitude: 45.0333,
  modern_nation_qids: ['Q805'],
  name: 'Aden Colony',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1937-04-01',
  verified: true,
  verified_date: '2025-08-05T20:19:40.904000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['YE'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q49910'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'aden_protectorate_1839_1967'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Aden Protectorate',
  colony_id: 'aden_protectorate_1839_1967',
  colony_type: 'Protectorate',
  comments: 'Protected tribal areas around Aden colony',
  created_date: '2025-07-19T22:11:19',
  end_date: '1967-11-30',
  established_year: 1869,
  independence_year: 1967,
  modern_nation_qids: ['Q805'],
  name: 'Aden Protectorate',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1869-01-01',
  verified: true,
  verified_date: '2025-08-05T20:21:41.260000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['YE'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1865132'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'ajmer_merwara_1818_1947'})
SET c += {
  canonical_name: 'Ajmer-Merwara',
  colony_id: 'ajmer_merwara_1818_1947',
  established_year: 1818,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Province',
  wikidata_id: 'Q4700553'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'alberta_1905'})
SET c += {
  canonical_name: 'Alberta',
  colony_id: 'alberta_1905',
  colony_type: 'Province',
  established_year: 1905,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1951'
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'aldabra_islands_1903_1965'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Aldabra Islands',
  colony_id: 'aldabra_islands_1903_1965',
  colony_type: 'Dependency',
  comments: 'Dependency of Seychelles, transferred to BIOT then back to Seychelles',
  created_date: '2025-07-19T23:25:07',
  end_date: '1965-11-08',
  established_year: 1903,
  independence_year: 1965,
  link_status: 'verified',
  modern_nation_qids: ['Q1042'],
  name: 'Aldabra Islands',
  qid_type: 'geographical',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  start_date: '1903-08-31',
  verified: true,
  verified_date: '2025-08-05T20:24:56.722000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SC'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1426882'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'andaman_and_nicobar_islands_1789_1947'})
SET c += {
  canonical_name: 'Andaman and Nicobar Islands',
  colony_id: 'andaman_and_nicobar_islands_1789_1947',
  established_year: 1789,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Province',
  wikidata_id: 'Q40888'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'anguilla_1650_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Anguilla',
  colony_id: 'anguilla_1650_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Still British Overseas Territory',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:09:32',
  established_year: 1650,
  latitude: 18.227222222,
  link_status: 'verified',
  longitude: -63.048888888,
  modern_nation_qids: ['Q25228'],
  name: 'Anguilla',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: '2025-07-21T10:19:47',
  start_date: '1650-01-01',
  verified: true,
  verified_date: '2025-08-05T20:27:14.710000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q25228'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'antigua_colony_1632_1981'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Antigua Colony',
  colony_id: 'antigua_colony_1632_1981',
  colony_type: 'Crown Colony',
  comments: 'Part of Leeward Islands federation, sugar plantation economy',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T12:11:28',
  end_date: '1981-11-01',
  established_year: 1632,
  independence_year: 1981,
  latitude: 17.085,
  link_status: 'verified',
  longitude: -61.8,
  modern_nation_qids: ['Q781'],
  name: 'Antigua Colony',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Comprehensive Missing Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1632-01-01',
  verified: true,
  verified_date: '2025-08-05T20:29:09.886000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q22007334'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'antigua_montserrat_barbuda_1816_1833'})
SET c += {
  canonical_name: 'Colony of Antigua-Barbuda-Montserrat',
  colony_id: 'antigua_montserrat_barbuda_1816_1833',
  colony_type: 'Crown Colony',
  end_date: '1833-01-01',
  established_year: 1816,
  independence_year: 1833,
  modern_nation_qids: ['Q781'],
  name: 'Colony of Antigua-Barbuda-Montserrat',
  region: 'Caribbean',
  source: 'Manual Correction',
  start_date: '1816-01-01',
  verified: true,
  verified_date: '2025-08-06T02:08:47.163000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AG'],
  whg_fclasses: ['A']
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'ascension_island_1815_ongoing'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Ascension Island',
  colony_id: 'ascension_island_1815_ongoing',
  colony_type: 'Dependency',
  comments: 'Dependency of St. Helena, strategic naval station',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T23:25:07',
  established_year: 1815,
  latitude: -7.95,
  link_status: 'verified',
  longitude: -14.35,
  modern_nation_qids: ['Q192184'],
  name: 'Ascension Island',
  qid_type: 'historical_colony',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1815-10-22',
  verified: true,
  verified_date: '2025-08-05T20:54:32.235000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q46197'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'ashanti_1901_1957'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Ashanti',
  colony_id: 'ashanti_1901_1957',
  colony_type: 'Crown Colony',
  comments: 'Became a part of the dominion of Ghana',
  created_date: '2025-07-19T18:39:07.554455',
  end_date: '1957-01-01',
  established_year: 1901,
  independence_year: 1957,
  link_status: 'verified',
  modern_nation_qids: ['Q117'],
  name: 'Ashanti',
  qid_type: 'historical_colony',
  region: 'West Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1901-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-05T20:56:33.692000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GH'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q96372444'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'assam_bengal_presidency_1826_1874'})
SET c += {
  administrative_status: 'Division of a Presidency',
  canonical_name: 'Assam (Bengal Presidency)',
  colony_id: 'assam_bengal_presidency_1826_1874',
  colony_type: 'Province of British India',
  comments: 'Acquired by Britain in the Treaty of Yandabo and administered as part of the Bengal Presidency.',
  coordinates_source: 'wikidata_batch',
  created_date: '1826-01-01',
  end_date: '1874-02-06',
  established_year: 1826,
  independence_year: 1874,
  modern_nation_qids: ['Q668'],
  name: 'Assam (Bengal Presidency)',
  region: 'South Asia',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1826-02-24',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-05T22:11:50.906000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5148287'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'assam_province_1874_1905'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Assam Province (1874-1905)',
  colony_id: 'assam_province_1874_1905',
  colony_type: 'Province',
  comments: 'Assam as a separate Chief Commissioner\'s Province until the 1905 Partition of Bengal.',
  created_date: '2025-07-19T21:53:26',
  end_date: '1905-10-16',
  established_year: 1874,
  independence_year: 1905,
  modern_nation_qids: ['Q668'],
  name: 'Assam Province (1874-1905)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1874-02-07',
  verified: true,
  verified_date: '2025-08-05T22:11:50.906000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q17513379'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'assam_province_restored_1912_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Assam Province (Restored)',
  colony_id: 'assam_province_restored_1912_1947',
  comments: 'Assam was re-established as a province after the Partition of Bengal was annulled. At independence in 1947, most of Assam joined India while the Sylhet district joined Pakistan.',
  end_date: '1947-08-15',
  established_year: 1912,
  independence_year: 1947,
  modern_nation_qids: ['Q668'],
  name: 'Assam Province (Restored)',
  region: 'South Asia',
  source: 'Manual Correction',
  start_date: '1912-04-01',
  type: 'Province',
  verified: true,
  verified_date: '2025-08-05T22:11:50.906000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q17513379'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'australia_independent_1942'})
SET c += {
  canonical_name: 'Australia',
  colony_id: 'australia_independent_1942',
  established_year: 1942,
  region: 'Pacific',
  type: 'Independence',
  wikidata_id: 'Q408'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'bahamas_colony_1666_1973'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Bahamas Colony',
  colony_id: 'bahamas_colony_1666_1973',
  colony_type: 'Crown Colony',
  comments: 'Colonized from Bermuda, piracy and later tourism',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:09:32',
  end_date: '1973-07-10',
  established_year: 1666,
  independence_year: 1973,
  latitude: 25.0,
  link_status: 'verified',
  longitude: -77.4,
  modern_nation_qids: ['Q778'],
  name: 'Bahamas Colony',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1666-01-01',
  verified: true,
  verified_date: '2025-08-05T21:15:25.849000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BS'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1060894'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'bahrain_protectorate_1861_1971'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Bahrain Protectorate',
  colony_id: 'bahrain_protectorate_1861_1971',
  colony_type: 'Protectorate',
  comments: 'Formal protectorate established by the Perpetual Truce of Peace and Friendship, which ceded foreign relations control to Britain.',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:07.985245',
  end_date: '1971-08-15',
  established_year: 1861,
  independence_year: 1971,
  latitude: 26.0675,
  longitude: 50.551111,
  modern_nation_qids: ['Q398'],
  name: 'Bahrain Protectorate',
  region: 'Middle East',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1861-05-21',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-05T21:25:42.750000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['BH'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q21816225'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'baker_island_1855_1898'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Baker Island',
  colony_id: 'baker_island_1855_1898',
  colony_type: 'Guano Island',
  comments: 'Claimed for guano mining, transferred to United States',
  created_date: '2025-07-20T11:26:12',
  end_date: '1898-07-07',
  established_year: 1897,
  independence_year: 1898,
  modern_nation_qids: ['Q30'],
  name: 'Baker Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1897-01-01',
  verified: true,
  verified_date: '2025-08-05T21:28:26.049000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['US'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q46879'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'baluchistan_1877_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Baluchistan',
  colony_id: 'baluchistan_1877_1947',
  colony_type: 'Province',
  comments: 'Now part of Balochistan and Federally Administered Tribal Areas in Pakistan',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:07.992364',
  end_date: '1947-01-01',
  established_year: 1877,
  independence_year: 1947,
  latitude: 30.0,
  longitude: 71.0,
  modern_nation_qids: ['Q843'],
  name: 'Baluchistan',
  region: 'South Asia',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1877-01-01',
  transition_type: 'partition',
  verified: true,
  verified_date: '2025-08-05T21:29:19.975000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['PK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2336399'
};

MERGE (c:HistoricalTerritory:MilitaryAdministration:Colony {colony_id: 'banda_islands_british_occupation_1810_1817'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Banda Islands (British Occupation)',
  colony_id: 'banda_islands_british_occupation_1810_1817',
  colony_type: 'Military Administration',
  comments: 'British occupation of nutmeg islands during Napoleonic Wars',
  created_date: '2025-07-19T23:21:55',
  end_date: '1817-01-01',
  established_year: 1810,
  independence_year: 1817,
  modern_nation_qids: ['Q252'],
  name: 'Banda Islands (British Occupation)',
  region: 'Southeast Asia',
  source: 'Additional Southeast Asian Territories',
  start_date: '1810-08-01',
  verified: true,
  verified_date: '2025-08-05T21:29:55.663000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['ID'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q76495389'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'barbados_colony_1627_1966'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Barbados Colony',
  colony_id: 'barbados_colony_1627_1966',
  colony_type: 'Crown Colony',
  comments: 'British colony from 1627 until independence. Served as the headquarters of the British Windward Islands from 1833 to 1885.',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:09:32',
  end_date: '1966-11-30',
  established_year: 1627,
  independence_year: 1966,
  latitude: 13.17,
  link_status: 'verified',
  longitude: -59.5525,
  mapping_note: 'FLAGGED: Duplicate with Barbados - needs further mapping',
  modern_nation_qids: ['Q244'],
  name: 'Barbados Colony',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1627-02-17',
  verified: true,
  verified_date: '2025-08-05T21:47:25.537000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BB'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q63973349'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'basutoland_1868_1966'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Basutoland',
  colony_id: 'basutoland_1868_1966',
  colony_type: 'Crown Colony',
  comments: 'Wanted to join Cape Colony, but was authorized to join Colony of Natal instead',
  created_date: '2025-07-19T18:39:07.576834',
  end_date: '1966-01-01',
  established_year: 1868,
  independence_year: 1966,
  link_status: 'verified',
  modern_nation_qids: ['Q1013'],
  name: 'Basutoland',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1868-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-05T21:48:08.575000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['LS'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2340665'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'bay_islands_1852_1859'})
SET c += {
  canonical_name: 'Bay Islands',
  colony_id: 'bay_islands_1852_1859',
  established_year: 1852,
  independence_year: 1859,
  region: 'Caribbean',
  type: 'Crown Colony',
  wikidata_id: 'Q1553529'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'bechuanaland_protectorate_1884_1966'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Bechuanaland Protectorate',
  colony_id: 'bechuanaland_protectorate_1884_1966',
  colony_type: 'Protectorate',
  comments: 'Resident Commissioner assigned 1884, treaties with chiefs signed 1885',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T18:39:07.595247',
  end_date: '1966-01-01',
  established_year: 1884,
  independence_year: 1966,
  latitude: -22.9507,
  link_status: 'verified',
  longitude: 27.3747,
  modern_nation_qids: ['Q963'],
  name: 'Bechuanaland Protectorate',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1884-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-05T21:48:55.542000000+00:00',
  whg_aat_types: [],
  whg_ccodes: ['BW'],
  whg_fclasses: [],
  wikidata_id: 'Q747314'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'bencoolen_bengkulu_1685_1824'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Bencoolen (Bengkulu)',
  colony_id: 'bencoolen_bengkulu_1685_1824',
  colony_type: 'Trading Post',
  comments: 'British East India Company settlement in Sumatra, traded to Dutch for Malacca',
  created_date: '2025-07-19T23:21:55',
  end_date: '1824-03-17',
  established_year: 1685,
  independence_year: 1824,
  modern_nation_qids: ['Q252'],
  name: 'Bencoolen (Bengkulu)',
  region: 'Southeast Asia',
  source: 'Additional Southeast Asian Territories',
  start_date: '1685-01-01',
  verified: true,
  verified_date: '2025-08-05T21:49:31.306000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ID'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4969562'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'bengal_presidency_company_1757_1858'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Bengal Presidency (Company)',
  colony_id: 'bengal_presidency_company_1757_1858',
  colony_type: 'Presidency',
  comments: 'Battle of Plassey 1757, included Bengal, Bihar, Orissa, eventually much of northern India',
  created_date: '2025-07-19T21:53:26',
  end_date: '1858-11-01',
  established_year: 1757,
  independence_year: 1858,
  modern_nation_qids: ['Q668', 'Q902'],
  name: 'Bengal Presidency (Company)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1757-06-23',
  verified: true,
  verified_date: '2025-08-05T22:08:42.147000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN', 'BD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q817165'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'bengal_presidency_crown_1858_1912'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Bengal Presidency (Crown)',
  colony_id: 'bengal_presidency_crown_1858_1912',
  colony_type: 'Presidency',
  comments: 'Direct Crown rule over the Bengal Presidency until its partition in 1905.',
  created_date: '2025-07-19T21:53:26',
  end_date: '1905-10-16',
  established_year: 1858,
  independence_year: 1912,
  modern_nation_qids: ['Q668', 'Q902'],
  name: 'Bengal Presidency (Crown)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1858-11-01',
  verified: true,
  verified_date: '2025-08-05T22:08:42.147000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN', 'BD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q817165'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'bengal_province_partitioned_1905_1912'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Bengal Province (Partitioned)',
  colony_id: 'bengal_province_partitioned_1905_1912',
  colony_type: 'Province',
  comments: 'Western part of Bengal during partition period',
  created_date: '2025-07-19T21:53:27',
  end_date: '1912-12-12',
  established_year: 1905,
  independence_year: 1912,
  modern_nation_qids: ['Q668', 'Q902'],
  name: 'Bengal Province (Partitioned)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1905-10-16',
  verified: true,
  verified_date: '2025-08-05T22:08:42.147000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN', 'BD'],
  whg_fclasses: ['A']
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'bengal_province_reunited_1912_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Bengal Province (Reunited)',
  colony_id: 'bengal_province_reunited_1912_1947',
  colony_type: 'Province',
  comments: 'Bengal reunited 1912, partitioned again 1947 between India (West Bengal) and Pakistan (East Bengal)',
  created_date: '2025-07-19T21:53:27',
  end_date: '1947-08-15',
  established_year: 1912,
  independence_year: 1947,
  modern_nation_qids: ['Q668', 'Q902'],
  name: 'Bengal Province (Reunited)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1912-12-12',
  verified: true,
  verified_date: '2025-08-05T22:08:42.147000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN', 'BD'],
  whg_fclasses: ['A']
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'berbice_colony_1803_1831'})
SET c += {
  canonical_name: 'Berbice',
  colony_id: 'berbice_colony_1803_1831',
  established_year: 1803,
  independence_year: 1831,
  region: 'South America',
  type: 'Crown Colony',
  wikidata_id: 'Q861922'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'bermuda_1609_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Bermuda',
  colony_id: 'bermuda_1609_ongoing',
  colony_type: 'Crown Colony',
  comments: 'England\'s oldest remaining overseas territory',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T12:11:27',
  established_year: 1609,
  latitude: 32.32,
  longitude: -64.74,
  modern_nation_qids: ['Q23635'],
  name: 'Bermuda',
  region: 'Atlantic',
  source: 'Comprehensive Missing Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1609-07-28',
  verified: true,
  verified_date: '2025-08-05T23:40:15.150000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q23635'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'bihar_and_orissa_1912_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Bihar and Orissa',
  colony_id: 'bihar_and_orissa_1912_1947',
  colony_type: 'Province',
  comments: 'Separated from Bengal 1912, Orissa separated as separate province 1936',
  created_date: '2025-07-19T21:53:27',
  end_date: '1947-08-15',
  established_year: 1912,
  independence_year: 1947,
  modern_nation_qids: ['Q668'],
  name: 'Bihar and Orissa',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1912-04-01',
  verified: true,
  verified_date: '2025-08-05T23:41:38.205000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4907084'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'birnie_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Birnie Island',
  colony_id: 'birnie_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, transferred to Kiribati',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1860,
  independence_year: 1979,
  modern_nation_qids: ['Q710'],
  name: 'Birnie Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1860-01-01',
  verified: true,
  verified_date: '2025-08-05T23:42:40.915000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q45295'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'bombay_presidency_company_1687_1858'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Bombay Presidency (Company)',
  colony_id: 'bombay_presidency_company_1687_1858',
  colony_type: 'Presidency',
  comments: 'Moved from Surat, expanded across western India, included Sind 1843',
  created_date: '2025-07-19T21:53:26',
  end_date: '1858-11-01',
  established_year: 1687,
  independence_year: 1858,
  modern_nation_qids: ['Q668'],
  name: 'Bombay Presidency (Company)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1687-01-01',
  verified: true,
  verified_date: '2025-08-05T23:46:30.960000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q891827'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'bombay_presidency_crown_1858_1947'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Bombay Presidency (Crown)',
  colony_id: 'bombay_presidency_crown_1858_1947',
  colony_type: 'Presidency',
  comments: 'Crown rule over western India, Maharashtra, Gujarat, parts of Karnataka',
  created_date: '2025-07-19T21:53:26',
  end_date: '1947-08-15',
  established_year: 1858,
  independence_year: 1947,
  modern_nation_qids: ['Q668'],
  name: 'Bombay Presidency (Crown)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1858-11-01',
  verified: true,
  verified_date: '2025-08-05T23:46:55.038000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q891827'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'bouvet_island_brief_claim_1825_1928'})
SET c += {
  administrative_status: 'Remote Island',
  canonical_name: 'Bouvet Island (Brief Claim)',
  colony_id: 'bouvet_island_brief_claim_1825_1928',
  colony_type: 'Remote Island',
  comments: 'Remote sub-Antarctic island, claimed before Norwegian annexation',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T11:26:12',
  end_date: '1928-01-01',
  established_year: 1825,
  independence_year: 1928,
  latitude: -54.25,
  longitude: -36.75,
  modern_nation_qids: ['Q31747'],
  name: 'Bouvet Island (Brief Claim)',
  region: 'Antarctica',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1825-12-01',
  verified: true,
  verified_date: '2025-08-05T23:47:56.473000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['NO'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q23408'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'british_bechuanaland_1885_1895'})
SET c += {
  administrative_status: 'Crown colony',
  canonical_name: 'British Bechuanaland',
  colony_id: 'british_bechuanaland_1885_1895',
  colony_type: 'Crown colony',
  comments: 'Now part of Northern Cape and North West provinces of South Africa',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T18:39:07.612986',
  end_date: '1895-01-01',
  established_year: 1885,
  independence_year: 1895,
  latitude: -29.0,
  link_status: 'verified',
  longitude: 24.0,
  modern_nation_qids: ['Q963'],
  name: 'British Bechuanaland',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1885-01-01',
  transition_type: 'incorporation',
  verified: true,
  verified_date: '2025-08-05T23:48:54.596000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BW'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4530733'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'british_cameroons_1916_1961'})
SET c += {
  administrative_status: 'Mandate/Trust Territory',
  canonical_name: 'British Cameroons',
  colony_id: 'british_cameroons_1916_1961',
  colony_type: 'Mandate/Trust Territory',
  comments: 'Northern part merged into Nigeria, southern part into Republic of Cameroon',
  created_date: '2025-07-19T18:39:07.632593',
  end_date: '1961-01-01',
  established_year: 1916,
  independence_year: 1961,
  link_status: 'verified',
  modern_nation_qids: ['Q1033', 'Q1009'],
  name: 'British Cameroons',
  qid_type: 'historical_colony',
  region: 'West Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1916-01-01',
  transition_type: 'partition',
  verified: true,
  verified_date: '2025-08-05T23:49:47.254000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['NG', 'CM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1028835'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'british_central_africa_protectorate_1891_1907'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'British Central Africa Protectorate',
  colony_id: 'british_central_africa_protectorate_1891_1907',
  colony_type: 'Protectorate',
  comments: 'Renamed to Nyasaland Protectorate 1907',
  created_date: '2025-07-19T22:06:51',
  end_date: '1907-07-06',
  established_year: 1891,
  independence_year: 1907,
  link_status: 'verified',
  modern_nation_qids: ['Q1020'],
  name: 'British Central Africa Protectorate',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'East African Territorial Evolution',
  start_date: '1891-05-14',
  verified: true,
  verified_date: '2025-08-05T23:51:40.633000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['MW'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2642989'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'british_columbia_province_1871'})
SET c += {
  canonical_name: 'British Columbia',
  colony_id: 'british_columbia_province_1871',
  colony_type: 'Province',
  established_year: 1871,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1974'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'british_gold_coast_1821_1874'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'British Gold Coast',
  colony_id: 'british_gold_coast_1821_1874',
  colony_type: 'Crown Colony',
  comments: 'Crown administration of coastal trading posts',
  created_date: '2025-07-19T22:03:12',
  end_date: '1874-07-24',
  established_year: 1821,
  independence_year: 1874,
  link_status: 'verified',
  modern_nation_qids: ['Q117'],
  name: 'British Gold Coast',
  qid_type: 'historical_colony',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1821-03-07',
  verified: true,
  verified_date: '2025-08-06T00:08:23.387000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GH'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q503623'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'british_guiana_1831_1966'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'British Guiana',
  colony_id: 'british_guiana_1831_1966',
  colony_type: 'Crown Colony',
  comments: 'Formed from Dutch colonies Demerara, Essequibo, Berbice',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:09:32',
  end_date: '1966-05-26',
  established_year: 1831,
  independence_year: 1966,
  latitude: 5,
  longitude: -58.75,
  modern_nation_qids: ['Q734'],
  name: 'British Guiana',
  region: 'South America',
  source: 'Caribbean and South American Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1831-08-03',
  verified: true,
  verified_date: '2025-08-06T00:11:11.052000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q918126'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'british_honduras_1862_1981'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'British Honduras',
  colony_id: 'british_honduras_1862_1981',
  colony_type: 'Crown Colony',
  comments: 'Mahogany logging settlement, became crown colony 1862',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:09:32',
  end_date: '1981-09-21',
  established_year: 1862,
  independence_year: 1981,
  latitude: 54.2,
  longitude: -6.833333,
  modern_nation_qids: ['Q242'],
  name: 'British Honduras',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1862-05-12',
  verified: true,
  verified_date: '2025-08-06T00:19:18.154000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BZ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1643555'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'british_new_guinea_1884_1906'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'British New Guinea',
  colony_id: 'british_new_guinea_1884_1906',
  colony_type: 'Protectorate',
  comments: 'British protectorate over southeastern New Guinea',
  created_date: '2025-07-19T22:13:10',
  end_date: '1906-09-01',
  established_year: 1884,
  independence_year: 1906,
  modern_nation_qids: ['Q691'],
  name: 'British New Guinea',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1884-11-06',
  verified: true,
  verified_date: '2025-08-06T02:17:06.296000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['PG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2645837'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'british_north_borneo_1882_1946'})
SET c += {
  administrative_status: 'Company Territory',
  canonical_name: 'British North Borneo',
  colony_id: 'british_north_borneo_1882_1946',
  colony_type: 'Company Territory',
  comments: 'British North Borneo Company territory, became Crown Colony 1946',
  created_date: '2025-07-19T23:20:16',
  end_date: '1946-07-15',
  established_year: 1882,
  independence_year: 1946,
  modern_nation_qids: ['Q833'],
  name: 'British North Borneo',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1882-05-12',
  verified: true,
  verified_date: '2025-08-06T02:17:58.936000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1147441'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'british_solomon_islands_1893_1978'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'British Solomon Islands',
  colony_id: 'british_solomon_islands_1893_1978',
  colony_type: 'Protectorate',
  comments: 'Protectorate over chain of Pacific islands',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:13:09',
  end_date: '1978-07-07',
  established_year: 1893,
  independence_year: 1978,
  latitude: -9.466666666,
  longitude: 159.816666666,
  modern_nation_qids: ['Q685'],
  name: 'British Solomon Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1893-06-28',
  verified: true,
  verified_date: '2025-08-06T02:19:03.301000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SB'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q13410267'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'british_somaliland_1884_1960'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'British Somaliland',
  colony_id: 'british_somaliland_1884_1960',
  colony_type: 'Protectorate',
  comments: 'Independent as State of Somaliland for 5 days, then merged with Trust Territory of Somaliland',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T18:39:07.662621',
  end_date: '1960-01-01',
  established_year: 1884,
  independence_year: 1960,
  latitude: 9.560555555,
  link_status: 'verified',
  longitude: 44.054722222,
  modern_nation_qids: ['Q1045'],
  name: 'British Somaliland',
  qid_type: 'historical_colony',
  region: 'Middle East',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1884-01-01',
  transition_type: 'independence_merger',
  verified: true,
  verified_date: '2025-08-06T02:19:35.826000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SO'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q662653'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'british_south_africa_company_territory_1889_1923'})
SET c += {
  administrative_status: 'Company Territory',
  canonical_name: 'British South Africa Company Territory',
  colony_id: 'british_south_africa_company_territory_1889_1923',
  colony_type: 'Company Territory',
  comments: 'BSAC administered both Northern and Southern Rhodesia',
  created_date: '2025-07-19T22:06:51',
  end_date: '1923-10-01',
  established_year: 1889,
  independence_year: 1923,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'British South Africa Company Territory',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'East African Territorial Evolution',
  start_date: '1889-10-29',
  verified: true,
  verified_date: '2025-08-06T02:21:20.488000000+00:00',
  whg_aat_types: ['300387081'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5155572'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'british_togoland_1919_1957'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'British Togoland',
  colony_id: 'british_togoland_1919_1957',
  colony_type: 'Mandate',
  comments: 'British mandate territory, joined Gold Coast in independence',
  created_date: '2025-07-19T22:03:12',
  end_date: '1957-03-06',
  established_year: 1919,
  independence_year: 1957,
  link_status: 'verified',
  modern_nation_qids: ['Q117'],
  name: 'British Togoland',
  qid_type: 'historical_colony',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1919-07-20',
  verified: true,
  verified_date: '2025-08-06T02:22:23.132000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GH'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q797527'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'british_virgin_islands_1672_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'British Virgin Islands',
  colony_id: 'british_virgin_islands_1672_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Still British Overseas Territory',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:09:32',
  established_year: 1672,
  latitude: 18.445,
  link_status: 'verified',
  longitude: -64.54,
  modern_nation_qids: ['Q25305'],
  name: 'British Virgin Islands',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1672-01-01',
  verified: true,
  verified_date: '2025-08-06T02:22:43.949000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['VG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q25305'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'british_western_pacific_territories_1877_1978'})
SET c += {
  administrative_status: 'Administration',
  canonical_name: 'British Western Pacific Territories',
  colony_id: 'british_western_pacific_territories_1877_1978',
  colony_type: 'Administration',
  comments: 'Administrative unit covering multiple Pacific islands',
  created_date: '2025-07-19T22:13:10',
  end_date: '1978-07-07',
  established_year: 1877,
  independence_year: 1978,
  modern_nation_qids: ['Q712', 'Q685', 'Q672', 'Q710'],
  name: 'British Western Pacific Territories',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1877-01-01',
  verified: true,
  verified_date: '2025-08-06T02:23:26.504000000+00:00',
  whg_aat_types: ['300387081'],
  whg_ccodes: ['FJ', 'SB', 'TV', 'KI'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1545934'
};

MERGE (c:HistoricalTerritory:Federation:Colony {colony_id: 'british_windward_islands_1833_1959'})
SET c += {
  administrative_status: 'Federal Colony',
  canonical_name: 'British Windward Islands',
  colony_id: 'british_windward_islands_1833_1959',
  colony_type: 'Federal Colony',
  comments: 'Federation of Grenada, St Lucia, St Vincent, Dominica (after 1940)',
  created_date: '2025-07-20T12:11:28',
  end_date: '1959-01-01',
  established_year: 1833,
  independence_year: 1959,
  link_status: 'verified',
  modern_nation_qids: ['Q760', 'Q757', 'Q784', 'Q769'],
  name: 'British Windward Islands',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Comprehensive Missing Territories',
  start_date: '1833-01-01',
  verified: true,
  verified_date: '2025-08-06T02:24:00.016000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['LC', 'VC', 'DM', 'GD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2660774'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'brunei_protectorate_1888_1984'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Brunei Protectorate',
  colony_id: 'brunei_protectorate_1888_1984',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Sultanate of Brunei',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T23:20:17',
  end_date: '1984-01-01',
  established_year: 1888,
  independence_year: 1984,
  latitude: 4.4,
  longitude: 114.566667,
  modern_nation_qids: ['Q921'],
  name: 'Brunei Protectorate',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1888-09-17',
  verified: true,
  verified_date: '2025-08-06T02:41:24.811000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['BN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q921'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'burma_british_india_1886_1937'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Burma (British India)',
  colony_id: 'burma_british_india_1886_1937',
  colony_type: 'Province',
  comments: 'Upper Burma added 1886, administered as province of British India until 1937',
  created_date: '2025-07-19T21:53:27',
  end_date: '1937-04-01',
  established_year: 1886,
  independence_year: 1937,
  modern_nation_qids: ['Q668', 'Q843', 'Q902'],
  name: 'Burma (British India)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1886-01-01',
  verified: true,
  verified_date: '2025-08-06T02:31:54.454000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN', 'PK', 'BD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2376315'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'burma_separate_colony_1937_1948'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Burma (Separate Colony)',
  colony_id: 'burma_separate_colony_1937_1948',
  colony_type: 'Crown Colony',
  comments: 'Separated from British India 1937, became independent Burma 1948',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:53:27',
  end_date: '1948-01-04',
  established_year: 1937,
  independence_year: 1948,
  latitude: 22.0,
  longitude: 96.0,
  modern_nation_qids: ['Q836'],
  name: 'Burma (Separate Colony)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1937-04-01',
  verified: true,
  verified_date: '2025-08-06T02:31:54.454000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2376315'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'campbell_island_whaling_1810_1860'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'Campbell Island Whaling',
  colony_id: 'campbell_island_whaling_1810_1860',
  colony_type: 'Whaling Station',
  comments: 'Sub-Antarctic whaling and sealing operations',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T11:26:12',
  end_date: '1860-12-31',
  established_year: 1810,
  independence_year: 1860,
  latitude: -52.534215,
  longitude: 169.166525,
  modern_nation_qids: ['Q664'],
  name: 'Campbell Island Whaling',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1810-01-01',
  verified: true,
  verified_date: '2025-08-06T14:09:38.747000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['NZ'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q3593036'
};

MERGE (c:HistoricalTerritory:Dominion:Colony {colony_id: 'canada_dominion_of_1867_ongoing'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Dominion of Canada',
  colony_id: 'canada_dominion_of_1867_ongoing',
  colony_type: 'Dominion',
  comments: 'Formed by federation of Canada, New Brunswick, Nova Scotia provinces',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.150018',
  established_year: 1867,
  independence_year: 1931,
  latitude: 56.0,
  link_status: 'verified',
  longitude: -109.0,
  modern_nation_qids: ['Q16'],
  name: 'Canada, Dominion of',
  qid_type: 'modern_nation',
  region: 'North America',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1867-01-01',
  transition_type: 'constitutional_monarchy',
  verified: true,
  verified_date: '2025-08-06T14:14:36.062000000+00:00',
  whg_aat_types: ['300387506'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q16'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'canada_independent_1931'})
SET c += {
  canonical_name: 'Canada',
  colony_id: 'canada_independent_1931',
  established_year: 1931,
  region: 'North America',
  type: 'Independence',
  wikidata_id: 'Q16'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'cape_breton_colony_1784_1820'})
SET c += {
  colony_id: 'cape_breton_colony_1784_1820',
  established_year: 1784,
  independence_year: 1820,
  name: 'Cape Breton Colony',
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q107457458'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'cape_coast_castle_1664_1821'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Cape Coast Castle',
  colony_id: 'cape_coast_castle_1664_1821',
  colony_type: 'Trading Post',
  comments: 'Royal African Company headquarters on Gold Coast',
  created_date: '2025-07-19T22:03:12',
  end_date: '1821-03-07',
  established_year: 1664,
  independence_year: 1821,
  link_status: 'verified',
  modern_nation_qids: ['Q117'],
  name: 'Cape Coast Castle',
  qid_type: 'historical_colony',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1664-01-01',
  verified: true,
  verified_date: '2025-08-06T14:15:42.712000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GH'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1254826'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'cape_colony_british_1795_1803_1795_1803'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Cape Colony (British 1795-1803)',
  colony_id: 'cape_colony_british_1795_1803_1795_1803',
  colony_type: 'Crown Colony',
  comments: 'First British occupation during French Revolutionary Wars',
  created_date: '2025-07-19T22:00:07',
  end_date: '1803-02-25',
  established_year: 1795,
  independence_year: 1803,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Cape Colony (British 1795-1803)',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1795-09-16',
  verified: true,
  verified_date: '2025-08-06T14:17:02.478000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4806993'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'cape_colony_british_1806_1910'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Cape Colony (British)',
  colony_id: 'cape_colony_british_1806_1910',
  colony_type: 'Crown Colony',
  comments: 'Permanent British control from 1806, confirmed at Congress of Vienna 1815',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T22:00:07',
  end_date: '1910-05-31',
  established_year: 1806,
  independence_year: 1910,
  latitude: -33.0,
  link_status: 'verified',
  longitude: 18.0,
  modern_nation_qids: ['Q258'],
  name: 'Cape Colony (British)',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1806-01-10',
  verified: true,
  verified_date: '2025-08-06T14:17:47.512000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4806993'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'cape_colony_dutch_1652_1795'})
SET c += {
  administrative_status: 'Dutch Company Colony',
  canonical_name: 'Cape Colony (Dutch)',
  colony_id: 'cape_colony_dutch_1652_1795',
  colony_type: 'Dutch Company Colony',
  comments: 'Dutch East India Company settlement, first European settlement in South Africa',
  created_date: '2025-07-19T22:00:07',
  end_date: '1795-09-16',
  established_year: 1652,
  independence_year: 1795,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Cape Colony (Dutch)',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1652-04-06',
  verified: true,
  verified_date: '2025-08-06T14:19:05.185000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4807130'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'cape_colony_dutch_restored_1803_1806'})
SET c += {
  administrative_status: 'Dutch Colony',
  canonical_name: 'Cape Colony (Dutch Restored)',
  colony_id: 'cape_colony_dutch_restored_1803_1806',
  colony_type: 'Dutch Colony',
  comments: 'Brief restoration under Treaty of Amiens',
  created_date: '2025-07-19T22:00:07',
  end_date: '1806-01-10',
  established_year: 1803,
  independence_year: 1806,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Cape Colony (Dutch Restored)',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1803-02-25',
  verified: true,
  verified_date: '2025-08-06T14:18:23.715000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4807130'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'caroline_island_1868_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Caroline Island',
  colony_id: 'caroline_island_1868_1979',
  colony_type: 'Guano Island',
  comments: 'Line Islands guano mining, transferred to Kiribati',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1868,
  independence_year: 1979,
  latitude: -9.955,
  longitude: -150.2125,
  modern_nation_qids: ['Q710'],
  name: 'Caroline Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1868-01-01',
  verified: true,
  verified_date: '2025-08-06T14:22:03.105000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q822151'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'cayman_islands_1670_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Cayman Islands',
  colony_id: 'cayman_islands_1670_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Dependency of Jamaica until 1962, still British Overseas Territory',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:09:32',
  established_year: 1670,
  latitude: 19.5,
  link_status: 'verified',
  longitude: -80.5,
  modern_nation_qids: ['Q5785'],
  name: 'Cayman Islands',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1670-01-01',
  verified: true,
  verified_date: '2025-08-06T14:23:35.684000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5785'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'central_provinces_1861_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Central Provinces',
  colony_id: 'central_provinces_1861_1947',
  colony_type: 'Province',
  comments: 'Created from Nagpur and Saugor territories, became Central Provinces and Berar 1903',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:53:26',
  end_date: '1947-08-15',
  established_year: 1861,
  independence_year: 1947,
  latitude: 21.15,
  longitude: 79.09,
  modern_nation_qids: ['Q668'],
  name: 'Central Provinces',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1861-01-01',
  verified: true,
  verified_date: '2025-08-06T14:26:05.071000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q521864'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'ceylon_1795_1948'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Ceylon',
  colony_id: 'ceylon_1795_1948',
  colony_type: 'Crown Colony',
  comments: 'Now the Democratic Socialist Republic of Sri Lanka',
  created_date: '2025-07-19T18:39:08.040898',
  end_date: '1948-01-01',
  established_year: 1795,
  independence_year: 1948,
  latitude: 6.916667,
  longitude: 79.833333,
  modern_nation_qids: ['Q854'],
  name: 'Ceylon',
  region: 'South Asia',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1795-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-06T14:27:37.493000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['LK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q918153'
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'chagos_islands_mauritius_dependency_1814_1965'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Chagos Islands (Mauritius Dependency)',
  colony_id: 'chagos_islands_mauritius_dependency_1814_1965',
  colony_type: 'Dependency',
  comments: 'Part of Mauritius until detached to form BIOT',
  created_date: '2025-07-19T23:25:07',
  end_date: '1965-11-08',
  established_year: 1814,
  independence_year: 1965,
  modern_nation_qids: ['Q1027'],
  name: 'Chagos Islands (Mauritius Dependency)',
  region: 'South Asia',
  source: 'Indian Ocean Territories',
  start_date: '1814-05-30',
  verified: true,
  verified_date: '2025-08-06T14:28:22.687000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q192188'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'christmas_island_1888_1958'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Christmas Island',
  colony_id: 'christmas_island_1888_1958',
  colony_type: 'Crown Colony',
  comments: 'Phosphate mining, transferred to Australia',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:13:10',
  end_date: '1958-10-01',
  established_year: 1888,
  independence_year: 1958,
  latitude: -10.49,
  longitude: 105.6275,
  modern_nation_qids: ['Q31063'],
  name: 'Christmas Island',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1888-06-01',
  verified: true,
  verified_date: '2025-08-06T14:28:45.326000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['CX'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q31063'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'christmas_island_line_islands_1857_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Christmas Island (Line Islands)',
  colony_id: 'christmas_island_line_islands_1857_1979',
  colony_type: 'Guano Island',
  comments: 'Major Line Islands guano deposits, transferred to Kiribati',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1857,
  independence_year: 1979,
  latitude: 1.85,
  longitude: -157.4,
  modern_nation_qids: ['Q710'],
  name: 'Christmas Island (Line Islands)',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1857-01-01',
  verified: true,
  verified_date: '2025-08-06T14:31:20.411000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q193331'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'cocos_keeling_islands_1857_1955'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Cocos (Keeling) Islands',
  colony_id: 'cocos_keeling_islands_1857_1955',
  colony_type: 'Crown Colony',
  comments: 'Strategic islands, transferred to Australia',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:13:10',
  end_date: '1955-11-23',
  established_year: 1857,
  independence_year: 1955,
  latitude: -12.1175,
  longitude: 96.895,
  modern_nation_qids: ['Q36004'],
  name: 'Cocos (Keeling) Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1857-04-01',
  verified: true,
  verified_date: '2025-08-06T14:31:41.388000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['CC'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q36004'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'})
SET c += {
  administrative_status: 'Colony/Protectorate',
  canonical_name: 'Colony and Protectorate of Nigeria',
  colony_id: 'colony_and_protectorate_of_nigeria_1914_1960',
  colony_type: 'Colony/Protectorate',
  comments: 'Created from merger of Southern and Northern Nigeria',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:07.856327',
  end_date: '1960-01-01',
  established_year: 1914,
  independence_year: 1960,
  latitude: 9.0,
  link_status: 'verified',
  longitude: 8.0,
  modern_nation_qids: ['Q1033'],
  name: 'Colony and Protectorate of Nigeria',
  qid_type: 'historical_colony',
  region: 'West Africa',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1914-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-06T14:32:57.100000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['NG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5148517'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'colony_of_natal_1843_1910'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Colony of Natal',
  colony_id: 'colony_of_natal_1843_1910',
  colony_type: 'Crown Colony',
  comments: 'Annexed from Natalia Republic, became separate colony 1856',
  created_date: '2025-07-19T22:00:07',
  end_date: '1910-05-31',
  established_year: 1843,
  independence_year: 1910,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Colony of Natal',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1843-08-04',
  verified: true,
  verified_date: '2025-08-06T14:33:39.878000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1301901'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'colony_of_newfoundland_1610_1949'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Colony of Newfoundland',
  colony_id: 'colony_of_newfoundland_1610_1949',
  colony_type: 'Crown Colony',
  comments: 'Separate British colony until joining Canada 1949',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T12:11:27',
  end_date: '1949-03-31',
  established_year: 1610,
  independence_year: 1907,
  latitude: 53,
  longitude: -60,
  modern_nation_qids: ['Q16'],
  name: 'Colony of Newfoundland',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1610-05-02',
  verified: true,
  verified_date: '2025-08-06T14:36:04.009000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2984260'
};

MERGE (c:HistoricalTerritory:Dominion:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Commonwealth of Australia',
  colony_id: 'commonwealth_of_australia_1901_ongoing',
  colony_type: 'Dominion',
  comments: 'Federation of six Australian colonies into Commonwealth',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:49:48',
  established_year: 1901,
  independence_year: 1942,
  latitude: -25.0,
  longitude: 133.0,
  modern_nation_qids: ['Q408'],
  name: 'Commonwealth of Australia',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1901-01-01',
  verified: true,
  verified_date: '2025-08-06T14:36:45.361000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q408'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'connecticut_colony_1636_1783'})
SET c += {
  administrative_status: 'Charter Colony',
  canonical_name: 'Connecticut Colony',
  colony_id: 'connecticut_colony_1636_1783',
  colony_type: 'Charter Colony',
  comments: 'Founded by Thomas Hooker, Hartford',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1636,
  independence_year: 1783,
  latitude: 39.828175,
  longitude: -98.5795,
  modern_nation_qids: ['Q30'],
  name: 'Connecticut Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1636-01-01',
  verified: true,
  verified_date: '2025-08-06T14:38:33.458000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q951500'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'cook_islands_1888_1901'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Cook Islands',
  colony_id: 'cook_islands_1888_1901',
  colony_type: 'Protectorate',
  comments: 'Transferred to New Zealand administration',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:13:10',
  end_date: '1901-06-11',
  established_year: 1888,
  independence_year: 1901,
  latitude: -21.233333333,
  longitude: -159.783333333,
  modern_nation_qids: ['Q26988'],
  name: 'Cook Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1888-10-01',
  verified: true,
  verified_date: '2025-08-06T14:38:43.967000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q26988'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'coorg_province_1834_1947'})
SET c += {
  canonical_name: 'Coorg',
  colony_id: 'coorg_province_1834_1947',
  established_year: 1834,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Province',
  wikidata_id: 'Q864930'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'corsica_1794_1796'})
SET c += {
  canonical_name: 'Anglo-Corsican Kingdom',
  colony_id: 'corsica_1794_1796',
  established_year: 1794,
  independence_year: 1796,
  region: 'Europe',
  type: 'Protectorate',
  wikidata_id: 'Q2259576'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'cyprus_1878_1960'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Cyprus',
  colony_id: 'cyprus_1878_1960',
  colony_type: 'Crown Colony',
  comments: 'Two sovereign base areas remain under British sovereignty',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.362167',
  end_date: '1960-08-16',
  established_year: 1878,
  independence_year: 1960,
  latitude: 35.0,
  link_status: 'verified',
  longitude: 33.0,
  modern_nation_qids: ['Q229'],
  name: 'Cyprus',
  qid_type: 'historical_colony',
  region: 'Europe',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1878-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-06T14:38:57.612000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q15240466'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'deception_island_whaling_1906_1931'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'Deception Island Whaling',
  colony_id: 'deception_island_whaling_1906_1931',
  colony_type: 'Whaling Station',
  comments: 'Major whaling station in Whalers Bay',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T11:26:12',
  end_date: '1931-12-31',
  established_year: 1906,
  independence_year: 1931,
  latitude: -54.25,
  longitude: -36.75,
  modern_nation_qids: ['Q35086'],
  name: 'Deception Island Whaling',
  region: 'Antarctica',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1906-01-01',
  verified: true,
  verified_date: '2025-08-06T14:39:36.963000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: [],
  whg_fclasses: ['T'],
  wikidata_id: 'Q1045820'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'delaware_colony_1664_1783'})
SET c += {
  administrative_status: 'Proprietary Colony',
  canonical_name: 'Delaware Colony',
  colony_id: 'delaware_colony_1664_1783',
  colony_type: 'Proprietary Colony',
  comments: 'Lower counties of Pennsylvania, separate after 1701',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1664,
  independence_year: 1783,
  latitude: 39.828175,
  longitude: -98.5795,
  modern_nation_qids: ['Q30'],
  name: 'Delaware Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1664-09-08',
  verified: true,
  verified_date: '2025-08-06T14:41:33.138000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2571194'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'demerara_colony_1803_1831'})
SET c += {
  canonical_name: 'Demerara',
  colony_id: 'demerara_colony_1803_1831',
  established_year: 1803,
  independence_year: 1831,
  region: 'South America',
  type: 'Crown Colony',
  wikidata_id: 'Q2399707'
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'desroches_islands_1903_1965'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Desroches Islands',
  colony_id: 'desroches_islands_1903_1965',
  colony_type: 'Dependency',
  comments: 'Dependency of Seychelles, briefly part of BIOT',
  created_date: '2025-07-19T23:25:07',
  end_date: '1965-11-08',
  established_year: 1903,
  independence_year: 1965,
  link_status: 'verified',
  modern_nation_qids: ['Q1042'],
  name: 'Desroches Islands',
  qid_type: 'geographical',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  start_date: '1903-08-31',
  verified: true,
  verified_date: '2025-08-06T14:41:58.959000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SC'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q620506'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'dominica_colony_1763_1978'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Dominica Colony',
  colony_id: 'dominica_colony_1763_1978',
  colony_type: 'Crown Colony',
  comments: 'Ceded by France, part of Windward Islands',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:09:32',
  end_date: '1978-11-03',
  established_year: 1763,
  independence_year: 1978,
  latitude: 15.416667,
  link_status: 'verified',
  longitude: -61.333333,
  modern_nation_qids: ['Q784'],
  name: 'Dominica Colony',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1763-02-10',
  verified: true,
  verified_date: '2025-08-06T14:42:42.630000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['DM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q137394892'
};

MERGE (c:HistoricalTerritory:Dominion:Colony {colony_id: 'dominion_of_india_1947_1950'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Dominion of India',
  colony_id: 'dominion_of_india_1947_1950',
  colony_type: 'Dominion',
  comments: 'India at independence, became Republic of India 1950',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:53:27',
  end_date: '1950-01-26',
  established_year: 1947,
  independence_year: 1950,
  latitude: 22.8,
  longitude: 83.0,
  modern_nation_qids: ['Q668', 'Q843', 'Q902'],
  name: 'Dominion of India',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1947-08-15',
  verified: true,
  verified_date: '2025-08-06T14:43:01.723000000+00:00',
  whg_aat_types: ['300387346'],
  whg_ccodes: ['IN', 'PK', 'BD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1775277'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'dominion_of_new_zealand_1907_1947'})
SET c += {
  canonical_name: 'Dominion of New Zealand',
  colony_id: 'dominion_of_new_zealand_1907_1947',
  established_year: 1907,
  independence_year: 1947,
  region: 'Pacific',
  type: 'Dominion',
  wikidata_id: 'Q664'
};

MERGE (c:HistoricalTerritory:Dominion:Colony {colony_id: 'dominion_of_newfoundland_1907_1934'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Dominion of Newfoundland',
  colony_id: 'dominion_of_newfoundland_1907_1934',
  colony_type: 'Dominion',
  comments: 'Self-governing dominion, reverted to Crown colony 1934',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T12:11:27',
  end_date: '1949-03-31',
  established_year: 1907,
  independence_year: 1934,
  latitude: 56.0,
  link_status: 'verified',
  longitude: -109.0,
  modern_nation_qids: ['Q16'],
  name: 'Dominion of Newfoundland',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1907-09-26',
  verified: true,
  verified_date: '2025-08-06T14:43:35.136000000+00:00',
  whg_aat_types: ['300387346'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q38610'
};

MERGE (c:HistoricalTerritory:Dominion:Colony {colony_id: 'dominion_of_pakistan_1947_1956'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Dominion of Pakistan',
  colony_id: 'dominion_of_pakistan_1947_1956',
  colony_type: 'Dominion',
  comments: 'Pakistan at independence (West and East), became Islamic Republic 1956',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:53:27',
  end_date: '1956-03-23',
  established_year: 1947,
  independence_year: 1956,
  latitude: 30.0,
  longitude: 71.0,
  modern_nation_qids: ['Q843'],
  name: 'Dominion of Pakistan',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1947-08-15',
  verified: true,
  verified_date: '2025-08-06T14:45:13.897000000+00:00',
  whg_aat_types: ['300387346'],
  whg_ccodes: ['PK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2006542'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'ducie_island_1902_ongoing'})
SET c += {
  administrative_status: 'Remote Island',
  canonical_name: 'Ducie Island',
  colony_id: 'ducie_island_1902_ongoing',
  colony_type: 'Remote Island',
  comments: 'Part of Pitcairn Islands group, uninhabited coral atoll',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T11:26:12',
  established_year: 1902,
  latitude: -25.0677812,
  longitude: -130.1045778,
  modern_nation_qids: ['Q35672'],
  name: 'Ducie Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1902-01-01',
  verified: true,
  verified_date: '2025-08-06T14:45:32.093000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['PN'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q35672'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'east_africa_protectorate_1895_1920'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'East Africa Protectorate',
  colony_id: 'east_africa_protectorate_1895_1920',
  colony_type: 'Protectorate',
  comments: 'British protectorate after IBEA Company collapse, Uganda separated 1894',
  created_date: '2025-07-19T22:06:51',
  end_date: '1920-07-23',
  established_year: 1895,
  independence_year: 1920,
  link_status: 'verified',
  modern_nation_qids: ['Q114'],
  name: 'East Africa Protectorate',
  qid_type: 'historical_colony',
  region: 'East Africa',
  source: 'East African Territorial Evolution',
  start_date: '1895-07-01',
  verified: true,
  verified_date: '2025-08-06T14:49:17.991000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['KE'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q876185'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'east_florida_1763_1783'})
SET c += {
  colony_id: 'east_florida_1763_1783',
  established_year: 1763,
  independence_year: 1783,
  name: 'East Florida',
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q1770351'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Eastern Bengal and Assam',
  colony_id: 'eastern_bengal_and_assam_1905_1912',
  colony_type: 'Province',
  comments: 'Created by partition of Bengal, reunited 1912 due to protests',
  created_date: '2025-07-19T21:53:27',
  end_date: '1912-12-12',
  established_year: 1905,
  independence_year: 1912,
  modern_nation_qids: ['Q668', 'Q902'],
  name: 'Eastern Bengal and Assam',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1905-10-16',
  verified: true,
  verified_date: '2025-08-05T22:11:50.906000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN', 'BD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4126447'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'egypt_1882_1922'})
SET c += {
  administrative_status: 'Occupation/Protectorate',
  canonical_name: 'Egypt',
  colony_id: 'egypt_1882_1922',
  colony_type: 'Occupation/Protectorate',
  comments: '',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:07.709908',
  end_date: '1922-01-01',
  established_year: 1882,
  independence_year: 1922,
  latitude: 27.0,
  link_status: 'verified',
  longitude: 29.0,
  modern_nation_qids: ['Q79'],
  name: 'Egypt',
  qid_type: 'historical_colony',
  region: 'Middle East',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1882-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-06T14:52:56.382000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['EG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2474428'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'ellice_islands_1976_1978'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Ellice Islands',
  colony_id: 'ellice_islands_1976_1978',
  colony_type: 'Crown Colony',
  comments: 'Separated from Gilbert Islands before independence',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:13:10',
  end_date: '1978-10-01',
  established_year: 1976,
  independence_year: 1978,
  latitude: -7.475,
  longitude: 178.005556,
  modern_nation_qids: ['Q672'],
  name: 'Ellice Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1976-01-01',
  verified: true,
  verified_date: '2025-08-06T14:53:27.293000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['TV'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1050859'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'ellice_islands_separate_1892_1916'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Ellice Islands (Separate)',
  colony_id: 'ellice_islands_separate_1892_1916',
  colony_type: 'Crown Colony',
  comments: 'Separate protectorate before joining Gilbert and Ellice Islands',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T23:21:55',
  end_date: '1916-01-12',
  established_year: 1892,
  independence_year: 1916,
  latitude: -7.475,
  longitude: 178.005556,
  modern_nation_qids: ['Q672'],
  name: 'Ellice Islands (Separate)',
  region: 'Pacific',
  source: 'Additional Southeast Asian Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1892-01-01',
  verified: true,
  verified_date: '2025-08-06T14:53:39.857000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['TV'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1050859'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'enderbury_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Enderbury Island',
  colony_id: 'enderbury_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, disputed with USA, transferred to Kiribati',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1860,
  independence_year: 1979,
  modern_nation_qids: ['Q710'],
  name: 'Enderbury Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1860-01-01',
  verified: true,
  verified_date: '2025-08-06T14:54:08.069000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q30638'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'essequibo_colony_1803_1831'})
SET c += {
  canonical_name: 'Essequibo',
  colony_id: 'essequibo_colony_1803_1831',
  established_year: 1803,
  independence_year: 1831,
  region: 'South America',
  type: 'Crown Colony',
  wikidata_id: 'Q2199929'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'factory_at_surat_1612_1857'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Factory at Surat',
  colony_id: 'factory_at_surat_1612_1857',
  colony_type: 'Trading Post',
  comments: 'First English factory in India, EIC headquarters before Bombay',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T12:11:28',
  end_date: '1857-05-10',
  established_year: 1612,
  independence_year: 1687,
  latitude: 22.8,
  longitude: 83.0,
  modern_nation_qids: ['Q668'],
  name: 'Factory at Surat',
  region: 'South Asia',
  source: 'Comprehensive Missing Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1612-01-01',
  verified: true,
  verified_date: '2025-08-06T14:58:59.508000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q19898523'
};

MERGE (c:HistoricalTerritory:OverseasTerritory:Colony {colony_id: 'falkland_islands_1833_ongoing'})
SET c += {
  administrative_status: 'British Overseas Territory',
  canonical_name: 'Falkland Islands',
  colony_id: 'falkland_islands_1833_ongoing',
  colony_type: 'British Overseas Territory',
  comments: 'Sovereignty disputed by Argentina',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.367423',
  established_year: 1833,
  latitude: -51.73,
  longitude: -59.22,
  modern_nation_qids: ['Q9648'],
  name: 'Falkland Islands',
  region: 'Atlantic',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1833-01-01',
  transition_type: 'ongoing',
  verified: true,
  verified_date: '2025-08-06T14:59:11.756000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q9648'
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'farquhar_islands_1903_1965'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Farquhar Islands',
  colony_id: 'farquhar_islands_1903_1965',
  colony_type: 'Dependency',
  comments: 'Dependency of Seychelles, briefly part of BIOT',
  created_date: '2025-07-19T23:25:07',
  end_date: '1965-11-08',
  established_year: 1903,
  independence_year: 1965,
  link_status: 'verified',
  modern_nation_qids: ['Q1042'],
  name: 'Farquhar Islands',
  qid_type: 'geographical',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  start_date: '1903-08-31',
  verified: true,
  verified_date: '2025-08-06T14:59:47.214000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SC'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q967943'
};

MERGE (c:HistoricalTerritory:Federation:Colony {colony_id: 'federal_colony_leeward_islands_1833-1960'})
SET c += {
  administrative_status: 'Federal Colony',
  canonical_name: 'British Leeward Islands',
  colony_id: 'federal_colony_leeward_islands_1833-1960',
  comments: 'Re-established federal colony that administered various British islands until its dissolution in 1960.',
  end_date: '1960-01-01',
  established_year: 1833,
  independence_year: 1960,
  link_status: 'verified',
  modern_nation_qids: ['Q781', 'Q763', 'Q13353', 'Q25305'],
  name: 'Federal Colony of the Leeward Islands',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Manual Correction',
  start_date: '1833-01-01',
  type: 'Federal Colony',
  verified: true,
  verified_date: '2025-08-06T02:08:47.163000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AG', 'KN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1796551'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'federated_malay_states_1895_1946'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Federated Malay States',
  colony_id: 'federated_malay_states_1895_1946',
  colony_type: 'Protectorate',
  comments: 'Federation of Perak, Selangor, Negeri Sembilan, Pahang under British Residents',
  created_date: '2025-07-19T23:20:16',
  end_date: '1946-04-01',
  established_year: 1895,
  independence_year: 1946,
  modern_nation_qids: ['Q833'],
  name: 'Federated Malay States',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1895-07-01',
  verified: true,
  verified_date: '2025-08-06T15:00:24.050000000+00:00',
  whg_aat_types: ['300387129'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1400154'
};

MERGE (c:HistoricalTerritory:Federation:Colony {colony_id: 'federation_of_malaya_1948_1957'})
SET c += {
  administrative_status: 'Federation',
  canonical_name: 'Federation of Malaya',
  colony_id: 'federation_of_malaya_1948_1957',
  colony_type: 'Federation',
  comments: 'Self-governing federation of Malay states',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T23:20:17',
  end_date: '1957-08-31',
  established_year: 1948,
  independence_year: 1957,
  latitude: 3.15969444,
  longitude: 101.7,
  modern_nation_qids: ['Q833'],
  name: 'Federation of Malaya',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1948-02-01',
  verified: true,
  verified_date: '2025-08-06T15:00:39.925000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1479726'
};

MERGE (c:HistoricalTerritory:Federation:Colony {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'})
SET c += {
  administrative_status: 'Federation',
  canonical_name: 'Federation of Rhodesia and Nyasaland',
  colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963',
  colony_type: 'Federation',
  comments: 'Central African Federation of three territories',
  created_date: '2025-07-19T22:06:51',
  end_date: '1963-12-31',
  established_year: 1953,
  independence_year: 1963,
  link_status: 'verified',
  modern_nation_qids: ['Q954', 'Q953'],
  name: 'Federation of Rhodesia and Nyasaland',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'East African Territorial Evolution',
  start_date: '1953-08-01',
  verified: true,
  verified_date: '2025-08-07T02:36:26.449000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZW', 'ZM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q654342'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'fernando_po_british_1827_1843'})
SET c += {
  administrative_status: 'Possession',
  canonical_name: 'Fernando Po (British)',
  colony_id: 'fernando_po_british_1827_1843',
  colony_type: 'Possession',
  comments: 'Briefly held island, ceded to Spain 1843',
  created_date: '2025-07-19T22:03:12',
  end_date: '1843-01-01',
  established_year: 1827,
  independence_year: 1843,
  link_status: 'verified',
  modern_nation_qids: ['Q983'],
  name: 'Fernando Po (British)',
  qid_type: 'geographical',
  region: 'Africa (Islands)',
  source: 'West African Territorial Evolution',
  start_date: '1827-01-01',
  verified: true,
  verified_date: '2025-08-07T02:38:15.304000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q205022'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'fiji_1874_1970'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Fiji',
  colony_id: 'fiji_1874_1970',
  colony_type: 'Crown Colony',
  comments: '',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.424106',
  end_date: '1970-01-01',
  established_year: 1874,
  independence_year: 1970,
  latitude: -18.0,
  longitude: 178.0,
  modern_nation_qids: ['Q712'],
  name: 'Fiji',
  region: 'Pacific',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1874-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-07T02:39:02.101000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['FJ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5148320'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'flint_island_1866_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Flint Island',
  colony_id: 'flint_island_1866_1979',
  colony_type: 'Guano Island',
  comments: 'Line Islands guano mining, transferred to Kiribati',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1866,
  independence_year: 1979,
  latitude: -7.475,
  longitude: 178.005556,
  modern_nation_qids: ['Q710'],
  name: 'Flint Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1866-01-01',
  verified: true,
  verified_date: '2025-08-07T02:40:30.828000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q741650'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'fort_william_calcutta_1696_1857'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Fort William (Calcutta)',
  colony_id: 'fort_william_calcutta_1696_1857',
  colony_type: 'Trading Post',
  comments: 'EIC Bengal headquarters, became Bengal Presidency',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T12:11:28',
  end_date: '1857-05-10',
  established_year: 1696,
  independence_year: 1757,
  latitude: 22.8,
  longitude: 83.0,
  modern_nation_qids: ['Q668'],
  name: 'Fort William (Calcutta)',
  region: 'South Asia',
  source: 'Comprehensive Missing Territories',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1696-08-24',
  verified: true,
  verified_date: '2025-08-07T02:48:53.518000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2750027'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'gambia_colony_1816_1888'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Gambia Colony',
  colony_id: 'gambia_colony_1816_1888',
  colony_type: 'Crown Colony',
  comments: 'Crown colony before protectorate expansion',
  created_date: '2025-07-19T22:03:12',
  end_date: '1888-01-01',
  established_year: 1816,
  independence_year: 1888,
  link_status: 'verified',
  modern_nation_qids: ['Q1005'],
  name: 'Gambia Colony',
  qid_type: 'historical_colony',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1816-01-01',
  verified: true,
  verified_date: '2025-08-07T02:54:28.415000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3557236'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'gambia_colony_and_protectorate_1816_1965'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Gambia Colony and Protectorate',
  colony_id: 'gambia_colony_and_protectorate_1816_1965',
  colony_type: 'Crown Colony',
  comments: 'Combined administration of the original Gambia Colony and the newly declared Protectorate over the hinterland.',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:07.734739',
  end_date: '1965-01-01',
  established_year: 1888,
  independence_year: 1965,
  latitude: 13.5,
  link_status: 'verified',
  longitude: -15.5,
  modern_nation_qids: ['Q1005'],
  name: 'Gambia Colony and Protectorate',
  qid_type: 'historical_colony',
  region: 'West Africa',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1888-02-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-07T02:54:28.415000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['GM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3557236'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'georgia_colony_1732_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'Georgia Colony',
  colony_id: 'georgia_colony_1732_1783',
  colony_type: 'Royal Colony',
  comments: 'Last of Thirteen Colonies, founded by James Oglethorpe',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1732,
  independence_year: 1783,
  latitude: 39.828175,
  longitude: -98.5795,
  modern_nation_qids: ['Q30'],
  name: 'Georgia Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1732-06-09',
  verified: true,
  verified_date: '2025-08-07T02:55:15.182000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q785035'
};

MERGE (c:HistoricalTerritory:MilitaryAdministration:Colony {colony_id: 'german_east_africa_british_occupied_1916_1922'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'German East Africa (British Occupied)',
  colony_id: 'german_east_africa_british_occupied_1916_1922',
  colony_type: 'Military Administration',
  comments: 'Former German East Africa under British military administration',
  created_date: '2025-07-19T22:06:51',
  end_date: '1922-01-01',
  established_year: 1916,
  independence_year: 1922,
  link_status: 'verified',
  modern_nation_qids: ['Q924'],
  name: 'German East Africa (British Occupied)',
  qid_type: 'historical_colony',
  region: 'East Africa',
  source: 'East African Territorial Evolution',
  start_date: '1916-01-01',
  verified: true,
  whg_aat_types: ['300387081'],
  whg_ccodes: ['TZ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q153963'
};

MERGE (c:HistoricalTerritory:OverseasTerritory:Colony {colony_id: 'gibraltar_1704_ongoing'})
SET c += {
  administrative_status: 'British Overseas Territory',
  canonical_name: 'Gibraltar',
  colony_id: 'gibraltar_1704_ongoing',
  colony_type: 'British Overseas Territory',
  comments: 'Sovereignty claimed by Spain',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.327189',
  established_year: 1704,
  latitude: 36.14,
  link_status: 'verified',
  longitude: -5.35,
  modern_nation_qids: ['Q1410'],
  name: 'Gibraltar',
  qid_type: 'historical_colony',
  region: 'Europe',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1704-01-01',
  transition_type: 'ongoing',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GI'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1410'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'gilbert_and_ellice_islands_1916_1976'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Gilbert and Ellice Islands',
  colony_id: 'gilbert_and_ellice_islands_1916_1976',
  colony_type: 'Crown Colony',
  comments: 'Combined colony of central Pacific atolls',
  created_date: '2025-07-19T22:13:09',
  end_date: '1976-01-01',
  established_year: 1916,
  independence_year: 1976,
  modern_nation_qids: ['Q710'],
  name: 'Gilbert and Ellice Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1916-01-12',
  verified: false,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1050859'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'gilbert_islands_1976_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Gilbert Islands',
  colony_id: 'gilbert_islands_1976_1979',
  colony_type: 'Crown Colony',
  comments: 'Separated from Ellice Islands before independence',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:13:10',
  end_date: '1979-07-12',
  established_year: 1976,
  independence_year: 1979,
  latitude: 1.466666666,
  longitude: 173.033333333,
  modern_nation_qids: ['Q710'],
  name: 'Gilbert Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1976-01-01',
  verified: false,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1050859'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'gold_coast_colony_1874_1957'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Gold Coast Colony',
  colony_id: 'gold_coast_colony_1874_1957',
  colony_type: 'Crown Colony',
  comments: 'Expanded colony after conquest of Ashanti interior',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T22:03:12',
  end_date: '1957-03-06',
  established_year: 1874,
  independence_year: 1957,
  latitude: 5.55,
  link_status: 'verified',
  longitude: -0.2167,
  modern_nation_qids: ['Q117'],
  name: 'Gold Coast Colony',
  qid_type: 'historical_colony',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1874-07-24',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GH'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q503623'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'grenada_colony_1763_1974'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Grenada Colony',
  colony_id: 'grenada_colony_1763_1974',
  colony_type: 'Crown Colony',
  comments: 'Ceded by France, spice island economy',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:09:32',
  end_date: '1974-02-07',
  established_year: 1763,
  independence_year: 1974,
  latitude: 12.1,
  link_status: 'verified',
  longitude: -61.7,
  modern_nation_qids: ['Q769'],
  name: 'Grenada Colony',
  qid_type: 'geographical',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1763-02-10',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3116419'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'griqualand_west_1871_1880'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Griqualand West',
  colony_id: 'griqualand_west_1871_1880',
  colony_type: 'Crown Colony',
  comments: 'Diamond mining area, incorporated into Cape Colony 1880',
  created_date: '2025-07-19T22:00:07',
  end_date: '1880-01-15',
  established_year: 1871,
  independence_year: 1880,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Griqualand West',
  qid_type: 'historical_colony',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1871-10-27',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2547918'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'heard_and_mcdonald_islands_1833_1947'})
SET c += {
  administrative_status: 'Remote Island',
  canonical_name: 'Heard and McDonald Islands',
  colony_id: 'heard_and_mcdonald_islands_1833_1947',
  colony_type: 'Remote Island',
  comments: 'Sub-Antarctic islands, sealing and research, transferred to Australia',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-20T11:26:12',
  end_date: '1947-12-26',
  established_year: 1833,
  independence_year: 1947,
  latitude: -54.25,
  link_status: 'verified',
  longitude: -36.75,
  modern_nation_qids: ['Q408'],
  name: 'Heard and McDonald Islands',
  region: 'Antarctica',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1833-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:01.860000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q35086'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'heligoland_1807_1890'})
SET c += {
  canonical_name: 'Heligoland',
  colony_id: 'heligoland_1807_1890',
  established_year: 1807,
  independence_year: 1890,
  region: 'Europe',
  type: 'Crown Colony',
  wikidata_id: 'Q3104'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'henderson_island_1902_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Henderson Island',
  colony_id: 'henderson_island_1902_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Part of Pitcairn Islands group, uninhabited',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T23:21:55',
  established_year: 1902,
  latitude: -25.0677812,
  link_status: 'verified',
  longitude: -130.1045778,
  modern_nation_qids: ['Q35672'],
  name: 'Henderson Island',
  region: 'Pacific',
  source: 'Additional Southeast Asian Territories',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1902-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:08.833000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['PN'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q184851'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'hong_kong_1841_1997'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Hong Kong',
  colony_id: 'hong_kong_1841_1997',
  colony_type: 'Crown Colony',
  comments: 'Handover to China as special administrative region',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.048410',
  end_date: '1997-01-01',
  established_year: 1841,
  independence_year: 1997,
  latitude: -5.0,
  longitude: 120.0,
  modern_nation_qids: ['Q8646'],
  name: 'Hong Kong',
  region: 'Southeast Asia',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1841-01-01',
  transition_type: 'handover',
  verified: false,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['HK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1054923'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'howland_island_1857_1898'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Howland Island',
  colony_id: 'howland_island_1857_1898',
  colony_type: 'Guano Island',
  comments: 'Claimed for guano mining, transferred to United States',
  created_date: '2025-07-20T11:26:12',
  end_date: '1898-07-07',
  established_year: 1857,
  independence_year: 1898,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'Howland Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1857-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:09.120000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['US'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q131305'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'ile_royale_1713_1763'})
SET c += {
  administrative_status: 'Colonial Territory',
  canonical_name: 'Île Royale',
  colony_id: 'ile_royale_1713_1763',
  colony_type: 'Colonial Territory',
  comments: 'French colony on Cape Breton Island, site of Fortress Louisbourg',
  created_date: '2025-07-20T16:50:25',
  end_date: '1763-02-10',
  established_year: 1713,
  independence_year: 1763,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'Île Royale (French)',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'French Colonial System',
  start_date: '1713-04-11',
  verified: true,
  whg_aat_types: ['300000776'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3593199'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'imperial_british_east_africa_company_territory_1888_1895'})
SET c += {
  administrative_status: 'Company Territory',
  canonical_name: 'Imperial British East Africa Company Territory',
  colony_id: 'imperial_british_east_africa_company_territory_1888_1895',
  colony_type: 'Company Territory',
  comments: 'IBEA Company administered coastal Kenya and parts of Uganda',
  created_date: '2025-07-19T22:06:51',
  end_date: '1895-07-01',
  established_year: 1888,
  independence_year: 1895,
  link_status: 'verified',
  modern_nation_qids: ['Q114'],
  name: 'Imperial British East Africa Company Territory',
  qid_type: 'geographical',
  region: 'East Africa',
  source: 'East African Territorial Evolution',
  start_date: '1888-09-03',
  verified: true,
  verified_date: '2025-08-06T14:49:17.991000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KE'],
  whg_fclasses: ['P'],
  wikidata_id: 'Q926921'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'indian_empire_british_raj_1858_1947'})
SET c += {
  administrative_status: 'Colony/Empire',
  canonical_name: 'Indian Empire (British Raj)',
  colony_id: 'indian_empire_british_raj_1858_1947',
  colony_type: 'Colony/Empire',
  comments: 'Independent as India & Pakistan after partition',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.072510',
  end_date: '1947-01-01',
  established_year: 1858,
  independence_year: 1947,
  latitude: 22.8,
  link_status: 'verified',
  longitude: 83.0,
  modern_nation_qids: ['Q668', 'Q843', 'Q902'],
  name: 'Indian Empire (British Raj)',
  region: 'South Asia',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1613-01-01',
  transition_type: 'partition',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:03.060000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN', 'PK', 'BD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q129286'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'ionian_islands_1815_1864'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Ionian Islands',
  colony_id: 'ionian_islands_1815_1864',
  colony_type: 'Protectorate',
  comments: 'British protectorate, ceded to Greece 1864',
  created_date: '2025-07-19T22:11:19',
  end_date: '1864-05-29',
  established_year: 1815,
  independence_year: 1864,
  link_status: 'verified',
  modern_nation_qids: ['Q41'],
  name: 'Ionian Islands',
  qid_type: 'historical_colony',
  region: 'Europe',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1815-11-05',
  verified: true,
  whg_aat_types: ['300387178'],
  whg_ccodes: ['GR'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1063498'
};

MERGE (c:HistoricalTerritory:IndependentNation {colony_id: 'iraq_1932_ongoing'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'Iraq',
  colony_id: 'iraq_1932_ongoing',
  colony_type: 'Independence',
  comments: 'Kingdom of Iraq, first Arab state to gain independence from League mandate',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T22:11:19',
  established_year: 1932,
  latitude: 33.0,
  link_status: 'verified',
  longitude: 43.0,
  modern_nation_qids: ['Q796'],
  name: 'Iraq',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1932-10-03',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.637000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IQ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q146720'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'ireland_uk_1801_1922'})
SET c += {
  canonical_name: 'Ireland (UK)',
  colony_id: 'ireland_uk_1801_1922',
  established_year: 1801,
  independence_year: 1922,
  region: 'Europe',
  type: 'Union',
  wikidata_id: 'Q174193'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'irish_free_state_1922_1937'})
SET c += {
  canonical_name: 'Irish Free State',
  colony_id: 'irish_free_state_1922_1937',
  established_year: 1922,
  independence_year: 1937,
  region: 'Europe',
  type: 'Dominion',
  wikidata_id: 'Q31747'
};

MERGE (c:HistoricalTerritory:MilitaryAdministration:Colony {colony_id: 'isle_de_france_british_occupation_1810_1814'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Isle de France (British Occupation)',
  colony_id: 'isle_de_france_british_occupation_1810_1814',
  colony_type: 'Military Administration',
  comments: 'Captured from France during Napoleonic Wars',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T23:25:06',
  end_date: '1814-05-30',
  established_year: 1810,
  independence_year: 1814,
  latitude: 46.567602,
  link_status: 'verified',
  longitude: 26.08901,
  modern_nation_qids: ['Q1027'],
  name: 'Isle de France (British Occupation)',
  qid_type: 'historical_colony',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1810-12-03',
  verified: true,
  whg_aat_types: ['300387081'],
  whg_ccodes: ['MU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q12053604'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'jamaica_1655_1962'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Jamaica',
  colony_id: 'jamaica_1655_1962',
  colony_type: 'Crown Colony',
  comments: '',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.250622',
  end_date: '1962-01-01',
  established_year: 1655,
  independence_year: 1962,
  latitude: 18.18,
  link_status: 'verified',
  longitude: -77.4,
  modern_nation_qids: ['Q766'],
  name: 'Jamaica',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1655-01-01',
  transition_type: 'independence',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['JM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2526023'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'james_island_trading_post_1661_1816'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'James Island Trading Post',
  colony_id: 'james_island_trading_post_1661_1816',
  colony_type: 'Trading Post',
  comments: 'Royal African Company trading post on James Island',
  created_date: '2025-07-19T22:03:12',
  end_date: '1816-01-01',
  established_year: 1661,
  independence_year: 1816,
  link_status: 'verified',
  modern_nation_qids: ['Q1005'],
  name: 'James Island Trading Post',
  qid_type: '',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1661-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.555000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1254836'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'jarvis_island_1857_1898'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Jarvis Island',
  colony_id: 'jarvis_island_1857_1898',
  colony_type: 'Guano Island',
  comments: 'Claimed for guano mining, transferred to United States',
  created_date: '2025-07-20T11:26:12',
  end_date: '1898-07-07',
  established_year: 1857,
  independence_year: 1898,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'Jarvis Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1857-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:09.168000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['US'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q62218'
};

MERGE (c:HistoricalTerritory:MilitaryAdministration:Colony {colony_id: 'java_british_occupation_1811_1816'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Java (British Occupation)',
  colony_id: 'java_british_occupation_1811_1816',
  colony_type: 'Military Administration',
  comments: 'British occupation during Napoleonic Wars, administered by Stamford Raffles',
  created_date: '2025-07-19T23:21:55',
  end_date: '1816-08-19',
  established_year: 1811,
  independence_year: 1816,
  modern_nation_qids: ['Q252'],
  name: 'Java (British Occupation)',
  region: 'Southeast Asia',
  source: 'Additional Southeast Asian Territories',
  start_date: '1811-08-26',
  verified: false,
  whg_aat_types: ['300387081'],
  whg_ccodes: ['ID'],
  whg_fclasses: ['A']
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'kenya_colony_and_protectorate_of_1920_1963'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Kenya, Colony & Protectorate of',
  colony_id: 'kenya_colony_and_protectorate_of_1920_1963',
  colony_type: 'Crown Colony',
  comments: 'Previously part of British East Africa',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:07.783985',
  end_date: '1963-01-01',
  established_year: 1920,
  independence_year: 1963,
  latitude: 0.1,
  link_status: 'verified',
  longitude: 38.0,
  modern_nation_qids: ['Q114'],
  name: 'Kenya, Colony & Protectorate of',
  region: 'East Africa',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1920-01-01',
  transition_type: 'independence',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.882000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['KE'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2538511'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'kingdom_of_ireland_1541_1801'})
SET c += {
  canonical_name: 'Kingdom of Ireland',
  colony_id: 'kingdom_of_ireland_1541_1801',
  established_year: 1541,
  independence_year: 1801,
  region: 'Europe',
  type: 'Kingdom',
  wikidata_id: 'Q179876'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'kuwait_1899_1961'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Kuwait',
  colony_id: 'kuwait_1899_1961',
  colony_type: 'Protectorate',
  comments: '',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.065332',
  end_date: '1961-01-01',
  established_year: 1899,
  independence_year: 1961,
  latitude: 29.166667,
  link_status: 'verified',
  longitude: 47.6,
  modern_nation_qids: ['Q817'],
  name: 'Kuwait',
  region: 'Middle East',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:49',
  start_date: '1899-01-01',
  transition_type: 'independence',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.722000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KW'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3480281'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'labuan_1846_1963'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Labuan',
  colony_id: 'labuan_1846_1963',
  colony_type: 'Crown Colony',
  comments: 'Island off Borneo coast, coal station, joined Malaysia',
  created_date: '2025-07-19T23:20:16',
  end_date: '1963-09-16',
  established_year: 1846,
  independence_year: 1963,
  link_status: 'verified',
  modern_nation_qids: ['Q833'],
  name: 'Labuan',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1846-12-24',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.854000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q6420545'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'lagos_protectorate_1887_1906'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Lagos Colony',
  colony_id: 'lagos_protectorate_1887_1906',
  colony_type: 'Protectorate',
  comments: 'Governed from Lagos Colony, incorporated into Southern Nigeria',
  created_date: '2025-07-19T18:39:07.806235',
  end_date: '1906-01-01',
  established_year: 1862,
  independence_year: 1906,
  link_status: 'verified',
  modern_nation_qids: ['Q1033'],
  name: 'Lagos Protectorate',
  region: 'West Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1887-01-01',
  transition_type: 'incorporation',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:51.161000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['NG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q472146'
};

MERGE (c:HistoricalTerritory:Federation:Colony {colony_id: 'leeward_islands_colony_1671_1816'})
SET c += {
  administrative_status: 'Federal Colony',
  canonical_name: 'Leeward Islands Colony',
  colony_id: 'leeward_islands_colony_1671_1816',
  colony_type: 'Federal Colony',
  comments: 'The first British federal colony in the Leeward Islands, which was dissolved in 1816.',
  created_date: '2025-07-20T12:11:28',
  end_date: '1816-01-01',
  established_year: 1671,
  independence_year: 1816,
  link_status: 'verified',
  modern_nation_qids: ['Q781', 'Q763', 'Q13353', 'Q25305'],
  name: 'Leeward Islands Colony (1671-1816)',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Comprehensive Missing Territories',
  start_date: '1671-01-01',
  verified: true,
  verified_date: '2025-08-06T02:08:47.163000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AG', 'KN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1796551'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'line_islands_british_1888_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Line Islands (British)',
  colony_id: 'line_islands_british_1888_1979',
  colony_type: 'Crown Colony',
  comments: 'Part of Gilbert and Ellice Islands, became part of Kiribati',
  created_date: '2025-07-19T22:13:10',
  end_date: '1979-07-12',
  established_year: 1888,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q710'],
  name: 'Line Islands (British)',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1888-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:09.231000000+00:00',
  whg_aat_types: ['300008804'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q234796'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'lower_burma_1824_1886'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Lower Burma',
  colony_id: 'lower_burma_1824_1886',
  colony_type: 'Crown Colony',
  comments: 'Territories in Lower Burma annexed by Britain after the First and Second Anglo-Burmese Wars, administered as part of British India.',
  coordinates_source: 'wikidata_batch',
  created_date: '2025-07-19T18:39:08.033603',
  end_date: '1886-01-01',
  established_year: 1824,
  independence_year: 1886,
  latitude: 22.0,
  longitude: 96.0,
  modern_nation_qids: ['Q836'],
  name: 'British Territories in Burma',
  region: 'South Asia',
  source: 'Wikipedia Territorial Evolution',
  spatial_updated: '2025-07-21T10:19:48',
  start_date: '1824-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-06T02:31:54.454000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1937196'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'lower_canada_1791_1841'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Lower Canada',
  colony_id: 'lower_canada_1791_1841',
  colony_type: 'Crown Colony',
  comments: 'Created by Constitutional Act 1791, merged into Province of Canada',
  created_date: '2025-07-19T21:45:18',
  end_date: '1841-01-01',
  established_year: 1791,
  independence_year: 1841,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'Lower Canada',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Canadian Territorial Evolution',
  start_date: '1791-01-01',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1134180'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'madras_presidency_company_1640_1858'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Madras Presidency (Company)',
  colony_id: 'madras_presidency_company_1640_1858',
  colony_type: 'Presidency',
  comments: 'Fort St. George, expanded across southern India, Carnatic Wars',
  created_date: '2025-07-19T21:53:26',
  end_date: '1858-11-01',
  established_year: 1640,
  independence_year: 1858,
  link_status: 'verified',
  modern_nation_qids: ['Q668'],
  name: 'Madras Presidency (Company)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1640-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:03.899000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1772596'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'madras_presidency_crown_1858_1947'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Madras Presidency (Crown)',
  colony_id: 'madras_presidency_crown_1858_1947',
  colony_type: 'Presidency',
  comments: 'Crown rule over southern India, Tamil Nadu, Andhra Pradesh, parts of Kerala',
  created_date: '2025-07-19T21:53:26',
  end_date: '1947-08-15',
  established_year: 1858,
  independence_year: 1947,
  link_status: 'verified',
  modern_nation_qids: ['Q668'],
  name: 'Madras Presidency (Crown)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1858-11-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:04.163000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1772596'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'mainland_british_columbia_1858_1866'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Colony of British Columbia (Mainland)',
  colony_id: 'mainland_british_columbia_1858_1866',
  colony_type: 'Crown Colony',
  comments: 'Mainland-only colony established during the Fraser Canyon Gold Rush.',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:45:18',
  end_date: '1866-08-06',
  established_year: 1858,
  independence_year: 1866,
  latitude: 51.483333333,
  link_status: 'verified',
  longitude: 7.216666666,
  modern_nation_qids: ['Q16'],
  name: 'British Columbia (Colony)',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Canadian Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1858-01-01',
  verified: true,
  verified_date: '2025-08-06T00:00:25.599000000+00:00',
  whg_aat_types: ['300387506'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2514958'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'malacca_settlement_1824_1826'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Malacca Settlement',
  colony_id: 'malacca_settlement_1824_1826',
  colony_type: 'Crown Colony',
  comments: 'Acquired from Dutch in Anglo-Dutch Treaty',
  created_date: '2025-07-19T23:20:16',
  end_date: '1826-01-01',
  established_year: 1824,
  independence_year: 1826,
  link_status: 'verified',
  modern_nation_qids: ['Q833'],
  name: 'Malacca Settlement',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1824-03-17',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.957000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q7621163'
};

MERGE (c:HistoricalTerritory:IndependentNation {colony_id: 'malaya_independent_1957_1963'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'Malaya (Independent)',
  colony_id: 'malaya_independent_1957_1963',
  colony_type: 'Independence',
  comments: 'Independent Federation of Malaya before Malaysia formation',
  created_date: '2025-07-19T23:20:17',
  end_date: '1963-09-16',
  established_year: 1957,
  independence_year: 1963,
  modern_nation_qids: ['Q833'],
  name: 'Malaya (Independent)',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1957-08-31',
  verified: false,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1479726'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'malayan_union_1946_1948'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Malayan Union',
  colony_id: 'malayan_union_1946_1948',
  colony_type: 'Crown Colony',
  comments: 'Failed attempt to unite Malayan territories',
  created_date: '2025-07-19T23:20:16',
  end_date: '1948-02-01',
  established_year: 1946,
  independence_year: 1948,
  link_status: 'verified',
  modern_nation_qids: ['Q833'],
  name: 'Malayan Union',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1946-04-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:04.442000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q976099'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'malaysia_1963'})
SET c += {
  canonical_name: 'Malaysia',
  colony_id: 'malaysia_1963',
  established_year: 1963,
  region: 'Southeast Asia',
  type: 'Independence',
  wikidata_id: 'Q833'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'maldives_protectorate_1887_1965'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Maldives Protectorate',
  colony_id: 'maldives_protectorate_1887_1965',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Sultanate of Maldives',
  created_date: '2025-07-19T23:25:07',
  end_date: '1965-07-26',
  established_year: 1887,
  independence_year: 1965,
  link_status: 'verified',
  modern_nation_qids: ['Q826'],
  name: 'Maldives Protectorate',
  region: 'South Asia',
  source: 'Indian Ocean Territories',
  start_date: '1887-12-16',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.005000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['MV'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q11344632'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'malta_1800_1964'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Malta',
  colony_id: 'malta_1800_1964',
  colony_type: 'Crown Colony',
  comments: '',
  created_date: '2025-07-19T18:39:08.351753',
  end_date: '1964-09-21',
  established_year: 1800,
  independence_year: 1964,
  link_status: 'verified',
  modern_nation_qids: ['Q233'],
  name: 'Malta',
  qid_type: 'historical_colony',
  region: 'Europe',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1800-01-01',
  transition_type: 'independence',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MT'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q6744657'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'mandatory_iraq_1920_1932'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Mandatory Iraq',
  colony_id: 'mandatory_iraq_1920_1932',
  colony_type: 'Mandate',
  comments: 'British Mandate for Mesopotamia, became Kingdom of Iraq',
  created_date: '2025-07-19T22:11:19',
  end_date: '1932-10-03',
  established_year: 1920,
  independence_year: 1932,
  link_status: 'verified',
  modern_nation_qids: ['Q796'],
  name: 'Mandatory Iraq',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1920-04-25',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.056000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IQ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q146720'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'manra_sydney_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Manra (Sydney Island)',
  colony_id: 'manra_sydney_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, transferred to Kiribati',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1860,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q710'],
  name: 'Manra (Sydney Island)',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1860-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:09.376000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q48478'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'maryland_colony_1634_1783'})
SET c += {
  administrative_status: 'Proprietary Colony',
  canonical_name: 'Maryland Colony',
  colony_id: 'maryland_colony_1634_1783',
  colony_type: 'Proprietary Colony',
  comments: 'Catholic colony founded by Lord Baltimore',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1634,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'Maryland Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1634-03-25',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:00.171000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2452027'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'massachusetts_bay_colony_1630_1783'})
SET c += {
  administrative_status: 'Charter Colony',
  canonical_name: 'Massachusetts Bay Colony',
  colony_id: 'massachusetts_bay_colony_1630_1783',
  colony_type: 'Charter Colony',
  comments: 'Puritan colony, Boston founded 1630',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1630,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'Massachusetts Bay Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1630-03-04',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:00.356000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1191350'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'mauritius_1814_1968'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Mauritius',
  colony_id: 'mauritius_1814_1968',
  colony_type: 'Crown Colony',
  comments: 'Major sugar plantation colony, important naval base and coaling station',
  created_date: '2025-07-19T23:25:06',
  end_date: '1968-01-01',
  established_year: 1814,
  independence_year: 1968,
  link_status: 'verified',
  modern_nation_qids: ['Q1027'],
  name: 'Mauritius',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  start_date: '1814-05-30',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.001000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q12053604'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'mckean_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'McKean Island',
  colony_id: 'mckean_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, transferred to Kiribati',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1860,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q710'],
  name: 'McKean Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1860-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:09.530000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q1050899'
};

MERGE (c:HistoricalTerritory:MilitaryAdministration:Colony {colony_id: 'mesopotamia_british_occupied_1914_1920'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Mesopotamia (British Occupied)',
  colony_id: 'mesopotamia_british_occupied_1914_1920',
  colony_type: 'Military Administration',
  comments: 'Occupied from Ottoman Empire during WWI',
  created_date: '2025-07-19T22:11:19',
  end_date: '1920-04-25',
  established_year: 1914,
  independence_year: 1920,
  link_status: 'verified',
  modern_nation_qids: ['Q796'],
  name: 'Mesopotamia (British Occupied)',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1914-11-06',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:05.067000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IQ'],
  whg_fclasses: ['A']
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'minorca_first_1708_1756'})
SET c += {
  canonical_name: 'Minorca (1st British)',
  colony_id: 'minorca_first_1708_1756',
  established_year: 1708,
  independence_year: 1756,
  region: 'Europe',
  type: 'Crown Colony',
  wikidata_id: 'Q173095'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'minorca_second_1763_1782'})
SET c += {
  canonical_name: 'Minorca (2nd British)',
  colony_id: 'minorca_second_1763_1782',
  established_year: 1763,
  independence_year: 1782,
  region: 'Europe',
  type: 'Crown Colony',
  wikidata_id: 'Q173095'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'minorca_third_1798_1802'})
SET c += {
  canonical_name: 'Minorca (3rd British)',
  colony_id: 'minorca_third_1798_1802',
  established_year: 1798,
  independence_year: 1802,
  region: 'Europe',
  type: 'Crown Colony',
  wikidata_id: 'Q173095'
};

MERGE (c:HistoricalTerritory:MilitaryAdministration:Colony {colony_id: 'moluccas_british_occupation_1810_1817'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Moluccas (British Occupation)',
  colony_id: 'moluccas_british_occupation_1810_1817',
  colony_type: 'Military Administration',
  comments: 'British occupation of Spice Islands during Napoleonic Wars',
  created_date: '2025-07-19T23:21:55',
  end_date: '1817-01-01',
  established_year: 1810,
  independence_year: 1817,
  modern_nation_qids: ['Q252'],
  name: 'Moluccas (British Occupation)',
  region: 'Southeast Asia',
  source: 'Additional Southeast Asian Territories',
  start_date: '1810-02-01',
  verified: false,
  whg_aat_types: ['300387081'],
  whg_ccodes: ['ID'],
  whg_fclasses: ['A']
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'montserrat_1632_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Montserrat',
  colony_id: 'montserrat_1632_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Still British Overseas Territory, volcanic island',
  created_date: '2025-07-19T22:09:32',
  established_year: 1632,
  link_status: 'verified',
  modern_nation_qids: ['Q13353'],
  name: 'Montserrat',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  start_date: '1632-01-01',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['HK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q13353'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'mosquito_coast_1638_1860'})
SET c += {
  canonical_name: 'Mosquito Coast',
  colony_id: 'mosquito_coast_1638_1860',
  established_year: 1638,
  independence_year: 1860,
  region: 'Caribbean',
  type: 'Protectorate',
  wikidata_id: 'Q1948981'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'muscat_and_oman_protectorate_1891_1971'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Muscat and Oman Protectorate',
  colony_id: 'muscat_and_oman_protectorate_1891_1971',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Sultanate of Muscat and Oman',
  created_date: '2025-07-19T22:11:19',
  end_date: '1971-01-01',
  established_year: 1891,
  independence_year: 1971,
  link_status: 'verified',
  modern_nation_qids: ['Q842'],
  name: 'Muscat and Oman Protectorate',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1891-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.210000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['OM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q157734'
};

MERGE (c:HistoricalTerritory:BoerRepublic {colony_id: 'natalia_republic_1839_1843'})
SET c += {
  administrative_status: 'Boer Republic',
  canonical_name: 'Natalia Republic',
  colony_id: 'natalia_republic_1839_1843',
  colony_type: 'Boer Republic',
  comments: 'Voortrekker republic in Natal, annexed by Britain 1843',
  created_date: '2025-07-19T22:00:07',
  end_date: '1843-08-04',
  established_year: 1839,
  independence_year: 1843,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Natalia Republic',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1839-10-05',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:52.209000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1029847'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'nauru_1920_1968'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Nauru',
  colony_id: 'nauru_1920_1968',
  colony_type: 'Mandate',
  comments: 'Former German possession, phosphate mining island',
  created_date: '2025-07-19T22:13:10',
  end_date: '1968-01-01',
  established_year: 1920,
  independence_year: 1968,
  link_status: 'verified',
  modern_nation_qids: ['Q697'],
  name: 'Nauru',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1920-12-17',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:55.913000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['NR'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q21816219'
};

MERGE (c:HistoricalTerritory:MilitaryAdministration:Colony {colony_id: 'netherlands_east_indies_british_administration_1945_1946'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Netherlands East Indies (British Administration)',
  colony_id: 'netherlands_east_indies_british_administration_1945_1946',
  colony_type: 'Military Administration',
  comments: 'Brief British military administration after Japanese surrender before Dutch return',
  created_date: '2025-07-19T23:21:55',
  end_date: '1946-11-30',
  established_year: 1945,
  independence_year: 1946,
  modern_nation_qids: ['Q252'],
  name: 'Netherlands East Indies (British Administration)',
  region: 'Southeast Asia',
  source: 'Additional Southeast Asian Territories',
  start_date: '1945-09-29',
  verified: false,
  whg_aat_types: ['300387081'],
  whg_ccodes: ['ID'],
  whg_fclasses: ['A']
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'new_brunswick_1784_1867'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'New Brunswick',
  colony_id: 'new_brunswick_1784_1867',
  colony_type: 'Crown Colony',
  comments: 'Separated from Nova Scotia, became province of Canada',
  created_date: '2025-07-19T18:39:08.201508',
  end_date: '1867-07-01',
  established_year: 1784,
  independence_year: 1867,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'New Brunswick',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1784-01-01',
  transition_type: 'federation',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q107499350'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'new_brunswick_province_1867'})
SET c += {
  canonical_name: 'New Brunswick (Province)',
  colony_id: 'new_brunswick_province_1867',
  colony_type: 'Province',
  established_year: 1867,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1965'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'new_france_1608_1763'})
SET c += {
  administrative_status: 'Colonial Empire',
  canonical_name: 'New France',
  colony_id: 'new_france_1608_1763',
  colony_type: 'Colonial Empire',
  comments: 'French colonial empire in North America, ended with Treaty of Paris 1763',
  created_date: '2025-07-20T16:50:25',
  end_date: '1763-02-10',
  established_year: 1608,
  independence_year: 1763,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'New France',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'French Colonial System',
  start_date: '1608-07-03',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q170604'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'new_hampshire_colony_1623_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'New Hampshire Colony',
  colony_id: 'new_hampshire_colony_1623_1783',
  colony_type: 'Royal Colony',
  comments: 'Separated from Massachusetts 1679',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1629,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'New Hampshire Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1623-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:00.421000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1617382'
};

MERGE (c:HistoricalTerritory:Condominium:Colony {colony_id: 'new_hebrides_1906_1980'})
SET c += {
  administrative_status: 'Anglo-French Condominium',
  canonical_name: 'New Hebrides',
  colony_id: 'new_hebrides_1906_1980',
  colony_type: 'Anglo-French Condominium',
  comments: 'Joint British-French administration',
  created_date: '2025-07-19T22:13:09',
  end_date: '1980-07-30',
  established_year: 1906,
  independence_year: 1980,
  link_status: 'verified',
  modern_nation_qids: ['Q686'],
  name: 'New Hebrides',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1906-02-27',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.058000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['VU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q752431'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'new_jersey_colony_1664_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'New Jersey Colony',
  colony_id: 'new_jersey_colony_1664_1783',
  colony_type: 'Royal Colony',
  comments: 'Divided into East/West Jersey, reunited 1702',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1664,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'New Jersey Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1664-09-08',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:00.532000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2335128'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'new_south_wales_original_1788_1901'})
SET c += {
  administrative_status: 'Penal Colony',
  canonical_name: 'New South Wales',
  colony_id: 'new_south_wales_original_1788_1901',
  colony_type: 'Penal Colony',
  comments: 'Original colony covering most of eastern Australia, gradually subdivided',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:49:47',
  end_date: '1901-01-01',
  established_year: 1788,
  independence_year: 1901,
  latitude: -32.0,
  link_status: 'verified',
  longitude: 147.0,
  modern_nation_qids: ['Q408'],
  name: 'New South Wales (Original)',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1788-01-26',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:09.601000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q18348382'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'new_york_colony_1664_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'New York Colony',
  colony_id: 'new_york_colony_1664_1783',
  colony_type: 'Royal Colony',
  comments: 'Captured from Dutch New Amsterdam',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1664,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'New York Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1664-09-08',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:00.646000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q769668'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'new_zealand_colony_1840_1907'})
SET c += {
  canonical_name: 'New Zealand Colony',
  colony_id: 'new_zealand_colony_1840_1907',
  established_year: 1840,
  independence_year: 1907,
  region: 'Pacific',
  type: 'Crown Colony',
  wikidata_id: 'Q664'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'new_zealand_independent_1947'})
SET c += {
  canonical_name: 'New Zealand',
  colony_id: 'new_zealand_independent_1947',
  established_year: 1947,
  region: 'Pacific',
  type: 'Independence',
  wikidata_id: 'Q664'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'newfoundland_commission_1934_1949'})
SET c += {
  canonical_name: 'Newfoundland (Commission)',
  colony_id: 'newfoundland_commission_1934_1949',
  established_year: 1934,
  independence_year: 1949,
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q5152678'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'newfoundland_province_1949'})
SET c += {
  canonical_name: 'Newfoundland and Labrador',
  colony_id: 'newfoundland_province_1949',
  colony_type: 'Province',
  established_year: 1949,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q2003'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'niger_coast_protectorate_1893_1900'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Niger Coast Protectorate',
  colony_id: 'niger_coast_protectorate_1893_1900',
  colony_type: 'Protectorate',
  comments: 'Renamed Oil Rivers Protectorate',
  created_date: '2025-07-19T22:03:12',
  end_date: '1900-01-01',
  established_year: 1893,
  independence_year: 1900,
  link_status: 'verified',
  modern_nation_qids: ['Q1033'],
  name: 'Niger Coast Protectorate',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1893-05-12',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.155000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['NG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2566427'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'norfolk_island_1788_1914'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Norfolk Island',
  colony_id: 'norfolk_island_1788_1914',
  colony_type: 'Crown Colony',
  comments: 'Penal settlement, transferred to Australian administration',
  created_date: '2025-07-19T22:13:10',
  end_date: '1914-07-01',
  established_year: 1788,
  independence_year: 1914,
  link_status: 'verified',
  modern_nation_qids: ['Q31057'],
  name: 'Norfolk Island',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1788-03-06',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:09.843000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q31057'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'norfolk_island_whaling_station_1830_1870'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'Norfolk Island Whaling Station',
  colony_id: 'norfolk_island_whaling_station_1830_1870',
  colony_type: 'Whaling Station',
  comments: 'Seasonal whaling operations around Norfolk Island',
  created_date: '2025-07-20T11:26:12',
  end_date: '1870-12-31',
  established_year: 1830,
  independence_year: 1870,
  link_status: 'verified',
  modern_nation_qids: ['Q31057'],
  name: 'Norfolk Island Whaling Station',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1830-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:10.246000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q31057'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'north_borneo_crown_colony_1946_1963'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'North Borneo Crown Colony',
  colony_id: 'north_borneo_crown_colony_1946_1963',
  colony_type: 'Crown Colony',
  comments: 'Crown colony before joining Malaysia as Sabah',
  created_date: '2025-07-19T23:20:16',
  end_date: '1963-09-16',
  established_year: 1946,
  independence_year: 1963,
  link_status: 'verified',
  modern_nation_qids: ['Q833'],
  name: 'North Borneo Crown Colony',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1946-07-15',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.256000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q16933920'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'north_carolina_colony_1663_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'North Carolina Colony',
  colony_id: 'north_carolina_colony_1663_1783',
  colony_type: 'Royal Colony',
  comments: 'Originally part of Carolina, split 1712',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1663,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'North Carolina Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1663-03-24',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:01.034000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2334526'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'north_west_frontier_province_1901_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'North-West Frontier Province',
  colony_id: 'north_west_frontier_province_1901_1947',
  colony_type: 'Province',
  comments: 'Created from districts of Punjab, joined Pakistan 1947',
  created_date: '2025-07-19T21:53:27',
  end_date: '1947-08-15',
  established_year: 1901,
  independence_year: 1947,
  link_status: 'verified',
  modern_nation_qids: ['Q843'],
  name: 'North-West Frontier Province',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1901-11-09',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.305000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['PK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4412467'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'north_western_territory_1670_1870'})
SET c += {
  administrative_status: 'Territory',
  canonical_name: 'North-Western Territory',
  colony_id: 'north_western_territory_1670_1870',
  colony_type: 'Territory',
  comments: 'Transferred to Canada with Rupert\'s Land',
  created_date: '2025-07-19T21:45:18',
  end_date: '1870-07-15',
  established_year: 1670,
  independence_year: 1870,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'North-Western Territory',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Canadian Territorial Evolution',
  start_date: '1670-01-01',
  verified: true,
  whg_aat_types: ['300387081'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1998931'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'northern_ireland_1920'})
SET c += {
  canonical_name: 'Northern Ireland',
  colony_id: 'northern_ireland_1920',
  established_year: 1920,
  region: 'Europe',
  type: 'Devolved Government',
  wikidata_id: 'Q26'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'northern_nigeria_1900_1914'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Northern Nigeria',
  colony_id: 'northern_nigeria_1900_1914',
  colony_type: 'Protectorate',
  comments: 'Merged with Southern Nigeria to form Nigeria',
  created_date: '2025-07-19T18:39:07.832282',
  end_date: '1914-01-01',
  established_year: 1900,
  independence_year: 1914,
  link_status: 'verified',
  modern_nation_qids: ['Q1033'],
  name: 'Northern Nigeria',
  region: 'West Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1900-01-01',
  transition_type: 'merger',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.212000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['NG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q585408'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'northern_rhodesia_colony_1924_1953'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Northern Rhodesia Colony',
  colony_id: 'northern_rhodesia_colony_1924_1953',
  colony_type: 'Crown Colony',
  comments: 'Crown colony after BSAC rule ended, before federation',
  created_date: '2025-07-19T22:06:51',
  end_date: '1953-08-01',
  established_year: 1924,
  independence_year: 1953,
  link_status: 'verified',
  modern_nation_qids: ['Q954', 'Q953'],
  name: 'Northern Rhodesia Colony',
  region: 'Southern Africa',
  source: 'East African Territorial Evolution',
  start_date: '1924-04-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.539000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZW', 'ZM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q953903'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'northern_rhodesia_post_federation_1964'})
SET c += {
  canonical_name: 'Northern Rhodesia',
  colony_id: 'northern_rhodesia_post_federation_1964',
  established_year: 1963,
  independence_year: 1964,
  region: 'Southern Africa',
  type: 'Transitional',
  wikidata_id: 'Q953903'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'northern_territories_gold_coast_1897_1957'})
SET c += {
  canonical_name: 'Northern Territories of the Gold Coast',
  colony_id: 'northern_territories_gold_coast_1897_1957',
  established_year: 1897,
  independence_year: 1957,
  region: 'West Africa',
  type: 'Protectorate',
  wikidata_id: 'Q2000610'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'nova_scotia_post_1784_1867'})
SET c += {
  canonical_name: 'Nova Scotia',
  colony_id: 'nova_scotia_post_1784_1867',
  established_year: 1784,
  independence_year: 1867,
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q98931415'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'nova_scotia_pre_1713_1784'})
SET c += {
  canonical_name: 'Nova Scotia',
  colony_id: 'nova_scotia_pre_1713_1784',
  established_year: 1713,
  independence_year: 1784,
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q98931415'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'nova_scotia_province_1867'})
SET c += {
  canonical_name: 'Nova Scotia (Province)',
  colony_id: 'nova_scotia_province_1867',
  colony_type: 'Province',
  established_year: 1867,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1952'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'nunavut_1999'})
SET c += {
  canonical_name: 'Nunavut',
  colony_id: 'nunavut_1999',
  colony_type: 'Territory',
  established_year: 1999,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q2023'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'nyasaland_1891_1964'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Nyasaland',
  colony_id: 'nyasaland_1891_1964',
  colony_type: 'Protectorate',
  comments: 'Known as Nyasaland Districts until 1893, British Central Africa until 1907',
  created_date: '2025-07-19T18:39:07.864213',
  end_date: '1964-01-01',
  established_year: 1891,
  independence_year: 1953,
  link_status: 'verified',
  modern_nation_qids: ['Q1020'],
  name: 'Nyasaland',
  region: 'Southern Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1891-01-01',
  transition_type: 'independence',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.695000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MW'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1649306'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'nyasaland_post_federation_1963'})
SET c += {
  canonical_name: 'Nyasaland',
  colony_id: 'nyasaland_post_federation_1963',
  comments: 'Brief return to colonial status after Federation dissolution',
  created_date: '2025-07-20T12:01:56',
  end_date: '1964-07-06',
  entity_type: 'Crown Colony',
  established_year: 1963,
  independence_year: 1964,
  link_status: 'verified',
  modern_nation_qids: ['Q1020'],
  name: 'Nyasaland (Post-Federation)',
  region: 'Southern Africa',
  source: 'Temporal Model Fix - Federation Dissolution',
  start_date: '1964-01-01',
  type: 'Transitional',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.596000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MW'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1649306'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'ocean_island_banaba_1900_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Ocean Island (Banaba)',
  colony_id: 'ocean_island_banaba_1900_1979',
  colony_type: 'Crown Colony',
  comments: 'Phosphate mining island, became part of Kiribati',
  created_date: '2025-07-19T22:13:10',
  end_date: '1979-07-12',
  established_year: 1900,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q710'],
  name: 'Ocean Island (Banaba)',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1900-09-28',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.172000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q271901'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'oeno_island_1902_ongoing'})
SET c += {
  administrative_status: 'Remote Island',
  canonical_name: 'Oeno Island',
  colony_id: 'oeno_island_1902_ongoing',
  colony_type: 'Remote Island',
  comments: 'Part of Pitcairn Islands group, coral atoll',
  created_date: '2025-07-20T11:26:12',
  established_year: 1902,
  link_status: 'verified',
  modern_nation_qids: ['Q35672'],
  name: 'Oeno Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1902-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:10.638000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['PN'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q35672'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'oil_rivers_protectorate_1885_1893'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Oil Rivers Protectorate',
  colony_id: 'oil_rivers_protectorate_1885_1893',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Niger Delta trading states',
  created_date: '2025-07-19T22:03:12',
  end_date: '1893-05-12',
  established_year: 1885,
  independence_year: 1893,
  link_status: 'verified',
  modern_nation_qids: ['Q1033'],
  name: 'Oil Rivers Protectorate',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1885-06-05',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.758000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['NG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2566427'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'ontario_1867'})
SET c += {
  canonical_name: 'Ontario',
  colony_id: 'ontario_1867',
  colony_type: 'Province',
  established_year: 1867,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1904'
};

MERGE (c:HistoricalTerritory:BoerRepublic {colony_id: 'orange_free_state_1854_1900'})
SET c += {
  administrative_status: 'Boer Republic',
  canonical_name: 'Orange Free State',
  colony_id: 'orange_free_state_1854_1900',
  colony_type: 'Boer Republic',
  comments: 'Independent Boer republic, conquered during Second Boer War',
  created_date: '2025-07-19T22:00:07',
  end_date: '1900-05-28',
  established_year: 1854,
  independence_year: 1900,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Orange Free State',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1854-02-23',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:52.312000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q218023'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'orange_river_colony_1900_1910'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Orange River Colony',
  colony_id: 'orange_river_colony_1900_1910',
  colony_type: 'Crown Colony',
  comments: 'Orange Free State conquered and renamed, gained self-government 1907',
  created_date: '2025-07-19T22:00:07',
  end_date: '1910-05-31',
  established_year: 1900,
  independence_year: 1910,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Orange River Colony',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1900-05-28',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:52.576000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1142179'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'orange_river_sovereignty_1848_1854'})
SET c += {
  administrative_status: 'British Sovereignty',
  canonical_name: 'Orange River Sovereignty',
  colony_id: 'orange_river_sovereignty_1848_1854',
  colony_type: 'British Sovereignty',
  comments: 'British sovereignty between Orange and Vaal rivers, abandoned in Bloemfontein Convention',
  created_date: '2025-07-19T22:00:07',
  end_date: '1854-02-23',
  established_year: 1848,
  independence_year: 1854,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Orange River Sovereignty',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1848-02-03',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:52.738000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3048062'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'palestine_1920_1948'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Palestine',
  colony_id: 'palestine_1920_1948',
  colony_type: 'Mandate',
  comments: 'British mandate dissolved; Israel established, ongoing territorial dispute',
  created_date: '2025-07-19T18:39:08.103306',
  end_date: '1948-01-01',
  established_year: 1920,
  independence_year: 1948,
  link_status: 'verified',
  modern_nation_qids: ['Q219060', 'Q801'],
  name: 'Palestine',
  region: 'Middle East',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1920-01-01',
  transition_type: 'dissolution',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.683000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q193714'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'penang_prince_of_wales_island_1786_1826'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Penang (Prince of Wales Island)',
  colony_id: 'penang_prince_of_wales_island_1786_1826',
  colony_type: 'Trading Post',
  comments: 'First British settlement in Southeast Asia, acquired from Sultan of Kedah',
  created_date: '2025-07-19T23:20:16',
  end_date: '1826-01-01',
  established_year: 1786,
  independence_year: 1826,
  link_status: 'verified',
  modern_nation_qids: ['Q833'],
  name: 'Penang (Prince of Wales Island)',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1786-08-11',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.745000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1150673'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'pennsylvania_colony_1681_1783'})
SET c += {
  administrative_status: 'Proprietary Colony',
  canonical_name: 'Pennsylvania Colony',
  colony_id: 'pennsylvania_colony_1681_1783',
  colony_type: 'Proprietary Colony',
  comments: 'William Penn\'s Quaker colony, Philadelphia',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1681,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'Pennsylvania Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1681-03-04',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:01.078000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2475732'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'phoenix_islands_1937_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Phoenix Islands',
  colony_id: 'phoenix_islands_1937_1979',
  colony_type: 'Crown Colony',
  comments: 'Part of Gilbert and Ellice Islands, became part of Kiribati',
  created_date: '2025-07-19T22:13:10',
  end_date: '1979-07-12',
  established_year: 1937,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q710'],
  name: 'Phoenix Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1937-06-18',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:10.715000000+00:00',
  whg_aat_types: ['300008804'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q271674'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'pitcairn_islands_1838_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Pitcairn Islands',
  colony_id: 'pitcairn_islands_1838_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Settlement of Bounty mutineers, still British territory',
  created_date: '2025-07-19T22:13:10',
  established_year: 1838,
  link_status: 'verified',
  modern_nation_qids: ['Q35672'],
  name: 'Pitcairn Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1838-11-30',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:10.863000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q35672'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'prince_edward_island_1769_1873'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Prince Edward Island',
  colony_id: 'prince_edward_island_1769_1873',
  colony_type: 'Crown Colony',
  comments: 'Known as New Ireland until 1769, St. John\'s Island until 1799',
  created_date: '2025-07-19T18:39:08.216646',
  end_date: '1873-01-01',
  established_year: 1769,
  independence_year: 1873,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'Prince Edward Island',
  qid_notes: 'QID needs verification - historical colony entity vs modern province',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1769-01-01',
  transition_type: 'federation',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q137324703'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'prince_edward_island_province_1873'})
SET c += {
  canonical_name: 'Prince Edward Island (Province)',
  colony_id: 'prince_edward_island_province_1873',
  colony_type: 'Province',
  established_year: 1873,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1979'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'princely_states_placeholder_1818_1947'})
SET c += {
  canonical_name: 'Princely States (placeholder)',
  colony_id: 'princely_states_placeholder_1818_1947',
  established_year: 1818,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Princely State',
  wikidata_id: 'Q1336152'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'province_of_canada_1841_1867'})
SET c += {
  administrative_status: 'United Province',
  canonical_name: 'Province of Canada',
  colony_id: 'province_of_canada_1841_1867',
  colony_type: 'United Province',
  comments: 'Union of Upper and Lower Canada, split into Ontario and Quebec at Confederation',
  created_date: '2025-07-19T21:45:18',
  end_date: '1867-07-01',
  established_year: 1841,
  independence_year: 1867,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'Province of Canada',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Canadian Territorial Evolution',
  start_date: '1841-01-01',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1121436'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'province_of_freedom_1787_1792'})
SET c += {
  administrative_status: 'Settlement',
  canonical_name: 'Province of Freedom',
  colony_id: 'province_of_freedom_1787_1792',
  colony_type: 'Settlement',
  comments: 'First settlement for freed slaves, failed due to conflicts',
  created_date: '2025-07-19T22:03:12',
  end_date: '1792-01-01',
  established_year: 1787,
  independence_year: 1792,
  link_status: 'verified',
  modern_nation_qids: ['Q1044'],
  name: 'Province of Freedom',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1787-05-09',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:52.786000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SL'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q11300378'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'province_of_quebec_british_1763_1791'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Province of Quebec (British)',
  colony_id: 'province_of_quebec_british_1763_1791',
  colony_type: 'Crown Colony',
  comments: 'British conquest of New France, Quebec Act 1774',
  created_date: '2025-07-20T12:11:27',
  end_date: '1791-12-26',
  established_year: 1763,
  independence_year: 1791,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'Province of Quebec (British)',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1763-10-07',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:01.128000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q251668'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'punjab_province_1849_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Punjab Province',
  colony_id: 'punjab_province_1849_1947',
  colony_type: 'Province',
  comments: 'Annexed after Second Anglo-Sikh War, partitioned 1947 between India and Pakistan',
  created_date: '2025-07-19T21:53:26',
  end_date: '1947-08-15',
  established_year: 1849,
  independence_year: 1947,
  link_status: 'verified',
  modern_nation_qids: ['Q668', 'Q843'],
  name: 'Punjab Province',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1849-03-30',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.802000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN', 'PK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2629708'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'qatar_protectorate_1916_1971'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Qatar Protectorate',
  colony_id: 'qatar_protectorate_1916_1971',
  colony_type: 'Protectorate',
  comments: 'British protectorate replacing Ottoman rule',
  created_date: '2025-07-19T22:11:19',
  end_date: '1971-09-03',
  established_year: 1916,
  independence_year: 1971,
  link_status: 'verified',
  modern_nation_qids: ['Q846'],
  name: 'Qatar Protectorate',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1916-11-03',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.921000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['QA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q105633777'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'quebec_1867'})
SET c += {
  canonical_name: 'Quebec',
  colony_id: 'quebec_1867',
  colony_type: 'Province',
  established_year: 1867,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q176'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'queensland_1859_1901'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Queensland',
  colony_id: 'queensland_1859_1901',
  colony_type: 'Crown Colony',
  comments: 'Northern NSW separated as Queensland, immediately self-governing',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:49:48',
  end_date: '1901-01-01',
  established_year: 1859,
  independence_year: 1901,
  latitude: -26.0,
  link_status: 'verified',
  longitude: 121.0,
  modern_nation_qids: ['Q408'],
  name: 'Queensland',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1859-06-06',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:11.146000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q28401203'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'rawaki_phoenix_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Rawaki (Phoenix Island)',
  colony_id: 'rawaki_phoenix_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, transferred to Kiribati',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1860,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q710'],
  name: 'Rawaki (Phoenix Island)',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1860-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:11.257000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q1059295'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'red_river_colony_1811_1870'})
SET c += {
  canonical_name: 'Red River Colony',
  colony_id: 'red_river_colony_1811_1870',
  established_year: 1811,
  independence_year: 1870,
  region: 'North America',
  type: 'Colony',
  wikidata_id: 'Q1143638'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'rhode_island_colony_1636_1783'})
SET c += {
  administrative_status: 'Charter Colony',
  canonical_name: 'Rhode Island Colony',
  colony_id: 'rhode_island_colony_1636_1783',
  colony_type: 'Charter Colony',
  comments: 'Founded by Roger Williams, religious tolerance',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1636,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'Rhode Island Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1636-06-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:01.237000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2335224'
};

MERGE (c:HistoricalTerritory:IndependentNation {colony_id: 'rhodesia_udi_1965_1979'})
SET c += {
  administrative_status: 'Unilateral Independence',
  canonical_name: 'Rhodesia (UDI)',
  colony_id: 'rhodesia_udi_1965_1979',
  colony_type: 'Unilateral Independence',
  comments: 'Unilateral Declaration of Independence by white minority government',
  created_date: '2025-07-19T22:06:51',
  end_date: '1979-06-01',
  established_year: 1965,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q954', 'Q953'],
  name: 'Rhodesia (UDI)',
  region: 'Southern Africa',
  source: 'East African Territorial Evolution',
  start_date: '1965-11-11',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.811000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZW', 'ZM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q217169'
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'rodrigues_1814_1968'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Rodrigues',
  colony_id: 'rodrigues_1814_1968',
  colony_type: 'Dependency',
  comments: 'Dependency of Mauritius, important way station',
  created_date: '2025-07-19T23:25:06',
  end_date: '1968-03-12',
  established_year: 1814,
  independence_year: 1968,
  link_status: 'verified',
  modern_nation_qids: ['Q1027'],
  name: 'Rodrigues',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  start_date: '1814-05-30',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:52.846000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['MU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q208668'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'royal_niger_company_territory_1886_1900'})
SET c += {
  administrative_status: 'Company Territory',
  canonical_name: 'Royal Niger Company Territory',
  colony_id: 'royal_niger_company_territory_1886_1900',
  colony_type: 'Company Territory',
  comments: 'Royal Niger Company controlled interior Nigeria',
  created_date: '2025-07-19T22:03:12',
  end_date: '1900-01-01',
  established_year: 1886,
  independence_year: 1900,
  link_status: 'verified',
  modern_nation_qids: ['Q1033'],
  name: 'Royal Niger Company Territory',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1886-07-10',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.896000000+00:00',
  whg_aat_types: ['300387081'],
  whg_ccodes: ['NG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1806380'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'ruperts_land_1670_1870'})
SET c += {
  administrative_status: 'Hudson\'s Bay Company Territory',
  canonical_name: 'Rupert\'s Land',
  colony_id: 'ruperts_land_1670_1870',
  colony_type: 'Hudson\'s Bay Company Territory',
  comments: 'Vast HBC territory, sold to Canada 1870, became Manitoba and Northwest Territories',
  created_date: '2025-07-19T21:45:18',
  end_date: '1870-07-15',
  established_year: 1670,
  independence_year: 1870,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'Rupert\'s Land',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Canadian Territorial Evolution',
  start_date: '1670-01-01',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q738395'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'saint_christopher_nevis_anguilla_1958_1983'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Saint Kitts and Nevis Colony',
  colony_id: 'saint_christopher_nevis_anguilla_1958_1983',
  colony_type: 'Crown Colony',
  comments: 'First British settlement in Caribbean, mother colony of West Indies',
  created_date: '2025-07-19T22:09:32',
  end_date: '1983-09-19',
  established_year: 1624,
  independence_year: 1983,
  modern_nation_qids: ['Q763'],
  name: 'Saint Christopher-Nevis-Anguilla',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  start_date: '1958-01-03',
  verified: true,
  verified_date: '2025-08-06T02:06:38.945000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1637975'
};

MERGE (c:HistoricalTerritory:OverseasTerritory:Colony {colony_id: 'saint_helena_ascension_and_tristan_da_cunha_1588_ongoing'})
SET c += {
  administrative_status: 'British Overseas Territory',
  canonical_name: 'Saint Helena, Ascension and Tristan da Cunha',
  colony_id: 'saint_helena_ascension_and_tristan_da_cunha_1588_ongoing',
  colony_type: 'British Overseas Territory',
  comments: 'Formerly St. Helena and its Dependencies',
  created_date: '2025-07-19T18:39:08.388916',
  established_year: 1588,
  link_status: 'verified',
  modern_nation_qids: ['Q192184'],
  name: 'Saint Helena, Ascension and Tristan da Cunha',
  region: 'Atlantic',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1588-01-01',
  transition_type: 'ongoing',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:07.985000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q192184'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'saint_lucia_colony_1814_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Saint Lucia Colony',
  colony_id: 'saint_lucia_colony_1814_1979',
  colony_type: 'Crown Colony',
  comments: 'Ceded by France after Napoleonic Wars',
  created_date: '2025-07-19T22:09:32',
  end_date: '1979-02-22',
  established_year: 1814,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q760'],
  name: 'Saint Lucia Colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  start_date: '1814-05-30',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:55.834000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['LC'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q15238409'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'sarawak_1841_1946'})
SET c += {
  administrative_status: 'Personal Rule',
  canonical_name: 'Sarawak',
  colony_id: 'sarawak_1841_1946',
  colony_type: 'Personal Rule',
  comments: 'Kingdom of Sarawak under Brooke family, British protection from 1888',
  created_date: '2025-07-19T23:20:16',
  end_date: '1946-07-01',
  established_year: 1841,
  independence_year: 1946,
  link_status: 'verified',
  modern_nation_qids: ['Q833'],
  name: 'Sarawak',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1841-09-24',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:54.964000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1658411'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'sarawak_crown_colony_1946_1963'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Sarawak Crown Colony',
  colony_id: 'sarawak_crown_colony_1946_1963',
  colony_type: 'Crown Colony',
  comments: 'Crown colony before joining Malaysia',
  created_date: '2025-07-19T23:20:16',
  end_date: '1963-09-16',
  established_year: 1946,
  independence_year: 1963,
  link_status: 'verified',
  modern_nation_qids: ['Q833'],
  name: 'Sarawak Crown Colony',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1946-07-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:55.041000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5589708'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'saskatchewan_1905'})
SET c += {
  canonical_name: 'Saskatchewan',
  colony_id: 'saskatchewan_1905',
  colony_type: 'Province',
  established_year: 1905,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1989'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'settlement_of_belize_1798_1862'})
SET c += {
  administrative_status: 'Supervised Settlement',
  canonical_name: 'English settlement of Belize',
  colony_id: 'settlement_of_belize_1798_1862',
  comments: 'De facto British territory secured after the Battle of St. George\'s Caye, administered by a superintendent under the Governor of Jamaica.',
  end_date: '1862-01-01',
  established_year: 1798,
  independence_year: 1862,
  modern_nation_qids: ['Q242'],
  name: 'Settlement of Belize',
  region: 'Caribbean',
  source: 'Manual Correction',
  start_date: '1798-09-10',
  verified: true,
  verified_date: '2025-08-06T00:19:01.728000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BZ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q115829224'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'seychelles_1903_1976'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Seychelles',
  colony_id: 'seychelles_1903_1976',
  colony_type: 'Crown Colony',
  comments: 'Separate crown colony from 1903',
  created_date: '2025-07-19T23:25:06',
  end_date: '1976-01-01',
  established_year: 1903,
  independence_year: 1976,
  link_status: 'verified',
  modern_nation_qids: ['Q1042'],
  name: 'Seychelles',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  start_date: '1903-08-31',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.948000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SC'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q21821453'
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'seychelles_mauritius_dependency_1814_1903'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Seychelles (Mauritius Dependency)',
  colony_id: 'seychelles_mauritius_dependency_1814_1903',
  colony_type: 'Dependency',
  comments: 'Administered as dependency of Mauritius',
  created_date: '2025-07-19T23:25:06',
  end_date: '1903-08-31',
  established_year: 1814,
  independence_year: 1903,
  link_status: 'verified',
  modern_nation_qids: ['Q1027'],
  name: 'Seychelles (Mauritius Dependency)',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  start_date: '1814-05-30',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:57.990000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q21821453'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'shanghai_international_settlement_1863_1943'})
SET c += {
  administrative_status: 'International Settlement',
  canonical_name: 'Shanghai International Settlement',
  colony_id: 'shanghai_international_settlement_1863_1943',
  colony_type: 'International Settlement',
  comments: 'Joint British-American administration in Shanghai',
  created_date: '2025-07-19T23:21:55',
  end_date: '1943-08-01',
  established_year: 1863,
  independence_year: 1943,
  link_status: 'verified',
  modern_nation_qids: ['Q148'],
  name: 'Shanghai International Settlement',
  region: 'Southeast Asia',
  source: 'Additional Southeast Asian Territories',
  start_date: '1863-09-21',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:05.193000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2170587'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'sierra_leone_colony_1808_1896'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Sierra Leone Colony',
  colony_id: 'sierra_leone_colony_1808_1896',
  colony_type: 'Crown Colony',
  comments: 'Crown colony centered on Freetown',
  created_date: '2025-07-19T22:03:12',
  end_date: '1896-08-31',
  established_year: 1808,
  independence_year: 1896,
  link_status: 'verified',
  modern_nation_qids: ['Q1044'],
  name: 'Sierra Leone Colony',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1808-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:58.059000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SL'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q30059027'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'sierra_leone_colony_and_protectorate_1787_1961'})
SET c += {
  administrative_status: 'Colony/Protectorate',
  canonical_name: 'Sierra Leone Colony and Protectorate',
  colony_id: 'sierra_leone_colony_and_protectorate_1787_1961',
  colony_type: 'Colony/Protectorate',
  comments: 'Complex administrative history with multiple reorganizations',
  created_date: '2025-07-19T18:39:07.888048',
  end_date: '1961-01-01',
  established_year: 1896,
  independence_year: 1961,
  link_status: 'verified',
  modern_nation_qids: ['Q1044'],
  name: 'Sierra Leone Colony and Protectorate',
  region: 'West Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1787-01-01',
  transition_type: 'independence',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:52.909000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['SL'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q30059027'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'sierra_leone_company_settlement_1792_1808'})
SET c += {
  administrative_status: 'Company Settlement',
  canonical_name: 'Sierra Leone Company Settlement',
  colony_id: 'sierra_leone_company_settlement_1792_1808',
  colony_type: 'Company Settlement',
  comments: 'Sierra Leone Company administered Freetown',
  created_date: '2025-07-19T22:03:12',
  end_date: '1808-01-01',
  established_year: 1792,
  independence_year: 1808,
  link_status: 'verified',
  modern_nation_qids: ['Q1044'],
  name: 'Sierra Leone Company Settlement',
  region: 'West Africa',
  source: 'West African Territorial Evolution',
  start_date: '1792-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:13.282000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SL'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3483448'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'sind_province_1843_1947'})
SET c += {
  canonical_name: 'Sind',
  colony_id: 'sind_province_1843_1947',
  established_year: 1936,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Province',
  wikidata_id: 'Q7523949'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'singapore_crown_colony_1946_1963'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Singapore Crown Colony',
  colony_id: 'singapore_crown_colony_1946_1963',
  colony_type: 'Crown Colony',
  comments: 'Separated from Straits Settlements, joined Malaysia 1963',
  created_date: '2025-07-19T23:20:17',
  end_date: '1963-09-16',
  established_year: 1946,
  independence_year: 1963,
  link_status: 'verified',
  modern_nation_qids: ['Q334'],
  name: 'Singapore Crown Colony',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1946-04-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:05.871000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4373718'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'singapore_independent_1965'})
SET c += {
  canonical_name: 'Singapore',
  colony_id: 'singapore_independent_1965',
  established_year: 1965,
  region: 'Southeast Asia',
  type: 'Independence',
  wikidata_id: 'Q334'
};

MERGE (c:HistoricalTerritory:CompanyTerritory:Colony {colony_id: 'singapore_settlement_1819_1826'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Singapore Settlement',
  colony_id: 'singapore_settlement_1819_1826',
  colony_type: 'Trading Post',
  comments: 'Founded by Stamford Raffles, strategic port',
  created_date: '2025-07-19T23:20:16',
  end_date: '1826-01-01',
  established_year: 1819,
  independence_year: 1826,
  link_status: 'verified',
  modern_nation_qids: ['Q334'],
  name: 'Singapore Settlement',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1819-01-29',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:55.182000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4420036'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'socotra_island_1886_1967'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Socotra Island',
  colony_id: 'socotra_island_1886_1967',
  colony_type: 'Protectorate',
  comments: 'Strategic island in Arabian Sea, part of Aden Protectorate',
  created_date: '2025-07-19T22:11:19',
  end_date: '1967-11-30',
  established_year: 1886,
  independence_year: 1967,
  link_status: 'verified',
  modern_nation_qids: ['Q805'],
  name: 'Socotra Island',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1886-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:05.988000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['YE'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q82859'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'somali_republic_1960'})
SET c += {
  canonical_name: 'Somali Republic',
  colony_id: 'somali_republic_1960',
  established_year: 1960,
  region: 'Middle East',
  type: 'Independence',
  wikidata_id: 'Q1045'
};

MERGE (c:HistoricalTerritory:BoerRepublic {colony_id: 'south_african_republic_restored_1881_1900'})
SET c += {
  administrative_status: 'Boer Republic',
  canonical_name: 'South African Republic (Restored)',
  colony_id: 'south_african_republic_restored_1881_1900',
  colony_type: 'Boer Republic',
  comments: 'Independence restored after First Boer War, lost in Second Boer War',
  created_date: '2025-07-19T22:00:07',
  end_date: '1900-10-25',
  established_year: 1881,
  independence_year: 1900,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'South African Republic (Restored)',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1881-08-03',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.082000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q550374'
};

MERGE (c:HistoricalTerritory:BoerRepublic {colony_id: 'south_african_republic_transvaal_1852_1877'})
SET c += {
  administrative_status: 'Boer Republic',
  canonical_name: 'South African Republic (Transvaal)',
  colony_id: 'south_african_republic_transvaal_1852_1877',
  colony_type: 'Boer Republic',
  comments: 'Independent Boer republic north of Vaal River, first British annexation',
  created_date: '2025-07-19T22:00:07',
  end_date: '1877-04-12',
  established_year: 1852,
  independence_year: 1877,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'South African Republic (Transvaal)',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1852-01-17',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.130000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q550374'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'south_australia_1836_1901'})
SET c += {
  administrative_status: 'Planned Colony',
  canonical_name: 'South Australia',
  colony_id: 'south_australia_1836_1901',
  colony_type: 'Planned Colony',
  comments: 'Planned free settlement colony, gained self-government 1856',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:49:48',
  end_date: '1901-01-01',
  established_year: 1836,
  independence_year: 1901,
  latitude: -26.0,
  link_status: 'verified',
  longitude: 121.0,
  modern_nation_qids: ['Q408'],
  name: 'South Australia',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1836-02-19',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:11.454000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q35715'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'south_carolina_colony_1663_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'South Carolina Colony',
  colony_id: 'south_carolina_colony_1663_1783',
  colony_type: 'Royal Colony',
  comments: 'Originally part of Carolina, split 1712, Charleston',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1663,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'South Carolina Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1663-03-24',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:01.283000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2513167'
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'south_georgia_1775_ongoing'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'South Georgia',
  colony_id: 'south_georgia_1775_ongoing',
  colony_type: 'Dependency',
  comments: 'Sub-Antarctic whaling and sealing base, Cook\'s landing',
  created_date: '2025-07-20T12:11:28',
  established_year: 1775,
  link_status: 'verified',
  modern_nation_qids: ['Q35086'],
  name: 'South Georgia',
  region: 'Antarctica',
  source: 'Comprehensive Missing Territories',
  start_date: '1775-01-17',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:01.915000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q35086'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'south_georgia_whaling_stations_1904_1965'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'South Georgia Whaling Stations',
  colony_id: 'south_georgia_whaling_stations_1904_1965',
  colony_type: 'Whaling Station',
  comments: 'Multiple whaling stations including Grytviken, Leith Harbour, Stromness',
  created_date: '2025-07-20T11:26:12',
  established_year: 1904,
  link_status: 'verified',
  modern_nation_qids: ['Q35086'],
  name: 'South Georgia Whaling Stations',
  region: 'Antarctica',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1904-11-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:02.352000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q35086'
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'south_sandwich_islands_1775_ongoing'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'South Sandwich Islands',
  colony_id: 'south_sandwich_islands_1775_ongoing',
  colony_type: 'Dependency',
  comments: 'Remote volcanic islands, discovered by Cook',
  created_date: '2025-07-20T12:11:28',
  established_year: 1775,
  link_status: 'verified',
  modern_nation_qids: ['Q35086'],
  name: 'South Sandwich Islands',
  region: 'Antarctica',
  source: 'Comprehensive Missing Territories',
  start_date: '1775-01-31',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:02.551000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q35086'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'south_shetland_islands_whaling_1820_1959'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'South Shetland Islands Whaling',
  colony_id: 'south_shetland_islands_whaling_1820_1959',
  colony_type: 'Whaling Station',
  comments: 'Seasonal whaling stations, Antarctic Treaty suspension',
  created_date: '2025-07-20T11:26:12',
  end_date: '1959-12-01',
  established_year: 1820,
  independence_year: 1959,
  link_status: 'verified',
  modern_nation_qids: ['Q35086'],
  name: 'South Shetland Islands Whaling',
  region: 'Antarctica',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1820-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:02.875000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: [],
  whg_fclasses: ['T'],
  wikidata_id: 'Q35086'
};

MERGE (c:HistoricalTerritory:IndependentNation {colony_id: 'south_yemen_1967_1990'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'South Yemen',
  colony_id: 'south_yemen_1967_1990',
  colony_type: 'Independence',
  comments: 'People\'s Democratic Republic of Yemen, united with North Yemen 1990',
  created_date: '2025-07-19T22:11:19',
  end_date: '1990-05-22',
  established_year: 1967,
  independence_year: 1990,
  link_status: 'verified',
  modern_nation_qids: ['Q805'],
  name: 'South Yemen',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1967-11-30',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:55.433000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['YE'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q199841'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Southern Nigeria Protectorate',
  colony_id: 'southern_nigeria_protectorate_1900_1914',
  colony_type: 'Protectorate',
  comments: 'Created from Niger Coast Protectorate and Royal Niger Company territories',
  created_date: '2025-07-19T18:39:07.812806',
  end_date: '1914-01-01',
  established_year: 1900,
  independence_year: 1914,
  link_status: 'verified',
  modern_nation_qids: ['Q1033'],
  name: 'Southern Nigeria Protectorate',
  region: 'West Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1900-01-01',
  transition_type: 'merger',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:58.346000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['NG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2062030'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'southern_rhodesia_colony_1923_1953'})
SET c += {
  administrative_status: 'Self-governing Colony',
  canonical_name: 'Southern Rhodesia Colony',
  colony_id: 'southern_rhodesia_colony_1923_1953',
  colony_type: 'Self-governing Colony',
  comments: 'Self-governing colony after BSAC rule, before federation',
  created_date: '2025-07-19T22:06:51',
  end_date: '1953-08-01',
  established_year: 1923,
  independence_year: 1953,
  link_status: 'verified',
  modern_nation_qids: ['Q954', 'Q953'],
  name: 'Southern Rhodesia Colony',
  region: 'Southern Africa',
  source: 'East African Territorial Evolution',
  start_date: '1923-10-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:58.714000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZW', 'ZM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q750583'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'southern_rhodesia_post_federation_1963'})
SET c += {
  canonical_name: 'Southern Rhodesia',
  colony_id: 'southern_rhodesia_post_federation_1963',
  established_year: 1963,
  independence_year: 1965,
  region: 'Southern Africa',
  type: 'Self-governing Colony',
  wikidata_id: 'Q750583'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'southern_rhodesia_restored_1979_1980'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Southern Rhodesia (Restored)',
  colony_id: 'southern_rhodesia_restored_1979_1980',
  colony_type: 'Crown Colony',
  comments: 'Briefly restored to Crown Colony status during transition',
  created_date: '2025-07-19T22:06:51',
  end_date: '1980-04-18',
  established_year: 1979,
  independence_year: 1980,
  link_status: 'verified',
  modern_nation_qids: ['Q954', 'Q953'],
  name: 'Southern Rhodesia (Restored)',
  region: 'Southern Africa',
  source: 'East African Territorial Evolution',
  start_date: '1979-12-12',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:58.650000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZW', 'ZM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q750583'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'st._helena_1659_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'St. Helena',
  colony_id: 'st._helena_1659_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Strategic island, Napoleon\'s exile, still British Overseas Territory',
  created_date: '2025-07-19T23:25:07',
  established_year: 1659,
  link_status: 'verified',
  modern_nation_qids: ['Q192184'],
  name: 'St. Helena',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  start_date: '1659-05-05',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:58.847000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q34497'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'st_vincent_colony_1763_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'St. Vincent Colony',
  colony_id: 'st_vincent_colony_1763_1979',
  colony_type: 'Crown Colony',
  comments: 'Part of Windward Islands, Black Carib resistance',
  created_date: '2025-07-20T12:11:28',
  end_date: '1979-10-27',
  established_year: 1763,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q757'],
  name: 'St. Vincent Colony',
  region: 'Caribbean',
  source: 'Comprehensive Missing Territories',
  start_date: '1763-02-10',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:08.173000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['VC'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q15240384'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'starbuck_island_1866_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Starbuck Island',
  colony_id: 'starbuck_island_1866_1979',
  colony_type: 'Guano Island',
  comments: 'Line Islands guano mining, transferred to Kiribati',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1866,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q710'],
  name: 'Starbuck Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1866-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:11.684000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q911028'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'state_of_israel_1948'})
SET c += {
  canonical_name: 'State of Israel',
  colony_id: 'state_of_israel_1948',
  established_year: 1948,
  region: 'Middle East',
  type: 'Independence',
  wikidata_id: 'Q801'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'stkitts_nevis_anguilla_1816_1833'})
SET c += {
  canonical_name: 'Colony of St. Kitts-Nevis-Anguilla',
  colony_id: 'stkitts_nevis_anguilla_1816_1833',
  colony_type: 'Crown Colony',
  end_date: '1833-01-01',
  established_year: 1816,
  independence_year: 1833,
  modern_nation_qids: ['Q763'],
  name: 'Colony of St. Kitts-Nevis-Anguilla',
  region: 'Caribbean',
  source: 'Manual Correction',
  start_date: '1816-01-01',
  verified: true,
  verified_date: '2025-08-06T02:08:47.163000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KN'],
  whg_fclasses: ['A']
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'straits_settlements_1826_1946'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Straits Settlements',
  colony_id: 'straits_settlements_1826_1946',
  colony_type: 'Crown Colony',
  comments: 'Combined Penang, Singapore, Malacca; transferred from India Office to Colonial Office 1867',
  created_date: '2025-07-19T23:20:16',
  end_date: '1946-04-01',
  established_year: 1826,
  independence_year: 1946,
  link_status: 'verified',
  modern_nation_qids: ['Q833', 'Q334'],
  name: 'Straits Settlements',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1826-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:06.143000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY', 'SG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q376178'
};

MERGE (c:HistoricalTerritory:Condominium:Colony {colony_id: 'sudan_anglo-egyptian_1899_1956'})
SET c += {
  administrative_status: 'Condominium',
  canonical_name: 'Sudan, Anglo-Egyptian',
  colony_id: 'sudan_anglo-egyptian_1899_1956',
  colony_type: 'Condominium',
  comments: 'Joint administration with Egypt',
  created_date: '2025-07-19T18:39:07.896854',
  end_date: '1956-01-01',
  established_year: 1899,
  independence_year: 1956,
  link_status: 'verified',
  modern_nation_qids: ['Q1049'],
  name: 'Sudan, Anglo-Egyptian',
  region: 'Middle East',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1899-01-01',
  transition_type: 'independence',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:58.893000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q541455'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'swains_island_1856_1925'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Swains Island',
  colony_id: 'swains_island_1856_1925',
  colony_type: 'Guano Island',
  comments: 'Claimed under Guano Islands Act, transferred to American Samoa',
  created_date: '2025-07-20T11:26:12',
  end_date: '1925-02-16',
  established_year: 1856,
  independence_year: 1925,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'Swains Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1856-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:12.092000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['US'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q1128488'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'swan_river_colony_1829_1832'})
SET c += {
  administrative_status: 'Free Settlement Colony',
  canonical_name: 'Swan River Colony',
  colony_id: 'swan_river_colony_1829_1832',
  colony_type: 'Free Settlement Colony',
  comments: 'Free settlement colony, renamed to Western Australia',
  created_date: '2025-07-19T21:49:48',
  end_date: '1832-01-01',
  established_year: 1829,
  independence_year: 1832,
  link_status: 'verified',
  modern_nation_qids: ['Q408'],
  name: 'Swan River Colony',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  start_date: '1829-05-02',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.250000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1162123'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'swaziland_1903_1968'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Swaziland',
  colony_id: 'swaziland_1903_1968',
  colony_type: 'Protectorate',
  comments: 'Administered by Transvaal 1894-1906, then High Commissioner, became Eswatini',
  created_date: '2025-07-19T22:00:07',
  end_date: '1968-09-06',
  established_year: 1903,
  independence_year: 1968,
  link_status: 'verified',
  modern_nation_qids: ['Q1050'],
  name: 'Swaziland',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1903-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.021000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SZ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1050'
};

MERGE (c:HistoricalTerritory:IndependentNation {colony_id: 'tanganyika_1961_1964'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'Tanganyika',
  colony_id: 'tanganyika_1961_1964',
  colony_type: 'Independence',
  comments: 'Independent Tanganyika before union with Zanzibar',
  created_date: '2025-07-19T22:06:51',
  end_date: '1964-04-26',
  established_year: 1961,
  independence_year: 1964,
  link_status: 'verified',
  modern_nation_qids: ['Q924'],
  name: 'Tanganyika',
  region: 'East Africa',
  source: 'East African Territorial Evolution',
  start_date: '1961-12-09',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.196000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['TZ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q158725'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'tanganyika_territory_1922_1961'})
SET c += {
  administrative_status: 'Mandate/Trust Territory',
  canonical_name: 'Tanganyika Territory',
  colony_id: 'tanganyika_territory_1922_1961',
  colony_type: 'Mandate/Trust Territory',
  comments: 'Merged with Zanzibar in 1964 to form Tanzania',
  created_date: '2025-07-19T18:39:07.905608',
  end_date: '1961-01-01',
  established_year: 1922,
  independence_year: 1961,
  link_status: 'verified',
  modern_nation_qids: ['Q924'],
  name: 'Tanganyika Territory',
  region: 'East Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1922-01-01',
  transition_type: 'independence_merger',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.443000000+00:00',
  whg_aat_types: ['300387081'],
  whg_ccodes: ['TZ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q158725'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'tanzania_1964'})
SET c += {
  canonical_name: 'Tanzania',
  colony_id: 'tanzania_1964',
  established_year: 1964,
  region: 'East Africa',
  type: 'Independence',
  wikidata_id: 'Q924'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'tasmania_1856_1901'})
SET c += {
  administrative_status: 'Self-governing Colony',
  canonical_name: 'Tasmania',
  colony_id: 'tasmania_1856_1901',
  colony_type: 'Self-governing Colony',
  comments: 'Van Diemen\'s Land renamed to Tasmania, gained self-government',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:49:48',
  end_date: '1901-01-01',
  established_year: 1856,
  independence_year: 1901,
  latitude: -32.0,
  link_status: 'verified',
  longitude: 147.0,
  modern_nation_qids: ['Q408'],
  name: 'Tasmania',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1856-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:12.296000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5148519'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'territory_of_new_guinea_1920_1975'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Territory of New Guinea',
  colony_id: 'territory_of_new_guinea_1920_1975',
  colony_type: 'Mandate',
  comments: 'Former German New Guinea, administered by Australia for Britain',
  created_date: '2025-07-20T12:11:28',
  end_date: '1975-09-16',
  established_year: 1920,
  independence_year: 1975,
  link_status: 'verified',
  modern_nation_qids: ['Q691'],
  name: 'Territory of New Guinea',
  region: 'Pacific',
  source: 'Comprehensive Missing Territories',
  start_date: '1920-12-17',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.327000000+00:00',
  whg_aat_types: ['300387081'],
  whg_ccodes: ['PG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1443945'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'territory_of_papua_1906_1949'})
SET c += {
  administrative_status: 'Territory',
  canonical_name: 'Territory of Papua',
  colony_id: 'territory_of_papua_1906_1949',
  colony_type: 'Territory',
  comments: 'Transferred to Australian administration',
  created_date: '2025-07-19T22:13:10',
  end_date: '1949-12-01',
  established_year: 1906,
  independence_year: 1949,
  link_status: 'verified',
  modern_nation_qids: ['Q691'],
  name: 'Territory of Papua',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1906-09-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:12.604000000+00:00',
  whg_aat_types: ['300387081'],
  whg_ccodes: ['PG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q530560'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'territory_of_papua_and_new_guinea_1949_1975'})
SET c += {
  administrative_status: 'Trust Territory',
  canonical_name: 'Territory of Papua and New Guinea',
  colony_id: 'territory_of_papua_and_new_guinea_1949_1975',
  colony_type: 'Trust Territory',
  comments: 'Combined Papua and New Guinea territories before independence',
  created_date: '2025-07-20T12:11:28',
  end_date: '1975-09-16',
  established_year: 1949,
  independence_year: 1975,
  link_status: 'verified',
  modern_nation_qids: ['Q691'],
  name: 'Territory of Papua and New Guinea',
  region: 'Pacific',
  source: 'Comprehensive Missing Territories',
  start_date: '1949-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.418000000+00:00',
  whg_aat_types: ['300387081'],
  whg_ccodes: ['PG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2301972'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'tonga_protectorate_1900_1970'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Tonga Protectorate',
  colony_id: 'tonga_protectorate_1900_1970',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Kingdom of Tonga',
  created_date: '2025-07-19T22:13:10',
  end_date: '1970-06-04',
  established_year: 1900,
  independence_year: 1970,
  link_status: 'verified',
  modern_nation_qids: ['Q678'],
  name: 'Tonga Protectorate',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1900-05-18',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:12.688000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['TO'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q17197946'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'transjordan_1922_1946'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Transjordan',
  colony_id: 'transjordan_1922_1946',
  colony_type: 'Mandate',
  comments: 'Emirate of Transjordan under British mandate',
  created_date: '2025-07-19T22:11:19',
  end_date: '1946-05-25',
  established_year: 1922,
  independence_year: 1946,
  link_status: 'verified',
  modern_nation_qids: ['Q810'],
  name: 'Transjordan',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1922-09-16',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:55.561000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['JO'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1121819'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'transvaal_colony_first_british_1877_1881'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Transvaal Colony (First British)',
  colony_id: 'transvaal_colony_first_british_1877_1881',
  colony_type: 'Crown Colony',
  comments: 'First British annexation, lost independence after First Boer War',
  created_date: '2025-07-19T22:00:07',
  end_date: '1881-08-03',
  established_year: 1877,
  independence_year: 1881,
  link_status: 'verified',
  modern_nation_qids: ['Q258'],
  name: 'Transvaal Colony (First British)',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  start_date: '1877-04-12',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.179000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1187978'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'transvaal_colony_second_british_1900_1910'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Transvaal Colony (Second British)',
  colony_id: 'transvaal_colony_second_british_1900_1910',
  colony_type: 'Crown Colony',
  comments: 'South African Republic conquered and renamed, gained self-government 1906',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T22:00:07',
  end_date: '1910-05-31',
  established_year: 1900,
  independence_year: 1910,
  latitude: 41.138855555,
  link_status: 'verified',
  longitude: 16.760594444,
  modern_nation_qids: ['Q258'],
  name: 'Transvaal Colony (Second British)',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1900-10-25',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.321000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1187978'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'trinidad_and_tobago_1889_1962'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Colony of Trinidad and Tobago',
  colony_id: 'trinidad_and_tobago_1889_1962',
  colony_type: 'Crown Colony',
  comments: 'Formed by amalgamation of Trinidad and Tobago',
  created_date: '2025-07-19T18:39:08.268117',
  end_date: '1962-01-01',
  established_year: 1889,
  independence_year: 1962,
  link_status: 'verified',
  modern_nation_qids: ['Q754'],
  name: 'Trinidad and Tobago',
  region: 'Caribbean',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1889-01-01',
  transition_type: 'independence',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:08.281000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['TT'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q116282722'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'trinidad_and_tobago_colony_1797_1962'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Trinidad Colony',
  colony_id: 'trinidad_and_tobago_colony_1797_1962',
  colony_type: 'Crown Colony',
  comments: 'Trinidad captured from Spain 1797, Tobago added 1814',
  created_date: '2025-07-19T22:09:32',
  end_date: '1962-08-31',
  established_year: 1797,
  independence_year: 1889,
  link_status: 'verified',
  modern_nation_qids: ['Q754'],
  name: 'Trinidad and Tobago Colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  start_date: '1797-02-18',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:08.499000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['TT'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q116282722'
};

MERGE (c:HistoricalTerritory:Dependency:Colony {colony_id: 'tristan_da_cunha_1816_ongoing'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Tristan da Cunha',
  colony_id: 'tristan_da_cunha_1816_ongoing',
  colony_type: 'Dependency',
  comments: 'Dependency of St. Helena, most remote inhabited island',
  created_date: '2025-07-19T23:25:07',
  established_year: 1816,
  link_status: 'verified',
  modern_nation_qids: ['Q192184'],
  name: 'Tristan da Cunha',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  start_date: '1816-08-14',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.497000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q220982'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'trucial_states_1820_1971'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Trucial States',
  colony_id: 'trucial_states_1820_1971',
  colony_type: 'Protectorate',
  comments: 'Seven emirates under British protection in Persian Gulf',
  created_date: '2025-07-19T22:11:19',
  end_date: '1971-12-02',
  established_year: 1820,
  independence_year: 1971,
  link_status: 'verified',
  modern_nation_qids: ['Q878'],
  name: 'Trucial States',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  start_date: '1820-01-08',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:06.557000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AE'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1852345'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'turks_and_caicos_islands_1799_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Turks and Caicos Islands',
  colony_id: 'turks_and_caicos_islands_1799_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Separated from Bahamas, still British Overseas Territory',
  created_date: '2025-07-19T22:09:32',
  established_year: 1799,
  link_status: 'verified',
  modern_nation_qids: ['Q18221'],
  name: 'Turks and Caicos Islands',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  start_date: '1799-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:08.678000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q18221'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'uganda_1894_1962'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Uganda',
  colony_id: 'uganda_1894_1962',
  colony_type: 'Protectorate',
  comments: '',
  created_date: '2025-07-19T18:39:07.912639',
  end_date: '1962-01-01',
  established_year: 1894,
  independence_year: 1962,
  link_status: 'verified',
  modern_nation_qids: ['Q1036'],
  name: 'Uganda',
  region: 'East Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1894-01-01',
  transition_type: 'independence',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.545000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['UG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1097943'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'unfederated_malay_states_1909_1946'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Unfederated Malay States',
  colony_id: 'unfederated_malay_states_1909_1946',
  colony_type: 'Protectorate',
  comments: 'Johor, Kedah, Kelantan, Terengganu, Perlis under British protection',
  created_date: '2025-07-19T23:20:16',
  end_date: '1946-04-01',
  established_year: 1909,
  independence_year: 1946,
  link_status: 'verified',
  modern_nation_qids: ['Q833'],
  name: 'Unfederated Malay States',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  start_date: '1909-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:06.956000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1973084'
};

MERGE (c:HistoricalTerritory:Dominion:Colony {colony_id: 'union_of_south_africa_1910_1961'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Union of South Africa',
  colony_id: 'union_of_south_africa_1910_1961',
  colony_type: 'Dominion',
  comments: 'Self-governing dominion formed from four colonies, became Republic 1961',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T22:00:07',
  end_date: '1961-05-31',
  established_year: 1910,
  independence_year: 1961,
  latitude: -29.0,
  link_status: 'verified',
  longitude: 24.0,
  modern_nation_qids: ['Q258'],
  name: 'Union of South Africa',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1910-05-31',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.661000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q193619'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'united_colony_of_bc_1866_1871'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'United Colony of British Columbia',
  colony_id: 'united_colony_of_bc_1866_1871',
  comments: 'Formed by the union of the mainland Colony of British Columbia and the Colony of Vancouver Island.',
  end_date: '1871-07-20',
  established_year: 1866,
  independence_year: 1871,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'United Colony of British Columbia',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Manual Correction',
  start_date: '1866-08-06',
  verified: true,
  verified_date: '2025-08-06T00:00:25.599000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2514958'
};

MERGE (c:HistoricalTerritory:Province:Colony {colony_id: 'united_provinces_1877_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'United Provinces',
  colony_id: 'united_provinces_1877_1947',
  colony_type: 'Province',
  comments: 'Formed from North-Western Provinces and Oudh, became Uttar Pradesh in India',
  created_date: '2025-07-19T21:53:26',
  end_date: '1947-08-15',
  established_year: 1877,
  independence_year: 1947,
  link_status: 'verified',
  modern_nation_qids: ['Q668'],
  name: 'United Provinces',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  start_date: '1877-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:55.697000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2160037'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'united_states_1776'})
SET c += {
  canonical_name: 'United States of America',
  colony_id: 'united_states_1776',
  established_year: 1776,
  region: 'North America',
  type: 'Independence',
  wikidata_id: 'Q30'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'united_states_of_america_1783'})
SET c += {
  canonical_name: 'United States of America',
  colony_id: 'united_states_of_america_1783',
  colony_type: 'Former Colony (Independent)',
  established_year: 1783,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q30'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'upper_canada_1791_1841'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Upper Canada',
  colony_id: 'upper_canada_1791_1841',
  colony_type: 'Crown Colony',
  comments: 'Created by Constitutional Act 1791, merged into Province of Canada',
  created_date: '2025-07-19T21:45:18',
  end_date: '1841-01-01',
  established_year: 1791,
  independence_year: 1841,
  link_status: 'verified',
  modern_nation_qids: ['Q16'],
  name: 'Upper Canada',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Canadian Territorial Evolution',
  start_date: '1791-01-01',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q795427'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'van_diemens_land_1803_1856'})
SET c += {
  administrative_status: 'Penal Colony',
  canonical_name: 'Van Diemen\'s Land',
  colony_id: 'van_diemens_land_1803_1856',
  colony_type: 'Penal Colony',
  comments: 'Separate colony from 1825, renamed to Tasmania 1856',
  created_date: '2025-07-19T21:49:48',
  end_date: '1856-01-01',
  established_year: 1803,
  independence_year: 1856,
  link_status: 'verified',
  modern_nation_qids: ['Q408'],
  name: 'Van Diemen\'s Land',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  start_date: '1803-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:12.799000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1780114'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'vancouver_island_1849_1866'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Colony of Vancouver Island',
  colony_id: 'vancouver_island_1849_1866',
  colony_type: 'Crown Colony',
  comments: 'Merged with mainland British Columbia colony',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:45:18',
  end_date: '1866-08-06',
  established_year: 1849,
  independence_year: 1866,
  latitude: 51.483333333,
  link_status: 'verified',
  longitude: 7.216666666,
  modern_nation_qids: ['Q16'],
  name: 'Colony of Vancouver Island',
  qid_type: 'historical_colony',
  region: 'North America',
  source: 'Canadian Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1849-01-01',
  verified: true,
  verified_date: '2025-08-06T00:00:25.599000000+00:00',
  whg_aat_types: ['300387506'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2510000'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'victoria_colony_1851_1901'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Victoria (Colony)',
  colony_id: 'victoria_colony_1851_1901',
  colony_type: 'Crown Colony',
  comments: 'Separated from New South Wales due to gold rush, gained self-government 1855',
  created_date: '2025-07-19T21:49:48',
  end_date: '1901-01-01',
  established_year: 1851,
  independence_year: 1901,
  link_status: 'verified',
  modern_nation_qids: ['Q408'],
  name: 'Victoria (Colony)',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  start_date: '1851-07-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:13.116000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q56850459'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'virginia_colony_1607_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'Virginia Colony',
  colony_id: 'virginia_colony_1607_1783',
  colony_type: 'Royal Colony',
  comments: 'First permanent English settlement in North America, Jamestown',
  created_date: '2025-07-20T12:11:27',
  end_date: '1783-09-03',
  established_year: 1607,
  independence_year: 1783,
  link_status: 'verified',
  modern_nation_qids: ['Q30'],
  name: 'Virginia Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  start_date: '1607-05-14',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:01.554000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1070529'
};

MERGE (c:HistoricalTerritory:MinorTerritory:Colony {colony_id: 'vostok_island_1866_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Vostok Island',
  colony_id: 'vostok_island_1866_1979',
  colony_type: 'Guano Island',
  comments: 'Line Islands guano mining, transferred to Kiribati',
  created_date: '2025-07-20T11:26:12',
  end_date: '1979-07-12',
  established_year: 1866,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q710'],
  name: 'Vostok Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  start_date: '1866-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:13.224000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q976570'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'weihaiwei_1898_1930'})
SET c += {
  administrative_status: 'Leased Territory',
  canonical_name: 'Weihaiwei',
  colony_id: 'weihaiwei_1898_1930',
  colony_type: 'Leased Territory',
  comments: 'Chinese territory leased to Britain as naval base in Shandong',
  created_date: '2025-07-19T23:21:55',
  end_date: '1930-10-01',
  established_year: 1898,
  independence_year: 1930,
  link_status: 'verified',
  modern_nation_qids: ['Q148'],
  name: 'Weihaiwei',
  region: 'Southeast Asia',
  source: 'Additional Southeast Asian Territories',
  start_date: '1898-07-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:07.383000000+00:00',
  whg_aat_types: ['300387081'],
  whg_ccodes: ['CN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q15939896'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'west_florida_1763_1783'})
SET c += {
  colony_id: 'west_florida_1763_1783',
  established_year: 1763,
  independence_year: 1783,
  name: 'West Florida',
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q4971241'
};

MERGE (c:HistoricalTerritory:Federation:Colony {colony_id: 'west_indies_federation_1958_1962'})
SET c += {
  administrative_status: 'Federation',
  canonical_name: 'West Indies Federation',
  colony_id: 'west_indies_federation_1958_1962',
  colony_type: 'Federation',
  comments: 'Included 10 territories, dissolved when Jamaica and Trinidad left',
  created_date: '2025-07-19T18:39:08.291016',
  end_date: '1962-01-01',
  established_year: 1958,
  independence_year: 1962,
  link_status: 'verified',
  modern_nation_qids: ['Q766', 'Q754', 'Q244', 'Q769', 'Q760', 'Q757', 'Q784', 'Q781', 'Q763'],
  name: 'West Indies Federation',
  region: 'Caribbean',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1958-01-01',
  transition_type: 'dissolution',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:08.753000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['JM', 'TT', 'BB', 'GD', 'LC', 'VC', 'DM', 'AG', 'KN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q652560'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'western_australia_1832_1901'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Western Australia',
  colony_id: 'western_australia_1832_1901',
  colony_type: 'Crown Colony',
  comments: 'Swan River Colony renamed, gained self-government 1890',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T21:49:48',
  end_date: '1901-01-01',
  established_year: 1832,
  independence_year: 1901,
  latitude: -26.0,
  link_status: 'verified',
  longitude: 121.0,
  modern_nation_qids: ['Q408'],
  name: 'Western Australia',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1832-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.461000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3206'
};

MERGE (c:HistoricalTerritory:Mandate:Colony {colony_id: 'western_samoa_1920_1962'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Western Samoa',
  colony_id: 'western_samoa_1920_1962',
  colony_type: 'Mandate',
  comments: 'Former German Samoa under New Zealand administration',
  created_date: '2025-07-19T22:13:10',
  end_date: '1962-01-01',
  established_year: 1920,
  independence_year: 1962,
  link_status: 'verified',
  modern_nation_qids: ['Q683'],
  name: 'Western Samoa',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  start_date: '1920-05-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.506000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['WS'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q7988268'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'yukon_territory_1898'})
SET c += {
  canonical_name: 'Yukon Territory',
  colony_id: 'yukon_territory_1898',
  colony_type: 'Territory',
  established_year: 1898,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q2009'
};

MERGE (c:HistoricalTerritory:Protectorate:Colony {colony_id: 'zanzibar_1890_1963'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Zanzibar',
  colony_id: 'zanzibar_1890_1963',
  colony_type: 'Protectorate',
  comments: 'Merged with Tanganyika in 1964 to form Tanzania',
  created_date: '2025-07-19T18:39:07.938095',
  end_date: '1963-01-01',
  established_year: 1890,
  independence_year: 1963,
  link_status: 'verified',
  modern_nation_qids: ['Q924'],
  name: 'Zanzibar',
  region: 'East Africa',
  source: 'Wikipedia Territorial Evolution',
  start_date: '1890-01-01',
  transition_type: 'independence_merger',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.804000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['TZ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3574782'
};

MERGE (c:HistoricalTerritory:IndependentNation {colony_id: 'zanzibar_independent_1963_1964'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'Zanzibar (Independent)',
  colony_id: 'zanzibar_independent_1963_1964',
  colony_type: 'Independence',
  comments: 'Independent Zanzibar before union with Tanganyika',
  created_date: '2025-07-19T22:06:51',
  end_date: '1964-04-26',
  established_year: 1963,
  independence_year: 1964,
  link_status: 'verified',
  modern_nation_qids: ['Q924'],
  name: 'Zanzibar (Independent)',
  region: 'East Africa',
  source: 'East African Territorial Evolution',
  start_date: '1963-12-10',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.849000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['TZ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q48769061'
};

MERGE (c:HistoricalTerritory:Colony {colony_id: 'zimbabwe_rhodesia_1979_1979'})
SET c += {
  administrative_status: 'Transitional',
  canonical_name: 'Zimbabwe Rhodesia',
  colony_id: 'zimbabwe_rhodesia_1979_1979',
  colony_type: 'Transitional',
  comments: 'Brief internal settlement before Lancaster House Agreement',
  created_date: '2025-07-19T22:06:51',
  end_date: '1979-12-12',
  established_year: 1979,
  independence_year: 1979,
  link_status: 'verified',
  modern_nation_qids: ['Q954', 'Q953'],
  name: 'Zimbabwe Rhodesia',
  region: 'Southern Africa',
  source: 'East African Territorial Evolution',
  start_date: '1979-06-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.893000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZW', 'ZM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q890120'
};

MERGE (c:HistoricalTerritory:CrownColony:Colony {colony_id: 'zululand_1887_1897'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Zululand',
  colony_id: 'zululand_1887_1897',
  colony_type: 'Crown Colony',
  comments: 'Incorporated into Colony of Natal 1897',
  coordinates_source: 'wikidata',
  created_date: '2025-07-19T22:00:07',
  end_date: '1897-12-30',
  established_year: 1887,
  independence_year: 1897,
  latitude: -23.83694444,
  link_status: 'verified',
  longitude: 31.63777778,
  modern_nation_qids: ['Q258'],
  name: 'Zululand',
  region: 'Southern Africa',
  source: 'South African Territorial Evolution',
  spatial_updated: '2025-07-21T00:41:48',
  start_date: '1887-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.435000000+00:00',
  whg_aat_types: ['300387081'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q729768'
};



// ── Relationships ──
// Relationship types: EVOLVED_INTO, BECAME_INDEPENDENT, BECAME_CROWN_COLONY,
//   BECAME_COLONY, BECAME_PROTECTORATE, BECAME_MANDATE, BECAME_SEPARATE_COLONY,
//   BECAME_SELF_GOVERNING, MERGED_INTO, INCORPORATED_INTO, REORGANIZED_AS,
//   FEDERATED_INTO, PARTITIONED_INTO, TRANSFERRED_SOVEREIGNTY, REUNITED_INTO,
//   SUCCEEDED, PART_OF, WAS_MEMBER_OF, ADMINISTERED_UNDER,
//   BORDERS_WITH, NEAR_COAST_OF, TRANSFERRED_TERRITORY


MATCH (a:HistoricalTerritory {colony_id: 'acadia_french_1604_1713'}), (b:HistoricalTerritory {colony_id: 'nova_scotia_pre_1713_1784'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'aden_1839_1963'}), (b:HistoricalTerritory {colony_id: 'aden_colony_1937_1967'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'aden_colony_1937_1967'}), (b:HistoricalTerritory {colony_id: 'south_yemen_1967_1990'}) MERGE (a)-[:BECAME_INDEPENDENT {description: 'Aden became part of independent South Yemen', year: 1967, detail: 'BECAME_INDEPENDENT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'aden_protectorate_1839_1967'}), (b:HistoricalTerritory {colony_id: 'south_yemen_1967_1990'}) MERGE (a)-[:BECAME_INDEPENDENT {description: 'Aden Protectorate became part of independent South Yemen', year: 1967, detail: 'BECAME_INDEPENDENT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ajmer_merwara_1818_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'alberta_1905'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'andaman_and_nicobar_islands_1789_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'anguilla_1650_ongoing'}), (b:HistoricalTerritory {colony_id: 'stkitts_nevis_anguilla_1816_1833'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1833, start_year: 1816}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'antigua_colony_1632_1981'}), (b:HistoricalTerritory {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'antigua_montserrat_barbuda_1816_1833'}), (b:HistoricalTerritory {colony_id: 'federal_colony_leeward_islands_1833-1960'}) MERGE (a)-[:MERGED_INTO {year: 1833, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ascension_island_1815_ongoing'}), (b:HistoricalTerritory {colony_id: 'south_african_republic_restored_1881_1900'}) MERGE (a)-[:NEAR_COAST_OF {created_date: '2025-07-21T10:19:50', source: 'comprehensive_coastal'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'assam_bengal_presidency_1826_1874'}), (b:HistoricalTerritory {colony_id: 'assam_province_1874_1905'}) MERGE (a)-[:REORGANIZED_AS {description: 'Assam was separated from the Bengal Presidency to become a Chief Commissioner\'s Province.', year: 1874, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'assam_province_1874_1905'}), (b:HistoricalTerritory {colony_id: 'eastern_bengal_and_assam_1905_1912'}) MERGE (a)-[:MERGED_INTO {description: 'Assam merged with Eastern Bengal during partition', year: 1905, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'assam_province_1874_1905'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'assam_province_1874_1905'}), (b:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:SUCCEEDED {description: 'Assam separated from Bengal Presidency as chief commissionership', succession_type: 'COMPLEX_SUCCESSION', year: 1874, detail: 'CARVED_OUT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'assam_province_1874_1905'}), (b:HistoricalTerritory {colony_id: 'eastern_bengal_and_assam_1905_1912'}) MERGE (a)-[:SUCCEEDED {description: 'Assam separated again as chief commissionership', succession_type: 'COMPLEX_SUCCESSION', year: 1912, detail: 'SEPARATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'assam_province_restored_1912_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:PARTITIONED_INTO {description: 'Most of Assam joined the Dominion of India.', year: 1947, detail: 'PARTITIONED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'assam_province_restored_1912_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baluchistan_1877_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baluchistan_1877_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'barbados_colony_1627_1966'}), (b:HistoricalTerritory {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF {description: 'Barbados served as the administrative headquarters of the British Windward Islands during this period.', end_year: 1885, start_year: 1833}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_presidency_company_1757_1858'}), (b:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'Crown took over after Indian Rebellion 1857', year: 1858, detail: 'TRANSFERRED_TO_CROWN'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_presidency_company_1757_1858'}), (b:HistoricalTerritory {colony_id: 'assam_bengal_presidency_1826_1874'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:HistoricalTerritory {colony_id: 'assam_province_1874_1905'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:HistoricalTerritory {colony_id: 'bengal_province_partitioned_1905_1912'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:HistoricalTerritory {colony_id: 'bihar_and_orissa_1912_1947'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:HistoricalTerritory {colony_id: 'eastern_bengal_and_assam_1905_1912'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:HistoricalTerritory {colony_id: 'bengal_presidency_company_1757_1858'}) MERGE (a)-[:SUCCEEDED {description: 'Crown took over after Indian Rebellion 1857', succession_type: 'DIRECT_SUCCESSION', year: 1858, detail: 'TRANSFERRED_TO_CROWN'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_province_partitioned_1905_1912'}), (b:HistoricalTerritory {colony_id: 'bengal_province_reunited_1912_1947'}) MERGE (a)-[:REUNITED_INTO {description: 'Bengal reunited due to Swadeshi movement protests', year: 1912, detail: 'REUNITED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_province_partitioned_1905_1912'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_province_partitioned_1905_1912'}), (b:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:SUCCEEDED {description: 'Bengal partitioned by Curzon - western part', succession_type: 'COMPLEX_SUCCESSION', year: 1905, detail: 'PARTITIONED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_province_reunited_1912_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_province_reunited_1912_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bengal_province_reunited_1912_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'berbice_colony_1803_1831'}), (b:HistoricalTerritory {colony_id: 'british_guiana_1831_1966'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bihar_and_orissa_1912_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:FEDERATED_INTO {description: 'Bihar and Orissa joined India', year: 1947, detail: 'JOINED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bihar_and_orissa_1912_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bihar_and_orissa_1912_1947'}), (b:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:SUCCEEDED {description: 'Bihar and Orissa separated from Bengal during reorganization', succession_type: 'COMPLEX_SUCCESSION', year: 1912, detail: 'CARVED_OUT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bombay_presidency_company_1687_1858'}), (b:HistoricalTerritory {colony_id: 'bombay_presidency_crown_1858_1947'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'Crown took over after Indian Rebellion 1857', year: 1858, detail: 'TRANSFERRED_TO_CROWN'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bombay_presidency_crown_1858_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:FEDERATED_INTO {description: 'Bombay Presidency joined India', year: 1947, detail: 'JOINED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bombay_presidency_crown_1858_1947'}), (b:HistoricalTerritory {colony_id: 'sind_province_1843_1947'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bombay_presidency_crown_1858_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bombay_presidency_crown_1858_1947'}), (b:HistoricalTerritory {colony_id: 'bombay_presidency_company_1687_1858'}) MERGE (a)-[:SUCCEEDED {description: 'Crown took over after Indian Rebellion 1857', succession_type: 'DIRECT_SUCCESSION', year: 1858, detail: 'TRANSFERRED_TO_CROWN'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_bechuanaland_1885_1895'}), (b:HistoricalTerritory {colony_id: 'cape_colony_british_1806_1910'}) MERGE (a)-[:INCORPORATED_INTO {description: 'British Bechuanaland incorporated into Cape Colony', year: 1895, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_central_africa_protectorate_1891_1907'}), (b:HistoricalTerritory {colony_id: 'nyasaland_1891_1964'}) MERGE (a)-[:REORGANIZED_AS {description: 'British Central Africa Protectorate renamed to Nyasaland', year: 1907, detail: 'RENAMED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_columbia_province_1871'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_gold_coast_1821_1874'}), (b:HistoricalTerritory {colony_id: 'gold_coast_colony_1874_1957'}) MERGE (a)-[:REORGANIZED_AS {description: 'The British Gold Coast was formally established as the Gold Coast Crown Colony, with an administration separate from Sierra Leone.', year: 1874, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_gold_coast_1821_1874'}), (b:HistoricalTerritory {colony_id: 'cape_coast_castle_1664_1821'}) MERGE (a)-[:SUCCEEDED {description: 'Trading posts taken over by Crown administration', succession_type: 'DIRECT_SUCCESSION', year: 1821, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_guiana_1831_1966'}), (b:HistoricalTerritory {colony_id: 'trinidad_and_tobago_1889_1962'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T00:41:49', source: 'historical_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_honduras_1862_1981'}), (b:HistoricalTerritory {colony_id: 'jamaica_1655_1962'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T00:41:49', source: 'historical_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_new_guinea_1884_1906'}), (b:HistoricalTerritory {colony_id: 'territory_of_papua_1906_1949'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'British New Guinea transferred to Australian administration', year: 1906, detail: 'TRANSFERRED_TO_AUSTRALIA'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_north_borneo_1882_1946'}), (b:HistoricalTerritory {colony_id: 'north_borneo_crown_colony_1946_1963'}) MERGE (a)-[:BECAME_CROWN_COLONY {description: 'Company territory became Crown Colony', year: 1946, detail: 'BECAME_CROWN_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_somaliland_1884_1960'}), (b:HistoricalTerritory {colony_id: 'somali_republic_1960'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_south_africa_company_territory_1889_1923'}), (b:HistoricalTerritory {colony_id: 'northern_rhodesia_colony_1924_1953'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_south_africa_company_territory_1889_1923'}), (b:HistoricalTerritory {colony_id: 'southern_rhodesia_colony_1923_1953'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'british_virgin_islands_1672_ongoing'}), (b:HistoricalTerritory {colony_id: 'stkitts_nevis_anguilla_1816_1833'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1833, start_year: 1816}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'burma_british_india_1886_1937'}), (b:HistoricalTerritory {colony_id: 'burma_separate_colony_1937_1948'}) MERGE (a)-[:PARTITIONED_INTO {description: 'Burma separated from British India as separate crown colony', year: 1937, detail: 'SEPARATED_FROM_INDIA'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'burma_british_india_1886_1937'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}), (b:HistoricalTerritory {colony_id: 'canada_independent_1931'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}), (b:HistoricalTerritory {colony_id: 'new_brunswick_1784_1867'}) MERGE (a)-[:SUCCEEDED {description: 'New Brunswick joined Confederation as founding province', succession_type: 'COMPLEX_SUCCESSION', year: 1867, detail: 'CONFEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}), (b:HistoricalTerritory {colony_id: 'province_of_canada_1841_1867'}) MERGE (a)-[:SUCCEEDED {description: 'Province of Canada split into Ontario and Quebec, joined Confederation as Dominion of Canada', succession_type: 'COMPLEX_SUCCESSION', year: 1867, detail: 'CONFEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cape_breton_colony_1784_1820'}), (b:HistoricalTerritory {colony_id: 'nova_scotia_post_1784_1867'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cape_coast_castle_1664_1821'}), (b:HistoricalTerritory {colony_id: 'british_gold_coast_1821_1874'}) MERGE (a)-[:REORGANIZED_AS {description: 'Trading posts taken over by Crown administration', year: 1821, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cape_colony_british_1795_1803_1795_1803'}), (b:HistoricalTerritory {colony_id: 'cape_colony_dutch_restored_1803_1806'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'Cape returned to Dutch under Treaty of Amiens', year: 1803, detail: 'RETURNED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cape_colony_british_1806_1910'}), (b:HistoricalTerritory {colony_id: 'union_of_south_africa_1910_1961'}) MERGE (a)-[:FEDERATED_INTO {description: 'Cape Colony joined Union of South Africa as Cape Province', year: 1910, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cape_colony_british_1806_1910'}), (b:HistoricalTerritory {colony_id: 'british_bechuanaland_1885_1895'}) MERGE (a)-[:SUCCEEDED {description: 'British Bechuanaland incorporated into Cape Colony', succession_type: 'COMPLEX_SUCCESSION', year: 1895, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cape_colony_british_1806_1910'}), (b:HistoricalTerritory {colony_id: 'griqualand_west_1871_1880'}) MERGE (a)-[:SUCCEEDED {description: 'Griqualand West incorporated into Cape Colony', succession_type: 'COMPLEX_SUCCESSION', year: 1880, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cape_colony_dutch_1652_1795'}), (b:HistoricalTerritory {colony_id: 'cape_colony_british_1795_1803_1795_1803'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'British conquered Cape Colony during French Revolutionary Wars', year: 1795, detail: 'CONQUERED_BY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cape_colony_dutch_restored_1803_1806'}), (b:HistoricalTerritory {colony_id: 'cape_colony_british_1806_1910'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'British permanently conquered Cape Colony, confirmed 1815 Congress of Vienna', year: 1806, detail: 'CONQUERED_BY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'central_provinces_1861_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:FEDERATED_INTO {description: 'Central Provinces joined India', year: 1947, detail: 'JOINED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'central_provinces_1861_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}), (b:HistoricalTerritory {colony_id: 'northern_nigeria_1900_1914'}) MERGE (a)-[:SUCCEEDED {description: 'Northern and Southern Nigeria amalgamated by Lord Lugard', succession_type: 'COMPLEX_SUCCESSION', year: 1914, detail: 'AMALGAMATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}), (b:HistoricalTerritory {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:SUCCEEDED {description: 'Northern and Southern Nigeria amalgamated by Lord Lugard', succession_type: 'COMPLEX_SUCCESSION', year: 1914, detail: 'AMALGAMATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}), (b:HistoricalTerritory {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:SUCCEEDED {description: 'Southern and Northern Nigeria merged to form Nigeria', succession_type: 'COMPLEX_SUCCESSION', year: '1914', detail: 'MERGED_WITH'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'colony_of_natal_1843_1910'}), (b:HistoricalTerritory {colony_id: 'union_of_south_africa_1910_1961'}) MERGE (a)-[:FEDERATED_INTO {description: 'Natal joined Union of South Africa as Natal Province', year: 1910, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'colony_of_natal_1843_1910'}), (b:HistoricalTerritory {colony_id: 'zululand_1887_1897'}) MERGE (a)-[:SUCCEEDED {description: 'Zululand incorporated into Colony of Natal', succession_type: 'COMPLEX_SUCCESSION', year: 1897, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'colony_of_newfoundland_1610_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_newfoundland_1907_1934'}) MERGE (a)-[:EVOLVED_INTO {year: 1907}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}), (b:HistoricalTerritory {colony_id: 'australia_independent_1942'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}), (b:HistoricalTerritory {colony_id: 'new_south_wales_original_1788_1901'}) MERGE (a)-[:SUCCEEDED {description: 'New South Wales joined Australian federation', succession_type: 'FEDERATION_SUCCESSION', year: 1901, detail: 'FEDERATION_SUCCESSION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}), (b:HistoricalTerritory {colony_id: 'queensland_1859_1901'}) MERGE (a)-[:SUCCEEDED {description: 'Queensland joined Australian federation', succession_type: 'FEDERATION_SUCCESSION', year: 1901, detail: 'FEDERATION_SUCCESSION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}), (b:HistoricalTerritory {colony_id: 'victoria_colony_1851_1901'}) MERGE (a)-[:SUCCEEDED {description: 'Victoria joined Australian federation', succession_type: 'FEDERATION_SUCCESSION', year: 1901, detail: 'FEDERATION_SUCCESSION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'connecticut_colony_1636_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'connecticut_colony_1636_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'coorg_province_1834_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'delaware_colony_1664_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'delaware_colony_1664_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'demerara_colony_1803_1831'}), (b:HistoricalTerritory {colony_id: 'british_guiana_1831_1966'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dominica_colony_1763_1978'}), (b:HistoricalTerritory {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dominica_colony_1763_1978'}), (b:HistoricalTerritory {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1959, start_year: 1940}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}), (b:HistoricalTerritory {colony_id: 'bengal_province_reunited_1912_1947'}) MERGE (a)-[:SUCCEEDED {description: 'West Bengal to India', succession_type: 'COMPLEX_SUCCESSION', year: 1947, detail: 'PARTITIONED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}), (b:HistoricalTerritory {colony_id: 'punjab_province_1849_1947'}) MERGE (a)-[:SUCCEEDED {description: 'Eastern Punjab to India', succession_type: 'COMPLEX_SUCCESSION', year: 1947, detail: 'PARTITIONED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dominion_of_new_zealand_1907_1947'}), (b:HistoricalTerritory {colony_id: 'new_zealand_independent_1947'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dominion_of_newfoundland_1907_1934'}), (b:HistoricalTerritory {colony_id: 'newfoundland_commission_1934_1949'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dominion_of_newfoundland_1907_1934'}), (b:HistoricalTerritory {colony_id: 'newfoundland_province_1949'}) MERGE (a)-[:EVOLVED_INTO {year: 1949}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}), (b:HistoricalTerritory {colony_id: 'bengal_province_reunited_1912_1947'}) MERGE (a)-[:SUCCEEDED {description: 'East Bengal to Pakistan', succession_type: 'COMPLEX_SUCCESSION', year: 1947, detail: 'PARTITIONED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}), (b:HistoricalTerritory {colony_id: 'punjab_province_1849_1947'}) MERGE (a)-[:SUCCEEDED {description: 'Western Punjab to Pakistan', succession_type: 'COMPLEX_SUCCESSION', year: 1947, detail: 'PARTITIONED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'east_africa_protectorate_1895_1920'}), (b:HistoricalTerritory {colony_id: 'kenya_colony_and_protectorate_of_1920_1963'}) MERGE (a)-[:BECAME_COLONY {description: 'East Africa Protectorate became Kenya Colony and Protectorate', year: 1920, detail: 'BECAME_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'east_africa_protectorate_1895_1920'}), (b:HistoricalTerritory {colony_id: 'imperial_british_east_africa_company_territory_1888_1895'}) MERGE (a)-[:SUCCEEDED {description: 'IBEA Company territory became Crown protectorate due to financial difficulties', succession_type: 'DIRECT_SUCCESSION', year: 1895, detail: 'BECAME_PROTECTORATE'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:HistoricalTerritory {colony_id: 'assam_province_1874_1905'}) MERGE (a)-[:PARTITIONED_INTO {description: 'Assam separated again as chief commissionership', year: 1912, detail: 'SEPARATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:HistoricalTerritory {colony_id: 'assam_province_restored_1912_1947'}) MERGE (a)-[:PARTITIONED_INTO {year: 1912, detail: 'SEPARATED_FROM'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:HistoricalTerritory {colony_id: 'bengal_province_reunited_1912_1947'}) MERGE (a)-[:REUNITED_INTO {description: 'Eastern Bengal reunited with western Bengal', year: 1912, detail: 'REUNITED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:HistoricalTerritory {colony_id: 'assam_province_1874_1905'}) MERGE (a)-[:SUCCEEDED {description: 'Assam merged with Eastern Bengal during partition', succession_type: 'COMPLEX_SUCCESSION', year: 1905, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:HistoricalTerritory {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:SUCCEEDED {description: 'Bengal partitioned by Curzon - eastern part with Assam', succession_type: 'COMPLEX_SUCCESSION', year: 1905, detail: 'PARTITIONED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ellice_islands_1976_1978'}), (b:HistoricalTerritory {colony_id: 'gilbert_and_ellice_islands_1916_1976'}) MERGE (a)-[:SUCCEEDED {description: 'Ellice Islands separated from Gilbert Islands', succession_type: 'COMPLEX_SUCCESSION', year: 1976, detail: 'SEPARATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'essequibo_colony_1803_1831'}), (b:HistoricalTerritory {colony_id: 'british_guiana_1831_1966'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'factory_at_surat_1612_1857'}), (b:HistoricalTerritory {colony_id: 'bombay_presidency_company_1687_1858'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'federated_malay_states_1895_1946'}), (b:HistoricalTerritory {colony_id: 'malayan_union_1946_1948'}) MERGE (a)-[:INCORPORATED_INTO {description: 'FMS incorporated into Malayan Union', year: 1946, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'federation_of_malaya_1948_1957'}), (b:HistoricalTerritory {colony_id: 'malaya_independent_1957_1963'}) MERGE (a)-[:BECAME_INDEPENDENT {description: 'Federation of Malaya gained independence', year: 1957, detail: 'BECAME_INDEPENDENT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'federation_of_malaya_1948_1957'}), (b:HistoricalTerritory {colony_id: 'malayan_union_1946_1948'}) MERGE (a)-[:SUCCEEDED {description: 'Malayan Union reorganized as Federation due to opposition', succession_type: 'DIRECT_SUCCESSION', year: 1948, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}), (b:HistoricalTerritory {colony_id: 'northern_rhodesia_post_federation_1964'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}), (b:HistoricalTerritory {colony_id: 'nyasaland_post_federation_1963'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}), (b:HistoricalTerritory {colony_id: 'southern_rhodesia_post_federation_1963'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'fort_william_calcutta_1696_1857'}), (b:HistoricalTerritory {colony_id: 'bengal_presidency_company_1757_1858'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gambia_colony_1816_1888'}), (b:HistoricalTerritory {colony_id: 'gambia_colony_and_protectorate_1816_1965'}) MERGE (a)-[:REORGANIZED_AS {description: 'The original colony was expanded with the addition of a protectorate over the Gambian hinterland.', year: 1888, detail: 'EXPANDED_WITH_PROTECTORATE'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gambia_colony_1816_1888'}), (b:HistoricalTerritory {colony_id: 'james_island_trading_post_1661_1816'}) MERGE (a)-[:SUCCEEDED {description: 'Trading post reorganized as Crown Colony', succession_type: 'DIRECT_SUCCESSION', year: 1816, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'georgia_colony_1732_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'georgia_colony_1732_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'german_east_africa_british_occupied_1916_1922'}), (b:HistoricalTerritory {colony_id: 'tanganyika_territory_1922_1961'}) MERGE (a)-[:BECAME_MANDATE {description: 'German East Africa became League of Nations mandate territory', year: 1922, detail: 'BECAME_MANDATE'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gilbert_and_ellice_islands_1916_1976'}), (b:HistoricalTerritory {colony_id: 'ellice_islands_1976_1978'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gilbert_and_ellice_islands_1916_1976'}), (b:HistoricalTerritory {colony_id: 'gilbert_islands_1976_1979'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gilbert_islands_1976_1979'}), (b:HistoricalTerritory {colony_id: 'gilbert_and_ellice_islands_1916_1976'}) MERGE (a)-[:SUCCEEDED {description: 'Gilbert Islands separated from Ellice Islands', succession_type: 'COMPLEX_SUCCESSION', year: 1976, detail: 'SEPARATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gold_coast_colony_1874_1957'}), (b:HistoricalTerritory {colony_id: 'ashanti_1901_1957'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gold_coast_colony_1874_1957'}), (b:HistoricalTerritory {colony_id: 'british_togoland_1919_1957'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gold_coast_colony_1874_1957'}), (b:HistoricalTerritory {colony_id: 'northern_territories_gold_coast_1897_1957'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gold_coast_colony_1874_1957'}), (b:HistoricalTerritory {colony_id: 'british_gold_coast_1821_1874'}) MERGE (a)-[:SUCCEEDED {description: 'Formal colony established after Ashanti conquest', succession_type: 'DIRECT_SUCCESSION', year: 1874, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'grenada_colony_1763_1974'}), (b:HistoricalTerritory {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'grenada_colony_1763_1974'}), (b:HistoricalTerritory {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1959, start_year: 1833}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'griqualand_west_1871_1880'}), (b:HistoricalTerritory {colony_id: 'cape_colony_british_1806_1910'}) MERGE (a)-[:INCORPORATED_INTO {description: 'Griqualand West incorporated into Cape Colony', year: 1880, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ile_royale_1713_1763'}), (b:HistoricalTerritory {colony_id: 'nova_scotia_pre_1713_1784'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ile_royale_1713_1763'}), (b:HistoricalTerritory {colony_id: 'new_france_1608_1763'}) MERGE (a)-[:PART_OF {created_date: 1753030225686, end_year: 1763, start_year: 1713}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'imperial_british_east_africa_company_territory_1888_1895'}), (b:HistoricalTerritory {colony_id: 'east_africa_protectorate_1895_1920'}) MERGE (a)-[:BECAME_PROTECTORATE {description: 'The territory was transferred from the bankrupt IBEA Company to direct British government control.', year: 1895, detail: 'BECAME_PROTECTORATE'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ireland_uk_1801_1922'}), (b:HistoricalTerritory {colony_id: 'irish_free_state_1922_1937'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ireland_uk_1801_1922'}), (b:HistoricalTerritory {colony_id: 'northern_ireland_1920'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'isle_de_france_british_occupation_1810_1814'}), (b:HistoricalTerritory {colony_id: 'mauritius_1814_1968'}) MERGE (a)-[:BECAME_CROWN_COLONY {description: 'Isle de France became British Crown Colony of Mauritius', year: 1814, detail: 'BECAME_CROWN_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jamaica_1655_1962'}), (b:HistoricalTerritory {colony_id: 'british_honduras_1862_1981'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T00:41:49', source: 'historical_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jamaica_1655_1962'}), (b:HistoricalTerritory {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'james_island_trading_post_1661_1816'}), (b:HistoricalTerritory {colony_id: 'gambia_colony_1816_1888'}) MERGE (a)-[:REORGANIZED_AS {description: 'Trading post reorganized as Crown Colony', year: 1816, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kenya_colony_and_protectorate_of_1920_1963'}), (b:HistoricalTerritory {colony_id: 'east_africa_protectorate_1895_1920'}) MERGE (a)-[:SUCCEEDED {description: 'East Africa Protectorate became Kenya Colony and Protectorate', succession_type: 'DIRECT_SUCCESSION', year: 1920, detail: 'BECAME_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_ireland_1541_1801'}), (b:HistoricalTerritory {colony_id: 'ireland_uk_1801_1922'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'labuan_1846_1963'}), (b:HistoricalTerritory {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lagos_protectorate_1887_1906'}), (b:HistoricalTerritory {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'leeward_islands_colony_1671_1816'}), (b:HistoricalTerritory {colony_id: 'antigua_montserrat_barbuda_1816_1833'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'leeward_islands_colony_1671_1816'}), (b:HistoricalTerritory {colony_id: 'stkitts_nevis_anguilla_1816_1833'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lower_burma_1824_1886'}), (b:HistoricalTerritory {colony_id: 'burma_british_india_1886_1937'}) MERGE (a)-[:REORGANIZED_AS {year: 1886, detail: 'CONSOLIDATED_AS_PROVINCE'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lower_canada_1791_1841'}), (b:HistoricalTerritory {colony_id: 'new_brunswick_1784_1867'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T00:41:49', source: 'historical_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lower_canada_1791_1841'}), (b:HistoricalTerritory {colony_id: 'upper_canada_1791_1841'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T00:41:49', source: 'historical_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lower_canada_1791_1841'}), (b:HistoricalTerritory {colony_id: 'province_of_canada_1841_1867'}) MERGE (a)-[:MERGED_INTO {description: 'Lower Canada merged with Upper Canada to form Province of Canada (Act of Union 1840)', year: 1841, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'madras_presidency_company_1640_1858'}), (b:HistoricalTerritory {colony_id: 'madras_presidency_crown_1858_1947'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'Crown took over after Indian Rebellion 1857', year: 1858, detail: 'TRANSFERRED_TO_CROWN'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'madras_presidency_crown_1858_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:FEDERATED_INTO {description: 'Madras Presidency joined India', year: 1947, detail: 'JOINED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'madras_presidency_crown_1858_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'madras_presidency_crown_1858_1947'}), (b:HistoricalTerritory {colony_id: 'madras_presidency_company_1640_1858'}) MERGE (a)-[:SUCCEEDED {description: 'Crown took over after Indian Rebellion 1857', succession_type: 'DIRECT_SUCCESSION', year: 1858, detail: 'TRANSFERRED_TO_CROWN'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mainland_british_columbia_1858_1866'}), (b:HistoricalTerritory {colony_id: 'united_colony_of_bc_1866_1871'}) MERGE (a)-[:MERGED_INTO {year: 1866, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mainland_british_columbia_1858_1866'}), (b:HistoricalTerritory {colony_id: 'vancouver_island_1849_1866'}) MERGE (a)-[:SUCCEEDED {description: 'Vancouver Island merged with mainland British Columbia colony', succession_type: 'COMPLEX_SUCCESSION', year: 1866, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malacca_settlement_1824_1826'}), (b:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:INCORPORATED_INTO {description: 'Malacca incorporated into Straits Settlements', year: 1826, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malaya_independent_1957_1963'}), (b:HistoricalTerritory {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malayan_union_1946_1948'}), (b:HistoricalTerritory {colony_id: 'federation_of_malaya_1948_1957'}) MERGE (a)-[:REORGANIZED_AS {description: 'Malayan Union reorganized as Federation due to opposition', year: 1948, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malayan_union_1946_1948'}), (b:HistoricalTerritory {colony_id: 'federated_malay_states_1895_1946'}) MERGE (a)-[:SUCCEEDED {description: 'FMS incorporated into Malayan Union', succession_type: 'COMPLEX_SUCCESSION', year: 1946, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malayan_union_1946_1948'}), (b:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:SUCCEEDED {description: 'Penang and Malacca joined Malayan Union', succession_type: 'COMPLEX_SUCCESSION', year: 1946, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malayan_union_1946_1948'}), (b:HistoricalTerritory {colony_id: 'unfederated_malay_states_1909_1946'}) MERGE (a)-[:SUCCEEDED {description: 'UMS incorporated into Malayan Union', succession_type: 'COMPLEX_SUCCESSION', year: 1946, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malaysia_1963'}), (b:HistoricalTerritory {colony_id: 'singapore_independent_1965'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mandatory_iraq_1920_1932'}), (b:HistoricalTerritory {colony_id: 'iraq_1932_ongoing'}) MERGE (a)-[:BECAME_INDEPENDENT {description: 'Iraq became first Arab state independent from mandate', year: 1932, detail: 'BECAME_INDEPENDENT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mandatory_iraq_1920_1932'}), (b:HistoricalTerritory {colony_id: 'mesopotamia_british_occupied_1914_1920'}) MERGE (a)-[:SUCCEEDED {description: 'Mesopotamia became League of Nations mandate', succession_type: 'DIRECT_SUCCESSION', year: 1920, detail: 'BECAME_MANDATE'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'maryland_colony_1634_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'maryland_colony_1634_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'massachusetts_bay_colony_1630_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'massachusetts_bay_colony_1630_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mauritius_1814_1968'}), (b:HistoricalTerritory {colony_id: 'isle_de_france_british_occupation_1810_1814'}) MERGE (a)-[:SUCCEEDED {description: 'Isle de France became British Crown Colony of Mauritius', succession_type: 'DIRECT_SUCCESSION', year: 1814, detail: 'BECAME_CROWN_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mesopotamia_british_occupied_1914_1920'}), (b:HistoricalTerritory {colony_id: 'mandatory_iraq_1920_1932'}) MERGE (a)-[:BECAME_MANDATE {description: 'Mesopotamia became League of Nations mandate', year: 1920, detail: 'BECAME_MANDATE'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'minorca_first_1708_1756'}), (b:HistoricalTerritory {colony_id: 'minorca_second_1763_1782'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'minorca_second_1763_1782'}), (b:HistoricalTerritory {colony_id: 'minorca_third_1798_1802'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'montserrat_1632_ongoing'}), (b:HistoricalTerritory {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'montserrat_1632_ongoing'}), (b:HistoricalTerritory {colony_id: 'antigua_montserrat_barbuda_1816_1833'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1833, start_year: 1816}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'natalia_republic_1839_1843'}), (b:HistoricalTerritory {colony_id: 'colony_of_natal_1843_1910'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'Britain annexed Natalia Republic as Colony of Natal', year: 1843, detail: 'ANNEXED_BY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_brunswick_1784_1867'}), (b:HistoricalTerritory {colony_id: 'lower_canada_1791_1841'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T00:41:49', source: 'historical_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_brunswick_1784_1867'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:FEDERATED_INTO {description: 'New Brunswick joined Confederation as founding province', year: 1867, detail: 'CONFEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_brunswick_1784_1867'}), (b:HistoricalTerritory {colony_id: 'new_brunswick_province_1867'}) MERGE (a)-[:EVOLVED_INTO {year: 1867}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_brunswick_province_1867'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_france_1608_1763'}), (b:HistoricalTerritory {colony_id: 'province_of_quebec_british_1763_1791'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_france_1608_1763'}), (b:HistoricalTerritory {colony_id: 'province_of_quebec_british_1763_1791'}) MERGE (a)-[:TRANSFERRED_TERRITORY {created_date: 1753030225718, year: 1763}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_hampshire_colony_1623_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_hampshire_colony_1623_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_jersey_colony_1664_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_jersey_colony_1664_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_south_wales_original_1788_1901'}), (b:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:FEDERATED_INTO {description: 'New South Wales joined Federation as founding state', year: 1901, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_south_wales_original_1788_1901'}), (b:HistoricalTerritory {colony_id: 'queensland_1859_1901'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_south_wales_original_1788_1901'}), (b:HistoricalTerritory {colony_id: 'van_diemens_land_1803_1856'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_south_wales_original_1788_1901'}), (b:HistoricalTerritory {colony_id: 'victoria_colony_1851_1901'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_york_colony_1664_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_york_colony_1664_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'new_zealand_colony_1840_1907'}), (b:HistoricalTerritory {colony_id: 'dominion_of_new_zealand_1907_1947'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'newfoundland_commission_1934_1949'}), (b:HistoricalTerritory {colony_id: 'canada_independent_1931'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'newfoundland_province_1949'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'niger_coast_protectorate_1893_1900'}), (b:HistoricalTerritory {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:REORGANIZED_AS {description: 'Niger Coast Protectorate reorganized as Southern Nigeria', year: 1900, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'niger_coast_protectorate_1893_1900'}), (b:HistoricalTerritory {colony_id: 'oil_rivers_protectorate_1885_1893'}) MERGE (a)-[:SUCCEEDED {description: 'Oil Rivers Protectorate renamed to Niger Coast Protectorate', succession_type: 'DIRECT_SUCCESSION', year: 1893, detail: 'RENAMED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'north_borneo_crown_colony_1946_1963'}), (b:HistoricalTerritory {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'north_borneo_crown_colony_1946_1963'}), (b:HistoricalTerritory {colony_id: 'british_north_borneo_1882_1946'}) MERGE (a)-[:SUCCEEDED {description: 'Company territory became Crown Colony', succession_type: 'DIRECT_SUCCESSION', year: 1946, detail: 'BECAME_CROWN_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'north_carolina_colony_1663_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'north_carolina_colony_1663_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'north_west_frontier_province_1901_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:FEDERATED_INTO {description: 'NWFP joined Pakistan', year: 1947, detail: 'JOINED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'north_west_frontier_province_1901_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'north_west_frontier_province_1901_1947'}), (b:HistoricalTerritory {colony_id: 'punjab_province_1849_1947'}) MERGE (a)-[:SUCCEEDED {description: 'NWFP created from frontier districts of Punjab', succession_type: 'COMPLEX_SUCCESSION', year: 1901, detail: 'CARVED_OUT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'north_western_territory_1670_1870'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'northern_nigeria_1900_1914'}), (b:HistoricalTerritory {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}) MERGE (a)-[:MERGED_INTO {description: 'Northern and Southern Nigeria amalgamated by Lord Lugard', year: 1914, detail: 'AMALGAMATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'northern_nigeria_1900_1914'}), (b:HistoricalTerritory {colony_id: 'royal_niger_company_territory_1886_1900'}) MERGE (a)-[:SUCCEEDED {description: 'Company territory became Northern Nigeria Protectorate', succession_type: 'DIRECT_SUCCESSION', year: 1900, detail: 'BECAME_PROTECTORATE'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'northern_nigeria_1900_1914'}), (b:HistoricalTerritory {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:SUCCEEDED {description: 'Southern and Northern Nigeria merged to form Nigeria', succession_type: 'COMPLEX_SUCCESSION', year: '1914', detail: 'MERGED_WITH'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'northern_rhodesia_colony_1924_1953'}), (b:HistoricalTerritory {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}) MERGE (a)-[:FEDERATED_INTO {description: 'Northern Rhodesia joined Central African Federation', year: 1953, detail: 'JOINED_FEDERATION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nova_scotia_post_1784_1867'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nova_scotia_post_1784_1867'}), (b:HistoricalTerritory {colony_id: 'nova_scotia_province_1867'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nova_scotia_pre_1713_1784'}), (b:HistoricalTerritory {colony_id: 'cape_breton_colony_1784_1820'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nova_scotia_pre_1713_1784'}), (b:HistoricalTerritory {colony_id: 'new_brunswick_1784_1867'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nova_scotia_pre_1713_1784'}), (b:HistoricalTerritory {colony_id: 'nova_scotia_post_1784_1867'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nova_scotia_province_1867'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nunavut_1999'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nyasaland_1891_1964'}), (b:HistoricalTerritory {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}) MERGE (a)-[:FEDERATED_INTO {description: 'Nyasaland joined Central African Federation', year: 1953, detail: 'JOINED_FEDERATION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nyasaland_1891_1964'}), (b:HistoricalTerritory {colony_id: 'british_central_africa_protectorate_1891_1907'}) MERGE (a)-[:SUCCEEDED {description: 'British Central Africa Protectorate renamed to Nyasaland', succession_type: 'DIRECT_SUCCESSION', year: 1907, detail: 'RENAMED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'oil_rivers_protectorate_1885_1893'}), (b:HistoricalTerritory {colony_id: 'niger_coast_protectorate_1893_1900'}) MERGE (a)-[:REORGANIZED_AS {description: 'Oil Rivers Protectorate renamed to Niger Coast Protectorate', year: 1893, detail: 'RENAMED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ontario_1867'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'orange_free_state_1854_1900'}), (b:HistoricalTerritory {colony_id: 'orange_river_colony_1900_1910'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'Orange Free State conquered and renamed during Second Boer War', year: 1900, detail: 'CONQUERED_AND_RENAMED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'orange_river_colony_1900_1910'}), (b:HistoricalTerritory {colony_id: 'union_of_south_africa_1910_1961'}) MERGE (a)-[:FEDERATED_INTO {description: 'Orange River Colony joined Union as Orange Free State Province', year: 1910, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'orange_river_sovereignty_1848_1854'}), (b:HistoricalTerritory {colony_id: 'orange_free_state_1854_1900'}) MERGE (a)-[:BECAME_INDEPENDENT {description: 'Britain granted independence in Bloemfontein Convention', year: 1854, detail: 'INDEPENDENCE_GRANTED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'palestine_1920_1948'}), (b:HistoricalTerritory {colony_id: 'state_of_israel_1948'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'penang_prince_of_wales_island_1786_1826'}), (b:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:INCORPORATED_INTO {description: 'Penang incorporated into Straits Settlements', year: 1826, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pennsylvania_colony_1681_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pennsylvania_colony_1681_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'prince_edward_island_1769_1873'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:FEDERATED_INTO {description: 'Prince Edward Island joined Confederation as 7th province', year: 1873, detail: 'JOINED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'prince_edward_island_1769_1873'}), (b:HistoricalTerritory {colony_id: 'prince_edward_island_province_1873'}) MERGE (a)-[:EVOLVED_INTO {year: 1873}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'prince_edward_island_province_1873'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'princely_states_placeholder_1818_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'princely_states_placeholder_1818_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'province_of_canada_1841_1867'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:FEDERATED_INTO {description: 'Province of Canada split into Ontario and Quebec, joined Confederation as Dominion of Canada', year: 1867, detail: 'CONFEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'province_of_canada_1841_1867'}), (b:HistoricalTerritory {colony_id: 'ontario_1867'}) MERGE (a)-[:EVOLVED_INTO {year: 1867}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'province_of_canada_1841_1867'}), (b:HistoricalTerritory {colony_id: 'quebec_1867'}) MERGE (a)-[:EVOLVED_INTO {year: 1867}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'province_of_canada_1841_1867'}), (b:HistoricalTerritory {colony_id: 'lower_canada_1791_1841'}) MERGE (a)-[:SUCCEEDED {description: 'Lower Canada merged with Upper Canada to form Province of Canada (Act of Union 1840)', succession_type: 'COMPLEX_SUCCESSION', year: 1841, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'province_of_canada_1841_1867'}), (b:HistoricalTerritory {colony_id: 'upper_canada_1791_1841'}) MERGE (a)-[:SUCCEEDED {description: 'Upper Canada merged with Lower Canada to form Province of Canada (Act of Union 1840)', succession_type: 'COMPLEX_SUCCESSION', year: 1841, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'province_of_freedom_1787_1792'}), (b:HistoricalTerritory {colony_id: 'sierra_leone_company_settlement_1792_1808'}) MERGE (a)-[:REORGANIZED_AS {description: 'Province of Freedom reorganized under Sierra Leone Company', year: 1792, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'province_of_quebec_british_1763_1791'}), (b:HistoricalTerritory {colony_id: 'lower_canada_1791_1841'}) MERGE (a)-[:PARTITIONED_INTO {date: '1791-12-26', description: 'Constitutional Act 1791 divided Quebec', relationship_type: 'PARTITIONED_INTO', year: 1791}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'province_of_quebec_british_1763_1791'}), (b:HistoricalTerritory {colony_id: 'upper_canada_1791_1841'}) MERGE (a)-[:PARTITIONED_INTO {date: '1791-12-26', description: 'Constitutional Act 1791 divided Quebec', relationship_type: 'PARTITIONED_INTO', year: 1791}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'punjab_province_1849_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'punjab_province_1849_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'punjab_province_1849_1947'}), (b:HistoricalTerritory {colony_id: 'north_west_frontier_province_1901_1947'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'punjab_province_1849_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'quebec_1867'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'queensland_1859_1901'}), (b:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:FEDERATED_INTO {description: 'Queensland joined Federation as founding state', year: 1901, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'red_river_colony_1811_1870'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rhode_island_colony_1636_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rhode_island_colony_1636_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rhodesia_udi_1965_1979'}), (b:HistoricalTerritory {colony_id: 'zimbabwe_rhodesia_1979_1979'}) MERGE (a)-[:REORGANIZED_AS {description: 'Internal settlement created Zimbabwe Rhodesia', year: 1979, detail: 'INTERNAL_SETTLEMENT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'royal_niger_company_territory_1886_1900'}), (b:HistoricalTerritory {colony_id: 'northern_nigeria_1900_1914'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ruperts_land_1670_1870'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ruperts_land_1670_1870'}), (b:HistoricalTerritory {colony_id: 'north_western_territory_1670_1870'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ruperts_land_1670_1870'}), (b:HistoricalTerritory {colony_id: 'red_river_colony_1811_1870'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'saint_christopher_nevis_anguilla_1958_1983'}), (b:HistoricalTerritory {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'saint_christopher_nevis_anguilla_1958_1983'}), (b:HistoricalTerritory {colony_id: 'stkitts_nevis_anguilla_1816_1833'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1833, start_year: 1816}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'saint_lucia_colony_1814_1979'}), (b:HistoricalTerritory {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sarawak_1841_1946'}), (b:HistoricalTerritory {colony_id: 'sarawak_crown_colony_1946_1963'}) MERGE (a)-[:BECAME_CROWN_COLONY {description: 'Brooke family ceded Sarawak to Crown', year: 1946, detail: 'BECAME_CROWN_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sarawak_crown_colony_1946_1963'}), (b:HistoricalTerritory {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sarawak_crown_colony_1946_1963'}), (b:HistoricalTerritory {colony_id: 'sarawak_1841_1946'}) MERGE (a)-[:SUCCEEDED {description: 'Brooke family ceded Sarawak to Crown', succession_type: 'DIRECT_SUCCESSION', year: 1946, detail: 'BECAME_CROWN_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'saskatchewan_1905'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'settlement_of_belize_1798_1862'}), (b:HistoricalTerritory {colony_id: 'british_honduras_1862_1981'}) MERGE (a)-[:BECAME_COLONY {description: 'The settlement was formally declared the Crown Colony of British Honduras.', year: 1862, detail: 'FORMALIZED_AS_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'seychelles_1903_1976'}), (b:HistoricalTerritory {colony_id: 'seychelles_mauritius_dependency_1814_1903'}) MERGE (a)-[:SUCCEEDED {description: 'Seychelles separated from Mauritius as Crown Colony', succession_type: 'DIRECT_SUCCESSION', year: 1903, detail: 'BECAME_SEPARATE_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'seychelles_mauritius_dependency_1814_1903'}), (b:HistoricalTerritory {colony_id: 'seychelles_1903_1976'}) MERGE (a)-[:BECAME_SEPARATE_COLONY {description: 'Seychelles separated from Mauritius as Crown Colony', year: 1903, detail: 'BECAME_SEPARATE_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sierra_leone_colony_1808_1896'}), (b:HistoricalTerritory {colony_id: 'sierra_leone_colony_and_protectorate_1787_1961'}) MERGE (a)-[:REORGANIZED_AS {description: 'Colony expanded with interior protectorate', year: 1896, detail: 'EXPANDED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sierra_leone_colony_1808_1896'}), (b:HistoricalTerritory {colony_id: 'sierra_leone_company_settlement_1792_1808'}) MERGE (a)-[:SUCCEEDED {description: 'Company rule ended, became Crown Colony', succession_type: 'DIRECT_SUCCESSION', year: 1808, detail: 'BECAME_CROWN_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sierra_leone_company_settlement_1792_1808'}), (b:HistoricalTerritory {colony_id: 'sierra_leone_colony_1808_1896'}) MERGE (a)-[:BECAME_CROWN_COLONY {description: 'Company rule ended, became Crown Colony', year: 1808, detail: 'BECAME_CROWN_COLONY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sierra_leone_company_settlement_1792_1808'}), (b:HistoricalTerritory {colony_id: 'province_of_freedom_1787_1792'}) MERGE (a)-[:SUCCEEDED {description: 'Province of Freedom reorganized under Sierra Leone Company', succession_type: 'DIRECT_SUCCESSION', year: 1792, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sind_province_1843_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'singapore_crown_colony_1946_1963'}), (b:HistoricalTerritory {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'singapore_crown_colony_1946_1963'}), (b:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:SUCCEEDED {description: 'Singapore became separate crown colony', succession_type: 'COMPLEX_SUCCESSION', year: 1946, detail: 'SEPARATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'singapore_settlement_1819_1826'}), (b:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:INCORPORATED_INTO {description: 'Singapore incorporated into Straits Settlements', year: 1826, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'socotra_island_1886_1967'}), (b:HistoricalTerritory {colony_id: 'south_yemen_1967_1990'}) MERGE (a)-[:MERGED_INTO {description: 'Socotra became part of South Yemen', year: 1967, detail: 'BECAME_PART_OF'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'south_african_republic_restored_1881_1900'}), (b:HistoricalTerritory {colony_id: 'transvaal_colony_second_british_1900_1910'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'Transvaal conquered and renamed during Second Boer War', year: 1900, detail: 'CONQUERED_AND_RENAMED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'south_african_republic_transvaal_1852_1877'}), (b:HistoricalTerritory {colony_id: 'transvaal_colony_first_british_1877_1881'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'Britain annexed Transvaal citing financial difficulties and conflicts', year: 1877, detail: 'ANNEXED_BY'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'south_australia_1836_1901'}), (b:HistoricalTerritory {colony_id: 'western_australia_1832_1901'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T10:19:49', source: 'comprehensive_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'south_australia_1836_1901'}), (b:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:FEDERATED_INTO {description: 'South Australia joined Federation as founding state', year: 1901, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'south_carolina_colony_1663_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'south_carolina_colony_1663_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'southern_nigeria_protectorate_1900_1914'}), (b:HistoricalTerritory {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'southern_nigeria_protectorate_1900_1914'}), (b:HistoricalTerritory {colony_id: 'lagos_protectorate_1887_1906'}) MERGE (a)-[:SUCCEEDED {description: 'Lagos Protectorate incorporated into Southern Nigeria', succession_type: 'COMPLEX_SUCCESSION', year: '1906', detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'southern_nigeria_protectorate_1900_1914'}), (b:HistoricalTerritory {colony_id: 'lagos_protectorate_1887_1906'}) MERGE (a)-[:SUCCEEDED {description: 'Lagos merged into Southern Nigeria Protectorate', succession_type: 'COMPLEX_SUCCESSION', year: 1906, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'southern_nigeria_protectorate_1900_1914'}), (b:HistoricalTerritory {colony_id: 'niger_coast_protectorate_1893_1900'}) MERGE (a)-[:SUCCEEDED {description: 'Niger Coast Protectorate reorganized as Southern Nigeria', succession_type: 'DIRECT_SUCCESSION', year: 1900, detail: 'REORGANIZED_AS'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'southern_rhodesia_colony_1923_1953'}), (b:HistoricalTerritory {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}) MERGE (a)-[:FEDERATED_INTO {description: 'Southern Rhodesia joined Central African Federation', year: 1953, detail: 'JOINED_FEDERATION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'southern_rhodesia_colony_1923_1953'}), (b:HistoricalTerritory {colony_id: 'british_south_africa_company_territory_1889_1923'}) MERGE (a)-[:SUCCEEDED {description: 'Southern Rhodesia became self-governing colony after BSAC rule', succession_type: 'DIRECT_SUCCESSION', year: 1923, detail: 'BECAME_SELF_GOVERNING'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'southern_rhodesia_post_federation_1963'}), (b:HistoricalTerritory {colony_id: 'rhodesia_udi_1965_1979'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'southern_rhodesia_restored_1979_1980'}), (b:HistoricalTerritory {colony_id: 'zimbabwe_rhodesia_1979_1979'}) MERGE (a)-[:SUCCEEDED {description: 'Lancaster House Agreement restored Crown Colony status', succession_type: 'DIRECT_SUCCESSION', year: 1979, detail: 'RESTORED_TO_CROWN'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'st._helena_1659_ongoing'}), (b:HistoricalTerritory {colony_id: 'south_african_republic_restored_1881_1900'}) MERGE (a)-[:NEAR_COAST_OF {created_date: '2025-07-21T10:19:50', source: 'comprehensive_coastal'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'st_vincent_colony_1763_1979'}), (b:HistoricalTerritory {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'st_vincent_colony_1763_1979'}), (b:HistoricalTerritory {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1959, start_year: 1833}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'stkitts_nevis_anguilla_1816_1833'}), (b:HistoricalTerritory {colony_id: 'federal_colony_leeward_islands_1833-1960'}) MERGE (a)-[:MERGED_INTO {year: 1833, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}), (b:HistoricalTerritory {colony_id: 'malayan_union_1946_1948'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}), (b:HistoricalTerritory {colony_id: 'singapore_crown_colony_1946_1963'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}), (b:HistoricalTerritory {colony_id: 'malacca_settlement_1824_1826'}) MERGE (a)-[:SUCCEEDED {description: 'Malacca incorporated into Straits Settlements', succession_type: 'COMPLEX_SUCCESSION', year: 1826, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}), (b:HistoricalTerritory {colony_id: 'penang_prince_of_wales_island_1786_1826'}) MERGE (a)-[:SUCCEEDED {description: 'Penang incorporated into Straits Settlements', succession_type: 'COMPLEX_SUCCESSION', year: 1826, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'straits_settlements_1826_1946'}), (b:HistoricalTerritory {colony_id: 'singapore_settlement_1819_1826'}) MERGE (a)-[:SUCCEEDED {description: 'Singapore incorporated into Straits Settlements', succession_type: 'COMPLEX_SUCCESSION', year: 1826, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'swan_river_colony_1829_1832'}), (b:HistoricalTerritory {colony_id: 'western_australia_1832_1901'}) MERGE (a)-[:REORGANIZED_AS {description: 'Swan River Colony renamed to Western Australia', year: 1832, detail: 'RENAMED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tanganyika_1961_1964'}), (b:HistoricalTerritory {colony_id: 'uganda_1894_1962'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T10:19:49', source: 'comprehensive_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tanganyika_1961_1964'}), (b:HistoricalTerritory {colony_id: 'tanzania_1964'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tanganyika_territory_1922_1961'}), (b:HistoricalTerritory {colony_id: 'tanganyika_1961_1964'}) MERGE (a)-[:BECAME_INDEPENDENT {description: 'Tanganyika gained independence under Julius Nyerere', year: 1961, detail: 'BECAME_INDEPENDENT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tanganyika_territory_1922_1961'}), (b:HistoricalTerritory {colony_id: 'german_east_africa_british_occupied_1916_1922'}) MERGE (a)-[:SUCCEEDED {description: 'German East Africa became League of Nations mandate territory', succession_type: 'DIRECT_SUCCESSION', year: 1922, detail: 'BECAME_MANDATE'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tasmania_1856_1901'}), (b:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:FEDERATED_INTO {description: 'Tasmania joined Federation as founding state', year: 1901, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tasmania_1856_1901'}), (b:HistoricalTerritory {colony_id: 'van_diemens_land_1803_1856'}) MERGE (a)-[:SUCCEEDED {description: 'Van Diemen\'s Land officially renamed to Tasmania and gained self-government', succession_type: 'DIRECT_SUCCESSION', year: 1856, detail: 'RENAMED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tasmania_1856_1901'}), (b:HistoricalTerritory {colony_id: 'van_diemens_land_1803_1856'}) MERGE (a)-[:SUCCEEDED {description: 'Van Diemen\'s Land renamed to Tasmania', succession_type: 'DIRECT_SUCCESSION', year: 1856, detail: 'DIRECT_SUCCESSION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tonga_protectorate_1900_1970'}), (b:HistoricalTerritory {colony_id: 'fiji_1874_1970'}) MERGE (a)-[:NEAR_COAST_OF {created_date: '2025-07-21T10:19:50', source: 'comprehensive_coastal'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'transvaal_colony_first_british_1877_1881'}), (b:HistoricalTerritory {colony_id: 'south_african_republic_restored_1881_1900'}) MERGE (a)-[:BECAME_INDEPENDENT {description: 'Independence restored after First Boer War defeat of British', year: 1881, detail: 'INDEPENDENCE_RESTORED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'transvaal_colony_second_british_1900_1910'}), (b:HistoricalTerritory {colony_id: 'union_of_south_africa_1910_1961'}) MERGE (a)-[:FEDERATED_INTO {description: 'Transvaal joined Union of South Africa as Transvaal Province', year: 1910, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'trinidad_and_tobago_1889_1962'}), (b:HistoricalTerritory {colony_id: 'british_guiana_1831_1966'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T00:41:49', source: 'historical_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'trinidad_and_tobago_1889_1962'}), (b:HistoricalTerritory {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'trinidad_and_tobago_colony_1797_1962'}), (b:HistoricalTerritory {colony_id: 'trinidad_and_tobago_1889_1962'}) MERGE (a)-[:BECAME_INDEPENDENT {description: 'Trinidad and Tobago gained independence from Britain', year: 1962, detail: 'BECAME_INDEPENDENT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'uganda_1894_1962'}), (b:HistoricalTerritory {colony_id: 'tanganyika_1961_1964'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T10:19:49', source: 'comprehensive_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'unfederated_malay_states_1909_1946'}), (b:HistoricalTerritory {colony_id: 'malayan_union_1946_1948'}) MERGE (a)-[:INCORPORATED_INTO {description: 'UMS incorporated into Malayan Union', year: 1946, detail: 'INCORPORATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'union_of_south_africa_1910_1961'}), (b:HistoricalTerritory {colony_id: 'cape_colony_british_1806_1910'}) MERGE (a)-[:SUCCEEDED {description: 'Cape Colony joined Union of South Africa', succession_type: 'FEDERATION_SUCCESSION', year: 1910, detail: 'FEDERATION_SUCCESSION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'union_of_south_africa_1910_1961'}), (b:HistoricalTerritory {colony_id: 'orange_river_colony_1900_1910'}) MERGE (a)-[:SUCCEEDED {description: 'Orange River Colony joined Union of South Africa', succession_type: 'FEDERATION_SUCCESSION', year: 1910, detail: 'FEDERATION_SUCCESSION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'united_colony_of_bc_1866_1871'}), (b:HistoricalTerritory {colony_id: 'british_columbia_province_1871'}) MERGE (a)-[:EVOLVED_INTO {year: 1871}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'united_colony_of_bc_1866_1871'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:FEDERATED_INTO {year: 1871, detail: 'JOINED_CONFEDERATION'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'united_provinces_1877_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:FEDERATED_INTO {description: 'United Provinces joined India', year: 1947, detail: 'JOINED'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'united_provinces_1877_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'upper_canada_1791_1841'}), (b:HistoricalTerritory {colony_id: 'lower_canada_1791_1841'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T00:41:49', source: 'historical_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'upper_canada_1791_1841'}), (b:HistoricalTerritory {colony_id: 'province_of_canada_1841_1867'}) MERGE (a)-[:MERGED_INTO {description: 'Upper Canada merged with Lower Canada to form Province of Canada (Act of Union 1840)', year: 1841, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'van_diemens_land_1803_1856'}), (b:HistoricalTerritory {colony_id: 'tasmania_1856_1901'}) MERGE (a)-[:REORGANIZED_AS {description: 'Van Diemen\'s Land officially renamed to Tasmania and gained self-government', year: 1856, detail: 'RENAMED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vancouver_island_1849_1866'}), (b:HistoricalTerritory {colony_id: 'united_colony_of_bc_1866_1871'}) MERGE (a)-[:MERGED_INTO {year: 1866, detail: 'MERGED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'victoria_colony_1851_1901'}), (b:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:FEDERATED_INTO {description: 'Victoria joined Federation as founding state', year: 1901, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'virginia_colony_1607_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'virginia_colony_1607_1783'}), (b:HistoricalTerritory {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'western_australia_1832_1901'}), (b:HistoricalTerritory {colony_id: 'south_australia_1836_1901'}) MERGE (a)-[:BORDERS_WITH {created_date: '2025-07-21T10:19:49', source: 'comprehensive_borders'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'western_australia_1832_1901'}), (b:HistoricalTerritory {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:FEDERATED_INTO {description: 'Western Australia joined Federation as founding state (last to join after referendum)', year: 1901, detail: 'FEDERATED_INTO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'western_australia_1832_1901'}), (b:HistoricalTerritory {colony_id: 'swan_river_colony_1829_1832'}) MERGE (a)-[:SUCCEEDED {description: 'Swan River Colony renamed to Western Australia', succession_type: 'DIRECT_SUCCESSION', year: 1832, detail: 'RENAMED_TO'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'yukon_territory_1898'}), (b:HistoricalTerritory {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'zanzibar_1890_1963'}), (b:HistoricalTerritory {colony_id: 'zanzibar_independent_1963_1964'}) MERGE (a)-[:BECAME_INDEPENDENT {description: 'Zanzibar gained independence from British protectorate', year: 1963, detail: 'BECAME_INDEPENDENT'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'zanzibar_1890_1963'}), (b:HistoricalTerritory {colony_id: 'tanganyika_territory_1922_1961'}) MERGE (a)-[:SUCCEEDED {description: 'Tanganyika and Zanzibar merged to form Tanzania', succession_type: 'COMPLEX_SUCCESSION', year: '1964', detail: 'MERGED_WITH'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'zanzibar_independent_1963_1964'}), (b:HistoricalTerritory {colony_id: 'tanzania_1964'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'zimbabwe_rhodesia_1979_1979'}), (b:HistoricalTerritory {colony_id: 'southern_rhodesia_restored_1979_1980'}) MERGE (a)-[:TRANSFERRED_SOVEREIGNTY {description: 'Lancaster House Agreement restored Crown Colony status', year: 1979, detail: 'RESTORED_TO_CROWN'}]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'zululand_1887_1897'}), (b:HistoricalTerritory {colony_id: 'colony_of_natal_1843_1910'}) MERGE (a)-[:INCORPORATED_INTO {description: 'Zululand incorporated into Colony of Natal', year: 1897, detail: 'INCORPORATED_INTO'}]->(b);

// Total: 314 nodes, 335 relationships
// ── Princely States of British India ──
// Source: Wikidata SPARQL (Q1336152) + verified manual supplements
// Total: 438 states

MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'achrol_1600_2000'}) SET c += {colony_id: 'achrol_1600_2000', name: 'Achrol', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075277', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1600, independence_year: 2000, latitude: 22.20775, longitude: 76.97021};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ahirwal'}) SET c += {colony_id: 'ahirwal', name: 'Ahirwal', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q4695139', source: 'wikidata_sparql_Q1336152', latitude: 28.172717, longitude: 76.616678};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ajaigarh_state_1765_1949'}) SET c += {colony_id: 'ajaigarh_state_1765_1949', name: 'Ajaigarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q5301066', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1765, independence_year: 1949, latitude: 24.9, longitude: 80.2667, capital: 'Ajaigarh', population: 96596};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'akkalkot_state_1725_1948'}) SET c += {colony_id: 'akkalkot_state_1725_1948', name: 'Akkalkot State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3963975', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1725, independence_year: 1948, latitude: 17.5223064, longitude: 76.2048938};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'akora_1800_1849'}) SET c += {colony_id: 'akora_1800_1849', name: 'Akora', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q28137490', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1800, independence_year: 1849, latitude: 33.532293, longitude: 71.499972};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'alampur'}) SET c += {colony_id: 'alampur', name: 'Alampur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q28171846', source: 'wikidata_sparql_Q1336152', latitude: 21.95, longitude: 71.766667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'alipura_state_1757_1947'}) SET c += {colony_id: 'alipura_state_1757_1947', name: 'Alipura State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q4726842', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1757, independence_year: 1947, latitude: 25.17534, longitude: 79.33549};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'alirajpur_state_1437_1948'}) SET c += {colony_id: 'alirajpur_state_1437_1948', name: 'Alirajpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q4726858', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1437, independence_year: 1948, latitude: 22.3053, longitude: 74.3525};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'alwar_state_1770_1949'}) SET c += {colony_id: 'alwar_state_1770_1949', name: 'Alwar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1553143', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1770, independence_year: 1949, latitude: 27.95, longitude: 76.1, capital: 'Alwar', population: 682926};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'amala_state'}) SET c += {colony_id: 'amala_state', name: 'Amala State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11942776', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'amb_state_1900_1969'}) SET c += {colony_id: 'amb_state_1900_1969', name: 'Amb State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2841472', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1900, independence_year: 1969, latitude: 34.364606, longitude: 72.859433};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ambliara_state_1600_1943'}) SET c += {colony_id: 'ambliara_state_1600_1943', name: 'Ambliara State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11905286', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1600, independence_year: 1943, latitude: 23.2219, longitude: 73.2167};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'anandpur_state'}) SET c += {colony_id: 'anandpur_state', name: 'Anandpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11905441', source: 'wikidata_sparql_Q1336152', latitude: 20.871879, longitude: 70.674426};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'angadh_estate_1874_1947'}) SET c += {colony_id: 'angadh_estate_1874_1947', name: 'Angadh Estate', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104151568', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1874, independence_year: 1947};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'anghar'}) SET c += {colony_id: 'anghar', name: 'Anghar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11905609', source: 'wikidata_sparql_Q1336152', latitude: 23.92777778, longitude: 72.225};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'athgarh_state_1178_1949'}) SET c += {colony_id: 'athgarh_state_1178_1949', name: 'Athgarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2869051', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1178, independence_year: 1949, latitude: 20.51666667, longitude: 85.62666667, population: 42351};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'athmallik_state_1874_1948'}) SET c += {colony_id: 'athmallik_state_1874_1948', name: 'Athmallik State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17513838', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1874, independence_year: 1948, latitude: 20.7197, longitude: 84.53};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'aundh_state_1699_1948'}) SET c += {colony_id: 'aundh_state_1699_1948', name: 'Aundh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2871819', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1699, independence_year: 1948, latitude: 17.54583333, longitude: 74.375};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'avchar_state'}) SET c += {colony_id: 'avchar_state', name: 'Avchar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075165', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'babariawad_1947'}) SET c += {colony_id: 'babariawad_1947', name: 'Babariawad', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q4837532', source: 'wikidata_sparql_Q1336152', independence_year: 1947, latitude: 20.8667, longitude: 71.3667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'badu'}) SET c += {colony_id: 'badu', name: 'Badu', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11907536', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'baghal_state_1310_1948'}) SET c += {colony_id: 'baghal_state_1310_1948', name: 'Baghal State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2879034', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1310, independence_year: 1948, latitude: 31.15, longitude: 76.97};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'baghat_state_1600_1948'}) SET c += {colony_id: 'baghat_state_1600_1948', name: 'Baghat State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q520403', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1600, independence_year: 1948, latitude: 30.525, longitude: 80.645};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bahawalpur_state_1690_1955'}) SET c += {colony_id: 'bahawalpur_state_1690_1955', name: 'Bahawalpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q800236', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1690, independence_year: 1955, latitude: 28.8333, longitude: 71.7167, capital: 'Bahawalpur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bajana_state'}) SET c += {colony_id: 'bajana_state', name: 'Bajana State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11907630', source: 'wikidata_sparql_Q1336152', latitude: 23.11666667, longitude: 71.81666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bakhatgarh'}) SET c += {colony_id: 'bakhatgarh', name: 'Bakhatgarh', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q28419349', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'balasinor_state_1758_1948'}) SET c += {colony_id: 'balasinor_state_1758_1948', name: 'Balasinor State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17514653', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1758, independence_year: 1948, latitude: 22.95, longitude: 73.33, capital: 'Balasinor'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'balladhdarh_state_1710_1867'}) SET c += {colony_id: 'balladhdarh_state_1710_1867', name: 'Balladhdarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152096', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1710, independence_year: 1867};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bamanbore_state'}) SET c += {colony_id: 'bamanbore_state', name: 'Bamanbore State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11907764', source: 'wikidata_sparql_Q1336152', latitude: 22.4, longitude: 71.1, capital: 'Bamanbore'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bamra_state_1545_1948'}) SET c += {colony_id: 'bamra_state_1545_1948', name: 'Bamra State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q806019', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1545, independence_year: 1948, latitude: 21.53, longitude: 84.73};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'banda_1790_1858'}) SET c += {colony_id: 'banda_1790_1858', name: 'Banda', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q806233', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1790, independence_year: 1858};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'banganapalle_state_1790_1948'}) SET c += {colony_id: 'banganapalle_state_1790_1948', name: 'Banganapalle State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q13389050', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1790, independence_year: 1948, latitude: 15.3167, longitude: 78.2333, capital: 'Banaganapalle', population: 32279};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bansda_1781_1948'}) SET c += {colony_id: 'bansda_1781_1948', name: 'Bansda', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q4857117', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1781, independence_year: 1948, latitude: 20.78333333, longitude: 73.46666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'banswara_state_1497_1949'}) SET c += {colony_id: 'banswara_state_1497_1949', name: 'Banswara State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q806963', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1497, independence_year: 1949, latitude: 23.55, longitude: 74.45, capital: 'Banswara', population: 165350};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bantva_manavadar_state_1760_1947'}) SET c += {colony_id: 'bantva_manavadar_state_1760_1947', name: 'Bantva Manavadar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q918500', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1760, independence_year: 1947, latitude: 21.5, longitude: 70.13};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'baoni_state_1784_1948'}) SET c += {colony_id: 'baoni_state_1784_1948', name: 'Baoni State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q807069', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1784, independence_year: 1948, latitude: 25.98, longitude: 79.85};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'baramba_state_1305_1949'}) SET c += {colony_id: 'baramba_state_1305_1949', name: 'Baramba State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2883798', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1305, independence_year: 1949, latitude: 20.4208, longitude: 85.3781};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'baraundha_state_1169_1950'}) SET c += {colony_id: 'baraundha_state_1169_1950', name: 'Baraundha State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q807288', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1169, independence_year: 1950, latitude: 25.05, longitude: 80.63333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'baria_state_1524_1948'}) SET c += {colony_id: 'baria_state_1524_1948', name: 'Baria State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2884562', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1524, independence_year: 1948, latitude: 22.7, longitude: 73.91};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'baroda_state_1721_1949'}) SET c += {colony_id: 'baroda_state_1721_1949', name: 'Baroda State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q808575', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1721, independence_year: 1949, latitude: 22.18, longitude: 73.12, capital: 'Vadodara'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'barpali'}) SET c += {colony_id: 'barpali', name: 'Barpali', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11908231', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'barwala_state'}) SET c += {colony_id: 'barwala_state', name: 'Barwala State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11908637', source: 'wikidata_sparql_Q1336152', latitude: 22.1375, longitude: 71.95833333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'barwani_state_836_1948'}) SET c += {colony_id: 'barwani_state_836_1948', name: 'Barwani State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q809652', source: 'wikidata_sparql_Q1336152', dynasty_founded: 836, independence_year: 1948, latitude: 22.03, longitude: 74.9, capital: 'Barwani', population: 176666};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bashahr_state_1412_1948'}) SET c += {colony_id: 'bashahr_state_1412_1948', name: 'Bashahr State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q809955', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1412, independence_year: 1948, latitude: 31.866666666, longitude: 78.333333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'basoda_state_1753_1947'}) SET c += {colony_id: 'basoda_state_1753_1947', name: 'Basoda State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q810432', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1753, independence_year: 1947, latitude: 23.849379, longitude: 77.937012};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bastar_state_1853_1948'}) SET c += {colony_id: 'bastar_state_1853_1948', name: 'Bastar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q810557', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1853, independence_year: 1948, latitude: 20.083, longitude: 83.2, capital: 'Jagdalpur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'baudh_state_1874_1948'}) SET c += {colony_id: 'baudh_state_1874_1948', name: 'Baudh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q894995', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1874, independence_year: 1948, latitude: 20.84, longitude: 84.32};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bavra_state'}) SET c += {colony_id: 'bavra_state', name: 'Bavra State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11908840', source: 'wikidata_sparql_Q1336152', latitude: 16.54361111, longitude: 73.8575};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'beja_state_1800_1948'}) SET c += {colony_id: 'beja_state_1800_1948', name: 'Beja State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2902467', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1800, independence_year: 1948, latitude: 30.93333333, longitude: 77.03333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'benares_state_1770_1948'}) SET c += {colony_id: 'benares_state_1770_1948', name: 'Benares State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1375154', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1770, independence_year: 1948, latitude: 25.282, longitude: 82.9563, capital: 'Varanasi', population: 115773};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'beri_state_1750_1950'}) SET c += {colony_id: 'beri_state_1750_1950', name: 'Beri State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909106', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1750, independence_year: 1950, latitude: 25.91666667, longitude: 79.9};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhabar_state'}) SET c += {colony_id: 'bhabar_state', name: 'Bhabar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21076367', source: 'wikidata_sparql_Q1336152', latitude: 24.071837, longitude: 71.589231};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhadli_state'}) SET c += {colony_id: 'bhadli_state', name: 'Bhadli State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909248', source: 'wikidata_sparql_Q1336152', latitude: 22.01666667, longitude: 71.58333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhadvana_state'}) SET c += {colony_id: 'bhadvana_state', name: 'Bhadvana State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075443', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhaisunda_1812_1948'}) SET c += {colony_id: 'bhaisunda_1812_1948', name: 'Bhaisunda', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909259', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1812, independence_year: 1948, latitude: 25.3, longitude: 80.8};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhajji_state_1800_1948'}) SET c += {colony_id: 'bhajji_state_1800_1948', name: 'Bhajji State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q642037', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1800, independence_year: 1948, latitude: 31.4, longitude: 77.2};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhalala'}) SET c += {colony_id: 'bhalala', name: 'Bhalala', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909260', source: 'wikidata_sparql_Q1336152', latitude: 22.85, longitude: 71.93333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhandaria'}) SET c += {colony_id: 'bhandaria', name: 'Bhandaria', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909266', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bharatpur_state_1680_1948'}) SET c += {colony_id: 'bharatpur_state_1680_1948', name: 'Bharatpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q854850', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1680, independence_year: 1948, latitude: 27.22, longitude: 77.48, capital: 'Bharatpur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bharauli_state'}) SET c += {colony_id: 'bharauli_state', name: 'Bharauli State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909267', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bharejda'}) SET c += {colony_id: 'bharejda', name: 'Bharejda', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075444', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhathan_state'}) SET c += {colony_id: 'bhathan_state', name: 'Bhathan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17588101', source: 'wikidata_sparql_Q1336152', latitude: 22.6833, longitude: 71.9};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhavnagar_state_1723_1948'}) SET c += {colony_id: 'bhavnagar_state_1723_1948', name: 'Bhavnagar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q854917', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1723, independence_year: 1948, latitude: 28.76, longitude: 72.15, capital: 'Bhavnagar', population: 464671};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhayavadar'}) SET c += {colony_id: 'bhayavadar', name: 'Bhayavadar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909279', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhith_bhagwanpur_state_1711_1948'}) SET c += {colony_id: 'bhith_bhagwanpur_state_1711_1948', name: 'Bhith Bhagwanpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152097', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1711, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhoika_state'}) SET c += {colony_id: 'bhoika_state', name: 'Bhoika State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909287', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhojavadar'}) SET c += {colony_id: 'bhojavadar', name: 'Bhojavadar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075445', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhopal_state_1723_1947'}) SET c += {colony_id: 'bhopal_state_1723_1947', name: 'Bhopal State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q855044', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1723, independence_year: 1947, latitude: 23.25, longitude: 77.4, capital: 'Bhopal'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhor_state_1697_1948'}) SET c += {colony_id: 'bhor_state_1697_1948', name: 'Bhor State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q855058', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1697, independence_year: 1948, latitude: 18.16666667, longitude: 73.85};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bhowal_state'}) SET c += {colony_id: 'bhowal_state', name: 'Bhowal State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075310', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bihat_state'}) SET c += {colony_id: 'bihat_state', name: 'Bihat State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909349', source: 'wikidata_sparql_Q1336152', latitude: 25.41666667, longitude: 79.35};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bihora_state'}) SET c += {colony_id: 'bihora_state', name: 'Bihora State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075380', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bijawar_state_1765_1950'}) SET c += {colony_id: 'bijawar_state_1765_1950', name: 'Bijawar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7905915', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1765, independence_year: 1950, latitude: 24.63, longitude: 79.5, capital: 'Bijawar', population: 110500};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bikaner_state_1465_1947'}) SET c += {colony_id: 'bikaner_state_1465_1947', name: 'Bikaner State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q859966', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1465, independence_year: 1947, latitude: 28.01, longitude: 73.3, capital: 'Bikaner'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bilbari_state'}) SET c += {colony_id: 'bilbari_state', name: 'Bilbari State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909369', source: 'wikidata_sparql_Q1336152', latitude: 21.75, longitude: 84.97};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bildi_state'}) SET c += {colony_id: 'bildi_state', name: 'Bildi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11909376', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bonai_state_1200_1948'}) SET c += {colony_id: 'bonai_state_1200_1948', name: 'Bonai State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q892061', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1200, independence_year: 1948, latitude: 21.75, longitude: 84.97};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'bundi_state_1342_1949'}) SET c += {colony_id: 'bundi_state_1342_1949', name: 'Bundi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q4997536', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1342, independence_year: 1949, latitude: 25.44, longitude: 75.64, capital: 'Bundi', population: 216722};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'cambay_state_1730_1948'}) SET c += {colony_id: 'cambay_state_1730_1948', name: 'Cambay State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1028095', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1730, independence_year: 1948, latitude: 22.3, longitude: 72.62};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'carnatic_state_1692_1855'}) SET c += {colony_id: 'carnatic_state_1692_1855', name: 'Carnatic state', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3277580', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1692, independence_year: 1855, latitude: 24.18, longitude: 88.27, capital: 'Arcot'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chamardi_state'}) SET c += {colony_id: 'chamardi_state', name: 'Chamardi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11913589', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chamba_state_550_1948'}) SET c += {colony_id: 'chamba_state_550_1948', name: 'Chamba State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1060520', source: 'wikidata_sparql_Q1336152', dynasty_founded: 550, independence_year: 1948, latitude: 32.57, longitude: 76.13, capital: 'Chamba', population: 11773};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'changbhakar_1790_1948'}) SET c += {colony_id: 'changbhakar_1790_1948', name: 'Changbhakar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q932370', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1790, independence_year: 1948, latitude: 23.73333333, longitude: 81.81666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'charkhari_state_1765_1947'}) SET c += {colony_id: 'charkhari_state_1765_1947', name: 'Charkhari State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2624304', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1765, independence_year: 1947, latitude: 25.4, longitude: 79.75, capital: 'Charkhari', population: 123254};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chaube_jagirs_1812_1948'}) SET c += {colony_id: 'chaube_jagirs_1812_1948', name: 'Chaube Jagirs', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11927113', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1812, independence_year: 1948, latitude: 25.0833, longitude: 80.8333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chhatarpur_state_1785_1950'}) SET c += {colony_id: 'chhatarpur_state_1785_1950', name: 'Chhatarpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1071493', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1785, independence_year: 1950, latitude: 24.9157, longitude: 79.5822, capital: 'Chhatarpur', population: 156139};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chhota_udaipur_state_1743_1948'}) SET c += {colony_id: 'chhota_udaipur_state_1743_1948', name: 'Chhota Udaipur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17986421', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1743, independence_year: 1948, latitude: 22.32, longitude: 74.01, capital: 'Chhota Udepur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chhuikhadan_state_1750_1950'}) SET c += {colony_id: 'chhuikhadan_state_1750_1950', name: 'Chhuikhadan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2963204', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1750, independence_year: 1950, latitude: 21.53, longitude: 80.98};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chinchli_gaded_state'}) SET c += {colony_id: 'chinchli_gaded_state', name: 'Chinchli Gaded State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11913671', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chitral_state_1571_1969'}) SET c += {colony_id: 'chitral_state_1571_1969', name: 'Chitral State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11317232', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1571, independence_year: 1969, latitude: 35.837777777, longitude: 71.783888888, capital: 'Chitral'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chobari_state'}) SET c += {colony_id: 'chobari_state', name: 'Chobari State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11913700', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chorangla_state'}) SET c += {colony_id: 'chorangla_state', name: 'Chorangla State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075382', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chota_nagpur_states_1821_1947'}) SET c += {colony_id: 'chota_nagpur_states_1821_1947', name: 'Chota Nagpur States', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q5105376', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1821, independence_year: 1947};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chotila'}) SET c += {colony_id: 'chotila', name: 'Chotila', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11913712', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'chuda_state'}) SET c += {colony_id: 'chuda_state', name: 'Chuda State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17318475', source: 'wikidata_sparql_Q1336152', latitude: 22.4833, longitude: 71.7333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'cooch_behar_1586_1949'}) SET c += {colony_id: 'cooch_behar_1586_1949', name: 'Cooch Behar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q509572', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1586, independence_year: 1949, latitude: 26.2, longitude: 89.0};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'cutch_state_1147_1948'}) SET c += {colony_id: 'cutch_state_1147_1948', name: 'Cutch State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1720882', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1147, independence_year: 1948, latitude: 23.915, longitude: 70.367, capital: 'Bhuj', population: 488022};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dabri_state'}) SET c += {colony_id: 'dabri_state', name: 'Dabri State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11916465', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'danta_state_1061_1948'}) SET c += {colony_id: 'danta_state_1061_1948', name: 'Danta State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17513023', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1061, independence_year: 1948, latitude: 24.20305556, longitude: 72.74472222};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'darkoti_1100_1948'}) SET c += {colony_id: 'darkoti_1100_1948', name: 'Darkoti', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3016348', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1100, independence_year: 1948, latitude: 31.0941021, longitude: 77.5909424};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'daspalla_1498_1948'}) SET c += {colony_id: 'daspalla_1498_1948', name: 'Daspalla', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11916643', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1498, independence_year: 1948, latitude: 20.35, longitude: 84.85};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'datarpur_1550_1849'}) SET c += {colony_id: 'datarpur_1550_1849', name: 'Datarpur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11916665', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1550, independence_year: 1849, latitude: 31.82, longitude: 75.66};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'datia_state_1626_1950'}) SET c += {colony_id: 'datia_state_1626_1950', name: 'Datia State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1172600', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1626, independence_year: 1950, latitude: 25.68333333, longitude: 78.46666667, capital: 'Datia', population: 53759};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dawa_state'}) SET c += {colony_id: 'dawa_state', name: 'Dawa State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11916720', source: 'wikidata_sparql_Q1336152', latitude: 21.18333333, longitude: 80.21666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dedhrota'}) SET c += {colony_id: 'dedhrota', name: 'Dedhrota', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q131126101', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dedhrota_1900_1947'}) SET c += {colony_id: 'dedhrota_1900_1947', name: 'Dedhrota', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11916768', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1900, independence_year: 1947};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'deloli_state'}) SET c += {colony_id: 'deloli_state', name: 'Deloli State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21076401', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'deogarh'}) SET c += {colony_id: 'deogarh', name: 'Deogarh', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11916911', source: 'wikidata_sparql_Q1336152', latitude: 25.53333333, longitude: 73.91666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'derbhavti_state'}) SET c += {colony_id: 'derbhavti_state', name: 'Derbhavti State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11916930', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'derol'}) SET c += {colony_id: 'derol', name: 'Derol', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11916942', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dewas_state_1728_1948'}) SET c += {colony_id: 'dewas_state_1728_1948', name: 'Dewas State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1207105', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1728, independence_year: 1948, latitude: 22.96, longitude: 76.06, capital: 'Dewas'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dhadi'}) SET c += {colony_id: 'dhadi', name: 'Dhadi', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17600192', source: 'wikidata_sparql_Q1336152', latitude: 31.1333, longitude: 77.8};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dhami_state_1815_1948'}) SET c += {colony_id: 'dhami_state_1815_1948', name: 'Dhami (state)', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3025690', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1815, independence_year: 1948, latitude: 31.9765793, longitude: 76.0507949};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dhar_state_1728_1947'}) SET c += {colony_id: 'dhar_state_1728_1947', name: 'Dhar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1207561', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1728, independence_year: 1947, latitude: 22.6, longitude: 75.3, capital: 'Dhar'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dharampur_state_1262_1948'}) SET c += {colony_id: 'dharampur_state_1262_1948', name: 'Dharampur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q5269129', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1262, independence_year: 1948, latitude: 20.537, longitude: 73.168, capital: 'Dharampur', population: 102000};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dhenkanal_state_1529_1948'}) SET c += {colony_id: 'dhenkanal_state_1529_1948', name: 'Dhenkanal State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1207641', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1529, independence_year: 1948, latitude: 20.6625, longitude: 85.63777778};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dholpur_state_1806_1948'}) SET c += {colony_id: 'dholpur_state_1806_1948', name: 'Dholpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q657861', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1806, independence_year: 1948, latitude: 26.7, longitude: 77.9, capital: 'Dholpur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dhrangadhra_state_1742_1948'}) SET c += {colony_id: 'dhrangadhra_state_1742_1948', name: 'Dhrangadhra State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q16829581', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1742, independence_year: 1948, latitude: 22.98, longitude: 71.47, capital: 'Dhrangadhra', population: 100000};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dhrol_state_1595_1948'}) SET c += {colony_id: 'dhrol_state_1595_1948', name: 'Dhrol State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18111824', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1595, independence_year: 1948, latitude: 22.5689, longitude: 70.4125};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dhurwai_1690_1950'}) SET c += {colony_id: 'dhurwai_1690_1950', name: 'Dhurwai', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11917045', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1690, independence_year: 1950, latitude: 25.31666667, longitude: 79.05};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dir_state_1900_1969'}) SET c += {colony_id: 'dir_state_1900_1969', name: 'Dir State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3243592', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1900, independence_year: 1969, capital: 'Dir'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dodka'}) SET c += {colony_id: 'dodka', name: 'Dodka', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11917542', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dumraon_raj'}) SET c += {colony_id: 'dumraon_raj', name: 'Dumraon Raj', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21076409', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'dungarpur_state_1197_1947'}) SET c += {colony_id: 'dungarpur_state_1197_1947', name: 'Dungarpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q973433', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1197, independence_year: 1947, latitude: 23.83, longitude: 73.72, capital: 'Dungarpur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'faridkot_state_1803_1947'}) SET c += {colony_id: 'faridkot_state_1803_1947', name: 'Faridkot State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1396700', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1803, independence_year: 1947, latitude: 31.116666666, longitude: 77.633333333, capital: 'Faridkot', population: 97034};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'farrukhabad'}) SET c += {colony_id: 'farrukhabad', name: 'Farrukhabad', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11921599', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'gadvi_state'}) SET c += {colony_id: 'gadvi_state', name: 'Gadvi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075179', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'gadwal_samsthanam'}) SET c += {colony_id: 'gadwal_samsthanam', name: 'Gadwal Samsthanam', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11923490', source: 'wikidata_sparql_Q1336152', latitude: 16.23333333, longitude: 77.21666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'gangpur_state_1821_1948'}) SET c += {colony_id: 'gangpur_state_1821_1948', name: 'Gangpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q16838406', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1821, independence_year: 1948, latitude: 22.12, longitude: 84.03};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'garh_state'}) SET c += {colony_id: 'garh_state', name: 'Garh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11923790', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'garhwal_kingdom_1358_1949'}) SET c += {colony_id: 'garhwal_kingdom_1358_1949', name: 'Garhwal Kingdom', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1381495', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1358, independence_year: 1949, latitude: 30.38, longitude: 78.48};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'gaurihar_state_1807_1950'}) SET c += {colony_id: 'gaurihar_state_1807_1950', name: 'Gaurihar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11923882', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1807, independence_year: 1950, latitude: 25.2956, longitude: 80.1747};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'gharra_state'}) SET c += {colony_id: 'gharra_state', name: 'Gharra State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11924173', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ghodasar'}) SET c += {colony_id: 'ghodasar', name: 'Ghodasar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11924185', source: 'wikidata_sparql_Q1336152', latitude: 23.46666667, longitude: 73.33333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'gond_umri'}) SET c += {colony_id: 'gond_umri', name: 'Gond-Umri', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11924463', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'gondal_state_1634_1949'}) SET c += {colony_id: 'gondal_state_1634_1949', name: 'Gondal State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q16839606', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1634, independence_year: 1949, latitude: 21.97, longitude: 70.8, capital: 'Gondal', population: 205840};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'guler_state_1415_1813'}) SET c += {colony_id: 'guler_state_1415_1813', name: 'Guler State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17311418', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1415, independence_year: 1813, latitude: 32.0, longitude: 76.16};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'gwalior_state_1761_1948'}) SET c += {colony_id: 'gwalior_state_1761_1948', name: 'Gwalior State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1557792', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1761, independence_year: 1948, latitude: 26.22, longitude: 78.17, capital: 'Ujjain'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'hapa_state'}) SET c += {colony_id: 'hapa_state', name: 'Hapa State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11925218', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'hasht_bhaiya_1690_1948'}) SET c += {colony_id: 'hasht_bhaiya_1690_1948', name: 'Hasht-Bhaiya', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17297442', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1690, independence_year: 1948, latitude: 25.5, longitude: 79.0};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'hindol_state_1554_1948'}) SET c += {colony_id: 'hindol_state_1554_1948', name: 'Hindol State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11925661', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1554, independence_year: 1948, latitude: 20.36, longitude: 85.2};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'hunza_state_1600_1974'}) SET c += {colony_id: 'hunza_state_1600_1974', name: 'Hunza State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q14957246', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1600, independence_year: 1974, latitude: 36.333, longitude: 74.666, capital: 'Karimabad'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'hyderabad_state_1724_1948'}) SET c += {colony_id: 'hyderabad_state_1724_1948', name: 'Hyderabad State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1240096', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1724, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'icha'}) SET c += {colony_id: 'icha', name: 'Icha', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11926391', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'idar_state_1257_1948'}) SET c += {colony_id: 'idar_state_1257_1948', name: 'Idar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q649310', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1257, independence_year: 1948, latitude: 23.83, longitude: 73.0};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'indore_state_1732_1948'}) SET c += {colony_id: 'indore_state_1732_1948', name: 'Indore State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q716890', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1732, independence_year: 1948, latitude: 22.7252, longitude: 75.8655, capital: 'Indore'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'itwad_state'}) SET c += {colony_id: 'itwad_state', name: 'Itwad State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11926997', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jafarabad_state_1650_1948'}) SET c += {colony_id: 'jafarabad_state_1650_1948', name: 'Jafarabad State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q16849282', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1650, independence_year: 1948, latitude: 20.8667, longitude: 71.3667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jaipur_state_1727_1949'}) SET c += {colony_id: 'jaipur_state_1727_1949', name: 'Jaipur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6124144', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1727, independence_year: 1949};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jaisalmer_state_1156_1947'}) SET c += {colony_id: 'jaisalmer_state_1156_1947', name: 'Jaisalmer State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1678784', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1156, independence_year: 1947, latitude: 26.92, longitude: 70.9, capital: 'Jaisalmer', population: 76255};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jaitpur_state_1731_1849'}) SET c += {colony_id: 'jaitpur_state_1731_1849', name: 'Jaitpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1678787', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1731, independence_year: 1849, latitude: 25.25972222, longitude: 79.60694444};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jalaun_state_1806_1840'}) SET c += {colony_id: 'jalaun_state_1806_1840', name: 'Jalaun State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18126183', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1806, independence_year: 1840, latitude: 26.15, longitude: 79.35};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jambughoda_state_1400_1948'}) SET c += {colony_id: 'jambughoda_state_1400_1948', name: 'Jambughoda State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11927151', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1400, independence_year: 1948, latitude: 22.3667, longitude: 73.7167};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jamkhandi_state_1811_1948'}) SET c += {colony_id: 'jamkhandi_state_1811_1948', name: 'Jamkhandi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1681450', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1811, independence_year: 1948, latitude: 16.5167, longitude: 75.3};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jammu_and_kashmir_1846_1947'}) SET c += {colony_id: 'jammu_and_kashmir_1846_1947', name: 'Jammu and Kashmir', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2571484', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1846, independence_year: 1947, latitude: 32.733333333, longitude: 74.85, capital: 'Srinagar'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jandol_state_1830_1948'}) SET c += {colony_id: 'jandol_state_1830_1948', name: 'Jandol State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q28172756', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1830, independence_year: 1948, capital: 'Samar Bagh'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'janjira_state_1489_1948'}) SET c += {colony_id: 'janjira_state_1489_1948', name: 'Janjira State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18126222', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1489, independence_year: 1948, latitude: 18.3, longitude: 73.0, capital: 'Murud-Janjira', population: 110389};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jaoli_state_1700_1700'}) SET c += {colony_id: 'jaoli_state_1700_1700', name: 'Jaoli State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6156427', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1700, independence_year: 1700, latitude: 17.99, longitude: 74.42};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jaora_state_1817_1948'}) SET c += {colony_id: 'jaora_state_1817_1948', name: 'Jaora State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1683106', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1817, independence_year: 1948, latitude: 23.63, longitude: 75.13, capital: 'Jaora', population: 84202};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jasdan_state_1665_1948'}) SET c += {colony_id: 'jasdan_state_1665_1948', name: 'Jasdan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1683756', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1665, independence_year: 1948, latitude: 22.03, longitude: 71.2};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jashpur_state_1800_1948'}) SET c += {colony_id: 'jashpur_state_1800_1948', name: 'Jashpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1683780', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1800, independence_year: 1948, latitude: 22.9, longitude: 84.15};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jaso_state_1732_1948'}) SET c += {colony_id: 'jaso_state_1732_1948', name: 'Jaso State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11927206', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1732, independence_year: 1948, latitude: 24.5, longitude: 80.5};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jasrota_1020_1820'}) SET c += {colony_id: 'jasrota_1020_1820', name: 'Jasrota', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104151575', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1020, independence_year: 1820, latitude: 32.48, longitude: 75.44, capital: 'Jasrota'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jaswan_1170_1849'}) SET c += {colony_id: 'jaswan_1170_1849', name: 'Jaswan', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6164350', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1170, independence_year: 1849, latitude: 30.484, longitude: 76.594};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jath_state_1642_1948'}) SET c += {colony_id: 'jath_state_1642_1948', name: 'Jath State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q933413', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1642, independence_year: 1948, latitude: 17.05, longitude: 75.26666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jawhar_state_1343_1947'}) SET c += {colony_id: 'jawhar_state_1343_1947', name: 'Jawhar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11927430', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1343, independence_year: 1947, latitude: 19.93333333, longitude: 73.26666667, capital: 'Jawhar', population: 47538};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jesar_state'}) SET c += {colony_id: 'jesar_state', name: 'Jesar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q65063637', source: 'wikidata_sparql_Q1336152', capital: 'Jesar'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jhabua_state_1584_1948'}) SET c += {colony_id: 'jhabua_state_1584_1948', name: 'Jhabua State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1688822', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1584, independence_year: 1948, latitude: 22.77, longitude: 74.6, population: 80889};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jhalawan_state_1955'}) SET c += {colony_id: 'jhalawan_state_1955', name: 'Jhalawan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6190797', source: 'wikidata_sparql_Q1336152', independence_year: 1955, latitude: 27.8, longitude: 66.6};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jhalawar_state_1838_1949'}) SET c += {colony_id: 'jhalawar_state_1838_1949', name: 'Jhalawar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1261339', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1838, independence_year: 1949, latitude: 24.59, longitude: 76.16, capital: 'Jhalawar', population: 90175};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jhansi_state_1804_1853'}) SET c += {colony_id: 'jhansi_state_1804_1853', name: 'Jhansi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11927544', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1804, independence_year: 1853, latitude: 25.458055555, longitude: 78.575555555};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jhari_gharkhadi_state'}) SET c += {colony_id: 'jhari_gharkhadi_state', name: 'Jhari Gharkhadi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11927468', source: 'wikidata_sparql_Q1336152', latitude: 20.8, longitude: 73.88};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jigni_state_1730_1950'}) SET c += {colony_id: 'jigni_state_1730_1950', name: 'Jigni State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11927549', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1730, independence_year: 1950, latitude: 25.75, longitude: 79.41666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jind_state_1763_1948'}) SET c += {colony_id: 'jind_state_1763_1948', name: 'Jind State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1252744', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1763, independence_year: 1948, latitude: 31.1167, longitude: 77.6333, capital: 'Sangrur', population: 324676};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jiral_1870'}) SET c += {colony_id: 'jiral_1870', name: 'Jiral', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11927559', source: 'wikidata_sparql_Q1336152', independence_year: 1870};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jobat_state_1500_1948'}) SET c += {colony_id: 'jobat_state_1500_1948', name: 'Jobat State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6206774', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1500, independence_year: 1948, latitude: 22.42, longitude: 74.57};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jodhpur_state_1226_1949'}) SET c += {colony_id: 'jodhpur_state_1226_1949', name: 'Jodhpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6207845', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1226, independence_year: 1949};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'jubbal_state_1815_1948'}) SET c += {colony_id: 'jubbal_state_1815_1948', name: 'Jubbal State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3187887', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1815, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'junagadh_state_1748_1948'}) SET c += {colony_id: 'junagadh_state_1748_1948', name: 'Junagadh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q14491604', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1748, independence_year: 1948, latitude: 21.52, longitude: 70.47, capital: 'Junagadh', population: 465493};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kahlur_state_697_1948'}) SET c += {colony_id: 'kahlur_state_697_1948', name: 'Kahlur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q860407', source: 'wikidata_sparql_Q1336152', dynasty_founded: 697, independence_year: 1948, latitude: 31.31666667, longitude: 76.83333333, capital: 'Bilaspur, Himachal Pradesh'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kalahandi_state_1005_1948'}) SET c += {colony_id: 'kalahandi_state_1005_1948', name: 'Kalahandi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1535236', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1005, independence_year: 1948, latitude: 20.083, longitude: 83.2, capital: 'Bhawanipatna', population: 224548};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kalakankar'}) SET c += {colony_id: 'kalakankar', name: 'Kalakankar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17607099', source: 'wikidata_sparql_Q1336152', latitude: 25.8, longitude: 81.366667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kalsia_state_1760_1948'}) SET c += {colony_id: 'kalsia_state_1760_1948', name: 'Kalsia State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q932359', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1760, independence_year: 1948, latitude: 30.25, longitude: 77.37};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kamta_rajaula_1812_1948'}) SET c += {colony_id: 'kamta_rajaula_1812_1948', name: 'Kamta-Rajaula', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11929623', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1812, independence_year: 1948, latitude: 25.18333333, longitude: 80.85};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kangra_lambagraon_1400_1948'}) SET c += {colony_id: 'kangra_lambagraon_1400_1948', name: 'Kangra-Lambagraon', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3192661', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1400, independence_year: 1948, latitude: 32.1, longitude: 76.2667, population: 1625000};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kanjarda'}) SET c += {colony_id: 'kanjarda', name: 'Kanjarda', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11929630', source: 'wikidata_sparql_Q1336152', latitude: 21.77027778, longitude: 72.14305556};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kanker_state_200_1947'}) SET c += {colony_id: 'kanker_state_200_1947', name: 'Kanker State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q12816977', source: 'wikidata_sparql_Q1336152', dynasty_founded: 200, independence_year: 1947, latitude: 20.26666667, longitude: 81.48333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kapshi_estate_1750_1956'}) SET c += {colony_id: 'kapshi_estate_1750_1956', name: 'Kapshi Estate', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11929645', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1750, independence_year: 1956, latitude: 16.334167, longitude: 74.286111};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kapurthala_state_1772_1947'}) SET c += {colony_id: 'kapurthala_state_1772_1947', name: 'Kapurthala State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1728782', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1772, independence_year: 1947, latitude: 31.3833, longitude: 75.3833, capital: 'Kapurthala', population: 314341};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'karauli_state_1348_1948'}) SET c += {colony_id: 'karauli_state_1348_1948', name: 'Karauli State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6368814', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1348, independence_year: 1948, latitude: 26.3, longitude: 77.23, capital: 'Karauli'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kari_state'}) SET c += {colony_id: 'kari_state', name: 'Kari State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21099425', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kawardha_state_1751_1948'}) SET c += {colony_id: 'kawardha_state_1751_1948', name: 'Kawardha State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18126687', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1751, independence_year: 1948, latitude: 22.02, longitude: 81.25};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'keonjhar_state_1200_1948'}) SET c += {colony_id: 'keonjhar_state_1200_1948', name: 'Keonjhar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q19792051', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1200, independence_year: 1948, latitude: 21.63333333, longitude: 81.6};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'keonthal_state_1800_1948'}) SET c += {colony_id: 'keonthal_state_1800_1948', name: 'Keonthal State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3195357', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1800, independence_year: 1948, latitude: 31.0333, longitude: 77.3};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kesaria'}) SET c += {colony_id: 'kesaria', name: 'Kesaria', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17607189', source: 'wikidata_sparql_Q1336152', latitude: 22.866667, longitude: 71.833333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'khairagarh_state_1833_1948'}) SET c += {colony_id: 'khairagarh_state_1833_1948', name: 'Khairagarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11929746', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1833, independence_year: 1948, latitude: 21.42, longitude: 80.97};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'khairpur_state_1775_1955'}) SET c += {colony_id: 'khairpur_state_1775_1955', name: 'Khairpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3249587', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1775, independence_year: 1955, latitude: 27.31666667, longitude: 68.46666667, capital: 'Khairpur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'khanate_of_kalat_1638_1955'}) SET c += {colony_id: 'khanate_of_kalat_1638_1955', name: 'Khanate of Kalat', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q139948', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1638, independence_year: 1955, latitude: 29.02583333, longitude: 66.59, capital: 'Kalat'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'khandpara_state_1599_1948'}) SET c += {colony_id: 'khandpara_state_1599_1948', name: 'Khandpara State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11929762', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1599, independence_year: 1948, latitude: 20.26388889, longitude: 85.21416667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'khaniadhana_state_1724_1948'}) SET c += {colony_id: 'khaniadhana_state_1724_1948', name: 'Khaniadhana State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q16852121', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1724, independence_year: 1948, latitude: 25.025, longitude: 78.1917};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'khaniyadhana'}) SET c += {colony_id: 'khaniyadhana', name: 'Khaniyadhana', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2120351', source: 'wikidata_sparql_Q1336152', latitude: 25.01, longitude: 78.07};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kharagpur_state'}) SET c += {colony_id: 'kharagpur_state', name: 'Kharagpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11929766', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kharan_state_1697_1955'}) SET c += {colony_id: 'kharan_state_1697_1955', name: 'Kharan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2989491', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1697, independence_year: 1955, capital: 'Kharan'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kharsawan_state_1650_1948'}) SET c += {colony_id: 'kharsawan_state_1650_1948', name: 'Kharsawan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18126780', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1650, independence_year: 1948, latitude: 22.8, longitude: 85.83};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'khilchipur_state_1544_1948'}) SET c += {colony_id: 'khilchipur_state_1544_1948', name: 'Khilchipur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6401617', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1544, independence_year: 1948, latitude: 24.03, longitude: 76.57};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kingdom_of_cochin_1500_1949'}) SET c += {colony_id: 'kingdom_of_cochin_1500_1949', name: 'Kingdom of Cochin', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q150056', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1500, independence_year: 1949, latitude: 9.952777777, longitude: 76.338611111, capital: 'Thrippunithura'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kingdom_of_coorg_1834'}) SET c += {colony_id: 'kingdom_of_coorg_1834', name: 'Kingdom of Coorg', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q19892830', source: 'wikidata_sparql_Q1336152', independence_year: 1834};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kingdom_of_mysore_1399_1950'}) SET c += {colony_id: 'kingdom_of_mysore_1399_1950', name: 'Kingdom of Mysore', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q266923', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1399, independence_year: 1950, latitude: 12.3, longitude: 76.65, capital: 'Mysore'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kingdom_of_sikkim_1642_1975'}) SET c += {colony_id: 'kingdom_of_sikkim_1642_1975', name: 'Kingdom of Sikkim', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3960459', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1642, independence_year: 1975};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kingdom_of_thiruvithamkoor_1729_1949'}) SET c += {colony_id: 'kingdom_of_thiruvithamkoor_1729_1949', name: 'Kingdom of Thiruvithamkoor', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q150058', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1729, independence_year: 1949, latitude: 8.433333333, longitude: 76.916666666, capital: 'Thiruvananthapuram'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kinhi'}) SET c += {colony_id: 'kinhi', name: 'Kinhi', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17607217', source: 'wikidata_sparql_Q1336152', latitude: 21.6167, longitude: 80.4833};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kirli_state'}) SET c += {colony_id: 'kirli_state', name: 'Kirli State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075184', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kirnapur'}) SET c += {colony_id: 'kirnapur', name: 'Kirnapur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11929872', source: 'wikidata_sparql_Q1336152', latitude: 21.65, longitude: 80.36666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kishangarh_state_1611_1947'}) SET c += {colony_id: 'kishangarh_state_1611_1947', name: 'Kishangarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6416549', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1611, independence_year: 1947, latitude: 26.57, longitude: 74.87, capital: 'Kishangarh'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'koela_state'}) SET c += {colony_id: 'koela_state', name: 'Koela State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11929890', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kolhapur_state_1707_1949'}) SET c += {colony_id: 'kolhapur_state_1707_1949', name: 'Kolhapur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q657946', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1707, independence_year: 1949, latitude: 16.683333333, longitude: 74.233333333, capital: 'Kolhapur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'koriya_1600_1948'}) SET c += {colony_id: 'koriya_1600_1948', name: 'Koriya', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1784316', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1600, independence_year: 1948, latitude: 23.7333, longitude: 81.8167};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kota_state_1613_1949'}) SET c += {colony_id: 'kota_state_1613_1949', name: 'Kota State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1785349', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1613, independence_year: 1949, latitude: 25.18, longitude: 75.83, capital: 'Kota', population: 685804};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kotharia_state_rajasthan_1527_2000'}) SET c += {colony_id: 'kotharia_state_rajasthan_1527_2000', name: 'Kotharia State, Rajasthan', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152099', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1527, independence_year: 2000};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kotharia_state_rajkot_1733_2000'}) SET c += {colony_id: 'kotharia_state_rajkot_1733_2000', name: 'Kotharia State, Rajkot', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152100', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1733, independence_year: 2000};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kothi_state_1800_1950'}) SET c += {colony_id: 'kothi_state_1800_1950', name: 'Kothi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q23136942', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1800, independence_year: 1950, latitude: 24.76666667, longitude: 80.76666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kotra_pitha'}) SET c += {colony_id: 'kotra_pitha', name: 'Kotra Pitha', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11929937', source: 'wikidata_sparql_Q1336152', latitude: 21.95, longitude: 71.2};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kulpahar_state_1700_1858'}) SET c += {colony_id: 'kulpahar_state_1700_1858', name: 'Kulpahar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152101', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1700, independence_year: 1858};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kumharsain_state_1500_1947'}) SET c += {colony_id: 'kumharsain_state_1500_1947', name: 'Kumharsain State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152102', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1500, independence_year: 1947};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kurundvad_junior_1733_1948'}) SET c += {colony_id: 'kurundvad_junior_1733_1948', name: 'Kurundvad Junior', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18127026', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1733, independence_year: 1948, latitude: 16.6833, longitude: 74.6333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kurundvad_senior_1733_1948'}) SET c += {colony_id: 'kurundvad_senior_1733_1948', name: 'Kurundvad Senior', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18127028', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1733, independence_year: 1948, latitude: 16.6833, longitude: 74.6333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kurwai_state_1707_1948'}) SET c += {colony_id: 'kurwai_state_1707_1948', name: 'Kurwai State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6447564', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1707, independence_year: 1948, latitude: 24.1172, longitude: 78.0383};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kuthar_1700_1900'}) SET c += {colony_id: 'kuthar_1700_1900', name: 'Kuthar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3200690', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1700, independence_year: 1900, latitude: 30.973042, longitude: 76.96764};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'kutlehar_state_1803_1825'}) SET c += {colony_id: 'kutlehar_state_1803_1825', name: 'Kutlehar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6448442', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1803, independence_year: 1825, latitude: 31.611667, longitude: 76.112222};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'laira_state'}) SET c += {colony_id: 'laira_state', name: 'Laira State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11931111', source: 'wikidata_sparql_Q1336152', latitude: 21.73333333, longitude: 84.28333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'lakhtar_state_1604_1947'}) SET c += {colony_id: 'lakhtar_state_1604_1947', name: 'Lakhtar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11931118', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1604, independence_year: 1947, latitude: 22.85, longitude: 71.83333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'las_bela_state_1742_1955'}) SET c += {colony_id: 'las_bela_state_1742_1955', name: 'Las Bela State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1806438', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1742, independence_year: 1955, latitude: 26.2, longitude: 66.333333, capital: 'Bela'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'lathi_state_1340_1948'}) SET c += {colony_id: 'lathi_state_1340_1948', name: 'Lathi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152103', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1340, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'lawa_thikana_1772_1947'}) SET c += {colony_id: 'lawa_thikana_1772_1947', name: 'Lawa Thikana', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6503547', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1772, independence_year: 1947, latitude: 26.36666667, longitude: 75.55};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'limbda_1780_1948'}) SET c += {colony_id: 'limbda_1780_1948', name: 'Limbda', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075471', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1780, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'limbdi_state_1500_1947'}) SET c += {colony_id: 'limbdi_state_1500_1947', name: 'Limbdi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3241025', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1500, independence_year: 1947, latitude: 22.56666667, longitude: 71.88333333, capital: 'Limbdi', population: 40688};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'lohara_sahaspur'}) SET c += {colony_id: 'lohara_sahaspur', name: 'Lohara Sahaspur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075186', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'loharu_state_1806_1947'}) SET c += {colony_id: 'loharu_state_1806_1947', name: 'Loharu State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3258086', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1806, independence_year: 1947, latitude: 28.45, longitude: 75.82, capital: 'Loharu', population: 15229};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'lunavada'}) SET c += {colony_id: 'lunavada', name: 'Lunavada', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2240915', source: 'wikidata_sparql_Q1336152', latitude: 23.133333333, longitude: 73.616666666};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'lunavada_state_1434_1948'}) SET c += {colony_id: 'lunavada_state_1434_1948', name: 'Lunavada State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18127558', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1434, independence_year: 1948, latitude: 23.1333, longitude: 73.65};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'madanpur_state'}) SET c += {colony_id: 'madanpur_state', name: 'Madanpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11934520', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mahlog_state_1768_1948'}) SET c += {colony_id: 'mahlog_state_1768_1948', name: 'Mahlog State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6734208', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1768, independence_year: 1948, latitude: 31.1833, longitude: 76.5667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'maihar_state_1778_1948'}) SET c += {colony_id: 'maihar_state_1778_1948', name: 'Maihar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q999297', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1778, independence_year: 1948, latitude: 24.0, longitude: 80.75};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'makrai_state_1663_1948'}) SET c += {colony_id: 'makrai_state_1663_1948', name: 'Makrai State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18127719', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1663, independence_year: 1948, latitude: 22.0667, longitude: 77.1167};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'makran_1701_1955'}) SET c += {colony_id: 'makran_1701_1955', name: 'Makran', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2989469', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1701, independence_year: 1955, capital: 'Turbat'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'malerkotla_state_1657_1948'}) SET c += {colony_id: 'malerkotla_state_1657_1948', name: 'Malerkotla State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11934705', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1657, independence_year: 1948, latitude: 30.5333, longitude: 75.9833, capital: 'Malerkotla'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'malia_state'}) SET c += {colony_id: 'malia_state', name: 'Malia State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17618884', source: 'wikidata_sparql_Q1336152', latitude: 23.0667, longitude: 70.7667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'malpur_state_1466_1943'}) SET c += {colony_id: 'malpur_state_1466_1943', name: 'Malpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17618911', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1466, independence_year: 1943, latitude: 23.3556, longitude: 73.475};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'manalikkara'}) SET c += {colony_id: 'manalikkara', name: 'Manalikkara', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q16894556', source: 'wikidata_sparql_Q1336152', latitude: 8.285, longitude: 77.31};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'manda_zamindari_1542_1947'}) SET c += {colony_id: 'manda_zamindari_1542_1947', name: 'Manda (zamindari)', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6747689', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1542, independence_year: 1947, latitude: 25.45, longitude: 81.85};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mandholi'}) SET c += {colony_id: 'mandholi', name: 'Mandholi', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11934828', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mandi_state_1290_1948'}) SET c += {colony_id: 'mandi_state_1290_1948', name: 'Mandi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q6748050', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1290, independence_year: 1948, latitude: 31.70694444, longitude: 76.93166667, capital: 'Mandi'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mandwa_state'}) SET c += {colony_id: 'mandwa_state', name: 'Mandwa State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11934840', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mangal_state'}) SET c += {colony_id: 'mangal_state', name: 'Mangal State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3285692', source: 'wikidata_sparql_Q1336152', latitude: 32.24, longitude: 76.08};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'manipur_state_1110_1949'}) SET c += {colony_id: 'manipur_state_1110_1949', name: 'Manipur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q889030', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1110, independence_year: 1949, latitude: 24.8167, longitude: 93.95, capital: 'Imphal'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mansa_state'}) SET c += {colony_id: 'mansa_state', name: 'Mansa State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17619012', source: 'wikidata_sparql_Q1336152', latitude: 23.4333, longitude: 72.7167};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'marwar'}) SET c += {colony_id: 'marwar', name: 'Marwar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1419618', source: 'wikidata_sparql_Q1336152', latitude: 26.3, longitude: 73.0};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'maurha_state_1894_1949'}) SET c += {colony_id: 'maurha_state_1894_1949', name: 'Maurha State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104151601', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1894, independence_year: 1949, capital: 'Maurha'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mayurbhanj_state_1790_1949'}) SET c += {colony_id: 'mayurbhanj_state_1790_1949', name: 'Mayurbhanj State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18127928', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1790, independence_year: 1949, latitude: 21.94, longitude: 86.72};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'miraj_junior_1820_1948'}) SET c += {colony_id: 'miraj_junior_1820_1948', name: 'Miraj Junior', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3315863', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1820, independence_year: 1948, latitude: 16.818672222, longitude: 74.641405555};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'miraj_senior_1820_1948'}) SET c += {colony_id: 'miraj_senior_1820_1948', name: 'Miraj Senior', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q932487', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1820, independence_year: 1948, latitude: 16.83333333, longitude: 74.63333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mohanpur_state_1227_1948'}) SET c += {colony_id: 'mohanpur_state_1227_1948', name: 'Mohanpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11937172', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1227, independence_year: 1948, latitude: 23.45, longitude: 73.06666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mohrampur_jagir_state_1580_1948'}) SET c += {colony_id: 'mohrampur_jagir_state_1580_1948', name: 'Mohrampur Jagir State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152105', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1580, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'morvi_state_1698_1948'}) SET c += {colony_id: 'morvi_state_1698_1948', name: 'Morvi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q922317', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1698, independence_year: 1948, latitude: 22.82, longitude: 70.83, capital: 'Morbi'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mudhol_state_1465_1948'}) SET c += {colony_id: 'mudhol_state_1465_1948', name: 'Mudhol State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1951726', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1465, independence_year: 1948, latitude: 16.33055556, longitude: 75.32222222, capital: 'Mudhol'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'muhammadgarh_state_1853_1947'}) SET c += {colony_id: 'muhammadgarh_state_1853_1947', name: 'Muhammadgarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1951905', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1853, independence_year: 1947, latitude: 23.65, longitude: 78.2};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'muli_state_1470'}) SET c += {colony_id: 'muli_state_1470', name: 'Muli State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11937876', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1470, latitude: 22.63333333, longitude: 71.5};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mundru_state_1621_1818'}) SET c += {colony_id: 'mundru_state_1621_1818', name: 'Mundru State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152106', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1621, independence_year: 1818};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'mursan_state'}) SET c += {colony_id: 'mursan_state', name: 'Mursan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11938026', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nabha_state_1763_1947'}) SET c += {colony_id: 'nabha_state_1763_1947', name: 'Nabha State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q929357', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1763, independence_year: 1947, latitude: 30.37, longitude: 76.15};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nagar_state_1400_1974'}) SET c += {colony_id: 'nagar_state_1400_1974', name: 'Nagar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q372426', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1400, independence_year: 1974, latitude: 35.4, longitude: 73.8, capital: 'Nagarkhas'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nagod_state_1344_1950'}) SET c += {colony_id: 'nagod_state_1344_1950', name: 'Nagod State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1963593', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1344, independence_year: 1950, latitude: 24.57, longitude: 80.6};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nahara_state'}) SET c += {colony_id: 'nahara_state', name: 'Nahara State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q28126531', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'naila_state'}) SET c += {colony_id: 'naila_state', name: 'Naila State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11938347', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nalagarh_1100_1948'}) SET c += {colony_id: 'nalagarh_1100_1948', name: 'Nalagarh', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1682371', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1100, independence_year: 1948, latitude: 31.05, longitude: 76.72};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nandgaon_state_1833_1948'}) SET c += {colony_id: 'nandgaon_state_1833_1948', name: 'Nandgaon State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1964552', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1833, independence_year: 1948, latitude: 21.1, longitude: 81.03};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'narsinghgarh_state_1681_1948'}) SET c += {colony_id: 'narsinghgarh_state_1681_1948', name: 'Narsinghgarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q976913', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1681, independence_year: 1948, latitude: 23.99, longitude: 79.39};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'narsinghpur_state_1292_1948'}) SET c += {colony_id: 'narsinghpur_state_1292_1948', name: 'Narsinghpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q19669126', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1292, independence_year: 1948, latitude: 20.466666666, longitude: 85.116666666};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'narwar_state'}) SET c += {colony_id: 'narwar_state', name: 'Narwar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q19669125', source: 'wikidata_sparql_Q1336152', latitude: 24.983333333, longitude: 76.95};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nasvadi'}) SET c += {colony_id: 'nasvadi', name: 'Nasvadi', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q122955960', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'naugaon'}) SET c += {colony_id: 'naugaon', name: 'Naugaon', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11938469', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nawalpur'}) SET c += {colony_id: 'nawalpur', name: 'Nawalpur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11938484', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nawanagar_state_1540_1948'}) SET c += {colony_id: 'nawanagar_state_1540_1948', name: 'Nawanagar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1545942', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1540, independence_year: 1948, latitude: 22.47, longitude: 70.07};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nayagarh_state_1500_1948'}) SET c += {colony_id: 'nayagarh_state_1500_1948', name: 'Nayagarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q10797411', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1500, independence_year: 1948, latitude: 20.1333, longitude: 85.1};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nazargunj_1899_2000'}) SET c += {colony_id: 'nazargunj_1899_2000', name: 'Nazargunj', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q16932578', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1899, independence_year: 2000};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nilgiri_state_1125_1949'}) SET c += {colony_id: 'nilgiri_state_1125_1949', name: 'Nilgiri State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7037080', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1125, independence_year: 1949, latitude: 23.46, longitude: 86.77};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'nirmali_state'}) SET c += {colony_id: 'nirmali_state', name: 'Nirmali State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11938840', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'orchha_state_1501_1950'}) SET c += {colony_id: 'orchha_state_1501_1950', name: 'Orchha State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q668415', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1501, independence_year: 1950, latitude: 25.35, longitude: 78.64, capital: 'Orchha'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'orissa_tributary_states_1888_1947'}) SET c += {colony_id: 'orissa_tributary_states_1888_1947', name: 'Orissa Tributary States', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q15630982', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1888, independence_year: 1947};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'oudh_state_1732_1859'}) SET c += {colony_id: 'oudh_state_1732_1859', name: 'Oudh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18129046', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1732, independence_year: 1859, latitude: 26.78, longitude: 82.13};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pahra_1812_1948'}) SET c += {colony_id: 'pahra_1812_1948', name: 'Pahra', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11939770', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1812, independence_year: 1948, latitude: 25.1, longitude: 80.8};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pal_lahara_state_1100_1947'}) SET c += {colony_id: 'pal_lahara_state_1100_1947', name: 'Pal Lahara State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7126114', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1100, independence_year: 1947, latitude: 21.45, longitude: 85.1833};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'palali_state'}) SET c += {colony_id: 'palali_state', name: 'Palali State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11939827', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'palanpur_state_1370_1948'}) SET c += {colony_id: 'palanpur_state_1370_1948', name: 'Palanpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7126720', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1370, independence_year: 1948, latitude: 24.17, longitude: 72.43, capital: 'Palanpur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'palasvihir_state'}) SET c += {colony_id: 'palasvihir_state', name: 'Palasvihir State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11939836', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'paldeo_state_1812_1948'}) SET c += {colony_id: 'paldeo_state_1812_1948', name: 'Paldeo State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7127047', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1812, independence_year: 1948, latitude: 25.1, longitude: 80.83333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'palitana_state_1194_1948'}) SET c += {colony_id: 'palitana_state_1194_1948', name: 'Palitana State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7127625', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1194, independence_year: 1948, latitude: 21.516666666, longitude: 71.833333333, capital: 'Palitana'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'paliyad'}) SET c += {colony_id: 'paliyad', name: 'Paliyad', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11939904', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pandaria_state'}) SET c += {colony_id: 'pandaria_state', name: 'Pandaria State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11939961', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'panna_state_1731_1950'}) SET c += {colony_id: 'panna_state_1731_1950', name: 'Panna State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1588594', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1731, independence_year: 1950, latitude: 24.27, longitude: 80.17, capital: 'Panna'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'patan_state_rajasthan_1200_2000'}) SET c += {colony_id: 'patan_state_rajasthan_1200_2000', name: 'Patan State, Rajasthan', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152107', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1200, independence_year: 2000};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pataudi_1804_1947'}) SET c += {colony_id: 'pataudi_1804_1947', name: 'Pataudi', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17991935', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1804, independence_year: 1947, latitude: 28.32, longitude: 76.78, capital: 'Pataudi', population: 21933};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'patdi_state_1741_1947'}) SET c += {colony_id: 'patdi_state_1741_1947', name: 'Patdi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11940483', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1741, independence_year: 1947};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pathari_state_1794_1948'}) SET c += {colony_id: 'pathari_state_1794_1948', name: 'Pathari state', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3428760', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1794, independence_year: 1948, latitude: 23.93333333, longitude: 78.2};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pathari_state_1794_1948'}) SET c += {colony_id: 'pathari_state_1794_1948', name: 'Pathari State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152108', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1794, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'patiala_state_1761_1947'}) SET c += {colony_id: 'patiala_state_1761_1947', name: 'Patiala State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q917553', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1761, independence_year: 1947, latitude: 31.1167, longitude: 77.6333, capital: 'Patiala'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'patna_state_1191_1948'}) SET c += {colony_id: 'patna_state_1191_1948', name: 'Patna State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2056970', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1191, independence_year: 1948, latitude: 20.72, longitude: 83.48};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'payagpur'}) SET c += {colony_id: 'payagpur', name: 'Payagpur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11940634', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'peelwa'}) SET c += {colony_id: 'peelwa', name: 'Peelwa', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11940753', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pethapur_state_1300_1940'}) SET c += {colony_id: 'pethapur_state_1300_1940', name: 'Pethapur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q19605411', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1300, independence_year: 1940, latitude: 23.216666666, longitude: 72.55};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'phaltan_state_1284_1948'}) SET c += {colony_id: 'phaltan_state_1284_1948', name: 'Phaltan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7180358', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1284, independence_year: 1948, latitude: 17.99444444, longitude: 78.68888889};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'phulra_1828_1950'}) SET c += {colony_id: 'phulra_1828_1950', name: 'Phulra', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3246273', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1828, independence_year: 1950};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pimpladevi_state'}) SET c += {colony_id: 'pimpladevi_state', name: 'Pimpladevi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11941639', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pimpri_state'}) SET c += {colony_id: 'pimpri_state', name: 'Pimpri State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q134491987', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'piploda_state_1547_1948'}) SET c += {colony_id: 'piploda_state_1547_1948', name: 'Piploda State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7197455', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1547, independence_year: 1948, latitude: 23.6, longitude: 74.95};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'porbandar_state_1193_1948'}) SET c += {colony_id: 'porbandar_state_1193_1948', name: 'Porbandar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q14552167', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1193, independence_year: 1948, latitude: 21.63, longitude: 69.6, capital: 'Chhaya', population: 115673};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'potegaon'}) SET c += {colony_id: 'potegaon', name: 'Potegaon', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11942517', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pratapgarh_state_1775_1949'}) SET c += {colony_id: 'pratapgarh_state_1775_1949', name: 'Pratapgarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q175934', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1775, independence_year: 1949, latitude: 24.05, longitude: 74.8, capital: 'Pratapgarh', population: 52025};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'prempur'}) SET c += {colony_id: 'prempur', name: 'Prempur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11942666', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'pudukkottai_state_1680_1948'}) SET c += {colony_id: 'pudukkottai_state_1680_1948', name: 'Pudukkottai State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3535371', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1680, independence_year: 1948, latitude: 10.3833, longitude: 78.7833, capital: 'Pudukkottai'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'punadra'}) SET c += {colony_id: 'punadra', name: 'Punadra', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11943892', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q101242542_1825_1924'}) SET c += {colony_id: 'q101242542_1825_1924', name: 'Kadana State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q101242542', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1825, independence_year: 1924, latitude: 23.289591, longitude: 73.838231, capital: 'Kadana'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q104152112_1733_1842'}) SET c += {colony_id: 'q104152112_1733_1842', name: 'Surat State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152112', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1733, independence_year: 1842};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q104152114_1640_1972'}) SET c += {colony_id: 'q104152114_1640_1972', name: 'Yasin State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152114', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1640, independence_year: 1972};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q11904734'}) SET c += {colony_id: 'q11904734', name: 'Alaniawas', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11904734', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q11905355'}) SET c += {colony_id: 'q11905355', name: 'Ammayanayakan', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11905355', source: 'wikidata_sparql_Q1336152', latitude: 10.169662, longitude: 77.895792};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q11905439'}) SET c += {colony_id: 'q11905439', name: 'Anakapalle', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11905439', source: 'wikidata_sparql_Q1336152', latitude: 17.69009, longitude: 82.953007};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q11905698'}) SET c += {colony_id: 'q11905698', name: 'Antarbella', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11905698', source: 'wikidata_sparql_Q1336152', latitude: 22.919684, longitude: 74.648001};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q11908900'}) SET c += {colony_id: 'q11908900', name: 'Bedam', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11908900', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q131080302'}) SET c += {colony_id: 'q131080302', name: 'Sudasana State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q131080302', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q134436280'}) SET c += {colony_id: 'q134436280', name: 'Bilkha', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q134436280', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q1632695_1159_1948'}) SET c += {colony_id: 'q1632695_1159_1948', name: 'Sanjeli State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1632695', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1159, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q21044436'}) SET c += {colony_id: 'q21044436', name: 'Edappalli', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21044436', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q21075438'}) SET c += {colony_id: 'q21075438', name: 'Gopalpet', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075438', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q21075439'}) SET c += {colony_id: 'q21075439', name: 'Kaddatanad', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075439', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q48838868_1759_1948'}) SET c += {colony_id: 'q48838868_1759_1948', name: 'Tharad State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q48838868', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1759, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q48838869_1244_1948'}) SET c += {colony_id: 'q48838869_1244_1948', name: 'Wao State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q48838869', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1244, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q48838872_1948'}) SET c += {colony_id: 'q48838872_1948', name: 'Santalpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q48838872', source: 'wikidata_sparql_Q1336152', independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'q48838989_1755_1950'}) SET c += {colony_id: 'q48838989_1755_1950', name: 'Sarila State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q48838989', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1755, independence_year: 1950};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'radhanpur_state_1787_1948'}) SET c += {colony_id: 'radhanpur_state_1787_1948', name: 'Radhanpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18164260', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1787, independence_year: 1948, latitude: 23.8333, longitude: 71.6};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'raeka'}) SET c += {colony_id: 'raeka', name: 'Raeka', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11944396', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'raghogarh_state_1673_1947'}) SET c += {colony_id: 'raghogarh_state_1673_1947', name: 'Raghogarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11944481', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1673, independence_year: 1947, latitude: 24.43333333, longitude: 77.25};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'raigarh_state_1911_1947'}) SET c += {colony_id: 'raigarh_state_1911_1947', name: 'Raigarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q932393', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1911, independence_year: 1947, latitude: 21.9, longitude: 83.4};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rairakhol_state_1200_1948'}) SET c += {colony_id: 'rairakhol_state_1200_1948', name: 'Rairakhol State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2128542', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1200, independence_year: 1948, latitude: 21.75, longitude: 84.97};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rajgarh_state_1681_1948'}) SET c += {colony_id: 'rajgarh_state_1681_1948', name: 'Rajgarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2128715', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1681, independence_year: 1948, latitude: 24.0333, longitude: 76.8833, capital: 'Rajgarh'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rajkot_state_1620_1948'}) SET c += {colony_id: 'rajkot_state_1620_1948', name: 'Rajkot State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2128743', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1620, independence_year: 1948, latitude: 22.3, longitude: 70.7833, capital: 'Rajkot'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rajoli_zamindari_estate_1775_1948'}) SET c += {colony_id: 'rajoli_zamindari_estate_1775_1948', name: 'Rajoli Zamindari Estate', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7286362', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1775, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rajouli_-400_1947'}) SET c += {colony_id: 'rajouli_-400_1947', name: 'Rajouli', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11944509', source: 'wikidata_sparql_Q1336152', dynasty_founded: -400, independence_year: 1947};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rajpara_state_1811_1949'}) SET c += {colony_id: 'rajpara_state_1811_1949', name: 'Rajpara State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q28179897', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1811, independence_year: 1949};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rajpipla_state_1340_1948'}) SET c += {colony_id: 'rajpipla_state_1340_1948', name: 'Rajpipla State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q918204', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1340, independence_year: 1948, latitude: 21.78, longitude: 73.57, capital: 'Rajpipla', population: 249032};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rajpur_kathiawar'}) SET c += {colony_id: 'rajpur_kathiawar', name: 'Rajpur (Kathiawar)', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075480', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rajpur_state_baroda'}) SET c += {colony_id: 'rajpur_state_baroda', name: 'Rajpur State, Baroda', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152109', source: 'wikidata_sparql_Q1336152', capital: 'Rajpur, Baroda'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ramanka'}) SET c += {colony_id: 'ramanka', name: 'Ramanka', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075481', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ramas_state'}) SET c += {colony_id: 'ramas_state', name: 'Ramas State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11944524', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ramdurg_state_1742_1948'}) SET c += {colony_id: 'ramdurg_state_1742_1948', name: 'Ramdurg State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1776972', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1742, independence_year: 1948, latitude: 15.95, longitude: 75.3};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rampur_state_1719_1949'}) SET c += {colony_id: 'rampur_state_1719_1949', name: 'Rampur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3454186', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1719, independence_year: 1949, latitude: 28.8, longitude: 79.0, capital: 'Rampur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ranasan_state_1700_1943'}) SET c += {colony_id: 'ranasan_state_1700_1943', name: 'Ranasan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11944704', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1700, independence_year: 1943, latitude: 23.35, longitude: 72.95};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'randhia_state'}) SET c += {colony_id: 'randhia_state', name: 'Randhia State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21075482', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ranpur_state_1700_1948'}) SET c += {colony_id: 'ranpur_state_1700_1948', name: 'Ranpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17399594', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1700, independence_year: 1948, latitude: 19.9, longitude: 85.4167};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'ratlam_state_1652_1948'}) SET c += {colony_id: 'ratlam_state_1652_1948', name: 'Ratlam State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1604981', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1652, independence_year: 1948, latitude: 23.32, longitude: 75.07, capital: 'Ratlam', population: 83773};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rewa_state_1755_1947'}) SET c += {colony_id: 'rewa_state_1755_1947', name: 'Rewa State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q176466', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1755, independence_year: 1947, latitude: 24.53, longitude: 81.3, capital: 'Rewa'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'rinsi_state'}) SET c += {colony_id: 'rinsi_state', name: 'Rinsi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11945665', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sachin_state_1791_1948'}) SET c += {colony_id: 'sachin_state_1791_1948', name: 'Sachin State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1476723', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1791, independence_year: 1948, latitude: 21.08, longitude: 72.88, capital: 'Sachin', population: 22107};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sahaspur'}) SET c += {colony_id: 'sahaspur', name: 'Sahaspur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11946624', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sailana_state_1736_1948'}) SET c += {colony_id: 'sailana_state_1736_1948', name: 'Sailana State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1400780', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1736, independence_year: 1948, latitude: 23.47, longitude: 74.92, population: 29723};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sakti_state_1800_1948'}) SET c += {colony_id: 'sakti_state_1800_1948', name: 'Sakti State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7403120', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1800, independence_year: 1948, latitude: 22.03, longitude: 82.97};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sambalpur_district_1493_1848'}) SET c += {colony_id: 'sambalpur_district_1493_1848', name: 'Sambalpur District', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17315177', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1493, independence_year: 1848, latitude: 21.47, longitude: 83.97};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'samla'}) SET c += {colony_id: 'samla', name: 'Samla', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q28179818', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'samthar_state_1760_1950'}) SET c += {colony_id: 'samthar_state_1760_1950', name: 'Samthar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1261743', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1760, independence_year: 1950, latitude: 25.85, longitude: 78.9167, capital: 'Samthar State'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sandur_state_1713_1949'}) SET c += {colony_id: 'sandur_state_1713_1949', name: 'Sandur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q532048', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1713, independence_year: 1949, latitude: 15.1, longitude: 76.55};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sangli_state_1801_1948'}) SET c += {colony_id: 'sangli_state_1801_1948', name: 'Sangli State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2221701', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1801, independence_year: 1948, latitude: 16.867, longitude: 74.567, capital: 'Sangli', population: 137268};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sangri_state_1948'}) SET c += {colony_id: 'sangri_state_1948', name: 'Sangri State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11946883', source: 'wikidata_sparql_Q1336152', independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sant_state_1255_1948'}) SET c += {colony_id: 'sant_state_1255_1948', name: 'Sant State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17198610', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1255, independence_year: 1948, latitude: 23.1895, longitude: 73.8928};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'saraikela_state_1620_1948'}) SET c += {colony_id: 'saraikela_state_1620_1948', name: 'Saraikela State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7422962', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1620, independence_year: 1948, latitude: 22.69777778, longitude: 85.97444444};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sarangarh_state_1948'}) SET c += {colony_id: 'sarangarh_state_1948', name: 'Sarangarh State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1778255', source: 'wikidata_sparql_Q1336152', independence_year: 1948, latitude: 21.6, longitude: 83.08};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sarawan'}) SET c += {colony_id: 'sarawan', name: 'Sarawan', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7423443', source: 'wikidata_sparql_Q1336152', latitude: 29.809166666, longitude: 66.856666666};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sardargarh_bantva_1760_1947'}) SET c += {colony_id: 'sardargarh_bantva_1760_1947', name: 'Sardargarh Bantva', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7423761', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1760, independence_year: 1947, latitude: 25.2333, longitude: 74.0};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sarwan_state'}) SET c += {colony_id: 'sarwan_state', name: 'Sarwan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q21099444', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'satanones'}) SET c += {colony_id: 'satanones', name: 'Satanones', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11947797', source: 'wikidata_sparql_Q1336152', capital: 'Satanones'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'satara_state_1818_1849'}) SET c += {colony_id: 'satara_state_1818_1849', name: 'Satara state', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2225895', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1818, independence_year: 1849, latitude: 17.688423, longitude: 73.99288};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sathamba_1948'}) SET c += {colony_id: 'sathamba_1948', name: 'Sathamba', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11947838', source: 'wikidata_sparql_Q1336152', independence_year: 1948, capital: 'Sathamba', population: 5360};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'savanur_state_1680_1948'}) SET c += {colony_id: 'savanur_state_1680_1948', name: 'Savanur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1607154', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1680, independence_year: 1948, latitude: 14.967, longitude: 75.35};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sawantwadi_state_1627_1948'}) SET c += {colony_id: 'sawantwadi_state_1627_1948', name: 'Sawantwadi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18164343', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1627, independence_year: 1948, latitude: 16.0, longitude: 73.75, capital: 'Sawantwadi taluka', population: 250589};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'shahpur_state'}) SET c += {colony_id: 'shahpur_state', name: 'Shahpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11942806', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'shahpura_state_1629_1949'}) SET c += {colony_id: 'shahpura_state_1629_1949', name: 'Shahpura State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2276431', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1629, independence_year: 1949, latitude: 25.63, longitude: 74.93, capital: 'Shahpura, Bhilwara', population: 54233};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sheikhsar_state'}) SET c += {colony_id: 'sheikhsar_state', name: 'Sheikhsar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q111016259', source: 'wikidata_sparql_Q1336152', latitude: 28.604383333, longitude: 73.979422222, capital: 'Sheikhsar'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'shergarh'}) SET c += {colony_id: 'shergarh', name: 'Shergarh', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11949670', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'shivbara_state'}) SET c += {colony_id: 'shivbara_state', name: 'Shivbara State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11949678', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'siba_state_1450_1849'}) SET c += {colony_id: 'siba_state_1450_1849', name: 'Siba State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11949691', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1450, independence_year: 1849, latitude: 31.9199, longitude: 76.1175};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sihora_state'}) SET c += {colony_id: 'sihora_state', name: 'Sihora State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11949750', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sikar'}) SET c += {colony_id: 'sikar', name: 'Sikar', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104924924', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sirmoor_state_1616_1948'}) SET c += {colony_id: 'sirmoor_state_1616_1948', name: 'Sirmoor State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1541353', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1616, independence_year: 1948, latitude: 30.55, longitude: 77.3, capital: 'Nahan'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sirohi_state_1405_1949'}) SET c += {colony_id: 'sirohi_state_1405_1949', name: 'Sirohi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7530545', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1405, independence_year: 1949, latitude: 24.88333333, longitude: 72.86666667, capital: 'Sirohi', population: 216528};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sirsi'}) SET c += {colony_id: 'sirsi', name: 'Sirsi', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11949891', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sitamau_state_1701_1948'}) SET c += {colony_id: 'sitamau_state_1701_1948', name: 'Sitamau State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2290502', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1701, independence_year: 1948, latitude: 20.02, longitude: 75.35, capital: 'Sitamau', population: 23863};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sohawal_state_1550_1950'}) SET c += {colony_id: 'sohawal_state_1550_1950', name: 'Sohawal State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3488924', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1550, independence_year: 1950, latitude: 24.5703, longitude: 80.7672};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'somna_state_1900_1949'}) SET c += {colony_id: 'somna_state_1900_1949', name: 'Somna State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152111', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1900, independence_year: 1949};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sonepur_state_1556_1948'}) SET c += {colony_id: 'sonepur_state_1556_1948', name: 'Sonepur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1798703', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1556, independence_year: 1948, latitude: 20.83, longitude: 83.92};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'stok_jair_state_1842_1948'}) SET c += {colony_id: 'stok_jair_state_1842_1948', name: 'Stok jair State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152110', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1842, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'suket_state_765_1948'}) SET c += {colony_id: 'suket_state_765_1948', name: 'Suket State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3503368', source: 'wikidata_sparql_Q1336152', dynasty_founded: 765, independence_year: 1948, latitude: 31.53, longitude: 76.88, population: 58408};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'sundem_1555_1935'}) SET c += {colony_id: 'sundem_1555_1935', name: 'Sundem', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11950532', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1555, independence_year: 1935};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'surgana_state_1800_1948'}) SET c += {colony_id: 'surgana_state_1800_1948', name: 'Surgana State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17298275', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1800, independence_year: 1948, latitude: 20.57, longitude: 73.62};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'surguja_state_1613_1948'}) SET c += {colony_id: 'surguja_state_1613_1948', name: 'Surguja State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2368545', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1613, independence_year: 1948, latitude: 23.2, longitude: 83.0333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'swat_state_1849_1955'}) SET c += {colony_id: 'swat_state_1849_1955', name: 'Swat State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3246260', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1849, independence_year: 1955, capital: 'Saidu Sharif'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'talcher_state_1200_1948'}) SET c += {colony_id: 'talcher_state_1200_1948', name: 'Talcher State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17244162', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1200, independence_year: 1948, latitude: 20.95, longitude: 85.216667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'taraon_state_1812_1948'}) SET c += {colony_id: 'taraon_state_1812_1948', name: 'Taraon State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q18008280', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1812, independence_year: 1948, latitude: 24.9833, longitude: 80.95};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'tasgaon_state'}) SET c += {colony_id: 'tasgaon_state', name: 'Tasgaon State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11950935', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'tavi'}) SET c += {colony_id: 'tavi', name: 'Tavi', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11950971', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'thanjavur_maratha_kingdom_1674_1855'}) SET c += {colony_id: 'thanjavur_maratha_kingdom_1674_1855', name: 'Thanjavur Maratha kingdom', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q3530610', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1674, independence_year: 1855, capital: 'Thanjavur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'the_punial_state_1948'}) SET c += {colony_id: 'the_punial_state_1948', name: 'The Punial State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7260195', source: 'wikidata_sparql_Q1336152', independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'theog_state'}) SET c += {colony_id: 'theog_state', name: 'Theog State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11951769', source: 'wikidata_sparql_Q1336152', latitude: 31.1, longitude: 77.43333333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'tigiria_state_1600_1948'}) SET c += {colony_id: 'tigiria_state_1600_1948', name: 'Tigiria State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11951827', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1600, independence_year: 1948, latitude: 20.48333333, longitude: 85.51666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'tonk_state_1817_1949'}) SET c += {colony_id: 'tonk_state_1817_1949', name: 'Tonk State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q914031', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1817, independence_year: 1949, latitude: 26.166666666, longitude: 75.783333333, capital: 'Tonk'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'torawati_1200_2000'}) SET c += {colony_id: 'torawati_1200_2000', name: 'Torawati', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q7825423', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1200, independence_year: 2000};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'tori_fatehpur_1690_1950'}) SET c += {colony_id: 'tori_fatehpur_1690_1950', name: 'Tori Fatehpur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11952191', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1690, independence_year: 1950, latitude: 25.45, longitude: 79.1333};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'tripura_1809_1949'}) SET c += {colony_id: 'tripura_1809_1949', name: 'Tripura', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17342164', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1809, independence_year: 1949, latitude: 23.8333, longitude: 91.2833, capital: 'Agartala', population: 513000};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'tulsipur_state_1600_1859'}) SET c += {colony_id: 'tulsipur_state_1600_1859', name: 'Tulsipur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q5915498', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1600, independence_year: 1859};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'udaipur_state'}) SET c += {colony_id: 'udaipur_state', name: 'Udaipur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q130642141', source: 'wikidata_sparql_Q1336152', capital: 'Udaipur'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'udaipur_state_1818_1948'}) SET c += {colony_id: 'udaipur_state_1818_1948', name: 'Udaipur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1457519', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1818, independence_year: 1948, latitude: 22.47, longitude: 83.22};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'umari_state'}) SET c += {colony_id: 'umari_state', name: 'Umari State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11953931', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'umri_1000_1948'}) SET c += {colony_id: 'umri_1000_1948', name: 'Umri', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11953949', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1000, independence_year: 1948, latitude: 24.75, longitude: 77.31666667};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vadhyawan_state'}) SET c += {colony_id: 'vadhyawan_state', name: 'Vadhyawan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11954165', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vadia_state'}) SET c += {colony_id: 'vadia_state', name: 'Vadia State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11954167', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vakhtapur_1948'}) SET c += {colony_id: 'vakhtapur_1948', name: 'Vakhtapur', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2771763', source: 'wikidata_sparql_Q1336152', independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vallabhi_1740_1948'}) SET c += {colony_id: 'vallabhi_1740_1948', name: 'Vallabhi', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q1534153', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1740, independence_year: 1948, latitude: 21.866667, longitude: 71.95};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vallavpur_state_1434_1949'}) SET c += {colony_id: 'vallavpur_state_1434_1949', name: 'Vallavpur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152104', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1434, independence_year: 1949};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vallbhapur_state_1600_1948'}) SET c += {colony_id: 'vallbhapur_state_1600_1948', name: 'Vallbhapur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152246', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1600, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'varsoda_state_745_1948'}) SET c += {colony_id: 'varsoda_state_745_1948', name: 'Varsoda State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q101242375', source: 'wikidata_sparql_Q1336152', dynasty_founded: 745, independence_year: 1948, capital: 'Varsoda'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vasavad'}) SET c += {colony_id: 'vasavad', name: 'Vasavad', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11954379', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vasurna_state'}) SET c += {colony_id: 'vasurna_state', name: 'Vasurna State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11954387', source: 'wikidata_sparql_Q1336152'};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vijaipur_state_1542_1947'}) SET c += {colony_id: 'vijaipur_state_1542_1947', name: 'Vijaipur State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q104152343', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1542, independence_year: 1947};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'vijaynagar_state_1577_1948'}) SET c += {colony_id: 'vijaynagar_state_1577_1948', name: 'Vijaynagar State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q17267634', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1577, independence_year: 1948, latitude: 23.6, longitude: 72.95};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'virpur_kherdi_state_1600_1948'}) SET c += {colony_id: 'virpur_kherdi_state_1600_1948', name: 'Virpur-Kherdi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q16258513', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1600, independence_year: 1948};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'wadagam_state_1800_1948'}) SET c += {colony_id: 'wadagam_state_1800_1948', name: 'Wadagam State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q11954352', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1800, independence_year: 1948, latitude: 24.0833, longitude: 72.4833};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'wadhwan_state_1630_1948'}) SET c += {colony_id: 'wadhwan_state_1630_1948', name: 'Wadhwan State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q180235', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1630, independence_year: 1948, latitude: 22.42, longitude: 71.41};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'wankaner_state_1807_1947'}) SET c += {colony_id: 'wankaner_state_1807_1947', name: 'Wankaner State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2548416', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1807, independence_year: 1947, latitude: 22.62, longitude: 70.93, capital: 'Wankaner', population: 44259};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'warahi_state_1943'}) SET c += {colony_id: 'warahi_state_1943', name: 'Warahi State', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q2510553', source: 'wikidata_sparql_Q1336152', independence_year: 1943, latitude: 23.78888889, longitude: 71.48888889};
MERGE (c:HistoricalTerritory:PrincelyState {colony_id: 'zainabad_1300_1948'}) SET c += {colony_id: 'zainabad_1300_1948', name: 'Zainabad', colony_type: 'Princely State', region: 'South Asia', wikidata_id: 'Q144395', source: 'wikidata_sparql_Q1336152', dynasty_founded: 1300, independence_year: 1948, latitude: 23.283333333, longitude: 71.766666666};

// ── Princely States Relationships ──
MATCH (a:HistoricalTerritory {colony_id: 'achrol_1600_2000'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'achrol_1600_2000'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ahirwal'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ahirwal'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ajaigarh_state_1765_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ajaigarh_state_1765_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'akkalkot_state_1725_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'akkalkot_state_1725_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'akora_1800_1849'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'akora_1800_1849'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'alampur'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'alampur'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'alipura_state_1757_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'alipura_state_1757_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'alirajpur_state_1437_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'alirajpur_state_1437_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'alwar_state_1770_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'alwar_state_1770_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'amala_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'amala_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'amb_state_1900_1969'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'amb_state_1900_1969'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ambliara_state_1600_1943'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ambliara_state_1600_1943'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'anandpur_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'anandpur_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'angadh_estate_1874_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'angadh_estate_1874_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'anghar'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'anghar'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'athgarh_state_1178_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'athgarh_state_1178_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'athmallik_state_1874_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'athmallik_state_1874_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'aundh_state_1699_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'aundh_state_1699_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'avchar_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'avchar_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'babariawad_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'babariawad_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'badu'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'badu'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baghal_state_1310_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baghal_state_1310_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baghat_state_1600_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baghat_state_1600_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bahawalpur_state_1690_1955'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bahawalpur_state_1690_1955'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bajana_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bajana_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bakhatgarh'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bakhatgarh'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'balasinor_state_1758_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'balasinor_state_1758_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'balladhdarh_state_1710_1867'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'balladhdarh_state_1710_1867'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bamanbore_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bamanbore_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bamra_state_1545_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bamra_state_1545_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'banda_1790_1858'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'banda_1790_1858'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'banganapalle_state_1790_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'banganapalle_state_1790_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bansda_1781_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bansda_1781_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'banswara_state_1497_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'banswara_state_1497_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bantva_manavadar_state_1760_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bantva_manavadar_state_1760_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baoni_state_1784_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baoni_state_1784_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baramba_state_1305_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baramba_state_1305_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baraundha_state_1169_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baraundha_state_1169_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baria_state_1524_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baria_state_1524_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baroda_state_1721_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baroda_state_1721_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'barpali'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'barpali'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'barwala_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'barwala_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'barwani_state_836_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'barwani_state_836_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bashahr_state_1412_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bashahr_state_1412_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'basoda_state_1753_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'basoda_state_1753_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bastar_state_1853_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bastar_state_1853_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baudh_state_1874_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'baudh_state_1874_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bavra_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bavra_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'beja_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'beja_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'benares_state_1770_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'benares_state_1770_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'beri_state_1750_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'beri_state_1750_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhabar_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhabar_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhadli_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhadli_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhadvana_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhadvana_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhaisunda_1812_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhaisunda_1812_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhajji_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhajji_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhalala'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhalala'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhandaria'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhandaria'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bharatpur_state_1680_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bharatpur_state_1680_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bharauli_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bharauli_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bharejda'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bharejda'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhathan_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhathan_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhavnagar_state_1723_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhavnagar_state_1723_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhayavadar'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhayavadar'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhith_bhagwanpur_state_1711_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhith_bhagwanpur_state_1711_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhoika_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhoika_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhojavadar'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhojavadar'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhopal_state_1723_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhopal_state_1723_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhor_state_1697_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhor_state_1697_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhowal_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bhowal_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bihat_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bihat_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bihora_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bihora_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bijawar_state_1765_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bijawar_state_1765_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bikaner_state_1465_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bikaner_state_1465_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bilbari_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bilbari_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bildi_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bildi_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bonai_state_1200_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bonai_state_1200_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bundi_state_1342_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'bundi_state_1342_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cambay_state_1730_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cambay_state_1730_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'carnatic_state_1692_1855'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'carnatic_state_1692_1855'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chamardi_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chamardi_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chamba_state_550_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chamba_state_550_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'changbhakar_1790_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'changbhakar_1790_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'charkhari_state_1765_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'charkhari_state_1765_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chaube_jagirs_1812_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chaube_jagirs_1812_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chhatarpur_state_1785_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chhatarpur_state_1785_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chhota_udaipur_state_1743_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chhota_udaipur_state_1743_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chhuikhadan_state_1750_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chhuikhadan_state_1750_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chinchli_gaded_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chinchli_gaded_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chitral_state_1571_1969'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chitral_state_1571_1969'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chobari_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chobari_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chorangla_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chorangla_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chota_nagpur_states_1821_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chota_nagpur_states_1821_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chotila'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chotila'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chuda_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'chuda_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cooch_behar_1586_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cooch_behar_1586_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cutch_state_1147_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'cutch_state_1147_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dabri_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dabri_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'danta_state_1061_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'danta_state_1061_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'darkoti_1100_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'darkoti_1100_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'daspalla_1498_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'daspalla_1498_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'datarpur_1550_1849'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'datarpur_1550_1849'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'datia_state_1626_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'datia_state_1626_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dawa_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dawa_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dedhrota'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dedhrota'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dedhrota_1900_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dedhrota_1900_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'deloli_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'deloli_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'deogarh'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'deogarh'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'derbhavti_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'derbhavti_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'derol'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'derol'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dewas_state_1728_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dewas_state_1728_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhadi'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhadi'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhami_state_1815_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhami_state_1815_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhar_state_1728_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhar_state_1728_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dharampur_state_1262_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dharampur_state_1262_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhenkanal_state_1529_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhenkanal_state_1529_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dholpur_state_1806_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dholpur_state_1806_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhrangadhra_state_1742_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhrangadhra_state_1742_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhrol_state_1595_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhrol_state_1595_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhurwai_1690_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dhurwai_1690_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dir_state_1900_1969'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dir_state_1900_1969'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dodka'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dodka'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dumraon_raj'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dumraon_raj'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dungarpur_state_1197_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'dungarpur_state_1197_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'faridkot_state_1803_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'faridkot_state_1803_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'farrukhabad'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'farrukhabad'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gadvi_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gadvi_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gadwal_samsthanam'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gadwal_samsthanam'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gangpur_state_1821_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gangpur_state_1821_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'garh_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'garh_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'garhwal_kingdom_1358_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'garhwal_kingdom_1358_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gaurihar_state_1807_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gaurihar_state_1807_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gharra_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gharra_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ghodasar'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ghodasar'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gond_umri'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gond_umri'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gondal_state_1634_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gondal_state_1634_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'guler_state_1415_1813'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'guler_state_1415_1813'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gwalior_state_1761_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'gwalior_state_1761_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hapa_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hapa_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hasht_bhaiya_1690_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hasht_bhaiya_1690_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hindol_state_1554_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hindol_state_1554_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hunza_state_1600_1974'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hunza_state_1600_1974'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hyderabad_state_1724_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'hyderabad_state_1724_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'icha'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'icha'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'idar_state_1257_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'idar_state_1257_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'indore_state_1732_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'indore_state_1732_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'itwad_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'itwad_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jafarabad_state_1650_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jafarabad_state_1650_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaipur_state_1727_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaipur_state_1727_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaisalmer_state_1156_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaisalmer_state_1156_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaitpur_state_1731_1849'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaitpur_state_1731_1849'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jalaun_state_1806_1840'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jalaun_state_1806_1840'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jambughoda_state_1400_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jambughoda_state_1400_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jamkhandi_state_1811_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jamkhandi_state_1811_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jammu_and_kashmir_1846_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jammu_and_kashmir_1846_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jandol_state_1830_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jandol_state_1830_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'janjira_state_1489_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'janjira_state_1489_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaoli_state_1700_1700'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaoli_state_1700_1700'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaora_state_1817_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaora_state_1817_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jasdan_state_1665_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jasdan_state_1665_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jashpur_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jashpur_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaso_state_1732_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaso_state_1732_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jasrota_1020_1820'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jasrota_1020_1820'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaswan_1170_1849'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jaswan_1170_1849'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jath_state_1642_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jath_state_1642_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jawhar_state_1343_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jawhar_state_1343_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jesar_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jesar_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhabua_state_1584_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhabua_state_1584_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhalawan_state_1955'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhalawan_state_1955'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhalawar_state_1838_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhalawar_state_1838_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhansi_state_1804_1853'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhansi_state_1804_1853'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhari_gharkhadi_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jhari_gharkhadi_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jigni_state_1730_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jigni_state_1730_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jind_state_1763_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jind_state_1763_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jiral_1870'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jiral_1870'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jobat_state_1500_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jobat_state_1500_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jodhpur_state_1226_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jodhpur_state_1226_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jubbal_state_1815_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'jubbal_state_1815_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'junagadh_state_1748_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'junagadh_state_1748_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kahlur_state_697_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kahlur_state_697_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kalahandi_state_1005_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kalahandi_state_1005_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kalakankar'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kalakankar'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kalsia_state_1760_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kalsia_state_1760_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kamta_rajaula_1812_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kamta_rajaula_1812_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kangra_lambagraon_1400_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kangra_lambagraon_1400_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kanjarda'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kanjarda'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kanker_state_200_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kanker_state_200_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kapshi_estate_1750_1956'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kapshi_estate_1750_1956'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kapurthala_state_1772_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kapurthala_state_1772_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'karauli_state_1348_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'karauli_state_1348_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kari_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kari_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kawardha_state_1751_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kawardha_state_1751_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'keonjhar_state_1200_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'keonjhar_state_1200_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'keonthal_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'keonthal_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kesaria'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kesaria'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khairagarh_state_1833_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khairagarh_state_1833_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khairpur_state_1775_1955'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khairpur_state_1775_1955'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khanate_of_kalat_1638_1955'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khanate_of_kalat_1638_1955'}), (b:HistoricalTerritory {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khandpara_state_1599_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khandpara_state_1599_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khaniadhana_state_1724_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khaniadhana_state_1724_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khaniyadhana'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khaniyadhana'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kharagpur_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kharagpur_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kharan_state_1697_1955'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kharan_state_1697_1955'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kharsawan_state_1650_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kharsawan_state_1650_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khilchipur_state_1544_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'khilchipur_state_1544_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_cochin_1500_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_cochin_1500_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_coorg_1834'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_coorg_1834'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_mysore_1399_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_mysore_1399_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_sikkim_1642_1975'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_sikkim_1642_1975'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_thiruvithamkoor_1729_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kingdom_of_thiruvithamkoor_1729_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kinhi'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kinhi'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kirli_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kirli_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kirnapur'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kirnapur'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kishangarh_state_1611_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kishangarh_state_1611_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'koela_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'koela_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kolhapur_state_1707_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kolhapur_state_1707_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'koriya_1600_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'koriya_1600_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kota_state_1613_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kota_state_1613_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kotharia_state_rajasthan_1527_2000'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kotharia_state_rajasthan_1527_2000'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kotharia_state_rajkot_1733_2000'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kotharia_state_rajkot_1733_2000'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kothi_state_1800_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kothi_state_1800_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kotra_pitha'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kotra_pitha'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kulpahar_state_1700_1858'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kulpahar_state_1700_1858'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kumharsain_state_1500_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kumharsain_state_1500_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kurundvad_junior_1733_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kurundvad_junior_1733_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kurundvad_senior_1733_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kurundvad_senior_1733_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kurwai_state_1707_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kurwai_state_1707_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kuthar_1700_1900'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kuthar_1700_1900'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kutlehar_state_1803_1825'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'kutlehar_state_1803_1825'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'laira_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'laira_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lakhtar_state_1604_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lakhtar_state_1604_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'las_bela_state_1742_1955'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'las_bela_state_1742_1955'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lathi_state_1340_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lathi_state_1340_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lawa_thikana_1772_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lawa_thikana_1772_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'limbda_1780_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'limbda_1780_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'limbdi_state_1500_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'limbdi_state_1500_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lohara_sahaspur'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lohara_sahaspur'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'loharu_state_1806_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'loharu_state_1806_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lunavada'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lunavada'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lunavada_state_1434_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'lunavada_state_1434_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'madanpur_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'madanpur_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mahlog_state_1768_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mahlog_state_1768_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'maihar_state_1778_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'maihar_state_1778_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'makrai_state_1663_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'makrai_state_1663_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'makran_1701_1955'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'makran_1701_1955'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malerkotla_state_1657_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malerkotla_state_1657_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malia_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malia_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malpur_state_1466_1943'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'malpur_state_1466_1943'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'manalikkara'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'manalikkara'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'manda_zamindari_1542_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'manda_zamindari_1542_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mandholi'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mandholi'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mandi_state_1290_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mandi_state_1290_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mandwa_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mandwa_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mangal_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mangal_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'manipur_state_1110_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'manipur_state_1110_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mansa_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mansa_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'marwar'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'marwar'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'maurha_state_1894_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'maurha_state_1894_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mayurbhanj_state_1790_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mayurbhanj_state_1790_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'miraj_junior_1820_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'miraj_junior_1820_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'miraj_senior_1820_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'miraj_senior_1820_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mohanpur_state_1227_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mohanpur_state_1227_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mohrampur_jagir_state_1580_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mohrampur_jagir_state_1580_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'morvi_state_1698_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'morvi_state_1698_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mudhol_state_1465_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mudhol_state_1465_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'muhammadgarh_state_1853_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'muhammadgarh_state_1853_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'muli_state_1470'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'muli_state_1470'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mundru_state_1621_1818'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mundru_state_1621_1818'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mursan_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'mursan_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nabha_state_1763_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nabha_state_1763_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nagar_state_1400_1974'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nagar_state_1400_1974'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nagod_state_1344_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nagod_state_1344_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nahara_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nahara_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'naila_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'naila_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nalagarh_1100_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nalagarh_1100_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nandgaon_state_1833_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nandgaon_state_1833_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'narsinghgarh_state_1681_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'narsinghgarh_state_1681_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'narsinghpur_state_1292_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'narsinghpur_state_1292_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'narwar_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'narwar_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nasvadi'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nasvadi'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'naugaon'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'naugaon'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nawalpur'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nawalpur'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nawanagar_state_1540_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nawanagar_state_1540_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nayagarh_state_1500_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nayagarh_state_1500_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nazargunj_1899_2000'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nazargunj_1899_2000'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nilgiri_state_1125_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nilgiri_state_1125_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nirmali_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'nirmali_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'orchha_state_1501_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'orchha_state_1501_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'orissa_tributary_states_1888_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'orissa_tributary_states_1888_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'oudh_state_1732_1859'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'oudh_state_1732_1859'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pahra_1812_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pahra_1812_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pal_lahara_state_1100_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pal_lahara_state_1100_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'palali_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'palali_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'palanpur_state_1370_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'palanpur_state_1370_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'palasvihir_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'palasvihir_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'paldeo_state_1812_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'paldeo_state_1812_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'palitana_state_1194_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'palitana_state_1194_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'paliyad'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'paliyad'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pandaria_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pandaria_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'panna_state_1731_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'panna_state_1731_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'patan_state_rajasthan_1200_2000'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'patan_state_rajasthan_1200_2000'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pataudi_1804_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pataudi_1804_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'patdi_state_1741_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'patdi_state_1741_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pathari_state_1794_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pathari_state_1794_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pathari_state_1794_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pathari_state_1794_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'patiala_state_1761_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'patiala_state_1761_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'patna_state_1191_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'patna_state_1191_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'payagpur'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'payagpur'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'peelwa'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'peelwa'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pethapur_state_1300_1940'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pethapur_state_1300_1940'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'phaltan_state_1284_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'phaltan_state_1284_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'phulra_1828_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'phulra_1828_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pimpladevi_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pimpladevi_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pimpri_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pimpri_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'piploda_state_1547_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'piploda_state_1547_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'porbandar_state_1193_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'porbandar_state_1193_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'potegaon'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'potegaon'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pratapgarh_state_1775_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pratapgarh_state_1775_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'prempur'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'prempur'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pudukkottai_state_1680_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'pudukkottai_state_1680_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'punadra'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'punadra'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q101242542_1825_1924'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q101242542_1825_1924'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q104152112_1733_1842'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q104152112_1733_1842'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q104152114_1640_1972'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q104152114_1640_1972'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11904734'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11904734'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11905355'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11905355'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11905439'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11905439'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11905698'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11905698'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11908900'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q11908900'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q131080302'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q131080302'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q134436280'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q134436280'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q1632695_1159_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q1632695_1159_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q21044436'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q21044436'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q21075438'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q21075438'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q21075439'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q21075439'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q48838868_1759_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q48838868_1759_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q48838869_1244_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q48838869_1244_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q48838872_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q48838872_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q48838989_1755_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'q48838989_1755_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'radhanpur_state_1787_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'radhanpur_state_1787_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'raeka'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'raeka'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'raghogarh_state_1673_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'raghogarh_state_1673_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'raigarh_state_1911_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'raigarh_state_1911_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rairakhol_state_1200_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rairakhol_state_1200_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajgarh_state_1681_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajgarh_state_1681_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajkot_state_1620_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajkot_state_1620_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajoli_zamindari_estate_1775_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajoli_zamindari_estate_1775_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajouli_-400_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajouli_-400_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajpara_state_1811_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajpara_state_1811_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajpipla_state_1340_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajpipla_state_1340_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajpur_kathiawar'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajpur_kathiawar'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajpur_state_baroda'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rajpur_state_baroda'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ramanka'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ramanka'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ramas_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ramas_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ramdurg_state_1742_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ramdurg_state_1742_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rampur_state_1719_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rampur_state_1719_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ranasan_state_1700_1943'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ranasan_state_1700_1943'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'randhia_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'randhia_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ranpur_state_1700_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ranpur_state_1700_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ratlam_state_1652_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'ratlam_state_1652_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rewa_state_1755_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rewa_state_1755_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rinsi_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'rinsi_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sachin_state_1791_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sachin_state_1791_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sahaspur'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sahaspur'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sailana_state_1736_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sailana_state_1736_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sakti_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sakti_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sambalpur_district_1493_1848'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sambalpur_district_1493_1848'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'samla'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'samla'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'samthar_state_1760_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'samthar_state_1760_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sandur_state_1713_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sandur_state_1713_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sangli_state_1801_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sangli_state_1801_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sangri_state_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sangri_state_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sant_state_1255_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sant_state_1255_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'saraikela_state_1620_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'saraikela_state_1620_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sarangarh_state_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sarangarh_state_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sarawan'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sarawan'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sardargarh_bantva_1760_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sardargarh_bantva_1760_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sarwan_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sarwan_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'satanones'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'satanones'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'satara_state_1818_1849'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'satara_state_1818_1849'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sathamba_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sathamba_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'savanur_state_1680_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'savanur_state_1680_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sawantwadi_state_1627_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sawantwadi_state_1627_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'shahpur_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'shahpur_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'shahpura_state_1629_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'shahpura_state_1629_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sheikhsar_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sheikhsar_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'shergarh'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'shergarh'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'shivbara_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'shivbara_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'siba_state_1450_1849'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'siba_state_1450_1849'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sihora_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sihora_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sikar'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sikar'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sirmoor_state_1616_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sirmoor_state_1616_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sirohi_state_1405_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sirohi_state_1405_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sirsi'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sirsi'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sitamau_state_1701_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sitamau_state_1701_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sohawal_state_1550_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sohawal_state_1550_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'somna_state_1900_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'somna_state_1900_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sonepur_state_1556_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sonepur_state_1556_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'stok_jair_state_1842_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'stok_jair_state_1842_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'suket_state_765_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'suket_state_765_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sundem_1555_1935'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'sundem_1555_1935'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'surgana_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'surgana_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'surguja_state_1613_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'surguja_state_1613_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'swat_state_1849_1955'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'swat_state_1849_1955'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'talcher_state_1200_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'talcher_state_1200_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'taraon_state_1812_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'taraon_state_1812_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tasgaon_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tasgaon_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tavi'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tavi'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'thanjavur_maratha_kingdom_1674_1855'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'thanjavur_maratha_kingdom_1674_1855'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'the_punial_state_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'the_punial_state_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'theog_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'theog_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tigiria_state_1600_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tigiria_state_1600_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tonk_state_1817_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tonk_state_1817_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'torawati_1200_2000'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'torawati_1200_2000'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tori_fatehpur_1690_1950'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tori_fatehpur_1690_1950'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tripura_1809_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tripura_1809_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tulsipur_state_1600_1859'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'tulsipur_state_1600_1859'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'udaipur_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'udaipur_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'udaipur_state_1818_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'udaipur_state_1818_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'umari_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'umari_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'umri_1000_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'umri_1000_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vadhyawan_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vadhyawan_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vadia_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vadia_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vakhtapur_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vakhtapur_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vallabhi_1740_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vallabhi_1740_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vallavpur_state_1434_1949'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vallavpur_state_1434_1949'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vallbhapur_state_1600_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vallbhapur_state_1600_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'varsoda_state_745_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'varsoda_state_745_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vasavad'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vasavad'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vasurna_state'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vasurna_state'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vijaipur_state_1542_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vijaipur_state_1542_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vijaynagar_state_1577_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'vijaynagar_state_1577_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'virpur_kherdi_state_1600_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'virpur_kherdi_state_1600_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'wadagam_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'wadagam_state_1800_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'wadhwan_state_1630_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'wadhwan_state_1630_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'wankaner_state_1807_1947'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'wankaner_state_1807_1947'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'warahi_state_1943'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'warahi_state_1943'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'zainabad_1300_1948'}), (b:HistoricalTerritory {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:HistoricalTerritory {colony_id: 'zainabad_1300_1948'}), (b:HistoricalTerritory {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);

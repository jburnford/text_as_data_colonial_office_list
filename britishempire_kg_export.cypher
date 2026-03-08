// British Empire Knowledge Graph — Colony nodes and relationships
// Exported from Neo4j on 2026-03-08 11:58
// 
// To import: run this file in Neo4j Browser or cypher-shell

// ── Constraints ──
CREATE CONSTRAINT colony_id_unique IF NOT EXISTS FOR (c:Colony) REQUIRE c.colony_id IS UNIQUE;

// ── Colony Nodes ──

MERGE (c:Colony {colony_id: 'acadia_french_1604_1713'})
SET c += {
  administrative_status: 'Colonial Territory',
  canonical_name: 'Acadia',
  colony_id: 'acadia_french_1604_1713',
  colony_type: 'Colonial Territory',
  comments: 'French colony in Maritime provinces, ceded to Britain 1713. End date: Treaty of Utrecht 1713.',
  coordinates_source: 'wikidata_batch',
  created_date: 1753030225514,
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
  spatial_updated: 1753093187820,
  start_date: '1604-06-26',
  verified: true,
  verified_date: '2025-08-05T20:04:03.412000000+00:00',
  whg_aat_types: ['300387506'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q207353'
};

MERGE (c:Colony {colony_id: 'aden_1839_1963'})
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
  latitude: '12.8',
  longitude: '45.0333',
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

MERGE (c:Colony {colony_id: 'aden_colony_1937_1967'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Aden Colony',
  colony_id: 'aden_colony_1937_1967',
  colony_type: 'Crown Colony',
  comments: 'Strategic port at entrance to Red Sea, key refueling station',
  created_date: 1752963079,
  end_date: '1967-11-30',
  established_year: 1937,
  independence_year: 1967,
  latitude: '12.8',
  longitude: '45.0333',
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

MERGE (c:Colony {colony_id: 'aden_protectorate_1839_1967'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Aden Protectorate',
  colony_id: 'aden_protectorate_1839_1967',
  colony_type: 'Protectorate',
  comments: 'Protected tribal areas around Aden colony',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'ajmer_merwara_1818_1947'})
SET c += {
  canonical_name: 'Ajmer-Merwara',
  colony_id: 'ajmer_merwara_1818_1947',
  established_year: 1818,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Province',
  wikidata_id: 'Q4700553'
};

MERGE (c:Colony {colony_id: 'alberta_1905'})
SET c += {
  canonical_name: 'Alberta',
  colony_id: 'alberta_1905',
  colony_type: 'Province',
  established_year: 1905,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1951'
};

MERGE (c:Colony {colony_id: 'aldabra_islands_1903_1965'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Aldabra Islands',
  colony_id: 'aldabra_islands_1903_1965',
  colony_type: 'Dependency',
  comments: 'Dependency of Seychelles, transferred to BIOT then back to Seychelles',
  created_date: 1752967507,
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

MERGE (c:Colony {colony_id: 'andaman_and_nicobar_islands_1789_1947'})
SET c += {
  canonical_name: 'Andaman and Nicobar Islands',
  colony_id: 'andaman_and_nicobar_islands_1789_1947',
  established_year: 1789,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Province',
  wikidata_id: 'Q40888'
};

MERGE (c:Colony {colony_id: 'anguilla_1650_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Anguilla',
  colony_id: 'anguilla_1650_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Still British Overseas Territory',
  coordinates_source: 'wikidata_batch',
  created_date: 1752962972,
  established_year: 1650,
  latitude: 18.227222222,
  link_status: 'verified',
  longitude: -63.048888888,
  modern_nation_qids: ['Q25228'],
  name: 'Anguilla',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: 1753093187957,
  start_date: '1650-01-01',
  verified: true,
  verified_date: '2025-08-05T20:27:14.710000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q25228'
};

MERGE (c:Colony {colony_id: 'antigua_colony_1632_1981'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Antigua Colony',
  colony_id: 'antigua_colony_1632_1981',
  colony_type: 'Crown Colony',
  comments: 'Part of Leeward Islands federation, sugar plantation economy',
  coordinates_source: 'wikidata_batch',
  created_date: 1753013488,
  end_date: '1981-11-01',
  established_year: 1632,
  independence_year: 1981,
  latitude: '17.085',
  link_status: 'verified',
  longitude: '-61.8',
  modern_nation_qids: ['Q781'],
  name: 'Antigua Colony',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Comprehensive Missing Territories',
  spatial_updated: 1753093188012,
  start_date: '1632-01-01',
  verified: true,
  verified_date: '2025-08-05T20:29:09.886000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q22007334'
};

MERGE (c:Colony {colony_id: 'antigua_montserrat_barbuda_1816_1833'})
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

MERGE (c:Colony {colony_id: 'ascension_island_1815_ongoing'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Ascension Island',
  colony_id: 'ascension_island_1815_ongoing',
  colony_type: 'Dependency',
  comments: 'Dependency of St. Helena, strategic naval station',
  coordinates_source: 'wikidata_batch',
  created_date: 1752967507,
  established_year: 1815,
  latitude: '-7.95',
  link_status: 'verified',
  longitude: '-14.35',
  modern_nation_qids: ['Q192184'],
  name: 'Ascension Island',
  qid_type: 'historical_colony',
  region: 'Africa (Islands)',
  source: 'Indian Ocean Territories',
  spatial_updated: 1753093188099,
  start_date: '1815-10-22',
  verified: true,
  verified_date: '2025-08-05T20:54:32.235000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q46197'
};

MERGE (c:Colony {colony_id: 'ashanti_1901_1957'})
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

MERGE (c:Colony {colony_id: 'assam_bengal_presidency_1826_1874'})
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
  spatial_updated: 1753093188126,
  start_date: '1826-02-24',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-05T22:11:50.906000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5148287'
};

MERGE (c:Colony {colony_id: 'assam_province_1874_1905'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Assam Province (1874-1905)',
  colony_id: 'assam_province_1874_1905',
  colony_type: 'Province',
  comments: 'Assam as a separate Chief Commissioner\'s Province until the 1905 Partition of Bengal.',
  created_date: 1752962006,
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

MERGE (c:Colony {colony_id: 'assam_province_restored_1912_1947'})
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

MERGE (c:Colony {colony_id: 'australia_independent_1942'})
SET c += {
  canonical_name: 'Australia',
  colony_id: 'australia_independent_1942',
  established_year: 1942,
  region: 'Pacific',
  type: 'Independence',
  wikidata_id: 'Q408'
};

MERGE (c:Colony {colony_id: 'bahamas_colony_1666_1973'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Bahamas Colony',
  colony_id: 'bahamas_colony_1666_1973',
  colony_type: 'Crown Colony',
  comments: 'Colonized from Bermuda, piracy and later tourism',
  coordinates_source: 'wikidata_batch',
  created_date: 1752962972,
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
  spatial_updated: 1753093188207,
  start_date: '1666-01-01',
  verified: true,
  verified_date: '2025-08-05T21:15:25.849000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BS'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1060894'
};

MERGE (c:Colony {colony_id: 'bahrain_protectorate_1861_1971'})
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
  spatial_updated: 1753093188232,
  start_date: '1861-05-21',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-05T21:25:42.750000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['BH'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q21816225'
};

MERGE (c:Colony {colony_id: 'baker_island_1855_1898'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Baker Island',
  colony_id: 'baker_island_1855_1898',
  colony_type: 'Guano Island',
  comments: 'Claimed for guano mining, transferred to United States',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'baluchistan_1877_1947'})
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
  spatial_updated: 1753093188280,
  start_date: '1877-01-01',
  transition_type: 'partition',
  verified: true,
  verified_date: '2025-08-05T21:29:19.975000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['PK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2336399'
};

MERGE (c:Colony {colony_id: 'banda_islands_british_occupation_1810_1817'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Banda Islands (British Occupation)',
  colony_id: 'banda_islands_british_occupation_1810_1817',
  colony_type: 'Military Administration',
  comments: 'British occupation of nutmeg islands during Napoleonic Wars',
  created_date: 1752967315,
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

MERGE (c:Colony {colony_id: 'barbados_colony_1627_1966'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Barbados Colony',
  colony_id: 'barbados_colony_1627_1966',
  colony_type: 'Crown Colony',
  comments: 'British colony from 1627 until independence. Served as the headquarters of the British Windward Islands from 1833 to 1885.',
  coordinates_source: 'wikidata_batch',
  created_date: 1752962972,
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
  spatial_updated: 1753093188359,
  start_date: '1627-02-17',
  verified: true,
  verified_date: '2025-08-05T21:47:25.537000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BB'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q63973349'
};

MERGE (c:Colony {colony_id: 'basutoland_1868_1966'})
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

MERGE (c:Colony {colony_id: 'bay_islands_1852_1859'})
SET c += {
  canonical_name: 'Bay Islands',
  colony_id: 'bay_islands_1852_1859',
  established_year: 1852,
  independence_year: 1859,
  region: 'Caribbean',
  type: 'Crown Colony',
  wikidata_id: 'Q1553529'
};

MERGE (c:Colony {colony_id: 'bechuanaland_protectorate_1884_1966'})
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
  spatial_updated: 1753058508810,
  start_date: '1884-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-05T21:48:55.542000000+00:00',
  whg_aat_types: [],
  whg_ccodes: ['BW'],
  whg_fclasses: [],
  wikidata_id: 'Q747314'
};

MERGE (c:Colony {colony_id: 'bencoolen_bengkulu_1685_1824'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Bencoolen (Bengkulu)',
  colony_id: 'bencoolen_bengkulu_1685_1824',
  colony_type: 'Trading Post',
  comments: 'British East India Company settlement in Sumatra, traded to Dutch for Malacca',
  created_date: 1752967315,
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

MERGE (c:Colony {colony_id: 'bengal_presidency_company_1757_1858'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Bengal Presidency (Company)',
  colony_id: 'bengal_presidency_company_1757_1858',
  colony_type: 'Presidency',
  comments: 'Battle of Plassey 1757, included Bengal, Bihar, Orissa, eventually much of northern India',
  created_date: 1752962006,
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

MERGE (c:Colony {colony_id: 'bengal_presidency_crown_1858_1912'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Bengal Presidency (Crown)',
  colony_id: 'bengal_presidency_crown_1858_1912',
  colony_type: 'Presidency',
  comments: 'Direct Crown rule over the Bengal Presidency until its partition in 1905.',
  created_date: 1752962006,
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

MERGE (c:Colony {colony_id: 'bengal_province_partitioned_1905_1912'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Bengal Province (Partitioned)',
  colony_id: 'bengal_province_partitioned_1905_1912',
  colony_type: 'Province',
  comments: 'Western part of Bengal during partition period',
  created_date: 1752962007,
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

MERGE (c:Colony {colony_id: 'bengal_province_reunited_1912_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Bengal Province (Reunited)',
  colony_id: 'bengal_province_reunited_1912_1947',
  colony_type: 'Province',
  comments: 'Bengal reunited 1912, partitioned again 1947 between India (West Bengal) and Pakistan (East Bengal)',
  created_date: 1752962007,
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

MERGE (c:Colony {colony_id: 'berbice_colony_1803_1831'})
SET c += {
  canonical_name: 'Berbice',
  colony_id: 'berbice_colony_1803_1831',
  established_year: 1803,
  independence_year: 1831,
  region: 'South America',
  type: 'Crown Colony',
  wikidata_id: 'Q861922'
};

MERGE (c:Colony {colony_id: 'bermuda_1609_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Bermuda',
  colony_id: 'bermuda_1609_ongoing',
  colony_type: 'Crown Colony',
  comments: 'England\'s oldest remaining overseas territory',
  coordinates_source: 'wikidata_batch',
  created_date: 1753013487,
  established_year: 1609,
  latitude: 32.32,
  longitude: -64.74,
  modern_nation_qids: ['Q23635'],
  name: 'Bermuda',
  region: 'Atlantic',
  source: 'Comprehensive Missing Territories',
  spatial_updated: 1753093188408,
  start_date: '1609-07-28',
  verified: true,
  verified_date: '2025-08-05T23:40:15.150000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q23635'
};

MERGE (c:Colony {colony_id: 'bihar_and_orissa_1912_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Bihar and Orissa',
  colony_id: 'bihar_and_orissa_1912_1947',
  colony_type: 'Province',
  comments: 'Separated from Bengal 1912, Orissa separated as separate province 1936',
  created_date: 1752962007,
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

MERGE (c:Colony {colony_id: 'birnie_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Birnie Island',
  colony_id: 'birnie_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, transferred to Kiribati',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'bombay_presidency_company_1687_1858'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Bombay Presidency (Company)',
  colony_id: 'bombay_presidency_company_1687_1858',
  colony_type: 'Presidency',
  comments: 'Moved from Surat, expanded across western India, included Sind 1843',
  created_date: 1752962006,
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

MERGE (c:Colony {colony_id: 'bombay_presidency_crown_1858_1947'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Bombay Presidency (Crown)',
  colony_id: 'bombay_presidency_crown_1858_1947',
  colony_type: 'Presidency',
  comments: 'Crown rule over western India, Maharashtra, Gujarat, parts of Karnataka',
  created_date: 1752962006,
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

MERGE (c:Colony {colony_id: 'bouvet_island_brief_claim_1825_1928'})
SET c += {
  administrative_status: 'Remote Island',
  canonical_name: 'Bouvet Island (Brief Claim)',
  colony_id: 'bouvet_island_brief_claim_1825_1928',
  colony_type: 'Remote Island',
  comments: 'Remote sub-Antarctic island, claimed before Norwegian annexation',
  coordinates_source: 'wikidata_batch',
  created_date: 1753010772,
  end_date: '1928-01-01',
  established_year: 1825,
  independence_year: 1928,
  latitude: -54.25,
  longitude: -36.75,
  modern_nation_qids: ['Q31747'],
  name: 'Bouvet Island (Brief Claim)',
  region: 'Antarctica',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: 1753093188431,
  start_date: '1825-12-01',
  verified: true,
  verified_date: '2025-08-05T23:47:56.473000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['NO'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q23408'
};

MERGE (c:Colony {colony_id: 'british_bechuanaland_1885_1895'})
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
  spatial_updated: 1753058508823,
  start_date: '1885-01-01',
  transition_type: 'incorporation',
  verified: true,
  verified_date: '2025-08-05T23:48:54.596000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BW'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4530733'
};

MERGE (c:Colony {colony_id: 'british_cameroons_1916_1961'})
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

MERGE (c:Colony {colony_id: 'british_central_africa_protectorate_1891_1907'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'British Central Africa Protectorate',
  colony_id: 'british_central_africa_protectorate_1891_1907',
  colony_type: 'Protectorate',
  comments: 'Renamed to Nyasaland Protectorate 1907',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'british_columbia_province_1871'})
SET c += {
  canonical_name: 'British Columbia',
  colony_id: 'british_columbia_province_1871',
  colony_type: 'Province',
  established_year: 1871,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1974'
};

MERGE (c:Colony {colony_id: 'british_gold_coast_1821_1874'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'British Gold Coast',
  colony_id: 'british_gold_coast_1821_1874',
  colony_type: 'Crown Colony',
  comments: 'Crown administration of coastal trading posts',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'british_guiana_1831_1966'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'British Guiana',
  colony_id: 'british_guiana_1831_1966',
  colony_type: 'Crown Colony',
  comments: 'Formed from Dutch colonies Demerara, Essequibo, Berbice',
  coordinates_source: 'wikidata_batch',
  created_date: 1752962972,
  end_date: '1966-05-26',
  established_year: 1831,
  independence_year: 1966,
  latitude: 5,
  longitude: '-58.75',
  modern_nation_qids: ['Q734'],
  name: 'British Guiana',
  region: 'South America',
  source: 'Caribbean and South American Evolution',
  spatial_updated: 1753093188499,
  start_date: '1831-08-03',
  verified: true,
  verified_date: '2025-08-06T00:11:11.052000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q918126'
};

MERGE (c:Colony {colony_id: 'british_honduras_1862_1981'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'British Honduras',
  colony_id: 'british_honduras_1862_1981',
  colony_type: 'Crown Colony',
  comments: 'Mahogany logging settlement, became crown colony 1862',
  coordinates_source: 'wikidata_batch',
  created_date: 1752962972,
  end_date: '1981-09-21',
  established_year: 1862,
  independence_year: 1981,
  latitude: 54.2,
  longitude: -6.833333,
  modern_nation_qids: ['Q242'],
  name: 'British Honduras',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: 1753093188532,
  start_date: '1862-05-12',
  verified: true,
  verified_date: '2025-08-06T00:19:18.154000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['BZ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1643555'
};

MERGE (c:Colony {colony_id: 'british_new_guinea_1884_1906'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'British New Guinea',
  colony_id: 'british_new_guinea_1884_1906',
  colony_type: 'Protectorate',
  comments: 'British protectorate over southeastern New Guinea',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'british_north_borneo_1882_1946'})
SET c += {
  administrative_status: 'Company Territory',
  canonical_name: 'British North Borneo',
  colony_id: 'british_north_borneo_1882_1946',
  colony_type: 'Company Territory',
  comments: 'British North Borneo Company territory, became Crown Colony 1946',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'british_solomon_islands_1893_1978'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'British Solomon Islands',
  colony_id: 'british_solomon_islands_1893_1978',
  colony_type: 'Protectorate',
  comments: 'Protectorate over chain of Pacific islands',
  coordinates_source: 'wikidata_batch',
  created_date: 1752963189,
  end_date: '1978-07-07',
  established_year: 1893,
  independence_year: 1978,
  latitude: -9.466666666,
  longitude: 159.816666666,
  modern_nation_qids: ['Q685'],
  name: 'British Solomon Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: 1753093188578,
  start_date: '1893-06-28',
  verified: true,
  verified_date: '2025-08-06T02:19:03.301000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SB'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q13410267'
};

MERGE (c:Colony {colony_id: 'british_somaliland_1884_1960'})
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
  spatial_updated: 1753058508836,
  start_date: '1884-01-01',
  transition_type: 'independence_merger',
  verified: true,
  verified_date: '2025-08-06T02:19:35.826000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['SO'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q662653'
};

MERGE (c:Colony {colony_id: 'british_south_africa_company_territory_1889_1923'})
SET c += {
  administrative_status: 'Company Territory',
  canonical_name: 'British South Africa Company Territory',
  colony_id: 'british_south_africa_company_territory_1889_1923',
  colony_type: 'Company Territory',
  comments: 'BSAC administered both Northern and Southern Rhodesia',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'british_togoland_1919_1957'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'British Togoland',
  colony_id: 'british_togoland_1919_1957',
  colony_type: 'Mandate',
  comments: 'British mandate territory, joined Gold Coast in independence',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'british_virgin_islands_1672_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'British Virgin Islands',
  colony_id: 'british_virgin_islands_1672_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Still British Overseas Territory',
  coordinates_source: 'wikidata_batch',
  created_date: 1752962972,
  established_year: 1672,
  latitude: 18.445,
  link_status: 'verified',
  longitude: -64.54,
  modern_nation_qids: ['Q25305'],
  name: 'British Virgin Islands',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: 1753093188591,
  start_date: '1672-01-01',
  verified: true,
  verified_date: '2025-08-06T02:22:43.949000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['VG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q25305'
};

MERGE (c:Colony {colony_id: 'british_western_pacific_territories_1877_1978'})
SET c += {
  administrative_status: 'Administration',
  canonical_name: 'British Western Pacific Territories',
  colony_id: 'british_western_pacific_territories_1877_1978',
  colony_type: 'Administration',
  comments: 'Administrative unit covering multiple Pacific islands',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'british_windward_islands_1833_1959'})
SET c += {
  administrative_status: 'Federal Colony',
  canonical_name: 'British Windward Islands',
  colony_id: 'british_windward_islands_1833_1959',
  colony_type: 'Federal Colony',
  comments: 'Federation of Grenada, St Lucia, St Vincent, Dominica (after 1940)',
  created_date: 1753013488,
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

MERGE (c:Colony {colony_id: 'brunei_protectorate_1888_1984'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Brunei Protectorate',
  colony_id: 'brunei_protectorate_1888_1984',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Sultanate of Brunei',
  coordinates_source: 'wikidata_batch',
  created_date: 1752967217,
  end_date: '1984-01-01',
  established_year: 1888,
  independence_year: 1984,
  latitude: 4.4,
  longitude: 114.566667,
  modern_nation_qids: ['Q921'],
  name: 'Brunei Protectorate',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  spatial_updated: 1753093188619,
  start_date: '1888-09-17',
  verified: true,
  verified_date: '2025-08-06T02:41:24.811000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['BN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q921'
};

MERGE (c:Colony {colony_id: 'burma_british_india_1886_1937'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Burma (British India)',
  colony_id: 'burma_british_india_1886_1937',
  colony_type: 'Province',
  comments: 'Upper Burma added 1886, administered as province of British India until 1937',
  created_date: 1752962007,
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

MERGE (c:Colony {colony_id: 'burma_separate_colony_1937_1948'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Burma (Separate Colony)',
  colony_id: 'burma_separate_colony_1937_1948',
  colony_type: 'Crown Colony',
  comments: 'Separated from British India 1937, became independent Burma 1948',
  coordinates_source: 'wikidata',
  created_date: 1752962007,
  end_date: '1948-01-04',
  established_year: 1937,
  independence_year: 1948,
  latitude: 22.0,
  longitude: 96.0,
  modern_nation_qids: ['Q836'],
  name: 'Burma (Separate Colony)',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  spatial_updated: 1753058508722,
  start_date: '1937-04-01',
  verified: true,
  verified_date: '2025-08-06T02:31:54.454000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2376315'
};

MERGE (c:Colony {colony_id: 'campbell_island_whaling_1810_1860'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'Campbell Island Whaling',
  colony_id: 'campbell_island_whaling_1810_1860',
  colony_type: 'Whaling Station',
  comments: 'Sub-Antarctic whaling and sealing operations',
  coordinates_source: 'wikidata_batch',
  created_date: 1753010772,
  end_date: '1860-12-31',
  established_year: 1810,
  independence_year: 1860,
  latitude: '-52.534215',
  longitude: '169.166525',
  modern_nation_qids: ['Q664'],
  name: 'Campbell Island Whaling',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: 1753093188647,
  start_date: '1810-01-01',
  verified: true,
  verified_date: '2025-08-06T14:09:38.747000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['NZ'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q3593036'
};

MERGE (c:Colony:Dominion {colony_id: 'canada_dominion_of_1867_ongoing'})
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
  spatial_updated: 1753093188673,
  start_date: '1867-01-01',
  transition_type: 'constitutional_monarchy',
  verified: true,
  verified_date: '2025-08-06T14:14:36.062000000+00:00',
  whg_aat_types: ['300387506'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q16'
};

MERGE (c:Colony {colony_id: 'canada_independent_1931'})
SET c += {
  canonical_name: 'Canada',
  colony_id: 'canada_independent_1931',
  established_year: 1931,
  region: 'North America',
  type: 'Independence',
  wikidata_id: 'Q16'
};

MERGE (c:Colony {colony_id: 'cape_breton_colony_1784_1820'})
SET c += {
  colony_id: 'cape_breton_colony_1784_1820',
  established_year: 1784,
  independence_year: 1820,
  name: 'Cape Breton Colony',
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q107457458'
};

MERGE (c:Colony {colony_id: 'cape_coast_castle_1664_1821'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Cape Coast Castle',
  colony_id: 'cape_coast_castle_1664_1821',
  colony_type: 'Trading Post',
  comments: 'Royal African Company headquarters on Gold Coast',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'cape_colony_british_1795_1803_1795_1803'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Cape Colony (British 1795-1803)',
  colony_id: 'cape_colony_british_1795_1803_1795_1803',
  colony_type: 'Crown Colony',
  comments: 'First British occupation during French Revolutionary Wars',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'cape_colony_british_1806_1910'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Cape Colony (British)',
  colony_id: 'cape_colony_british_1806_1910',
  colony_type: 'Crown Colony',
  comments: 'Permanent British control from 1806, confirmed at Congress of Vienna 1815',
  coordinates_source: 'wikidata',
  created_date: 1752962407,
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
  spatial_updated: 1753058508779,
  start_date: '1806-01-10',
  verified: true,
  verified_date: '2025-08-06T14:17:47.512000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q4806993'
};

MERGE (c:Colony {colony_id: 'cape_colony_dutch_1652_1795'})
SET c += {
  administrative_status: 'Dutch Company Colony',
  canonical_name: 'Cape Colony (Dutch)',
  colony_id: 'cape_colony_dutch_1652_1795',
  colony_type: 'Dutch Company Colony',
  comments: 'Dutch East India Company settlement, first European settlement in South Africa',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'cape_colony_dutch_restored_1803_1806'})
SET c += {
  administrative_status: 'Dutch Colony',
  canonical_name: 'Cape Colony (Dutch Restored)',
  colony_id: 'cape_colony_dutch_restored_1803_1806',
  colony_type: 'Dutch Colony',
  comments: 'Brief restoration under Treaty of Amiens',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'caroline_island_1868_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Caroline Island',
  colony_id: 'caroline_island_1868_1979',
  colony_type: 'Guano Island',
  comments: 'Line Islands guano mining, transferred to Kiribati',
  coordinates_source: 'wikidata_batch',
  created_date: 1753010772,
  end_date: '1979-07-12',
  established_year: 1868,
  independence_year: 1979,
  latitude: '-9.955',
  longitude: '-150.2125',
  modern_nation_qids: ['Q710'],
  name: 'Caroline Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: 1753093188685,
  start_date: '1868-01-01',
  verified: true,
  verified_date: '2025-08-06T14:22:03.105000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q822151'
};

MERGE (c:Colony {colony_id: 'cayman_islands_1670_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Cayman Islands',
  colony_id: 'cayman_islands_1670_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Dependency of Jamaica until 1962, still British Overseas Territory',
  coordinates_source: 'wikidata_batch',
  created_date: 1752962972,
  established_year: 1670,
  latitude: 19.5,
  link_status: 'verified',
  longitude: -80.5,
  modern_nation_qids: ['Q5785'],
  name: 'Cayman Islands',
  qid_type: 'historical_colony',
  region: 'Caribbean',
  source: 'Caribbean and South American Evolution',
  spatial_updated: 1753093188698,
  start_date: '1670-01-01',
  verified: true,
  verified_date: '2025-08-06T14:23:35.684000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5785'
};

MERGE (c:Colony {colony_id: 'central_provinces_1861_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Central Provinces',
  colony_id: 'central_provinces_1861_1947',
  colony_type: 'Province',
  comments: 'Created from Nagpur and Saugor territories, became Central Provinces and Berar 1903',
  coordinates_source: 'wikidata',
  created_date: 1752962006,
  end_date: '1947-08-15',
  established_year: 1861,
  independence_year: 1947,
  latitude: '21.15',
  longitude: '79.09',
  modern_nation_qids: ['Q668'],
  name: 'Central Provinces',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  spatial_updated: 1753058508709,
  start_date: '1861-01-01',
  verified: true,
  verified_date: '2025-08-06T14:26:05.071000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q521864'
};

MERGE (c:Colony {colony_id: 'ceylon_1795_1948'})
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
  latitude: '6.916667',
  longitude: '79.833333',
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

MERGE (c:Colony {colony_id: 'chagos_islands_mauritius_dependency_1814_1965'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Chagos Islands (Mauritius Dependency)',
  colony_id: 'chagos_islands_mauritius_dependency_1814_1965',
  colony_type: 'Dependency',
  comments: 'Part of Mauritius until detached to form BIOT',
  created_date: 1752967507,
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

MERGE (c:Colony {colony_id: 'christmas_island_1888_1958'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Christmas Island',
  colony_id: 'christmas_island_1888_1958',
  colony_type: 'Crown Colony',
  comments: 'Phosphate mining, transferred to Australia',
  coordinates_source: 'wikidata_batch',
  created_date: 1752963190,
  end_date: '1958-10-01',
  established_year: 1888,
  independence_year: 1958,
  latitude: -10.49,
  longitude: 105.6275,
  modern_nation_qids: ['Q31063'],
  name: 'Christmas Island',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: 1753093188711,
  start_date: '1888-06-01',
  verified: true,
  verified_date: '2025-08-06T14:28:45.326000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['CX'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q31063'
};

MERGE (c:Colony {colony_id: 'christmas_island_line_islands_1857_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Christmas Island (Line Islands)',
  colony_id: 'christmas_island_line_islands_1857_1979',
  colony_type: 'Guano Island',
  comments: 'Major Line Islands guano deposits, transferred to Kiribati',
  coordinates_source: 'wikidata_batch',
  created_date: 1753010772,
  end_date: '1979-07-12',
  established_year: 1857,
  independence_year: 1979,
  latitude: '1.85',
  longitude: '-157.4',
  modern_nation_qids: ['Q710'],
  name: 'Christmas Island (Line Islands)',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: 1753093188723,
  start_date: '1857-01-01',
  verified: true,
  verified_date: '2025-08-06T14:31:20.411000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q193331'
};

MERGE (c:Colony {colony_id: 'cocos_keeling_islands_1857_1955'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Cocos (Keeling) Islands',
  colony_id: 'cocos_keeling_islands_1857_1955',
  colony_type: 'Crown Colony',
  comments: 'Strategic islands, transferred to Australia',
  coordinates_source: 'wikidata_batch',
  created_date: 1752963190,
  end_date: '1955-11-23',
  established_year: 1857,
  independence_year: 1955,
  latitude: -12.1175,
  longitude: 96.895,
  modern_nation_qids: ['Q36004'],
  name: 'Cocos (Keeling) Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: 1753093188736,
  start_date: '1857-04-01',
  verified: true,
  verified_date: '2025-08-06T14:31:41.388000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['CC'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q36004'
};

MERGE (c:Colony {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'})
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
  spatial_updated: 1753093188749,
  start_date: '1914-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-06T14:32:57.100000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['NG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5148517'
};

MERGE (c:Colony {colony_id: 'colony_of_natal_1843_1910'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Colony of Natal',
  colony_id: 'colony_of_natal_1843_1910',
  colony_type: 'Crown Colony',
  comments: 'Annexed from Natalia Republic, became separate colony 1856',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'colony_of_newfoundland_1610_1949'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Colony of Newfoundland',
  colony_id: 'colony_of_newfoundland_1610_1949',
  colony_type: 'Crown Colony',
  comments: 'Separate British colony until joining Canada 1949',
  coordinates_source: 'wikidata_batch',
  created_date: 1753013487,
  end_date: '1949-03-31',
  established_year: 1610,
  independence_year: 1907,
  latitude: 53,
  longitude: -60,
  modern_nation_qids: ['Q16'],
  name: 'Colony of Newfoundland',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  spatial_updated: 1753093188762,
  start_date: '1610-05-02',
  verified: true,
  verified_date: '2025-08-06T14:36:04.009000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2984260'
};

MERGE (c:Colony:Dominion {colony_id: 'commonwealth_of_australia_1901_ongoing'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Commonwealth of Australia',
  colony_id: 'commonwealth_of_australia_1901_ongoing',
  colony_type: 'Dominion',
  comments: 'Federation of six Australian colonies into Commonwealth',
  coordinates_source: 'wikidata',
  created_date: 1752961788,
  established_year: 1901,
  independence_year: 1942,
  latitude: -25.0,
  longitude: 133.0,
  modern_nation_qids: ['Q408'],
  name: 'Commonwealth of Australia',
  region: 'Pacific',
  source: 'Australian Territorial Evolution',
  spatial_updated: 1753058508651,
  start_date: '1901-01-01',
  verified: true,
  verified_date: '2025-08-06T14:36:45.361000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q408'
};

MERGE (c:Colony {colony_id: 'connecticut_colony_1636_1783'})
SET c += {
  administrative_status: 'Charter Colony',
  canonical_name: 'Connecticut Colony',
  colony_id: 'connecticut_colony_1636_1783',
  colony_type: 'Charter Colony',
  comments: 'Founded by Thomas Hooker, Hartford',
  coordinates_source: 'wikidata_batch',
  created_date: 1753013487,
  end_date: '1783-09-03',
  established_year: 1636,
  independence_year: 1783,
  latitude: 39.828175,
  longitude: -98.5795,
  modern_nation_qids: ['Q30'],
  name: 'Connecticut Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  spatial_updated: 1753093188773,
  start_date: '1636-01-01',
  verified: true,
  verified_date: '2025-08-06T14:38:33.458000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q951500'
};

MERGE (c:Colony {colony_id: 'cook_islands_1888_1901'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Cook Islands',
  colony_id: 'cook_islands_1888_1901',
  colony_type: 'Protectorate',
  comments: 'Transferred to New Zealand administration',
  coordinates_source: 'wikidata_batch',
  created_date: 1752963190,
  end_date: '1901-06-11',
  established_year: 1888,
  independence_year: 1901,
  latitude: -21.233333333,
  longitude: -159.783333333,
  modern_nation_qids: ['Q26988'],
  name: 'Cook Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: 1753093188784,
  start_date: '1888-10-01',
  verified: true,
  verified_date: '2025-08-06T14:38:43.967000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q26988'
};

MERGE (c:Colony {colony_id: 'coorg_province_1834_1947'})
SET c += {
  canonical_name: 'Coorg',
  colony_id: 'coorg_province_1834_1947',
  established_year: 1834,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Province',
  wikidata_id: 'Q864930'
};

MERGE (c:Colony {colony_id: 'corsica_1794_1796'})
SET c += {
  canonical_name: 'Anglo-Corsican Kingdom',
  colony_id: 'corsica_1794_1796',
  established_year: 1794,
  independence_year: 1796,
  region: 'Europe',
  type: 'Protectorate',
  wikidata_id: 'Q2259576'
};

MERGE (c:Colony {colony_id: 'cyprus_1878_1960'})
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
  spatial_updated: 1753093188795,
  start_date: '1878-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-06T14:38:57.612000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['CY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q15240466'
};

MERGE (c:Colony {colony_id: 'deception_island_whaling_1906_1931'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'Deception Island Whaling',
  colony_id: 'deception_island_whaling_1906_1931',
  colony_type: 'Whaling Station',
  comments: 'Major whaling station in Whalers Bay',
  coordinates_source: 'wikidata_batch',
  created_date: 1753010772,
  end_date: '1931-12-31',
  established_year: 1906,
  independence_year: 1931,
  latitude: -54.25,
  longitude: -36.75,
  modern_nation_qids: ['Q35086'],
  name: 'Deception Island Whaling',
  region: 'Antarctica',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: 1753093188806,
  start_date: '1906-01-01',
  verified: true,
  verified_date: '2025-08-06T14:39:36.963000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: [],
  whg_fclasses: ['T'],
  wikidata_id: 'Q1045820'
};

MERGE (c:Colony {colony_id: 'delaware_colony_1664_1783'})
SET c += {
  administrative_status: 'Proprietary Colony',
  canonical_name: 'Delaware Colony',
  colony_id: 'delaware_colony_1664_1783',
  colony_type: 'Proprietary Colony',
  comments: 'Lower counties of Pennsylvania, separate after 1701',
  coordinates_source: 'wikidata_batch',
  created_date: 1753013487,
  end_date: '1783-09-03',
  established_year: 1664,
  independence_year: 1783,
  latitude: 39.828175,
  longitude: -98.5795,
  modern_nation_qids: ['Q30'],
  name: 'Delaware Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  spatial_updated: 1753093188817,
  start_date: '1664-09-08',
  verified: true,
  verified_date: '2025-08-06T14:41:33.138000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2571194'
};

MERGE (c:Colony {colony_id: 'demerara_colony_1803_1831'})
SET c += {
  canonical_name: 'Demerara',
  colony_id: 'demerara_colony_1803_1831',
  established_year: 1803,
  independence_year: 1831,
  region: 'South America',
  type: 'Crown Colony',
  wikidata_id: 'Q2399707'
};

MERGE (c:Colony {colony_id: 'desroches_islands_1903_1965'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Desroches Islands',
  colony_id: 'desroches_islands_1903_1965',
  colony_type: 'Dependency',
  comments: 'Dependency of Seychelles, briefly part of BIOT',
  created_date: 1752967507,
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

MERGE (c:Colony {colony_id: 'dominica_colony_1763_1978'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Dominica Colony',
  colony_id: 'dominica_colony_1763_1978',
  colony_type: 'Crown Colony',
  comments: 'Ceded by France, part of Windward Islands',
  coordinates_source: 'wikidata_batch',
  created_date: 1752962972,
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
  spatial_updated: 1753093188839,
  start_date: '1763-02-10',
  verified: true,
  verified_date: '2025-08-06T14:42:42.630000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['DM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q137394892'
};

MERGE (c:Colony:Dominion {colony_id: 'dominion_of_india_1947_1950'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Dominion of India',
  colony_id: 'dominion_of_india_1947_1950',
  colony_type: 'Dominion',
  comments: 'India at independence, became Republic of India 1950',
  coordinates_source: 'wikidata',
  created_date: 1752962007,
  end_date: '1950-01-26',
  established_year: 1947,
  independence_year: 1950,
  latitude: 22.8,
  longitude: 83.0,
  modern_nation_qids: ['Q668', 'Q843', 'Q902'],
  name: 'Dominion of India',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  spatial_updated: 1753058508735,
  start_date: '1947-08-15',
  verified: true,
  verified_date: '2025-08-06T14:43:01.723000000+00:00',
  whg_aat_types: ['300387346'],
  whg_ccodes: ['IN', 'PK', 'BD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1775277'
};

MERGE (c:Colony {colony_id: 'dominion_of_new_zealand_1907_1947'})
SET c += {
  canonical_name: 'Dominion of New Zealand',
  colony_id: 'dominion_of_new_zealand_1907_1947',
  established_year: 1907,
  independence_year: 1947,
  region: 'Pacific',
  type: 'Dominion',
  wikidata_id: 'Q664'
};

MERGE (c:Colony {colony_id: 'dominion_of_newfoundland_1907_1934'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Dominion of Newfoundland',
  colony_id: 'dominion_of_newfoundland_1907_1934',
  colony_type: 'Dominion',
  comments: 'Self-governing dominion, reverted to Crown colony 1934',
  coordinates_source: 'wikidata_batch',
  created_date: 1753013487,
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
  spatial_updated: 1753093188851,
  start_date: '1907-09-26',
  verified: true,
  verified_date: '2025-08-06T14:43:35.136000000+00:00',
  whg_aat_types: ['300387346'],
  whg_ccodes: ['CA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q38610'
};

MERGE (c:Colony:Dominion {colony_id: 'dominion_of_pakistan_1947_1956'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Dominion of Pakistan',
  colony_id: 'dominion_of_pakistan_1947_1956',
  colony_type: 'Dominion',
  comments: 'Pakistan at independence (West and East), became Islamic Republic 1956',
  coordinates_source: 'wikidata',
  created_date: 1752962007,
  end_date: '1956-03-23',
  established_year: 1947,
  independence_year: 1956,
  latitude: 30.0,
  longitude: 71.0,
  modern_nation_qids: ['Q843'],
  name: 'Dominion of Pakistan',
  region: 'South Asia',
  source: 'British India Territorial Evolution',
  spatial_updated: 1753058508752,
  start_date: '1947-08-15',
  verified: true,
  verified_date: '2025-08-06T14:45:13.897000000+00:00',
  whg_aat_types: ['300387346'],
  whg_ccodes: ['PK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2006542'
};

MERGE (c:Colony {colony_id: 'ducie_island_1902_ongoing'})
SET c += {
  administrative_status: 'Remote Island',
  canonical_name: 'Ducie Island',
  colony_id: 'ducie_island_1902_ongoing',
  colony_type: 'Remote Island',
  comments: 'Part of Pitcairn Islands group, uninhabited coral atoll',
  coordinates_source: 'wikidata_batch',
  created_date: 1753010772,
  established_year: 1902,
  latitude: -25.0677812,
  longitude: -130.1045778,
  modern_nation_qids: ['Q35672'],
  name: 'Ducie Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: 1753093188862,
  start_date: '1902-01-01',
  verified: true,
  verified_date: '2025-08-06T14:45:32.093000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['PN'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q35672'
};

MERGE (c:Colony {colony_id: 'east_africa_protectorate_1895_1920'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'East Africa Protectorate',
  colony_id: 'east_africa_protectorate_1895_1920',
  colony_type: 'Protectorate',
  comments: 'British protectorate after IBEA Company collapse, Uganda separated 1894',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'east_florida_1763_1783'})
SET c += {
  colony_id: 'east_florida_1763_1783',
  established_year: 1763,
  independence_year: 1783,
  name: 'East Florida',
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q1770351'
};

MERGE (c:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Eastern Bengal and Assam',
  colony_id: 'eastern_bengal_and_assam_1905_1912',
  colony_type: 'Province',
  comments: 'Created by partition of Bengal, reunited 1912 due to protests',
  created_date: 1752962007,
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

MERGE (c:Colony {colony_id: 'egypt_1882_1922'})
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
  spatial_updated: 1753093188875,
  start_date: '1882-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-06T14:52:56.382000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['EG'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2474428'
};

MERGE (c:Colony {colony_id: 'ellice_islands_1976_1978'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Ellice Islands',
  colony_id: 'ellice_islands_1976_1978',
  colony_type: 'Crown Colony',
  comments: 'Separated from Gilbert Islands before independence',
  coordinates_source: 'wikidata_batch',
  created_date: 1752963190,
  end_date: '1978-10-01',
  established_year: 1976,
  independence_year: 1978,
  latitude: -7.475,
  longitude: 178.005556,
  modern_nation_qids: ['Q672'],
  name: 'Ellice Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: 1753093188887,
  start_date: '1976-01-01',
  verified: true,
  verified_date: '2025-08-06T14:53:27.293000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['TV'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1050859'
};

MERGE (c:Colony {colony_id: 'ellice_islands_separate_1892_1916'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Ellice Islands (Separate)',
  colony_id: 'ellice_islands_separate_1892_1916',
  colony_type: 'Crown Colony',
  comments: 'Separate protectorate before joining Gilbert and Ellice Islands',
  coordinates_source: 'wikidata_batch',
  created_date: 1752967315,
  end_date: '1916-01-12',
  established_year: 1892,
  independence_year: 1916,
  latitude: -7.475,
  longitude: 178.005556,
  modern_nation_qids: ['Q672'],
  name: 'Ellice Islands (Separate)',
  region: 'Pacific',
  source: 'Additional Southeast Asian Territories',
  spatial_updated: 1753093188900,
  start_date: '1892-01-01',
  verified: true,
  verified_date: '2025-08-06T14:53:39.857000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['TV'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1050859'
};

MERGE (c:Colony {colony_id: 'enderbury_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Enderbury Island',
  colony_id: 'enderbury_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, disputed with USA, transferred to Kiribati',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'essequibo_colony_1803_1831'})
SET c += {
  canonical_name: 'Essequibo',
  colony_id: 'essequibo_colony_1803_1831',
  established_year: 1803,
  independence_year: 1831,
  region: 'South America',
  type: 'Crown Colony',
  wikidata_id: 'Q2199929'
};

MERGE (c:Colony {colony_id: 'factory_at_surat_1612_1857'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Factory at Surat',
  colony_id: 'factory_at_surat_1612_1857',
  colony_type: 'Trading Post',
  comments: 'First English factory in India, EIC headquarters before Bombay',
  coordinates_source: 'wikidata_batch',
  created_date: 1753013488,
  end_date: '1857-05-10',
  established_year: 1612,
  independence_year: 1687,
  latitude: 22.8,
  longitude: 83.0,
  modern_nation_qids: ['Q668'],
  name: 'Factory at Surat',
  region: 'South Asia',
  source: 'Comprehensive Missing Territories',
  spatial_updated: 1753093188912,
  start_date: '1612-01-01',
  verified: true,
  verified_date: '2025-08-06T14:58:59.508000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q19898523'
};

MERGE (c:Colony {colony_id: 'falkland_islands_1833_ongoing'})
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
  spatial_updated: 1753093188923,
  start_date: '1833-01-01',
  transition_type: 'ongoing',
  verified: true,
  verified_date: '2025-08-06T14:59:11.756000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: [],
  whg_fclasses: ['A'],
  wikidata_id: 'Q9648'
};

MERGE (c:Colony {colony_id: 'farquhar_islands_1903_1965'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Farquhar Islands',
  colony_id: 'farquhar_islands_1903_1965',
  colony_type: 'Dependency',
  comments: 'Dependency of Seychelles, briefly part of BIOT',
  created_date: 1752967507,
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

MERGE (c:Colony {colony_id: 'federal_colony_leeward_islands_1833-1960'})
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

MERGE (c:Colony {colony_id: 'federated_malay_states_1895_1946'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Federated Malay States',
  colony_id: 'federated_malay_states_1895_1946',
  colony_type: 'Protectorate',
  comments: 'Federation of Perak, Selangor, Negeri Sembilan, Pahang under British Residents',
  created_date: 1752967216,
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

MERGE (c:Colony:Federation {colony_id: 'federation_of_malaya_1948_1957'})
SET c += {
  administrative_status: 'Federation',
  canonical_name: 'Federation of Malaya',
  colony_id: 'federation_of_malaya_1948_1957',
  colony_type: 'Federation',
  comments: 'Self-governing federation of Malay states',
  coordinates_source: 'wikidata_batch',
  created_date: 1752967217,
  end_date: '1957-08-31',
  established_year: 1948,
  independence_year: 1957,
  latitude: 3.15969444,
  longitude: 101.7,
  modern_nation_qids: ['Q833'],
  name: 'Federation of Malaya',
  region: 'Southeast Asia',
  source: 'Southeast Asian Territorial Evolution',
  spatial_updated: 1753093188935,
  start_date: '1948-02-01',
  verified: true,
  verified_date: '2025-08-06T15:00:39.925000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MY'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1479726'
};

MERGE (c:Colony:Federation {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'})
SET c += {
  administrative_status: 'Federation',
  canonical_name: 'Federation of Rhodesia and Nyasaland',
  colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963',
  colony_type: 'Federation',
  comments: 'Central African Federation of three territories',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'fernando_po_british_1827_1843'})
SET c += {
  administrative_status: 'Possession',
  canonical_name: 'Fernando Po (British)',
  colony_id: 'fernando_po_british_1827_1843',
  colony_type: 'Possession',
  comments: 'Briefly held island, ceded to Spain 1843',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'fiji_1874_1970'})
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
  spatial_updated: 1753093188947,
  start_date: '1874-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-07T02:39:02.101000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['FJ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5148320'
};

MERGE (c:Colony {colony_id: 'flint_island_1866_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Flint Island',
  colony_id: 'flint_island_1866_1979',
  colony_type: 'Guano Island',
  comments: 'Line Islands guano mining, transferred to Kiribati',
  coordinates_source: 'wikidata_batch',
  created_date: 1753010772,
  end_date: '1979-07-12',
  established_year: 1866,
  independence_year: 1979,
  latitude: -7.475,
  longitude: 178.005556,
  modern_nation_qids: ['Q710'],
  name: 'Flint Island',
  region: 'Pacific (Guano/Whaling)',
  source: 'Guano Islands and Whaling Stations',
  spatial_updated: 1753093188959,
  start_date: '1866-01-01',
  verified: true,
  verified_date: '2025-08-07T02:40:30.828000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q741650'
};

MERGE (c:Colony {colony_id: 'fort_william_calcutta_1696_1857'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Fort William (Calcutta)',
  colony_id: 'fort_william_calcutta_1696_1857',
  colony_type: 'Trading Post',
  comments: 'EIC Bengal headquarters, became Bengal Presidency',
  coordinates_source: 'wikidata_batch',
  created_date: 1753013488,
  end_date: '1857-05-10',
  established_year: 1696,
  independence_year: 1757,
  latitude: 22.8,
  longitude: 83.0,
  modern_nation_qids: ['Q668'],
  name: 'Fort William (Calcutta)',
  region: 'South Asia',
  source: 'Comprehensive Missing Territories',
  spatial_updated: 1753093188986,
  start_date: '1696-08-24',
  verified: true,
  verified_date: '2025-08-07T02:48:53.518000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IN'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2750027'
};

MERGE (c:Colony {colony_id: 'gambia_colony_1816_1888'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Gambia Colony',
  colony_id: 'gambia_colony_1816_1888',
  colony_type: 'Crown Colony',
  comments: 'Crown colony before protectorate expansion',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'gambia_colony_and_protectorate_1816_1965'})
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
  spatial_updated: 1753093189011,
  start_date: '1888-02-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-07T02:54:28.415000000+00:00',
  whg_aat_types: ['300387178'],
  whg_ccodes: ['GM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3557236'
};

MERGE (c:Colony {colony_id: 'georgia_colony_1732_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'Georgia Colony',
  colony_id: 'georgia_colony_1732_1783',
  colony_type: 'Royal Colony',
  comments: 'Last of Thirteen Colonies, founded by James Oglethorpe',
  coordinates_source: 'wikidata_batch',
  created_date: 1753013487,
  end_date: '1783-09-03',
  established_year: 1732,
  independence_year: 1783,
  latitude: 39.828175,
  longitude: -98.5795,
  modern_nation_qids: ['Q30'],
  name: 'Georgia Colony',
  region: 'North America',
  source: 'Comprehensive Missing Territories',
  spatial_updated: 1753093189026,
  start_date: '1732-06-09',
  verified: true,
  verified_date: '2025-08-07T02:55:15.182000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['US'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q785035'
};

MERGE (c:Colony {colony_id: 'german_east_africa_british_occupied_1916_1922'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'German East Africa (British Occupied)',
  colony_id: 'german_east_africa_british_occupied_1916_1922',
  colony_type: 'Military Administration',
  comments: 'Former German East Africa under British military administration',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'gibraltar_1704_ongoing'})
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
  spatial_updated: 1753093189059,
  start_date: '1704-01-01',
  transition_type: 'ongoing',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GI'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1410'
};

MERGE (c:Colony {colony_id: 'gilbert_and_ellice_islands_1916_1976'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Gilbert and Ellice Islands',
  colony_id: 'gilbert_and_ellice_islands_1916_1976',
  colony_type: 'Crown Colony',
  comments: 'Combined colony of central Pacific atolls',
  created_date: 1752963189,
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

MERGE (c:Colony {colony_id: 'gilbert_islands_1976_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Gilbert Islands',
  colony_id: 'gilbert_islands_1976_1979',
  colony_type: 'Crown Colony',
  comments: 'Separated from Ellice Islands before independence',
  coordinates_source: 'wikidata_batch',
  created_date: 1752963190,
  end_date: '1979-07-12',
  established_year: 1976,
  independence_year: 1979,
  latitude: 1.466666666,
  longitude: 173.033333333,
  modern_nation_qids: ['Q710'],
  name: 'Gilbert Islands',
  region: 'Pacific',
  source: 'Pacific Territories Evolution',
  spatial_updated: 1753093189072,
  start_date: '1976-01-01',
  verified: false,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['KI'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1050859'
};

MERGE (c:Colony {colony_id: 'gold_coast_colony_1874_1957'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Gold Coast Colony',
  colony_id: 'gold_coast_colony_1874_1957',
  colony_type: 'Crown Colony',
  comments: 'Expanded colony after conquest of Ashanti interior',
  coordinates_source: 'wikidata',
  created_date: 1752962592,
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
  spatial_updated: 1753058508765,
  start_date: '1874-07-24',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GH'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q503623'
};

MERGE (c:Colony {colony_id: 'grenada_colony_1763_1974'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Grenada Colony',
  colony_id: 'grenada_colony_1763_1974',
  colony_type: 'Crown Colony',
  comments: 'Ceded by France, spice island economy',
  coordinates_source: 'wikidata_batch',
  created_date: 1752962972,
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
  spatial_updated: 1753093189094,
  start_date: '1763-02-10',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['GD'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3116419'
};

MERGE (c:Colony {colony_id: 'griqualand_west_1871_1880'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Griqualand West',
  colony_id: 'griqualand_west_1871_1880',
  colony_type: 'Crown Colony',
  comments: 'Diamond mining area, incorporated into Cape Colony 1880',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'heard_and_mcdonald_islands_1833_1947'})
SET c += {
  administrative_status: 'Remote Island',
  canonical_name: 'Heard and McDonald Islands',
  colony_id: 'heard_and_mcdonald_islands_1833_1947',
  colony_type: 'Remote Island',
  comments: 'Sub-Antarctic islands, sealing and research, transferred to Australia',
  coordinates_source: 'wikidata_batch',
  created_date: 1753010772,
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
  spatial_updated: 1753093189117,
  start_date: '1833-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:01.860000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q35086'
};

MERGE (c:Colony {colony_id: 'heligoland_1807_1890'})
SET c += {
  canonical_name: 'Heligoland',
  colony_id: 'heligoland_1807_1890',
  established_year: 1807,
  independence_year: 1890,
  region: 'Europe',
  type: 'Crown Colony',
  wikidata_id: 'Q3104'
};

MERGE (c:Colony {colony_id: 'henderson_island_1902_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Henderson Island',
  colony_id: 'henderson_island_1902_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Part of Pitcairn Islands group, uninhabited',
  coordinates_source: 'wikidata_batch',
  created_date: 1752967315,
  established_year: 1902,
  latitude: -25.0677812,
  link_status: 'verified',
  longitude: -130.1045778,
  modern_nation_qids: ['Q35672'],
  name: 'Henderson Island',
  region: 'Pacific',
  source: 'Additional Southeast Asian Territories',
  spatial_updated: 1753093189127,
  start_date: '1902-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:08.833000000+00:00',
  whg_aat_types: ['300000776'],
  whg_ccodes: ['PN'],
  whg_fclasses: ['T'],
  wikidata_id: 'Q184851'
};

MERGE (c:Colony {colony_id: 'hong_kong_1841_1997'})
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
  spatial_updated: 1753093189138,
  start_date: '1841-01-01',
  transition_type: 'handover',
  verified: false,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['HK'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1054923'
};

MERGE (c:Colony {colony_id: 'howland_island_1857_1898'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Howland Island',
  colony_id: 'howland_island_1857_1898',
  colony_type: 'Guano Island',
  comments: 'Claimed for guano mining, transferred to United States',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'ile_royale_1713_1763'})
SET c += {
  administrative_status: 'Colonial Territory',
  canonical_name: 'Île Royale',
  colony_id: 'ile_royale_1713_1763',
  colony_type: 'Colonial Territory',
  comments: 'French colony on Cape Breton Island, site of Fortress Louisbourg',
  created_date: 1753030225546,
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

MERGE (c:Colony {colony_id: 'imperial_british_east_africa_company_territory_1888_1895'})
SET c += {
  administrative_status: 'Company Territory',
  canonical_name: 'Imperial British East Africa Company Territory',
  colony_id: 'imperial_british_east_africa_company_territory_1888_1895',
  colony_type: 'Company Territory',
  comments: 'IBEA Company administered coastal Kenya and parts of Uganda',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'indian_empire_british_raj_1858_1947'})
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
  spatial_updated: 1753093189159,
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

MERGE (c:Colony {colony_id: 'ionian_islands_1815_1864'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Ionian Islands',
  colony_id: 'ionian_islands_1815_1864',
  colony_type: 'Protectorate',
  comments: 'British protectorate, ceded to Greece 1864',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'iraq_1932_ongoing'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'Iraq',
  colony_id: 'iraq_1932_ongoing',
  colony_type: 'Independence',
  comments: 'Kingdom of Iraq, first Arab state to gain independence from League mandate',
  coordinates_source: 'wikidata_batch',
  created_date: 1752963079,
  established_year: 1932,
  latitude: 33.0,
  link_status: 'verified',
  longitude: 43.0,
  modern_nation_qids: ['Q796'],
  name: 'Iraq',
  region: 'Middle East',
  source: 'Middle East and Mediterranean Evolution',
  spatial_updated: 1753093189171,
  start_date: '1932-10-03',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.637000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['IQ'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q146720'
};

MERGE (c:Colony {colony_id: 'ireland_uk_1801_1922'})
SET c += {
  canonical_name: 'Ireland (UK)',
  colony_id: 'ireland_uk_1801_1922',
  established_year: 1801,
  independence_year: 1922,
  region: 'Europe',
  type: 'Union',
  wikidata_id: 'Q174193'
};

MERGE (c:Colony {colony_id: 'irish_free_state_1922_1937'})
SET c += {
  canonical_name: 'Irish Free State',
  colony_id: 'irish_free_state_1922_1937',
  established_year: 1922,
  independence_year: 1937,
  region: 'Europe',
  type: 'Dominion',
  wikidata_id: 'Q31747'
};

MERGE (c:Colony {colony_id: 'isle_de_france_british_occupation_1810_1814'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Isle de France (British Occupation)',
  colony_id: 'isle_de_france_british_occupation_1810_1814',
  colony_type: 'Military Administration',
  comments: 'Captured from France during Napoleonic Wars',
  coordinates_source: 'wikidata_batch',
  created_date: 1752967506,
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
  spatial_updated: 1753093189206,
  start_date: '1810-12-03',
  verified: true,
  whg_aat_types: ['300387081'],
  whg_ccodes: ['MU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q12053604'
};

MERGE (c:Colony {colony_id: 'jamaica_1655_1962'})
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
  spatial_updated: 1753093189218,
  start_date: '1655-01-01',
  transition_type: 'independence',
  verified: true,
  whg_aat_types: ['300387506'],
  whg_ccodes: ['JM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2526023'
};

MERGE (c:Colony {colony_id: 'james_island_trading_post_1661_1816'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'James Island Trading Post',
  colony_id: 'james_island_trading_post_1661_1816',
  colony_type: 'Trading Post',
  comments: 'Royal African Company trading post on James Island',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'jarvis_island_1857_1898'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Jarvis Island',
  colony_id: 'jarvis_island_1857_1898',
  colony_type: 'Guano Island',
  comments: 'Claimed for guano mining, transferred to United States',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'java_british_occupation_1811_1816'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Java (British Occupation)',
  colony_id: 'java_british_occupation_1811_1816',
  colony_type: 'Military Administration',
  comments: 'British occupation during Napoleonic Wars, administered by Stamford Raffles',
  created_date: 1752967315,
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

MERGE (c:Colony {colony_id: 'kenya_colony_and_protectorate_of_1920_1963'})
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
  spatial_updated: 1753093189277,
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

MERGE (c:Colony {colony_id: 'kingdom_of_ireland_1541_1801'})
SET c += {
  canonical_name: 'Kingdom of Ireland',
  colony_id: 'kingdom_of_ireland_1541_1801',
  established_year: 1541,
  independence_year: 1801,
  region: 'Europe',
  type: 'Kingdom',
  wikidata_id: 'Q179876'
};

MERGE (c:Colony {colony_id: 'kuwait_1899_1961'})
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
  spatial_updated: 1753093189299,
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

MERGE (c:Colony {colony_id: 'labuan_1846_1963'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Labuan',
  colony_id: 'labuan_1846_1963',
  colony_type: 'Crown Colony',
  comments: 'Island off Borneo coast, coal station, joined Malaysia',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'lagos_protectorate_1887_1906'})
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

MERGE (c:Colony {colony_id: 'leeward_islands_colony_1671_1816'})
SET c += {
  administrative_status: 'Federal Colony',
  canonical_name: 'Leeward Islands Colony',
  colony_id: 'leeward_islands_colony_1671_1816',
  colony_type: 'Federal Colony',
  comments: 'The first British federal colony in the Leeward Islands, which was dissolved in 1816.',
  created_date: 1753013488,
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

MERGE (c:Colony {colony_id: 'line_islands_british_1888_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Line Islands (British)',
  colony_id: 'line_islands_british_1888_1979',
  colony_type: 'Crown Colony',
  comments: 'Part of Gilbert and Ellice Islands, became part of Kiribati',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'lower_burma_1824_1886'})
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
  spatial_updated: 1753093188633,
  start_date: '1824-01-01',
  transition_type: 'independence',
  verified: true,
  verified_date: '2025-08-06T02:31:54.454000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['MM'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1937196'
};

MERGE (c:Colony {colony_id: 'lower_canada_1791_1841'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Lower Canada',
  colony_id: 'lower_canada_1791_1841',
  colony_type: 'Crown Colony',
  comments: 'Created by Constitutional Act 1791, merged into Province of Canada',
  created_date: 1752961518,
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

MERGE (c:Colony {colony_id: 'madras_presidency_company_1640_1858'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Madras Presidency (Company)',
  colony_id: 'madras_presidency_company_1640_1858',
  colony_type: 'Presidency',
  comments: 'Fort St. George, expanded across southern India, Carnatic Wars',
  created_date: 1752962006,
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

MERGE (c:Colony {colony_id: 'madras_presidency_crown_1858_1947'})
SET c += {
  administrative_status: 'Presidency',
  canonical_name: 'Madras Presidency (Crown)',
  colony_id: 'madras_presidency_crown_1858_1947',
  colony_type: 'Presidency',
  comments: 'Crown rule over southern India, Tamil Nadu, Andhra Pradesh, parts of Kerala',
  created_date: 1752962006,
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

MERGE (c:Colony {colony_id: 'mainland_british_columbia_1858_1866'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Colony of British Columbia (Mainland)',
  colony_id: 'mainland_british_columbia_1858_1866',
  colony_type: 'Crown Colony',
  comments: 'Mainland-only colony established during the Fraser Canyon Gold Rush.',
  coordinates_source: 'wikidata',
  created_date: 1752961518,
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
  spatial_updated: 1753058508557,
  start_date: '1858-01-01',
  verified: true,
  verified_date: '2025-08-06T00:00:25.599000000+00:00',
  whg_aat_types: ['300387506'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2514958'
};

MERGE (c:Colony {colony_id: 'malacca_settlement_1824_1826'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Malacca Settlement',
  colony_id: 'malacca_settlement_1824_1826',
  colony_type: 'Crown Colony',
  comments: 'Acquired from Dutch in Anglo-Dutch Treaty',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'malaya_independent_1957_1963'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'Malaya (Independent)',
  colony_id: 'malaya_independent_1957_1963',
  colony_type: 'Independence',
  comments: 'Independent Federation of Malaya before Malaysia formation',
  created_date: 1752967217,
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

MERGE (c:Colony:Federation {colony_id: 'malayan_union_1946_1948'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Malayan Union',
  colony_id: 'malayan_union_1946_1948',
  colony_type: 'Crown Colony',
  comments: 'Failed attempt to unite Malayan territories',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'malaysia_1963'})
SET c += {
  canonical_name: 'Malaysia',
  colony_id: 'malaysia_1963',
  established_year: 1963,
  region: 'Southeast Asia',
  type: 'Independence',
  wikidata_id: 'Q833'
};

MERGE (c:Colony {colony_id: 'maldives_protectorate_1887_1965'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Maldives Protectorate',
  colony_id: 'maldives_protectorate_1887_1965',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Sultanate of Maldives',
  created_date: 1752967507,
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

MERGE (c:Colony {colony_id: 'malta_1800_1964'})
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

MERGE (c:Colony {colony_id: 'mandatory_iraq_1920_1932'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Mandatory Iraq',
  colony_id: 'mandatory_iraq_1920_1932',
  colony_type: 'Mandate',
  comments: 'British Mandate for Mesopotamia, became Kingdom of Iraq',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'manra_sydney_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Manra (Sydney Island)',
  colony_id: 'manra_sydney_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, transferred to Kiribati',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'maryland_colony_1634_1783'})
SET c += {
  administrative_status: 'Proprietary Colony',
  canonical_name: 'Maryland Colony',
  colony_id: 'maryland_colony_1634_1783',
  colony_type: 'Proprietary Colony',
  comments: 'Catholic colony founded by Lord Baltimore',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'massachusetts_bay_colony_1630_1783'})
SET c += {
  administrative_status: 'Charter Colony',
  canonical_name: 'Massachusetts Bay Colony',
  colony_id: 'massachusetts_bay_colony_1630_1783',
  colony_type: 'Charter Colony',
  comments: 'Puritan colony, Boston founded 1630',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'mauritius_1814_1968'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Mauritius',
  colony_id: 'mauritius_1814_1968',
  colony_type: 'Crown Colony',
  comments: 'Major sugar plantation colony, important naval base and coaling station',
  created_date: 1752967506,
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

MERGE (c:Colony {colony_id: 'mckean_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'McKean Island',
  colony_id: 'mckean_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, transferred to Kiribati',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'mesopotamia_british_occupied_1914_1920'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Mesopotamia (British Occupied)',
  colony_id: 'mesopotamia_british_occupied_1914_1920',
  colony_type: 'Military Administration',
  comments: 'Occupied from Ottoman Empire during WWI',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'minorca_first_1708_1756'})
SET c += {
  canonical_name: 'Minorca (1st British)',
  colony_id: 'minorca_first_1708_1756',
  established_year: 1708,
  independence_year: 1756,
  region: 'Europe',
  type: 'Crown Colony',
  wikidata_id: 'Q173095'
};

MERGE (c:Colony {colony_id: 'minorca_second_1763_1782'})
SET c += {
  canonical_name: 'Minorca (2nd British)',
  colony_id: 'minorca_second_1763_1782',
  established_year: 1763,
  independence_year: 1782,
  region: 'Europe',
  type: 'Crown Colony',
  wikidata_id: 'Q173095'
};

MERGE (c:Colony {colony_id: 'minorca_third_1798_1802'})
SET c += {
  canonical_name: 'Minorca (3rd British)',
  colony_id: 'minorca_third_1798_1802',
  established_year: 1798,
  independence_year: 1802,
  region: 'Europe',
  type: 'Crown Colony',
  wikidata_id: 'Q173095'
};

MERGE (c:Colony {colony_id: 'moluccas_british_occupation_1810_1817'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Moluccas (British Occupation)',
  colony_id: 'moluccas_british_occupation_1810_1817',
  colony_type: 'Military Administration',
  comments: 'British occupation of Spice Islands during Napoleonic Wars',
  created_date: 1752967315,
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

MERGE (c:Colony {colony_id: 'montserrat_1632_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Montserrat',
  colony_id: 'montserrat_1632_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Still British Overseas Territory, volcanic island',
  created_date: 1752962972,
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

MERGE (c:Colony {colony_id: 'mosquito_coast_1638_1860'})
SET c += {
  canonical_name: 'Mosquito Coast',
  colony_id: 'mosquito_coast_1638_1860',
  established_year: 1638,
  independence_year: 1860,
  region: 'Caribbean',
  type: 'Protectorate',
  wikidata_id: 'Q1948981'
};

MERGE (c:Colony {colony_id: 'muscat_and_oman_protectorate_1891_1971'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Muscat and Oman Protectorate',
  colony_id: 'muscat_and_oman_protectorate_1891_1971',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Sultanate of Muscat and Oman',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'natalia_republic_1839_1843'})
SET c += {
  administrative_status: 'Boer Republic',
  canonical_name: 'Natalia Republic',
  colony_id: 'natalia_republic_1839_1843',
  colony_type: 'Boer Republic',
  comments: 'Voortrekker republic in Natal, annexed by Britain 1843',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'nauru_1920_1968'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Nauru',
  colony_id: 'nauru_1920_1968',
  colony_type: 'Mandate',
  comments: 'Former German possession, phosphate mining island',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'netherlands_east_indies_british_administration_1945_1946'})
SET c += {
  administrative_status: 'Military Administration',
  canonical_name: 'Netherlands East Indies (British Administration)',
  colony_id: 'netherlands_east_indies_british_administration_1945_1946',
  colony_type: 'Military Administration',
  comments: 'Brief British military administration after Japanese surrender before Dutch return',
  created_date: 1752967315,
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

MERGE (c:Colony {colony_id: 'new_brunswick_1784_1867'})
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

MERGE (c:Colony {colony_id: 'new_brunswick_province_1867'})
SET c += {
  canonical_name: 'New Brunswick (Province)',
  colony_id: 'new_brunswick_province_1867',
  colony_type: 'Province',
  established_year: 1867,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1965'
};

MERGE (c:Colony {colony_id: 'new_france_1608_1763'})
SET c += {
  administrative_status: 'Colonial Empire',
  canonical_name: 'New France',
  colony_id: 'new_france_1608_1763',
  colony_type: 'Colonial Empire',
  comments: 'French colonial empire in North America, ended with Treaty of Paris 1763',
  created_date: 1753030225482,
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

MERGE (c:Colony {colony_id: 'new_hampshire_colony_1623_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'New Hampshire Colony',
  colony_id: 'new_hampshire_colony_1623_1783',
  colony_type: 'Royal Colony',
  comments: 'Separated from Massachusetts 1679',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'new_hebrides_1906_1980'})
SET c += {
  administrative_status: 'Anglo-French Condominium',
  canonical_name: 'New Hebrides',
  colony_id: 'new_hebrides_1906_1980',
  colony_type: 'Anglo-French Condominium',
  comments: 'Joint British-French administration',
  created_date: 1752963189,
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

MERGE (c:Colony {colony_id: 'new_jersey_colony_1664_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'New Jersey Colony',
  colony_id: 'new_jersey_colony_1664_1783',
  colony_type: 'Royal Colony',
  comments: 'Divided into East/West Jersey, reunited 1702',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'new_south_wales_original_1788_1901'})
SET c += {
  administrative_status: 'Penal Colony',
  canonical_name: 'New South Wales',
  colony_id: 'new_south_wales_original_1788_1901',
  colony_type: 'Penal Colony',
  comments: 'Original colony covering most of eastern Australia, gradually subdivided',
  coordinates_source: 'wikidata',
  created_date: 1752961787,
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
  spatial_updated: 1753058508573,
  start_date: '1788-01-26',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:09.601000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q18348382'
};

MERGE (c:Colony {colony_id: 'new_york_colony_1664_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'New York Colony',
  colony_id: 'new_york_colony_1664_1783',
  colony_type: 'Royal Colony',
  comments: 'Captured from Dutch New Amsterdam',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'new_zealand_colony_1840_1907'})
SET c += {
  canonical_name: 'New Zealand Colony',
  colony_id: 'new_zealand_colony_1840_1907',
  established_year: 1840,
  independence_year: 1907,
  region: 'Pacific',
  type: 'Crown Colony',
  wikidata_id: 'Q664'
};

MERGE (c:Colony {colony_id: 'new_zealand_independent_1947'})
SET c += {
  canonical_name: 'New Zealand',
  colony_id: 'new_zealand_independent_1947',
  established_year: 1947,
  region: 'Pacific',
  type: 'Independence',
  wikidata_id: 'Q664'
};

MERGE (c:Colony {colony_id: 'newfoundland_commission_1934_1949'})
SET c += {
  canonical_name: 'Newfoundland (Commission)',
  colony_id: 'newfoundland_commission_1934_1949',
  established_year: 1934,
  independence_year: 1949,
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q5152678'
};

MERGE (c:Colony {colony_id: 'newfoundland_province_1949'})
SET c += {
  canonical_name: 'Newfoundland and Labrador',
  colony_id: 'newfoundland_province_1949',
  colony_type: 'Province',
  established_year: 1949,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q2003'
};

MERGE (c:Colony {colony_id: 'niger_coast_protectorate_1893_1900'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Niger Coast Protectorate',
  colony_id: 'niger_coast_protectorate_1893_1900',
  colony_type: 'Protectorate',
  comments: 'Renamed Oil Rivers Protectorate',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'norfolk_island_1788_1914'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Norfolk Island',
  colony_id: 'norfolk_island_1788_1914',
  colony_type: 'Crown Colony',
  comments: 'Penal settlement, transferred to Australian administration',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'norfolk_island_whaling_station_1830_1870'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'Norfolk Island Whaling Station',
  colony_id: 'norfolk_island_whaling_station_1830_1870',
  colony_type: 'Whaling Station',
  comments: 'Seasonal whaling operations around Norfolk Island',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'north_borneo_crown_colony_1946_1963'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'North Borneo Crown Colony',
  colony_id: 'north_borneo_crown_colony_1946_1963',
  colony_type: 'Crown Colony',
  comments: 'Crown colony before joining Malaysia as Sabah',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'north_carolina_colony_1663_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'North Carolina Colony',
  colony_id: 'north_carolina_colony_1663_1783',
  colony_type: 'Royal Colony',
  comments: 'Originally part of Carolina, split 1712',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'north_west_frontier_province_1901_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'North-West Frontier Province',
  colony_id: 'north_west_frontier_province_1901_1947',
  colony_type: 'Province',
  comments: 'Created from districts of Punjab, joined Pakistan 1947',
  created_date: 1752962007,
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

MERGE (c:Colony {colony_id: 'north_western_territory_1670_1870'})
SET c += {
  administrative_status: 'Territory',
  canonical_name: 'North-Western Territory',
  colony_id: 'north_western_territory_1670_1870',
  colony_type: 'Territory',
  comments: 'Transferred to Canada with Rupert\'s Land',
  created_date: 1752961518,
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

MERGE (c:Colony {colony_id: 'northern_ireland_1920'})
SET c += {
  canonical_name: 'Northern Ireland',
  colony_id: 'northern_ireland_1920',
  established_year: 1920,
  region: 'Europe',
  type: 'Devolved Government',
  wikidata_id: 'Q26'
};

MERGE (c:Colony {colony_id: 'northern_nigeria_1900_1914'})
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

MERGE (c:Colony {colony_id: 'northern_rhodesia_colony_1924_1953'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Northern Rhodesia Colony',
  colony_id: 'northern_rhodesia_colony_1924_1953',
  colony_type: 'Crown Colony',
  comments: 'Crown colony after BSAC rule ended, before federation',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'northern_rhodesia_post_federation_1964'})
SET c += {
  canonical_name: 'Northern Rhodesia',
  colony_id: 'northern_rhodesia_post_federation_1964',
  established_year: 1963,
  independence_year: 1964,
  region: 'Southern Africa',
  type: 'Transitional',
  wikidata_id: 'Q953903'
};

MERGE (c:Colony {colony_id: 'northern_territories_gold_coast_1897_1957'})
SET c += {
  canonical_name: 'Northern Territories of the Gold Coast',
  colony_id: 'northern_territories_gold_coast_1897_1957',
  established_year: 1897,
  independence_year: 1957,
  region: 'West Africa',
  type: 'Protectorate',
  wikidata_id: 'Q2000610'
};

MERGE (c:Colony {colony_id: 'nova_scotia_post_1784_1867'})
SET c += {
  canonical_name: 'Nova Scotia',
  colony_id: 'nova_scotia_post_1784_1867',
  established_year: 1784,
  independence_year: 1867,
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q98931415'
};

MERGE (c:Colony {colony_id: 'nova_scotia_pre_1713_1784'})
SET c += {
  canonical_name: 'Nova Scotia',
  colony_id: 'nova_scotia_pre_1713_1784',
  established_year: 1713,
  independence_year: 1784,
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q98931415'
};

MERGE (c:Colony {colony_id: 'nova_scotia_province_1867'})
SET c += {
  canonical_name: 'Nova Scotia (Province)',
  colony_id: 'nova_scotia_province_1867',
  colony_type: 'Province',
  established_year: 1867,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1952'
};

MERGE (c:Colony {colony_id: 'nunavut_1999'})
SET c += {
  canonical_name: 'Nunavut',
  colony_id: 'nunavut_1999',
  colony_type: 'Territory',
  established_year: 1999,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q2023'
};

MERGE (c:Colony {colony_id: 'nyasaland_1891_1964'})
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

MERGE (c:Colony:Federation {colony_id: 'nyasaland_post_federation_1963'})
SET c += {
  canonical_name: 'Nyasaland',
  colony_id: 'nyasaland_post_federation_1963',
  comments: 'Brief return to colonial status after Federation dissolution',
  created_date: 1753012916,
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

MERGE (c:Colony {colony_id: 'ocean_island_banaba_1900_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Ocean Island (Banaba)',
  colony_id: 'ocean_island_banaba_1900_1979',
  colony_type: 'Crown Colony',
  comments: 'Phosphate mining island, became part of Kiribati',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'oeno_island_1902_ongoing'})
SET c += {
  administrative_status: 'Remote Island',
  canonical_name: 'Oeno Island',
  colony_id: 'oeno_island_1902_ongoing',
  colony_type: 'Remote Island',
  comments: 'Part of Pitcairn Islands group, coral atoll',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'oil_rivers_protectorate_1885_1893'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Oil Rivers Protectorate',
  colony_id: 'oil_rivers_protectorate_1885_1893',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Niger Delta trading states',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'ontario_1867'})
SET c += {
  canonical_name: 'Ontario',
  colony_id: 'ontario_1867',
  colony_type: 'Province',
  established_year: 1867,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1904'
};

MERGE (c:Colony {colony_id: 'orange_free_state_1854_1900'})
SET c += {
  administrative_status: 'Boer Republic',
  canonical_name: 'Orange Free State',
  colony_id: 'orange_free_state_1854_1900',
  colony_type: 'Boer Republic',
  comments: 'Independent Boer republic, conquered during Second Boer War',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'orange_river_colony_1900_1910'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Orange River Colony',
  colony_id: 'orange_river_colony_1900_1910',
  colony_type: 'Crown Colony',
  comments: 'Orange Free State conquered and renamed, gained self-government 1907',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'orange_river_sovereignty_1848_1854'})
SET c += {
  administrative_status: 'British Sovereignty',
  canonical_name: 'Orange River Sovereignty',
  colony_id: 'orange_river_sovereignty_1848_1854',
  colony_type: 'British Sovereignty',
  comments: 'British sovereignty between Orange and Vaal rivers, abandoned in Bloemfontein Convention',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'palestine_1920_1948'})
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

MERGE (c:Colony {colony_id: 'penang_prince_of_wales_island_1786_1826'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Penang (Prince of Wales Island)',
  colony_id: 'penang_prince_of_wales_island_1786_1826',
  colony_type: 'Trading Post',
  comments: 'First British settlement in Southeast Asia, acquired from Sultan of Kedah',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'pennsylvania_colony_1681_1783'})
SET c += {
  administrative_status: 'Proprietary Colony',
  canonical_name: 'Pennsylvania Colony',
  colony_id: 'pennsylvania_colony_1681_1783',
  colony_type: 'Proprietary Colony',
  comments: 'William Penn\'s Quaker colony, Philadelphia',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'phoenix_islands_1937_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Phoenix Islands',
  colony_id: 'phoenix_islands_1937_1979',
  colony_type: 'Crown Colony',
  comments: 'Part of Gilbert and Ellice Islands, became part of Kiribati',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'pitcairn_islands_1838_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Pitcairn Islands',
  colony_id: 'pitcairn_islands_1838_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Settlement of Bounty mutineers, still British territory',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'prince_edward_island_1769_1873'})
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

MERGE (c:Colony {colony_id: 'prince_edward_island_province_1873'})
SET c += {
  canonical_name: 'Prince Edward Island (Province)',
  colony_id: 'prince_edward_island_province_1873',
  colony_type: 'Province',
  established_year: 1873,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1979'
};

MERGE (c:Colony {colony_id: 'princely_states_placeholder_1818_1947'})
SET c += {
  canonical_name: 'Princely States (placeholder)',
  colony_id: 'princely_states_placeholder_1818_1947',
  established_year: 1818,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Princely State',
  wikidata_id: 'Q1336152'
};

MERGE (c:Colony {colony_id: 'province_of_canada_1841_1867'})
SET c += {
  administrative_status: 'United Province',
  canonical_name: 'Province of Canada',
  colony_id: 'province_of_canada_1841_1867',
  colony_type: 'United Province',
  comments: 'Union of Upper and Lower Canada, split into Ontario and Quebec at Confederation',
  created_date: 1752961518,
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

MERGE (c:Colony {colony_id: 'province_of_freedom_1787_1792'})
SET c += {
  administrative_status: 'Settlement',
  canonical_name: 'Province of Freedom',
  colony_id: 'province_of_freedom_1787_1792',
  colony_type: 'Settlement',
  comments: 'First settlement for freed slaves, failed due to conflicts',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'province_of_quebec_british_1763_1791'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Province of Quebec (British)',
  colony_id: 'province_of_quebec_british_1763_1791',
  colony_type: 'Crown Colony',
  comments: 'British conquest of New France, Quebec Act 1774',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'punjab_province_1849_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'Punjab Province',
  colony_id: 'punjab_province_1849_1947',
  colony_type: 'Province',
  comments: 'Annexed after Second Anglo-Sikh War, partitioned 1947 between India and Pakistan',
  created_date: 1752962006,
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

MERGE (c:Colony {colony_id: 'qatar_protectorate_1916_1971'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Qatar Protectorate',
  colony_id: 'qatar_protectorate_1916_1971',
  colony_type: 'Protectorate',
  comments: 'British protectorate replacing Ottoman rule',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'quebec_1867'})
SET c += {
  canonical_name: 'Quebec',
  colony_id: 'quebec_1867',
  colony_type: 'Province',
  established_year: 1867,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q176'
};

MERGE (c:Colony {colony_id: 'queensland_1859_1901'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Queensland',
  colony_id: 'queensland_1859_1901',
  colony_type: 'Crown Colony',
  comments: 'Northern NSW separated as Queensland, immediately self-governing',
  coordinates_source: 'wikidata',
  created_date: 1752961788,
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
  spatial_updated: 1753058508636,
  start_date: '1859-06-06',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:11.146000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q28401203'
};

MERGE (c:Colony {colony_id: 'rawaki_phoenix_island_1860_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Rawaki (Phoenix Island)',
  colony_id: 'rawaki_phoenix_island_1860_1979',
  colony_type: 'Guano Island',
  comments: 'Phoenix Islands guano mining, transferred to Kiribati',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'red_river_colony_1811_1870'})
SET c += {
  canonical_name: 'Red River Colony',
  colony_id: 'red_river_colony_1811_1870',
  established_year: 1811,
  independence_year: 1870,
  region: 'North America',
  type: 'Colony',
  wikidata_id: 'Q1143638'
};

MERGE (c:Colony {colony_id: 'rhode_island_colony_1636_1783'})
SET c += {
  administrative_status: 'Charter Colony',
  canonical_name: 'Rhode Island Colony',
  colony_id: 'rhode_island_colony_1636_1783',
  colony_type: 'Charter Colony',
  comments: 'Founded by Roger Williams, religious tolerance',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'rhodesia_udi_1965_1979'})
SET c += {
  administrative_status: 'Unilateral Independence',
  canonical_name: 'Rhodesia (UDI)',
  colony_id: 'rhodesia_udi_1965_1979',
  colony_type: 'Unilateral Independence',
  comments: 'Unilateral Declaration of Independence by white minority government',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'rodrigues_1814_1968'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Rodrigues',
  colony_id: 'rodrigues_1814_1968',
  colony_type: 'Dependency',
  comments: 'Dependency of Mauritius, important way station',
  created_date: 1752967506,
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

MERGE (c:Colony {colony_id: 'royal_niger_company_territory_1886_1900'})
SET c += {
  administrative_status: 'Company Territory',
  canonical_name: 'Royal Niger Company Territory',
  colony_id: 'royal_niger_company_territory_1886_1900',
  colony_type: 'Company Territory',
  comments: 'Royal Niger Company controlled interior Nigeria',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'ruperts_land_1670_1870'})
SET c += {
  administrative_status: 'Hudson\'s Bay Company Territory',
  canonical_name: 'Rupert\'s Land',
  colony_id: 'ruperts_land_1670_1870',
  colony_type: 'Hudson\'s Bay Company Territory',
  comments: 'Vast HBC territory, sold to Canada 1870, became Manitoba and Northwest Territories',
  created_date: 1752961518,
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

MERGE (c:Colony {colony_id: 'saint_christopher_nevis_anguilla_1958_1983'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Saint Kitts and Nevis Colony',
  colony_id: 'saint_christopher_nevis_anguilla_1958_1983',
  colony_type: 'Crown Colony',
  comments: 'First British settlement in Caribbean, mother colony of West Indies',
  created_date: 1752962972,
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

MERGE (c:Colony {colony_id: 'saint_helena_ascension_and_tristan_da_cunha_1588_ongoing'})
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

MERGE (c:Colony {colony_id: 'saint_lucia_colony_1814_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Saint Lucia Colony',
  colony_id: 'saint_lucia_colony_1814_1979',
  colony_type: 'Crown Colony',
  comments: 'Ceded by France after Napoleonic Wars',
  created_date: 1752962972,
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

MERGE (c:Colony {colony_id: 'sarawak_1841_1946'})
SET c += {
  administrative_status: 'Personal Rule',
  canonical_name: 'Sarawak',
  colony_id: 'sarawak_1841_1946',
  colony_type: 'Personal Rule',
  comments: 'Kingdom of Sarawak under Brooke family, British protection from 1888',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'sarawak_crown_colony_1946_1963'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Sarawak Crown Colony',
  colony_id: 'sarawak_crown_colony_1946_1963',
  colony_type: 'Crown Colony',
  comments: 'Crown colony before joining Malaysia',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'saskatchewan_1905'})
SET c += {
  canonical_name: 'Saskatchewan',
  colony_id: 'saskatchewan_1905',
  colony_type: 'Province',
  established_year: 1905,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q1989'
};

MERGE (c:Colony {colony_id: 'settlement_of_belize_1798_1862'})
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

MERGE (c:Colony {colony_id: 'seychelles_1903_1976'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Seychelles',
  colony_id: 'seychelles_1903_1976',
  colony_type: 'Crown Colony',
  comments: 'Separate crown colony from 1903',
  created_date: 1752967506,
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

MERGE (c:Colony {colony_id: 'seychelles_mauritius_dependency_1814_1903'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Seychelles (Mauritius Dependency)',
  colony_id: 'seychelles_mauritius_dependency_1814_1903',
  colony_type: 'Dependency',
  comments: 'Administered as dependency of Mauritius',
  created_date: 1752967506,
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

MERGE (c:Colony {colony_id: 'shanghai_international_settlement_1863_1943'})
SET c += {
  administrative_status: 'International Settlement',
  canonical_name: 'Shanghai International Settlement',
  colony_id: 'shanghai_international_settlement_1863_1943',
  colony_type: 'International Settlement',
  comments: 'Joint British-American administration in Shanghai',
  created_date: 1752967315,
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

MERGE (c:Colony {colony_id: 'sierra_leone_colony_1808_1896'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Sierra Leone Colony',
  colony_id: 'sierra_leone_colony_1808_1896',
  colony_type: 'Crown Colony',
  comments: 'Crown colony centered on Freetown',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'sierra_leone_colony_and_protectorate_1787_1961'})
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

MERGE (c:Colony {colony_id: 'sierra_leone_company_settlement_1792_1808'})
SET c += {
  administrative_status: 'Company Settlement',
  canonical_name: 'Sierra Leone Company Settlement',
  colony_id: 'sierra_leone_company_settlement_1792_1808',
  colony_type: 'Company Settlement',
  comments: 'Sierra Leone Company administered Freetown',
  created_date: 1752962592,
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

MERGE (c:Colony {colony_id: 'sind_province_1843_1947'})
SET c += {
  canonical_name: 'Sind',
  colony_id: 'sind_province_1843_1947',
  established_year: 1936,
  independence_year: 1947,
  region: 'South Asia',
  type: 'Province',
  wikidata_id: 'Q7523949'
};

MERGE (c:Colony {colony_id: 'singapore_crown_colony_1946_1963'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Singapore Crown Colony',
  colony_id: 'singapore_crown_colony_1946_1963',
  colony_type: 'Crown Colony',
  comments: 'Separated from Straits Settlements, joined Malaysia 1963',
  created_date: 1752967217,
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

MERGE (c:Colony {colony_id: 'singapore_independent_1965'})
SET c += {
  canonical_name: 'Singapore',
  colony_id: 'singapore_independent_1965',
  established_year: 1965,
  region: 'Southeast Asia',
  type: 'Independence',
  wikidata_id: 'Q334'
};

MERGE (c:Colony {colony_id: 'singapore_settlement_1819_1826'})
SET c += {
  administrative_status: 'Trading Post',
  canonical_name: 'Singapore Settlement',
  colony_id: 'singapore_settlement_1819_1826',
  colony_type: 'Trading Post',
  comments: 'Founded by Stamford Raffles, strategic port',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'socotra_island_1886_1967'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Socotra Island',
  colony_id: 'socotra_island_1886_1967',
  colony_type: 'Protectorate',
  comments: 'Strategic island in Arabian Sea, part of Aden Protectorate',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'somali_republic_1960'})
SET c += {
  canonical_name: 'Somali Republic',
  colony_id: 'somali_republic_1960',
  established_year: 1960,
  region: 'Middle East',
  type: 'Independence',
  wikidata_id: 'Q1045'
};

MERGE (c:Colony {colony_id: 'south_african_republic_restored_1881_1900'})
SET c += {
  administrative_status: 'Boer Republic',
  canonical_name: 'South African Republic (Restored)',
  colony_id: 'south_african_republic_restored_1881_1900',
  colony_type: 'Boer Republic',
  comments: 'Independence restored after First Boer War, lost in Second Boer War',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'south_african_republic_transvaal_1852_1877'})
SET c += {
  administrative_status: 'Boer Republic',
  canonical_name: 'South African Republic (Transvaal)',
  colony_id: 'south_african_republic_transvaal_1852_1877',
  colony_type: 'Boer Republic',
  comments: 'Independent Boer republic north of Vaal River, first British annexation',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'south_australia_1836_1901'})
SET c += {
  administrative_status: 'Planned Colony',
  canonical_name: 'South Australia',
  colony_id: 'south_australia_1836_1901',
  colony_type: 'Planned Colony',
  comments: 'Planned free settlement colony, gained self-government 1856',
  coordinates_source: 'wikidata',
  created_date: 1752961788,
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
  spatial_updated: 1753058508623,
  start_date: '1836-02-19',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:11.454000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q35715'
};

MERGE (c:Colony {colony_id: 'south_carolina_colony_1663_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'South Carolina Colony',
  colony_id: 'south_carolina_colony_1663_1783',
  colony_type: 'Royal Colony',
  comments: 'Originally part of Carolina, split 1712, Charleston',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'south_georgia_1775_ongoing'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'South Georgia',
  colony_id: 'south_georgia_1775_ongoing',
  colony_type: 'Dependency',
  comments: 'Sub-Antarctic whaling and sealing base, Cook\'s landing',
  created_date: 1753013488,
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

MERGE (c:Colony {colony_id: 'south_georgia_whaling_stations_1904_1965'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'South Georgia Whaling Stations',
  colony_id: 'south_georgia_whaling_stations_1904_1965',
  colony_type: 'Whaling Station',
  comments: 'Multiple whaling stations including Grytviken, Leith Harbour, Stromness',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'south_sandwich_islands_1775_ongoing'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'South Sandwich Islands',
  colony_id: 'south_sandwich_islands_1775_ongoing',
  colony_type: 'Dependency',
  comments: 'Remote volcanic islands, discovered by Cook',
  created_date: 1753013488,
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

MERGE (c:Colony {colony_id: 'south_shetland_islands_whaling_1820_1959'})
SET c += {
  administrative_status: 'Whaling Station',
  canonical_name: 'South Shetland Islands Whaling',
  colony_id: 'south_shetland_islands_whaling_1820_1959',
  colony_type: 'Whaling Station',
  comments: 'Seasonal whaling stations, Antarctic Treaty suspension',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'south_yemen_1967_1990'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'South Yemen',
  colony_id: 'south_yemen_1967_1990',
  colony_type: 'Independence',
  comments: 'People\'s Democratic Republic of Yemen, united with North Yemen 1990',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'})
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

MERGE (c:Colony {colony_id: 'southern_rhodesia_colony_1923_1953'})
SET c += {
  administrative_status: 'Self-governing Colony',
  canonical_name: 'Southern Rhodesia Colony',
  colony_id: 'southern_rhodesia_colony_1923_1953',
  colony_type: 'Self-governing Colony',
  comments: 'Self-governing colony after BSAC rule, before federation',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'southern_rhodesia_post_federation_1963'})
SET c += {
  canonical_name: 'Southern Rhodesia',
  colony_id: 'southern_rhodesia_post_federation_1963',
  established_year: 1963,
  independence_year: 1965,
  region: 'Southern Africa',
  type: 'Self-governing Colony',
  wikidata_id: 'Q750583'
};

MERGE (c:Colony {colony_id: 'southern_rhodesia_restored_1979_1980'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Southern Rhodesia (Restored)',
  colony_id: 'southern_rhodesia_restored_1979_1980',
  colony_type: 'Crown Colony',
  comments: 'Briefly restored to Crown Colony status during transition',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'st._helena_1659_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'St. Helena',
  colony_id: 'st._helena_1659_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Strategic island, Napoleon\'s exile, still British Overseas Territory',
  created_date: 1752967507,
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

MERGE (c:Colony {colony_id: 'st_vincent_colony_1763_1979'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'St. Vincent Colony',
  colony_id: 'st_vincent_colony_1763_1979',
  colony_type: 'Crown Colony',
  comments: 'Part of Windward Islands, Black Carib resistance',
  created_date: 1753013488,
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

MERGE (c:Colony {colony_id: 'starbuck_island_1866_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Starbuck Island',
  colony_id: 'starbuck_island_1866_1979',
  colony_type: 'Guano Island',
  comments: 'Line Islands guano mining, transferred to Kiribati',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'state_of_israel_1948'})
SET c += {
  canonical_name: 'State of Israel',
  colony_id: 'state_of_israel_1948',
  established_year: 1948,
  region: 'Middle East',
  type: 'Independence',
  wikidata_id: 'Q801'
};

MERGE (c:Colony {colony_id: 'stkitts_nevis_anguilla_1816_1833'})
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

MERGE (c:Colony {colony_id: 'straits_settlements_1826_1946'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Straits Settlements',
  colony_id: 'straits_settlements_1826_1946',
  colony_type: 'Crown Colony',
  comments: 'Combined Penang, Singapore, Malacca; transferred from India Office to Colonial Office 1867',
  created_date: 1752967216,
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

MERGE (c:Colony {colony_id: 'sudan_anglo-egyptian_1899_1956'})
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

MERGE (c:Colony {colony_id: 'swains_island_1856_1925'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Swains Island',
  colony_id: 'swains_island_1856_1925',
  colony_type: 'Guano Island',
  comments: 'Claimed under Guano Islands Act, transferred to American Samoa',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'swan_river_colony_1829_1832'})
SET c += {
  administrative_status: 'Free Settlement Colony',
  canonical_name: 'Swan River Colony',
  colony_id: 'swan_river_colony_1829_1832',
  colony_type: 'Free Settlement Colony',
  comments: 'Free settlement colony, renamed to Western Australia',
  created_date: 1752961788,
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

MERGE (c:Colony {colony_id: 'swaziland_1903_1968'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Swaziland',
  colony_id: 'swaziland_1903_1968',
  colony_type: 'Protectorate',
  comments: 'Administered by Transvaal 1894-1906, then High Commissioner, became Eswatini',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'tanganyika_1961_1964'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'Tanganyika',
  colony_id: 'tanganyika_1961_1964',
  colony_type: 'Independence',
  comments: 'Independent Tanganyika before union with Zanzibar',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'tanganyika_territory_1922_1961'})
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

MERGE (c:Colony {colony_id: 'tanzania_1964'})
SET c += {
  canonical_name: 'Tanzania',
  colony_id: 'tanzania_1964',
  established_year: 1964,
  region: 'East Africa',
  type: 'Independence',
  wikidata_id: 'Q924'
};

MERGE (c:Colony {colony_id: 'tasmania_1856_1901'})
SET c += {
  administrative_status: 'Self-governing Colony',
  canonical_name: 'Tasmania',
  colony_id: 'tasmania_1856_1901',
  colony_type: 'Self-governing Colony',
  comments: 'Van Diemen\'s Land renamed to Tasmania, gained self-government',
  coordinates_source: 'wikidata',
  created_date: 1752961788,
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
  spatial_updated: 1753058508589,
  start_date: '1856-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:32:12.296000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q5148519'
};

MERGE (c:Colony {colony_id: 'territory_of_new_guinea_1920_1975'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Territory of New Guinea',
  colony_id: 'territory_of_new_guinea_1920_1975',
  colony_type: 'Mandate',
  comments: 'Former German New Guinea, administered by Australia for Britain',
  created_date: 1753013488,
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

MERGE (c:Colony {colony_id: 'territory_of_papua_1906_1949'})
SET c += {
  administrative_status: 'Territory',
  canonical_name: 'Territory of Papua',
  colony_id: 'territory_of_papua_1906_1949',
  colony_type: 'Territory',
  comments: 'Transferred to Australian administration',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'territory_of_papua_and_new_guinea_1949_1975'})
SET c += {
  administrative_status: 'Trust Territory',
  canonical_name: 'Territory of Papua and New Guinea',
  colony_id: 'territory_of_papua_and_new_guinea_1949_1975',
  colony_type: 'Trust Territory',
  comments: 'Combined Papua and New Guinea territories before independence',
  created_date: 1753013488,
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

MERGE (c:Colony {colony_id: 'tonga_protectorate_1900_1970'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Tonga Protectorate',
  colony_id: 'tonga_protectorate_1900_1970',
  colony_type: 'Protectorate',
  comments: 'British protectorate over Kingdom of Tonga',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'transjordan_1922_1946'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Transjordan',
  colony_id: 'transjordan_1922_1946',
  colony_type: 'Mandate',
  comments: 'Emirate of Transjordan under British mandate',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'transvaal_colony_first_british_1877_1881'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Transvaal Colony (First British)',
  colony_id: 'transvaal_colony_first_british_1877_1881',
  colony_type: 'Crown Colony',
  comments: 'First British annexation, lost independence after First Boer War',
  created_date: 1752962407,
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

MERGE (c:Colony {colony_id: 'transvaal_colony_second_british_1900_1910'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Transvaal Colony (Second British)',
  colony_id: 'transvaal_colony_second_british_1900_1910',
  colony_type: 'Crown Colony',
  comments: 'South African Republic conquered and renamed, gained self-government 1906',
  coordinates_source: 'wikidata',
  created_date: 1752962407,
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
  spatial_updated: 1753058508170,
  start_date: '1900-10-25',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:53.321000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q1187978'
};

MERGE (c:Colony {colony_id: 'trinidad_and_tobago_1889_1962'})
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

MERGE (c:Colony {colony_id: 'trinidad_and_tobago_colony_1797_1962'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Trinidad Colony',
  colony_id: 'trinidad_and_tobago_colony_1797_1962',
  colony_type: 'Crown Colony',
  comments: 'Trinidad captured from Spain 1797, Tobago added 1814',
  created_date: 1752962972,
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

MERGE (c:Colony {colony_id: 'tristan_da_cunha_1816_ongoing'})
SET c += {
  administrative_status: 'Dependency',
  canonical_name: 'Tristan da Cunha',
  colony_id: 'tristan_da_cunha_1816_ongoing',
  colony_type: 'Dependency',
  comments: 'Dependency of St. Helena, most remote inhabited island',
  created_date: 1752967507,
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

MERGE (c:Colony {colony_id: 'trucial_states_1820_1971'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Trucial States',
  colony_id: 'trucial_states_1820_1971',
  colony_type: 'Protectorate',
  comments: 'Seven emirates under British protection in Persian Gulf',
  created_date: 1752963079,
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

MERGE (c:Colony {colony_id: 'turks_and_caicos_islands_1799_ongoing'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Turks and Caicos Islands',
  colony_id: 'turks_and_caicos_islands_1799_ongoing',
  colony_type: 'Crown Colony',
  comments: 'Separated from Bahamas, still British Overseas Territory',
  created_date: 1752962972,
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

MERGE (c:Colony {colony_id: 'uganda_1894_1962'})
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

MERGE (c:Colony {colony_id: 'unfederated_malay_states_1909_1946'})
SET c += {
  administrative_status: 'Protectorate',
  canonical_name: 'Unfederated Malay States',
  colony_id: 'unfederated_malay_states_1909_1946',
  colony_type: 'Protectorate',
  comments: 'Johor, Kedah, Kelantan, Terengganu, Perlis under British protection',
  created_date: 1752967216,
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

MERGE (c:Colony:Dominion:Federation {colony_id: 'union_of_south_africa_1910_1961'})
SET c += {
  administrative_status: 'Dominion',
  canonical_name: 'Union of South Africa',
  colony_id: 'union_of_south_africa_1910_1961',
  colony_type: 'Dominion',
  comments: 'Self-governing dominion formed from four colonies, became Republic 1961',
  coordinates_source: 'wikidata',
  created_date: 1752962407,
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
  spatial_updated: 1753058508386,
  start_date: '1910-05-31',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:59.661000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['ZA'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q193619'
};

MERGE (c:Colony {colony_id: 'united_colony_of_bc_1866_1871'})
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

MERGE (c:Colony {colony_id: 'united_provinces_1877_1947'})
SET c += {
  administrative_status: 'Province',
  canonical_name: 'United Provinces',
  colony_id: 'united_provinces_1877_1947',
  colony_type: 'Province',
  comments: 'Formed from North-Western Provinces and Oudh, became Uttar Pradesh in India',
  created_date: 1752962006,
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

MERGE (c:Colony {colony_id: 'united_states_1776'})
SET c += {
  canonical_name: 'United States of America',
  colony_id: 'united_states_1776',
  established_year: 1776,
  region: 'North America',
  type: 'Independence',
  wikidata_id: 'Q30'
};

MERGE (c:Colony {colony_id: 'united_states_of_america_1783'})
SET c += {
  canonical_name: 'United States of America',
  colony_id: 'united_states_of_america_1783',
  colony_type: 'Former Colony (Independent)',
  established_year: 1783,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q30'
};

MERGE (c:Colony {colony_id: 'upper_canada_1791_1841'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Upper Canada',
  colony_id: 'upper_canada_1791_1841',
  colony_type: 'Crown Colony',
  comments: 'Created by Constitutional Act 1791, merged into Province of Canada',
  created_date: 1752961518,
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

MERGE (c:Colony {colony_id: 'van_diemens_land_1803_1856'})
SET c += {
  administrative_status: 'Penal Colony',
  canonical_name: 'Van Diemen\'s Land',
  colony_id: 'van_diemens_land_1803_1856',
  colony_type: 'Penal Colony',
  comments: 'Separate colony from 1825, renamed to Tasmania 1856',
  created_date: 1752961788,
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

MERGE (c:Colony {colony_id: 'vancouver_island_1849_1866'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Colony of Vancouver Island',
  colony_id: 'vancouver_island_1849_1866',
  colony_type: 'Crown Colony',
  comments: 'Merged with mainland British Columbia colony',
  coordinates_source: 'wikidata',
  created_date: 1752961518,
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
  spatial_updated: 1753058508540,
  start_date: '1849-01-01',
  verified: true,
  verified_date: '2025-08-06T00:00:25.599000000+00:00',
  whg_aat_types: ['300387506'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q2510000'
};

MERGE (c:Colony {colony_id: 'victoria_colony_1851_1901'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Victoria (Colony)',
  colony_id: 'victoria_colony_1851_1901',
  colony_type: 'Crown Colony',
  comments: 'Separated from New South Wales due to gold rush, gained self-government 1855',
  created_date: 1752961788,
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

MERGE (c:Colony {colony_id: 'virginia_colony_1607_1783'})
SET c += {
  administrative_status: 'Royal Colony',
  canonical_name: 'Virginia Colony',
  colony_id: 'virginia_colony_1607_1783',
  colony_type: 'Royal Colony',
  comments: 'First permanent English settlement in North America, Jamestown',
  created_date: 1753013487,
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

MERGE (c:Colony {colony_id: 'vostok_island_1866_1979'})
SET c += {
  administrative_status: 'Guano Island',
  canonical_name: 'Vostok Island',
  colony_id: 'vostok_island_1866_1979',
  colony_type: 'Guano Island',
  comments: 'Line Islands guano mining, transferred to Kiribati',
  created_date: 1753010772,
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

MERGE (c:Colony {colony_id: 'weihaiwei_1898_1930'})
SET c += {
  administrative_status: 'Leased Territory',
  canonical_name: 'Weihaiwei',
  colony_id: 'weihaiwei_1898_1930',
  colony_type: 'Leased Territory',
  comments: 'Chinese territory leased to Britain as naval base in Shandong',
  created_date: 1752967315,
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

MERGE (c:Colony {colony_id: 'west_florida_1763_1783'})
SET c += {
  colony_id: 'west_florida_1763_1783',
  established_year: 1763,
  independence_year: 1783,
  name: 'West Florida',
  region: 'North America',
  type: 'Crown Colony',
  wikidata_id: 'Q4971241'
};

MERGE (c:Colony:Federation {colony_id: 'west_indies_federation_1958_1962'})
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

MERGE (c:Colony {colony_id: 'western_australia_1832_1901'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Western Australia',
  colony_id: 'western_australia_1832_1901',
  colony_type: 'Crown Colony',
  comments: 'Swan River Colony renamed, gained self-government 1890',
  coordinates_source: 'wikidata',
  created_date: 1752961788,
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
  spatial_updated: 1753058508603,
  start_date: '1832-01-01',
  verification_method: 'mcp_wikidata_review',
  verified: true,
  verified_date: '2026-03-06T13:31:56.461000000+00:00',
  whg_aat_types: ['300387506'],
  whg_ccodes: ['AU'],
  whg_fclasses: ['A'],
  wikidata_id: 'Q3206'
};

MERGE (c:Colony {colony_id: 'western_samoa_1920_1962'})
SET c += {
  administrative_status: 'Mandate',
  canonical_name: 'Western Samoa',
  colony_id: 'western_samoa_1920_1962',
  colony_type: 'Mandate',
  comments: 'Former German Samoa under New Zealand administration',
  created_date: 1752963190,
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

MERGE (c:Colony {colony_id: 'yukon_territory_1898'})
SET c += {
  canonical_name: 'Yukon Territory',
  colony_id: 'yukon_territory_1898',
  colony_type: 'Territory',
  established_year: 1898,
  region: 'North America',
  verified: true,
  wikidata_id: 'Q2009'
};

MERGE (c:Colony {colony_id: 'zanzibar_1890_1963'})
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

MERGE (c:Colony {colony_id: 'zanzibar_independent_1963_1964'})
SET c += {
  administrative_status: 'Independence',
  canonical_name: 'Zanzibar (Independent)',
  colony_id: 'zanzibar_independent_1963_1964',
  colony_type: 'Independence',
  comments: 'Independent Zanzibar before union with Tanganyika',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'zimbabwe_rhodesia_1979_1979'})
SET c += {
  administrative_status: 'Transitional',
  canonical_name: 'Zimbabwe Rhodesia',
  colony_id: 'zimbabwe_rhodesia_1979_1979',
  colony_type: 'Transitional',
  comments: 'Brief internal settlement before Lancaster House Agreement',
  created_date: 1752962811,
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

MERGE (c:Colony {colony_id: 'zululand_1887_1897'})
SET c += {
  administrative_status: 'Crown Colony',
  canonical_name: 'Zululand',
  colony_id: 'zululand_1887_1897',
  colony_type: 'Crown Colony',
  comments: 'Incorporated into Colony of Natal 1897',
  coordinates_source: 'wikidata',
  created_date: 1752962407,
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
  spatial_updated: 1753058508336,
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

MATCH (a:Colony {colony_id: 'acadia_french_1604_1713'}), (b:Colony {colony_id: 'nova_scotia_pre_1713_1784'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'aden_1839_1963'}), (b:Colony {colony_id: 'aden_colony_1937_1967'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'aden_colony_1937_1967'}), (b:Colony {colony_id: 'south_yemen_1967_1990'}) MERGE (a)-[:EVOLVED_INTO {description: 'Aden became part of independent South Yemen', relationship_type: 'BECAME_INDEPENDENT', year: 1967}]->(b);
MATCH (a:Colony {colony_id: 'aden_protectorate_1839_1967'}), (b:Colony {colony_id: 'south_yemen_1967_1990'}) MERGE (a)-[:EVOLVED_INTO {description: 'Aden Protectorate became part of independent South Yemen', relationship_type: 'BECAME_INDEPENDENT', year: 1967}]->(b);
MATCH (a:Colony {colony_id: 'ajmer_merwara_1818_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'alberta_1905'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'andaman_and_nicobar_islands_1789_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'anguilla_1650_ongoing'}), (b:Colony {colony_id: 'stkitts_nevis_anguilla_1816_1833'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1833, start_year: 1816}]->(b);
MATCH (a:Colony {colony_id: 'antigua_colony_1632_1981'}), (b:Colony {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'antigua_montserrat_barbuda_1816_1833'}), (b:Colony {colony_id: 'federal_colony_leeward_islands_1833-1960'}) MERGE (a)-[:EVOLVED_INTO {relationship_type: 'MERGED_INTO', year: 1833}]->(b);
MATCH (a:Colony {colony_id: 'ascension_island_1815_ongoing'}), (b:Colony {colony_id: 'south_african_republic_restored_1881_1900'}) MERGE (a)-[:NEAR_COAST_OF {created_date: 1753093190044, relationship_type: 'coastal_proximity', source: 'comprehensive_coastal'}]->(b);
MATCH (a:Colony {colony_id: 'assam_bengal_presidency_1826_1874'}), (b:Colony {colony_id: 'assam_province_1874_1905'}) MERGE (a)-[:EVOLVED_INTO {description: 'Assam was separated from the Bengal Presidency to become a Chief Commissioner\'s Province.', relationship_type: 'REORGANIZED_AS', year: 1874}]->(b);
MATCH (a:Colony {colony_id: 'assam_province_1874_1905'}), (b:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'}) MERGE (a)-[:EVOLVED_INTO {description: 'Assam merged with Eastern Bengal during partition', relationship_type: 'MERGED_INTO', year: 1905}]->(b);
MATCH (a:Colony {colony_id: 'assam_province_1874_1905'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'assam_province_1874_1905'}), (b:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Assam separated from Bengal Presidency as chief commissionership', relationship_type: 'CARVED_OUT', succession_type: 'COMPLEX_SUCCESSION', year: 1874}]->(b);
MATCH (a:Colony {colony_id: 'assam_province_1874_1905'}), (b:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Assam separated again as chief commissionership', relationship_type: 'SEPARATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1912}]->(b);
MATCH (a:Colony {colony_id: 'assam_province_restored_1912_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO {description: 'Most of Assam joined the Dominion of India.', relationship_type: 'PARTITIONED_TO', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'assam_province_restored_1912_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'baluchistan_1877_1947'}), (b:Colony {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'baluchistan_1877_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'barbados_colony_1627_1966'}), (b:Colony {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF {description: 'Barbados served as the administrative headquarters of the British Windward Islands during this period.', end_year: 1885, start_year: 1833}]->(b);
MATCH (a:Colony {colony_id: 'bengal_presidency_company_1757_1858'}), (b:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:EVOLVED_INTO {description: 'Crown took over after Indian Rebellion 1857', relationship_type: 'TRANSFERRED_TO_CROWN', year: 1858}]->(b);
MATCH (a:Colony {colony_id: 'bengal_presidency_company_1757_1858'}), (b:Colony {colony_id: 'assam_bengal_presidency_1826_1874'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:Colony {colony_id: 'assam_province_1874_1905'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:Colony {colony_id: 'bengal_province_partitioned_1905_1912'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:Colony {colony_id: 'bihar_and_orissa_1912_1947'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}), (b:Colony {colony_id: 'bengal_presidency_company_1757_1858'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Crown took over after Indian Rebellion 1857', relationship_type: 'TRANSFERRED_TO_CROWN', succession_type: 'DIRECT_SUCCESSION', year: 1858}]->(b);
MATCH (a:Colony {colony_id: 'bengal_province_partitioned_1905_1912'}), (b:Colony {colony_id: 'bengal_province_reunited_1912_1947'}) MERGE (a)-[:EVOLVED_INTO {description: 'Bengal reunited due to Swadeshi movement protests', relationship_type: 'REUNITED_INTO', year: 1912}]->(b);
MATCH (a:Colony {colony_id: 'bengal_province_partitioned_1905_1912'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'bengal_province_partitioned_1905_1912'}), (b:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Bengal partitioned by Curzon - western part', relationship_type: 'PARTITIONED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1905}]->(b);
MATCH (a:Colony {colony_id: 'bengal_province_reunited_1912_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'bengal_province_reunited_1912_1947'}), (b:Colony {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'bengal_province_reunited_1912_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'berbice_colony_1803_1831'}), (b:Colony {colony_id: 'british_guiana_1831_1966'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'bihar_and_orissa_1912_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO {description: 'Bihar and Orissa joined India', relationship_type: 'JOINED', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'bihar_and_orissa_1912_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'bihar_and_orissa_1912_1947'}), (b:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Bihar and Orissa separated from Bengal during reorganization', relationship_type: 'CARVED_OUT', succession_type: 'COMPLEX_SUCCESSION', year: 1912}]->(b);
MATCH (a:Colony {colony_id: 'bombay_presidency_company_1687_1858'}), (b:Colony {colony_id: 'bombay_presidency_crown_1858_1947'}) MERGE (a)-[:EVOLVED_INTO {description: 'Crown took over after Indian Rebellion 1857', relationship_type: 'TRANSFERRED_TO_CROWN', year: 1858}]->(b);
MATCH (a:Colony {colony_id: 'bombay_presidency_crown_1858_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO {description: 'Bombay Presidency joined India', relationship_type: 'JOINED', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'bombay_presidency_crown_1858_1947'}), (b:Colony {colony_id: 'sind_province_1843_1947'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'bombay_presidency_crown_1858_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'bombay_presidency_crown_1858_1947'}), (b:Colony {colony_id: 'bombay_presidency_company_1687_1858'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Crown took over after Indian Rebellion 1857', relationship_type: 'TRANSFERRED_TO_CROWN', succession_type: 'DIRECT_SUCCESSION', year: 1858}]->(b);
MATCH (a:Colony {colony_id: 'british_bechuanaland_1885_1895'}), (b:Colony {colony_id: 'cape_colony_british_1806_1910'}) MERGE (a)-[:EVOLVED_INTO {description: 'British Bechuanaland incorporated into Cape Colony', relationship_type: 'INCORPORATED_INTO', year: 1895}]->(b);
MATCH (a:Colony {colony_id: 'british_central_africa_protectorate_1891_1907'}), (b:Colony {colony_id: 'nyasaland_1891_1964'}) MERGE (a)-[:EVOLVED_INTO {description: 'British Central Africa Protectorate renamed to Nyasaland', relationship_type: 'RENAMED_TO', year: 1907}]->(b);
MATCH (a:Colony {colony_id: 'british_columbia_province_1871'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'british_gold_coast_1821_1874'}), (b:Colony {colony_id: 'gold_coast_colony_1874_1957'}) MERGE (a)-[:EVOLVED_INTO {description: 'The British Gold Coast was formally established as the Gold Coast Crown Colony, with an administration separate from Sierra Leone.', relationship_type: 'REORGANIZED_AS', year: 1874}]->(b);
MATCH (a:Colony {colony_id: 'british_gold_coast_1821_1874'}), (b:Colony {colony_id: 'cape_coast_castle_1664_1821'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Trading posts taken over by Crown administration', relationship_type: 'REORGANIZED_AS', succession_type: 'DIRECT_SUCCESSION', year: 1821}]->(b);
MATCH (a:Colony {colony_id: 'british_guiana_1831_1966'}), (b:Colony {colony_id: 'trinidad_and_tobago_1889_1962'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753058509160, relationship_type: 'land_border', source: 'historical_borders'}]->(b);
MATCH (a:Colony {colony_id: 'british_honduras_1862_1981'}), (b:Colony {colony_id: 'jamaica_1655_1962'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753058509152, relationship_type: 'land_border', source: 'historical_borders'}]->(b);
MATCH (a:Colony {colony_id: 'british_new_guinea_1884_1906'}), (b:Colony {colony_id: 'territory_of_papua_1906_1949'}) MERGE (a)-[:EVOLVED_INTO {description: 'British New Guinea transferred to Australian administration', relationship_type: 'TRANSFERRED_TO_AUSTRALIA', year: 1906}]->(b);
MATCH (a:Colony {colony_id: 'british_north_borneo_1882_1946'}), (b:Colony {colony_id: 'north_borneo_crown_colony_1946_1963'}) MERGE (a)-[:EVOLVED_INTO {description: 'Company territory became Crown Colony', relationship_type: 'BECAME_CROWN_COLONY', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'british_somaliland_1884_1960'}), (b:Colony {colony_id: 'somali_republic_1960'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'british_south_africa_company_territory_1889_1923'}), (b:Colony {colony_id: 'northern_rhodesia_colony_1924_1953'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'british_south_africa_company_territory_1889_1923'}), (b:Colony {colony_id: 'southern_rhodesia_colony_1923_1953'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'british_virgin_islands_1672_ongoing'}), (b:Colony {colony_id: 'stkitts_nevis_anguilla_1816_1833'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1833, start_year: 1816}]->(b);
MATCH (a:Colony {colony_id: 'burma_british_india_1886_1937'}), (b:Colony {colony_id: 'burma_separate_colony_1937_1948'}) MERGE (a)-[:EVOLVED_INTO {description: 'Burma separated from British India as separate crown colony', relationship_type: 'SEPARATED_FROM_INDIA', year: 1937}]->(b);
MATCH (a:Colony {colony_id: 'burma_british_india_1886_1937'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}), (b:Colony {colony_id: 'canada_independent_1931'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}), (b:Colony {colony_id: 'new_brunswick_1784_1867'}) MERGE (a)-[:SUCCESSOR_TO {description: 'New Brunswick joined Confederation as founding province', relationship_type: 'CONFEDERATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1867}]->(b);
MATCH (a:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}), (b:Colony {colony_id: 'province_of_canada_1841_1867'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Province of Canada split into Ontario and Quebec, joined Confederation as Dominion of Canada', relationship_type: 'CONFEDERATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1867}]->(b);
MATCH (a:Colony {colony_id: 'cape_breton_colony_1784_1820'}), (b:Colony {colony_id: 'nova_scotia_post_1784_1867'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'cape_coast_castle_1664_1821'}), (b:Colony {colony_id: 'british_gold_coast_1821_1874'}) MERGE (a)-[:EVOLVED_INTO {description: 'Trading posts taken over by Crown administration', relationship_type: 'REORGANIZED_AS', year: 1821}]->(b);
MATCH (a:Colony {colony_id: 'cape_colony_british_1795_1803_1795_1803'}), (b:Colony {colony_id: 'cape_colony_dutch_restored_1803_1806'}) MERGE (a)-[:EVOLVED_INTO {description: 'Cape returned to Dutch under Treaty of Amiens', relationship_type: 'RETURNED_TO', year: 1803}]->(b);
MATCH (a:Colony {colony_id: 'cape_colony_british_1806_1910'}), (b:Colony {colony_id: 'union_of_south_africa_1910_1961'}) MERGE (a)-[:EVOLVED_INTO {description: 'Cape Colony joined Union of South Africa as Cape Province', relationship_type: 'FEDERATED_INTO', year: 1910}]->(b);
MATCH (a:Colony {colony_id: 'cape_colony_british_1806_1910'}), (b:Colony {colony_id: 'british_bechuanaland_1885_1895'}) MERGE (a)-[:SUCCESSOR_TO {description: 'British Bechuanaland incorporated into Cape Colony', relationship_type: 'INCORPORATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1895}]->(b);
MATCH (a:Colony {colony_id: 'cape_colony_british_1806_1910'}), (b:Colony {colony_id: 'griqualand_west_1871_1880'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Griqualand West incorporated into Cape Colony', relationship_type: 'INCORPORATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1880}]->(b);
MATCH (a:Colony {colony_id: 'cape_colony_dutch_1652_1795'}), (b:Colony {colony_id: 'cape_colony_british_1795_1803_1795_1803'}) MERGE (a)-[:EVOLVED_INTO {description: 'British conquered Cape Colony during French Revolutionary Wars', relationship_type: 'CONQUERED_BY', year: 1795}]->(b);
MATCH (a:Colony {colony_id: 'cape_colony_dutch_restored_1803_1806'}), (b:Colony {colony_id: 'cape_colony_british_1806_1910'}) MERGE (a)-[:EVOLVED_INTO {description: 'British permanently conquered Cape Colony, confirmed 1815 Congress of Vienna', relationship_type: 'CONQUERED_BY', year: 1806}]->(b);
MATCH (a:Colony {colony_id: 'central_provinces_1861_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO {description: 'Central Provinces joined India', relationship_type: 'JOINED', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'central_provinces_1861_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}), (b:Colony {colony_id: 'northern_nigeria_1900_1914'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Northern and Southern Nigeria amalgamated by Lord Lugard', relationship_type: 'AMALGAMATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1914}]->(b);
MATCH (a:Colony {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}), (b:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Northern and Southern Nigeria amalgamated by Lord Lugard', relationship_type: 'AMALGAMATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1914}]->(b);
MATCH (a:Colony {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}), (b:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Southern and Northern Nigeria merged to form Nigeria', relationship_type: 'MERGED_WITH', succession_type: 'COMPLEX_SUCCESSION', year: '1914'}]->(b);
MATCH (a:Colony {colony_id: 'colony_of_natal_1843_1910'}), (b:Colony {colony_id: 'union_of_south_africa_1910_1961'}) MERGE (a)-[:EVOLVED_INTO {description: 'Natal joined Union of South Africa as Natal Province', relationship_type: 'FEDERATED_INTO', year: 1910}]->(b);
MATCH (a:Colony {colony_id: 'colony_of_natal_1843_1910'}), (b:Colony {colony_id: 'zululand_1887_1897'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Zululand incorporated into Colony of Natal', relationship_type: 'INCORPORATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1897}]->(b);
MATCH (a:Colony {colony_id: 'colony_of_newfoundland_1610_1949'}), (b:Colony {colony_id: 'dominion_of_newfoundland_1907_1934'}) MERGE (a)-[:EVOLVED_INTO {year: 1907}]->(b);
MATCH (a:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}), (b:Colony {colony_id: 'australia_independent_1942'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}), (b:Colony {colony_id: 'new_south_wales_original_1788_1901'}) MERGE (a)-[:SUCCESSOR_TO {description: 'New South Wales joined Australian federation', relationship_type: 'FEDERATION_SUCCESSION', succession_type: 'FEDERATION_SUCCESSION', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}), (b:Colony {colony_id: 'queensland_1859_1901'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Queensland joined Australian federation', relationship_type: 'FEDERATION_SUCCESSION', succession_type: 'FEDERATION_SUCCESSION', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}), (b:Colony {colony_id: 'victoria_colony_1851_1901'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Victoria joined Australian federation', relationship_type: 'FEDERATION_SUCCESSION', succession_type: 'FEDERATION_SUCCESSION', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'connecticut_colony_1636_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'connecticut_colony_1636_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'coorg_province_1834_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'delaware_colony_1664_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'delaware_colony_1664_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'demerara_colony_1803_1831'}), (b:Colony {colony_id: 'british_guiana_1831_1966'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'dominica_colony_1763_1978'}), (b:Colony {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'dominica_colony_1763_1978'}), (b:Colony {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1959, start_year: 1940}]->(b);
MATCH (a:Colony {colony_id: 'dominion_of_india_1947_1950'}), (b:Colony {colony_id: 'bengal_province_reunited_1912_1947'}) MERGE (a)-[:SUCCESSOR_TO {description: 'West Bengal to India', relationship_type: 'PARTITIONED_TO', succession_type: 'COMPLEX_SUCCESSION', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'dominion_of_india_1947_1950'}), (b:Colony {colony_id: 'punjab_province_1849_1947'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Eastern Punjab to India', relationship_type: 'PARTITIONED_TO', succession_type: 'COMPLEX_SUCCESSION', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'dominion_of_new_zealand_1907_1947'}), (b:Colony {colony_id: 'new_zealand_independent_1947'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'dominion_of_newfoundland_1907_1934'}), (b:Colony {colony_id: 'newfoundland_commission_1934_1949'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'dominion_of_newfoundland_1907_1934'}), (b:Colony {colony_id: 'newfoundland_province_1949'}) MERGE (a)-[:EVOLVED_INTO {year: 1949}]->(b);
MATCH (a:Colony {colony_id: 'dominion_of_pakistan_1947_1956'}), (b:Colony {colony_id: 'bengal_province_reunited_1912_1947'}) MERGE (a)-[:SUCCESSOR_TO {description: 'East Bengal to Pakistan', relationship_type: 'PARTITIONED_TO', succession_type: 'COMPLEX_SUCCESSION', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'dominion_of_pakistan_1947_1956'}), (b:Colony {colony_id: 'punjab_province_1849_1947'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Western Punjab to Pakistan', relationship_type: 'PARTITIONED_TO', succession_type: 'COMPLEX_SUCCESSION', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'east_africa_protectorate_1895_1920'}), (b:Colony {colony_id: 'kenya_colony_and_protectorate_of_1920_1963'}) MERGE (a)-[:EVOLVED_INTO {description: 'East Africa Protectorate became Kenya Colony and Protectorate', relationship_type: 'BECAME_COLONY', year: 1920}]->(b);
MATCH (a:Colony {colony_id: 'east_africa_protectorate_1895_1920'}), (b:Colony {colony_id: 'imperial_british_east_africa_company_territory_1888_1895'}) MERGE (a)-[:SUCCESSOR_TO {description: 'IBEA Company territory became Crown protectorate due to financial difficulties', relationship_type: 'BECAME_PROTECTORATE', succession_type: 'DIRECT_SUCCESSION', year: 1895}]->(b);
MATCH (a:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:Colony {colony_id: 'assam_province_1874_1905'}) MERGE (a)-[:EVOLVED_INTO {description: 'Assam separated again as chief commissionership', relationship_type: 'SEPARATED_INTO', year: 1912}]->(b);
MATCH (a:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:Colony {colony_id: 'assam_province_restored_1912_1947'}) MERGE (a)-[:EVOLVED_INTO {relationship_type: 'SEPARATED_FROM', year: 1912}]->(b);
MATCH (a:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:Colony {colony_id: 'bengal_province_reunited_1912_1947'}) MERGE (a)-[:EVOLVED_INTO {description: 'Eastern Bengal reunited with western Bengal', relationship_type: 'REUNITED_INTO', year: 1912}]->(b);
MATCH (a:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:Colony {colony_id: 'assam_province_1874_1905'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Assam merged with Eastern Bengal during partition', relationship_type: 'MERGED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1905}]->(b);
MATCH (a:Colony {colony_id: 'eastern_bengal_and_assam_1905_1912'}), (b:Colony {colony_id: 'bengal_presidency_crown_1858_1912'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Bengal partitioned by Curzon - eastern part with Assam', relationship_type: 'PARTITIONED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1905}]->(b);
MATCH (a:Colony {colony_id: 'ellice_islands_1976_1978'}), (b:Colony {colony_id: 'gilbert_and_ellice_islands_1916_1976'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Ellice Islands separated from Gilbert Islands', relationship_type: 'SEPARATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1976}]->(b);
MATCH (a:Colony {colony_id: 'essequibo_colony_1803_1831'}), (b:Colony {colony_id: 'british_guiana_1831_1966'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'factory_at_surat_1612_1857'}), (b:Colony {colony_id: 'bombay_presidency_company_1687_1858'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'federated_malay_states_1895_1946'}), (b:Colony {colony_id: 'malayan_union_1946_1948'}) MERGE (a)-[:EVOLVED_INTO {description: 'FMS incorporated into Malayan Union', relationship_type: 'INCORPORATED_INTO', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'federation_of_malaya_1948_1957'}), (b:Colony {colony_id: 'malaya_independent_1957_1963'}) MERGE (a)-[:EVOLVED_INTO {description: 'Federation of Malaya gained independence', relationship_type: 'BECAME_INDEPENDENT', year: 1957}]->(b);
MATCH (a:Colony {colony_id: 'federation_of_malaya_1948_1957'}), (b:Colony {colony_id: 'malayan_union_1946_1948'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Malayan Union reorganized as Federation due to opposition', relationship_type: 'REORGANIZED_AS', succession_type: 'DIRECT_SUCCESSION', year: 1948}]->(b);
MATCH (a:Colony {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}), (b:Colony {colony_id: 'northern_rhodesia_post_federation_1964'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}), (b:Colony {colony_id: 'nyasaland_post_federation_1963'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}), (b:Colony {colony_id: 'southern_rhodesia_post_federation_1963'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'fort_william_calcutta_1696_1857'}), (b:Colony {colony_id: 'bengal_presidency_company_1757_1858'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'gambia_colony_1816_1888'}), (b:Colony {colony_id: 'gambia_colony_and_protectorate_1816_1965'}) MERGE (a)-[:EVOLVED_INTO {description: 'The original colony was expanded with the addition of a protectorate over the Gambian hinterland.', relationship_type: 'EXPANDED_WITH_PROTECTORATE', year: 1888}]->(b);
MATCH (a:Colony {colony_id: 'gambia_colony_1816_1888'}), (b:Colony {colony_id: 'james_island_trading_post_1661_1816'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Trading post reorganized as Crown Colony', relationship_type: 'REORGANIZED_AS', succession_type: 'DIRECT_SUCCESSION', year: 1816}]->(b);
MATCH (a:Colony {colony_id: 'georgia_colony_1732_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'georgia_colony_1732_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'german_east_africa_british_occupied_1916_1922'}), (b:Colony {colony_id: 'tanganyika_territory_1922_1961'}) MERGE (a)-[:EVOLVED_INTO {description: 'German East Africa became League of Nations mandate territory', relationship_type: 'BECAME_MANDATE', year: 1922}]->(b);
MATCH (a:Colony {colony_id: 'gilbert_and_ellice_islands_1916_1976'}), (b:Colony {colony_id: 'ellice_islands_1976_1978'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'gilbert_and_ellice_islands_1916_1976'}), (b:Colony {colony_id: 'gilbert_islands_1976_1979'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'gilbert_islands_1976_1979'}), (b:Colony {colony_id: 'gilbert_and_ellice_islands_1916_1976'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Gilbert Islands separated from Ellice Islands', relationship_type: 'SEPARATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1976}]->(b);
MATCH (a:Colony {colony_id: 'gold_coast_colony_1874_1957'}), (b:Colony {colony_id: 'ashanti_1901_1957'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:Colony {colony_id: 'gold_coast_colony_1874_1957'}), (b:Colony {colony_id: 'british_togoland_1919_1957'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:Colony {colony_id: 'gold_coast_colony_1874_1957'}), (b:Colony {colony_id: 'northern_territories_gold_coast_1897_1957'}) MERGE (a)-[:ADMINISTERED_UNDER]->(b);
MATCH (a:Colony {colony_id: 'gold_coast_colony_1874_1957'}), (b:Colony {colony_id: 'british_gold_coast_1821_1874'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Formal colony established after Ashanti conquest', relationship_type: 'REORGANIZED_AS', succession_type: 'DIRECT_SUCCESSION', year: 1874}]->(b);
MATCH (a:Colony {colony_id: 'grenada_colony_1763_1974'}), (b:Colony {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'grenada_colony_1763_1974'}), (b:Colony {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1959, start_year: 1833}]->(b);
MATCH (a:Colony {colony_id: 'griqualand_west_1871_1880'}), (b:Colony {colony_id: 'cape_colony_british_1806_1910'}) MERGE (a)-[:EVOLVED_INTO {description: 'Griqualand West incorporated into Cape Colony', relationship_type: 'INCORPORATED_INTO', year: 1880}]->(b);
MATCH (a:Colony {colony_id: 'ile_royale_1713_1763'}), (b:Colony {colony_id: 'nova_scotia_pre_1713_1784'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'ile_royale_1713_1763'}), (b:Colony {colony_id: 'new_france_1608_1763'}) MERGE (a)-[:PART_OF {created_date: 1753030225686, end_year: 1763, start_year: 1713}]->(b);
MATCH (a:Colony {colony_id: 'imperial_british_east_africa_company_territory_1888_1895'}), (b:Colony {colony_id: 'east_africa_protectorate_1895_1920'}) MERGE (a)-[:EVOLVED_INTO {description: 'The territory was transferred from the bankrupt IBEA Company to direct British government control.', relationship_type: 'BECAME_PROTECTORATE', year: 1895}]->(b);
MATCH (a:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}), (b:Colony {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'ireland_uk_1801_1922'}), (b:Colony {colony_id: 'irish_free_state_1922_1937'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'ireland_uk_1801_1922'}), (b:Colony {colony_id: 'northern_ireland_1920'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'isle_de_france_british_occupation_1810_1814'}), (b:Colony {colony_id: 'mauritius_1814_1968'}) MERGE (a)-[:EVOLVED_INTO {description: 'Isle de France became British Crown Colony of Mauritius', relationship_type: 'BECAME_CROWN_COLONY', year: 1814}]->(b);
MATCH (a:Colony {colony_id: 'jamaica_1655_1962'}), (b:Colony {colony_id: 'british_honduras_1862_1981'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753058509152, relationship_type: 'land_border', source: 'historical_borders'}]->(b);
MATCH (a:Colony {colony_id: 'jamaica_1655_1962'}), (b:Colony {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'james_island_trading_post_1661_1816'}), (b:Colony {colony_id: 'gambia_colony_1816_1888'}) MERGE (a)-[:EVOLVED_INTO {description: 'Trading post reorganized as Crown Colony', relationship_type: 'REORGANIZED_AS', year: 1816}]->(b);
MATCH (a:Colony {colony_id: 'kenya_colony_and_protectorate_of_1920_1963'}), (b:Colony {colony_id: 'east_africa_protectorate_1895_1920'}) MERGE (a)-[:SUCCESSOR_TO {description: 'East Africa Protectorate became Kenya Colony and Protectorate', relationship_type: 'BECAME_COLONY', succession_type: 'DIRECT_SUCCESSION', year: 1920}]->(b);
MATCH (a:Colony {colony_id: 'kingdom_of_ireland_1541_1801'}), (b:Colony {colony_id: 'ireland_uk_1801_1922'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'labuan_1846_1963'}), (b:Colony {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'lagos_protectorate_1887_1906'}), (b:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'leeward_islands_colony_1671_1816'}), (b:Colony {colony_id: 'antigua_montserrat_barbuda_1816_1833'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'leeward_islands_colony_1671_1816'}), (b:Colony {colony_id: 'stkitts_nevis_anguilla_1816_1833'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'lower_burma_1824_1886'}), (b:Colony {colony_id: 'burma_british_india_1886_1937'}) MERGE (a)-[:EVOLVED_INTO {relationship_type: 'CONSOLIDATED_AS_PROVINCE', year: 1886}]->(b);
MATCH (a:Colony {colony_id: 'lower_canada_1791_1841'}), (b:Colony {colony_id: 'new_brunswick_1784_1867'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753058509072, relationship_type: 'land_border', source: 'historical_borders'}]->(b);
MATCH (a:Colony {colony_id: 'lower_canada_1791_1841'}), (b:Colony {colony_id: 'upper_canada_1791_1841'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753058509064, relationship_type: 'land_border', source: 'historical_borders'}]->(b);
MATCH (a:Colony {colony_id: 'lower_canada_1791_1841'}), (b:Colony {colony_id: 'province_of_canada_1841_1867'}) MERGE (a)-[:EVOLVED_INTO {description: 'Lower Canada merged with Upper Canada to form Province of Canada (Act of Union 1840)', relationship_type: 'MERGED_INTO', year: 1841}]->(b);
MATCH (a:Colony {colony_id: 'madras_presidency_company_1640_1858'}), (b:Colony {colony_id: 'madras_presidency_crown_1858_1947'}) MERGE (a)-[:EVOLVED_INTO {description: 'Crown took over after Indian Rebellion 1857', relationship_type: 'TRANSFERRED_TO_CROWN', year: 1858}]->(b);
MATCH (a:Colony {colony_id: 'madras_presidency_crown_1858_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO {description: 'Madras Presidency joined India', relationship_type: 'JOINED', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'madras_presidency_crown_1858_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'madras_presidency_crown_1858_1947'}), (b:Colony {colony_id: 'madras_presidency_company_1640_1858'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Crown took over after Indian Rebellion 1857', relationship_type: 'TRANSFERRED_TO_CROWN', succession_type: 'DIRECT_SUCCESSION', year: 1858}]->(b);
MATCH (a:Colony {colony_id: 'mainland_british_columbia_1858_1866'}), (b:Colony {colony_id: 'united_colony_of_bc_1866_1871'}) MERGE (a)-[:EVOLVED_INTO {relationship_type: 'MERGED_INTO', year: 1866}]->(b);
MATCH (a:Colony {colony_id: 'mainland_british_columbia_1858_1866'}), (b:Colony {colony_id: 'vancouver_island_1849_1866'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Vancouver Island merged with mainland British Columbia colony', relationship_type: 'MERGED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1866}]->(b);
MATCH (a:Colony {colony_id: 'malacca_settlement_1824_1826'}), (b:Colony {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:EVOLVED_INTO {description: 'Malacca incorporated into Straits Settlements', relationship_type: 'INCORPORATED_INTO', year: 1826}]->(b);
MATCH (a:Colony {colony_id: 'malaya_independent_1957_1963'}), (b:Colony {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'malayan_union_1946_1948'}), (b:Colony {colony_id: 'federation_of_malaya_1948_1957'}) MERGE (a)-[:EVOLVED_INTO {description: 'Malayan Union reorganized as Federation due to opposition', relationship_type: 'REORGANIZED_AS', year: 1948}]->(b);
MATCH (a:Colony {colony_id: 'malayan_union_1946_1948'}), (b:Colony {colony_id: 'federated_malay_states_1895_1946'}) MERGE (a)-[:SUCCESSOR_TO {description: 'FMS incorporated into Malayan Union', relationship_type: 'INCORPORATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'malayan_union_1946_1948'}), (b:Colony {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Penang and Malacca joined Malayan Union', relationship_type: 'INCORPORATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'malayan_union_1946_1948'}), (b:Colony {colony_id: 'unfederated_malay_states_1909_1946'}) MERGE (a)-[:SUCCESSOR_TO {description: 'UMS incorporated into Malayan Union', relationship_type: 'INCORPORATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'malaysia_1963'}), (b:Colony {colony_id: 'singapore_independent_1965'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'mandatory_iraq_1920_1932'}), (b:Colony {colony_id: 'iraq_1932_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'Iraq became first Arab state independent from mandate', relationship_type: 'BECAME_INDEPENDENT', year: 1932}]->(b);
MATCH (a:Colony {colony_id: 'mandatory_iraq_1920_1932'}), (b:Colony {colony_id: 'mesopotamia_british_occupied_1914_1920'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Mesopotamia became League of Nations mandate', relationship_type: 'BECAME_MANDATE', succession_type: 'DIRECT_SUCCESSION', year: 1920}]->(b);
MATCH (a:Colony {colony_id: 'maryland_colony_1634_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'maryland_colony_1634_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'massachusetts_bay_colony_1630_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'massachusetts_bay_colony_1630_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'mauritius_1814_1968'}), (b:Colony {colony_id: 'isle_de_france_british_occupation_1810_1814'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Isle de France became British Crown Colony of Mauritius', relationship_type: 'BECAME_CROWN_COLONY', succession_type: 'DIRECT_SUCCESSION', year: 1814}]->(b);
MATCH (a:Colony {colony_id: 'mesopotamia_british_occupied_1914_1920'}), (b:Colony {colony_id: 'mandatory_iraq_1920_1932'}) MERGE (a)-[:EVOLVED_INTO {description: 'Mesopotamia became League of Nations mandate', relationship_type: 'BECAME_MANDATE', year: 1920}]->(b);
MATCH (a:Colony {colony_id: 'minorca_first_1708_1756'}), (b:Colony {colony_id: 'minorca_second_1763_1782'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'minorca_second_1763_1782'}), (b:Colony {colony_id: 'minorca_third_1798_1802'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'montserrat_1632_ongoing'}), (b:Colony {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'montserrat_1632_ongoing'}), (b:Colony {colony_id: 'antigua_montserrat_barbuda_1816_1833'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1833, start_year: 1816}]->(b);
MATCH (a:Colony {colony_id: 'natalia_republic_1839_1843'}), (b:Colony {colony_id: 'colony_of_natal_1843_1910'}) MERGE (a)-[:EVOLVED_INTO {description: 'Britain annexed Natalia Republic as Colony of Natal', relationship_type: 'ANNEXED_BY', year: 1843}]->(b);
MATCH (a:Colony {colony_id: 'new_brunswick_1784_1867'}), (b:Colony {colony_id: 'lower_canada_1791_1841'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753058509072, relationship_type: 'land_border', source: 'historical_borders'}]->(b);
MATCH (a:Colony {colony_id: 'new_brunswick_1784_1867'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'New Brunswick joined Confederation as founding province', relationship_type: 'CONFEDERATED_INTO', year: 1867}]->(b);
MATCH (a:Colony {colony_id: 'new_brunswick_1784_1867'}), (b:Colony {colony_id: 'new_brunswick_province_1867'}) MERGE (a)-[:EVOLVED_INTO {year: 1867}]->(b);
MATCH (a:Colony {colony_id: 'new_brunswick_province_1867'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'new_france_1608_1763'}), (b:Colony {colony_id: 'province_of_quebec_british_1763_1791'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'new_france_1608_1763'}), (b:Colony {colony_id: 'province_of_quebec_british_1763_1791'}) MERGE (a)-[:TRANSFERRED_TERRITORY {created_date: 1753030225718, year: 1763}]->(b);
MATCH (a:Colony {colony_id: 'new_hampshire_colony_1623_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'new_hampshire_colony_1623_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'new_jersey_colony_1664_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'new_jersey_colony_1664_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'new_south_wales_original_1788_1901'}), (b:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'New South Wales joined Federation as founding state', relationship_type: 'FEDERATED_INTO', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'new_south_wales_original_1788_1901'}), (b:Colony {colony_id: 'queensland_1859_1901'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'new_south_wales_original_1788_1901'}), (b:Colony {colony_id: 'van_diemens_land_1803_1856'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'new_south_wales_original_1788_1901'}), (b:Colony {colony_id: 'victoria_colony_1851_1901'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'new_york_colony_1664_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'new_york_colony_1664_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'new_zealand_colony_1840_1907'}), (b:Colony {colony_id: 'dominion_of_new_zealand_1907_1947'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'newfoundland_commission_1934_1949'}), (b:Colony {colony_id: 'canada_independent_1931'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'newfoundland_province_1949'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'niger_coast_protectorate_1893_1900'}), (b:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:EVOLVED_INTO {description: 'Niger Coast Protectorate reorganized as Southern Nigeria', relationship_type: 'REORGANIZED_AS', year: 1900}]->(b);
MATCH (a:Colony {colony_id: 'niger_coast_protectorate_1893_1900'}), (b:Colony {colony_id: 'oil_rivers_protectorate_1885_1893'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Oil Rivers Protectorate renamed to Niger Coast Protectorate', relationship_type: 'RENAMED_TO', succession_type: 'DIRECT_SUCCESSION', year: 1893}]->(b);
MATCH (a:Colony {colony_id: 'north_borneo_crown_colony_1946_1963'}), (b:Colony {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'north_borneo_crown_colony_1946_1963'}), (b:Colony {colony_id: 'british_north_borneo_1882_1946'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Company territory became Crown Colony', relationship_type: 'BECAME_CROWN_COLONY', succession_type: 'DIRECT_SUCCESSION', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'north_carolina_colony_1663_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'north_carolina_colony_1663_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'north_west_frontier_province_1901_1947'}), (b:Colony {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO {description: 'NWFP joined Pakistan', relationship_type: 'JOINED', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'north_west_frontier_province_1901_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'north_west_frontier_province_1901_1947'}), (b:Colony {colony_id: 'punjab_province_1849_1947'}) MERGE (a)-[:SUCCESSOR_TO {description: 'NWFP created from frontier districts of Punjab', relationship_type: 'CARVED_OUT', succession_type: 'COMPLEX_SUCCESSION', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'north_western_territory_1670_1870'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'northern_nigeria_1900_1914'}), (b:Colony {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}) MERGE (a)-[:EVOLVED_INTO {description: 'Northern and Southern Nigeria amalgamated by Lord Lugard', relationship_type: 'AMALGAMATED_INTO', year: 1914}]->(b);
MATCH (a:Colony {colony_id: 'northern_nigeria_1900_1914'}), (b:Colony {colony_id: 'royal_niger_company_territory_1886_1900'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Company territory became Northern Nigeria Protectorate', relationship_type: 'BECAME_PROTECTORATE', succession_type: 'DIRECT_SUCCESSION', year: 1900}]->(b);
MATCH (a:Colony {colony_id: 'northern_nigeria_1900_1914'}), (b:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Southern and Northern Nigeria merged to form Nigeria', relationship_type: 'MERGED_WITH', succession_type: 'COMPLEX_SUCCESSION', year: '1914'}]->(b);
MATCH (a:Colony {colony_id: 'northern_rhodesia_colony_1924_1953'}), (b:Colony {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}) MERGE (a)-[:EVOLVED_INTO {description: 'Northern Rhodesia joined Central African Federation', relationship_type: 'JOINED_FEDERATION', year: 1953}]->(b);
MATCH (a:Colony {colony_id: 'nova_scotia_post_1784_1867'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'nova_scotia_post_1784_1867'}), (b:Colony {colony_id: 'nova_scotia_province_1867'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'nova_scotia_pre_1713_1784'}), (b:Colony {colony_id: 'cape_breton_colony_1784_1820'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'nova_scotia_pre_1713_1784'}), (b:Colony {colony_id: 'new_brunswick_1784_1867'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'nova_scotia_pre_1713_1784'}), (b:Colony {colony_id: 'nova_scotia_post_1784_1867'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'nova_scotia_province_1867'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'nunavut_1999'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'nyasaland_1891_1964'}), (b:Colony {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}) MERGE (a)-[:EVOLVED_INTO {description: 'Nyasaland joined Central African Federation', relationship_type: 'JOINED_FEDERATION', year: 1953}]->(b);
MATCH (a:Colony {colony_id: 'nyasaland_1891_1964'}), (b:Colony {colony_id: 'british_central_africa_protectorate_1891_1907'}) MERGE (a)-[:SUCCESSOR_TO {description: 'British Central Africa Protectorate renamed to Nyasaland', relationship_type: 'RENAMED_TO', succession_type: 'DIRECT_SUCCESSION', year: 1907}]->(b);
MATCH (a:Colony {colony_id: 'oil_rivers_protectorate_1885_1893'}), (b:Colony {colony_id: 'niger_coast_protectorate_1893_1900'}) MERGE (a)-[:EVOLVED_INTO {description: 'Oil Rivers Protectorate renamed to Niger Coast Protectorate', relationship_type: 'RENAMED_TO', year: 1893}]->(b);
MATCH (a:Colony {colony_id: 'ontario_1867'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'orange_free_state_1854_1900'}), (b:Colony {colony_id: 'orange_river_colony_1900_1910'}) MERGE (a)-[:EVOLVED_INTO {description: 'Orange Free State conquered and renamed during Second Boer War', relationship_type: 'CONQUERED_AND_RENAMED', year: 1900}]->(b);
MATCH (a:Colony {colony_id: 'orange_river_colony_1900_1910'}), (b:Colony {colony_id: 'union_of_south_africa_1910_1961'}) MERGE (a)-[:EVOLVED_INTO {description: 'Orange River Colony joined Union as Orange Free State Province', relationship_type: 'FEDERATED_INTO', year: 1910}]->(b);
MATCH (a:Colony {colony_id: 'orange_river_sovereignty_1848_1854'}), (b:Colony {colony_id: 'orange_free_state_1854_1900'}) MERGE (a)-[:EVOLVED_INTO {description: 'Britain granted independence in Bloemfontein Convention', relationship_type: 'INDEPENDENCE_GRANTED', year: 1854}]->(b);
MATCH (a:Colony {colony_id: 'palestine_1920_1948'}), (b:Colony {colony_id: 'state_of_israel_1948'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'penang_prince_of_wales_island_1786_1826'}), (b:Colony {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:EVOLVED_INTO {description: 'Penang incorporated into Straits Settlements', relationship_type: 'INCORPORATED_INTO', year: 1826}]->(b);
MATCH (a:Colony {colony_id: 'pennsylvania_colony_1681_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'pennsylvania_colony_1681_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'prince_edward_island_1769_1873'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'Prince Edward Island joined Confederation as 7th province', relationship_type: 'JOINED', year: 1873}]->(b);
MATCH (a:Colony {colony_id: 'prince_edward_island_1769_1873'}), (b:Colony {colony_id: 'prince_edward_island_province_1873'}) MERGE (a)-[:EVOLVED_INTO {year: 1873}]->(b);
MATCH (a:Colony {colony_id: 'prince_edward_island_province_1873'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'princely_states_placeholder_1818_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'princely_states_placeholder_1818_1947'}), (b:Colony {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'province_of_canada_1841_1867'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'Province of Canada split into Ontario and Quebec, joined Confederation as Dominion of Canada', relationship_type: 'CONFEDERATED_INTO', year: 1867}]->(b);
MATCH (a:Colony {colony_id: 'province_of_canada_1841_1867'}), (b:Colony {colony_id: 'ontario_1867'}) MERGE (a)-[:EVOLVED_INTO {year: 1867}]->(b);
MATCH (a:Colony {colony_id: 'province_of_canada_1841_1867'}), (b:Colony {colony_id: 'quebec_1867'}) MERGE (a)-[:EVOLVED_INTO {year: 1867}]->(b);
MATCH (a:Colony {colony_id: 'province_of_canada_1841_1867'}), (b:Colony {colony_id: 'lower_canada_1791_1841'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Lower Canada merged with Upper Canada to form Province of Canada (Act of Union 1840)', relationship_type: 'MERGED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1841}]->(b);
MATCH (a:Colony {colony_id: 'province_of_canada_1841_1867'}), (b:Colony {colony_id: 'upper_canada_1791_1841'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Upper Canada merged with Lower Canada to form Province of Canada (Act of Union 1840)', relationship_type: 'MERGED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1841}]->(b);
MATCH (a:Colony {colony_id: 'province_of_freedom_1787_1792'}), (b:Colony {colony_id: 'sierra_leone_company_settlement_1792_1808'}) MERGE (a)-[:EVOLVED_INTO {description: 'Province of Freedom reorganized under Sierra Leone Company', relationship_type: 'REORGANIZED_AS', year: 1792}]->(b);
MATCH (a:Colony {colony_id: 'province_of_quebec_british_1763_1791'}), (b:Colony {colony_id: 'lower_canada_1791_1841'}) MERGE (a)-[:PARTITIONED_INTO {date: '1791-12-26', description: 'Constitutional Act 1791 divided Quebec', relationship_type: 'PARTITIONED_INTO', year: 1791}]->(b);
MATCH (a:Colony {colony_id: 'province_of_quebec_british_1763_1791'}), (b:Colony {colony_id: 'upper_canada_1791_1841'}) MERGE (a)-[:PARTITIONED_INTO {date: '1791-12-26', description: 'Constitutional Act 1791 divided Quebec', relationship_type: 'PARTITIONED_INTO', year: 1791}]->(b);
MATCH (a:Colony {colony_id: 'punjab_province_1849_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'punjab_province_1849_1947'}), (b:Colony {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'punjab_province_1849_1947'}), (b:Colony {colony_id: 'north_west_frontier_province_1901_1947'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'punjab_province_1849_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'quebec_1867'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'queensland_1859_1901'}), (b:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'Queensland joined Federation as founding state', relationship_type: 'FEDERATED_INTO', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'red_river_colony_1811_1870'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'rhode_island_colony_1636_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'rhode_island_colony_1636_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'rhodesia_udi_1965_1979'}), (b:Colony {colony_id: 'zimbabwe_rhodesia_1979_1979'}) MERGE (a)-[:EVOLVED_INTO {description: 'Internal settlement created Zimbabwe Rhodesia', relationship_type: 'INTERNAL_SETTLEMENT', year: 1979}]->(b);
MATCH (a:Colony {colony_id: 'royal_niger_company_territory_1886_1900'}), (b:Colony {colony_id: 'northern_nigeria_1900_1914'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'ruperts_land_1670_1870'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'ruperts_land_1670_1870'}), (b:Colony {colony_id: 'north_western_territory_1670_1870'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'ruperts_land_1670_1870'}), (b:Colony {colony_id: 'red_river_colony_1811_1870'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'saint_christopher_nevis_anguilla_1958_1983'}), (b:Colony {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'saint_christopher_nevis_anguilla_1958_1983'}), (b:Colony {colony_id: 'stkitts_nevis_anguilla_1816_1833'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1833, start_year: 1816}]->(b);
MATCH (a:Colony {colony_id: 'saint_lucia_colony_1814_1979'}), (b:Colony {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF]->(b);
MATCH (a:Colony {colony_id: 'sarawak_1841_1946'}), (b:Colony {colony_id: 'sarawak_crown_colony_1946_1963'}) MERGE (a)-[:EVOLVED_INTO {description: 'Brooke family ceded Sarawak to Crown', relationship_type: 'BECAME_CROWN_COLONY', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'sarawak_crown_colony_1946_1963'}), (b:Colony {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'sarawak_crown_colony_1946_1963'}), (b:Colony {colony_id: 'sarawak_1841_1946'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Brooke family ceded Sarawak to Crown', relationship_type: 'BECAME_CROWN_COLONY', succession_type: 'DIRECT_SUCCESSION', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'saskatchewan_1905'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'settlement_of_belize_1798_1862'}), (b:Colony {colony_id: 'british_honduras_1862_1981'}) MERGE (a)-[:EVOLVED_INTO {description: 'The settlement was formally declared the Crown Colony of British Honduras.', relationship_type: 'FORMALIZED_AS_COLONY', year: 1862}]->(b);
MATCH (a:Colony {colony_id: 'seychelles_1903_1976'}), (b:Colony {colony_id: 'seychelles_mauritius_dependency_1814_1903'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Seychelles separated from Mauritius as Crown Colony', relationship_type: 'BECAME_SEPARATE_COLONY', succession_type: 'DIRECT_SUCCESSION', year: 1903}]->(b);
MATCH (a:Colony {colony_id: 'seychelles_mauritius_dependency_1814_1903'}), (b:Colony {colony_id: 'seychelles_1903_1976'}) MERGE (a)-[:EVOLVED_INTO {description: 'Seychelles separated from Mauritius as Crown Colony', relationship_type: 'BECAME_SEPARATE_COLONY', year: 1903}]->(b);
MATCH (a:Colony {colony_id: 'sierra_leone_colony_1808_1896'}), (b:Colony {colony_id: 'sierra_leone_colony_and_protectorate_1787_1961'}) MERGE (a)-[:EVOLVED_INTO {description: 'Colony expanded with interior protectorate', relationship_type: 'EXPANDED_TO', year: 1896}]->(b);
MATCH (a:Colony {colony_id: 'sierra_leone_colony_1808_1896'}), (b:Colony {colony_id: 'sierra_leone_company_settlement_1792_1808'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Company rule ended, became Crown Colony', relationship_type: 'BECAME_CROWN_COLONY', succession_type: 'DIRECT_SUCCESSION', year: 1808}]->(b);
MATCH (a:Colony {colony_id: 'sierra_leone_company_settlement_1792_1808'}), (b:Colony {colony_id: 'sierra_leone_colony_1808_1896'}) MERGE (a)-[:EVOLVED_INTO {description: 'Company rule ended, became Crown Colony', relationship_type: 'BECAME_CROWN_COLONY', year: 1808}]->(b);
MATCH (a:Colony {colony_id: 'sierra_leone_company_settlement_1792_1808'}), (b:Colony {colony_id: 'province_of_freedom_1787_1792'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Province of Freedom reorganized under Sierra Leone Company', relationship_type: 'REORGANIZED_AS', succession_type: 'DIRECT_SUCCESSION', year: 1792}]->(b);
MATCH (a:Colony {colony_id: 'sind_province_1843_1947'}), (b:Colony {colony_id: 'dominion_of_pakistan_1947_1956'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'singapore_crown_colony_1946_1963'}), (b:Colony {colony_id: 'malaysia_1963'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'singapore_crown_colony_1946_1963'}), (b:Colony {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Singapore became separate crown colony', relationship_type: 'SEPARATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'singapore_settlement_1819_1826'}), (b:Colony {colony_id: 'straits_settlements_1826_1946'}) MERGE (a)-[:EVOLVED_INTO {description: 'Singapore incorporated into Straits Settlements', relationship_type: 'INCORPORATED_INTO', year: 1826}]->(b);
MATCH (a:Colony {colony_id: 'socotra_island_1886_1967'}), (b:Colony {colony_id: 'south_yemen_1967_1990'}) MERGE (a)-[:EVOLVED_INTO {description: 'Socotra became part of South Yemen', relationship_type: 'BECAME_PART_OF', year: 1967}]->(b);
MATCH (a:Colony {colony_id: 'south_african_republic_restored_1881_1900'}), (b:Colony {colony_id: 'transvaal_colony_second_british_1900_1910'}) MERGE (a)-[:EVOLVED_INTO {description: 'Transvaal conquered and renamed during Second Boer War', relationship_type: 'CONQUERED_AND_RENAMED', year: 1900}]->(b);
MATCH (a:Colony {colony_id: 'south_african_republic_transvaal_1852_1877'}), (b:Colony {colony_id: 'transvaal_colony_first_british_1877_1881'}) MERGE (a)-[:EVOLVED_INTO {description: 'Britain annexed Transvaal citing financial difficulties and conflicts', relationship_type: 'ANNEXED_BY', year: 1877}]->(b);
MATCH (a:Colony {colony_id: 'south_australia_1836_1901'}), (b:Colony {colony_id: 'western_australia_1832_1901'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753093189489, relationship_type: 'land_border', source: 'comprehensive_borders'}]->(b);
MATCH (a:Colony {colony_id: 'south_australia_1836_1901'}), (b:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'South Australia joined Federation as founding state', relationship_type: 'FEDERATED_INTO', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'south_carolina_colony_1663_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'south_carolina_colony_1663_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'}), (b:Colony {colony_id: 'colony_and_protectorate_of_nigeria_1914_1960'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'}), (b:Colony {colony_id: 'lagos_protectorate_1887_1906'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Lagos Protectorate incorporated into Southern Nigeria', relationship_type: 'MERGED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: '1906'}]->(b);
MATCH (a:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'}), (b:Colony {colony_id: 'lagos_protectorate_1887_1906'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Lagos merged into Southern Nigeria Protectorate', relationship_type: 'MERGED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1906}]->(b);
MATCH (a:Colony {colony_id: 'southern_nigeria_protectorate_1900_1914'}), (b:Colony {colony_id: 'niger_coast_protectorate_1893_1900'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Niger Coast Protectorate reorganized as Southern Nigeria', relationship_type: 'REORGANIZED_AS', succession_type: 'DIRECT_SUCCESSION', year: 1900}]->(b);
MATCH (a:Colony {colony_id: 'southern_rhodesia_colony_1923_1953'}), (b:Colony {colony_id: 'federation_of_rhodesia_and_nyasaland_1953_1963'}) MERGE (a)-[:EVOLVED_INTO {description: 'Southern Rhodesia joined Central African Federation', relationship_type: 'JOINED_FEDERATION', year: 1953}]->(b);
MATCH (a:Colony {colony_id: 'southern_rhodesia_colony_1923_1953'}), (b:Colony {colony_id: 'british_south_africa_company_territory_1889_1923'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Southern Rhodesia became self-governing colony after BSAC rule', relationship_type: 'BECAME_SELF_GOVERNING', succession_type: 'DIRECT_SUCCESSION', year: 1923}]->(b);
MATCH (a:Colony {colony_id: 'southern_rhodesia_post_federation_1963'}), (b:Colony {colony_id: 'rhodesia_udi_1965_1979'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'southern_rhodesia_restored_1979_1980'}), (b:Colony {colony_id: 'zimbabwe_rhodesia_1979_1979'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Lancaster House Agreement restored Crown Colony status', relationship_type: 'RESTORED_TO_CROWN', succession_type: 'DIRECT_SUCCESSION', year: 1979}]->(b);
MATCH (a:Colony {colony_id: 'st._helena_1659_ongoing'}), (b:Colony {colony_id: 'south_african_republic_restored_1881_1900'}) MERGE (a)-[:NEAR_COAST_OF {created_date: 1753093190065, relationship_type: 'coastal_proximity', source: 'comprehensive_coastal'}]->(b);
MATCH (a:Colony {colony_id: 'st_vincent_colony_1763_1979'}), (b:Colony {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'st_vincent_colony_1763_1979'}), (b:Colony {colony_id: 'british_windward_islands_1833_1959'}) MERGE (a)-[:WAS_MEMBER_OF {end_year: 1959, start_year: 1833}]->(b);
MATCH (a:Colony {colony_id: 'stkitts_nevis_anguilla_1816_1833'}), (b:Colony {colony_id: 'federal_colony_leeward_islands_1833-1960'}) MERGE (a)-[:EVOLVED_INTO {relationship_type: 'MERGED_INTO', year: 1833}]->(b);
MATCH (a:Colony {colony_id: 'straits_settlements_1826_1946'}), (b:Colony {colony_id: 'malayan_union_1946_1948'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'straits_settlements_1826_1946'}), (b:Colony {colony_id: 'singapore_crown_colony_1946_1963'}) MERGE (a)-[:PARTITIONED_INTO]->(b);
MATCH (a:Colony {colony_id: 'straits_settlements_1826_1946'}), (b:Colony {colony_id: 'malacca_settlement_1824_1826'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Malacca incorporated into Straits Settlements', relationship_type: 'INCORPORATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1826}]->(b);
MATCH (a:Colony {colony_id: 'straits_settlements_1826_1946'}), (b:Colony {colony_id: 'penang_prince_of_wales_island_1786_1826'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Penang incorporated into Straits Settlements', relationship_type: 'INCORPORATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1826}]->(b);
MATCH (a:Colony {colony_id: 'straits_settlements_1826_1946'}), (b:Colony {colony_id: 'singapore_settlement_1819_1826'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Singapore incorporated into Straits Settlements', relationship_type: 'INCORPORATED_INTO', succession_type: 'COMPLEX_SUCCESSION', year: 1826}]->(b);
MATCH (a:Colony {colony_id: 'swan_river_colony_1829_1832'}), (b:Colony {colony_id: 'western_australia_1832_1901'}) MERGE (a)-[:EVOLVED_INTO {description: 'Swan River Colony renamed to Western Australia', relationship_type: 'RENAMED_TO', year: 1832}]->(b);
MATCH (a:Colony {colony_id: 'tanganyika_1961_1964'}), (b:Colony {colony_id: 'uganda_1894_1962'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753093189407, relationship_type: 'land_border', source: 'comprehensive_borders'}]->(b);
MATCH (a:Colony {colony_id: 'tanganyika_1961_1964'}), (b:Colony {colony_id: 'tanzania_1964'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'tanganyika_territory_1922_1961'}), (b:Colony {colony_id: 'tanganyika_1961_1964'}) MERGE (a)-[:EVOLVED_INTO {description: 'Tanganyika gained independence under Julius Nyerere', relationship_type: 'BECAME_INDEPENDENT', year: 1961}]->(b);
MATCH (a:Colony {colony_id: 'tanganyika_territory_1922_1961'}), (b:Colony {colony_id: 'german_east_africa_british_occupied_1916_1922'}) MERGE (a)-[:SUCCESSOR_TO {description: 'German East Africa became League of Nations mandate territory', relationship_type: 'BECAME_MANDATE', succession_type: 'DIRECT_SUCCESSION', year: 1922}]->(b);
MATCH (a:Colony {colony_id: 'tasmania_1856_1901'}), (b:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'Tasmania joined Federation as founding state', relationship_type: 'FEDERATED_INTO', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'tasmania_1856_1901'}), (b:Colony {colony_id: 'van_diemens_land_1803_1856'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Van Diemen\'s Land officially renamed to Tasmania and gained self-government', relationship_type: 'RENAMED_TO', succession_type: 'DIRECT_SUCCESSION', year: 1856}]->(b);
MATCH (a:Colony {colony_id: 'tasmania_1856_1901'}), (b:Colony {colony_id: 'van_diemens_land_1803_1856'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Van Diemen\'s Land renamed to Tasmania', relationship_type: 'DIRECT_SUCCESSION', succession_type: 'DIRECT_SUCCESSION', year: 1856}]->(b);
MATCH (a:Colony {colony_id: 'tonga_protectorate_1900_1970'}), (b:Colony {colony_id: 'fiji_1874_1970'}) MERGE (a)-[:NEAR_COAST_OF {created_date: 1753093190124, relationship_type: 'coastal_proximity', source: 'comprehensive_coastal'}]->(b);
MATCH (a:Colony {colony_id: 'transvaal_colony_first_british_1877_1881'}), (b:Colony {colony_id: 'south_african_republic_restored_1881_1900'}) MERGE (a)-[:EVOLVED_INTO {description: 'Independence restored after First Boer War defeat of British', relationship_type: 'INDEPENDENCE_RESTORED', year: 1881}]->(b);
MATCH (a:Colony {colony_id: 'transvaal_colony_second_british_1900_1910'}), (b:Colony {colony_id: 'union_of_south_africa_1910_1961'}) MERGE (a)-[:EVOLVED_INTO {description: 'Transvaal joined Union of South Africa as Transvaal Province', relationship_type: 'FEDERATED_INTO', year: 1910}]->(b);
MATCH (a:Colony {colony_id: 'trinidad_and_tobago_1889_1962'}), (b:Colony {colony_id: 'british_guiana_1831_1966'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753058509160, relationship_type: 'land_border', source: 'historical_borders'}]->(b);
MATCH (a:Colony {colony_id: 'trinidad_and_tobago_1889_1962'}), (b:Colony {colony_id: 'west_indies_federation_1958_1962'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'trinidad_and_tobago_colony_1797_1962'}), (b:Colony {colony_id: 'trinidad_and_tobago_1889_1962'}) MERGE (a)-[:EVOLVED_INTO {description: 'Trinidad and Tobago gained independence from Britain', relationship_type: 'BECAME_INDEPENDENT', year: 1962}]->(b);
MATCH (a:Colony {colony_id: 'uganda_1894_1962'}), (b:Colony {colony_id: 'tanganyika_1961_1964'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753093189407, relationship_type: 'land_border', source: 'comprehensive_borders'}]->(b);
MATCH (a:Colony {colony_id: 'unfederated_malay_states_1909_1946'}), (b:Colony {colony_id: 'malayan_union_1946_1948'}) MERGE (a)-[:EVOLVED_INTO {description: 'UMS incorporated into Malayan Union', relationship_type: 'INCORPORATED_INTO', year: 1946}]->(b);
MATCH (a:Colony {colony_id: 'union_of_south_africa_1910_1961'}), (b:Colony {colony_id: 'cape_colony_british_1806_1910'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Cape Colony joined Union of South Africa', relationship_type: 'FEDERATION_SUCCESSION', succession_type: 'FEDERATION_SUCCESSION', year: 1910}]->(b);
MATCH (a:Colony {colony_id: 'union_of_south_africa_1910_1961'}), (b:Colony {colony_id: 'orange_river_colony_1900_1910'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Orange River Colony joined Union of South Africa', relationship_type: 'FEDERATION_SUCCESSION', succession_type: 'FEDERATION_SUCCESSION', year: 1910}]->(b);
MATCH (a:Colony {colony_id: 'united_colony_of_bc_1866_1871'}), (b:Colony {colony_id: 'british_columbia_province_1871'}) MERGE (a)-[:EVOLVED_INTO {year: 1871}]->(b);
MATCH (a:Colony {colony_id: 'united_colony_of_bc_1866_1871'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:EVOLVED_INTO {relationship_type: 'JOINED_CONFEDERATION', year: 1871}]->(b);
MATCH (a:Colony {colony_id: 'united_provinces_1877_1947'}), (b:Colony {colony_id: 'dominion_of_india_1947_1950'}) MERGE (a)-[:EVOLVED_INTO {description: 'United Provinces joined India', relationship_type: 'JOINED', year: 1947}]->(b);
MATCH (a:Colony {colony_id: 'united_provinces_1877_1947'}), (b:Colony {colony_id: 'indian_empire_british_raj_1858_1947'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'upper_canada_1791_1841'}), (b:Colony {colony_id: 'lower_canada_1791_1841'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753058509064, relationship_type: 'land_border', source: 'historical_borders'}]->(b);
MATCH (a:Colony {colony_id: 'upper_canada_1791_1841'}), (b:Colony {colony_id: 'province_of_canada_1841_1867'}) MERGE (a)-[:EVOLVED_INTO {description: 'Upper Canada merged with Lower Canada to form Province of Canada (Act of Union 1840)', relationship_type: 'MERGED_INTO', year: 1841}]->(b);
MATCH (a:Colony {colony_id: 'van_diemens_land_1803_1856'}), (b:Colony {colony_id: 'tasmania_1856_1901'}) MERGE (a)-[:EVOLVED_INTO {description: 'Van Diemen\'s Land officially renamed to Tasmania and gained self-government', relationship_type: 'RENAMED_TO', year: 1856}]->(b);
MATCH (a:Colony {colony_id: 'vancouver_island_1849_1866'}), (b:Colony {colony_id: 'united_colony_of_bc_1866_1871'}) MERGE (a)-[:EVOLVED_INTO {relationship_type: 'MERGED_INTO', year: 1866}]->(b);
MATCH (a:Colony {colony_id: 'victoria_colony_1851_1901'}), (b:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'Victoria joined Federation as founding state', relationship_type: 'FEDERATED_INTO', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'virginia_colony_1607_1783'}), (b:Colony {colony_id: 'united_states_1776'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'virginia_colony_1607_1783'}), (b:Colony {colony_id: 'united_states_of_america_1783'}) MERGE (a)-[:EVOLVED_INTO {year: 1783}]->(b);
MATCH (a:Colony {colony_id: 'western_australia_1832_1901'}), (b:Colony {colony_id: 'south_australia_1836_1901'}) MERGE (a)-[:BORDERS_WITH {created_date: 1753093189489, relationship_type: 'land_border', source: 'comprehensive_borders'}]->(b);
MATCH (a:Colony {colony_id: 'western_australia_1832_1901'}), (b:Colony {colony_id: 'commonwealth_of_australia_1901_ongoing'}) MERGE (a)-[:EVOLVED_INTO {description: 'Western Australia joined Federation as founding state (last to join after referendum)', relationship_type: 'FEDERATED_INTO', year: 1901}]->(b);
MATCH (a:Colony {colony_id: 'western_australia_1832_1901'}), (b:Colony {colony_id: 'swan_river_colony_1829_1832'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Swan River Colony renamed to Western Australia', relationship_type: 'RENAMED_TO', succession_type: 'DIRECT_SUCCESSION', year: 1832}]->(b);
MATCH (a:Colony {colony_id: 'yukon_territory_1898'}), (b:Colony {colony_id: 'canada_dominion_of_1867_ongoing'}) MERGE (a)-[:PART_OF]->(b);
MATCH (a:Colony {colony_id: 'zanzibar_1890_1963'}), (b:Colony {colony_id: 'zanzibar_independent_1963_1964'}) MERGE (a)-[:EVOLVED_INTO {description: 'Zanzibar gained independence from British protectorate', relationship_type: 'BECAME_INDEPENDENT', year: 1963}]->(b);
MATCH (a:Colony {colony_id: 'zanzibar_1890_1963'}), (b:Colony {colony_id: 'tanganyika_territory_1922_1961'}) MERGE (a)-[:SUCCESSOR_TO {description: 'Tanganyika and Zanzibar merged to form Tanzania', relationship_type: 'MERGED_WITH', succession_type: 'COMPLEX_SUCCESSION', year: '1964'}]->(b);
MATCH (a:Colony {colony_id: 'zanzibar_independent_1963_1964'}), (b:Colony {colony_id: 'tanzania_1964'}) MERGE (a)-[:EVOLVED_INTO]->(b);
MATCH (a:Colony {colony_id: 'zimbabwe_rhodesia_1979_1979'}), (b:Colony {colony_id: 'southern_rhodesia_restored_1979_1980'}) MERGE (a)-[:EVOLVED_INTO {description: 'Lancaster House Agreement restored Crown Colony status', relationship_type: 'RESTORED_TO_CROWN', year: 1979}]->(b);
MATCH (a:Colony {colony_id: 'zululand_1887_1897'}), (b:Colony {colony_id: 'colony_of_natal_1843_1910'}) MERGE (a)-[:EVOLVED_INTO {description: 'Zululand incorporated into Colony of Natal', relationship_type: 'INCORPORATED_INTO', year: 1897}]->(b);

// Total: 314 nodes, 335 relationships
#!/usr/bin/env python3
"""
Extract effective per-region node and edge data from empire_viz_data.json
after applying all HTML patches (DATA_FIXES, REMOVE_IDS, REMOVE_EDGES, etc.).

Produces clean text summaries per region for history expert verification agents.
"""

import json
import sys
from collections import defaultdict

def main():
    with open('empire_viz_data.json') as f:
        raw = json.load(f)

    nodes = raw['nodes']
    edges = raw['edges']

    # ── DATA_FIXES: property patches ──
    DATA_FIXES = {
        'united_colony_of_bc_1866_1871': {'ind': 1871},
        'commonwealth_of_australia_1901_ongoing': {'ind': 1942},
        'mainland_british_columbia_1858_1866': {'ind': 1866},
        'colony_of_newfoundland_1610_1949': {'ind': 1907},
        'new_hampshire_colony_1623_1783': {'est': 1629},
        'canada_french_1608_1763': {'ind': 1763},
        'settlement_of_belize_1798_1862': {'ind': 1862, 'region': 'Caribbean'},
        'british_honduras_1862_1981': {'region': 'Caribbean'},
        'antigua_montserrat_barbuda_1816_1833': {'name': 'Antigua-Barbuda-Montserrat', 'est': 1816, 'ind': 1833, 'region': 'Caribbean'},
        'stkitts_nevis_anguilla_1816_1833': {'name': 'St. Kitts-Nevis-Anguilla', 'est': 1816, 'ind': 1833, 'region': 'Caribbean'},
        'acadia_french_1604_1713': {'ind': 1713},
        'bermuda_1609_ongoing': {'region': 'Atlantic'},
        'british_guiana_1831_1966': {'region': 'South America'},
        'canada_dominion_of_1867_ongoing': {'name': 'Dominion of Canada', 'ind': 1931},
        'leeward_islands_colony_1671_1816': {'ind': 1816},
        'federal_colony_leeward_islands_1833-1960': {'type': 'Federal Colony', 'ind': 1960},
        'antigua_colony_1632_1981': {'ind': 1981},
        'saint_christopher_nevis_anguilla_1958_1983': {'est': 1624},
        'trinidad_and_tobago_colony_1797_1962': {'name': 'Trinidad Colony', 'ind': 1888},
        'trinidad_and_tobago_1889_1962': {'name': 'Colony of Trinidad and Tobago'},
        'assam_province_1874_1905': {'ind': 1905},
        'lower_burma_1824_1886': {'ind': 1886},
        'assam_bengal_presidency_1826_1874': {'ind': 1874},
        'assam_province_restored_1912_1947': {'ind': 1947},
        'aden_1839_1963': {'ind': 1937},
        'bencoolen_bengkulu_1685_1824': {'ind': 1824},
        'banda_islands_british_occupation_1810_1817': {'ind': 1817},
        'factory_at_surat_1612_1857': {'ind': 1687},
        'fort_william_calcutta_1696_1857': {'ind': 1757},
        'nyasaland_1891_1964': {'ind': 1953},
        'sierra_leone_colony_and_protectorate_1787_1961': {'est': 1896},
    }

    AFRICA_FIXES = {
        'northern_rhodesia_post_federation_1963': {'type': 'Transitional'},
        'nyasaland_post_federation_1963': {'type': 'Transitional', 'est': 1963, 'ind': 1964},
    }

    for n in nodes:
        fix = DATA_FIXES.get(n['id'])
        if fix:
            n.update(fix)
        fix2 = AFRICA_FIXES.get(n['id'])
        if fix2:
            n.update(fix2)
        if n.get('ind') == '':
            n['ind'] = None
        if n.get('region') == 'America':
            n['region'] = 'North America'

    # ── REMOVE old Nova Scotia, replace with pre/post partition ──
    nodes = [n for n in nodes if n['id'] != 'nova_scotia_1621_1867']
    nodes.append({'id': 'nova_scotia_pre_1713_1784', 'name': 'Nova Scotia', 'est': 1713, 'ind': 1784,
                  'region': 'North America', 'type': 'Crown Colony', 'qid': 'Q98931415'})
    nodes.append({'id': 'nova_scotia_post_1784_1867', 'name': 'Nova Scotia', 'est': 1784, 'ind': 1867,
                  'region': 'North America', 'type': 'Crown Colony', 'qid': 'Q98931415'})

    # Update edges referencing old NS
    for e in edges:
        if e.get('target') == 'nova_scotia_1621_1867':
            e['target'] = 'nova_scotia_pre_1713_1784'
        if e.get('source') == 'nova_scotia_1621_1867':
            e['source'] = 'nova_scotia_post_1784_1867'

    # ── ADD NEW NODES ──
    new_nodes = [
        {'id': 'nova_scotia_scottish_1621_1632', 'name': 'Nova Scotia (Scottish Charter)', 'est': 1621, 'ind': 1632,
         'region': 'North America', 'type': 'Charter Colony', 'qid': 'Q1854755'},
        {'id': 'red_river_colony_1811_1870', 'name': 'Red River Colony', 'est': 1811, 'ind': 1870,
         'region': 'North America', 'type': 'Colony', 'qid': 'Q1143638'},
        {'id': 'australia_independent_1942', 'name': 'Australia', 'est': 1942, 'ind': None,
         'region': 'Pacific', 'type': 'Independence', 'qid': 'Q408'},
        {'id': 'new_zealand_colony_1840_1907', 'name': 'New Zealand Colony', 'est': 1840, 'ind': 1907,
         'region': 'Pacific', 'type': 'Crown Colony', 'qid': 'Q664'},
        {'id': 'dominion_of_new_zealand_1907_1947', 'name': 'Dominion of New Zealand', 'est': 1907, 'ind': 1947,
         'region': 'Pacific', 'type': 'Dominion', 'qid': 'Q664'},
        {'id': 'new_zealand_independent_1947', 'name': 'New Zealand', 'est': 1947, 'ind': None,
         'region': 'Pacific', 'type': 'Independence', 'qid': 'Q664'},
        {'id': 'united_states_1776', 'name': 'United States of America', 'est': 1776, 'ind': None,
         'region': 'North America', 'type': 'Independence', 'qid': 'Q30'},
        {'id': 'canada_independent_1931', 'name': 'Canada', 'est': 1931, 'ind': None,
         'region': 'North America', 'type': 'Independence', 'qid': 'Q16'},
        {'id': 'newfoundland_commission_1934_1949', 'name': 'Newfoundland (Commission)', 'est': 1934, 'ind': 1949,
         'region': 'North America', 'type': 'Crown Colony', 'qid': 'Q48378'},
        {'id': 'southern_rhodesia_post_federation_1963', 'name': 'Southern Rhodesia', 'est': 1963, 'ind': 1965,
         'region': 'Southern Africa', 'type': 'Self-governing Colony', 'qid': 'Q750583'},
        {'id': 'northern_rhodesia_post_federation_1964', 'name': 'Northern Rhodesia', 'est': 1963, 'ind': 1964,
         'region': 'Southern Africa', 'type': 'Transitional', 'qid': 'Q953903'},
        {'id': 'coorg_province_1834_1947', 'name': 'Coorg', 'est': 1834, 'ind': 1947,
         'region': 'South Asia', 'type': 'Province', 'qid': 'Q864930'},
        {'id': 'ajmer_merwara_1818_1947', 'name': 'Ajmer-Merwara', 'est': 1818, 'ind': 1947,
         'region': 'South Asia', 'type': 'Province', 'qid': 'Q4700553'},
        {'id': 'sind_province_1843_1947', 'name': 'Sind', 'est': 1936, 'ind': 1947,
         'region': 'South Asia', 'type': 'Province', 'qid': 'Q7523949'},
        {'id': 'andaman_and_nicobar_islands_1789_1947', 'name': 'Andaman and Nicobar Islands', 'est': 1789, 'ind': 1947,
         'region': 'South Asia', 'type': 'Province', 'qid': 'Q40888'},
        {'id': 'malaysia_1963', 'name': 'Malaysia', 'est': 1963, 'ind': None,
         'region': 'Southeast Asia', 'type': 'Independence', 'qid': 'Q833'},
        {'id': 'singapore_independent_1965', 'name': 'Singapore', 'est': 1965, 'ind': None,
         'region': 'Southeast Asia', 'type': 'Independence', 'qid': 'Q334'},
        {'id': 'tanzania_1964', 'name': 'Tanzania', 'est': 1964, 'ind': None,
         'region': 'East Africa', 'type': 'Independence', 'qid': 'Q924'},
        {'id': 'minorca_first_1708_1756', 'name': 'Minorca (1st British)', 'est': 1708, 'ind': 1756,
         'region': 'Europe', 'type': 'Crown Colony', 'qid': 'Q173095'},
        {'id': 'minorca_second_1763_1782', 'name': 'Minorca (2nd British)', 'est': 1763, 'ind': 1782,
         'region': 'Europe', 'type': 'Crown Colony', 'qid': 'Q173095'},
        {'id': 'minorca_third_1798_1802', 'name': 'Minorca (3rd British)', 'est': 1798, 'ind': 1802,
         'region': 'Europe', 'type': 'Crown Colony', 'qid': 'Q173095'},
        {'id': 'corsica_1794_1796', 'name': 'Anglo-Corsican Kingdom', 'est': 1794, 'ind': 1796,
         'region': 'Europe', 'type': 'Protectorate', 'qid': 'Q2259576'},
        {'id': 'heligoland_1807_1890', 'name': 'Heligoland', 'est': 1807, 'ind': 1890,
         'region': 'Europe', 'type': 'Crown Colony', 'qid': 'Q3104'},
        {'id': 'kingdom_of_ireland_1541_1801', 'name': 'Kingdom of Ireland', 'est': 1541, 'ind': 1801,
         'region': 'Europe', 'type': 'Kingdom', 'qid': 'Q179876'},
        {'id': 'ireland_uk_1801_1922', 'name': 'Ireland (UK)', 'est': 1801, 'ind': 1922,
         'region': 'Europe', 'type': 'Union', 'qid': 'Q174193'},
        {'id': 'irish_free_state_1922_1937', 'name': 'Irish Free State', 'est': 1922, 'ind': 1937,
         'region': 'Europe', 'type': 'Dominion', 'qid': 'Q31747'},
        {'id': 'northern_ireland_1920', 'name': 'Northern Ireland', 'est': 1920, 'ind': None,
         'region': 'Europe', 'type': 'Devolved Government', 'qid': 'Q26'},
    ]
    nodes.extend(new_nodes)

    # Remove old NZ node
    nodes = [n for n in nodes if n['id'] != 'new_zealand_1840_1947']
    # Redirect NZ edges
    for e in edges:
        if e.get('target') == 'new_zealand_1840_1947':
            e['target'] = 'new_zealand_colony_1840_1907'
        if e.get('source') == 'new_zealand_1840_1947':
            e['source'] = 'dominion_of_new_zealand_1907_1947'

    # Rename NSW
    for n in nodes:
        if n['id'] == 'new_south_wales_original_1788_1901':
            n['name'] = 'New South Wales'

    # ── ADD NEW EDGES ──
    new_edges = [
        {'source': 'nova_scotia_scottish_1621_1632', 'target': 'nova_scotia_pre_1713_1784', 'type': 'EVOLVED_INTO'},
        {'source': 'acadia_french_1604_1713', 'target': 'nova_scotia_pre_1713_1784', 'type': 'EVOLVED_INTO'},
        {'source': 'nova_scotia_pre_1713_1784', 'target': 'nova_scotia_post_1784_1867', 'type': 'PARTITIONED_INTO'},
        {'source': 'nova_scotia_pre_1713_1784', 'target': 'new_brunswick_1784_1867', 'type': 'PARTITIONED_INTO'},
        {'source': 'new_france_1608_1763', 'target': 'province_of_quebec_british_1763_1791', 'type': 'EVOLVED_INTO'},
        {'source': 'ile_royale_1713_1763', 'target': 'nova_scotia_pre_1713_1784', 'type': 'EVOLVED_INTO'},
        {'source': 'commonwealth_of_australia_1901_ongoing', 'target': 'australia_independent_1942', 'type': 'EVOLVED_INTO'},
        {'source': 'new_zealand_colony_1840_1907', 'target': 'dominion_of_new_zealand_1907_1947', 'type': 'EVOLVED_INTO'},
        {'source': 'dominion_of_new_zealand_1907_1947', 'target': 'new_zealand_independent_1947', 'type': 'EVOLVED_INTO'},
        {'source': 'canada_dominion_of_1867_ongoing', 'target': 'canada_independent_1931', 'type': 'EVOLVED_INTO'},
        {'source': 'ruperts_land_1670_1870', 'target': 'north_western_territory_1670_1870', 'type': 'PARTITIONED_INTO'},
        {'source': 'ruperts_land_1670_1870', 'target': 'red_river_colony_1811_1870', 'type': 'PARTITIONED_INTO'},
        {'source': 'ruperts_land_1670_1870', 'target': 'canada_dominion_of_1867_ongoing', 'type': 'EVOLVED_INTO'},
        {'source': 'red_river_colony_1811_1870', 'target': 'canada_dominion_of_1867_ongoing', 'type': 'EVOLVED_INTO'},
        {'source': 'north_western_territory_1670_1870', 'target': 'canada_dominion_of_1867_ongoing', 'type': 'EVOLVED_INTO'},
        {'source': 'colony_of_newfoundland_1610_1949', 'target': 'dominion_of_newfoundland_1907_1934', 'type': 'EVOLVED_INTO'},
        {'source': 'dominion_of_newfoundland_1907_1934', 'target': 'newfoundland_commission_1934_1949', 'type': 'EVOLVED_INTO'},
        {'source': 'newfoundland_commission_1934_1949', 'target': 'canada_independent_1931', 'type': 'EVOLVED_INTO'},
        # Federation PARTITIONED_INTO post-federation nodes
        {'source': 'federation_of_rhodesia_and_nyasaland_1953_1963', 'target': 'southern_rhodesia_post_federation_1963', 'type': 'PARTITIONED_INTO'},
        {'source': 'federation_of_rhodesia_and_nyasaland_1953_1963', 'target': 'northern_rhodesia_post_federation_1964', 'type': 'PARTITIONED_INTO'},
        {'source': 'federation_of_rhodesia_and_nyasaland_1953_1963', 'target': 'nyasaland_post_federation_1963', 'type': 'PARTITIONED_INTO'},
        {'source': 'southern_rhodesia_post_federation_1963', 'target': 'rhodesia_udi_1965_1979', 'type': 'EVOLVED_INTO'},
        # Gold Coast group
        {'source': 'gold_coast_colony_1874_1957', 'target': 'ashanti_1901_1957', 'type': 'PARTITIONED_INTO'},
        {'source': 'gold_coast_colony_1874_1957', 'target': 'british_togoland_1919_1957', 'type': 'PARTITIONED_INTO'},
        # EIC forts → Presidencies
        {'source': 'factory_at_surat_1612_1857', 'target': 'bombay_presidency_company_1687_1858', 'type': 'EVOLVED_INTO'},
        {'source': 'fort_william_calcutta_1696_1857', 'target': 'bengal_presidency_company_1757_1858', 'type': 'EVOLVED_INTO'},
        # 1947 partition edges
        {'source': 'baluchistan_1877_1947', 'target': 'dominion_of_pakistan_1947_1956', 'type': 'EVOLVED_INTO'},
        # Aden
        {'source': 'aden_1839_1963', 'target': 'aden_colony_1937_1967', 'type': 'EVOLVED_INTO'},
        # Assam from Bengal
        {'source': 'bengal_presidency_company_1757_1858', 'target': 'assam_bengal_presidency_1826_1874', 'type': 'PARTITIONED_INTO'},
        # Indian provinces → Dominion of India
        {'source': 'coorg_province_1834_1947', 'target': 'dominion_of_india_1947_1950', 'type': 'EVOLVED_INTO'},
        {'source': 'ajmer_merwara_1818_1947', 'target': 'dominion_of_india_1947_1950', 'type': 'EVOLVED_INTO'},
        {'source': 'andaman_and_nicobar_islands_1789_1947', 'target': 'dominion_of_india_1947_1950', 'type': 'EVOLVED_INTO'},
        {'source': 'bombay_presidency_crown_1858_1947', 'target': 'sind_province_1843_1947', 'type': 'PARTITIONED_INTO'},
        {'source': 'sind_province_1843_1947', 'target': 'dominion_of_pakistan_1947_1956', 'type': 'EVOLVED_INTO'},
        # Malaysia
        {'source': 'malaya_independent_1957_1963', 'target': 'malaysia_1963', 'type': 'EVOLVED_INTO'},
        {'source': 'singapore_crown_colony_1946_1963', 'target': 'malaysia_1963', 'type': 'EVOLVED_INTO'},
        {'source': 'north_borneo_crown_colony_1946_1963', 'target': 'malaysia_1963', 'type': 'EVOLVED_INTO'},
        {'source': 'sarawak_crown_colony_1946_1963', 'target': 'malaysia_1963', 'type': 'EVOLVED_INTO'},
        {'source': 'labuan_1846_1963', 'target': 'malaysia_1963', 'type': 'EVOLVED_INTO'},
        {'source': 'malaysia_1963', 'target': 'singapore_independent_1965', 'type': 'PARTITIONED_INTO'},
        # Tanzania
        {'source': 'tanganyika_1961_1964', 'target': 'tanzania_1964', 'type': 'EVOLVED_INTO'},
        {'source': 'zanzibar_independent_1963_1964', 'target': 'tanzania_1964', 'type': 'EVOLVED_INTO'},
        # Minorca succession
        {'source': 'minorca_first_1708_1756', 'target': 'minorca_second_1763_1782', 'type': 'EVOLVED_INTO'},
        {'source': 'minorca_second_1763_1782', 'target': 'minorca_third_1798_1802', 'type': 'EVOLVED_INTO'},
        # Ireland
        {'source': 'kingdom_of_ireland_1541_1801', 'target': 'ireland_uk_1801_1922', 'type': 'EVOLVED_INTO'},
        {'source': 'ireland_uk_1801_1922', 'target': 'irish_free_state_1922_1937', 'type': 'PARTITIONED_INTO'},
        {'source': 'ireland_uk_1801_1922', 'target': 'northern_ireland_1920', 'type': 'PARTITIONED_INTO'},
        # 13 colonies → USA
        *[{'source': cid, 'target': 'united_states_1776', 'type': 'EVOLVED_INTO'} for cid in [
            'virginia_colony_1607_1783', 'massachusetts_bay_colony_1630_1783',
            'pennsylvania_colony_1681_1783', 'new_york_colony_1664_1783',
            'maryland_colony_1634_1783', 'connecticut_colony_1636_1783',
            'rhode_island_colony_1636_1783', 'delaware_colony_1664_1783',
            'new_hampshire_colony_1623_1783', 'new_jersey_colony_1664_1783',
            'north_carolina_colony_1663_1783', 'south_carolina_colony_1663_1783',
            'georgia_colony_1732_1783',
        ]],
    ]
    edges.extend(new_edges)

    # ── EDGE REDIRECTS ──
    for e in edges:
        if e.get('target') == 'northern_rhodesia_1911_1964':
            e['target'] = 'northern_rhodesia_colony_1924_1953'
        if e.get('source') == 'northern_rhodesia_1911_1964':
            e['source'] = 'northern_rhodesia_colony_1924_1953'
        if e.get('source') == 'southern_rhodesia_1901_1980':
            e['source'] = 'southern_rhodesia_colony_1923_1953'
        if e.get('target') == 'southern_rhodesia_1901_1980':
            e['target'] = 'southern_rhodesia_colony_1923_1953'
        if e.get('source') == 'eastern_bengal_and_assam_1905_1912' and e.get('target') == 'assam_province_1874_1905':
            e['target'] = 'assam_province_restored_1912_1947'
        if e.get('target') == 'uganda_protectorate_1894_1962':
            e['target'] = 'uganda_1894_1962'
        if e.get('source') == 'uganda_protectorate_1894_1962':
            e['source'] = 'uganda_1894_1962'
        if e.get('target') == 'somaliland_protectorate_1884_1960':
            e['target'] = 'british_somaliland_1884_1960'
        if e.get('source') == 'somaliland_protectorate_1884_1960':
            e['source'] = 'british_somaliland_1884_1960'
        if e.get('target') == 'anglo_egyptian_sudan_1899_1956':
            e['target'] = 'sudan_anglo-egyptian_1899_1956'
        if e.get('source') == 'anglo_egyptian_sudan_1899_1956':
            e['source'] = 'sudan_anglo-egyptian_1899_1956'

    # ── EDGE TYPE FIXES ──
    for e in edges:
        # Leeward Islands partition
        if e.get('source') == 'leeward_islands_colony_1671_1816' and e.get('target') in ('antigua_montserrat_barbuda_1816_1833', 'stkitts_nevis_anguilla_1816_1833'):
            e['type'] = 'PARTITIONED_INTO'
        # BSAC partition
        if e.get('source') == 'british_south_africa_company_territory_1889_1923' and e.get('target') in ('southern_rhodesia_colony_1923_1953', 'northern_rhodesia_colony_1924_1953'):
            e['type'] = 'PARTITIONED_INTO'
        # Bengal Crown → Assam carve-out
        if e.get('source') == 'bengal_presidency_crown_1858_1912' and e.get('target') == 'assam_province_1874_1905':
            e['type'] = 'PARTITIONED_INTO'
        # Punjab → NWFP carve-out
        if e.get('source') == 'punjab_province_1849_1947' and e.get('target') == 'north_west_frontier_province_1901_1947':
            e['type'] = 'PARTITIONED_INTO'
        # NSW carve-outs
        if e.get('source') == 'new_south_wales_original_1788_1901' and e.get('target') in ('van_diemens_land_1803_1856', 'victoria_colony_1851_1901', 'queensland_1859_1901'):
            e['type'] = 'PARTITIONED_INTO'
        # Bengal/Punjab partition 1947
        if e.get('source') == 'bengal_province_reunited_1912_1947' and e.get('target') in ('dominion_of_india_1947_1950', 'dominion_of_pakistan_1947_1956'):
            e['type'] = 'PARTITIONED_INTO'
        if e.get('source') == 'punjab_province_1849_1947' and e.get('target') in ('dominion_of_india_1947_1950', 'dominion_of_pakistan_1947_1956'):
            e['type'] = 'PARTITIONED_INTO'
        # Straits → Singapore
        if e.get('source') == 'straits_settlements_1826_1946' and e.get('target') == 'singapore_crown_colony_1946_1963':
            e['type'] = 'PARTITIONED_INTO'

    # ── REMOVE EDGES ──
    edges = [e for e in edges if not (
        (e['source'] == 'cape_colony_british_1806_1910' and e['target'] == 'natalia_republic_1839_1843') or
        (e['source'] == 'cape_colony_british_1806_1910' and e['target'] == 'orange_river_sovereignty_1848_1854') or
        (e['source'] == 'federation_of_rhodesia_and_nyasaland_1953_1963' and e['target'] == 'rhodesia_udi_1965_1979') or
        (e['source'] == 'tanganyika_territory_1922_1961' and e['target'] == 'zanzibar_1890_1963') or
        (e['source'] == 'south_australia_1836_1901' and e['target'] == 'northern_territory_1911_ongoing')
    )]

    REMOVE_EDGES_SET = {
        'west_indies_federation_1958_1962->trinidad_and_tobago_1889_1962',
        'west_indies_federation_1958_1962->jamaica_1655_1962',
        'southern_nigeria_protectorate_1900_1914->northern_nigeria_1900_1914',
        'assam_province_1874_1905->dominion_of_india_1947_1950',
        'assam_province_restored_1912_1947->dominion_of_pakistan_1947_1956',
        'vancouver_island_1849_1866->mainland_british_columbia_1858_1866',
        'mainland_british_columbia_1858_1866->canada_dominion_of_1867_ongoing',
    }

    # ── REMOVE IDS ──
    REMOVE_IDS = {
        'manitoba_1870_1870_ongoing', 'northwest_territories_1870_1870_ongoing',
        'canada_french_1608_1763', 'newfoundland_1497_1949',
        'northern_territory_1911_ongoing', 'australian_capital_territory_1911_ongoing',
        'australia_1901_1942', 'louisiana_french_1682_1762',
        'uganda_protectorate_1894_1962', 'somaliland_protectorate_1884_1960',
        'anglo_egyptian_sudan_1899_1956', 'james_island_gambia_1661_1779',
        'southern_rhodesia_1901_1980', 'northern_rhodesia_1911_1964',
        'northern_rhodesia_post_federation_1963',
        'mandatory_palestine_1920_1948', 'kuwait_protectorate_1899_1961',
        'british_hong_kong_1842_1997', 'singapore_1824_1965', 'malaya_1824_1963',
        'indian_empire_(british_raj)_1613_1947', 'east_india_company_pre_territorial_1612_1757',
        'fort_st_george_madras_1640_1857', 'british_guyana_1831_1966',
    }

    # ── DEDUPLICATE EDGES ──
    seen = set()
    deduped = []
    for e in edges:
        key = f"{e['source']}->{e['target']}:{e['type']}"
        if key not in seen:
            seen.add(key)
            deduped.append(e)
    edges = deduped

    # ── FILTER ──
    nodes = [n for n in nodes if n.get('name') and n.get('est') and n['id'] not in REMOVE_IDS]
    node_ids = {n['id'] for n in nodes}

    edges = [e for e in edges if
             e['source'] != e['target'] and
             e['source'] not in REMOVE_IDS and
             e['target'] not in REMOVE_IDS and
             f"{e['source']}->{e['target']}" not in REMOVE_EDGES_SET and
             e['source'] in node_ids and
             e['target'] in node_ids]

    # ── REGION MAPPING ──
    AFRICA_SUBREGIONS = {
        'cape_colony_dutch_1652_1795': 'Southern Africa',
        'cape_colony_british_1795_1803_1795_1803': 'Southern Africa',
        'cape_colony_dutch_restored_1803_1806': 'Southern Africa',
        'cape_colony_british_1806_1910': 'Southern Africa',
        'natalia_republic_1839_1843': 'Southern Africa',
        'colony_of_natal_1843_1910': 'Southern Africa',
        'orange_river_sovereignty_1848_1854': 'Southern Africa',
        'south_african_republic_transvaal_1852_1877': 'Southern Africa',
        'orange_free_state_1854_1900': 'Southern Africa',
        'basutoland_1868_1966': 'Southern Africa',
        'griqualand_west_1871_1880': 'Southern Africa',
        'transvaal_colony_first_british_1877_1881': 'Southern Africa',
        'south_african_republic_restored_1881_1900': 'Southern Africa',
        'bechuanaland_protectorate_1884_1966': 'Southern Africa',
        'british_bechuanaland_1885_1895': 'Southern Africa',
        'zululand_1887_1897': 'Southern Africa',
        'british_south_africa_company_territory_1889_1923': 'Southern Africa',
        'orange_river_colony_1900_1910': 'Southern Africa',
        'transvaal_colony_second_british_1900_1910': 'Southern Africa',
        'swaziland_1903_1968': 'Southern Africa',
        'union_of_south_africa_1910_1961': 'Southern Africa',
        'southern_rhodesia_colony_1923_1953': 'Southern Africa',
        'northern_rhodesia_colony_1924_1953': 'Southern Africa',
        'federation_of_rhodesia_and_nyasaland_1953_1963': 'Southern Africa',
        'southern_rhodesia_post_federation_1963': 'Southern Africa',
        'northern_rhodesia_post_federation_1964': 'Southern Africa',
        'rhodesia_udi_1965_1979': 'Southern Africa',
        'zimbabwe_rhodesia_1979_1979': 'Southern Africa',
        'southern_rhodesia_restored_1979_1980': 'Southern Africa',
        'british_central_africa_protectorate_1891_1907': 'Southern Africa',
        'nyasaland_1891_1964': 'Southern Africa',
        'nyasaland_post_federation_1963': 'Southern Africa',
        # West Africa
        'james_island_trading_post_1661_1816': 'West Africa',
        'cape_coast_castle_1664_1821': 'West Africa',
        'gambia_colony_1816_1888': 'West Africa',
        'british_gold_coast_1821_1874': 'West Africa',
        'gold_coast_colony_1874_1957': 'West Africa',
        'oil_rivers_protectorate_1885_1893': 'West Africa',
        'royal_niger_company_territory_1886_1900': 'West Africa',
        'lagos_protectorate_1887_1906': 'West Africa',
        'gambia_colony_and_protectorate_1816_1965': 'West Africa',
        'niger_coast_protectorate_1893_1900': 'West Africa',
        'ashanti_1901_1957': 'West Africa',
        'southern_nigeria_protectorate_1900_1914': 'West Africa',
        'northern_nigeria_1900_1914': 'West Africa',
        'colony_and_protectorate_of_nigeria_1914_1960': 'West Africa',
        'british_cameroons_1916_1961': 'West Africa',
        'british_togoland_1919_1957': 'West Africa',
        'province_of_freedom_1787_1792': 'West Africa',
        'sierra_leone_company_settlement_1792_1808': 'West Africa',
        'sierra_leone_colony_1808_1896': 'West Africa',
        'sierra_leone_colony_and_protectorate_1787_1961': 'West Africa',
        # East Africa
        'imperial_british_east_africa_company_territory_1888_1895': 'East Africa',
        'zanzibar_1890_1963': 'East Africa',
        'uganda_1894_1962': 'East Africa',
        'east_africa_protectorate_1895_1920': 'East Africa',
        'german_east_africa_british_occupied_1916_1922': 'East Africa',
        'kenya_colony_and_protectorate_of_1920_1963': 'East Africa',
        'tanganyika_territory_1922_1961': 'East Africa',
        'tanganyika_1961_1964': 'East Africa',
        'zanzibar_independent_1963_1964': 'East Africa',
        'tanzania_1964': 'East Africa',
        # Africa (Islands)
        'fernando_po_british_1827_1843': 'Africa (Islands)',
        'st._helena_1659_ongoing': 'Africa (Islands)',
        'ascension_island_1815_ongoing': 'Africa (Islands)',
        'tristan_da_cunha_1816_ongoing': 'Africa (Islands)',
        'isle_de_france_british_occupation_1810_1814': 'Africa (Islands)',
        'mauritius_1814_1968': 'Africa (Islands)',
        'seychelles_mauritius_dependency_1814_1903': 'Africa (Islands)',
        'rodrigues_1814_1968': 'Africa (Islands)',
        'seychelles_1903_1976': 'Africa (Islands)',
        'aldabra_islands_1903_1965': 'Africa (Islands)',
        'farquhar_islands_1903_1965': 'Africa (Islands)',
        'desroches_islands_1903_1965': 'Africa (Islands)',
        # Middle East
        'egypt_1882_1922': 'Middle East',
        'sudan_anglo-egyptian_1899_1956': 'Middle East',
        'british_somaliland_1884_1960': 'Middle East',
        'aden_1839_1963': 'Middle East',
        'aden_colony_1937_1967': 'Middle East',
        'aden_protectorate_1839_1967': 'Middle East',
        'south_yemen_1967_1990': 'Middle East',
        'socotra_island_1886_1967': 'Middle East',
        'bahrain_protectorate_1861_1971': 'Middle East',
        'kuwait_1899_1961': 'Middle East',
        'qatar_protectorate_1916_1971': 'Middle East',
        'trucial_states_1820_1971': 'Middle East',
        'muscat_and_oman_protectorate_1891_1971': 'Middle East',
        'palestine_1920_1948': 'Middle East',
        'transjordan_1922_1946': 'Middle East',
        'mesopotamia_british_occupied_1914_1920': 'Middle East',
        'mandatory_iraq_1920_1932': 'Middle East',
        'iraq_1932_ongoing': 'Middle East',
        # South Asia
        'bengal_presidency_company_1757_1858': 'South Asia',
        'madras_presidency_company_1640_1858': 'South Asia',
        'bombay_presidency_company_1687_1858': 'South Asia',
        'bengal_presidency_crown_1858_1912': 'South Asia',
        'madras_presidency_crown_1858_1947': 'South Asia',
        'bombay_presidency_crown_1858_1947': 'South Asia',
        'punjab_province_1849_1947': 'South Asia',
        'central_provinces_1861_1947': 'South Asia',
        'united_provinces_1877_1947': 'South Asia',
        'assam_province_1874_1905': 'South Asia',
        'north_west_frontier_province_1901_1947': 'South Asia',
        'eastern_bengal_and_assam_1905_1912': 'South Asia',
        'bengal_province_partitioned_1905_1912': 'South Asia',
        'bengal_province_reunited_1912_1947': 'South Asia',
        'bihar_and_orissa_1912_1947': 'South Asia',
        'assam_bengal_presidency_1826_1874': 'South Asia',
        'baluchistan_1877_1947': 'South Asia',
        'assam_province_restored_1912_1947': 'South Asia',
        'dominion_of_india_1947_1950': 'South Asia',
        'dominion_of_pakistan_1947_1956': 'South Asia',
        'lower_burma_1824_1886': 'South Asia',
        'burma_british_india_1886_1937': 'South Asia',
        'burma_separate_colony_1937_1948': 'South Asia',
        'ceylon_1795_1948': 'South Asia',
        'factory_at_surat_1612_1857': 'South Asia',
        'coorg_province_1834_1947': 'South Asia',
        'ajmer_merwara_1818_1947': 'South Asia',
        'sind_province_1843_1947': 'South Asia',
        'andaman_and_nicobar_islands_1789_1947': 'South Asia',
        'maldives_protectorate_1887_1965': 'South Asia',
        'chagos_islands_mauritius_dependency_1814_1965': 'South Asia',
        'fort_william_calcutta_1696_1857': 'South Asia',
        # Southeast Asia
        'hong_kong_1841_1997': 'Southeast Asia',
        'penang_prince_of_wales_island_1786_1826': 'Southeast Asia',
        'singapore_settlement_1819_1826': 'Southeast Asia',
        'malacca_settlement_1824_1826': 'Southeast Asia',
        'straits_settlements_1826_1946': 'Southeast Asia',
        'labuan_1846_1963': 'Southeast Asia',
        'federated_malay_states_1895_1946': 'Southeast Asia',
        'unfederated_malay_states_1909_1946': 'Southeast Asia',
        'british_north_borneo_1882_1946': 'Southeast Asia',
        'north_borneo_crown_colony_1946_1963': 'Southeast Asia',
        'sarawak_1841_1946': 'Southeast Asia',
        'sarawak_crown_colony_1946_1963': 'Southeast Asia',
        'malayan_union_1946_1948': 'Southeast Asia',
        'federation_of_malaya_1948_1957': 'Southeast Asia',
        'malaya_independent_1957_1963': 'Southeast Asia',
        'singapore_crown_colony_1946_1963': 'Southeast Asia',
        'brunei_protectorate_1888_1984': 'Southeast Asia',
        'malaysia_1963': 'Southeast Asia',
        'singapore_independent_1965': 'Southeast Asia',
        'weihaiwei_1898_1930': 'Southeast Asia',
        'bencoolen_bengkulu_1685_1824': 'Southeast Asia',
        'java_british_occupation_1811_1816': 'Southeast Asia',
        'moluccas_british_occupation_1810_1817': 'Southeast Asia',
        'banda_islands_british_occupation_1810_1817': 'Southeast Asia',
        'netherlands_east_indies_british_administration_1945_1946': 'Southeast Asia',
        'shanghai_international_settlement_1863_1943': 'Southeast Asia',
        'macao_british_co_administration_1622_1623': 'Southeast Asia',
        # Pacific (Guano/Whaling)
        'campbell_island_whaling_1810_1860': 'Pacific (Guano/Whaling)',
        'norfolk_island_whaling_station_1830_1870': 'Pacific (Guano/Whaling)',
        'swains_island_1856_1925': 'Pacific (Guano/Whaling)',
        'howland_island_1857_1898': 'Pacific (Guano/Whaling)',
        'jarvis_island_1857_1898': 'Pacific (Guano/Whaling)',
        'christmas_island_line_islands_1857_1979': 'Pacific (Guano/Whaling)',
        'enderbury_island_1860_1979': 'Pacific (Guano/Whaling)',
        'mckean_island_1860_1979': 'Pacific (Guano/Whaling)',
        'birnie_island_1860_1979': 'Pacific (Guano/Whaling)',
        'rawaki_phoenix_island_1860_1979': 'Pacific (Guano/Whaling)',
        'manra_sydney_island_1860_1979': 'Pacific (Guano/Whaling)',
        'starbuck_island_1866_1979': 'Pacific (Guano/Whaling)',
        'vostok_island_1866_1979': 'Pacific (Guano/Whaling)',
        'flint_island_1866_1979': 'Pacific (Guano/Whaling)',
        'caroline_island_1868_1979': 'Pacific (Guano/Whaling)',
        'baker_island_1855_1898': 'Pacific (Guano/Whaling)',
        'ducie_island_1902_ongoing': 'Pacific (Guano/Whaling)',
        'oeno_island_1902_ongoing': 'Pacific (Guano/Whaling)',
    }

    for n in nodes:
        if n['id'] in AFRICA_SUBREGIONS:
            n['region'] = AFRICA_SUBREGIONS[n['id']]

    # ── GROUP BY REGION ──
    by_region = defaultdict(list)
    for n in nodes:
        by_region[n['region']].append(n)

    # Build edge index
    edge_by_node = defaultdict(list)
    for e in edges:
        edge_by_node[e['source']].append(e)
        edge_by_node[e['target']].append(e)

    # Output
    for region in sorted(by_region.keys()):
        rnodes = sorted(by_region[region], key=lambda n: (n['est'], n.get('ind') or 9999))
        region_ids = {n['id'] for n in rnodes}
        region_edges = [e for e in edges if e['source'] in region_ids or e['target'] in region_ids]
        # Deduplicate
        seen_edges = set()
        unique_edges = []
        for e in region_edges:
            key = f"{e['source']}->{e['target']}"
            if key not in seen_edges:
                seen_edges.add(key)
                unique_edges.append(e)

        print(f"\n{'='*80}")
        print(f"REGION: {region} ({len(rnodes)} nodes, {len(unique_edges)} edges)")
        print(f"{'='*80}")
        print(f"\n### Nodes")
        for n in rnodes:
            ind = n.get('ind') or 'ongoing'
            qid = n.get('qid', '?')
            typ = n.get('type', '?')
            print(f"  {n['id']}: {n['name']} ({n['est']}-{ind}) [{typ}] QID={qid}")

        print(f"\n### Edges (within and cross-region)")
        for e in unique_edges:
            src_in = '(local)' if e['source'] in region_ids else '(external)'
            tgt_in = '(local)' if e['target'] in region_ids else '(external)'
            # Get node names
            src_node = next((n for n in nodes if n['id'] == e['source']), None)
            tgt_node = next((n for n in nodes if n['id'] == e['target']), None)
            src_name = src_node['name'] if src_node else e['source']
            tgt_name = tgt_node['name'] if tgt_node else e['target']
            print(f"  {src_name} --[{e['type']}]--> {tgt_name} {src_in}{tgt_in}")


if __name__ == '__main__':
    main()

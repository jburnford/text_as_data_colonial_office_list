# Federated Territories Colonial Office List - Extraction Guide

## Overview

This guide provides instructions for extracting personnel data from Colonial Office List files covering **federated colonial groupings** -- territories where multiple sub-territories are administered under a single umbrella government. These are the most structurally complex files in the corpus because a single source document contains officials belonging to different sub-territories, and the extraction must correctly attribute each official to the appropriate sub-territory.

**Target Model**: Gemini 3 Flash Preview (via API)

**Key Challenge**: Each file contains personnel from MULTIPLE sub-territories. The extraction must:
1. Identify which sub-territory each official belongs to
2. Use the sub-territory name in the `department` field
3. Distinguish federal-level officials from sub-territory officials

---

## Colonies in This Group

| Federation | Sub-Territories | Years in Corpus |
|------------|----------------|-----------------|
| Leeward Islands | Antigua, Dominica (to 1940), Montserrat, St Christopher-Nevis, Virgin Islands | 1877-1959 |
| Windward Islands | Grenada, St Lucia, St Vincent, Tobago (to 1889), Dominica (from 1940) | 1877-1959 |
| Federated Malay States | Perak, Selangor, Negri Sembilan, Pahang | 1906-1925+ |
| Federation of Malaya | (successor to FMS/UMS) | 1948-1958 |
| High Commission Territories | Basutoland, Bechuanaland Protectorate, Swaziland | 1958-1964 |
| Federation of Rhodesia and Nyasaland | Southern Rhodesia, Northern Rhodesia, Nyasaland | 1954-1962 |
| West African Settlements | Sierra Leone, Gold Coast, Gambia, Lagos | 1867-1883 |

---

## Historical Context & Administrative Evolution

### Leeward Islands

| Era | Characteristics |
|-----|-----------------|
| 1871 | Federated by Imperial Act 34 & 35 Vict. cap. 107; six presidencies under one Governor |
| 1871-1882 | Six presidencies: Antigua, St Christopher, Nevis, Dominica, Montserrat, Virgin Islands |
| 1882 | St Christopher and Nevis united into one presidency (Federal Act No. 2 of 1882) |
| 1904 | Sombrero added to colony, attached to Virgin Islands |
| 1940 | Dominica transferred to Windward Islands -- now four presidencies |
| 1956-1958 | Federation winding down as islands gain separate administrations |

**Structure**: One Governor (seated at Antigua), with Administrators in each presidency. Federal-level officials (Governor, Colonial Secretary, Attorney-General, Auditor-General, Chief Justice) serve the whole colony. Each presidency has its own local civil establishment.

### Windward Islands

| Era | Characteristics |
|-----|-----------------|
| 1764 | First grouping: Grenada, Dominica, St Vincent, Tobago under one Governor |
| 1885 | Letters Patent reconstitute the Government: Grenada (HQ), St Lucia, St Vincent |
| 1889 | Tobago united with Trinidad (removed from Windward Islands) |
| 1940 | Dominica added from Leeward Islands; now four colonies |

**Structure**: Governor resident at St George's, Grenada. Each island has an Administrator (originally called Colonial Secretary). No common legislature, laws, revenue, or tariff -- looser federation than Leeward Islands.

### Federated Malay States (FMS)

| Era | Characteristics |
|-----|-----------------|
| 1874 | British Residents appointed to Perak, Selangor, Sungei Ujong |
| 1895 | Treaty of Federation signed; Resident-General appointed |
| 1896 | Federation formally constituted: Perak, Selangor, Negri Sembilan, Pahang |
| 1909 | Federal Council created; Resident-General title changed to Chief Secretary |
| 1948 | Replaced by Federation of Malaya |

**Structure**: High Commissioner (= Governor of Straits Settlements) over Chief Secretary, with British Residents in each state. Federal departments serve all four states. Currency is the Straits Settlements dollar.

### High Commission Territories

| Era | Characteristics |
|-----|-----------------|
| 1868-1966 | Basutoland, Bechuanaland Protectorate, Swaziland under High Commissioner |
| 1958+ | Appear in Colonial Office List as staffs are interchangeable with colonial territories |

**Structure**: High Commissioner (also High Commissioner for UK in South Africa) with Resident Commissioners for each territory. Common judiciary (Chief Justice serves all three).

---

## Regional Divisions (CRITICAL)

### How Sub-Territories Appear in Source Files

The files use section headers to mark transitions between sub-territories. These headers are the PRIMARY signal for determining which sub-territory an official belongs to.

#### Leeward Islands Pattern
Federal officials appear first under "General Establishment of the Leeward Islands" or "Civil Establishment", then each presidency is introduced with a capitalized header:

```
General Establishment of the Leeward Islands.
  [federal officials here]

ANTIGUA.
  [Antigua local officials here]

ST. CHRISTOPHER AND NEVIS.
  [St Kitts-Nevis local officials here]

DOMINICA.
  [Dominica local officials here]

MONTSERRAT.
  [Montserrat local officials here]

VIRGIN ISLANDS.
  [Virgin Islands local officials here]
```

#### Windward Islands Pattern
Federal officials appear first under "Civil Establishment", then each colony has its own section:

```
Civil Establishment.
Governor and Commander-in-Chief of the Windward Islands, Sir C. A. Moloney, K.C.M.G., 2,500l.
  [federal officials here]

GRENADA.
  [Grenada local officials here]

ST. LUCIA.
  [St Lucia officials here]

ST. VINCENT.
  [St Vincent officials here]
```

#### Federated Malay States Pattern
Federal officers appear first, then each state has its own section:

```
ESTABLISHMENTS OF THE MALAY STATES.

Federal Officers.
  [federal/central officials here]

Perak.
  [Perak officials here]

Selangor.
  [Selangor officials here]

Negri Sembilan.
  [Negri Sembilan officials here]

Pahang.
  [Pahang officials here]

Officers of the Cadet Service.
  [graded list across all states]
```

#### High Commission Territories Pattern
High Commissioner's Office comes first, then each territory:

```
HIGH COMMISSIONER'S OFFICE
  [central officials here]

JUDICIARY
  [common judiciary]

BASUTOLAND
  [Basutoland officials here]

BECHUANALAND PROTECTORATE
  [Bechuanaland officials here]

SWAZILAND
  [Swaziland officials here]
```

---

## File Organization in Corpus

Files appear in two forms:

1. **Combined files** (`is_federated_multi: true`): A single file containing ALL sub-territories (e.g., `THE_LEEWARD_ISLANDS.txt` with Antigua, St Kitts, Dominica, etc. all inside)
2. **Split files** (`is_federated_multi: false`): Separate files per sub-territory (e.g., `LEEWARD_ISLANDS___ANTIGUA.txt`, `LEEWARD_ISLANDS___DOMINICA.txt`)

For combined files, the extraction script MUST track which section of the file is being processed to correctly assign the `department` and `region` fields.

For split files, the sub-territory is indicated by the filename itself (e.g., `WINDWARD_ISLANDS_GRENADA.md`).

---

## Data Schema

### Official Record Structure

Refer to `guides/schema.py` for the complete schema. There are **20 fields** (5 required, 15 optional):

```python
{
    # REQUIRED (5 fields)
    "name": "Sir F. Fleming",             # Name as appears in source
    "canonical_name": "Fleming, F.",       # "Surname, Given Names"
    "surname": "Fleming",
    "position": "Governor",
    "department": "General Establishment - Leeward Islands",

    # OPTIONAL (15 fields)
    "given_names": "F.",
    "salary_min": 2600,
    "salary_max": 2600,
    "salary_currency": "GBP",            # GBP for pounds; "SSd" for Straits dollars
    "salary_scale": None,
    "allowances": None,
    "duty_allowance": None,
    "expatriation_pay": None,
    "per_diem": None,
    "acting_status": None,
    "honors": ["K.C.M.G."],
    "qualifications": [],
    "military_rank": None,
    "location": None,
    "region": None,                       # Sub-territory: "Antigua", "Perak", etc.
}
```

### Department Naming Convention

The `department` field MUST follow this pattern:

```
[Department Name] - [Federation Name]          # For federal-level officials
[Department Name] - [Sub-Territory Name]       # For sub-territory officials
```

Examples:
```
"General Establishment - Leeward Islands"       # Federal-level Governor
"Civil Establishment - Antigua"                  # Antigua local officials
"Treasury and Customs - Grenada"                 # Grenada treasury staff
"Medical - St Vincent"                           # St Vincent medical officers
"Federal Officers - Federated Malay States"      # FMS federal officers
"British Resident - Perak"                       # Perak state officers
"Resident Commissioner - Basutoland"             # Basutoland officials
```

### Region Field

The `region` field captures the sub-territory name. For federated territories this is critical:

| Federation | Valid region values |
|------------|-------------------|
| Leeward Islands | `"Antigua"`, `"St Christopher and Nevis"`, `"Dominica"`, `"Montserrat"`, `"Virgin Islands"` |
| Windward Islands | `"Grenada"`, `"St Lucia"`, `"St Vincent"`, `"Tobago"`, `"Dominica"` |
| Federated Malay States | `"Perak"`, `"Selangor"`, `"Negri Sembilan"`, `"Pahang"` |
| High Commission Territories | `"Basutoland"`, `"Bechuanaland"`, `"Swaziland"` |

For **federal-level** officials (Governor, Colonial Secretary, Chief Justice, etc.), set `region` to `None`.

---

## Department List by Era

### Leeward Islands

#### Federal Departments (all eras)
- General Establishment - Leeward Islands
- Executive Council - Leeward Islands
- General Legislative Council - Leeward Islands
- Judicial Establishment - Leeward Islands

#### Sub-Territory Departments (Antigua example, 1870s-1900s)
- Executive Council - Antigua
- Legislative Council - Antigua
- Civil Establishment - Antigua
- Medical - Antigua
- Clergy - Antigua

#### Sub-Territory Departments (St Christopher and Nevis example)
- Executive Council - St Christopher and Nevis
- Legislative Council - St Christopher and Nevis
- Civil Establishment - St Christopher and Nevis
- Medical - St Christopher and Nevis
- Police - St Christopher and Nevis

### Windward Islands

#### Federal Departments
- Civil Establishment - Windward Islands
- Court of Appeal - Windward Islands
- Lunatic Asylum - Windward Islands (at St George's, Grenada)

#### Sub-Territory Departments (Grenada example)
- Executive Council - Grenada
- Legislative Council - Grenada
- Secretariat - Grenada
- Treasury and Customs - Grenada
- Works - Grenada
- Medical - Grenada
- Police, Excise, and Prisons - Grenada
- Education - Grenada
- Judicial - Grenada
- Agricultural - Grenada
- Telephones - Grenada

### Federated Malay States

#### Federal Departments
- Federal Officers - Federated Malay States
- Federal Council - Federated Malay States
- Railways - Federated Malay States
- Posts and Telegraphs - Federated Malay States
- Education - Federated Malay States
- Forests - Federated Malay States
- Police - Federated Malay States
- Medical - Federated Malay States
- Lands - Federated Malay States
- Audit - Federated Malay States
- Museums - Federated Malay States
- Officers of the Cadet Service - Federated Malay States

#### State Departments (Perak example)
- British Resident - Perak
- District Officers - Perak
- Medical - Perak
- Education - Perak

### High Commission Territories

#### Central Departments
- High Commissioner's Office - High Commission Territories
- Judiciary - High Commission Territories

#### Territory Departments (Basutoland example)
- Resident Commissioner - Basutoland
- Agriculture and Livestock - Basutoland
- Audit - Basutoland
- Education - Basutoland
- Medical - Basutoland
- Police - Basutoland
- Posts and Telegraphs - Basutoland
- Public Works - Basutoland

---

## Salary Format Patterns with Real Examples

### Leeward Islands (Pounds Sterling)

#### Early Era (1877-1920s) -- "l." notation
```
Governor, George Berkeley, C.M.G., 3,000l.
    -> salary_min: 3000, salary_max: 3000

Private Secretary, Gilbert T. Carter, R.N., 300l.
    -> salary_min: 300, salary_max: 300

Colonial Secretary, G. Melville, C.M.G., 800l. (and 60l. from Antigua funds).
    -> salary_min: 800, salary_max: 800, allowances: "60l. from Antigua funds"

Clerks to Auditor-General, D. S. McGregor, 150l. to 200l.
    -> salary_min: 150, salary_max: 200

Inspector-General of Police, Capt. J. H. Learmouth, salary, 400l., travelling allowance, 100l., horse allowance, 60l.
    -> salary_min: 400, salary_max: 400, allowances: "travelling allowance, 100l., horse allowance, 60l."
```

#### Later Era (1946) -- No salaries in some files
The 1946 Leeward Islands file lists officials without salary amounts in many sections. When salaries are absent, set `salary_min` and `salary_max` to `None`.

### Windward Islands (Pounds Sterling)

```
Governor and Commander-in-Chief of the Windward Islands, Sir C. A. Moloney, K.C.M.G., 2,500l.
    -> salary_min: 2500, salary_max: 2500

Colonial Secretary and Registrar-General, Edward Drayton, 600l.
    -> salary_min: 600, salary_max: 600

Curator, Bot. Gardens, W. E. Broadway, 150l., to 200l., and 5l. allowances.
    -> salary_min: 150, salary_max: 200, allowances: "5l. allowances"
```

#### "Ditto" abbreviations in salary lines
```
Third ditto, L. T. Kerr, 120l.        -> position: "Third Clerk" (resolved from context)
Fourth ditto, J. E. T. Brathwaite, 110l.  -> position: "Fourth Clerk"
```

### Federated Malay States (Straits Dollars)

**IMPORTANT**: FMS salaries are in **Straits Settlements dollars** ($), not pounds sterling. Set `salary_currency` to `"SSd"`.

```
Chief Secretary to Government, $26,400, W. G. Maxwell, C.M.G.
    -> salary_min: 26400, salary_max: 26400, salary_currency: "SSd"

Secretary to High Commissioner, $9,900 to $11,400, M. E. Sherwood, M.B.E. (acting).
    -> salary_min: 9900, salary_max: 11400, salary_currency: "SSd", acting_status: "Acting"

District Officers—
Larut, $9,900 to $11,400.
    -> salary_min: 9900, salary_max: 11400, salary_currency: "SSd", location: "Larut"
```

**FMS Salary Pattern**: Note the distinctive format where the salary appears BEFORE the name:
```
[Position], $[amount], [Name], [honors]
```
This is opposite from the Caribbean pattern of `[Position], [Name], [amount]l.`

### High Commission Territories (1958)

The 1958 file lists officials by position and name but without individual salaries:
```
RESIDENT COMMISSIONER—A. G. T. Chaplin, C.M.G.
Deputy Resident Commissioner and Government Secretary—G. M. Hector, O.B.E.
Financial Secretary—E. C. Allen, O.B.E.
```
Set `salary_min` and `salary_max` to `None` for these entries.

---

## Special Patterns

### Ditto Marks -- Resolve to Full Position Name

```
Second Puisne Judge ditto, J. R. Semper, 1,200l.
    -> position: "Second Puisne Judge" (from context: "Chief Justice of the Supreme Court" above)
    Note: "ditto" here refers to "of the Supreme Court"

Second ditto, E. G. M. Dupigny, 100l.
    -> position: "Second Landing Waiter" (from "First Landing Waiter" above)

Third ditto, W. Thompson, 75l.
    -> position: "Third Landing Waiter"
```

Also watch for double-comma ditto notation:
```
1st Puime Judge ditto, J. R. Semper, 1,200l.
2nd ditto, ditto, S. Pemberton, 800l.
    -> position: "2nd Puisne Judge of the Supreme Court"
```

### Multi-Person Lines

#### Comma-separated list with shared salary
```
Clerks, W. M. Gordon, 150l. (and 150l. as Clerk of Federal and Antigua Legislative Councils); E. B. Jarvis, 100l. (and 50l. from local (Antigua) funds); G. O. Nugent, 100l.; H. F. Holme, 25l. and 50l. from local (Antigua) funds.
```
Creates FOUR officials, each with "Clerk" as position, but with DIFFERENT salaries. Parse each semicolon-separated entry independently.

#### Named lists in the Malay Cadet Service
```
Class I (Grade A).
Salary $14,400.
H. A. Smallwood, G. P. Bradney, E. C. H. Wolff, W. Peel, W. S. Gibson.
```
Creates FIVE officials, ALL with position "Cadet Officer, Class I Grade A", salary_min: 14400, salary_max: 14400.

#### Revenue officers with shared salary pattern
```
Revenue Officers:
A. Webster, 200l.; E. H. Moore, 150l.; E. T. Wilson, 75l.; A. N. Comissiong, 130l.; I. H. Otway, 120l.; J. F. E. Roberts, 120l.; H. L. Otway, R. M. D. Charles, F. C. Rudder, 100l. each.
```
Creates NINE officials. The last three share the "100l. each" salary.

### Acting Status

```
Rev. M. I. Drinkwater (acting), 500l.
    -> acting_status: "Acting"

C. W. H. Cochrane (acting).
    -> acting_status: "Acting"

M. E. Sherwood, M.B.E. (acting).
    -> acting_status: "Acting"

F. A. S. McClelland (acting).
    -> acting_status: "Acting"
```

### Vacant Positions

#### Early Era: Note but skip unnamed vacancies
```
Second Puisne Judge (vacant), 700l.
    -> SKIP or create entry with name: null (preserves salary data)
```

#### Later Era: Capture with salary
```
Deputy Director of Public Works—(Vacant).
    -> name: null, position: "Deputy Director of Public Works", department: "Public Works - Bechuanaland"
```

### Council Members Without Salary

Executive and Legislative Council members are often listed without salary:
```
Elective Members.

Antigua—
J. J. Camacho.
J. F. Foote.
John Maginley.
Martin J. Camacho.
```
These should still be extracted with `position: "Elective Member, General Legislative Council"` and `department: "General Legislative Council - Leeward Islands"`, `region: "Antigua"`.

### Dual Roles / Salary from Multiple Funds

```
President and Island Secretary, The Colonial Secretary of the Leeward Islands, 50l. (Geo. Melville, C.M.G.)
    -> name: "Geo. Melville", position: "President and Island Secretary", salary_min: 50
    Note: This person is also the Colonial Secretary at the federal level

Clerks, Edward B Jarvis, 50l.; H. F. Holme, 50l.
    -> Two officials, each with salary 50l. in the Antigua establishment
    Note: Jarvis also draws 100l. from federal funds (listed separately)
```

---

## Location/Region Extraction Rules

### Location from Position Title

```
District Magistrates, W. H. Whyham, 400l.
    -> position: "District Magistrate", location: None (no specific district named)

Assistants to Attorney-General, G. K. T. Purcell (St. Kitts), 200l.
    -> position: "Assistant to Attorney-General", location: "St Kitts", region: "St Christopher and Nevis"

Assistants to Attorney-General, E. St. J. Branch (Dominica), 200l.
    -> position: "Assistant to Attorney-General", location: "Dominica", region: "Dominica"
```

### Location from Section Header

```
ANTIGUA.
...
Civil Establishment.
Treasurer and Collector of Customs, W. D. Auchinleck, 500l.
    -> department: "Civil Establishment - Antigua", region: "Antigua"
```

### FMS District Officers -- Location from Line

```
District Officers—
Larut, $9,900 to $11,400.
Krian, $8,400 to $9,600.
Kuala Kangsar, $9,900 to $11,400.
```
Each becomes a District Officer with the district as `location` and the state (Perak) as `region`.

### Known Locations by Federation

**Leeward Islands**: St John (Antigua), Basseterre (St Kitts), Charlestown (Nevis), Roseau (Dominica), Plymouth (Montserrat), Road Town (Tortola/Virgin Islands), Anguilla

**Windward Islands**: St George's (Grenada), Castries (St Lucia), Kingstown (St Vincent), Grenville (Grenada), Carriacou (Grenada dependency)

**Federated Malay States**: Kuala Lumpur (Selangor, FMS HQ), Taiping (Perak HQ), Ipoh (Perak), Kuala Kangsar (Perak), Seremban (Negri Sembilan), Kuala Lipis (Pahang), Port Swettenham (Selangor), Klang (Selangor), Port Dickson (Negri Sembilan)

**High Commission Territories**: Maseru (Basutoland), Mafeking/Gaberones (Bechuanaland), Mbabane (Swaziland)

---

## Era-Specific Extraction Notes

### 1867-1883 (West African Settlements / Early Leewards & Windwards)

- **West African Settlements**: Sierra Leone, Gold Coast, Gambia, Lagos grouped loosely
- **Leeward Islands**: Federal Act of 1871 creates formal federation; early files may be very long with extensive historical/constitutional text before personnel section
- **Personnel section**: Look for "Civil Establishment" or "General Establishment" heading
- **Salaries**: Consistently in "Xl." format
- **Expected officials per file**: 20-60 for Leewards, 10-30 for Windwards

### 1886-1910 (Mature Caribbean Federations)

- **Split vs Combined files**: Some years split into separate files per presidency (1888, 1898, 1910); other years combine all in one file
- **Leeward Islands**: Five or six presidencies with detailed local establishments
- **Windward Islands**: Three colonies (Grenada, St Lucia, St Vincent) under one Governor
- **FMS begins appearing**: 1906 onwards
- **Best detail years**: 1899 (Leewards have 92KB file), 1900 (96KB)
- **Expected officials**: 100-250 for Leewards combined, 50-100 for Windwards combined

### 1906-1925 (Federated Malay States Peak)

- **Currency**: Straits dollars ($), NOT pounds sterling
- **Salary format**: Amount appears BEFORE name: `[Position], $[salary], [Name]`
- **Cadet Service**: Large grouped lists of officers by class/grade with shared salary
- **Many acting appointments**: "(acting)" appears frequently
- **FMS file is very large**: Dense personnel listings across four states
- **Expected officials**: 200-400+ for FMS

### 1925-1940 (Interwar Period)

- **Leeward Islands**: Files continue to be large (80-90KB)
- **Windward Islands**: Tobago gone (to Trinidad); Dominica transferred in 1940
- **Currency transition**: Caribbean files shift from "l." to "£" notation
- **Expected officials**: 100-200 per federation

### 1940-1957 (Late Colonial)

- **Leeward Islands**: Dominica removed (to Windward Islands)
- **Windward Islands**: Dominica added as fourth colony
- **Some files lack salary data**: 1946 Leewards lists officials without salaries in many sections
- **High Commission Territories**: Begin appearing in 1958
- **Federation of Rhodesia & Nyasaland**: 1954-1962, but files are very small (stub references)
- **Expected officials**: 50-200

### 1958-1965 (Decolonization)

- **High Commission Territories**: Compact files listing department heads only
- **Leeward Islands**: Reduced to stubs (9-10KB files)
- **Federation of Rhodesia & Nyasaland**: Stub files (under 1KB) saying "See separate entries"
- **Expected officials**: 30-60 for HCT, 10-30 for shrinking federations

---

## Validation Checklist

### All Years (Federated Territories)

- [ ] Officials list is non-empty
- [ ] All entries have `name`, `canonical_name`, `surname`, `position`, and `department` fields
- [ ] Department field includes the sub-territory or federation name as suffix
- [ ] `region` field correctly identifies the sub-territory (or is `None` for federal officials)
- [ ] Federal-level officials (Governor, Colonial Secretary, Chief Justice) have federation-level department
- [ ] Sub-territory officials have sub-territory-level department
- [ ] No officials orphaned without a sub-territory assignment (unless genuinely federal)
- [ ] Salaries parsed where present
- [ ] Honors and qualifications in correct fields
- [ ] "Ditto" entries expanded to proper position names

### Leeward Islands Specific

- [ ] Governor captured (federal level, region: None)
- [ ] Colonial Secretary captured (federal level)
- [ ] Chief Justice / Puisne Judges captured (Judicial Establishment, federal level)
- [ ] Attorney-General captured (federal level)
- [ ] Auditor-General captured (federal level)
- [ ] Each presidency has at least some officials extracted
- [ ] Antigua officials have `region: "Antigua"`
- [ ] St Kitts-Nevis officials have `region: "St Christopher and Nevis"`
- [ ] Dominica officials have `region: "Dominica"` (pre-1940 only)
- [ ] Montserrat officials have `region: "Montserrat"`
- [ ] Virgin Islands officials have `region: "Virgin Islands"`

### Windward Islands Specific

- [ ] Governor captured (federal level, region: None)
- [ ] Auditor captured (federal level)
- [ ] Court of Appeal justices captured
- [ ] Grenada Administrator/Colonial Secretary captured
- [ ] St Lucia Administrator captured
- [ ] St Vincent Administrator captured
- [ ] Each colony's medical officers captured with correct region
- [ ] After 1940: Dominica officials present

### Federated Malay States Specific

- [ ] High Commissioner captured
- [ ] Chief Secretary (or Resident-General) captured
- [ ] `salary_currency` set to `"SSd"` for all FMS entries
- [ ] British Residents for each state captured with correct region
- [ ] Federal department heads captured (Railways, Posts, Police, etc.)
- [ ] Cadet Service officers extracted with correct class/grade in position
- [ ] District Officers extracted with district as location, state as region
- [ ] Salary format correctly parsed (amount before name)

### High Commission Territories Specific

- [ ] High Commissioner captured
- [ ] Resident Commissioner for each territory captured
- [ ] Chief Justice captured (serves all three territories)
- [ ] Department heads for each territory extracted
- [ ] Each territory clearly separated in output

---

## Key Positions by Federation

### Leeward Islands (Federal Level)
1. Governor (and Commander-in-Chief)
2. Private Secretary / A.D.C.
3. Colonial Secretary
4. Attorney-General
5. Auditor-General
6. Inspector of Schools
7. Inspector-General of Police
8. Chief Justice of the Supreme Court
9. Puisne Judges (1st, 2nd)

### Leeward Islands (Per Presidency)
1. Administrator (or President/Commissioner for smaller presidencies)
2. Treasurer and Collector of Customs
3. Medical Officers (by district number)
4. District Magistrates
5. Inspector of Police (local)
6. Postmaster
7. Clerk of Councils

### Windward Islands (Federal Level)
1. Governor and Commander-in-Chief
2. Chief Clerk and Private Secretary
3. Aide-de-Camp
4. Auditor

### Windward Islands (Per Colony)
1. Administrator (originally Colonial Secretary)
2. Treasurer, Comptroller of Customs and Postmaster
3. Chief of Police
4. Colonial Surgeon / Medical Officers
5. Attorney-General (local)
6. Chief Justice (local)
7. Inspector of Schools
8. Superintendent of Works

### Federated Malay States (Federal)
1. High Commissioner
2. Chief Secretary to Government (originally Resident-General)
3. Chief Judicial Commissioner
4. Legal Adviser and Public Prosecutor
5. Treasurer
6. Auditor-General
7. Commissioner of Lands
8. Commissioner of Police
9. General Manager, Railways
10. Director of Education
11. Conservator of Forests
12. Director, Posts and Telegraphs
13. Principal Medical Officer
14. Secretary for Chinese Affairs

### Federated Malay States (Per State)
1. British Resident
2. Secretary to Resident
3. State Engineer
4. Senior Medical Officer
5. District Officers (multiple, by district)
6. Protector of Chinese (Perak, Selangor)
7. Registrar of Titles

### High Commission Territories (Central)
1. High Commissioner
2. Deputy High Commissioner
3. Administrative Secretary
4. Secretary for Finance
5. Attorney-General
6. Chief Justice

### High Commission Territories (Per Territory)
1. Resident Commissioner
2. Deputy Resident Commissioner and Government Secretary
3. Financial Secretary / Treasurer
4. Director of Medical Services
5. Commissioner of Police
6. Director of Education
7. Director of Public Works
8. Director of Agriculture / Livestock

---

## Sample Output

### Leeward Islands 1899 -- Federal Official
```python
{
    "name": "Sir F. Fleming",
    "canonical_name": "Fleming, F.",
    "given_names": "F.",
    "surname": "Fleming",
    "position": "Governor",
    "department": "General Establishment - Leeward Islands",
    "salary_min": 2600,
    "salary_max": 2600,
    "salary_currency": "GBP",
    "honors": ["K.C.M.G."],
    "region": None,
}
```

### Leeward Islands 1899 -- Antigua Local Official
```python
{
    "name": "W. D. Auchinleck",
    "canonical_name": "Auchinleck, W. D.",
    "given_names": "W. D.",
    "surname": "Auchinleck",
    "position": "Treasurer and Collector of Customs",
    "department": "Civil Establishment - Antigua",
    "salary_min": 500,
    "salary_max": 500,
    "salary_currency": "GBP",
    "allowances": "Fees as Registrar of Shipping",
    "region": "Antigua",
}
```

### Windward Islands 1899 -- Grenada Official
```python
{
    "name": "Edward Drayton",
    "canonical_name": "Drayton, Edward",
    "given_names": "Edward",
    "surname": "Drayton",
    "position": "Colonial Secretary and Registrar-General",
    "department": "Secretariat - Grenada",
    "salary_min": 600,
    "salary_max": 600,
    "salary_currency": "GBP",
    "region": "Grenada",
}
```

### Windward Islands 1899 -- Grenada Ditto Resolution
```python
{
    "name": "L. T. Kerr",
    "canonical_name": "Kerr, L. T.",
    "given_names": "L. T.",
    "surname": "Kerr",
    "position": "Third Clerk",
    "department": "Treasury and Customs - Grenada",
    "salary_min": 120,
    "salary_max": 120,
    "salary_currency": "GBP",
    "region": "Grenada",
}
```

### Federated Malay States 1923 -- Federal Officer
```python
{
    "name": "W. G. Maxwell",
    "canonical_name": "Maxwell, W. G.",
    "given_names": "W. G.",
    "surname": "Maxwell",
    "position": "Chief Secretary to Government",
    "department": "Federal Officers - Federated Malay States",
    "salary_min": 26400,
    "salary_max": 26400,
    "salary_currency": "SSd",
    "honors": ["C.M.G."],
    "region": None,
}
```

### Federated Malay States 1923 -- State Officer
```python
{
    "name": "C. W. C. Parr",
    "canonical_name": "Parr, C. W. C.",
    "given_names": "C. W. C.",
    "surname": "Parr",
    "position": "British Resident",
    "department": "British Resident - Perak",
    "salary_min": 17400,
    "salary_max": 17400,
    "salary_currency": "SSd",
    "honors": ["O.B.E."],
    "military_rank": "Major",
    "region": "Perak",
}
```

### Federated Malay States 1923 -- Cadet Service
```python
{
    "name": "H. A. Smallwood",
    "canonical_name": "Smallwood, H. A.",
    "given_names": "H. A.",
    "surname": "Smallwood",
    "position": "Officer, Cadet Service Class I Grade A",
    "department": "Officers of the Cadet Service - Federated Malay States",
    "salary_min": 14400,
    "salary_max": 14400,
    "salary_currency": "SSd",
    "region": None,
}
```

### High Commission Territories 1958 -- Central
```python
{
    "name": "Sir Percivale Liesching",
    "canonical_name": "Liesching, Percivale",
    "given_names": "Percivale",
    "surname": "Liesching",
    "position": "High Commissioner",
    "department": "High Commissioner's Office - High Commission Territories",
    "honors": ["G.C.M.G.", "K.C.B.", "K.C.V.O."],
    "region": None,
}
```

### High Commission Territories 1958 -- Basutoland
```python
{
    "name": "A. G. T. Chaplin",
    "canonical_name": "Chaplin, A. G. T.",
    "given_names": "A. G. T.",
    "surname": "Chaplin",
    "position": "Resident Commissioner",
    "department": "Resident Commissioner - Basutoland",
    "honors": ["C.M.G."],
    "region": "Basutoland",
}
```

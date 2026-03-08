# Mediterranean & Atlantic Colony Group - Extraction Guide

## Overview

This guide provides instructions for extracting personnel data from Colonial Office List files for the Mediterranean & Atlantic colony group. This group is geographically diverse, spanning the Mediterranean Sea, the North Sea, and the South Atlantic. The colonies range from substantial administrations (Malta, Cyprus) to tiny outposts (Ascension, Tristan da Cunha). Several colonies in this group have unique constitutional arrangements reflecting their strategic military importance.

**Target Model**: Gemini 3 Flash Preview (via API)

**Colonies in this group**:
- Malta (1867-1965)
- Gibraltar (1867-1966)
- Cyprus (1883-1961)
- St. Helena (1867-1966)
- Ascension (dependency of St. Helena from 1922; earlier under Admiralty)
- Tristan da Cunha (dependency of St. Helena from 1938)
- Falkland Islands (1867-1966)
- Bermuda (1879-1966)
- Heligoland (1867-1890 only)
- British Antarctic Territory (1963-1966)

---

## Source Files

### Available Years and Filename Variations

Files are named variously across years:
- `malta.txt`, `MALTA.txt`, `malta.md`, `state_of_malta.txt` (1963)
- `gibraltar.txt`, `GIBRALTAR.txt`, `gibraltar.md`
- `cyprus.txt`, `cyprus.md`, `republic_of_cyprus.txt` (1961)
- `st_helena.txt`, `ST_HELENA.txt` (also contains Ascension and Tristan da Cunha entries)
- `falkland_islands.txt`, `FALKLAND_ISLANDS.txt`, `falkland_islands_and_dependencies.txt` (1950s-1960s)
- `bermuda.txt`, `bermudas.txt` (1879-1880)
- `heligoland.txt`, `HELIGOLAND.txt`
- `ascension.txt` (standalone only in some years; otherwise in st_helena.txt)
- `british_antarctic_territory.txt` (1963-1966)

---

## Historical Context & Administrative Evolution

### Malta

| Era | Characteristics |
|-----|-----------------|
| 1800-1849 | British administration established; Crown Colony |
| 1849-1887 | Council of Government (10 official, 8 elected members) |
| 1887-1903 | Reconstituted council (6 official, 13 elected) |
| 1903-1921 | Various constitutional changes |
| 1921-1933 | Self-government under Amery-Milner Constitution |
| 1933-1947 | Constitution suspended; Crown Colony rule |
| 1947-1958 | Self-government restored; Letters Patent 1947; Legislative Assembly of 40 members |
| 1958-1961 | Constitution suspended again after political crisis |
| 1961-1964 | New constitution; internal self-government |
| 1964 | Independence |

**Special features**: Malta has a dual administration structure in the late period (1947-1964) with a "Maltese Imperial Government" (defence/external affairs, under Governor) and a "Maltese Government" (internal affairs, under elected Ministers). This produces two parallel sets of officials.

### Gibraltar

| Era | Characteristics |
|-----|-----------------|
| 1704 onwards | Captured by British; ceded by Treaty of Utrecht 1713 |
| 1704-1950 | No legislature; Governor exercises all functions of government and legislation |
| 1950 onwards | Legislative Council established (Governor + 3 ex-officio + 2 nominated + 5 elected) |
| 1956 onwards | City Council established |

**Special features**: Gibraltar is a military fortress. The Governor is also the General commanding the garrison. Many positions are military rather than civil. The Colonial Office List entry is typically very short compared to other colonies. Currency changed from Spanish pesetas to British sterling in 1898.

### Cyprus

| Era | Characteristics |
|-----|-----------------|
| 1878-1914 | Ottoman territory administered by Britain; head of state titled "High Commissioner" |
| 1914 | Annexed to British Crown on outbreak of war with Turkey |
| 1923-1925 | Turkey recognized annexation by Treaty of Lausanne; formally made a Colony |
| 1925-1931 | Governor; Legislative Council (9 official, 15 elected) |
| 1931 | Disturbances; Legislative Council abolished |
| 1931-1960 | Governor legislates alone; Executive Council only |
| 1960 | Independence as Republic of Cyprus |

**Special features**: Before 1925, the head of state is "High Commissioner" not "Governor". The island is divided into six administrative districts (Nicosia, Famagusta, Larnaca, Limassol, Paphos, Kyrenia). District Commissioners are a prominent feature. Cyprus has a unique Ottoman-derived legal system with separate Muslim religious tribunals.

### St. Helena

| Era | Characteristics |
|-----|-----------------|
| 1659-1834 | Under East India Company |
| 1834 onwards | Crown Colony; Governor + Executive Council + Advisory Council |
| 1922 | Ascension becomes dependency of St. Helena |
| 1938 | Tristan da Cunha becomes dependency |

**Special features**: Very small establishment. The Governor is also ex-officio Chief Justice. Many officials hold multiple concurrent positions (e.g., "Colonial Secretary and Auditor", "Postmaster, Registrar-General, Local Auditor"). No Legislative Council -- the Governor alone makes Ordinances.

### Falkland Islands

| Era | Characteristics |
|-----|-----------------|
| 1833-1843 | Under naval officers |
| 1843 onwards | Civil administration; Governor + Executive + Legislative Council |
| 1908 | Dependencies (South Georgia, South Shetlands, etc.) formally constituted |
| 1950s | Listed as "Falkland Islands and Dependencies" |
| 1962 | British Antarctic Territory separated from Dependencies |

**Special features**: Very small establishment. The Chief Justice is the Governor ex officio. Legislative Council has unofficial members but is mostly official. South Georgia has its own Deputy Collectors and Magistrates. The Falkland Islands Company is a dominant economic presence.

### Bermuda

| Era | Characteristics |
|-----|-----------------|
| 1612 onwards | One of the oldest British colonies; self-governing |
| 1620 onwards | House of Assembly (oldest in the British colonies after Westminster) |
| Throughout | Governor + Legislative Council + House of Assembly |

**Special features**: Bermuda is self-governing with an elected House of Assembly. The Colonial Office List entry reflects this with many elected officials. The establishment is relatively large for a small island due to Bermuda's wealth and importance as a naval base.

### Heligoland

| Era | Characteristics |
|-----|-----------------|
| 1807-1814 | Surrendered to Britain; formally ceded by Denmark |
| 1864 | New constitution substituted |
| 1868 | Executive and legislative authority centred in Governor by Order in Council |
| 1890 | **Ceded to Germany** (Anglo-German Heligoland-Zanzibar Treaty) |

**Special features**: Extremely small colony (3/4 square mile). Disappears from Colonial Office Lists after 1890. German names predominate among officials. Salaries are very low. The Governor is also judge of the Court of Sessions.

### Ascension

**Not a separate colony** until 1922. Before 1922, under Admiralty supervision. After 1922, a dependency of St. Helena. Appears as a brief entry within the St. Helena file, or occasionally as a standalone file. Typically lists only the Captain (when under Admiralty) or Resident Magistrate (after 1922).

### Tristan da Cunha

A dependency of St. Helena from 1938. Appears as a brief appendix within the St. Helena file. Extremely minimal establishment -- typically just an Administrator and Medical Officer. Before the 1940s, had no formal colonial administration.

### British Antarctic Territory

Created 3 March 1962, separated from Falkland Islands Dependencies. Administered by the High Commissioner resident in Stanley, Falkland Islands. Appears in Colonial Office Lists from 1963. The "civil establishment" is essentially just the High Commissioner (who is the Governor of Falkland Islands).

---

## Regional Divisions

### Malta
- **Malta** (main island, including Valletta, Floriana, "Three Cities")
- **Gozo** (second island, with its own Deputy Comptroller, medical staff, magistrates)

### Cyprus
- **Nicosia** (capital, usually also administers Kyrenia)
- **Famagusta**
- **Larnaca**
- **Limassol**
- **Paphos**
- **Kyrenia**

### Falkland Islands
- **Stanley** (capital, East Falkland)
- **East Falkland** (including Darwin settlement)
- **West Falkland**
- **South Georgia** (dependency; has its own magistrates and customs officers)
- **South Shetlands** (dependency)

### St. Helena
- No formal administrative divisions, but note:
  - **Ascension** (dependency from 1922)
  - **Tristan da Cunha** (dependency from 1938)

---

## Data Schema

### Official Record Structure

Refer to `guides/schema.py` for the full 20-field schema. The 5 required fields are:
- `name` (str): Name as appears in source
- `canonical_name` (str): "Surname, Given Names" format
- `surname` (str): Family name
- `position` (str): Official title/role
- `department` (str): Department with colony suffix

### Department Suffix Convention

Use the colony name as suffix:
- `"Civil Establishment - Malta"`
- `"Judicial Department - Gibraltar"`
- `"Administration - Cyprus"`
- `"Civil Establishment - St Helena"`
- `"Civil Establishment - Falkland Islands"`
- `"Civil Establishment - Bermuda"`
- `"Civil Establishment - Heligoland"`

For dependencies:
- `"Civil Establishment - Ascension"`
- `"Civil Establishment - Tristan da Cunha"`
- `"Civil Establishment - South Georgia"`
- `"Civil Establishment - British Antarctic Territory"`

---

## Department List by Era

### Malta

#### 1867-1899
- Council of Government - Malta
- Civil Establishment - Malta
- Chief Secretary's Department - Malta
- Auditor-General's Department - Malta
- Custom House - Malta
- Land Revenue and Public Works Department - Malta
- Treasury - Malta
- Port Department - Malta
- Charitable Institutions Department - Malta
- Government Press - Malta
- Island Post Office - Malta
- Hospitals - Malta
- Judicial Establishment - Malta
- Public Registry - Malta
- Ecclesiastical - Malta
- University - Malta
- Primary Schools - Malta
- Police Department - Malta
- Corradino Prison - Malta
- Monte di Pieta - Malta

#### 1899-1920 (additional departments)
- Public Health Department - Malta
- Water Works and Electric Lighting Department - Malta
- Railway Department - Malta
- Educational - Malta
- Crown Lawyers - Malta
- Audit and Contract Office - Malta

#### 1946-1965 (self-government era)
- Governor and Commander-in-Chief - Malta
- Maltese Imperial Government - Malta
- The Maltese Government - Malta
- Ministers - Malta
- Legislative Assembly - Malta

### Gibraltar

#### 1867-1950 (no legislature)
- Civil Establishment - Gibraltar
- Treasury / Revenue Department - Gibraltar
- Port Department / Port Office - Gibraltar
- Public Works - Gibraltar
- Audit - Gibraltar
- Judicial Department - Gibraltar
- Postal and Telegraph Department - Gibraltar
- Medical Department - Gibraltar
- Board of Sanitary Commissioners - Gibraltar
- Ecclesiastical - Gibraltar
- Crown Property Department - Gibraltar

#### 1950 onwards (Legislative Council)
- Executive Council - Gibraltar
- Legislative Council - Gibraltar
- City Council - Gibraltar
- Civil Establishment - Gibraltar (departments as above)

### Cyprus

#### 1883-1925 (High Commissioner era)
- Executive Council - Cyprus
- Legislative Council - Cyprus
- Courts of Justice - Cyprus
- District Commissioners - Cyprus
- Chief Secretary's Office - Cyprus

#### 1925-1960 (Governor era)
- Secretariat / Administration - Cyprus
- District Administration - Cyprus
- Accountant-General - Cyprus
- Agriculture - Cyprus
- Antiquities - Cyprus
- Audit - Cyprus
- Co-operation - Cyprus
- Customs and Excise - Cyprus
- Education - Cyprus
- Forestry - Cyprus
- Inland Revenue - Cyprus
- Judicial / Supreme Court - Cyprus
- Labour - Cyprus
- Land Registration and Surveys - Cyprus
- Legal - Cyprus
- Medical and Health - Cyprus
- Police - Cyprus
- Posts - Cyprus
- Prisons - Cyprus
- Public Information - Cyprus
- Public Works - Cyprus
- Railway - Cyprus
- Supplies - Cyprus
- Water Supply and Irrigation - Cyprus

### St. Helena (all eras)
Very sparse departmental structure:
- Civil Establishment - St Helena
- Judicial Establishment - St Helena
- Military Establishment - St Helena
- Ecclesiastical Department - St Helena

### Falkland Islands (all eras)
- Executive Council - Falkland Islands
- Legislative Council - Falkland Islands
- Civil Establishment - Falkland Islands
- Colonial Secretariat - Falkland Islands
- Treasury and Customs - Falkland Islands
- Post Office - Falkland Islands
- Medical - Falkland Islands
- Judicial Department - Falkland Islands
- Educational - Falkland Islands
- Police and Prisons - Falkland Islands
- Public Works - Falkland Islands
- Port and Harbour - Falkland Islands
- Stock Department - Falkland Islands

### Heligoland (1867-1890)
- Executive Council - Heligoland
- Civil Establishment - Heligoland

---

## Salary Format Patterns with Real Examples

### Early Era (1867-1920s) - Pounds with "l."

```
Simple salary:
  "Governor, Gen. Sir Arthur Borton, K.C.B., 4,500l."
  -> salary_min: 4500, salary_max: 4500

With table allowance:
  "Governor, Gen. Sir Arthur Borton, K.C.B., 4,500l., and 500l. table allowance as Commander of the Troops."
  -> salary_min: 4500, salary_max: 4500, allowances: "500l. table allowance as Commander of the Troops"

Salary range:
  "2nd Clerk, J. C. King, 150l. to 200l."
  -> salary_min: 150, salary_max: 200

Range with extra allowance:
  "2nd Clerk, J. C. King, 150l. to 200l. (and 25l. allowance for aiding in Audit duties)."
  -> salary_min: 150, salary_max: 200, allowances: "25l. allowance for aiding in Audit duties"

With shillings and pence:
  "A.D.C., Captain N. G. Biancardi, R.M.R., 173l. 17s. 6d."
  -> salary_min: 173, salary_max: 173, allowances: "17s. 6d."

With fees:
  "Governor and Com.-in-Chief, A. C. S. Barkly, C.M.G., 800l. and fees."
  -> salary_min: 800, salary_max: 800, allowances: "fees"

Salary from multiple sources:
  "Governor, Maj.-Gen. Sir Francis W. Grenfell, G.C.M.G., K.C.B., 5,000l. (2,000l. from Imperial Funds)."
  -> salary_min: 5000, salary_max: 5000, allowances: "2,000l. from Imperial Funds"

Per diem:
  "Superintendent of Foremen, F. S. Ferrante, 6s. per day."
  -> per_diem: "6s.", salary_min: None

Increment notation:
  "Colonial Secretary, W. P. Martin, 650l. to 750l., by 25l."
  -> salary_min: 650, salary_max: 750
```

### Middle Era (1920s-1930s) - Transition to pounds with "l." and duty allowance

```
With duty allowance:
  "Governor and Commander-in-Chief, John Middleton, Esq., C.M.G., 1,300l., duty allowance, 500l., and fees."
  -> salary_min: 1300, salary_max: 1300, duty_allowance: 500, allowances: "fees"
```

### Late Era (1946-1960s) - Pounds with "£" symbol and salary ranges

```
Fixed salary:
  "Governor and Commander-in-Chief—Sir Andrew Barkworth Wright, K.C.M.G., C.B.E., M.C. £3,300 duty allowance £1,200."
  -> salary_min: 3300, salary_max: 3300, duty_allowance: 1200

Salary range:
  "Accountant—R. Stott. £480-840."
  -> salary_min: 480, salary_max: 840

Range with dash:
  "Chief Accountant—H. Heys. £720-960."
  -> salary_min: 720, salary_max: 960

Expatriation allowance note (Cyprus 1950):
  "In addition to the salaries stated, expatriate Officers receive an expatriation allowance at the rate of 15 per cent. of their salary."
  -> expatriation_pay field: calculate 15% of salary where applicable
```

### Special: No salary listed (common for small colonies)

```
"Chief Justice, The Governor, ex officio."
  -> salary_min: None, salary_max: None

"Chaplain to the Forces, Rev. W. Helps."
  -> salary_min: None, salary_max: None

"Administrator—J. P. L. Scott."
  -> salary_min: None, salary_max: None
```

---

## Special Patterns

### "Ditto" - References previous position type

```
Malta 1880:
  "Assistant and Clerk to the Council, F. Vella, 350l."
  "Assistant ditto, M. Carnana, 150l. and fees."
  -> Position: "Assistant Superintendent of the Ports"
     (ditto refers to Superintendent of the Ports from context)

  "Inspector of ditto, F. Falzon, LL.D., 50l."
  -> Position: "Inspector of Corradino Prison" (ditto refers to prison)

Gibraltar 1879:
  "1st Clerk, George Bassadone, 200l. to 275l."
  "2nd Clerk, A. C. J. King, 150l. to 200l."
  "3rd Clerk, A. Podesta, 100l. to 150l."
  -> Ordinal positions within same department

Heligoland 1890:
  "2nd " J. Berndt, 50l."
  "3rd " J. Lehmann, 45l."
  -> 2nd Teacher, 3rd Teacher (ditto from "Head Teacher" above)
```

### Acting/Temporary Status - ALWAYS CAPTURE

```
"Acting Colonial Secretary, Henry Byng."
  -> acting_status: "Acting"

"Assistant Colonial Engineer (temporary), B. S. Smith, 250l."
  -> acting_status: "Temporary"

"Commissioner, Nicosia, Maj. J. Inglis (acting), 600l."
  -> acting_status: "Acting"

"Lieutenant-Governor—(Vacant). (A. G. Lowe Acting)."
  -> Two entries: one Vacant for Lt-Governor, one for A. G. Lowe with acting_status: "Acting"
```

### Multiple People on One Line

#### Pattern 1: Comma-separated list with "each"
```
Malta 1899:
  "Second Class Clerks, George Borg Cardona, D. A. Garroni, E. L. Bonavia, Charles B. Sciortino, Edgar Arrigo, 110l. to 180l. each."
  -> Creates FIVE officials, EACH with salary_min: 110, salary_max: 180
```

#### Pattern 2: Comma-separated list without "each"
```
Malta 1899:
  "Quarantine Medical Officers, R. Carbone, M.D., 250l., F. Borg, M.D., 100l., V. Vella, M.D., 100l."
  -> Three officials with DIFFERENT salaries (look for salary indicators to split)
```

#### Pattern 3: Named with semicolons (late era)
```
Cyprus 1950:
  "Administrative Officers—I. Ll. Phillips; D. A. Shepherd; P. H. F. Dodd; M. N. Davidson. £480-960."
  -> Four officials sharing same salary range
```

#### Pattern 4: Parenthetical grouping
```
Gibraltar 1879:
  "Chief Clerk, James Davidson, 200l. to 250l.; 4 other clerks."
  -> Extract James Davidson; note "4 other clerks" but skip (no names)
```

### Vacancy Handling

#### Early Era (1867-1930s): Skip vacancies without salary
```
"Collector of Land Revenue (vacant)."
  -> SKIP

"Aide-de-Camp to the Governor, 178l. 17s. 6d. (vacant)."
  -> Create entry with name: null, salary_min: 178
```

#### Late Era (1940s-1960s): Capture vacancies with salary
```
"Chief Inspector of Schools—Vacant. £720-960."
  -> name: null, position: "Chief Inspector of Schools", salary_min: 720, salary_max: 960
```

### Em-Dash Separator (Late Era)

In late-era files (1946-1960s), positions and names are often separated by an em-dash:
```
"Governor and Commander-in-Chief—Sir Gerald Creasy, K.C.M.G., O.B.E."
"Colonial Secretary—R. E. Turnbull, C.M.G. £1,650."
"Director of Agriculture—P. C. Chambers. £1,320."
```

### Asterisk/Dagger Footnotes

Many entries have footnote markers (* or dagger) that reference notes elsewhere:
```
Malta 1899:
  "Second Class Clerks, George Borg Cardona, D. A. Garroni,... Charles B. Sciortino,* Edgar Arrigo"
  Footnote: "* Captain, R.M.R."
  -> For Sciortino, capture military_rank: "Captain" and note R.M.R. in qualifications

Cyprus 1950:
  "* Denotes free quarters, the value of which is taken at 6 per cent. of salary for pension purposes."
  -> Capture in allowances field: "free quarters"
```

---

## Location/Region Extraction Rules

### Location in Position Title

```
"Commissioner, Nicosia, Maj. J. Inglis (acting), 600l."
  -> position: "Commissioner", location: "Nicosia"

"Magistrate, East Falkland, M. Craigie-Halkett."
  -> position: "Magistrate", location: "East Falkland"

"Magistrate, South Georgia, E. B. Binnie, 375l."
  -> position: "Magistrate", location: "South Georgia"

"Sanitary Inspector, Gozo, F. S. Ross, M.D., 120l."
  -> position: "Sanitary Inspector", location: "Gozo", region: "Gozo"
```

### Location in Section Header

```
"Gozo.
  Assistant-Secretary, C. Gatt, 350l."
  -> position: "Assistant-Secretary", location: "Gozo", region: "Gozo"

"Stanley Government School—
  Schoolmaster, A. R. Hoare, 350l. and quarters."
  -> position: "Schoolmaster", location: "Stanley"

"South Georgia—
  Deputy Collectors, E. B. Binnie and Wm. Barlas"
  -> location: "South Georgia"
```

### Region from Administrative Context

```
Malta: region: "Malta" or "Gozo"
Cyprus: region from district name (Nicosia, Famagusta, Larnaca, Limassol, Paphos, Kyrenia)
Falkland Islands: region: "East Falkland", "West Falkland", "South Georgia", "Stanley"
```

### Common Locations

**Malta**: Valletta, Floriana, Senglea (Senglea), Cospicua, Vittoriosa, Sliema, St. Julian's, Birkirkara, Qormi, Zabbar, Zejtun, Zebbug, Mosta, Naxxar, Notabile/Rabat, Citta Vecchia, Hamrun, Marsa, Pawla, Tarxien, Siggiewi, Mellieha, Dingli, Gozo (Victoria/Rabat), Nadur, Xaghra, Xewkija

**Gibraltar**: No internal divisions; entire colony is one settlement

**Cyprus**: Nicosia, Famagusta, Larnaca, Limassol, Paphos/Ktima, Kyrenia, Morphou, Troodos, Lefka

**St. Helena**: Jamestown (capital/only town)

**Falkland Islands**: Stanley, Darwin (East Falkland), Fox Bay (West Falkland), South Georgia (Grytviken)

**Bermuda**: Hamilton, St. George's, Ireland Island (Dockyard)

---

## Era-Specific Notes

### 1867-1890 (Early Era)

- **Malta**: Very detailed establishment. Governor is always a military officer (General). "Chief Secretary to Government" is the senior civil servant. Salaries in "Xl." format. Many Maltese names among officials. The University is listed with all professors by chair. Extensive judicial establishment with Maltese-language legal titles.
- **Gibraltar**: Very short entry. Governor is always a military officer. No legislature. Salaries in "Xl." or "Xl. to Yl." format. Currency initially in pesetas/Spanish money alongside pounds.
- **St. Helena**: Small establishment, 15-25 officials. Governor doubles as Chief Justice in some years. "Colonial Secretary and Auditor" is a single combined role.
- **Falkland Islands**: Very small establishment, 10-20 officials. Often combined in source files with other colonies (OCR artifacts). Governor is "Governor and Commander-in-Chief". Military Establishment listed separately.
- **Heligoland**: Tiny establishment, 10-15 officials. German names predominate. Governor also serves as judge. Disappears after 1890.
- **Bermuda**: Relatively large establishment due to self-governing status. House of Assembly members listed.
- **Expected officials**: Malta 80-200, Gibraltar 15-40, Cyprus (from 1883) 20-50, St. Helena 15-30, Falklands 10-25, Heligoland 10-15, Bermuda 30-80

### 1890-1920 (Expansion Era)

- **Malta**: Departments proliferate. Public Health Department created with extensive district medical service listing individual villages. Water Works and Electric Lighting. Railway Department. Military and naval officers listed at end.
- **Gibraltar**: Grows slowly. Sanitary Commissioners created (1893). Board of Health. Port Department expands.
- **Cyprus**: Significant expansion as British administration matures. District Commissioners prominent. "High Commissioner" title used (not Governor). Six administrative districts. Both Ottoman and British legal systems in use.
- **Falkland Islands**: Dependencies (South Georgia) gain their own officials. Whaling industry officials appear. South Georgia magistrates and customs officers.
- **Expected officials**: Malta 150-250, Gibraltar 20-50, Cyprus 40-100, St. Helena 15-30, Falklands 15-40

### 1920-1940 (Inter-war)

- **Malta**: Self-government period (1921-1933). Elected ministers appear. Constitution suspended 1933, reinstated partially later. Currency notation shifts from "l." to "£".
- **Gibraltar**: Still no legislature until 1950. Gradual expansion of services. Currency change from pesetas to sterling completed.
- **Cyprus**: Becomes formally a Colony in 1925. Governor replaces High Commissioner. Legislative Council (until 1931 disturbances). After 1931, Governor legislates alone.
- **Falkland Islands**: Battle of the Falklands (1914) noted in historical section. Dependencies grow in importance due to whaling.
- **Expected officials**: Malta 100-200, Gibraltar 25-50, Cyprus 50-120, St. Helena 15-25, Falklands 20-50

### 1946-1966 (Late Colonial)

- **Malta**: Complex dual administration. Self-government restored 1947. Maltese Government and Maltese Imperial Government listed separately. Many Maltese names in senior positions. No salary scales visible -- officials listed by title only in many cases.
- **Gibraltar**: Legislative Council from 1950. City Council from 1956. Executive Council listed. Salaries not always shown (1953 file omits them).
- **Cyprus**: Governor rules alone (no legislature). Extensive departmental structure. Salary ranges in "£X-Y" format. Expatriation allowance at 15% of salary. Many departments mirror UK civil service structure. Independence 1960.
- **St. Helena**: Small establishment persists. Ascension and Tristan da Cunha dependencies listed at end of file. Tristan da Cunha has Administrator and Medical Officer only.
- **Falkland Islands**: Listed as "Falkland Islands and Dependencies". British Antarctic Territory separated 1962.
- **Expected officials**: Malta 30-80 (many positions under Maltese Government, listed without salary), Gibraltar 20-40, Cyprus 80-200, St. Helena 10-20, Falklands 20-50

---

## Title Patterns (appear BEFORE name)

```
Military: General, Gen., Lieut.-General, Lieut.-Gen., Major-General, Maj.-Gen., Colonel, Col.,
         Lt.-Col., Lieut.-Col., Major, Captain, Capt., Commander, Rear-Admiral, Vice-Admiral,
         Admiral, Field Marshal, Brigadier, Wing Commander, Air Vice-Marshal
Honorific: Sir, The Right Hon., The Hon., Right Rev., Very Rev., Rev., Ven., Dr.,
          Monsignor (Mgr.), Notary
Naval: Commander (Com.), Captain R.N.
```

### Honors (appear AFTER name) - Post-nominal letters

```
K.C.M.G., G.C.M.G., C.M.G., K.C.B., G.C.B., C.B., K.B.E., O.B.E., M.B.E.,
C.B.E., G.B.E., K.C.S.I., C.I.E., D.S.O., M.C., V.D., E.D., T.D., Kt., Knt.,
K.C.V.O., C.V.O., M.V.O., I.S.O., K.P.M.
```

### Qualifications (appear AFTER name) - Academic/professional

```
Medical: M.D., M.B., M.R.C.S., F.R.C.S., L.R.C.S., L.R.C.P., F.R.C.P., Ch.B., D.P.H.,
         D.T.M., M.R.C.P., V.S. (Veterinary Surgeon)
Academic: B.A., M.A., B.Sc., M.Sc., LL.D., D.D., Ph.D., B.L., LL.B., LL.M., I.L.D.
         (for Malta: Iuris Legum Doctor)
Engineering: R.E., C.E., M.I.C.E., A.I.C.E., A.M.I.C.E., M.I.E.E., M.I.Mech.E., L.S.A.,
            L.S. (Licensed Surveyor)
Malta-specific: R.M.M. (Royal Malta Militia), R.M.R. (Royal Malta Regiment), R.M.A. (Royal Malta Artillery)
Other: F.R.S., F.R.G.S., F.Z.S., Q.C., K.C., J.P., Notary (Maltese legal designation)
```

---

## Known Name Abbreviations

Expand these standard abbreviations:
```
Wm. = William
Chas. = Charles
Thos. = Thomas
Jas. = James
Jno. = John
Robt. = Robert
Geo. = George
Edwd. = Edward
Fredk. = Frederick
Richd. = Richard
```

**DO NOT** expand single initials: C., G., J., etc. remain as-is.

**Malta-specific**: Many Maltese names with "di", "de", "della" particles (e.g., "Sir Gerald Strickland, Count della Catena"). Italian-style double surnames are common (e.g., "Borg Cardona", "Frendo Azopardi", "Mompalao De Piro"). Treat these as compound surnames.

---

## Validation Checklist

### All Years
- [ ] Officials list is non-empty
- [ ] All entries have name and position fields
- [ ] Salaries parsed (where present in source)
- [ ] Honors and qualifications in correct fields
- [ ] "Ditto" entries expanded to proper position names
- [ ] Maltese compound surnames preserved (Borg Cardona, not just Cardona)

### Malta (1867-1965)
- [ ] Governor captured (always a military officer in early era)
- [ ] Chief Secretary to Government captured
- [ ] Crown Advocate captured
- [ ] University professors captured (with their chairs noted in position)
- [ ] District medical officers captured with village locations
- [ ] Judges of all courts captured with LL.D. qualifications
- [ ] In late era (1947+): distinguish Maltese Imperial Government from Maltese Government officials
- [ ] Expected: 80-250 officials depending on era

### Gibraltar (1867-1966)
- [ ] Governor captured (also General commanding garrison)
- [ ] Colonial Secretary captured
- [ ] Chief Justice captured
- [ ] Note: very short list compared to other colonies
- [ ] In late era: Executive Council and Legislative Council members captured
- [ ] Expected: 15-50 officials

### Cyprus (1883-1961)
- [ ] Before 1925: "High Commissioner" not "Governor"
- [ ] After 1925: "Governor"
- [ ] District Commissioners captured for all six districts
- [ ] Queen's/Crown Advocate (later Attorney-General) captured
- [ ] Supreme Court judges captured
- [ ] In late era: expatriation allowance noted (15% of salary)
- [ ] Expected: 20-200 officials depending on era

### St. Helena (1867-1966)
- [ ] Governor captured (also ex-officio Chief Justice in some years)
- [ ] Colonial Secretary (sometimes "Government Secretary") captured
- [ ] Multiple-role holders correctly parsed
- [ ] Ascension officials captured (if present in file)
- [ ] Tristan da Cunha officials captured (if present in file)
- [ ] Expected: 10-25 officials

### Falkland Islands (1867-1966)
- [ ] Governor captured
- [ ] Colonial Secretary captured
- [ ] Chief Justice (often Governor ex officio) captured
- [ ] South Georgia officials captured
- [ ] Expected: 10-50 officials depending on era

### Heligoland (1867-1890)
- [ ] Governor captured
- [ ] Government Secretary captured
- [ ] Verify colony disappears after 1890 (ceded to Germany)
- [ ] Expected: 10-15 officials

### Bermuda (1879-1966)
- [ ] Governor captured
- [ ] Colonial Secretary captured
- [ ] House of Assembly Speaker captured
- [ ] Expected: 30-100 officials

### British Antarctic Territory (1963-1966)
- [ ] High Commissioner captured (same person as Governor of Falkland Islands)
- [ ] Expected: 1-2 officials

---

## Key Positions by Era

### Malta
1. Governor (military officer: General, Lieutenant-General, Major-General)
2. Chief Secretary to Government
3. Crown Advocate (later Attorney-General)
4. Collector of Customs and Superintendent of Ports
5. Comptroller of Charitable Institutions
6. Chief Justice and President of the Court of Appeal
7. Chief Government Medical Officer
8. Superintendent of Public Works
9. Auditor-General
10. Receiver-General / Treasurer

### Gibraltar
1. Governor (also General commanding garrison)
2. Colonial Secretary
3. Chief Justice
4. Attorney-General
5. Treasurer / Financial Secretary
6. Captain of the Port
7. Colonial Engineer
8. Police Magistrate
9. Chief of Police
10. Postmistress/Postmaster

### Cyprus
1. High Commissioner (pre-1925) / Governor (post-1925)
2. Chief Secretary / Colonial Secretary
3. Chief Justice
4. Queen's Advocate / Attorney-General
5. Financial Secretary
6. District Commissioners (6)
7. Director of Public Works
8. Director of Medical and Health Services
9. Director of Education
10. Commissioner of Police

### St. Helena
1. Governor and Commander-in-Chief
2. Colonial Secretary (also Auditor in some years)
3. Treasurer / Colonial Treasurer
4. Chief Justice (often Governor ex officio)
5. Colonial Surgeon / Senior Medical Officer
6. Superintendent of Police

### Falkland Islands
1. Governor and Commander-in-Chief
2. Colonial Secretary
3. Treasurer / Collector of Customs
4. Colonial Surgeon
5. Colonial Engineer
6. Chief Constable

---

## Sample Output

### Malta 1880 Style (Detailed, early era)

```python
{
    "name": "Gen. Sir Arthur Borton",
    "canonical_name": "Borton, Arthur",
    "given_names": "Arthur",
    "surname": "Borton",
    "position": "Governor",
    "department": "Civil Establishment - Malta",
    "salary_min": 4500,
    "salary_max": 4500,
    "allowances": "500l. table allowance as Commander of the Troops",
    "honors": ["K.C.B."],
    "military_rank": "General",
    "location": None,
    "region": None,
}
```

### Gibraltar 1899 Style (Detailed, no legislature)

```python
{
    "name": "H. M. Jackson",
    "canonical_name": "Jackson, H. M.",
    "given_names": "H. M.",
    "surname": "Jackson",
    "position": "Colonial Secretary",
    "department": "Civil Establishment - Gibraltar",
    "salary_min": 833,
    "salary_max": 833,
    "allowances": "free house",
    "honors": ["C.M.G."],
    "location": None,
    "region": None,
}
```

### Cyprus 1950 Style (Late colonial, salary ranges)

```python
{
    "name": "Sir Andrew Barkworth Wright",
    "canonical_name": "Wright, Andrew Barkworth",
    "given_names": "Andrew Barkworth",
    "surname": "Wright",
    "position": "Governor and Commander-in-Chief",
    "department": "Governor - Cyprus",
    "salary_min": 3300,
    "salary_max": 3300,
    "duty_allowance": 1200,
    "honors": ["K.C.M.G.", "C.B.E.", "M.C."],
    "location": None,
    "region": None,
}
```

### St. Helena 1953 Style (Small colony, multiple roles)

```python
{
    "name": "C. W. T. Johnson",
    "canonical_name": "Johnson, C. W. T.",
    "given_names": "C. W. T.",
    "surname": "Johnson",
    "position": "Government Secretary and Magistrate",
    "department": "Civil Establishment - St Helena",
    "salary_min": None,
    "salary_max": None,
    "honors": ["C.B.E."],
    "location": None,
    "region": None,
}
```

### Heligoland 1890 Style (Tiny colony, low salaries)

```python
{
    "name": "A. C. S. Barkly",
    "canonical_name": "Barkly, A. C. S.",
    "given_names": "A. C. S.",
    "surname": "Barkly",
    "position": "Governor and Commander-in-Chief",
    "department": "Civil Establishment - Heligoland",
    "salary_min": 800,
    "salary_max": 800,
    "allowances": "fees",
    "honors": ["C.M.G."],
    "location": None,
    "region": None,
}
```

### Falkland Islands 1921 Style (Small colony, dependencies)

```python
{
    "name": "E. B. Binnie",
    "canonical_name": "Binnie, E. B.",
    "given_names": "E. B.",
    "surname": "Binnie",
    "position": "Magistrate",
    "department": "Judicial Department - Falkland Islands",
    "salary_min": 375,
    "salary_max": 375,
    "duty_allowance": 100,
    "location": "South Georgia",
    "region": "South Georgia",
}
```

### Tristan da Cunha 1953 Style (Dependency, minimal)

```python
{
    "name": "J. P. L. Scott",
    "canonical_name": "Scott, J. P. L.",
    "given_names": "J. P. L.",
    "surname": "Scott",
    "position": "Administrator",
    "department": "Civil Establishment - Tristan da Cunha",
    "salary_min": None,
    "salary_max": None,
    "location": None,
    "region": None,
}
```

---

## Colony-Specific Extraction Challenges

### Malta
1. **Maltese compound surnames**: "Borg Cardona", "Frendo Azopardi", "Mompalao De Piro", "Tabone Engerer" -- treat the full compound as the surname.
2. **University professors**: Position should include the subject chair (e.g., "Professor of Medicine", not just "Professor").
3. **District Medical Officers**: Each village/locality listed gets its own entry with a location.
4. **Footnote references**: Asterisks (*), daggers, and double-daggers reference footnotes about R.M.M./R.M.R. rank or other notes.
5. **"Ditto" for district medical salaries**: "(1st class)" and "(2nd class)" refer to salary class, not position class.
6. **Dual government (1947+)**: Distinguish "Maltese Imperial Government" officials from "Maltese Government" officials by department name.

### Gibraltar
1. **Military overlap**: Governor's ADCs and military secretary are military positions paid partly from Imperial funds.
2. **Currency**: Before 1898, some figures in pesetas. After 1898, all in sterling.
3. **Miss Creswell**: A notable long-serving Postmistress/Superintendent of Telegraph (appears 1879-1899+). Gender should be correctly inferred.
4. **Short entries**: The entire Gibraltar civil establishment may have only 15-25 named officials.

### Cyprus
1. **Title change**: "High Commissioner" before 1925, "Governor" after.
2. **District Commissioners**: Must capture district names in location field.
3. **Late-era salary format**: "£480-960" means salary_min: 480, salary_max: 960.
4. **Expatriation allowance**: Noted as a percentage (15%) rather than fixed amount. Record in allowances field.
5. **Ottoman legal system**: Muslim religious tribunals and Cadi positions may appear.
6. **Free quarters notation**: Asterisk (*) often denotes "free quarters" per a note at the top of the civil establishment section.

### Falkland Islands
1. **Multiple roles per person**: "Postmaster, Registrar-General, Local Auditor, M. Craigie-Halkett" -- one person, multiple positions. Create single entry with primary position.
2. **South Georgia**: Create separate entries with location: "South Georgia".
3. **Dependencies**: In late-era files ("Falkland Islands and Dependencies"), dependencies include South Georgia, South Shetlands, South Orkneys, Graham's Land.
4. **Travelling Teachers**: Multiple teachers listed on one line with salary range.
5. **OCR artifacts**: Early files (1867) may contain text from unrelated colonies due to OCR combining.

### Heligoland
1. **German names**: "Gätke", "Michels", "Botter", "Payens" -- preserve umlauts where present.
2. **Low salaries**: Some as low as 6l., reflecting the tiny colony's budget.
3. **Disappears after 1890**: No files should exist after cession to Germany.

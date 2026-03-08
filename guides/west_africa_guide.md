# West Africa Colonial Office List -- Extraction Guide

## 1. Overview

This guide provides instructions for extracting personnel data from British West Africa Colonial Office List source files (1867-1966). It covers all West African colonies and territories **except** the Gold Coast, which has its own dedicated guide.

**Colonies and territories covered:**
- Sierra Leone (1867-1961)
- The Gambia (1867-1965)
- Lagos (1867-1906, then absorbed into Southern Nigeria)
- Southern Nigeria (1900-1914)
- Northern Nigeria (1900-1914)
- Nigeria (unified 1914-1960)
- Niger Coast Protectorate (1893-1900, precursor to Southern Nigeria)
- West African Settlements (1867-1874, umbrella administration)
- Togoland (British Mandate/Trusteeship, listed under Gold Coast)
- Cameroons (British Mandate/Trusteeship, listed under Nigeria)

**Schema**: All extractions must conform to the 20-field schema defined in `guides/schema.py`.

**Required fields**: `name`, `canonical_name`, `surname`, `position`, `department`

---

## 2. Historical Context

### Administrative Evolution

| Era | Territory | Characteristics |
|-----|-----------|-----------------|
| 1867-1874 | West African Settlements | Sierra Leone, Gambia, Gold Coast, Lagos under one Governor based in Freetown |
| 1874 | Separation | Gold Coast separated; Sierra Leone and Gambia become distinct colonies |
| 1867-1886 | Lagos | Administered under "Administrator" (not Governor); separated from Gold Coast 1886 |
| 1893-1900 | Niger Coast Protectorate | Precursor to Southern Nigeria |
| 1900-1906 | Lagos Colony + S. Nigeria Protectorate | Lagos Colony and Protectorate of Southern Nigeria coexist |
| 1906-1914 | Southern Nigeria | Lagos merged into Colony and Protectorate of Southern Nigeria |
| 1900-1914 | Northern Nigeria | Protectorate of Northern Nigeria under separate High Commissioner/Governor |
| 1914-1960 | Nigeria (unified) | Amalgamation of Northern and Southern Nigeria under one Governor |
| 1922 | Cameroons Mandate | Former German territory placed under British Mandate, administered as part of Nigeria |
| 1946 | Cameroons Trusteeship | Mandate becomes UN Trusteeship |
| 1960 | Nigeria independence | |
| 1961 | Sierra Leone independence | |
| 1961 | Cameroons plebiscite | Northern Cameroons joins Nigeria; Southern Cameroons joins Cameroun Republic |
| 1965 | Gambia independence | |

### Key Name Changes to Watch

- "Administrator" becomes "Governor" as colonies gain status (Gambia changed c.1901)
- "High Commissioner" used for Northern Nigeria (1900-1914)
- "Lieutenant-Governor" used for Southern Provinces / Northern Provinces after 1914 amalgamation
- "Chief Commissioner" replaces "Lieutenant-Governor" for regional heads in later years
- "West African Settlements" disappears after 1874

---

## 3. Regional Divisions

### Sierra Leone
- **Colony** (Freetown and peninsula)
- **Protectorate** (interior): Northern Province, Southern Province (from 1936); later South-Eastern Province added (1950)
- Districts under District Commissioners

### The Gambia
- **Colony** (Bathurst/Banjul and surroundings)
- **Protectorate**: Four divisions (North Bank, South Bank/MacCarthy Island, Upper River, Western)
- Travelling Commissioners in early era; Commissioners later

### Lagos (1867-1906)
- Colony of Lagos
- Badagry (sub-station with its own Civil Commandant)
- Absorbed into Southern Nigeria 1906

### Nigeria (post-1914)
- **Colony of Lagos** (the small coastal colony)
- **Southern Provinces** (under Lieutenant-Governor, later Chief Commissioner): Abeokuta, Benin, Calabar, Ijebu, Oyo, Ogoja, Ondo, Onitsha, Owerri, Warri, Cameroons (from 1922)
- **Northern Provinces** (under Chief Commissioner): Adamawa, Bauchi, Benue, Bornu, Ilorin, Kabba, Kano, Niger, Plateau, Sokoto, Zaria

### Northern Nigeria (1900-1914)
- Political department with Residents by province: Bauchi, Bornu, Kano, Kontagora, Muri, Nassarawa, Sokoto, Yola, Zaria, Ilorin, Kabba, Niger, Nupe

### Southern Nigeria (1906-1914)
- Three provinces: Western (Lagos), Central (Niger/Warri), Eastern (Calabar)
- Provincial Commissioners with District Commissioners

### Cameroons (under Nigeria)
- Administered as integral part of Nigeria; rarely has separate civil establishment
- After 1960: Commissioner for Southern Cameroons, Administrator for Northern Cameroons

---

## 4. Data Schema Reference

```python
{
    # REQUIRED fields
    "name": "F. Cardew",                              # As appears in source
    "canonical_name": "Cardew, F.",                    # "Surname, Given Names"
    "surname": "Cardew",                               # Family name only
    "position": "Governor",                             # Title/role
    "department": "Governor's Office - Sierra Leone",   # "Department - Colony"

    # OPTIONAL fields
    "given_names": "F.",
    "salary_min": 2000,          # int, pounds sterling
    "salary_max": 2000,          # int, pounds sterling
    "salary_currency": "GBP",    # Always GBP for West Africa
    "salary_scale": "B",         # Scale designation (1920s-1950s)
    "allowances": "500l. allowances",
    "duty_allowance": 500,       # Numeric duty allowance
    "expatriation_pay": 300,     # Numeric (1940s-1950s only)
    "per_diem": "5s. per diem",  # Daily rate string
    "acting_status": "Acting",   # Acting/Temporary/Officiating/Relief
    "honors": ["C.M.G."],        # List of post-nominals (honors)
    "qualifications": ["M.D."],  # List of post-nominals (qualifications)
    "military_rank": "Colonel",  # Military rank if present
    "location": "Freetown",      # Specific station
    "region": "Northern Province" # Administrative region
}
```

### Department Naming Convention

Always use the format: **"Department Name - Colony Name"**

Examples:
- `"Colonial Secretary's Office - Sierra Leone"`
- `"Judicial - Nigeria"`
- `"Administrative Service - Nigeria"`
- `"Customs - The Gambia"`
- `"Medical - Northern Nigeria"` (pre-1914)
- `"Civil Establishment - Lagos"` (pre-1906)
- `"Political Department - Northern Nigeria"`
- `"Provincial Administration - Sierra Leone"`

For the West African Settlements era (1867-1874), use:
- `"Civil Establishment - West African Settlements"`

For military units, use the unit name:
- `"Sierra Leone Battalion, WAFF - Sierra Leone"`
- `"Nigeria Regiment, WAFF - Nigeria"`

---

## 5. Department List by Era

### Early Era (1867-1890s)

Departments are small. Typical listing for a colony:

**Sierra Leone / West African Settlements (1867)**:
Civil Establishment, Customs, Judicial, Medical (Colonial Surgeon), Ecclesiastical

**The Gambia (1867)**:
Civil Establishment, Judicial Establishment

**Lagos (1867)**:
Civil Establishment, Judicial and Magisterial, Military, Commissariat, Vice-Admiralty Court

### Middle Era (1896-1914)

Departments expand significantly:

**Sierra Leone (1896)**: Governor's Office, Colonial Secretary's Office, Treasury, Customs (In-door Staff, Out-door Staff, Sherbro District, Officers-in-Charge), Audit, Native Affairs, Printing, Police, Prisons, Medical, Education, Public Works, Botanical/Agricultural, Railway, Ecclesiastical, Districts (Eastern, Western, Sherbro)

**Northern Nigeria (1910)**: Governor's Office, Secretary's Office, Political Department (Residents by province), Legal/Judicial, Treasury, Postal and Telegraphs, Medical, Audit, Police, Prisons, Marine, Customs, Botanical/Forestry, Public Works, Transport

**Southern Nigeria (1910)**: Governor's Office, Colonial Secretary's Office, Provincial Administration (Western/Central/Eastern Provinces), Legal, Judicial, Treasury, Customs, Marine, Medical, Education, Public Works, Railway, Police, Prisons, Audit, Postal/Telegraphs, Forestry, Agriculture, Harbour Works, Dredging Staff

### Late Era (1920s-1950s)

**Nigeria (1936)**: Nigerian Secretariat, Secretariat Southern Provinces, Secretariat Northern Provinces, Judicial, Legal, Administrative Service (classified by grade), Audit, Printing, Treasury, Customs, Marine, Medical, Education, Police, Prisons, Public Works, Railway, Posts and Telegraphs, Agriculture, Forestry, Surveys, Veterinary, Geological/Mines, Nigeria Regiment (WAFF)

**Sierra Leone (1950)**: Governor and Personal Staff, Administration (Colonial Secretary's Office, Provincial Administration), Accountant-General, Agricultural, Audit, Commerce and Industry, Customs, Education, Forestry, Geological, Income Tax, Judicial, Legal, Medical and Health, Police and Prisons, Post Office, Printing, Public Works, Railway, Survey, Sierra Leone Battalion (RWAFF)

**The Gambia (1950)**: Governor and Personal Staff, Administrative Service, Accountant General, Agricultural, Audit, Crown Law and Lands, Customs, Education, Judicial, Labour, Medical and Health, Meteorological, Police and Prisons, Post Office, Public Works, Veterinary

---

## 6. Salary Formats by Era

### Early Era (1867-1890s): Pounds with "l." suffix

```
Governor, Col. S. W. Blackall, 3,000l. and allowances, 500l.
Administrator, Admiral Patey, 1,300l. and 200l. table money.
1st Writer, H. G. M. Robertson, 300l.
Landing Waiters, Samuel Wellington, 50l., B. J. Pratt, 36l.
Colonial Chaplain, Rev. S. Spain, B.A., 204l. 12s.
```

Extraction rules:
- `3,000l.` -> salary_min=3000, salary_max=3000
- `100l. to 120l.` -> salary_min=100, salary_max=120
- `204l. 12s.` -> salary_min=204 (drop shillings or convert: 12s = 0.6, so 204.6)
- `500l. allowances` or `200l. table money` -> capture in `allowances` field
- Always set `salary_currency` = "GBP"

### Middle Era (1896-1914): Same pounds format with duty allowance

```
Governor...2,500l., and 500l. duty allowance
Chief Justice, 2,000l., duty, 400l.
Senior Resident, 700l. to 800l. by 25l.
```

Extraction rules:
- `duty allowance` / `duty` amounts -> `duty_allowance` field (numeric)
- `700l. to 800l. by 25l.` -> salary_min=700, salary_max=800 (the "by 25l." is the annual increment; ignore for min/max)
- Footnotes like `*Rising by L20` describe increment rates; do not extract as salary

### Interwar Era (1920s-1930s): Named salary scales introduced

```
Scale A is as follows:--For those appointed before 1st October, 1923; 450l. for three years,
then 510l. by 30l. to 720l., by 40l. to 920l., with seniority allowance of 72l. from 720l.
```

Example entries with scales:
```
Assistant Secretaries, R. D. Ross, Capt. C. N. A. Clarke, Scale B.
Assistant Auditors, E. H. C. Lillicrap, L. H. Pope, Scale A.
Office Assistant, Miss I. A. Reading, Scale C, with maximum 720l.
```

Extraction rules:
- When a salary scale is given (e.g., "Scale A", "Scale B"), set `salary_scale` field
- Do NOT attempt to compute salary_min/salary_max from scale definitions unless an explicit salary figure appears
- If both a scale and a specific salary appear (e.g., "Scale A, commencing at 600l."), use the explicit figure
- Named salary figures still appear for senior posts: `2,400l., duty, 600l.`

### Late Era (1940s-1950s): Salary groups, expatriation pay, new pound notation

**1950 format (Nigeria)**:
```
Governor—Sir John Stuart Macpherson, K.C.M.G. £6,500. Duty pay £1,750.
Chief Secretary—H. M. Foot, C.M.G., O.B.E. Group A1.
Administrative Officers—... Scale A.
```

**1950 format (Sierra Leone / Gambia)**:
```
Scale A: £450 for 3 years, 510-30-660, 720-30-960, 1,000.
Scale B: £450 for 3 years, 510-20-610, 660-30-900.
Scale M2: £690 for 3 years, 720-30-1,000, 1,080-30-1,200.

Governor—Sir George Beresford-Stooke, K.C.M.G. £3,000 and £1,000 duty allowance.
Colonial Secretary—R. O. Ramage, C.M.G. £1,650.
Director of Agriculture—R. R. Glanville, C.B.E. £1,350.
Assistant Colonial Secretaries—F. W. Essex; P. W. Youens; ... Scale A.
```

Extraction rules:
- `£6,500` -> salary_min=6500, salary_max=6500
- `Group A1` or `Scale A` -> salary_scale="A1" or salary_scale="A"
- `Scale M2` -> salary_scale="M2"
- Expatriation pay tables are provided; extract as `expatriation_pay` when given for individuals
- `£1,000 duty allowance` / `Duty pay £1,750` -> duty_allowance=1000 or 1750
- Salary notation switches from `l.` to `£` symbol around 1940s-1950s

---

## 7. Extraction Patterns

### Pattern 1: Standard Single Person Entry

```
Colonial Secretary, H. R. R. Blood, C.M.G., 1,400l., and 280l. duty allowance.
```

Extract:
- name: "H. R. R. Blood"
- canonical_name: "Blood, H. R. R."
- surname: "Blood"
- position: "Colonial Secretary"
- honors: ["C.M.G."]
- salary_min: 1400, salary_max: 1400
- duty_allowance: 280

### Pattern 2: Multiple People on One Line

```
Landing Waiters, Samuel Wellington, 50l., B. J. Pratt, 36l., A. J. Euba, 36l., C. E. Marke, 36l.--158l.
```

Extract as FOUR separate records, each with position "Landing Waiter":
- Samuel Wellington (salary_min=50, salary_max=50)
- B. J. Pratt (salary_min=36, salary_max=36)
- A. J. Euba (salary_min=36, salary_max=36)
- C. E. Marke (salary_min=36, salary_max=36)

The trailing `--158l.` is the total; do NOT extract it as a person.

Another common pattern with "each":
```
Compositors, T. B. Macauley and E. C. Johnston, 36l. to 45l. each.
```
Both get salary_min=36, salary_max=45.

### Pattern 3: Large Lists with Scale Reference

```
Assistant Secretaries, R. D. Ross, Capt. C. N. A. Clarke, C. R. Niven, M.C.,
I. W. E. Dods, D. E. R. M. Lambert, H. L. M. Butcher, T. Farley Smith,
K. A. Sinker, H. R. E. Browne.
```

Each name is a separate record with position "Assistant Secretary" and salary_scale from context.

### Pattern 4: Ditto Marks ("ditto")

```
1st Writer, H. G. M. Robertson, 300l.
2nd ditto, Thos. Johnson, 104l.
```

"ditto" replaces the noun from the previous entry. Here "2nd ditto" = "2nd Writer".
Extract: position="2nd Writer", name="Thos. Johnson", salary_min=104

More examples:
```
Chief Clerk, J. E. Dawson, 200l.
2nd ditto, E. W. Cole, 100l. to 120l.
3rd ditto, S. T. Wray, 100l. to 120l.
...
7th ditto, J. J. Thomas, 60l. to 80l.
```
All are "Clerks": 2nd Clerk, 3rd Clerk, etc.

### Pattern 5: Vacancy

```
Harbour Master (vacant), 150l.
Solicitor-General (vacant), 1,200l., duty, 240l.
```

Extract a record with the position but leave name/canonical_name/surname as the literal string "VACANT". Still capture salary.

### Pattern 6: Acting Status

```
Dr. Sherwood (acting), 300l.
Private Secretary and Aide-de-Camp, 450l. (vacant).
```

For "(acting)", set acting_status="Acting".

### Pattern 7: Position with Location

```
Civil Commandant and Collector of Customs at Badagry, J. Pilkington, 300l.
Dispenser, Waterloo, W. Z. Young, 50l.
Collector of Customs, Freelton, F. A. von Weiller, Scale A.
```

Extract location from the position text:
- location: "Badagry", "Waterloo", "Freelton"
- position: "Civil Commandant and Collector of Customs" (without location)

### Pattern 8: Military Ranks in Names

```
Governor, Colonel F. Cardew, C.M.G., 2,000l.
Administrator, Commander J. H. Glover, 1,300l.
Commandant, Capt. W. M. Fowler, 960l.
```

Extract military_rank separately:
- military_rank: "Colonel", "Commander", "Captain"
- name: "F. Cardew" (without rank), canonical_name: "Cardew, F."

### Pattern 9: Em-dash Separator (1950s)

```
Governor—Sir George Beresford-Stooke, K.C.M.G. £3,000 and £1,000 duty allowance.
Colonial Secretary—R. O. Ramage, C.M.G. £1,650.
```

The em-dash separates position from name. Same extraction rules apply.

### Pattern 10: Salary Scale with Maximum

```
Scale A, with maximum of 600l.
Scale C, with maximum 720l.
Scale A, commencing at 600l.
```

Set salary_scale="A" and note the maximum or commencing salary. If "commencing at 600l." appears, set salary_min=600.

---

## 8. Special Patterns

### Honors vs. Qualifications

Post-nominal letters must be classified correctly:

**Honors** (awards/decorations): K.C.M.G., G.C.M.G., C.M.G., K.B.E., O.B.E., M.B.E., C.B.E., D.S.O., M.C., K.C.B., I.S.O., K.P.M., V.D., E.D., T.D.

**Qualifications** (academic/professional): M.D., M.B., B.A., M.A., B.Sc., LL.B., LL.D., Ph.D., F.R.C.S., M.R.C.S., L.R.C.P., D.P.H., D.T.M.&H., M.I.C.E., A.M.I.C.E., A.M.I.E.E., F.R.G.S., A.R.I.B.A.

Example:
```
Director of Public Works, Capt. C. Wilson Brown, O.B.E., M.C., A.R.T.C. (Glasgow), F.R.G.S., M.Inst.C.E.
```
- honors: ["O.B.E.", "M.C."]
- qualifications: ["A.R.T.C.", "F.R.G.S.", "M.Inst.C.E."]
- military_rank: "Captain"

### West African Frontier Force (WAFF) Entries

Military personnel have regiment affiliations and military-style salary structures:

```
Lieut.-Colonel, G. P. Harding, M.C., 1,000l., and 182l. duty allowance per annum.
Adjutant, Capt. R. H. D. Grimley, 700l. to 750l., duty pay, 5s. per diem.
Captains, 700l. to 750l.
Lieutenants, 510l. to 600l.
```

Rules:
- Extract military_rank from position context (Lieut.-Colonel, Captain, etc.)
- Per diem amounts go in `per_diem` field: "5s. per diem"
- Generic rank entries without names (e.g., "Captains, 700l. to 750l.") represent salary scales only; skip these unless a specific name is given

### "Kt." and "Sir" Disambiguation

- "Sir" before a name indicates knighthood; do NOT add to honors list (it is implied by K.C.M.G., K.B.E., etc.)
- "Kt." or "Knt." as a post-nominal means "Knight Bachelor" and SHOULD be added to honors

### Footnotes and Cross-References

Common footnote markers: *, +, ++, (a), (b), numbers
```
* Now Rt. Hon. Lord Lugard, P.C.
+ Elected members.
For Scales A to C, see footnote on page 421.
```

Do NOT extract footnote text as personnel records. Footnotes provide context only.

### Compound Positions

Some officials hold multiple positions:
```
Civil Commandant and Collector of Customs at Badagry, J. Pilkington, 300l.
Police Magistrate, Coroner and Registrar-General, B. A. K. McRoberts, 660l.
Commissioner of Police and Inspector of Prisons, N. P. Hadow.
```

Extract the full compound position as a single string.

### "African" Prefix on Positions

In later eras, positions are sometimes qualified with "African":
```
African Assistant Colonial Secretaries, J. L. John, (one vacancy), 360l. to 500l.
African Medical Officers, M. C. F. Easmon, E. H. Taylor-Cummins, ...
Senior African Medical Officer, E. J. Wright, 740l.
```

Include "African" as part of the position name.

### Secondments

```
C. Ll. Rice (seconded from Nigeria)
R. Varvill, D.S.C. (seconded from Administration)
```

Extract the person normally. The "(seconded from...)" text provides context but does not change extraction.

---

## 9. Location Extraction

### From Section Headers

Department sections often indicate location context:
```
Secretariat, Southern Provinces and Colony.
Secretariat, Northern Provinces.
```
- Set region: "Southern Provinces" or "Northern Provinces"

### From Position Titles

```
Collector of Customs, Freelton
Provincial Engineers...Provincial Commissioners
Commissioner (Headquarters, Judicial and Freetown Police Districts)
```

### District/Provincial Assignments

For administrative officers, the province/district they serve is often the "region":
```
Senior District Commissioner, N. C. Hollins, O.B.E.
District Commissioners, E. F. Sayers, S. M. Deepicht, ...
```

Where a specific district/province is named, set `region` accordingly. Where officers are listed under a provincial header, inherit the province.

### Key Locations by Colony

**Sierra Leone**: Freetown (capital), Bo (Protectorate HQ), Bonthe (Sherbro), Waterloo, Lungi
**The Gambia**: Bathurst/Banjul (capital), MacCarthy Island, Georgetown, Kuntaur
**Lagos**: Lagos (capital), Badagry, Epe
**Nigeria**: Lagos, Kaduna (Northern HQ), Enugu (Eastern HQ), Ibadan (Western HQ), Calabar, Port Harcourt, Kano, Zaria, Jos

---

## 10. Era-Specific Notes

### 1867-1874: West African Settlements

- Sierra Leone text may simply say "See West African Settlements"
- Extract from the West African Settlements file instead
- The Governor is "Governor of W. A. Settlements" based in Sierra Leone
- Gambia and Lagos have their own separate listings with "Administrator" as head

Example from 1867:
```
Governor of W. A. Settlements, Col. S. W. Blackall, 3,000l. and allowances, 500l.
```
- department: "Civil Establishment - West African Settlements"

### 1896-1910: Expansion Era

- Sierra Leone has many detailed departments with salary ranges
- Ditto marks are very common in 1896 files
- Multiple people on one line common for junior positions
- "each" keyword indicates shared salary for listed individuals

### 1900-1914: Nigeria Split Era

- Northern Nigeria and Southern Nigeria are separate entries
- Northern Nigeria has a large "Political" department with Residents listed by province
- Southern Nigeria has three provincial structures (Western, Central, Eastern)
- Each has its own civil establishment and military (WAFF) sections

### 1914-1936: Unified Nigeria

- Salary scales (A, B, C) introduced in the 1920s
- Scale definitions appear as footnotes; record the scale letter
- The Administrative Service lists officers by class (Staff Grade, Class I, Class II, Classes III-IV)
- Enormous name lists (100+ names) for Administrative Service; each is a separate record
- Duty allowance notation: `2,400l., duty, 600l.` means salary=2400, duty_allowance=600

### 1940s-1950s: Late Colonial Era

- Salary scales become more complex: A, B, C plus sub-scales (C.1, C.2, C.3), M2, N
- Expatriation pay introduced: separate from basic salary
- Tables of expatriation pay by salary band appear in the preamble
- `£` symbol replaces `l.` suffix for salary notation
- Em-dash (--) replaces comma between position and name
- Nigeria uses "Group" designations (A1, A2, B, C, D1, etc.) for senior posts
- Sierra Leone and Gambia share some establishments (joint recruitment)
- "Scale N" appears for nursing and lower-grade positions

### Cameroons

- Almost never has its own civil establishment listing
- Administered as part of Nigeria throughout
- In 1961 file: just Commissioner and Administrator named
- When Cameroons officers appear, set department suffix as "- Cameroons (UK Trusteeship)"

### Togoland

- In the 1920s, listed under Gold Coast as a sub-section
- Officers are seconded from Gold Coast civil establishment
- Departments: Political/Administrative, Treasury/Customs, Post and Telegraphs, Medical, Police/Prisons, Railway/PWD
- Very small staff, typically 10-15 officers total

Example from 1921:
```
Togoland.
Officer Commanding British Forces and Senior Political Officer, Major F. W. F. Jackson, D.S.O.
Political and Administrative Service--
Lome and Lomeland, H. B. Popham, M.B.E.
Misahole, R. T. Mansfield.
```
- department: "Political and Administrative Service - Togoland"
- location: "Lome" or "Misahole" from context

---

## 11. Validation Checklist

Before finalizing extraction output, verify:

1. **Required fields present**: Every record has `name`, `canonical_name`, `surname`, `position`, `department`
2. **Department suffix**: Every `department` value ends with `" - Colony Name"` (e.g., "- Sierra Leone", "- Nigeria", "- The Gambia", "- Lagos", "- Northern Nigeria", "- Southern Nigeria", "- West African Settlements", "- Togoland", "- Cameroons (UK Trusteeship)")
3. **Salary coherence**: `salary_min` <= `salary_max` always; both are numeric (int or float); currency is "GBP"
4. **No duplicate totals**: Trailing totals like `--158l.` are NOT extracted as records
5. **Ditto expansion**: All "ditto" references are fully resolved to actual position names
6. **Honors vs. qualifications**: Post-nominals are correctly classified (C.M.G. is an honor, M.D. is a qualification)
7. **Acting status captured**: "(acting)", "Acting", "(Temporary)" entries have `acting_status` set
8. **Vacancies**: Positions marked "(vacant)" produce records with name="VACANT", canonical_name="VACANT", surname="VACANT"
9. **Military rank separated**: Ranks like "Colonel", "Captain", "Lieut.-Col." appear in `military_rank`, NOT in `name`
10. **Name formatting**: `canonical_name` follows "Surname, Given Names" format; `given_names` has initials/names only
11. **Scale notation**: When salary scales appear (Scale A, Scale B, Group A1), capture in `salary_scale` field
12. **No narrative text**: Governor lists, historical summaries, statistics tables, footnotes, and council membership lists are NOT extracted as personnel records -- only entries from the Civil Establishment section
13. **Cross-file awareness**: If a colony says "See [other territory]", extract from that other file
14. **Location extracted**: Where locations appear in position titles or section headers, populate `location` and/or `region`
15. **Per diem captured**: Daily rates like "5s. per diem" go in the `per_diem` field as strings

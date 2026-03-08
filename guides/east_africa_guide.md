# East Africa Colonial Office List - Extraction Guide

## Overview

This guide provides instructions for extracting personnel data from East Africa Colonial Office List files (1890-1964). The East Africa group encompasses a cluster of British territories in eastern Africa that evolved from chartered company rule and Foreign Office protectorates into Crown colonies and eventually independent nations.

**Target Model**: Gemini 3 Flash Preview (via API)

---

## Source Files

### Colonies in This Group
- **Imperial British East Africa Company** (1890 only)
- **East Africa Protectorate** (1896-1920) -- renamed Kenya
- **Kenya Colony and Protectorate** (1922-1964)
- **Uganda Protectorate** (1900-1963)
- **Tanganyika Territory** (1920-1962) -- League of Nations Mandate / UN Trust Territory
- **Zanzibar Protectorate** (1896-1964)
- **Nyasaland Protectorate** (1896-1964) -- previously "British Central Africa"
- **Somaliland Protectorate** (1905-1961)
- **East Africa High Commission** (1949 onwards)

### Available Years (~273 files)
Files are named variously depending on era:
- `imperial_british_east_african_company.txt` (1890)
- `british_east_africa_and_zanzibar.txt` (1896)
- `EAST_AFRICA_PROTECTORATE.md` / `.txt`
- `KENYA.txt` / `kenya.txt` / `THE_KENYA_COLONY_AND_PROTECTORATE.txt`
- `UGANDA.md` / `UGANDA.txt` / `uganda.txt`
- `TANGANYIKA_TERRITORY.md` / `TANGANYIKA.txt` / `tanganyika.txt`
- `ZANZIBAR.md` / `ZANZIBAR.txt` / `zanzibar.txt`
- `NYASALAND_PROTECTORATE.md` / `NYASALAND.txt` / `nyasaland.txt`
- `BRITISH_CENTRAL_AFRICA.md` / `british_zambezia_and_british_central_africa.txt`
- `SOMALILAND_PROTECTORATE.md` / `SOMALILAND.txt` / `somaliland.txt`
- `East_Africa_High_Commission.txt`

---

## Historical Context

### Administrative Evolution

| Era | Territory | Characteristics |
|-----|-----------|-----------------|
| 1888-1895 | Imperial British East Africa Company | Chartered company; minimal staff listed |
| 1895-1905 | East Africa Protectorate | Foreign Office control; Commissioner titles |
| 1894-1905 | Uganda Protectorate | Foreign Office; "Special Commissioner" title |
| 1905-1920 | East Africa Protectorate | Transferred to Colonial Office; Governor from 1906 |
| 1920 | Kenya Colony created | East Africa Protectorate renamed; "Colony and Protectorate" |
| 1920 | Tanganyika Territory | British Mandate over former German East Africa |
| 1890-1964 | Zanzibar | Sultanate under British Resident; unique administration |
| 1891-1964 | Nyasaland | "British Central Africa" until 1907; then Nyasaland |
| 1884-1960 | Somaliland | Small protectorate; military-style administration |
| 1948-1961 | East Africa High Commission | Inter-territorial coordination body |

### Key Name Changes and Transitions

1. **Imperial British East Africa Company** (1888-1895) -- territory transferred to Crown 1 July 1895
2. **East Africa Protectorate** (1895-1920) -- Foreign Office until 1905, then Colonial Office; became **Kenya Colony and Protectorate** (23 July 1920)
3. **British Central Africa Protectorate** (1891-1907) -- name changed to **Nyasaland Protectorate** (October 1907); Foreign Office until March 1904
4. **German East Africa** -- became **Tanganyika Territory** (1920) under British League of Nations Mandate
5. **Somaliland Protectorate** -- under Aden (Government of India) until 1898, then Foreign Office, then Colonial Office from 1 April 1905

### Regional Divisions (where applicable)

**Kenya** (post-1920):
- Colony (the interior, excised from Protectorate)
- Protectorate (10-mile coastal strip under Sultan of Zanzibar)
- Provinces: Nyanza, Rift Valley, Central, Coast, Northern, Masai

**Tanganyika** (post-1920):
- Provinces: Eastern (Dar-es-Salaam), Lake, Southern Highlands, Northern, Central, Western, Tanga, Southern

**Uganda** (post-1905):
- Provinces: Buganda, Eastern, Western, Northern
- Kingdom of Buganda (special status, "Kabaka" as ruler)

**Nyasaland**:
- Four Provinces: Northern, Central, Southern, Shire Highlands
- Districts under District Commissioners

**Zanzibar**:
- Zanzibar Island
- Pemba Island

---

## Data Schema

### Official Record Structure

Refer to `guides/schema.py` for the canonical 20-field schema. The 5 required fields are:
- `name`, `canonical_name`, `surname`, `position`, `department`

```python
{
    "name": "Sir Donald Stewart",                # Name as appears in source
    "canonical_name": "Stewart, Donald",         # "Surname, Given Names"
    "given_names": "Donald",
    "surname": "Stewart",
    "position": "Commissioner, Commander-in-Chief, and Consul-General",
    "department": "Civil Establishment - East Africa Protectorate",

    # Salary fields
    "salary_min": 2000,
    "salary_max": 2000,
    "salary_scale": None,
    "allowances": None,
    "duty_allowance": None,
    "expatriation_pay": None,
    "per_diem": None,

    # Status fields
    "acting_status": None,

    # Classification
    "honors": ["K.C.M.G."],
    "qualifications": [],
    "military_rank": None,

    # Location fields
    "location": None,
    "region": None,
}
```

### Department Naming Convention

Use the pattern: `Department Name - Colony Name`

Examples:
- `Civil Establishment - East Africa Protectorate`
- `Secretariat - Kenya`
- `Administrative Department - Tanganyika`
- `Medical Department - Uganda`
- `Police and Prisons - Tanganyika`
- `Civil Establishment - Zanzibar`
- `Administration - Somaliland`
- `Provincial Administration - Kenya`

---

## Department List by Era

### 1890 (Imperial British East Africa Company)
- No department structure -- a narrative description with a few named officers

### 1896-1905 (Foreign Office Era - East Africa, Zanzibar, Uganda)
Very sparse listings, often just a handful of officers:
- Commissioner's Office
- Sub-Commissioners (by province)
- Commandant of Forces
- (No formal department headers in most cases)

**East Africa Protectorate 1905 real example:**
```
Commissioner, Commander-in-Chief, and Consul-General, Sir Donald Stewart, K.C.M.G., 2,000l.
Deputy Commissioner, F. J. Jackson, C.B., C.M.G., 1,000l.
Sub-Commissioner (Mombasa), C. R. W. Lane, C.M.G.
Ditto (Ukaraba), J. Ainsworth, C.M.G.
```

**Uganda 1905:**
```
H.M. Commissioner and Commander-in-Chief, Lieut.-Col. J. H. Sadler, C.B., 1,500l.
Deputy Commissioner, George Wilson, C.B., 800l.
Commandant of the King's African Rifles and of the Troops in the Protectorate, Col. A. H. Coles, C.M.C., D.S.O., 900l.
Secretary, J. F. Cunningham, F.Z.S., F.R.G.S., 650l.
```

### 1905-1920 (Colonial Office Era - Expanded)
Departments begin to appear more formally:
- Commissioner/Governor's Office
- Secretariat
- Treasury
- Customs
- Judicial / Legal
- Medical Department
- Police / Constabulary
- Post and Telegraphs
- Public Works
- Administrative Department (District Officers)
- Education (emerging)
- Agriculture (emerging)

### 1920-1940 (Peak Expansion - Kenya, Tanganyika, Uganda)
Full departmental structure in all territories:

**Kenya (1922 onwards):**
- Governor and Personal Staff
- Secretariat
- Provincial Administration / Native Affairs Department
- Treasury
- Customs
- Audit
- Judicial Department
- Attorney General's Department
- Police Department
- Prisons Department
- Medical Department
- Chemical Research Department
- Education
- Trigonometrical and Topographical Survey
- Agricultural Department
- Veterinary Department
- Forestry
- Game Department
- Public Works Department
- Railway Department
- Marine Department
- Department of Lands (Lands Division, Survey Division, Registry Division)
- Post and Telegraphs Department

**Tanganyika (1920 onwards):**
- Governor and Personal Staff
- Secretariat
- Printing Department
- Administrative Department
- Treasury
- Customs Department
- Port and Marine
- Audit Department
- Legal Department (Chief Justice, Attorney-General)
- Police and Prisons
- Medical Department
- Veterinary Department
- Education Department
- Transport Department
- Post and Telegraphs Department
- Railway Department
- Agricultural Department
- Public Works Department
- Tsetse Research (unique to Tanganyika)
- Land Department
- Survey Department
- Mines Department
- Geological Survey
- Game Preservation
- Forestry

**Somaliland (1930):**
- Governor's Office (Secretary to the Government)
- Administration (Commissioners by district)
- Treasury
- Police
- Prisons
- Medical Department
- Customs Department
- Posts and Telegraphs Department
- Public Works Department
- Veterinary Department
- Geological and Agricultural Department
- Camel Corps, King's African Rifles (military unit)

**Zanzibar (1930):**
- British Resident's Office
- Chief Secretary
- Provincial Commissioners (Zanzibar, Pemba)
- Treasury
- Legal Department
- Medical and Sanitary Services
- Agriculture
- Education
- Public Works
- Police
- Customs
- Post Office

### 1940-1964 (Late Colonial)
All above plus:
- Accountant General (Kenya)
- African Information Services (Kenya)
- Labour Department
- Income Tax
- Co-operative Development
- Social Welfare
- Town Planning
- Water Development
- East Africa High Commission departments (from 1948)
- Geological Survey (expanded)

---

## Extraction Patterns

### Title Patterns (appear BEFORE name)
```
Military: Colonel, Col., Lt.-Col., Lieut.-Col., Major-General, Major, Captain, Capt., Brigadier, Brigadier-General, Comdr., Commander, Lieut., Wing Cdr., Sub-Lieut.
Honorific: Sir, The Right Hon., The Hon., Right Rev., Rev., Ven., Dr.
```

### Honors (appear AFTER name)
```
K.C.M.G., G.C.M.G., C.M.G., K.C.B., G.C.B., C.B., K.B.E., O.B.E., M.B.E.,
C.B.E., K.C.S.I., C.I.E., D.S.O., M.C., V.D., E.D., T.D., Kt., Knt.,
K.C.V.O., D.S.C., R.R.C., D.F.C., D.C.M., M.M., V.C.
```

### Qualifications (appear AFTER name)
```
Medical: M.D., M.B., M.R.C.S., F.R.C.S., L.R.C.S., L.R.C.P., Ch.B., D.P.H., D.T.M.&H., M.R.C.V.S.
Academic: B.A., M.A., B.Sc., M.Sc., LL.D., D.D., Ph.D., LL.B., B.E.
Engineering: R.E., C.E., M.I.C.E., A.M.I.C.E., M.I.E.E., A.M.I.E.E., M.I.Mech.E.
Other: F.R.S., F.R.G.S., F.Z.S., A.R.I.B.A., F.G.S., F.S.I., R.N., R.N.R.
```

---

## Salary Formats

### Early Era (1890-1920s) - Pounds with "l."
```
Simple: 2,000l.                        -> salary_min: 2000, salary_max: 2000
Range: 500l. by 25l. to 600l.         -> salary_min: 500, salary_max: 600
With comment: (Each 600l.)             -> salary_min: 600, salary_max: 600 (for all preceding entries)
```

**Real examples from East Africa Protectorate 1905:**
```
Commissioner, Commander-in-Chief, and Consul-General, Sir Donald Stewart, K.C.M.G., 2,000l.
Deputy Commissioner, F. J. Jackson, C.B., C.M.G., 1,000l.
Sub-Commissioner (Mombasa), C. R. W. Lane, C.M.G.
Ditto (Ukaraba), J. Ainsworth, C.M.G.
Ditto (Tana-land), K. MacDougall.
Ditto (Jubaland), Major L. R. H. Pope-Hennesey (acting).
Ditto (Kenya), S. L. Hinde.
Ditto (Naivasha), S. S. Bagge. (Each 600l.)
```
Note: "(Each 600l.)" means all Sub-Commissioners share the same salary.

**Real example from Uganda 1900:**
```
H.M. Special Commissioner and Commander-in-Chief, Sir Harry H. Johnston, K.C.B., 2,900l.
Deputy-Commissioner and Commandant of Troops, Col. T. P. B. Tornau, D.S.O., 1,000l.
Third in Command, Lieut.-Col. A. H. Coles, D.S.O., 800l.
```

### Transition Era (1920s-1930s) - Incremental scales with "l."
```
500l. by 25l. to 600l.               -> salary_min: 500, salary_max: 600
600l. by 25l. to 700l. by 40l. to 800l. -> salary_min: 600, salary_max: 800
300l. (two years) to 400l. by 20l. to 500l. -> salary_min: 300, salary_max: 500
```

**Real examples from Kenya 1922:**
```
Governor and Commander-in-Chief, Major-General Sir E. Northey, K.C.M.G., C.B., 4,000l., and 1,500l. duty allowance.
Colonial Secretary, Sir C. C. Bowring, K.B.E., C.M.G., 1,800l.
Assistant Colonial Secretary, G. A. S. Northcote, 800l. by 50l. to 1,000l.
Senior Assistant Secretaries, C. E. Spencer, 700l. and 100l. personal; H. B. Kittermaster, O.B.E., J. E. S. Merrick, 600l. by 25l. to 700l.
```

**Real examples from Tanganyika 1920:**
```
Administrator, Sir H. A. Byatt, K.C.M.G., 3,000l. and 1,000l. duty allowance.
Chief Secretary to the Government, A. C. Hollis, C.M.G., C.B.E., 1,200l. plus 200l. duty allowance.
District Political Officers ... 500l. by 25l. to 700l. plus 50l. duty allowance.
```
Note: Tanganyika frequently used "plus Xl. duty allowance" as a separate component.

### Later Era (1930s) - Mixed "l." and "L" notation
```
1,350L.                               -> salary_min: 1350, salary_max: 1350
720L by 30L to 840L by 40L to 920L   -> salary_min: 720, salary_max: 920
400L for two years, 475L by 25L to 600L by 30L to 840L by 40L to 920L -> salary_min: 400, salary_max: 920
```

**Real example from Tanganyika 1930:**
```
Governor and Commander-in-Chief, Sir D. C. Cameron, K.C.M.G., K.B.E., 4,500l., with 1,500l. duty allowance.
Chief Secretary, D. J. Jardine, O.B.E., 2,000l.
District Officers ... 720l. by 30l. to 840l. by 40l. to 920l.
Cadets ... 400L.
```

### Late Era (1950s) - Sterling with pound sign
```
Governor—Sir Philip Euen Mitchell, G.C.M.G., M.C. £5,000 and duty allowance, £3,500.
Chief Secretary—J. D. Rankine, C.M.G. £2,600.
Provincial Commissioners ... £1,775.
District Officers ... £550–1,320.
```

**Real example from Kenya 1950:**
```
Governor and Commander-in-Chief—Sir Philip Euen Mitchell, G.C.M.G., M.C. £5,000 and duty allowance, £3,500.
Private Secretary—Wing Cdr. J. R. Irving Bell. £775.
Aide-de-Camp—Sub-Lieut. D. W. M. Sim, R.N. £600.
Director of Agriculture—S. Gillett. £1,850.
Agricultural Officers ... £585–1,320.
```

### Duty Allowance Patterns
Duty allowances are very common in East Africa, especially Tanganyika:
```
3,000l. and 1,000l. duty allowance    -> salary_min: 3000, duty_allowance: 1000
1,200l. plus 200l. duty allowance     -> salary_min: 1200, duty_allowance: 200
500l. by 25l. to 700l. plus 50l. duty allowance -> salary_min: 500, salary_max: 700, duty_allowance: 50
£5,000 and duty allowance, £3,500     -> salary_min: 5000, duty_allowance: 3500
```

### Currency Note
- **Kenya, Uganda, Tanganyika**: British pounds (GBP) throughout, expressed as "l.", "L", or "£"
- **Zanzibar**: Early files use Indian Rupees (Rs.); later shifts to East African Shillings
- **Somaliland**: Early files use Indian Rupees; later East African Shillings
- **Nyasaland**: British pounds (GBP) throughout
- Set `salary_currency` to `"GBP"` for pound-denominated salaries; `"Rs"` for rupee salaries

---

## Special Patterns

### "Ditto" - References previous position type
Very common in early East Africa files:
```
Sub-Commissioner (Mombasa), C. R. W. Lane, C.M.G.
Ditto (Ukaraba), J. Ainsworth, C.M.G.
Ditto (Tana-land), K. MacDougall.
```
-> "Ditto" = "Sub-Commissioner"; the location in parentheses changes.

Another pattern from East Africa 1900:
```
Sub-Commissioner, Ukimba, J. Ainsworth, 500l.
Ditto Tanaland and Resident in Witu, A. S. Rogers, 700l.
Ditto Jubaland, A. C. W. Jenner, 500l.
```
-> "Ditto" = "Sub-Commissioner"; the province/location follows directly.

### Acting/Temporary Status - ALWAYS CAPTURE
```
Major L. R. H. Pope-Hennesey (acting)  -> acting_status: "Acting"
H. L. Sikes, B.A., B.E., A.M.Inst.C.E., F.G.S., (Acting) -> acting_status: "Acting"
Assistant Matron, Miss E. Hamilton (tempy.) -> acting_status: "Temporary"
Acting Commissioner of Prisons, S. R. Hill, M.C. -> acting_status: "Acting"
```

### Multiple People on One Line
Very common in East Africa lists, especially for District Officers, Cadets, and Medical Officers.

#### Pattern 1: Comma-separated list with shared salary
```
Senior Medical Officers, F. L. Henderson, G. R. H. Chell, J. Pugh, C. J. Wilson, M.C., N. P. Jewell, M.C., 700l. by 25l. to 800l.
```
-> Creates FIVE officials, each with salary_min: 700, salary_max: 800.

#### Pattern 2: Named individuals with different salaries
```
Senior Assistant Secretaries, C. E. Spencer, 700l. and 100l. personal; H. B. Kittermaster, O.B.E., J. E. S. Merrick, 600l. by 25l. to 700l.
```
-> Spencer gets 700l. + allowance; Kittermaster and Merrick get 600-700l.

#### Pattern 3: Unnamed count
```
Nine District Officers and sixteen Assistant District Officers.
Fifteen District Officers and twenty-eight Assistant District Officers (or Collectors).
Four 1st Class Assistants, 8 2nd Class Assistants, 15 3rd Class Assistants.
```
-> SKIP these -- no names to extract.

#### Pattern 4: Long lists of District Officers / Cadets
Kenya and Tanganyika have extremely long comma-separated lists:
```
District Officers, D. R. Crampton, C. H. Adams, Lieut. J. A. G. Elliot, F. M. Lamb, ... (dozens more) ... 600l. by 25l. to 700l.
```
-> Create one entry per person. ALL share the same salary range.

### Vacancies
```
Deputy Commissioner (vacant).           -> SKIP in early era
Director of Public Works (vacant), 1,200l. -> SKIP in early era
Director of Agriculture—Vacant. £1,850. -> In late era: Create entry with name: null
```

### "Personal Allowance" and "Non-Pensionable" Notes
```
Treasurer, S. S. Davis, C.M.G., 800l. by 50l. to 1,000l. plus 80l. duty allowance and 100l. personal allowance.
-> salary_min: 800, salary_max: 1000, duty_allowance: 80, allowances: "100l. personal allowance"

Principal Medical Officer, R. S. Taylor, 1,000l. by 50l. to 1,100l., plus 100l. non-pensionable, duty allowance.
-> salary_min: 1000, salary_max: 1100, allowances: "100l. non-pensionable duty allowance"
```

### Secondment Notes (1950s)
```
Colonel E. L. B. Anderson, C.B.E., D.S.O. (seconded to African Settlement and Land Utilization Board)
```
-> Extract as normal; note the secondment in the position or ignore it.

---

## Location/Region Extraction Rules

### Location in Position Title
```
Sub-Commissioner (Mombasa), C. R. W. Lane, C.M.G.
-> position: "Sub-Commissioner", location: "Mombasa"

Sub-Commissioner, Ukimba, J. Ainsworth, 500l.
-> position: "Sub-Commissioner", location: "Ukimba"

Collector of Customs, Mombasa, G. D. Kirropp, 500l. by 25l. to 600l.
-> position: "Collector of Customs", location: "Mombasa"

Superintendent, Mombasa, S. R. Hill, M.C., 400l. by 20l. to 500l.
-> position: "Superintendent", location: "Mombasa"
```

### Location in Section Header
```
Nairobi "A."
Headmaster, R. A. Low, 600l. to 700l.
-> position: "Headmaster", location: "Nairobi"

Nakuru "A."
Headmaster, E. R. Pratt, 500l. to 600l.
-> position: "Headmaster", location: "Nakuru"

Scott Agricultural Laboratory.
Mycologist, J. McDonald, 600l. by 30l. to 840l.
-> position: "Mycologist", department: "Scott Agricultural Laboratory - Kenya"
```

### Region from Colony Structure
For Kenya, assign region based on the section context:
- Officers listed under "Provincial Administration" with province assignments get `region` set accordingly
- Coast Province officers -> `region: "Coast"`
- Northern Province -> `region: "Northern"`

### Common Locations by Colony

**Kenya**: Nairobi, Mombasa, Kisumu, Nakuru, Eldoret, Nyeri, Kitale, Machakos, Nanyuki, Malindi, Lamu, Fort Hall, Kiambu, Voi, Kericho, Embu, Meru, Naivasha

**Uganda**: Entebbe (capital), Kampala, Jinja, Mbale, Fort Portal, Gulu, Soroti, Masaka, Hoima, Arua, Lira

**Tanganyika**: Dar-es-Salaam (capital), Tanga, Moshi, Arusha, Tabora, Dodoma, Mwanza, Ujiji, Kigoma, Iringa, Lindi, Mtwara, Kilosa

**Zanzibar**: Zanzibar (town), Pemba

**Nyasaland**: Zomba (capital), Blantyre, Lilongwe, Fort Johnston, Karonga, Nkhotakota (Kota-Kota)

**Somaliland**: Berbera, Burao, Hargeisa, Sheikh, Zeyla, Bulhar

---

## Era-Specific Extraction Notes

### 1890 (Imperial British East Africa Company)
- **Title**: Company officers only -- "Managing Director in East Africa"
- **Structure**: Narrative text with officers listed in a single paragraph
- **Names**: Minimal staff; directors listed as company board, not local officers
- **Format**: Names embedded in prose, not a structured list
- **Expected officials**: 3-5 (local officers only)

**Real example (1890):**
```
Chief Local Officers.
G. S. Mackenzie, Managing Director in East Africa. Lieut. Swayne, F. J. Jackson, and J. R. W. Pigott.
```

### 1896-1905 (Foreign Office Era)
- **Title**: "Administrator" (East Africa 1896), "Commissioner" (East Africa 1900-1905), "Special Commissioner" (Uganda)
- **Structure**: Very sparse; usually fewer than 20 named officials per territory
- **Salaries**: Often in "Xl." format; many positions without salary
- **Zanzibar**: Uses consular titles -- "Agent and Consul-General", "Vice-Consul"
- **Somaliland**: Military-style titles -- "Commissioner, Consul-General and Commander-in-Chief"
- **Expected officials**: 3-20 per territory

**Real example -- Zanzibar 1905:**
```
His Majesty's Agent and Consul-General, Basil S. Cave, C.B.
Vice-Consuls, J. H. Sinclair, H. C. Venables.
Vice-Consul at Pemba, D. R. O'Sullivan-Bearne.
Judge, Lindsey Smith.
```

**Real example -- Somaliland 1905:**
```
Commissioner, Consul-General and Commander-in-Chief, Brigadier-General E. J. E. Swayne, I.A.
Sub-Commissioner and Consul at Berbera, Capt. H. E. S. Cordeaux, C.M.G.
Vice-Consul at Zeyla, Mr. W. Malcolm Jones.
District Officer at Bulhar, Mr. E. le P. Power.
```

### 1905-1920 (Colonial Office Transition)
- **East Africa Protectorate**: "Commissioner" becomes "Governor" (1906 Order in Council)
- **Uganda**: Same transition, though "Commissioner" remains in some references
- **Structure**: Departments begin to form; clear section headers
- **Military notation**: "I.A." (Indian Army), "R.A.M.C." (Royal Army Medical Corps)
- **Expected officials**: 20-50 per territory

### 1920-1930 (Mandate and Colony Era)
- **Kenya**: Major expansion post-1920 annexation; 200+ officials
- **Tanganyika**: New territory; many vacancies marked; distinctive "plus Xl. duty allowance" pattern
- **Currency transition**: Indian Rupee demonetized 1921; East African Shilling introduced
- **Salary notation**: "l." format with incremental scales (e.g., "500l. by 25l. to 700l.")
- **Expected officials**: Kenya 300-500, Tanganyika 150-300, Uganda 100-200

**Key Tanganyika pattern -- duty allowance on every salary:**
```
District Political Officers ... 500l. by 25l. to 700l. plus 50l. duty allowance.
1st grade Assistant Political Officers ... 400l. by 20l. to 500l. plus 40l. duty allowance.
```
-> The duty allowance is proportional to the base salary and should always be captured.

### 1930-1940 (Peak Complexity)
- **All territories**: Full department structures established
- **Large staff lists**: Kenya and Tanganyika have hundreds of named officials each
- **Cadets**: Large cadet intakes post-WWI; listed at lowest salary grades
- **Railway staff**: Major section in Kenya (shared with Uganda) and Tanganyika
- **Tsetse Research** (Tanganyika only): Specialized research department
- **Expected officials**: Kenya 400-600, Tanganyika 300-500, Uganda 150-250

**Real example -- Tanganyika 1930 Cadets (long list):**
```
Cadets, A. L. Harris, J. R. C. Priddle, C. H. Gormley, ... (80+ names) ... 400L.
```
-> All cadets share the same salary.

### 1940-1950 (War and Post-War)
- **Format shift**: Move toward "£" notation
- **New departments**: Labour, Commerce and Industry, Information Services
- **Member system** (Kenya): Executive Council members double as department heads ("Member for Agriculture and Natural Resources")
- **Abbreviations**: "Ag." for "Acting" becomes common
- **Expected officials**: Kenya 400-500, Tanganyika 300-400

### 1950-1964 (Late Colonial / Decolonization)
- **Format**: Standardized departmental headers; salary in "£" with ranges using dash (e.g., "£550-1,320")
- **Em dash**: Position name separated from person by em dash ("Governor—Sir Philip Mitchell")
- **Simplified structure**: Fewer very long multi-person lines; cleaner formatting
- **Independence transitions**: Tanganyika (1961), Uganda (1962), Kenya (1963), Zanzibar (1963), Nyasaland/Malawi (1964)
- **Expected officials**: Kenya 300-500, Tanganyika 200-400

---

## Special Colony-Specific Patterns

### Zanzibar - Unique Administration
Zanzibar has a distinctive administrative structure:
- **British Resident** (not Governor) -- head of British administration
- **Sultan** -- titular head of state ("His Highness the Sultan")
- **Dual court system**: British Court and Sultan's Court
- **Currency**: Indian Rupees early; later East African currency
- **Small staff**: Typically 30-80 officials

**Real example -- Zanzibar 1930 Executive Council:**
```
H.H. the Sultan, President.
The British Resident, Vice-President.
The Chief Secretary.
The Treasurer.
The Attorney-General.
```
-> Extract the British Resident as the senior British official, not the Sultan.

### Somaliland - Military Character
Somaliland has a strongly military administration:
- **Camel Corps / King's African Rifles**: Military unit with commissioned officers listed
- **Small civil service**: Typically 20-40 officials total
- **Commissioners**: District officials called "Commissioners" (not "District Commissioners")
- **Consul**: "Consul at Harar" -- British representative in Abyssinia

**Real example -- Somaliland 1930:**
```
Governor and Commander-in-Chief, Sir H. B. Kittermaster, K.B.E., C.M.G., 1,700l. and duty allowance 350l.
Secretary to the Government, Major A. S. Lawrance, D.S.O., 900l. by 50l. to 1,100l.
Commissioners, Major B. H. Horsley, D.S.O., M.C., Capt. E. N. Park, M.C., 500l. by 25l. to 700l.; R. H. Smith, ... each 450l. by 25l. to 550l. by 30l. to 700l. by 40l. to 800l.
```

### Nyasaland - Compact Colony
- **Separate from East African currency union** -- uses sterling throughout
- **Close links to Southern Africa** -- railway connects via Mozambique to Beira
- **Four provinces**: Under Provincial Commissioners
- **Expected officials**: 50-150

**Real example -- Nyasaland 1930:**
```
Governor and Commander-in-Chief, T. S. W. Thomas, C.M.G., O.B.E., 2,500l., 500l. allowance.
Chief Secretary, Lieut.-Col. W. B. Davidson-Houston, C.M.G., 1,450l.
Government Printer, T. T. Davies, 480l. to 500l. by 20l., to 600l. by 25l. to 720l. by 30l.; Stationery allowance, 25l.
```

### East Africa High Commission (1948+)
- **Inter-territorial body**: Not a colony; coordinates services across Kenya, Uganda, Tanganyika
- **Departments**: Railways and Harbours, Posts and Telegraphs, Customs, Research
- **Staff may appear in multiple lists**: Some officials seconded from individual colonies

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

---

## Validation Checklist

### All Years, All Territories
- [ ] Officials list is non-empty
- [ ] All entries have name, canonical_name, surname, position, and department fields
- [ ] Salaries parsed (where present in source)
- [ ] Honors and qualifications in correct fields (not mixed up)
- [ ] "Ditto" entries expanded to proper position names
- [ ] Military ranks extracted where present
- [ ] Acting status captured where noted

### 1890 (IBEA Company)
- [ ] At least 3 named officers extracted
- [ ] Company directors NOT extracted (they are London-based board members)

### 1896-1905 (Foreign Office Era)
- [ ] Commissioner / Administrator captured for East Africa
- [ ] Special Commissioner captured for Uganda
- [ ] Consul-General titles captured for Zanzibar
- [ ] Sub-Commissioners captured with locations
- [ ] Expect 3-20 officials per territory

### 1905-1920 (Colonial Office Transition)
- [ ] Governor title appears (from 1906 for East Africa, 1907 for Nyasaland)
- [ ] Department heads captured
- [ ] Military Commandant / King's African Rifles officers captured
- [ ] Expect 20-50 officials per territory

### 1920-1940 (Expanded Administration)
- [ ] Governor captured for Kenya, Tanganyika, Uganda, Nyasaland, Somaliland
- [ ] British Resident captured for Zanzibar
- [ ] Colonial/Chief Secretary captured
- [ ] All major department heads captured
- [ ] District Officers / Political Officers lists fully extracted
- [ ] Railway staff captured (major section in Kenya and Tanganyika)
- [ ] Duty allowances captured (especially in Tanganyika)
- [ ] Expect 100-600 officials per territory

### 1950-1964 (Late Colonial)
- [ ] Governor and Executive Council members captured
- [ ] "Member for X" designations noted in position
- [ ] Sterling (£) salaries correctly parsed
- [ ] Range format (£550-1,320) correctly parsed as salary_min/salary_max
- [ ] Secondment notes not confused with position names

---

## Key Positions by Era

### 1890 (IBEA Company)
1. Managing Director in East Africa

### 1896-1905
1. Commissioner / Administrator / Agent and Consul-General
2. Deputy Commissioner / Sub-Commissioner
3. Commandant of Forces
4. Secretary
5. Judge / Judicial Vice-Consul

### 1905-1920
1. Commissioner (becoming Governor)
2. Deputy Commissioner
3. Secretary to Administration / Colonial Secretary
4. Treasurer
5. Chief of Customs
6. Principal Medical Officer
7. Commandant of Forces / King's African Rifles

### 1920-1940
1. Governor and Commander-in-Chief
2. Colonial Secretary / Chief Secretary
3. Chief Justice
4. Attorney-General
5. Treasurer
6. Director of Medical and Sanitary Services
7. Director of Education
8. Director of Agriculture
9. Director of Public Works
10. Commissioner of Police
11. General Manager, Railways
12. Postmaster-General
13. Secretary for Native Affairs (Tanganyika)
14. Chief Native Commissioner (Kenya)
15. Conservator of Forests

### 1950-1964
1. Governor and Commander-in-Chief
2. Chief Secretary (and Member for Development)
3. Financial Secretary (and Member for Finance)
4. Attorney-General (and Member for Law and Order)
5. Chief Native Commissioner / Member for African Affairs
6. Member for Agriculture and Natural Resources
7. Member for Health and Local Government
8. Deputy Chief Secretary (and Member for Education)
9. Chief Justice
10. Accountant General
11. Director of Medical Services
12. Commissioner of Police

---

## Sample Output

### 1905 Style (Foreign Office, Sparse)
```python
{
    "name": "Sir Donald Stewart",
    "canonical_name": "Stewart, Donald",
    "given_names": "Donald",
    "surname": "Stewart",
    "position": "Commissioner, Commander-in-Chief, and Consul-General",
    "department": "Civil Establishment - East Africa Protectorate",
    "salary_min": 2000,
    "salary_max": 2000,
    "honors": ["K.C.M.G."],
    "location": None,
    "region": None,
}
```

### 1922 Style (Kenya, Detailed)
```python
{
    "name": "Major-General Sir E. Northey",
    "canonical_name": "Northey, E.",
    "given_names": "E.",
    "surname": "Northey",
    "position": "Governor and Commander-in-Chief",
    "department": "Civil Establishment - Kenya",
    "salary_min": 4000,
    "salary_max": 4000,
    "duty_allowance": 1500,
    "honors": ["K.C.M.G.", "C.B."],
    "military_rank": "Major-General",
    "location": None,
    "region": None,
}
```

### 1920 Style (Tanganyika, with duty allowance)
```python
{
    "name": "Sir H. A. Byatt",
    "canonical_name": "Byatt, H. A.",
    "given_names": "H. A.",
    "surname": "Byatt",
    "position": "Administrator",
    "department": "Civil Establishment - Tanganyika",
    "salary_min": 3000,
    "salary_max": 3000,
    "duty_allowance": 1000,
    "honors": ["K.C.M.G."],
    "location": None,
    "region": None,
}
```

### 1930 Style (Somaliland, Military Administration)
```python
{
    "name": "Major B. H. Horsley",
    "canonical_name": "Horsley, B. H.",
    "given_names": "B. H.",
    "surname": "Horsley",
    "position": "Commissioner",
    "department": "Administration - Somaliland",
    "salary_min": 500,
    "salary_max": 700,
    "honors": ["D.S.O.", "M.C."],
    "military_rank": "Major",
    "location": None,
    "region": None,
}
```

### 1950 Style (Kenya, Late Colonial)
```python
{
    "name": "Sir Philip Euen Mitchell",
    "canonical_name": "Mitchell, Philip Euen",
    "given_names": "Philip Euen",
    "surname": "Mitchell",
    "position": "Governor and Commander-in-Chief",
    "department": "Governor and Personal Staff - Kenya",
    "salary_min": 5000,
    "salary_max": 5000,
    "duty_allowance": 3500,
    "honors": ["G.C.M.G.", "M.C."],
    "location": None,
    "region": None,
}
```

### 1930 Style (Zanzibar, British Resident)
```python
{
    "name": "Basil S. Cave",
    "canonical_name": "Cave, Basil S.",
    "given_names": "Basil S.",
    "surname": "Cave",
    "position": "His Majesty's Agent and Consul-General",
    "department": "Civil Establishment - Zanzibar",
    "salary_min": None,
    "salary_max": None,
    "honors": ["C.B."],
    "location": "Zanzibar",
    "region": None,
}
```

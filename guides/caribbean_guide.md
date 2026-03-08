# Caribbean Colonies - Colonial Office List Extraction Guide

## 1. Overview

This guide provides instructions for extracting personnel data from Caribbean colony
entries in the Colonial Office List (1867-1966). It covers **standalone colony files**
for individual Caribbean territories. The Leeward Islands and Windward Islands as
federated territories have their own separate guide; however, individual island colonies
that appear as standalone files (e.g., Dominica, Antigua, St Vincent, St Lucia, Grenada,
Montserrat, Nevis) are covered HERE when they appear independently.

### Colonies Covered

**Major colonies**: Jamaica, Trinidad (& Tobago), Barbados, British Guiana, British Honduras, Bahamas, Bermuda

**Smaller colonies** (also appear under Leeward/Windward Islands federation files):
Dominica, Antigua, St Vincent, St Lucia, Grenada, Montserrat, Nevis, Anguilla,
Virgin Islands, St Christopher and Nevis

**Dependencies** (within parent colony files): Cayman Islands (Jamaica),
Turks and Caicos Islands (Jamaica until 1959), Tobago (Trinidad from 1889)

File names vary: `jamaica.txt`, `JAMAICA.txt`, `trinidad_and_tobago.txt`, etc.
Early files may combine colonies (e.g., 1867 `barbados.txt` includes Bermudas section).

---

## 2. Historical Context

### Constitutional Variation - CRITICAL

Caribbean colonies had **very different constitutional arrangements**, unlike the more
uniform Crown Colony system in West Africa. This matters for extraction because
governance bodies differ:

| Colony | Constitution Type | Key Difference |
|--------|------------------|----------------|
| Jamaica | Crown Colony (post-1866) | Governor + Legislative Council; House of Representatives from 1944 |
| Trinidad | Crown Colony | Governor + Legislative Council |
| Barbados | **Representative Government** | **Elected House of Assembly** retained throughout; unique among Caribbean colonies |
| British Guiana | Modified Representative | Court of Policy, Financial Representatives, College of Electors (pre-1928); Legislative Council from 1928 |
| Bahamas | Representative Government | Elected House of Assembly |
| Bermuda | Representative Government | Elected House of Assembly |
| British Honduras | Crown Colony | Governor + Legislative Council |

### Administrative Evolution

| Era | Key Changes |
|-----|-------------|
| 1867-1870s | Many small colonies listed independently; very sparse data |
| 1870s-1880s | Leeward Islands federation (1871); Tobago merged with Trinidad (1889) |
| 1890s-1910s | Consolidation period; departments expand; salary ranges appear |
| 1920s-1930s | Currency transitions; salary scale systems introduced |
| 1940s-1950s | Adult suffrage introduced; ministerial systems begin; dollar currencies spread |
| 1958-1962 | West Indies Federation period |

### Regional Divisions Within Colonies

- **Jamaica**: 14 parishes; Cayman Islands and Turks & Caicos as dependencies
- **British Guiana**: Three counties (Demerara, Essequibo, Berbice); interior districts
- **Trinidad and Tobago**: Counties/wards; Tobago as separate ward
- **Barbados**: 11 parishes (St Michael, Christ Church, St George, etc.)

---

## 3. Data Schema

### Official Record Structure

```python
{
    # REQUIRED fields
    "name": "Sir John Peter Grant",           # Name as appears in source
    "canonical_name": "Grant, Sir John Peter", # "Surname, Given Names"
    "surname": "Grant",
    "position": "Governor",
    "department": "Civil Establishment - Jamaica",  # "Dept - Colony" format

    # OPTIONAL fields
    "given_names": "John Peter",
    "salary_min": 7000,               # Minimum salary (numeric)
    "salary_max": 7000,               # Maximum salary (numeric)
    "salary_currency": "GBP",         # GBP, BWI$, BG$, BH$ (see Currency section)
    "salary_scale": None,             # "A", "B", "C.1" etc. (1940s-50s)
    "allowances": "1,500l. duty allowance",
    "duty_allowance": 1500,           # Numeric duty allowance
    "expatriation_pay": None,         # 1940s-50s expatriate compensation
    "per_diem": None,                 # Daily rate if applicable
    "acting_status": None,            # "Acting", "Temporary", "Officiating", "Relief"
    "honors": ["K.C.B."],            # Post-nominal honors
    "qualifications": [],             # Academic/professional qualifications
    "military_rank": None,            # "Colonel", "Major", etc.
    "location": None,                 # Specific station (e.g., "Montego Bay")
    "region": None,                   # Sub-colony region (e.g., "Demerara")
}
```

### Department Naming Convention

ALWAYS use format: **"Department Name - Colony Name"**

```
Governor's Office - Jamaica
Colonial Secretary's Office - Trinidad and Tobago
Customs - Barbados
Medical Department - British Guiana
Judicial - British Honduras
Ecclesiastical - Trinidad
Warden's Office - Tobago
```

For sub-sections within a colony, use the ward/county when it forms a distinct
administrative unit:
```
Administration - Tobago          (Tobago ward within Trinidad and Tobago)
District Commissioner - Demerara (county within British Guiana)
```

---

## 4. Department List by Era

### Early Era (1867-1890s)

Common: Civil Establishment, Executive Council, Legislative Council, Colonial Secretary's
Office, Treasury, Customs, Post Office, Medical, Judicial, Police, Ecclesiastical, Public Works

Colony-specific: House of Assembly (Barbados/Bahamas/Bermuda), Immigration (Jamaica/BG),
Roman Catholic Establishment (Trinidad), Court of Policy/College of Electors (BG),
Warden system (Trinidad), Police Magistrates by parish (Barbados)

### Middle Era (1900-1930s) - Additional departments

Agriculture, Education, Railway (Jamaica/BG/Trinidad), Harbour, Survey, Forestry,
Bacteriological Laboratory, Prisons, Printing Office

### Late Era (1940s-1950s) - Modern structure

Civil Aviation, Commerce and Industries, Housing, Income Tax, Information, Labour,
Lands, Mines (Trinidad/BG), Social Welfare, Statistics, Town Planning, Waterworks

---

## 5. Salary Formats

### Early Era (1867-1920s) - Pounds with "l." suffix

```
Simple:           7,000l.                    -> salary_min: 7000, salary_max: 7000
Range:            300l. to 400l.             -> salary_min: 300, salary_max: 400
With shillings:   82l. 10s.                  -> salary_min: 82, salary_max: 82
With pence:       291l. 13s. 9d.             -> salary_min: 291, salary_max: 291
With allowances:  500l., and 75l. travelling -> salary_min: 500, allowances: "75l. travelling"
Fees-based:       fees averaging 500l.       -> salary_min: 500, allowances: "fees"
```

REAL EXAMPLES from source files:

Jamaica 1867:
```
Captain-General and Governor-in-Chief, Sir John Peter Grant, K.C.B., 7,000l.
```

Trinidad 1867:
```
J. O'Brien, 82l. 10s.
K. Finlay, M.D., 809l. 10s.
```

British Guiana 1867:
```
Chief Justice, Sir W. B. Arrindell, Knt., 3,000l.
Registrar of the Supreme Court, H. E. P. Sharp, 416l. 13s. 4d.
```

Barbados 1867:
```
Provost-Marshal, Robert Reece, fees averaging 500l.
```

### Middle Era (1910-1930s) - "l." or "£" notation, ranges common

Jamaica 1910:
```
Assistant Colonial Secretaries—C. C. Knollys; T. F. Roxburgh, salary, 300l. to 400l.
Resident Magistrate (Kingston)—P. S. Barnett, salary, 600l. to 700l., and 60l.
    travelling allowance.
```

Trinidad 1910:
```
Warden, Arima, C. Flanagin, 500l., and 75l. travelling allowance
Sub-Inspector of Police (San Fernando), L. M. Fraser 200l.
```

### Late Era (1940s-1950s) - Pounds (£) or Dollars ($)

Jamaica 1950 (pounds sterling):
```
Governor-in-Chief—Sir John Huggins, G.C.M.G., M.C. £4,500 and £1,500 duty allowance.
Colonial Secretary—D. C. MacGillivray, C.M.G., M.B.E. £2,000.
Assistant Secretaries—C. L. Swaby, M.B.E.; ... £800-50-1,000.
```

Barbados 1950 (dollars - BWI$):
```
Governor—A. W. L. Savage, C.M.G., $14,400. Plus $4,800 duty allowance.
Colonial Secretary—S. H. Perowne, O.B.E., $7,680.
Assistant Secretary—F. A. Bishop, C.I.S. $2,880 x 144 = 4,032.
```

Trinidad 1950 (dollars - TT$):
```
Colonial Secretary—P. M. Renison, C.M.G. $11,040.
Financial Secretary—A. R. W. Robertson, C.B.E. $9,000.
```

British Guiana 1950 (pounds sterling):
```
Governor—Sir Charles Campbell Woolley, K.C.M.G., O.B.E., M.C. £4,500.
    Allowances, £1,500. Exemption from customs duties.
Deputy Colonial Secretary—D. J. Parkinson. £1,250.
```

### Salary Range Notation in Late Era

The pattern `$2,880 x 144 = 4,032` or `£800-50-1,000` means:
- Starting salary of $2,880 (or £800)
- Annual increment of $144 (or £50)
- Maximum salary of $4,032 (or £1,000)
- Extract as: salary_min: 2880, salary_max: 4032 (or salary_min: 800, salary_max: 1000)

---

## 6. Currency - CRITICAL for Caribbean

### Currency by Colony and Era

| Colony | Early (1867-1930s) | Late (1940s-1960s) | salary_currency |
|--------|-------------------|-------------------|-----------------|
| Jamaica | GBP ("l." then "£") | GBP (£) | `"GBP"` |
| Trinidad (& Tobago) | GBP ("l.") in source, but local $ accounts | TT Dollars ($) | `"GBP"` early, `"TTD"` late |
| Barbados | GBP ("l.") | BWI Dollars ($) from 1949 | `"GBP"` early, `"BWI$"` late |
| British Guiana | GBP ("l." then "£") | BG Dollars ($) but £ in COL | `"GBP"` (COL uses £) |
| British Honduras | GBP ("l.") | BH Dollars ($) | `"GBP"` early, `"BHD"` late |
| Bahamas | GBP ("l.") | GBP (£) | `"GBP"` |
| Bermuda | GBP ("l.") | GBP (£) | `"GBP"` |

**Key rule**: If the source file uses "£" or "l.", set `salary_currency: "GBP"`. If the
source uses "$", determine the local dollar from the colony name.

**Special cases**:
- Trinidad 1950: Governor salary in £, but most civil establishment in $
- British Guiana 1950: Colonial Office List uses £ for most salaries despite local
  dollar currency (BG$ 4.80 = £1)
- Barbados: Switched from GBP to BWI$ in April 1949 (BWI$ 4.80 = £1)

When the source mixes currencies within a single file, note the currency for each
entry based on the symbol used in that specific line.

---

## 7. Extraction Patterns

### Position-Name-Salary Pattern

The basic pattern varies by era:

**Early (1867)**: `Position, Name, Honors, Salary.`
```
Colonial Secretary, Henry W. Austin, 2,000l.
Collector of Customs, H. Eales, 800l.
```

**Middle (1910)**: `Position—Name, Salary, and allowances.`
```
Colonial Secretary—W. H. Mercer, salary, 900l. to 1,000l., and 200l. lodging allowance.
```

**Late (1950)**: `Position—Name, Honors. Salary.`
```
Colonial Secretary—D. C. MacGillivray, C.M.G., M.B.E. £2,000.
```

### "Ditto" Pattern - References previous position type

```
Inspector of Police, A. L. McLean, 200l.
Ditto, Port of Spain, R. Fitzsimons, 200l.
```
-> Second entry: position = "Inspector of Police", location = "Port of Spain"

```
Chief Clerk, W. C. E. Hartley, 600l.
2nd ditto, E. Bourke, 400l.
```
-> Second entry: position = "2nd Clerk"

### Multiple People on One Line

**Pattern 1: Comma-separated with shared salary**
```
Assistant Colonial Secretaries—C. C. Knollys; T. F. Roxburgh, salary, 300l. to 400l.
```
-> Creates TWO officials, each with salary_min: 300, salary_max: 400

**Pattern 2: "each" keyword**
```
Curates, each 150l.
Rev. D. P. Hart; Rev. R. B. Doorly; Rev. B. J. Gibbon.
```
-> Creates THREE officials, each with salary_min: 150, salary_max: 150

**Pattern 3: Semicolon-separated names (1950s)**
```
Puisne Judges—R. M. Cluer, J. E. D. Carberry, C. M. MacGregor. £1,500.
```
-> Creates THREE officials, each with position "Puisne Judge" and salary 1500

**Pattern 4: Multiple people with grades (1950s Trinidad)**
```
Medical Officers (Grade A)—J. E. A. Boucaud; J. P. Watson; L. F. Chan; ... $5,760-6,240.
```
-> Creates one official per semicolon-separated name, all same salary range

### Acting/Temporary Status - ALWAYS CAPTURE

```
D. T. Gilbert, 700l., (acting Attorney-General.)
```
-> acting_status: "Acting", position: "Attorney-General" (the substantive position)

```
Acting Colonial Secretary—W. Low.
Temporary District Commissioner—J. Smith.
Officiating Colonial Secretary—T. Jones.
```
-> Extract the word before the position as acting_status

### Vacancy Handling

**Early era (1867-1930s)**: SKIP vacancies - do not create an entry.
```
Private Secretary (vacant).     -> SKIP
```

**Late era (1940s-1950s)**: Capture vacancy with salary to preserve position data.
```
Director of Agriculture—Vacant. £1,400.
-> name: "Vacant", position: "Director of Agriculture", salary_min: 1400
```

### Location Embedded in Position

```
Police Magistrate, St. Michael, Fras. Thornhill, 250l.
-> position: "Police Magistrate", location: "St. Michael"

Sub-Receiver and Harbour Master at San Fernando, J. F. Knox, 500l.
-> position: "Sub-Receiver and Harbour Master", location: "San Fernando"

Resident Magistrate (Kingston)—P. S. Barnett, salary, 600l.
-> position: "Resident Magistrate", location: "Kingston"

Warden, Arima, C. Flanagin, 500l.
-> position: "Warden", location: "Arima"
```

### Ecclesiastical Entries - Extract as valid officials

```
Bishop, Rt. Rev. R. Rawle, D.D., 2,500l.     -> qualifications: ["D.D."]
Roman Catholic Archbishop, Most Rev. Dr. Spaccapietra, 600l.
```

### House of Assembly Members (Barbados, Bahamas, Bermuda)

```
Bridgetown—E. D. Mottley; A. E. S. Lewis (Deputy Speaker).
-> Two officials: position: "Member, House of Assembly", location: "Bridgetown"
```

---

## 8. Honors, Qualifications, and Military Rank

### Honors (Post-nominal, service-related) -> `honors` list
```
K.C.M.G., G.C.M.G., C.M.G., K.C.B., C.B., K.B.E., O.B.E., M.B.E., C.B.E.,
G.B.E., D.S.O., M.C., V.D., E.D., T.D., Kt., Knt., K.C.V.O., C.V.O., M.V.O.
```

### Qualifications (Academic/professional) -> `qualifications` list
```
Medical: M.D., M.B., M.R.C.S., F.R.C.S., L.R.C.P., Ch.B., D.P.H., D.T.M.&H.
Academic: B.A., M.A., B.Sc., LL.D., Ph.D., LL.B., LL.M.
Engineering: R.E., C.E., M.I.C.E., A.M.I.C.E.
```

### Key Distinctions
- **K.C.** = King's Counsel -> `qualifications` (NOT honors)
- **M.C.** = Military Cross -> `honors`; **M.A.** = Master of Arts -> `qualifications`
- **Military rank** (Colonel, Major, Captain, etc.) before name -> `military_rank` field
- Include "(retd.)" or "R.N." in the name field as it appears

---

## 9. Colony-Specific Notes

### Jamaica
- **Largest colony**: Expect 100-400 officials depending on year
- **Parish system**: 14 parishes, each with Custos, Resident Magistrate, Clerk of Courts
- **Dependencies**: Cayman Islands section usually at end; Turks & Caicos Islands may appear
  within or as separate file
- **Morant Bay narrative**: 1867 file begins with extensive historical narrative about the
  1865 rebellion - skip to "CIVIL ESTABLISHMENT" section
- **1950 salary**: Uses GBP (£) throughout

### Trinidad and Tobago
- **Pre-1889**: Trinidad and Tobago are separate colonies with separate files
- **Warden system**: District wardens serve as local administrators with location-based titles
  (e.g., "Warden, Arima"); extract the location
- **Mixed currency**: Governor salary often in £; civil establishment in local $ from 1940s
- **Tobago section**: Appears at the end of the combined file. Extract Tobago's Warden and
  limited staff separately with department suffix "- Tobago"
- **Petroleum department**: Unique to Trinidad - Petroleum Technologist, Geologist

### Barbados
- **NOT a Crown Colony**: Retains elected House of Assembly with members by parish
- **House of Assembly members**: Extract with position and parish (location)
- **Compact colony**: Fewer officials than Jamaica or Trinidad (50-150)
- **Imperial Department of Agriculture**: Headquartered in Barbados (1910 era)
- **Dollar currency from 1949**: BWI$ 4.80 = £1; earlier files use GBP ("l.")
- **Notation**: `$2,880 x 144 = 4,032` means start $2,880, increment $144, max $4,032

### British Guiana
- **Complex constitution**: Court of Policy, College of Electors (pre-1928)
- **Three counties**: Demerara, Essequibo, Berbice - use as `region` field
- **Interior districts**: Mazaruni-Potaro, North West, Rupununi
- **Precise salaries**: Early era often has shillings and pence (e.g., "416l. 13s. 4d.")
- **Dollar currency**: BG$ used locally but Colonial Office List typically reports in £
- **Mining/forestry**: Significant departments for bauxite, gold, timber

### British Honduras
- **Very sparse** in early years: the 1867 file has only 21 lines of narrative, no civil
  establishment data
- **Small colony**: Expect 20-80 officials in most years
- **Later years**: Dollar currency (BH$)

### Bahamas and Bermuda
- **Representative government**: Both have elected assemblies
- **1867 Bermuda**: May appear within the Barbados file (the "Bermudas" section)
- **Small establishments**: 30-100 officials typically

### Small Island Colonies (Dominica, Antigua, St Vincent, St Lucia, Grenada, Montserrat, Nevis)
- **Dual listing**: These may appear both as standalone files AND within the Leeward/Windward
  Islands federated files - be aware of potential duplication
- **Very small**: Often 10-40 officials per island
- **Administrator or President**: Instead of "Governor" in many cases

---

## 10. Location Extraction

### Common Locations

**Jamaica**: Kingston, Spanish Town, Montego Bay, Falmouth, Port Antonio, Savanna-la-Mar
**Trinidad**: Port of Spain, San Fernando, Arima, Scarborough (Tobago)
**Barbados**: Bridgetown; most positions identified by parish name
**British Guiana**: Georgetown, New Amsterdam, Bartica, Mackenzie
**British Honduras**: Belize, Stann Creek, Orange Walk, Corozal, Cayo

### Extracting Location

1. **From position title**: `Police Magistrate, St. Michael` -> location: "St. Michael"
2. **From section header**: Under "San Fernando" sub-heading -> location: "San Fernando"
3. **From parenthetical**: `Resident Magistrate (Kingston)` -> location: "Kingston"
4. **From "at" preposition**: `Sub-Receiver at San Fernando` -> location: "San Fernando"
5. **From county context**: Under "Demerara" section -> region: "Demerara"

---

## 11. Validation Checklist

### All Years - Required Checks
- [ ] Officials list is non-empty
- [ ] Every entry has: name, canonical_name, surname, position, department
- [ ] Department names use "Department - Colony" format
- [ ] Salaries parsed correctly where present in source
- [ ] Honors and qualifications distinguished and placed in correct fields
- [ ] "Ditto" entries expanded to proper position names
- [ ] Multiple-person lines split into individual official records
- [ ] Acting/Temporary status captured in acting_status field
- [ ] K.C. treated as qualification, not honor

### Early Era (1867-1890s)
- [ ] Governor/Captain-General captured
- [ ] Colonial Secretary captured
- [ ] Salaries in "Xl." format parsed correctly
- [ ] Ecclesiastical officials included (Bishop, Archdeacon, Rectors)
- [ ] Shillings/pence values (e.g., "82l. 10s.") parsed - use pounds only for salary_min
- [ ] Barbados: House of Assembly members captured with parish locations
- [ ] British Guiana: Court of Policy members captured
- [ ] Historical narrative sections SKIPPED (only extract CIVIL ESTABLISHMENT data)

### Middle Era (1900-1930s)
- [ ] Salary ranges (e.g., "300l. to 400l.") captured as salary_min and salary_max
- [ ] Travelling allowances noted in allowances field
- [ ] Location-based positions (Wardens, Resident Magistrates) have location extracted
- [ ] Trinidad Warden districts identified
- [ ] Jamaica parish-based Resident Magistrates captured with parish locations

### Late Era (1940s-1960s)
- [ ] Currency correctly identified (£ vs $) per colony
- [ ] Salary scale notation parsed (e.g., "$2,880 x 144 = 4,032" or "£800-50-1,000")
- [ ] Duty allowances captured as separate numeric field
- [ ] Vacancies captured with salary data
- [ ] New departments (Civil Aviation, Labour, Statistics) captured
- [ ] Trinidad dollar amounts NOT confused with GBP

---

## Key Positions (Validation Targets)

**All colonies**: Governor/Administrator, Colonial Secretary, Chief Justice, Attorney-General, Treasurer/Financial Secretary

**Jamaica**: Collector-General, Director of Medical Services, Commissioner of Police, Resident Magistrates (by parish)

**Trinidad**: Wardens (by district), Petroleum Technologist (1940s+), Comptroller of Customs

**Barbados**: Speaker of the House of Assembly, Provost-Marshal, Director of Agriculture

**British Guiana**: Commissioner of Local Government, Commissioner of Interior, Transport and Harbours

---

## Sample Output

### 1867 Style (Early Era)
```python
# Jamaica - Governor with honors
{
    "name": "Sir John Peter Grant", "canonical_name": "Grant, Sir John Peter",
    "surname": "Grant", "position": "Captain-General and Governor-in-Chief",
    "department": "Civil Establishment - Jamaica",
    "salary_min": 7000, "salary_max": 7000, "salary_currency": "GBP",
    "honors": ["K.C.B."],
}
# Trinidad - Medical officer with shillings (use pounds only for salary_min)
{
    "name": "K. Finlay", "canonical_name": "Finlay, K.", "surname": "Finlay",
    "position": "Colonial Surgeon", "department": "Medical Department - Trinidad",
    "salary_min": 809, "salary_max": 809, "salary_currency": "GBP",
    "qualifications": ["M.D."],
}
```

### 1910 Style (Trinidad - With Location and Allowance)
```python
{
    "name": "C. Flanagin",
    "canonical_name": "Flanagin, C.",
    "given_names": "C.",
    "surname": "Flanagin",
    "position": "Warden",
    "department": "Administration - Trinidad and Tobago",
    "salary_min": 500,
    "salary_max": 500,
    "salary_currency": "GBP",
    "allowances": "75l. travelling allowance",
    "location": "Arima",
    "region": None,
}
```

### 1950 Style (Barbados - Dollar Currency, House of Assembly)
```python
# Dollar-salaried official
{
    "name": "A. W. L. Savage",
    "canonical_name": "Savage, A. W. L.",
    "surname": "Savage",
    "position": "Governor and Commander in Chief",
    "department": "Governor and Personal Staff - Barbados",
    "salary_min": 14400, "salary_max": 14400, "salary_currency": "BWI$",
    "duty_allowance": 4800, "honors": ["C.M.G."],
}
# House of Assembly member (no salary, parish as location)
{
    "name": "G. H. Adams",
    "canonical_name": "Adams, G. H.",
    "surname": "Adams",
    "position": "Member, House of Assembly",
    "department": "House of Assembly - Barbados",
    "qualifications": ["B.A."], "location": "St. Joseph",
}
```

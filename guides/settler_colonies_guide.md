# Settler Colonies - Colonial Office List Extraction Guide

## Overview

This guide provides instructions for extracting personnel data from the Settler Colonies group of the Colonial Office List (1867-1966). This is the **largest and most complex** colony group in the corpus, encompassing the British Dominions and their constituent provinces/states, as well as the Rhodesias. Files range from tiny (29 lines for Vancouver's Island) to very large (2,114 lines / 101KB for Dominion of Canada 1899).

**Target Model**: Gemini 3 Flash Preview (via API)

### Colonies in This Group

**Canada cluster:**
- Canada / Dominion of Canada (1867-1899)
- British Columbia (1867-1871), Vancouver's Island (1867)
- Nova Scotia (1867-1890s)
- New Brunswick (1867-1890s)
- Prince Edward Island (1867-1890s)
- Ontario (within Dominion file)
- Newfoundland (1867-1934, then 1949 onward as province)

**Australia cluster:**
- Australia / Commonwealth of Australia (1908-1927)
- New South Wales (1867-1927)
- Queensland (1867-1927)
- South Australia (1867-1927)
- Tasmania (1867-1927)
- Victoria (1867-1927)
- Western Australia (1867-1927)
- Northern Territory (within Australia file)

**New Zealand:**
- New Zealand (1867-1927)

**South Africa cluster:**
- Cape of Good Hope (1867-1927)
- Natal (1867-1912)
- Transvaal (1879-1880, 1905-1912)
- Orange River Colony (1905-1912)
- South Africa / Union of South Africa (1900-1922)
- Griqualand West (1877-1880)

**Rhodesia cluster:**
- Rhodesia / British South Africa Company (1900-1910)
- Southern Rhodesia (1922-1965)
- Northern Rhodesia (1922-1964)
- Federation of Rhodesia and Nyasaland (1954-1963)

---

## Historical Context & Administrative Evolution

### Key Dates and Transitions

| Date | Event | Impact on Files |
|------|-------|-----------------|
| 1867 | Canadian Confederation | Pre-1867: separate province files. Post-1867: `canada.txt` then `dominion_of_canada.txt` includes all provinces |
| 1871 | British Columbia joins Canada | BC file disappears from later years |
| 1893 | Natal gets responsible government | More ministers, fewer Imperial-appointed officers |
| 1895-1902 | Boer War period | Transvaal and Orange River Colony appear post-war |
| 1901 | Australian Federation | Individual state files continue but Commonwealth file added |
| 1907 | NZ becomes Dominion | Listed as "Dominion of New Zealand" |
| 1910 | Union of South Africa | Cape, Natal, Transvaal, ORC merge into Union file |
| 1923 | Southern Rhodesia gets responsible government | New colony file appears |
| 1924 | Northern Rhodesia becomes Crown Colony | Transferred from BSAC |
| 1927 | Last year for most Dominion listings | Canada, Australia, NZ, SA drop out of Colonial Office List |
| 1934 | Newfoundland loses Dominion status | Returns to Colonial Office List as Crown Colony |
| 1953 | Federation of Rhodesia and Nyasaland | New federal file alongside constituent territories |
| 1964 | Northern Rhodesia becomes Zambia | File disappears |
| 1965 | Rhodesia UDI | Southern Rhodesia entries cease |

### Critical Pattern: Dominions Drop Out

The self-governing Dominions (Canada, Australia, New Zealand, South Africa) are listed in the Colonial Office List only while they maintain a close enough administrative relationship with the Colonial Office. They typically disappear from the List by the late 1920s. However, Newfoundland returns after 1934 when it loses Dominion status and reverts to Crown Colony governance.

---

## Regional Divisions

### Canada (within Dominion of Canada files)

The Dominion of Canada file contains personnel for the federal government AND lists provinces. Key regions/provinces:

1. **Ontario** (Canada West pre-1867)
2. **Quebec** (Canada East / Lower Canada pre-1867)
3. **Nova Scotia**
4. **New Brunswick**
5. **Manitoba** (from 1870)
6. **British Columbia** (from 1871)
7. **Prince Edward Island** (from 1873)
8. **North-West Territories** (from 1875)
9. **Saskatchewan** (from 1905)
10. **Alberta** (from 1905)

Each province has its own Lieutenant-Governor, ministry, and legislature listed separately within the Dominion file.

### Australia (within Commonwealth and state files)

After Federation (1901), the Commonwealth file includes federal departments. State-level detail continues in separate files until the 1920s:

1. **New South Wales** (capital: Sydney)
2. **Victoria** (capital: Melbourne)
3. **Queensland** (capital: Brisbane)
4. **South Australia** (capital: Adelaide)
5. **Tasmania** (capital: Hobart)
6. **Western Australia** (capital: Perth)
7. **Northern Territory** (federal territory from 1911)
8. **Federal Capital Territory** (Canberra, from 1911)

### New Zealand

Provincial system abolished 1876. Key administrative regions:
- Auckland, Wellington, Canterbury, Otago (major centres)
- Districts administered by magistrates and commissioners

### South Africa

Pre-Union (before 1910):
1. **Cape of Good Hope** - Western Province and Eastern Province divisions
2. **Natal** - Counties: Durban, Victoria, Alexandra, Pietermaritzburg, Umvoti, Weenen, Klip River
3. **Transvaal** (after 1902)
4. **Orange River Colony** (after 1902)

Post-Union (1910): Single Union file with provincial administrations

### Rhodesia

1. **Mashonaland** (eastern, Salisbury)
2. **Matabeleland** (western, Bulawayo)
3. Native districts (32 in Southern Rhodesia)

---

## Data Schema

### Official Record Structure (20 fields, 5 required)

Refer to `guides/schema.py` for full definitions. The required fields are:

```python
{
    # REQUIRED
    "name": "Sir John A. Macdonald",          # Name as appears in source
    "canonical_name": "Macdonald, Sir John A.",# "Surname, Given Names"
    "surname": "Macdonald",                    # Family name
    "position": "Premier and President of Council", # Official title
    "department": "Privy Council - Canada",    # Department with colony suffix

    # OPTIONAL
    "given_names": "John A.",
    "salary_min": 7000,
    "salary_max": 7000,
    "salary_currency": "CAD",                  # IMPORTANT for settler colonies
    "salary_scale": None,
    "allowances": None,
    "duty_allowance": None,
    "expatriation_pay": None,
    "per_diem": None,
    "acting_status": None,
    "honors": ["K.C.M.G.", "Q.C."],
    "qualifications": [],
    "military_rank": None,
    "location": "Ottawa",
    "region": "Ontario",
}
```

### Critical: Currency Handling

Unlike Crown Colonies (which use GBP), settler colonies use **multiple currencies**:

| Colony | Currency | Symbol | salary_currency |
|--------|----------|--------|-----------------|
| Canada (federal) | Canadian Dollar | $ | `"CAD"` |
| Canadian provinces | Canadian Dollar | $ | `"CAD"` |
| Australia (Commonwealth) | Australian Pound | l. or £ | `"GBP"` (pre-1966) |
| Australian states | Australian Pound | l. or £ | `"GBP"` |
| New Zealand | NZ Pound | l. or £ | `"GBP"` |
| Cape of Good Hope | Cape Pound | l. or £ | `"GBP"` |
| Natal | Sterling | l. or £ | `"GBP"` |
| Newfoundland | NF Dollar | $ | `"CAD"` |
| Southern Rhodesia | Rhodesian Pound | L. or £ | `"GBP"` |

**Rule**: When salary is given in dollars ($), set `salary_currency` to `"CAD"` (for Canadian/Newfoundland) or note the local dollar. When given in pounds (l. or £), set to `"GBP"`.

---

## Department List by Era

### Canada (1867): Departments within Federal Government

From the 1867 source file:
- Cabinet
- Civil Establishment (Governor-General's Office)
- Finance Minister's Department
- Customs Department
- Public Works
- General Post-Office
- Crown Law Department
- Crown Lands
- Bureau of Agriculture and Statistics
- Militia Department
- Geological Department
- Legislature (Senate and House of Commons)
- Judicial and Legal Departments, Canada East
- Judicial and Legal Department, Canada West
- Ecclesiastical Establishment

### Canada (1896): Expanded Federal Structure

From the 1896 source file:
- Governor-General's Office
- Queen's Privy Council for Canada
- Treasury Board
- Supreme Court of Canada
- Court of Exchequer of Canada
- Senate of Canada
- House of Commons
- Department of the Secretary of State
- Department of Public Printing and Stationery
- Department of the Interior
- Department of Geological Survey
- Finance Department
- Audit Office
- Department of Public Works
- Department of Trade and Commerce
- Department of Inland Revenue
- Department of Customs
- Railways and Canals
- Post Office Department
- Department of Justice
- Mounted Police Office
- Department of Agriculture and Statistics
- Department of Marine and Fisheries
- Department of Militia and Defence
- Department of Indian Affairs
- High Commissioner in London
- Ecclesiastical (Church of England, Roman Catholic, Presbyterian, Methodist)

### Australia (1927): Commonwealth Departments

From the 1927 source file:
- Governor-General's Staff
- Prime Minister's Department (External Affairs, High Commissioner, Nauru)
- Treasury (Taxation, Pensions, Commonwealth Bank)
- Attorney-General's Department (High Court, Arbitration, Patents)
- Department of Defence (Navy, Army, Air)
- Department of Trade and Customs
- Department of Health
- Department of Home and Territories
- Department of Markets and Migration
- Department of Works and Railways
- Postmaster-General's Department

### New Zealand (1867): Early Colonial Structure

- Cabinet Ministers
- Executive Council
- Legislative Council
- House of Representatives
- Civil Establishment (Governor, Secretary, Treasurer)
- Native Department
- Crown Lands Department
- Customs
- Judicial Establishment
- Resident Magistrates (extensive list by district)
- Provincial Governments (9 provinces with Superintendents)

### Natal (1896): Responsible Government Structure

- Executive Council
- Legislative Council (by county)
- Legislative Assembly (by constituency)
- Civil Establishment (Governor's Office)
- Colonial Secretary's Office
- Attorney-General's Office
- Registrar of Deeds
- Treasury
- Audit Office
- Native Office
- Lands and Works
- Railways
- Harbour Department

### Southern Rhodesia (1927): Post-Self-Government

- Governor's Office
- Executive Council
- Members of the Ministry
- Legislative Assembly (by electoral district)
- Division of the Premier (Native Commissioner's Dept)
- Division of the Treasurer (Post, Customs, Taxes, Audit)
- Division of Minister of Agriculture and Lands
- Division of the Colonial Secretary
- Division of Attorney-General
- Division of Minister of Mines and Public Works

---

## Salary Format Patterns with Real Examples

### Canadian Dollar Notation (Canada, Newfoundland)

```
Simple:      $7,000                → salary_min: 7000, salary_max: 7000, salary_currency: "CAD"
Simple:      $2,400                → salary_min: 2400, salary_max: 2400
With comma:  $10,000               → salary_min: 10000, salary_max: 10000
Low salary:  $400                  → salary_min: 400, salary_max: 400
Per diem:    $4 per day when on duty → per_diem: "$4"
```

Real examples from Canada 1896:
```
Chief Justice of Canada, Sir S. H. Strong, $8,000.
→ salary_min: 8000, salary_currency: "CAD"

Puise Judges:—Hon. T. Fournier, LL.D., ... $7,000 each.
→ salary_min: 7000, salary_currency: "CAD"

Chief Clerk in Governor-General's Secretary's Office, Chas. J. Jonos, $2,400.
→ salary_min: 2400, salary_currency: "CAD"

Examiners, Captains G. A. Mackenzie, ... each $4 per day when on duty.
→ per_diem: "$4", salary_currency: "CAD"
```

Real examples from Newfoundland 1927:
```
Governor, ... Sir William Lamond Allardyce, K.C.M.G., $12,500 and allowance of $2,500 for travelling expenses.
→ salary_min: 12500, allowances: "$2,500 for travelling expenses", salary_currency: "CAD"

Clerk of the House of Assembly, H. Y. Mott, $2,000.
→ salary_min: 2000, salary_currency: "CAD"
```

### British Pound Notation (Australia, NZ, Cape, Natal, Rhodesia)

```
Early "l.":  4,000l.              → salary_min: 4000, salary_max: 4000, salary_currency: "GBP"
With allow:  5,000l., House allowance of 500l., and 1,000l. as High Commissioner
             → salary_min: 5000, allowances: "House allowance of 500l., and 1,000l. as High Commissioner"
Range:       350l. to 400l.       → salary_min: 350, salary_max: 400
Per diem:    30s. a day           → per_diem: "30s."
With pence:  247l. 8s. 6d.       → salary_min: 247
```

Real examples from Cape of Good Hope 1867:
```
Governor, Sir P. E. Wodehouse, K.C.B., 5,000l., House allowance of 500l., and 1,000l. as High Commissioner.
→ salary_min: 5000, allowances: "House allowance of 500l., and 1,000l. as High Commissioner"

Chief Justice, Sir W. Hodges, Kt., 2,000l.
→ salary_min: 2000

Commandant, Sir W. Currie, Kt., 30s. a day and travelling allowance.
→ per_diem: "30s.", allowances: "travelling allowance"

Paymaster, W. L. Hutchinson, 1l. a day.
→ per_diem: "1l."
```

Real examples from New Zealand 1867:
```
Governor and Commander-in-Chief, Sir G. Grey, K.C.B., 4,500l.
→ salary_min: 4500

Puisne Judge, Wellington, A. J. Johnston, 1500l.
→ salary_min: 1500, location: "Wellington"

Superintendent of Assay, F. Claudet, 500l.
→ salary_min: 500
```

### Australian Pound Notation (1927 Commonwealth)

```
Simple:      10,000l.             → salary_min: 10000, salary_currency: "GBP"
With allow:  1,000l., and 500l. allowance → salary_min: 1000, allowances: "500l. allowance"
Composite:   as State Printer, 900l., and allowance from Commonwealth Government 150l.
             → salary_min: 900, allowances: "150l. from Commonwealth Government"
```

Real examples from Australia 1927:
```
Governor-General ... Baron Stonehaven, P.C., G.C.M.G., D.S.O., ... 10,000l.
→ salary_min: 10000

Secretary to Prime Minister's Department, P. E. Deane, C.M.G., 1,300l.
→ salary_min: 1300

Commissioner of Taxation, R. Ewing, 1,250l., and 250l. allowance.
→ salary_min: 1250, allowances: "250l. allowance"
```

### Rhodesian Pound Notation (Southern Rhodesia)

```
With allow:  4,000L., 1,000L. personal allowance and 1,000L. entertainment allowance
             → salary_min: 4000, allowances: "1,000L. personal allowance and 1,000L. entertainment allowance"
```

Real example from Southern Rhodesia 1927:
```
Governor, Lieut.-Colonel Sir John R. Chancellor, G.C.M.G., G.C.V.O., D.S.O., R.E., 4,000L., 1,000L. personal allowance and 1,000L. entertainment allowance.
→ salary_min: 4000, allowances: "1,000L. personal allowance and 1,000L. entertainment allowance"
```

---

## Special Patterns

### "Ditto" References

Present in both early and mid-period files. Expand to the preceding position type.

From Canada 1867:
```
1st Clerk in Secretary's Office, H. Cotton, 402l.
2nd ditto, Captain J. Kidd, 336l.        → position: "2nd Clerk in Secretary's Office"
3rd ditto, F. D. Burrowes, 125l.         → position: "3rd Clerk in Secretary's Office"
```

From Canada 1867:
```
Deputy Provincial Registrar, Wm. Kent.
Senior Clerk, G. H. Lane, 450l.
...
Receiver-General, Sir N. J. Belleau, Kt., 1,250l.
Deputy ditto, T. D. Harrington, 600l.    → position: "Deputy Receiver-General"
```

From Cape 1867:
```
Collector of Customs, Quebec, J. W. Duncombe, 800l.
Ditto, Montreal, A. M. Delisle, 800l.    → position: "Collector of Customs", location: "Montreal"
```

### "Each" Salary Pattern (Multiple People, Same Salary)

From Canada 1896:
```
Puise Judges:—Hon. T. Fournier, LL.D., Hon. Henri E. Taschereau, Hon. J. W. Gwynne, Hon. Robert Sedgwick, LL.D., Hon. G. E. King, $7,000 each.
```
Creates FIVE officials, each with salary_min: 7000.

From Cape 1867:
```
Puisne Judges, Queen's Bench:—
R. E. Caron, T. C. Aylwyn, W. Badgley, L. T. Drummond, 1,000l. each.
```
Creates FOUR officials, each with salary_min: 1000.

### Per Diem Notation

From Cape 1867:
```
Commandant, Sir W. Currie, Kt., 30s. a day and travelling allowance.
→ per_diem: "30s.", allowances: "travelling allowance"

Inspectors, W. T. Gillfillan, I. H. Bowker, H. Bertram, 20s. a day each
→ Creates THREE officials, each with per_diem: "20s."

Sub-Inspectors, F. Jacobs, J. Surmon, ... 13s. a day each.
→ Creates MULTIPLE officials, each with per_diem: "13s."
```

### Acting/Temporary Status

From Cape 1867:
```
Clerk of Works, J. Flack, 400l.
Acting Registrar, C. E. Pooley, 400l.     → acting_status: "Acting"
```

From Canada 1867:
```
Acting Governor, Sir John Michel.           → acting_status: "Acting"
```

From Southern Rhodesia 1927:
```
Chief Clerk, C. F. Cranswick (acting).     → acting_status: "Acting"
Acting Chief Chemist, A. W. Facer, B.A.   → acting_status: "Acting"
```

### Ministers and Legislators

**Important Decision**: Settler colony files contain extensive lists of:
1. **Cabinet Ministers** - EXTRACT (they hold government positions)
2. **Senators / Legislative Councillors** - EXTRACT (they hold named positions)
3. **Members of Parliament / House of Assembly** - EXTRACT (they represent constituencies)
4. **Constituency lists without salary** - EXTRACT with salary as None

For legislators, set the department based on the chamber:
- `"Senate - Canada"`, `"House of Commons - Canada"`
- `"Legislative Council - Natal"`, `"Legislative Assembly - Natal"`
- `"House of Representatives - New Zealand"`
- `"Legislative Assembly - Southern Rhodesia"`

### Multiple Roles for One Person

Common in settler colonies where a minister holds several portfolios:

From Natal 1896:
```
The Hon. Sir John Robinson, K.C.M.G., M.L.A., Prime Minister, Colonial Secretary, and Minister of Education.
```
Create ONE official entry with the composite position: "Prime Minister, Colonial Secretary, and Minister of Education"

From Canada 1896:
```
Hon. Sir Mackenzie Bowell, K.C.M.G., Q.C., Premier and President of Council.
```
Create ONE entry with position: "Premier and President of Council"

### Post-nominal Abbreviations Specific to Settler Colonies

```
Q.C. = Queen's Counsel (qualification, NOT honor) → qualifications: ["Q.C."]
K.C. = King's Counsel (qualification) → qualifications: ["K.C."]
M.L.A. = Member of Legislative Assembly → NOTE in position context, not an honor
M.L.C. = Member of Legislative Council → NOTE in position context
M.P. = Member of Parliament → NOTE in position context
J.P. = Justice of the Peace → qualifications: ["J.P."]
I.S.O. = Imperial Service Order → honors: ["I.S.O."]
```

### Unnamed Groups

From British Columbia 1867:
```
Three Constables at 144l. each.
→ SKIP (no names to extract)

Two Gaolers at 144l. each, E. Daubney and Crawford
→ Extract the two NAMED individuals: E. Daubney and Crawford, each with salary_min: 144
```

### Vacant Positions

From Canada 1867:
```
Vacant, Solicitor-General of Lower Canada.
→ SKIP (no person to extract)
```

From British Columbia 1867:
```
Puisne Judge, (vacant), 800l.
→ SKIP in early era (no name)
```

---

## Location/Region Extraction Rules

### Location in Position Title

From New Zealand 1867:
```
Collector of Customs, Auckland, W. Young, 500l.
→ position: "Collector of Customs", location: "Auckland"

District Commissioners, Bay Islands, Henry Tacy Kemp.
→ position: "District Commissioner", location: "Bay Islands"

Resident Magistrate, Wellington, C. D. R. Ward.
→ position: "Resident Magistrate", location: "Wellington"
```

From Cape 1867:
```
Sub-Collector, Port Elizabeth, G. W. Browning, 750l.
→ position: "Sub-Collector", location: "Port Elizabeth"

Civil Commissioner and Resident Magistrate, John Montgomery Hill, 700l.
→ position: "Civil Commissioner and Resident Magistrate", location: "Cape Division" (from section header)
```

### Location from Section Headers

From Cape 1867, the file uses division headers:
```
Division of Stellenbosch.
Civil Commissioner and Resident Magistrate, D. J. van Ryneveld, 600l.
→ location: "Stellenbosch"

Division of Port Elizabeth.
Civil Commissioner and Resident Magistrate, John Campbell, 600l.
→ location: "Port Elizabeth"
```

### Region from Province/State Context

For Canada:
```
Attorney-General, Upper Canada, J. A. Macdonald, 1,250l.
→ region: "Ontario" (Upper Canada = Ontario post-1867)

Attorney-General, Lower Canada, G. E. Cartier, 1,250l.
→ region: "Quebec" (Lower Canada = Quebec post-1867)
```

For Australia (1927), the state-level sections set the region:
```
NEW SOUTH WALES section:
Governor, Lt.-Gen. Sir T. H. J. C. Goodman, ...
→ region: "New South Wales"
```

For Southern Rhodesia:
```
Native Commissioners - Mashonaland:
Bikita, H. N Watters
→ region: "Mashonaland", location: "Bikita"

Native Commissioners - Matabeleland:
Belingwe, C. Bullock
→ region: "Matabeleland", location: "Belingwe"
```

### Common Locations

**Canada**: Ottawa, Quebec, Montreal, Toronto, Halifax, Kingston, Winnipeg, Victoria (BC), Charlottetown

**New Zealand**: Auckland, Wellington, Christchurch, Dunedin, Nelson, New Plymouth, Napier, Invercargill, Hokianga, Lyttelton, Otago, Taranaki, Canterbury

**Cape of Good Hope**: Cape Town, Grahamstown, King William's Town, Port Elizabeth, Stellenbosch, East London, Simon's Bay, Mossel Bay, Knysna, Oudtshoorn

**Natal**: Pietermaritzburg, Durban, Ladysmith, Newcastle, Verulam

**Southern Rhodesia**: Salisbury, Bulawayo, Umtali, Gwelo, Gatooma, Victoria, Mazoe, Hartley

---

## Era-Specific Extraction Notes

### 1867-1875 (Pre-Federation/Early Colonial)

- **Canada**: Still transitioning to Dominion. File called `canada.txt`. Upper/Lower Canada divisions.
- **New Zealand**: Provincial system still in place (9 superintendents). Extensive magistrate lists.
- **Cape**: Enormous file with 800+ lines. Division-by-division civil commissioner lists.
- **British Columbia**: Separate colony file with Gold Commissioner structure.
- **Vancouver's Island**: Tiny file, merged with BC in 1866.
- **Salaries**: In pounds (l.) for NZ, Cape, BC. Canadian file uses pounds.
- **Expected officials**: Canada 50-100, NZ 200+, Cape 300+, BC 50-80

### 1876-1900 (Consolidation)

- **Canada**: Now `dominion_of_canada.txt`. Massive files with federal departments + provincial listings + full constituency lists for House of Commons.
- **New Zealand**: Provincial system abolished 1876. More centralized departments.
- **Cape**: Increasingly large files. Note responsible government evolving.
- **Natal**: Gets responsible government 1893. Ministers replace Imperial officers.
- **Salaries**: Canada uses **dollars ($)**. Others use pounds (l.).
- **Expected officials**: Canada 500+, NZ 100-300, Cape 400+, Natal 100-200

### 1901-1927 (Federation/Union Era)

- **Australia**: Commonwealth file appears alongside state files. Commonwealth uses departments modeled on British system. Very large combined files.
- **New Zealand**: Now styled "Dominion of New Zealand."
- **South Africa**: Union formed 1910. Pre-Union: separate Cape, Natal, Transvaal, ORC files. Post-Union: single file.
- **Southern Rhodesia**: Self-governing from 1923 with ministerial divisions.
- **Salaries**: Dollars for Canada/Newfoundland; pounds for rest.
- **Expected officials**: Australia 1927 file has 800+ officials across Commonwealth and states.

### 1927-1934 (Dominions Exit)

- Canada, Australia, NZ, SA disappear from Colonial Office List by late 1920s.
- Newfoundland remains (loses Dominion status 1934).
- Rhodesias continue to appear.

### 1934-1966 (Late Colonial)

- **Newfoundland**: Returns as Crown Colony 1934-1949 (joins Canada). Format similar to other Crown Colonies.
- **Northern Rhodesia**: Crown Colony format with salary scales.
- **Southern Rhodesia**: Self-governing colony, not Crown Colony.
- **Federation of Rhodesia and Nyasaland**: 1953-1963.
- **Salaries**: May use salary scales for Northern Rhodesia (Crown Colony pattern).
- **Expected officials**: Northern Rhodesia 200-400, Southern Rhodesia varies.

---

## Handling the Very Large Files

### Challenge: Files Up to 2,114 Lines (101KB)

The Dominion of Canada and Commonwealth of Australia files are exceptionally large. They contain:

1. **Extensive narrative history** (often 200-600 lines of pure text before any personnel data)
2. **Statistical tables** (revenue, population, trade)
3. **Bank and railway listings** (non-personnel data)
4. **Full constituency lists** with all MPs (can be 200+ entries with no salary)
5. **Ecclesiastical lists** (bishops, archbishops)

### Extraction Strategy for Large Files

1. **Skip narrative sections**: Everything before the first "Civil Establishment", "Executive Council", "Cabinet", or "Governors-General" heading is context, not personnel data.
2. **Skip statistical tables**: Revenue, expenditure, population, trade tables have no personnel.
3. **Skip bank listings**: Lists of banks are not personnel.
4. **Extract legislators**: Even when no salary is listed, extract MPs/Senators with their constituency as location.
5. **Extract ecclesiastical**: Bishops and archbishops should be extracted with appropriate department.

### Section Markers to Look For

```
Civil Establishment
Executive Council
Cabinet
Cabinet Ministers
Privy Council
Senate
House of Commons
House of Representatives
Legislative Council
Legislative Assembly
House of Assembly
DEPARTMENT OF ...
Department of ...
Division of ...
Judicial Establishment
Ecclesiastical
```

---

## Validation Checklist

### All Years - General

- [ ] Officials list is non-empty
- [ ] All entries have name, canonical_name, surname, position, department
- [ ] Salaries parsed where present (with correct currency)
- [ ] Honors and qualifications separated correctly (Q.C. is qualification, C.M.G. is honor)
- [ ] "Ditto" entries expanded to proper position names
- [ ] Acting status captured

### Canada Files

- [ ] Governor-General captured (or Administrator in early years)
- [ ] Premier / Prime Minister captured
- [ ] All Cabinet ministers captured
- [ ] Senate Speaker and key officers captured
- [ ] House of Commons Speaker captured
- [ ] Department heads captured with dollar salaries
- [ ] High Commissioner in London captured
- [ ] Provincial Lieutenant-Governors captured (post-1867)
- [ ] Currency set to CAD for dollar amounts

### Australian Files

- [ ] Governor-General captured (post-1901)
- [ ] State Governors captured
- [ ] Commonwealth department heads captured
- [ ] High Court justices captured
- [ ] High Commissioner captured
- [ ] State-level officials captured where present

### New Zealand

- [ ] Governor captured
- [ ] Premier captured
- [ ] Cabinet ministers captured
- [ ] Provincial Superintendents captured (pre-1876)
- [ ] Chief Justice and judges captured
- [ ] Resident Magistrates captured with locations

### Cape of Good Hope

- [ ] Governor captured with allowances
- [ ] Colonial Secretary captured
- [ ] All divisional Civil Commissioners captured
- [ ] Port officials captured
- [ ] Judicial establishment captured
- [ ] Ecclesiastical establishment captured

### Natal

- [ ] Governor captured
- [ ] All ministers captured
- [ ] Legislative Council members captured by county
- [ ] Legislative Assembly members captured by constituency
- [ ] Department heads captured (Railway, Native Affairs, etc.)

### Southern Rhodesia

- [ ] Governor captured
- [ ] All ministers captured
- [ ] Legislative Assembly members captured by electoral district
- [ ] Native Commissioners captured by district (Mashonaland/Matabeleland)
- [ ] Department heads captured within ministerial divisions

### Rhodesia - Northern

- [ ] Governor captured
- [ ] Provincial Commissioners captured
- [ ] District officers captured
- [ ] Expected format similar to Crown Colony (with salary scales in later years)

---

## Key Positions by Era

### Canada (1867)
1. Governor-General
2. Provincial A.D.C.s
3. Provincial Secretary
4. Finance Minister
5. Commissioner of Crown Lands
6. Postmaster-General
7. Attorney-General (Upper and Lower Canada)
8. Chief Justice (Queen's Bench, Common Pleas)

### Canada (1896 Dominion)
1. Governor-General
2. Premier and President of Council
3. Secretary of State
4. Minister of Finance
5. Minister of Justice and Attorney-General
6. Postmaster-General
7. Minister of Militia and Defence
8. Minister of the Interior
9. Chief Justice of Canada (Supreme Court)
10. High Commissioner in London

### Australia (1927)
1. Governor-General
2. Prime Minister (via Department Secretary)
3. High Commissioner in London
4. Solicitor-General
5. Chief Justice (High Court)
6. Auditor-General
7. Secretary to Treasury
8. State Governors (6)

### New Zealand (1867)
1. Governor and Commander-in-Chief
2. Colonial Secretary and Premier
3. Colonial Treasurer
4. Attorney-General
5. Commissioner of Customs
6. Chief Justice
7. Provincial Superintendents (9)

### Natal (1896)
1. Governor
2. Prime Minister / Colonial Secretary
3. Attorney-General
4. Treasurer
5. Secretary for Native Affairs
6. Minister of Lands and Works
7. General Manager, Railways

### Southern Rhodesia (1927)
1. Governor
2. Premier
3. Colonial Secretary
4. Treasurer
5. Attorney-General
6. Minister of Mines and Public Works
7. Minister of Agriculture and Lands
8. Chief Native Commissioner

---

## Sample Output

### Canada 1867 Style

```python
{
    "name": "Viscount Monck",
    "canonical_name": "Monck, Viscount",
    "given_names": None,
    "surname": "Monck",
    "position": "Governor-General",
    "department": "Civil Establishment - Canada",
    "salary_min": 7000,
    "salary_max": 7000,
    "salary_currency": "GBP",
    "location": None,
    "region": None,
}
```

### Canada 1896 Style (Dollar Salary)

```python
{
    "name": "Sir S. H. Strong",
    "canonical_name": "Strong, Sir S. H.",
    "given_names": "S. H.",
    "surname": "Strong",
    "position": "Chief Justice of Canada",
    "department": "Supreme Court of Canada - Canada",
    "salary_min": 8000,
    "salary_max": 8000,
    "salary_currency": "CAD",
    "honors": [],
    "location": "Ottawa",
    "region": None,
}
```

### New Zealand 1867 Style

```python
{
    "name": "Sir G. Grey",
    "canonical_name": "Grey, Sir G.",
    "given_names": "G.",
    "surname": "Grey",
    "position": "Governor and Commander-in-Chief",
    "department": "Civil Establishment - New Zealand",
    "salary_min": 4500,
    "salary_max": 4500,
    "salary_currency": "GBP",
    "honors": ["K.C.B."],
    "location": None,
    "region": None,
}
```

### Cape of Good Hope 1867 Style (Division Officer)

```python
{
    "name": "D. J. van Ryneveld",
    "canonical_name": "van Ryneveld, D. J.",
    "given_names": "D. J.",
    "surname": "van Ryneveld",
    "position": "Civil Commissioner and Resident Magistrate",
    "department": "Civil Establishment - Cape of Good Hope",
    "salary_min": 600,
    "salary_max": 600,
    "salary_currency": "GBP",
    "location": "Stellenbosch",
    "region": None,
}
```

### Natal 1896 Style (Minister)

```python
{
    "name": "The Hon. Sir John Robinson",
    "canonical_name": "Robinson, Sir John",
    "given_names": "John",
    "surname": "Robinson",
    "position": "Prime Minister, Colonial Secretary, and Minister of Education",
    "department": "Executive Council - Natal",
    "salary_min": 1000,
    "salary_max": 1000,
    "salary_currency": "GBP",
    "honors": ["K.C.M.G."],
    "location": "Pietermaritzburg",
    "region": None,
}
```

### Southern Rhodesia 1927 Style (Native Commissioner)

```python
{
    "name": "H. N Watters",
    "canonical_name": "Watters, H. N",
    "given_names": "H. N",
    "surname": "Watters",
    "position": "Native Commissioner",
    "department": "Chief Native Commissioner's Department - Southern Rhodesia",
    "salary_min": None,
    "salary_max": None,
    "salary_currency": "GBP",
    "location": "Bikita",
    "region": "Mashonaland",
}
```

### Australia 1927 Style (Commonwealth Official)

```python
{
    "name": "P. E. Deane",
    "canonical_name": "Deane, P. E.",
    "given_names": "P. E.",
    "surname": "Deane",
    "position": "Secretary to Prime Minister's Department",
    "department": "Prime Minister's Department - Australia",
    "salary_min": 1300,
    "salary_max": 1300,
    "salary_currency": "GBP",
    "honors": ["C.M.G."],
    "location": None,
    "region": None,
}
```

### Newfoundland 1927 Style (Dollar Salary)

```python
{
    "name": "Sir William Lamond Allardyce",
    "canonical_name": "Allardyce, Sir William Lamond",
    "given_names": "William Lamond",
    "surname": "Allardyce",
    "position": "Governor, Commander-in-Chief, and Vice-Admiral",
    "department": "Civil Establishment - Newfoundland",
    "salary_min": 12500,
    "salary_max": 12500,
    "salary_currency": "CAD",
    "allowances": "$2,500 for travelling expenses",
    "honors": ["K.C.M.G."],
    "location": "St. John's",
    "region": None,
}
```

### Legislator Without Salary

```python
{
    "name": "Hon. David Reesor",
    "canonical_name": "Reesor, David",
    "given_names": "David",
    "surname": "Reesor",
    "position": "Senator",
    "department": "Senate - Canada",
    "salary_min": None,
    "salary_max": None,
    "salary_currency": "CAD",
    "location": None,
    "region": None,
}
```

# Pacific Colony Group - Colonial Office List Extraction Guide

## Overview

This guide provides instructions for extracting personnel data from Pacific colony group Colonial Office List files (1877-1966). The Pacific group encompasses British territories scattered across the vast Pacific Ocean, ranging from the Crown Colony of Fiji to tiny protectorates and mandated territories. The administrative hub was at Suva, Fiji, with the Governor of Fiji also serving as High Commissioner for the Western Pacific until 1952.

**Target Model**: Gemini 3 Flash Preview (via API)

---

## Source Files

### Available Colonies and Approximate Coverage

| Colony | Approx. Years | File Names |
|--------|--------------|------------|
| Fiji | 1877-1966 | `FIJI.txt`, `fiji.txt`, `FIJI.md`, `fiji.md`, `FIJI_AND_PITCAIRN.txt`, `fiji_and_pitcairn_islands.txt` |
| Western Pacific (High Commission) | 1890-1958 | `WESTERN_PACIFIC.txt`, `western_pacific.txt`, `WESTERN_PACIFIC.md`, `western_pacific.md`, `WESTERN_PACIFIC_HIGH_COMMISSION.txt`, `western_pacific_high_commission.txt` |
| British New Guinea / Papua | 1889-1917 | `BRITISH_NEW_GUINEA.txt`, `british_new_guinea.txt`, `BRITISH_NEW_GUINEA.md`, `PAPUA.md`, `papua.txt`, `papua.md` |
| Territory of New Guinea | 1925+ | `THE_TERRITORY_OF_NEW_GUINEA.txt` |
| Gilbert and Ellice Islands | 1924-1957 | `GILBERT_AND_ELLICE_ISLANDS.md`, `THE_GILBERT_AND_ELLICE_ISLANDS_COLONY.txt`, `gilbert_and_ellice_islands.txt` |
| British Solomon Islands | 1933-1957 | `THE_BRITISH_SOLOMON_ISLANDS_PROTECTORATE.txt` |
| Tonga | 1931-1958 | `TONGA.txt`, `tonga.txt`, `KINGDOM_OF_TONGA.txt` |
| Norfolk Island | 1890-1917 | `NORFOLK_ISLAND.md`, `norfolk_island.txt`, `NORFOLK_ISLAND.txt` |
| New Hebrides (Condominium) | embedded in Western Pacific files |
| Pitcairn Island | embedded in Western Pacific or Fiji files |
| Cook Islands | 1911+ | `cook_islands.txt` |
| Nauru | 1925+ | `NAURU.txt` |
| Lord Howe Island | 1905-1907 | `LORD_HOWE_ISLAND.md` |

**IMPORTANT**: Many smaller territories (Tonga, Solomon Islands, Gilbert & Ellice, New Hebrides, Pitcairn) appear as sections WITHIN the Western Pacific High Commission file, not as standalone files. Always check both standalone and embedded locations.

---

## Historical Context & Administrative Evolution

### Key Administrative Changes

| Era | Characteristics |
|-----|----------------|
| 1874 | Fiji ceded to Britain; becomes Crown Colony |
| 1877 | Western Pacific High Commission created by Order in Council; High Commissioner based at Suva |
| 1884 | British New Guinea Protectorate proclaimed |
| 1888 | British New Guinea annexed; Cook Islands declared under British protection |
| 1892 | Gilbert and Ellice Islands placed under British Protectorate |
| 1893 | Pacific Order in Council extends High Commissioner jurisdiction to foreigners and natives |
| 1896 | British Solomon Islands Protectorate established |
| 1900 | Tonga becomes British Protected State by Treaty of Friendship |
| 1906 | British New Guinea renamed "Papua"; transferred to Australian administration |
| 1906-07 | Anglo-French Condominium established over New Hebrides |
| 1914 | Australian forces occupy German New Guinea |
| 1915-16 | Gilbert and Ellice Islands become a Colony (from Protectorate) |
| 1920 | League of Nations Mandate: Territory of New Guinea to Australia |
| 1922 | New Hebrides Protocol ratified, replacing 1906 Convention |
| 1952 | Offices of Governor of Fiji and High Commissioner for the Western Pacific SEPARATED; Tonga and Pitcairn transferred to Governor of Fiji |
| 1953 | Western Pacific High Commission headquarters moved from Suva to Honiara, British Solomon Islands |
| 1970 | Fiji independence |

### The Dual-Hat Arrangement (1877-1952)

The Governor of Fiji simultaneously served as High Commissioner for the Western Pacific. Personnel records reflect this:
- The Governor receives separate salaries for each role
- The Chief Justice of Fiji also serves as Judicial Commissioner for the Western Pacific
- Audit, legal and other officers may draw dual salaries from Fiji and High Commission funds
- Department suffixes should reflect which capacity: "Civil Establishment - Fiji" vs "High Commission - Western Pacific"

After 1952, these are separate offices and should be treated as distinct entities.

### Papua / British New Guinea Transition

- 1884-1906: "British New Guinea" - administered via Queensland, Australia
- 1906: Renamed "Papua" (Territory of Papua), transferred to Australian Commonwealth
- From 1906 onward, Papua gradually disappears from Colonial Office Lists as it becomes an Australian domestic matter
- "Territory of New Guinea" (formerly German) appears from ~1921 as an Australian Mandate

---

## Regional Divisions

The Pacific group has a hierarchical structure:

### Fiji (Crown Colony)
- Standalone colony with its own Governor, councils, and full administrative apparatus
- Islands: Viti Levu (capital Suva), Vanua Levu, Taveuni, Kadavu, Ovalau (old capital Levuka)
- Dependency: Rotuma (from 1881)
- After 1952: also administers Pitcairn Islands

### Western Pacific High Commission
Umbrella jurisdiction over:
1. **Gilbert and Ellice Islands Colony** (from 1916; Protectorate before that)
   - Headquarters: Ocean Island, then Tarawa
   - Includes Phoenix Islands, Northern Line Islands, Christmas Island, Fanning Island
2. **British Solomon Islands Protectorate**
   - Headquarters: Tulagi, then Honiara (post-WWII)
3. **Tonga** (Protected State, largely self-governing) - transferred to Fiji 1952
4. **New Hebrides** (Anglo-French Condominium)
   - British staff, French staff, and Joint Services staff
5. **Central and Southern Line Islands**
6. **Pitcairn Island** - transferred to Fiji 1952
7. **Phoenix Group**

---

## Data Schema

### Official Record Structure

Refer to `guides/schema.py` for complete field definitions. The 20 fields are:

**REQUIRED (5 fields)**:
- `name` - Name as appears in source
- `canonical_name` - "Surname, Given Names" format
- `surname` - Family name
- `position` - Official title/role
- `department` - Department with colony suffix

**OPTIONAL (15 fields)**:
- `given_names`, `salary_min`, `salary_max`, `salary_currency`, `salary_scale`, `allowances`, `duty_allowance`, `expatriation_pay`, `per_diem`, `acting_status`, `honors` (list), `qualifications` (list), `military_rank`, `location`, `region`

### Department Naming Convention

Use the pattern: `"Department Name - Colony Name"`

For Fiji:
```
"Civil Establishment - Fiji"
"Colonial Secretary's Department - Fiji"
"Medical Department - Fiji"
```

For Western Pacific High Commission:
```
"High Commission - Western Pacific"
```

For sub-territories under the WPHC:
```
"Civil Establishment - Gilbert and Ellice Islands"
"District Administration - British Solomon Islands"
"British National Administration - New Hebrides"
"French National Administration - New Hebrides"
"Joint Services - New Hebrides"
```

For Tonga (which is a protected state, not a colony):
```
"Ministers - Tonga"
"British Agent and Consul - Tonga"
```

For Territory of New Guinea:
```
"Central Administration - Territory of New Guinea"
"District Offices - Territory of New Guinea"
```

### Currency Notes

- **Fiji**: British sterling through the 1920s; Fiji pounds (linked to sterling) from the 1930s onwards. `salary_currency: "GBP"` for early era, `salary_currency: "FJD"` for later.
- **British Solomon Islands / Gilbert & Ellice**: Australian pounds (£A). `salary_currency: "AUD"`
- **Tonga**: Tongan pounds (linked to Australian £). `salary_currency: "TOP"`
- **New Hebrides**: Sterling and French francs both in use.
- **Default**: If currency is ambiguous, use `"GBP"` for positions clearly paid in pounds sterling notation.

---

## Department List by Era

### Fiji - 1877-1900 (Early Colony)

Source files show a flat structure, often no explicit department headers:

- Civil Establishment - Fiji
- Executive Council - Fiji
- Legislative Council - Fiji
- Department of Colonial Secretary - Fiji
- Department of Receiver-General - Fiji (Treasury)
- Government Store - Fiji
- Immigration Department - Fiji
- Department of Lands, Surveys, and Works - Fiji
- Postal Department - Fiji
- Medical Department - Fiji
- Department of Justice - Fiji
- Provincial Department - Fiji
- Armed Native Constabulary - Fiji
- Printing Office - Fiji
- Registrar-General - Fiji

### Fiji - 1900-1930 (Growth Period)

Above plus:
- Treasury - Fiji
- Customs Department - Fiji
- Audit Department - Fiji
- Lands Department - Fiji
- Constabulary - Fiji
- Prisons - Fiji
- Education Department - Fiji
- Agriculture Department - Fiji
- Native Lands Commission - Fiji
- Native Section - Fiji (within Colonial Secretary's Dept)
- Indian Section - Fiji (within Colonial Secretary's Dept)

### Fiji - 1930-1966 (Full Administration)

All above plus:
- Accountant-General - Fiji
- Director of Agriculture - Fiji
- Director of Audit - Fiji
- Director of Education - Fiji
- Conservator of Forests - Fiji
- Commissioner of Inland Revenue - Fiji
- Commissioner of Labour - Fiji
- Director of Lands, Mines and Survey - Fiji
- Attorney-General's Office - Fiji
- Director of Medical Services - Fiji
- Commissioner of Police - Fiji
- Postmaster-General's Office - Fiji
- Government Printer - Fiji
- Superintendent of Prisons - Fiji
- Director of Public Works - Fiji
- Registrar-General - Fiji
- Commerce and Industries - Fiji
- Registrar of Co-operatives - Fiji
- Broadcasting Commission - Fiji

### Western Pacific High Commission (all eras)

- High Commission - Western Pacific
- Audit (shared with Fiji) - Western Pacific

### Gilbert and Ellice Islands Colony

- Secretariat - Gilbert and Ellice Islands
- District Administration - Gilbert and Ellice Islands
- Treasury, Customs and Postal Departments - Gilbert and Ellice Islands
- Police and Prisons Department - Gilbert and Ellice Islands
- Medical Department - Gilbert and Ellice Islands
- Education Department - Gilbert and Ellice Islands
- Public Works Department - Gilbert and Ellice Islands
- Transport - Gilbert and Ellice Islands
- Wireless Department - Gilbert and Ellice Islands

### British Solomon Islands Protectorate

- Secretariat - British Solomon Islands
- District Administration - British Solomon Islands
- Treasury, Customs and Postal Department - British Solomon Islands
- Medical Department - British Solomon Islands
- Police and Prisons Department - British Solomon Islands
- Lands Department - British Solomon Islands
- Public Works Department - British Solomon Islands
- Native Labour Department - British Solomon Islands
- Wireless Department - British Solomon Islands
- Agricultural Committee - British Solomon Islands

### New Hebrides (Condominium)

Three parallel administrations:
- British National Administration - New Hebrides
- French National Administration - New Hebrides
- Joint Services - New Hebrides

### British New Guinea / Papua

- Executive Council - British New Guinea
- Legislative Council - British New Guinea
- Establishment - British New Guinea (or Papua)

### Territory of New Guinea (Australian Mandate)

- Central Administration - Territory of New Guinea
- Legal Department - Territory of New Guinea
- Treasury - Territory of New Guinea
- Customs and Trade Department - Territory of New Guinea
- Native Affairs Department - Territory of New Guinea
- Department of Lands and Survey - Territory of New Guinea
- Department of Health - Territory of New Guinea
- Department of Agriculture - Territory of New Guinea
- District Offices - Territory of New Guinea
- Expropriation Board - Territory of New Guinea

---

## Salary Format Patterns with Real Examples

### Early Era (1877-1920s) - Pounds with "l."

From Fiji 1877:
```
Governor and Commander-in-Chief, The Hon. Sir Arthur Hamilton Gordon, K.C.M.G., 5,000l.
→ salary_min: 5000, salary_max: 5000

Acting Chief Justice, John Gorrie, 1,000l.
→ salary_min: 1000, salary_max: 1000

Stipendiary Magistrates, H. G. C. Emberson, W. S. Carew, J. Blythe, A. Eastgate, 300l. each
→ salary_min: 300, salary_max: 300 (for EACH person)
```

From Fiji 1894:
```
Governor...Sir John Bates Thurston, K.C.M.G., 2,000l.
→ salary_min: 2000, salary_max: 2000

Assistant Private Secretary, E. A. Gledhill, 200l.
→ salary_min: 200, salary_max: 200

Boarding Officers, Suva, Geo. Gardiner, J. Campbell, and R. Bentley, 200l. each.
→ Creates THREE entries, each salary_min: 200, salary_max: 200

Sub-Collector of Customs, Levuka, Edgar C. Turner, 270l.
→ salary_min: 270, salary_max: 270, location: "Levuka"

Harbour Master, Levuka, W. W. Wilson, 100l., and 25l. as Marine Board Surveyor, and 25l. as Customs Officer.
→ salary_min: 100, allowances: "25l. as Marine Board Surveyor, and 25l. as Customs Officer"
```

From British New Guinea 1896:
```
Lieut. Governor, Sir W. MacGregor, K.C.M.G., M.D., D.Sc., LL.B., 1,500l., allowance 200l.
→ salary_min: 1500, salary_max: 1500, allowances: "200l.", honors: ["K.C.M.G."], qualifications: ["M.D.", "D.Sc.", "LL.B."]
```

From Western Pacific 1894:
```
High Commissioner, Sir J. B. Thurston, K.C.M.G.
→ (no salary listed here, but note dual-hat)

Chief Judicial Commissioner, H. S. Berkeley, 300l. (in addition to salary as Chief Justice of Fiji).
→ salary_min: 300, salary_max: 300, allowances: "in addition to salary as Chief Justice of Fiji"

Deputy Commissioner in Tonga, R. B. Leefe, 440l. and quarters.
→ salary_min: 440, salary_max: 440, allowances: "quarters", location: "Tonga"
```

### Middle Era (1920s-1930s) - Transition to ranges with "l." or "£"

From Fiji 1930:
```
Colonial Secretary, A. W. Seymour, 1,200£.
→ salary_min: 1200, salary_max: 1200

Assistant Colonial Secretary, A. A. Wright, 700£.-800£.
→ salary_min: 700, salary_max: 800

Chief Clerk, C. W. T. Johnson, 500£.-600£.
→ salary_min: 500, salary_max: 600

2nd Class Clerks, Miss W. Forster, Miss I. M. Smith, 270£.-400£.
→ Creates TWO entries, each salary_min: 270, salary_max: 400

Cadets, G. K. Roth, J. E. A. Bye, W. Pakenham-Walsh, J. Goepel, G. W. Bishop, 350£.
→ Creates FIVE entries, each salary_min: 350, salary_max: 350
```

From Gilbert and Ellice Islands 1933:
```
Resident Commissioner, A. F. Grimble, O.M.G., 800l. to 1,000l. by 50l.; 100l. duty allowance and quarters.
→ salary_min: 800, salary_max: 1000, duty_allowance: 100, allowances: "quarters"

Administrative Officers, W. C. B. Baverstock, A. C. F. Armstrong, and H. R. Maude, (one post vacant), 500l. to 600l. by 25l. and quarters.
→ Creates THREE entries (named persons only, skip vacant), salary_min: 500, salary_max: 600, allowances: "quarters"
```

From Tonga 1931:
```
Agent and Consul, Tonga, J. S. Neill, 800£. to 1,000£. and quarters; duty allowance 200£., and office allowance of 50£. as Consul.
→ salary_min: 800, salary_max: 1000, duty_allowance: 200, allowances: "quarters; office allowance of 50£. as Consul"
```

### Late Era (1940s-1960s) - Position-name format, no embedded salary

From British Solomon Islands 1940:
```
Resident Commissioner, W. S. Marchant, O.B.E., 1,200l. to 1,400l. and duty allowance, 100l.
→ salary_min: 1200, salary_max: 1400, duty_allowance: 100

Senior Medical Officer, H. B. Hetherington, M.D., Toronto, O.P. & S., Ontario, 700l. to 900l. and fees.
→ salary_min: 700, salary_max: 900, qualifications: ["M.D."], allowances: "fees"
```

From Fiji 1955 (no salary given - typical of latest era):
```
GOVERNOR AND COMMANDER-IN-CHIEF
—Sir Ronald Garvey, K.C.M.G., K.C.V.O., M.B.E.
→ salary_min: None, salary_max: None, honors: ["K.C.M.G.", "K.C.V.O.", "M.B.E."]

Colonial Secretary—A. F. R. Stoddart, C.M.G.
→ salary_min: None, salary_max: None, honors: ["C.M.G."]

Puisne Judge—W. D. Carew.
→ salary_min: None, salary_max: None
```

From Western Pacific 1957 (no salary given):
```
HIGH COMMISSIONER—J. Gutch, C.M.G., O.B.E.
→ honors: ["C.M.G.", "O.B.E."]

Administrative Officers—Class A—V. J. Andersen, M.B.E.; R. Davies; C. H. Allan; R. G. Roberts; T. Russell; L. M. Davies; A. C. Russell.
→ Creates SEVEN entries, each with position: "Administrative Officer, Class A"
```

From Fiji 1966:
```
Administrative Officers Class I.—Ratu E. T. T. Cakobau, O.B.E., M.C., E.D.; T. R. Cowell; J. S. Thomson, M.B.E.; ...
→ Creates multiple entries with position: "Administrative Officer, Class I"
```

### Increment Notation: "by Xl."

The pattern `500l. to 600l. by 25l.` means salary starts at 500, rises by increments of 25 to reach 600. Extract as:
```
salary_min: 500, salary_max: 600
```
The increment value itself is not captured as a separate field.

---

## Special Patterns

### "Ditto" References

From Fiji 1894:
```
1st Clerk, Arthur Langton, 250l.
2nd " Frank Spence, 200l. (acting Private Secretary and Despatch Clerk, 50l.)
3rd " Islay McOwan, 200l.
```
Expand "ditto" marks:
- `2nd "` = `2nd Clerk`
- `3rd "` = `3rd Clerk`

Also note the parenthetical for the 2nd Clerk: `(acting Private Secretary and Despatch Clerk, 50l.)` indicates additional duties and pay.

### Multi-Person Lines

**Pattern 1: Comma-separated with "each"**
From Fiji 1877:
```
Stipendiary Magistrates, H. G. C. Emberson, W. S. Carew, J. Blythe, A. Eastgate, 300l. each; H. Hunter, P. S. Friend, R. S. Swanston, A. Taylor, 250l. each.
```
Creates 4 persons at 300l. and 4 persons at 250l. Note the semicolon separates salary groups.

**Pattern 2: "and" separator**
From Fiji 1894:
```
Boarding Officers, Suva, Geo. Gardiner, J. Campbell, and R. Bentley, 200l. each.
```
Creates THREE entries.

**Pattern 3: Semicolon-separated in late era**
From Western Pacific 1957:
```
Administrative Officers—Class A—V. J. Andersen, M.B.E.; R. Davies; C. H. Allan; R. G. Roberts; T. Russell; L. M. Davies; A. C. Russell.
```
Creates SEVEN entries. Note semicolons separate individuals, and honors follow the name they belong to.

**Pattern 4: Named counts**
From Fiji 1894:
```
18 Roko Tu's, or Native Administrators of Provinces, and one Assistant, with salaries varying from 100l. to 340l.
```
SKIP - no individual names to extract. But note for validation that ~18 unnamed officials exist.

**Pattern 5: District Officers with locations**
From Territory of New Guinea 1925:
```
Rabaul.
District Officer, J. Walstab.
Deputy District Officers, W. J. Townsend, L. I. Hore.

Karieng.
District Officer, A. J. Hunter.
```
The location (Rabaul, Karieng, etc.) appears as a section header above the officer line.

### Acting/Temporary Status

```
Acting Chief Justice, John Gorrie, 1,000l.
→ acting_status: "Acting"

Chief Medical Officer, Dr. R. W. Alento (acting)
→ acting_status: "Acting"

A. L. Armstrong, Acting Secretary for Native Affairs.
→ acting_status: "Acting"

C. A. Holmes (acting), 100l.
→ acting_status: "Acting"

Clerk to Attorney-General (temporary), A. D. B. Parsons, 300l.
→ acting_status: "Temporary"
```

Note: "(acting)" often appears in parentheses AFTER the name, or the word "Acting" appears BEFORE the position title. Both patterns must be captured.

### Dual Salaries and Cross-Appointments

A distinctive Pacific pattern: officers hold positions in BOTH Fiji and the Western Pacific High Commission:

From Fiji 1930:
```
Chief Justice and Judicial Commissioner for the Western Pacific, Capt. M. H. Anderson, C.B.E., K.C., R.N. (retired), 1,200l., with quarters, receives 400l. from Western Pacific High Commission Funds.
```
Create entry with:
- `position`: "Chief Justice and Judicial Commissioner for the Western Pacific"
- `salary_min`: 1200
- `allowances`: "quarters; receives 400l. from Western Pacific High Commission Funds"

From Western Pacific 1933:
```
High Commissioner, Sir A. G. Murchison Fletcher K.C.M.G., C.B.E., 1,200l. (in addition to 3,000l. as Governor of Fiji, and allowance of 150l. as Consul-General for Western Pacific).
```
The parenthetical note explains the dual-hat. Extract the primary salary (1,200l.) and put the rest in `allowances`.

### Vacant Positions

**Early era: skip vacancies without salary**
```
Private Secretary (vacant).
→ SKIP

3rd Class Clerk (vacant).
→ SKIP
```

**Middle era: capture vacancies with salary**
```
First District Officer (vacant), 600l. to 700l.
→ name: None, position: "First District Officer", salary_min: 600, salary_max: 700

Commissioner of Lands and Crown Surveyor, (vacant), 600l. to 700l. and 25l. personal allowance.
→ name: None, position: "Commissioner of Lands and Crown Surveyor", salary_min: 600, salary_max: 700
```

**Late era: capture vacancies**
```
Comptroller of Customs—(Vacant).
→ name: None, position: "Comptroller of Customs"

Attorney-General—(Vacant).
→ name: None, position: "Attorney-General"
```

### Tongan Ministers and Native Officials

Tonga is a self-governing protected state. Tongan ministers appear with Tongan names:
```
Premier, Uliame Tugi.
Chief Justice, C. M. Murray Aynsley.
Speaker of the Legislative Assembly and Minister of the Crown, J. Finau Ulakalala.
Governor of Haapai, Satcki Faletau.
Governor of Vavau, J. Tuihaateiho.
```
Extract all of these. For Fijian chiefs:
```
Ratu J. C. Mataitini, Ratu D. Togainivalu, Ratu P. E. Seniloli.
```
"Ratu" is a Fijian chiefly title, NOT a military rank. Treat it as part of the name.

### Condominium Staff (New Hebrides)

The New Hebrides has three categories of staff that must be distinguished:
```
BRITISH NATIONAL ADMINISTRATION
Resident Commissioner—J. S. Rennie, O.B.E.

FRENCH NATIONAL ADMINISTRATION
Resident Commissioner—P. Anthonioz.

JOINT SERVICES
Treasurer—A. W. Garnett.
```
Use department suffixes: "British National Administration - New Hebrides", "French National Administration - New Hebrides", "Joint Services - New Hebrides". Extract French staff as well since they appear in the British Colonial Office List.

---

## Location/Region Extraction Rules

### Location from Position Title

```
Sub-Collector of Customs, Levuka, Edgar C. Turner, 270l.
→ position: "Sub-Collector of Customs", location: "Levuka"

Commissioner of Colo East and Stipendiary Magistrate, Rewa, W. S. Carew, 400l.
→ position: "Commissioner of Colo East and Stipendiary Magistrate", location: "Rewa", region: "Colo East"

Harbour Master, Suva, E. W. G. Twentyman, M.B.E., 400l.-500l.
→ location: "Suva"

Collector of Customs, Lautoka, A. Walker, 450l.-550l., and quarters.
→ location: "Lautoka"
```

### Location from Section Header

```
Rabaul.
District Officer, J. Walstab.
→ location: "Rabaul"

Manus.
District Officer (vacant).
→ location: "Manus"
```

### Region from Administrative Section

For Fiji, regions include the traditional administrative provinces:
- **Colo East**, **Colo West**, **Colo North** (interior Viti Levu)
- **Lau** (eastern island group)
- **Rotuma** (remote dependency)

For Territory of New Guinea, districts:
- **Rabaul**, **Kavieng**, **Madang**, **Kieta**, **Manus**, **Aitape**, **Morobe**, **Gasmata**, **Talasea**, **Namatanai**

For British Solomon Islands:
- **Malaita**, **Guadalcanal**, **Gizo**, **San Cristoval**, **Ysabel**, **Santa Cruz**, **Shortland Island**

For Gilbert and Ellice Islands:
- **Ocean Island** (headquarters until post-WWII)
- **Tarawa** (later headquarters)
- **Fanning Island**, **Christmas Island**

### Common Pacific Locations

**Fiji**: Suva (capital), Levuka (old capital), Lautoka, Nausori, Labasa, Savusavu, Taveuni, Kadavu, Nadi, Ba, Rotuma

**British Solomon Islands**: Tulagi (old HQ), Honiara (post-WWII HQ), Gizo, Auki (Malaita), Kirakira

**Gilbert and Ellice Islands**: Ocean Island (Banaba), Tarawa, Funafuti, Fanning Island, Christmas Island

**Tonga**: Nuku'alofa, Vava'u, Ha'apai

**New Hebrides**: Vila (Port Vila), Santo

**British New Guinea / Papua**: Port Moresby, Samarai, Daru

**Territory of New Guinea**: Rabaul, Kavieng, Madang, Kieta, Morobe

---

## Era-Specific Extraction Notes

### 1877-1899 (Early Fiji and Western Pacific)

- **Fiji**: Full colony listing with Governor, departments, and salary in "l." notation
- **Western Pacific**: Very small establishment; High Commissioner is the Governor of Fiji
- **British New Guinea**: Small establishment under a Lieutenant-Governor; administered via Queensland
- **Format**: Continuous prose-like entries, position and name on same line, salary at end
- **Key challenge**: Long run-on paragraphs with multiple people
- **Expected officials per file**: Fiji 15-60; Western Pacific 3-8; British New Guinea 10-20; Norfolk Island 1-2

**Example from Fiji 1877 (sparse)**:
```
Governor and Commander-in-Chief, The Hon. Sir Arthur Hamilton Gordon, K.C.M.G., 5,000l.
Private Secretary, A. L. Gordon.
Aide-de-Camp, Lieut. Knollys, 32nd Regiment.
Colonial Secretary and Receiver-General (provisional), — Maudsley, 500l.
```
Note the dash "—" for unknown first name. Extract surname only.

### 1900-1920 (Expansion)

- **British New Guinea becomes Papua** (1906); gradually ceases to appear
- **Fiji**: Growing departments, salary ranges appear (e.g., "300l. to 400l.")
- **Western Pacific**: Expanding with more Deputy Commissioners
- **Format**: Clearer department headers emerge
- **Expected officials**: Fiji 50-150; Western Pacific 5-15; Papua 15-30

### 1920-1940 (Peak Complexity)

- **New territories appear**: Gilbert and Ellice Islands Colony (from 1916/1924), Territory of New Guinea (from 1921/1925), British Solomon Islands (from ~1933), Tonga (from ~1931), Nauru
- **Fiji**: Full range of departments, salary in both "l." and "£" notation with ranges
- **Format**: Well-structured with clear department headers and salary ranges
- **Key challenge**: Multiple territories embedded in Western Pacific file
- **Expected officials**: Fiji 100-200; Western Pacific HQ 5-10; Gilbert & Ellice 20-40; Solomon Islands 20-40; Tonga 10-15; New Hebrides 5-15; Territory of New Guinea 30-50

**Example from Gilbert and Ellice Islands 1933**:
```
Medical Officers, D. C. M. Macpherson, M.B., Ch.B., 600l. to 650l. by 25l., and quarters and allowance of 100l., K. R. Steenson, M.B., Ch.B., 700l. to 800l. by 25l. and quarters. (Two vacancies.)
```
This is TWO named officers with DIFFERENT salary ranges, plus two vacancies. Each named officer has their own salary.

### 1940-1952 (War and Post-War)

- **WWII disruption**: Japanese occupation of Solomon Islands, Gilbert Islands; many posts vacant
- **Format**: Similar to 1930s but with more vacancies noted
- **Key note**: Solomon Islands and Gilbert & Ellice may show reduced staff
- **Free quarters and local allowance**: Often a blanket note at the end of a section applies to all staff listed above
- **Expected officials**: Variable due to wartime disruption

**Example from British Solomon Islands 1940** (blanket allowance note):
```
The above all receive free quarters and 50l. local allowance. Local allowance, however, is not payable to Native Medical Practitioners.
```
This applies to ALL officials listed above this line. Add to `allowances` field for each.

### 1952-1966 (Separation and Decolonization)

- **1952**: Governor of Fiji and High Commissioner for Western Pacific SEPARATED
- **High Commission moves to Honiara** (1953)
- **Format**: Modern directory style; position-name with em dash; often NO salary information
- **Key patterns**: "Administrative Officers—Class A—" followed by semicolon-separated names
- **Fiji files**: May include Pitcairn Islands section after 1952
- **Western Pacific files**: Much larger, containing detailed Solomon Islands and Gilbert & Ellice administrations
- **Expected officials**: Fiji 30-60 (named senior staff only); Western Pacific/Solomon Islands/Gilbert & Ellice 40-80

**Example from Fiji 1955 (no salary)**:
```
Director of Medical Services—J. M. Cruikshank, C.M.G., O.B.E.
Deputy Director—R. W. D. Maxwell.
Commissioner of Police—E. K. Laws, M.V.O.
```
No salary data at all. Extract position and honors only.

**Example from Western Pacific 1957 (classification system)**:
```
Administrative Officers—
Class A—V. J. Andersen, M.B.E.; R. Davies; C. H. Allan; R. G. Roberts; T. Russell; L. M. Davies; A. C. Russell.
```
Position for all is "Administrative Officer, Class A". Names are semicolon-separated.

---

## Validation Checklist

### All Years
- [ ] Officials list is non-empty
- [ ] All entries have name, canonical_name, surname, position, and department
- [ ] Salaries parsed where present in source
- [ ] Honors and qualifications in correct fields (not mixed)
- [ ] "Ditto" entries expanded to proper position names
- [ ] Fijian titles (Ratu) kept as part of name, not treated as military rank
- [ ] Multi-person lines split into individual entries

### 1877-1899
- [ ] Governor of Fiji captured (title varies: "Governor and Commander-in-Chief")
- [ ] High Commissioner role noted (same person as Governor)
- [ ] Chief Justice captured, noting dual role with Western Pacific
- [ ] British New Guinea Lieutenant-Governor captured
- [ ] Salary in "l." notation correctly parsed
- [ ] Expect: Fiji 15-60 officials; Western Pacific 3-8; British New Guinea 10-20

### 1900-1920
- [ ] Papua/British New Guinea staff captured (before Australian transfer)
- [ ] Salary ranges correctly parsed (e.g., "300l. to 400l.")
- [ ] Expect: Fiji 50-150 officials

### 1920-1940
- [ ] Multiple sub-territories extracted from Western Pacific file
- [ ] Gilbert and Ellice Islands Colony staff captured
- [ ] British Solomon Islands staff captured
- [ ] Tonga Agent/Consul AND Tongan Ministers captured
- [ ] Territory of New Guinea Administrator and district officers captured
- [ ] New Hebrides: British, French, AND Joint Services staff captured
- [ ] "by Xl." increments correctly handled in salary ranges
- [ ] Duty allowances extracted separately from base salary
- [ ] Expect: Fiji 100-200; each sub-territory 10-50

### 1940-1952
- [ ] Wartime vacancies noted
- [ ] Blanket allowance notes (e.g., "all receive free quarters") applied to relevant officials
- [ ] Native Medical Practitioners and similar local staff captured

### 1952-1966
- [ ] Fiji and Western Pacific treated as SEPARATE administrations
- [ ] Pitcairn Islands may appear under Fiji (Chief Magistrate)
- [ ] No salary in many late files - do not fabricate salary data
- [ ] Classification grades (Class A, Class I, etc.) captured in position title
- [ ] Solomon Islands and Gilbert & Ellice may appear as sub-sections of WPHC file
- [ ] Expect: Fiji 30-60 named senior officials; WPHC + sub-territories 40-80

---

## Key Positions by Era

### 1877-1899
1. Governor and Commander-in-Chief, Fiji (also High Commissioner for Western Pacific)
2. Colonial Secretary, Fiji
3. Chief Justice, Fiji (also Judicial Commissioner for Western Pacific)
4. Receiver-General, Fiji (Treasurer)
5. Attorney-General, Fiji
6. Chief Medical Officer, Fiji
7. Commissioner of Lands, Fiji
8. Lieutenant-Governor / Administrator, British New Guinea

### 1900-1940
All above (adjusted titles) plus:
9. Secretary for Native Affairs, Fiji
10. Secretary for Indian Affairs, Fiji (from ~1920s)
11. Resident Commissioner, Gilbert and Ellice Islands
12. Resident Commissioner, British Solomon Islands
13. Agent and Consul, Tonga
14. Resident Commissioner, New Hebrides (British)
15. Administrator, Territory of New Guinea

### 1952-1966
1. Governor and Commander-in-Chief, Fiji (NO LONGER High Commissioner)
2. High Commissioner for the Western Pacific (separate office, based at Honiara)
3. Colonial Secretary, Fiji
4. Financial Secretary, Fiji
5. Chief Secretary, Western Pacific
6. Resident Commissioner, Gilbert and Ellice Islands
7. Resident Commissioner, New Hebrides (British)
8. Judicial Commissioner, British Solomon Islands
9. British Agent and Consul, Tonga (under Governor of Fiji from 1952)
10. Chief Magistrate, Pitcairn Island (under Governor of Fiji from 1952)

---

## Sample Output

### 1894 Style (Early Fiji)
```python
{
    "name": "Sir John Bates Thurston",
    "canonical_name": "Thurston, Sir John Bates",
    "given_names": "John Bates",
    "surname": "Thurston",
    "position": "Governor and Commander-in-Chief and High Commissioner for the Western Pacific",
    "department": "Civil Establishment - Fiji",
    "salary_min": 2000,
    "salary_max": 2000,
    "honors": ["K.C.M.G."],
    "location": None,
    "region": None,
}
```

### 1896 Style (British New Guinea)
```python
{
    "name": "Sir W. MacGregor",
    "canonical_name": "MacGregor, Sir W.",
    "given_names": "W.",
    "surname": "MacGregor",
    "position": "Lieutenant Governor",
    "department": "Establishment - British New Guinea",
    "salary_min": 1500,
    "salary_max": 1500,
    "allowances": "200l.",
    "honors": ["K.C.M.G."],
    "qualifications": ["M.D.", "D.Sc.", "LL.B."],
    "location": None,
    "region": None,
}
```

### 1930 Style (Fiji with salary ranges)
```python
{
    "name": "A. W. Seymour",
    "canonical_name": "Seymour, A. W.",
    "given_names": "A. W.",
    "surname": "Seymour",
    "position": "Colonial Secretary",
    "department": "Colonial Secretary's Department - Fiji",
    "salary_min": 1200,
    "salary_max": 1200,
    "honors": [],
    "location": None,
    "region": None,
}
```

### 1933 Style (Gilbert and Ellice Islands)
```python
{
    "name": "A. F. Grimble",
    "canonical_name": "Grimble, A. F.",
    "given_names": "A. F.",
    "surname": "Grimble",
    "position": "Resident Commissioner",
    "department": "Civil Establishment - Gilbert and Ellice Islands",
    "salary_min": 800,
    "salary_max": 1000,
    "duty_allowance": 100,
    "allowances": "quarters",
    "honors": ["O.M.G."],
    "location": None,
    "region": None,
}
```

### 1940 Style (British Solomon Islands)
```python
{
    "name": "W. S. Marchant",
    "canonical_name": "Marchant, W. S.",
    "given_names": "W. S.",
    "surname": "Marchant",
    "position": "Resident Commissioner",
    "department": "Civil Establishment - British Solomon Islands",
    "salary_min": 1200,
    "salary_max": 1400,
    "duty_allowance": 100,
    "honors": ["O.B.E."],
    "allowances": "free quarters and 50l. local allowance",
    "location": None,
    "region": None,
}
```

### 1955 Style (Fiji, no salary)
```python
{
    "name": "Sir Ronald Garvey",
    "canonical_name": "Garvey, Sir Ronald",
    "given_names": "Ronald",
    "surname": "Garvey",
    "position": "Governor and Commander-in-Chief",
    "department": "Civil Establishment - Fiji",
    "salary_min": None,
    "salary_max": None,
    "honors": ["K.C.M.G.", "K.C.V.O.", "M.B.E."],
    "location": None,
    "region": None,
}
```

### 1957 Style (Western Pacific, administrative class)
```python
{
    "name": "V. J. Andersen",
    "canonical_name": "Andersen, V. J.",
    "given_names": "V. J.",
    "surname": "Andersen",
    "position": "Administrative Officer, Class A",
    "department": "Civil Establishment - British Solomon Islands",
    "salary_min": None,
    "salary_max": None,
    "honors": ["M.B.E."],
    "location": None,
    "region": None,
}
```

### Tonga Style (Protected State officials)
```python
{
    "name": "Uliame Tugi",
    "canonical_name": "Tugi, Uliame",
    "given_names": "Uliame",
    "surname": "Tugi",
    "position": "Premier",
    "department": "Ministers - Tonga",
    "salary_min": None,
    "salary_max": None,
    "honors": [],
    "location": None,
    "region": None,
}
```

### New Hebrides Condominium Style
```python
{
    "name": "J. S. Rennie",
    "canonical_name": "Rennie, J. S.",
    "given_names": "J. S.",
    "surname": "Rennie",
    "position": "Resident Commissioner",
    "department": "British National Administration - New Hebrides",
    "salary_min": None,
    "salary_max": None,
    "honors": ["O.B.E."],
    "location": None,
    "region": None,
}
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

**Pacific-specific names**: Fijian names (Ratu, Roko Tui, etc.) and Tongan names should be preserved as-is. "Ratu" is a chiefly title, not a personal name or military rank.

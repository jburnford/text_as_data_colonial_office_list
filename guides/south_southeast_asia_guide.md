# South and Southeast Asia Colonial Office List - Extraction Guide

## 1. Overview

This guide provides instructions for extracting personnel data from Colonial Office List files (1867-1966) for British colonies in South and Southeast Asia. These colonies present unique challenges due to multiple currency systems, complex administrative reorganizations, and dual-salary schemes for European vs. local staff.

**Colonies covered**: Ceylon, Hong Kong, Straits Settlements, Singapore, Labuan, North Borneo, Sarawak, Brunei, Federated Malay States, Unfederated Malay States, Federation of Malaya, Aden, Wei-hai-Wei

**Target Model**: Gemini 3 Flash Preview (via API)

**Schema**: 20 fields defined in `guides/schema.py`
**Required fields**: `name`, `canonical_name`, `surname`, `position`, `department`

---

## 2. Historical Context

### Administrative Evolution

| Era | Key Changes |
|-----|-------------|
| 1867 | Straits Settlements transferred from India Office to Colonial Office; Ceylon, Hong Kong, Labuan already Crown Colonies |
| 1874 | British Residents appointed to Perak, Selangor, Sungei Ujong (Malay States) |
| 1895 | Federated Malay States created (Perak, Selangor, Negri Sembilan, Pahang) |
| 1898 | New Territories (Hong Kong) leased for 99 years; Wei-hai-Wei leased |
| 1906-07 | Labuan incorporated into Straits Settlements; Brunei becomes protectorate |
| 1930 | Wei-hai-Wei returned to China |
| 1937 | Aden transferred from India to Colonial Office as Crown Colony |
| 1942-45 | Japanese occupation of all SE Asian colonies |
| 1946 | Straits Settlements dissolved; Singapore becomes separate colony; Malayan Union formed |
| 1948 | Ceylon independent; Federation of Malaya replaces Malayan Union |
| 1957 | Federation of Malaya independent |
| 1963 | Singapore, North Borneo (Sabah), Sarawak join Malaysia |
| 1966 | Aden independent (South Yemen) |

### The Malay States System

Unlike Crown Colonies, the Malay States operated under a system of British Residents (later Advisers) who theoretically advised Malay rulers rather than governing directly.

**Federated Malay States (FMS, 1895-1948)**: Perak, Selangor, Negri Sembilan, Pahang
- Headed by a Resident-General (later Chief Secretary), based at Kuala Lumpur
- Each state had a British Resident and state-level civil service
- Governor of Straits Settlements served as High Commissioner for FMS

**Unfederated Malay States (UMS)**: Johore, Kedah, Perlis, Kelantan, Trengganu
- Each had a British Adviser (less formal control than Residents)
- Retained more autonomy than FMS states
- Note: Johore accepted an Adviser only from 1914

**Federation of Malaya (1948-1957)**: All nine Malay States plus Penang and Malacca
- High Commissioner replaced Governor as head of state
- Conference of Rulers established for Malay sultans
- Mentri Besar (Chief Minister) in each state

---

## 3. Regional Divisions and Colony Structure

### Ceylon (1867-1948)
Nine provinces, each headed by a Government Agent:
- **Western Province** (Colombo) - seat of government
- **Central Province** (Kandy)
- **Southern Province** (Galle)
- **Northern Province** (Jaffna)
- **Eastern Province** (Trincomalee/Batticaloa)
- **North-Western Province** (Kurunegala/Chilaw)
- **North-Central Province** (Anuradhapura)
- **Uva Province** (Badulla)
- **Sabaragamuwa Province** (Ratnapura/Kegalla)

### Hong Kong (1843-1997)
- **Victoria** (Hong Kong Island) - main city and seat of government
- **Kowloon** (ceded 1860)
- **New Territories** (leased 1898)
- **Outlying Islands**
- Postal Agencies in China (Shanghai, Canton, Amoy, Foochow, etc.) under HK Postmaster-General

### Straits Settlements (1867-1946)
Three settlements, each with a Resident Councillor:
- **Singapore** - seat of government
- **Penang** (George Town) - includes Province Wellesley and the Dindings
- **Malacca**
- Dependencies: **Labuan** (from 1907), **Cocos-Keeling Islands**, **Christmas Island**

### Aden (1937-1967)
- **Aden Colony** (the port and immediate surroundings)
- **Aden Protectorate** (administered by Governor of Aden)
- Note: Before 1937, Aden was under the Government of India and does NOT appear in the Colonial Office List

### Smaller Territories
- **Labuan** (1848-1906 independent; 1907+ under Straits Settlements); **Wei-hai-Wei** (1898-1930, 5-15 officials)
- **North Borneo** (Chartered Company territory); **Sarawak** (Brooke family); **Brunei** (Protectorate from 1888)

---

## 4. Data Schema

### Official Record Structure

```python
{
    "name": "Sir Hugh Clifford",             # Name as appears in source
    "canonical_name": "Clifford, Hugh",       # "Surname, Given Names"
    "given_names": "Hugh",
    "surname": "Clifford",
    "position": "Colonial Secretary",
    "department": "Colonial Secretary's Office - Ceylon",

    # Salary fields - CRITICAL: currency varies by colony
    "salary_min": 20250,                      # Numeric value only
    "salary_max": 20250,
    "salary_currency": "Rs",                  # Rs, HKD, SSd, GBP, etc.
    "salary_scale": None,                     # 1940s-50s only
    "allowances": "entertainment allowance Rs. 22,500",
    "duty_allowance": None,
    "expatriation_pay": None,                 # 1940s-50s only
    "per_diem": None,

    # Status
    "acting_status": None,                    # "Acting", "Temporary", "Officiating", "Relief"

    # Classification
    "honors": ["K.C.M.G."],
    "qualifications": [],
    "military_rank": None,

    # Location
    "location": None,                         # Specific station
    "region": None,                           # Province or state
}
```

### Currency Field Values

| Colony | Currency Code | Symbol in Source | Notes |
|--------|--------------|------------------|-------|
| Ceylon (pre-1877) | GBP | l., £ | Pounds sterling |
| Ceylon (1877+) | Rs | Rs. | Ceylon rupees; senior European staff may still show GBP |
| Hong Kong (early) | GBP | l., £ | Senior officers in sterling |
| Hong Kong (early) | HKD | $ | Local/clerical staff |
| Hong Kong (1950s) | HKD | H.K. $, $ | All staff in HK dollars |
| Straits Settlements | GBP | £ | Senior European officers |
| Straits Settlements | SSd | $ | Straits dollars for local staff |
| Labuan | GBP | l. | Pounds sterling |
| FMS/UMS | GBP | £ | Most positions in sterling |
| Federation of Malaya | MYD | $ | Malayan dollars (post-1948) |
| Aden | GBP | £ | Pounds sterling |
| Wei-hai-Wei | GBP | l., £ | Pounds sterling |

**CRITICAL**: When both £ and $ appear in the same colony listing, you MUST determine the correct currency from context. In Hong Kong, $ without qualifier means HKD. In Straits Settlements, $ means SSd. Never assume GBP when $ is used.

---

## 5. Department Naming Convention

Use the format **"Department Name - Colony/Settlement Name"** for the `department` field.

**Ceylon**: Colonial Secretary's Office - Ceylon, Treasurer's Department - Ceylon, Audit Office - Ceylon, Surveyor General's Department - Ceylon, Queen's Advocate's Department - Ceylon, Government Agents - Ceylon, Medical Department - Ceylon, Police Department - Ceylon. Later additions: Controller of Revenue's Office, Irrigation, Forest, Railway, Electrical, Veterinary, Mines, Agriculture, Marine departments.

**Hong Kong**: Colonial Secretary's Department - Hong Kong, Treasurer's Department - Hong Kong, Registrar-General's Department - Hong Kong, Harbour Master's Department - Hong Kong, Police Department - Hong Kong, Judicial Establishments - Hong Kong. 1910 additions: Cadet Service, Sanitary, Prisons, Observatory. 1950 additions: Secretariat, Secretary for Chinese Affairs, Civil Aviation, Commerce and Industry, Labour, Social Welfare.

**Straits Settlements**: Departments are listed under each settlement. Use settlement name (Singapore, Penang, Malacca) not "Straits Settlements": Colonial Secretary's Office - Singapore, Chinese Protectorate - Singapore, Treasury - Singapore, Judicial Department - Singapore. For shared departments use: "Education Department - Straits Settlements" or note "S.S. and F.M.S." scope.

**Aden**: Governor's Office - Aden, Secretariat - Aden, Treasury - Aden, Legal Department - Aden, Medical Department - Aden, Police - Aden, Education - Aden, Public Works - Aden, Aden Protectorate Levies - Aden.

---

## 6. Salary Formats

### Early Era: Pounds with "l." (1867-1920s)

Used in Ceylon (pre-1877), Hong Kong, Straits Settlements, Labuan, Wei-hai-Wei.

```
Simple:     Governor, T. F. Callaghan, 800l.
            -> salary_min: 800, salary_max: 800, salary_currency: "GBP"

Range:      Chief Clerk, R. H. Crofton, 400l. to 600l.
            -> salary_min: 400, salary_max: 600, salary_currency: "GBP"

Shillings:  Interpreter, 187l. 10s.
            -> salary_min: 187, salary_max: 187, salary_currency: "GBP"
               allowances: "10s."

Per diem:   7s. 6d. per diem as Superintendent of Stamping Department
            -> per_diem: "7s. 6d.", salary_currency: "GBP"
```

### Ceylon Rupees (1877 onwards)

```
Simple:     Governor, Rs. 105,000.
            -> salary_min: 105000, salary_max: 105000, salary_currency: "Rs"

Mixed:      Second Assistant Colonial Secretary, E. B. Denham, 550l. to 700l.
            -> salary_min: 550, salary_max: 700, salary_currency: "GBP"
            (European cadets sometimes in sterling even in rupee-era Ceylon)

Footnotes:  * Including Rs. 22,500 entertainment allowance.
            -> allowances: "entertainment allowance Rs. 22,500"
```

### Hong Kong Dollars (1900s onwards)

```
Dollar:     Colonial Secretary, Sir F. H. May, K.C.M.G., $10,800.
            -> salary_min: 10800, salary_max: 10800, salary_currency: "HKD"

Sterling:   Governor, Sir F. J. D. Lugard, K.C.M.G., C.B., D.S.O., 6,000L
            -> salary_min: 6000, salary_max: 6000, salary_currency: "GBP"

Mixed:      Unpassed Cadets, 225L, and $540 each, house allowance.
            -> salary_min: 225, salary_currency: "GBP"
               allowances: "$540 house allowance"

1950 HKD:   Colonial Secretary—J. F. Nicoll, C.M.G. $38,400.
            -> salary_min: 38400, salary_max: 38400, salary_currency: "HKD"

Range:      Deputy Colonial Secretary—C. B. Burgess. $26,400-28,800.
            -> salary_min: 26400, salary_max: 28800, salary_currency: "HKD"
```

### Straits Settlements Dollars

```
Sterling:   Governor, Sir John Anderson, G.C.M.G. £6,000
            -> salary_min: 6000, salary_max: 6000, salary_currency: "GBP"

SS dollar:  Registrar Exports and Imports, A. Stuart $3,600
            -> salary_min: 3600, salary_max: 3600, salary_currency: "SSd"

Dual:       Resident Councillor, R. N. Bland (and entertainment allowance, $1,200) £1,500
            -> salary_min: 1500, salary_max: 1500, salary_currency: "GBP"
               allowances: "entertainment allowance $1,200"
```

### 1950s Expatriation Pay (Hong Kong)

Post-war Hong Kong lists expatriation pay tables at the start of the Civil Establishment section. Note the table exists but do NOT add expatriation amounts to individual salary fields unless explicitly listed for a specific officer.

---

## 7. Extraction Patterns

### Name Patterns

**Standard pattern**: `Position, Name, Salary`
```
Colonial Secretary, W. G. Gibson, 2,000l.
-> name: "W. G. Gibson", position: "Colonial Secretary"
```

**1950s em-dash pattern**: `Position—Name. Salary.`
```
Colonial Secretary—J. F. Nicoll, C.M.G. $38,400.
-> name: "J. F. Nicoll", position: "Colonial Secretary", honors: ["C.M.G."]
```

**Unknown first name (dash)**: `— Russell, 200l.`
```
-> name: "Russell", given_names: None, surname: "Russell"
```

**Multi-ethnic names** (common in this region):
```
Sinhalese:    M. Coomaraswamy, Sir Solomon Dias Bandaranaike
Dutch-Burgher: J. Kriekenbeeb, E. de Kretser, L. D'Almada e Castro
Chinese:       Chau Tsun-nin, Tan Jiak Kim, Wei Yuk
Malay:         W. M. Abdul Rahman, Muka (single name)
Portuguese:    J. M. D'Almada e Castro, D. J. Barrados
```

For non-European names where surname conventions differ, use the full name as `surname` if you cannot reliably determine the family name. For Chinese names, the first element is typically the surname (e.g., Chau in "Chau Tsun-nin").

### Ditto Patterns

"Ditto" refers to the previous line's position keyword.

```
Colonial Secretary, W. G. Gibson, 2,000l.
Principal Assistant, F. B. Templer, 1,000l.
Second ditto, J. Swan, 600l.
-> "Second ditto" resolves to "Second Assistant" (ditto = "Assistant")

Assistant Surveyor, W. R. Noad, 750l.
J. Winzer, 650l.
-> J. Winzer is also "Assistant Surveyor" (position carried from previous line)

Government Printer, H. C. Cottle, Rs. 6,375.
Assistant ditto, H. M. Richards, Rs. 4,290.
-> "Assistant ditto" = "Assistant Government Printer"

Harbour-Master and Marine Magistrate, Henry Thomsett, R.N., 700l.
1st Clerk, J. Thornton, 400l.
2nd ditto, W. Lording, 300l.
-> "2nd ditto" = "2nd Clerk"

Deputy ditto, Lieutenant B. A. Cator, R.N.
-> "Deputy ditto" = "Deputy Master Attendant" (ditto = previous position keyword)
```

### Acting Status

```
Acting Administrator, Col. Conran     -> acting_status: "Acting"
H. W. F. C. Brodhurst (on leave); L. W. Booth (acting)
  -> Two records: Brodhurst (no acting_status) and Booth (acting_status: "Acting")
Private Secretary—Vacant. $9,200. (Miss B. Budden, acting.)
  -> name: "B. Budden", acting_status: "Acting"
```

### Multiple People on One Line

```
# Pattern 1: Comma-separated list with "each"
Passed Cadets, F. Robinson, E. E. Colman, A. de Mello, each 300 to 350
-> THREE officials, each with salary_min: 300, salary_max: 350

# Pattern 2: Semicolon-separated (1950s)
Class II—J. H. B. Lee; H. J. Cruttwell; P. C. M. Sedgwick. $8,640-22,800.
-> THREE officials, each with salary_min: 8640, salary_max: 22800

# Pattern 3: "and" separator
1st-Class Assistant Surgeons, D. H. D. Waldron, and W. M. Elliott, 500l. to 600l.
-> TWO officials, each with same position and salary
```

### Writers/Clerks in Block + Footnotes

Writers or clerks may be listed as a block under a heading with shared salary:
```
Writers, commencing at 200l. per annum.
L. F. Lee, Æ. King, G. W. Templer, R. Massie, ...
-> Each person: position: "Writer", salary_min: 200, salary_currency: "GBP"
```

Watch for footnotes marked with `*`, `+`, or `||` that modify salary or allowances for specific entries above them.

---

## 8. Special Patterns for This Region

### Dual Currency Systems

Many colonies list senior European officers in GBP and local/clerical staff in local currency. The extraction must detect which currency is in use per line.

**Rules**:
1. If salary shows "l." or "L" suffix -> `salary_currency: "GBP"`
2. If salary shows "Rs." prefix -> `salary_currency: "Rs"`
3. If salary shows "$" in Hong Kong context -> `salary_currency: "HKD"`
4. If salary shows "$" in Straits Settlements context -> `salary_currency: "SSd"`
5. If salary shows "$" in Federation of Malaya context -> `salary_currency: "MYD"`
6. If salary shows "£" -> `salary_currency: "GBP"`
7. If no currency indicator, inherit from most recent salary line in same section

### The Resident/Adviser System (Malay States)

Federated Malay States entries appear either within the Straits Settlements section or in their own section, depending on the year.

```
Resident-General, Sir W. T. Taylor, K.C.M.G.
-> position: "Resident-General", department: "Resident-General's Office - FMS"

British Resident, Perak, E. W. Birch
-> position: "British Resident", department: "British Residency - Perak"
   location: None, region: "Perak"

British Adviser, Johore, D. J. Jardine
-> position: "British Adviser", department: "British Adviser's Office - Johore"
   region: "Johore"
```

### Shared Appointments

Some officers held posts spanning multiple territories:
```
Secretary for Chinese Affairs, S.S. and F.M.S., C. J. Saunders 1,200
-> department: "Chinese Protectorate - Straits Settlements"

Director of Education, S.S. and F.M.S., J. B. Elcum, £1,200
-> department: "Education Department - Straits Settlements"
```

### Other Special Cases

- **Labuan sub-section** (1907-1946): Appears under Straits Settlements; use `department: "Civil Establishment - Labuan"`
- **Ecclesiastical**: Bishops often listed as "(unpaid)" -> `salary_min: None`
- **Mint officers** (Hong Kong 1867): Footnote "All Mint officers have free quarters" -> `allowances: "free quarters"`
- **Salary increments**: "300l. by 50l. to 500l." -> `salary_min: 300, salary_max: 500` (ignore increment)
- **Exchange compensation** (Hong Kong 1900s-1930s): Note in `allowances` when mentioned for an individual

---

## 9. Location Extraction

### Location in Position Title
```
Government Agent, Western Province, H. W. F. C. Brodhurst
-> position: "Government Agent", region: "Western Province"

District Judge and 1st Magistrate, E. G. Broadrick
-> position: "District Judge and 1st Magistrate"
   (no location unless a place name follows)

Resident Councillor, Penang, R. N. Bland
-> position: "Resident Councillor", location: "Penang"
```

### Location from Section Headers

Source files use settlement names as section headers in Straits Settlements:
```
SINGAPORE.
Colonial Secretary's Office.
Colonial Secretary, Captain Sir A. H. Young, K.C.M.G. 1,700
-> department: "Colonial Secretary's Office - Singapore"
   location: "Singapore"

PENANG.
Resident Councillor, R. N. Bland £1,500
-> location: "Penang"
```

### Province as Region (Ceylon)
```
Government Agent, Central Province, J. P. Lewis.
-> region: "Central Province"

Provincial Assistant, Western Province, H. Byrne, 1000l.
-> region: "Western Province"
```

### Common Locations by Colony

**Ceylon**: Colombo, Kandy, Galle, Jaffna, Trincomalee, Batticaloa, Kurunegala, Anuradhapura, Badulla, Ratnapura, Nuwara Eliya, Matale, Matara, Chilaw, Kegalla, Hambantota, Mannar, Mullaittivu, Vavuniya

**Hong Kong**: Victoria, Kowloon, New Territories, Stanley, Aberdeen, Tai Po

**Straits Settlements**: Singapore, George Town (Penang), Malacca, Province Wellesley, Dindings, Labuan

**FMS**: Kuala Lumpur, Ipoh, Seremban, Kuantan, Taiping, Klang

**Aden**: Aden, Crater, Steamer Point, Sheikh Othman, Little Aden

---

## 10. Era-Specific Notes

### 1867-1876 (Early Crown Colony)

- **Ceylon**: GBP salaries (e.g., "7,000l."); provincial Government Agent system
- **Hong Kong**: Small establishment ~50 officials; Mint section (closed 1868); dual GBP + dollar salaries
- **Straits Settlements**: 1867 is first year in Colonial Office List; listed as "(Proposed) Civil Establishment"; three settlements (Singapore, Penang, Malacca) each with local staff
- **Labuan**: Tiny establishment ~15 officials; all GBP
- **Expected officials**: Ceylon 100-200, Hong Kong 50-80, SS 30-60, Labuan 10-20

### 1877-1899 (Expansion)

- **Ceylon**: Switches to Rs. (Rupees) from 1877; European cadets may still show GBP; establishment grows substantially
- **Hong Kong**: New Territories added 1898; dollar salaries more common for lower ranks
- **Straits Settlements**: FMS established 1895; may appear within SS section
- **Wei-hai-Wei**: Appears from 1898; very small establishment
- **Expected officials**: Ceylon 200-400, Hong Kong 80-150, SS 80-150

### 1900-1920 (Peak Imperial)

- **Ceylon**: Large establishment; Rs. salaries standard; dual currency (senior Europeans in GBP, locals in Rs.)
- **Hong Kong**: Exchange compensation system for dollar-salaried officers; "L" notation for GBP (e.g., "6,000L")
- **Straits Settlements**: Sub-sections for Singapore, Penang, Malacca; Labuan incorporated 1907; "$" means Straits dollars
- **FMS**: May have own section; Resident-General oversees Residents in each state
- **Expected officials**: Ceylon 400-600, Hong Kong 150-250, SS+FMS 200-400

### 1920-1940 (Interwar)

- **Ceylon**: Donoughmore Constitution 1931; increasing self-governance
- **Hong Kong**: Post-strike recovery; dollar standardizing
- **Straits Settlements**: Unified salary scales; combined SS and FMS departments
- **Aden**: Appears from 1937 edition; transferred from India; GBP throughout
- **Expected officials**: Ceylon 400-600, Hong Kong 200-350, SS+FMS 300-500, Aden 50-100

### 1942-1945 (Japanese Occupation)

Most SE Asian colonies under Japanese control; Colonial Office List entries may be minimal or absent. Ceylon and Aden (not occupied) continue normally.

### 1946-1966 (Post-War Reorganization)

- **Ceylon**: Independent 1948; drops from Colonial Office List
- **Hong Kong**: All salaries in HK$; expatriation pay tables; em-dash pattern ("Position--Name. Salary."); semi-colon-separated name lists
- **Singapore**: Separate colony from 1946; Malayan dollar
- **Federation of Malaya**: Created 1948; High Commissioner; nine Malay States + Penang + Malacca
- **North Borneo/Sarawak**: Crown Colonies from 1946
- **Aden**: Legislative Council from 1947; expanding administration
- **Expected officials**: Hong Kong 300-500, Singapore 200-400, Malaya 300-500, Aden 100-200

---

## 11. Validation Checklist

### All Years
- [ ] Officials list is non-empty
- [ ] All entries have `name`, `canonical_name`, `surname`, `position`, `department`
- [ ] `salary_currency` is set correctly for EVERY salary entry
- [ ] Rs. salaries are NOT confused with GBP
- [ ] $ salaries have correct currency code (HKD, SSd, or MYD, never USD)
- [ ] Honors and qualifications separated into correct fields
- [ ] "Ditto" entries resolved to proper position names
- [ ] Multi-ethnic names handled (Chinese, Malay, Sinhalese, Dutch-Burgher)
- [ ] Acting status captured where indicated

### Colony-Specific Checks

**Ceylon**:
- [ ] Government Agents captured for each province listed
- [ ] Currency is GBP for pre-1877, Rs for 1877+
- [ ] Mixed currency correctly handled (European cadets in GBP, locals in Rs)

**Hong Kong**:
- [ ] Governor captured with entertainment allowance noted
- [ ] Dual currency (GBP for senior, HKD for local) correctly differentiated
- [ ] Exchange compensation noted where mentioned
- [ ] 1950s expatriation pay table NOT added to individual salaries

**Straits Settlements**:
- [ ] Officials grouped by settlement (Singapore, Penang, Malacca)
- [ ] Shared departments (SS and FMS) handled
- [ ] Dollar amounts marked as SSd (not HKD or MYD)
- [ ] Labuan sub-section captured (post-1907)

**Malay States**:
- [ ] Residents/Advisers captured for each state listed
- [ ] State names used for region field
- [ ] High Commissioner position identified

**Aden**:
- [ ] Only appears from 1937; all salaries in GBP
- [ ] Protectorate officials distinguished from Colony officials

### Era-Specific Checks

- [ ] 1867-1876: Ceylon uses GBP only; Labuan very small (~15 officials)
- [ ] 1900-1920: FMS officials captured; Hong Kong "L" notation = GBP
- [ ] 1946-1966: Singapore separate from SS; Federation of Malaya instead of FMS

---

## Key Positions to Verify

Every extraction should capture these core positions (when present in the source):

**All colonies**: Governor, Colonial Secretary, Attorney-General (or Queen's Advocate), Treasurer, Chief Justice, Auditor-General, Director of Public Works, Principal Medical Officer

**Ceylon additionally**: Controller of Revenue, Government Agent (one per province), Surveyor-General

**Hong Kong additionally**: Registrar-General, Secretary for Chinese Affairs, Captain Superintendent of Police

**Straits Settlements additionally**: Resident Councillor (Penang), Resident Councillor (Malacca), Colonial Engineer/Surveyor-General, Inspector-General of Police. Note: Governor also serves as High Commissioner for FMS.

**Malay States additionally**: Resident-General (FMS), British Resident (per state), British Adviser (UMS states)

---

## Sample Output

### 1910 Ceylon (Rupee era with mixed GBP)
```python
# Source: "Second Assistant Colonial Secretary, E. B. Denham, 550l. to 700l."
# Note: European cadet in GBP despite Rs. era
{"name": "E. B. Denham", "canonical_name": "Denham, E. B.", "given_names": "E. B.",
 "surname": "Denham", "position": "Second Assistant Colonial Secretary",
 "department": "Colonial Secretary's Office - Ceylon",
 "salary_min": 550, "salary_max": 700, "salary_currency": "GBP"}

# Source: "Governor, Colonel Sir H. E. McCallum, R.E., G.C.M.G., Rs. 105,000.*"
# Footnote: "* Including Rs. 22,500 entertainment allowance."
{"name": "Sir H. E. McCallum", "canonical_name": "McCallum, H. E.",
 "given_names": "H. E.", "surname": "McCallum", "position": "Governor",
 "department": "Civil Establishment - Ceylon",
 "salary_min": 105000, "salary_max": 105000, "salary_currency": "Rs",
 "honors": ["G.C.M.G."], "qualifications": ["R.E."], "military_rank": "Colonel",
 "allowances": "entertainment allowance Rs. 22,500"}
```

### 1910 Hong Kong (dual currency)
```python
# Source: "Colonial Secretary, Sir F. H. May, K.C.M.G., $10,800."
{"name": "Sir F. H. May", "canonical_name": "May, F. H.", "given_names": "F. H.",
 "surname": "May", "position": "Colonial Secretary",
 "department": "Colonial Secretary's Department - Hong Kong",
 "salary_min": 10800, "salary_max": 10800, "salary_currency": "HKD",
 "honors": ["K.C.M.G."]}

# Source: "Governor, Sir F. J. D. Lugard, K.C.M.G., C.B., D.S.O., 6,000L"
{"name": "Sir F. J. D. Lugard", "canonical_name": "Lugard, F. J. D.",
 "given_names": "F. J. D.", "surname": "Lugard", "position": "Governor",
 "department": "Civil Establishment - Hong Kong",
 "salary_min": 6000, "salary_max": 6000, "salary_currency": "GBP",
 "honors": ["K.C.M.G.", "C.B.", "D.S.O."]}
```

### 1950 Hong Kong (post-war HKD)
```python
# Source: "Colonial Secretary—J. F. Nicoll, C.M.G. $38,400."
{"name": "J. F. Nicoll", "canonical_name": "Nicoll, J. F.", "given_names": "J. F.",
 "surname": "Nicoll", "position": "Colonial Secretary",
 "department": "Secretariat - Hong Kong",
 "salary_min": 38400, "salary_max": 38400, "salary_currency": "HKD",
 "honors": ["C.M.G."]}
```

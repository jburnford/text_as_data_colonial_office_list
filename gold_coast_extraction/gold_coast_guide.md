# Gold Coast Colonial Office List - Extraction Guide

## Overview

This guide provides instructions for extracting personnel data from Gold Coast Colonial Office List files (1867-1957). The Gold Coast became Ghana upon independence in 1957.

**Target Model**: Gemini 3 Flash Preview (via API)

---

## Source Files

### Available Years (58 files)
1867-1957 with some gaps. Files are named variously:
- `gold_coast.txt`
- `gold_coast_colony.txt`
- `the_gold_coast.txt`
- `THE_GOLD_COAST.md`
- `GOLD_COAST_GHANA.txt` (1957)

---

## Historical Context

### Administrative Evolution

| Era | Characteristics |
|-----|-----------------|
| 1867-1874 | Under Sierra Leone administration ("Administrator" not "Governor") |
| 1874-1886 | Gold Coast Colony established (separated from Lagos 1886) |
| 1896-1901 | Ashanti annexed after defeat of Prempeh |
| 1901 onwards | Northern Territories added as Protectorate |
| 1922-1946 | Togoland Mandate (British) added |
| 1946-1957 | UN Trusteeship era |
| 1957 | Independence as Ghana |

### Regional Divisions (post-1901)

1. **Gold Coast Colony** (coastal/southern) - also called just "Colony"
2. **Ashanti** (central, Kumasi/Coomassie)
3. **Northern Territories** (northern, Tamale)
4. **Togoland** (eastern, from 1922 as British Mandate)

---

## Data Schema

### Official Record Structure

```python
{
    "name": "F. M. Hodgson",           # Name as appears in source
    "canonical_name": "Hodgson, F. M.", # "Surname, Given Names"
    "given_names": "F. M.",
    "surname": "Hodgson",
    "position": "Governor",
    "department": "Civil Establishment - Gold Coast",

    # Salary fields
    "salary_min": 3000,                 # Minimum salary (pounds)
    "salary_max": 3000,                 # Maximum salary (pounds)
    "salary_scale": None,               # "A", "B", "C.1", "C.2", "M2" etc. (1940s-50s)
    "allowances": "500l. table allowance",  # Text description of allowances
    "duty_allowance": 500,              # Numeric duty allowance if specified
    "expatriation_pay": None,           # 1940s-50s: £150-600 based on salary band
    "per_diem": None,                   # e.g., "5s. 6d." for daily rate positions

    # Status fields
    "acting_status": None,              # "Acting", "Temporary", "Relief", "Officiating"
    "tenure_type": None,                # "Permanent", "Temporary", "Contract"

    # Classification
    "honors": ["C.M.G."],               # Post-nominal honors
    "qualifications": [],               # Academic/professional qualifications
    "military_rank": None,              # "Colonel", "Major", etc.

    # Location fields
    "location": None,                   # Specific station (Accra, Cape Coast, etc.)
    "region": None,                     # "Colony", "Ashanti", "Northern Territories", "Togoland"
}
```

---

## Department List by Era

### 1867-1874 (Sierra Leone Administration)
Very sparse - most positions listed under "Civil Establishment" without department headers:
- Civil Establishment - Gold Coast
- (No formal department structure)

### 1874-1900 (Colony Established)
- Civil Establishment - Gold Coast
- Executive Council - Gold Coast
- Legislative Council - Gold Coast
- Governor's Office - Gold Coast
- Colonial Secretary's Office - Gold Coast
- Treasury - Gold Coast
- Customs - Gold Coast
- Post Office - Gold Coast
- Telegraph Department - Gold Coast
- Medical Department - Gold Coast
- Judicial Department - Gold Coast
- Education Department - Gold Coast
- Police Department - Gold Coast
- Prison Department - Gold Coast
- Public Works Department - Gold Coast
- Printing Department - Gold Coast
- Ecclesiastical - Gold Coast
- Botanical Station - Gold Coast

### 1899-1920 (Expansion Era) - Additional departments:
- Volta River Preventive Service - Gold Coast
- Hausa Constabulary - Gold Coast
- Civil Police - Gold Coast
- Gold Coast Volunteer Corps - Gold Coast
- District Commissioners - Gold Coast
- Resident, Kumasi - Gold Coast (post-1896)

### 1901-1920 (Regional Administration Added)
- Administration - Ashanti
- Administration - Northern Territories
- Chief Commissioner's Office - Ashanti
- Chief Commissioner's Office - Northern Territories

### 1920-1940 (Peak Complexity)
All above plus:
- Railway Department - Gold Coast
- Harbour Department - Gold Coast
- Agriculture Department - Gold Coast
- Forestry Department - Gold Coast
- Veterinary Department - Gold Coast
- Survey Department - Gold Coast
- Mines Department - Gold Coast
- Administration - Togoland (post-1922)

### 1940-1957 (Modern Structure)
All above plus many new specialized departments:
- Accountant-General - Gold Coast
- Air Services - Gold Coast
- Animal Health - Gold Coast
- Broadcasting - Gold Coast
- Cocoa Rehabilitation - Gold Coast
- Commerce and Industry - Gold Coast
- Co-operation - Gold Coast
- Electrical Department - Gold Coast
- Fisheries - Gold Coast
- Geological Survey - Gold Coast
- Income Tax - Gold Coast
- Labour - Gold Coast
- Lands - Gold Coast
- Public Relations - Gold Coast
- Social Welfare and Housing - Gold Coast
- Water Supply - Gold Coast

---

## Extraction Patterns

### Title Patterns (appear BEFORE name)
```
Military: Colonel, Col., Lt.-Col., Lieut.-Col., Major-General, Major, Captain, Capt., Brigadier, Brigadier-General
Honorific: Sir, The Right Hon., The Hon., Right Rev., Rev., Ven., Dr.
```

### Honors (appear AFTER name) - Post-nominal letters for service
```
K.C.M.G., G.C.M.G., C.M.G., K.C.B., G.C.B., C.B., K.B.E., O.B.E., M.B.E.,
C.B.E., K.C.S.I., C.I.E., D.S.O., M.C., V.D., E.D., T.D., Kt., Knt.
```

### Qualifications (appear AFTER name) - Academic/professional
```
Medical: M.D., M.B., M.R.C.S., F.R.C.S., L.R.C.S., L.R.C.P., F.R.C.P., Ch.B., D.P.H.
Academic: B.A., M.A., B.Sc., M.Sc., LL.D., D.D., Ph.D., B.L., LL.B.
Engineering: R.E., C.E., M.I.C.E., A.I.C.E., A.M.I.C.E., M.I.E.E.
Other: F.R.S., F.R.G.S., A.R.I.B.A.
```

---

## Salary Formats

### Early Era (1867-1920s) - Pounds with "l."
```
Simple: 200l.                         → salary_min: 200, salary_max: 200
Range: 300l. to 400l.                → salary_min: 300, salary_max: 400
With increments: 500l. by 20l. to 600l. → salary_min: 500, salary_max: 600
With allowances: 500l. and quarters   → salary_min: 500, allowances: "quarters"
With shillings: 36l. 10s.            → salary_min: 36 (note "10s." in allowances)
With pence: 27l. 7s. 6d.             → salary_min: 27 (note "7s. 6d." in allowances)
```

### Per Diem Notation (1890s-1920s)
Some positions paid daily rates instead of annual salary:
```
5s. 6d. per diem                      → per_diem: "5s. 6d.", salary_min: None
1l. per diem in addition to emoluments → per_diem: "1l.", note additional pay
4s. 6d. to 5s. 6d. per diem          → per_diem: "4s. 6d. to 5s. 6d."
```

### Later Era (1920s-1930s) - Transition to £
```
Scale reference: Scale A              → salary_scale: "A"
Explicit amount: £1,200              → salary_min: 1200, salary_max: 1200
Range: £500-£700                     → salary_min: 500, salary_max: 700
With duty allowance: £1,800, and duty allowance, 360l. → salary_min: 1800, duty_allowance: 360
```

### Salary Scales (1940s-1950s)
```
Scale A: £450 for 3 years, 510-30-660, 720-30-960, 1,000
Scale B: £450 for 3 years, 510-20-610, 660-30-900
Scale C:
  Section 1 (C.1): £450 for 3 years, £510-15-600
  Section 2 (C.2): £660-20-720
  Section 3 (C.3): £735-30-825
  Section 1A (C.1A): £650
Scale M2: £690 for 3 years, 720-30-1,000, 1,080-30-1,200
```

Combined scale notation: "Scale C.1.2" means Section 1 progressing to Section 2.

### Expatriation Pay (1940s-1950s) - IMPORTANT

In addition to base salary, expatriate officers receive extra pay based on salary band:

| Basic Salary | Expatriation Pay |
|--------------|------------------|
| £450-599     | £150             |
| £600-700     | £200             |
| £700-829     | £250             |
| £830-1,050   | £300             |
| £1,051-1,175 | £350             |
| £1,176-1,350 | £400             |
| £1,351-1,600 | £450             |
| £1,601-1,850 | £500             |
| Over £1,850  | £600             |

**Note**: Expatriation pay applies to "expatriate officers" (typically Europeans). Extract this when the source mentions it or when processing 1940s-1950s data.

---

## Special Patterns

### "Ditto" - References previous position type
```
Chief Clerk, J. S. Hagan, 150l.
2nd ditto, S. H. Brew, 120l.        → Position: "2nd Clerk"
3rd ditto, T. W. Parker, 50l.       → Position: "3rd Clerk"
```

### Acting/Temporary Status - ALWAYS CAPTURE
```
Acting Administrator, Col. Conran.   → acting_status: "Acting"
Acting Governor, W. Low.             → acting_status: "Acting"
Officiating Colonial Secretary       → acting_status: "Officiating"
Temporary District Commissioner      → acting_status: "Temporary"
```

### Multiple People Patterns

#### Pattern 1: "and" separator (2 people)
```
1st-Class Assistant Surgeons, D. H. D. Waldron, and W. M. Elliott, 500l. to 600l.
```
→ Creates TWO officials, EACH with salary_min: 500, salary_max: 600

#### Pattern 2: Comma-separated list with "each"
```
Third-Class Clerks, K. F. T. Buco, G. F. N. Taylor, D. K. Meldowell, 350l. to 500l. each.
```
→ Creates THREE officials, EACH with same salary range

#### Pattern 3: Comma-separated list (no "each")
```
Assistant Colonial Secretaries, George Attrill, C. H. P. Hunter, S. W. Morgan, 400l. to 500l.
```
→ Creates THREE officials with same position and salary range

#### Pattern 4: Grouped count
```
Fourteen Third-Class Clerks, 50l. to 70l. each.
```
→ Note: "14 unnamed Third-Class Clerks" - skip (no names to extract)

#### Pattern 5: Complex multi-role (1950s) - CHALLENGING
```
Class I. Assistant Chief Commissioners, Commissioner, Cocoa Rehabilitation...—G. N. Burden, M.B.E.; W. H. Beeton; D. A. Sutherland. £1,350.
```
→ Names listed after all position types share the salary; exact role assignment may be ambiguous

---

## Location Extraction - IMPORTANT

### Location in Position Title
```
District Commissioner, Accra, L. N. Peregrine, 525l.
→ position: "District Commissioner", location: "Accra"

Dispenser, Waterloo, W. Z. Young, 50l.
→ position: "Dispenser", location: "Waterloo"

Keeper of Prison, Elmina, J. Baifie, 100l.
→ position: "Keeper of Prison", location: "Elmina"

Sub-Accountant at Sulymah, J. A. Cline, 10l.
→ position: "Sub-Accountant", location: "Sulymah"
```

### Location in Section Header
```
Accra Government School:
Schoolmaster, W. J. Lomax, 280l. to 300l.
→ position: "Schoolmaster", location: "Accra"
```
Location comes from the section header, not the position line.

### Region from Administrative Section
```
ADMINISTRATION section for Ashanti:
Chief Commissioner, Ashanti, C. H. Harper, C.M.G.
→ position: "Chief Commissioner", region: "Ashanti"
```

### Common Gold Coast Locations
**Coastal**: Accra, Cape Coast, Elmina, Sekondi, Takoradi, Axim, Winneba, Saltpond, Keta, Ada, Christiansborg, Dixcove, Quittah (Keta)

**Interior Colony**: Kumasi (Coomassie), Tarquah (Tarkwa), Koforidua, Aburi, Nsawam, Obuasi

**Northern**: Tamale, Gambaga, Wa, Kintampo, Salaga, Yendi, Navrongo, Bolgatanga

**Togoland**: Ho, Kpandu, Kete Krachi

---

## Vacancy Handling

### Early Era (1867-1930s): Skip vacancies
```
Private Secretary (vacant).          → SKIP - do not create entry
Superintendent of Public Works, (vacant). → SKIP
```

### Late Era (1940s-1950s): Capture vacancy with salary
```
Director of Agriculture—Vacant. £1,400.
→ Create entry with name: null, position: "Director of Agriculture", salary_min: 1400
→ This preserves the salary data for the position even when unfilled
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

---

## Era-Specific Extraction Notes

### 1867-1874 (Sierra Leone Era)
- **Title**: "Administrator" not "Governor" (Gold Coast under Sierra Leone)
- **Structure**: Very sparse, no department headers
- **Salaries**: Often missing for many positions
- **Names**: May be incomplete (e.g., "— Ussher, Esq." with dash for unknown first name)
- **Expected officials**: 10-30

### 1875-1899 (Colony Established)
- **Title**: "Governor" now used
- **Structure**: Clear department sections emerge
- **Best reference year**: 1899 has excellent detail
- **Salaries**: Consistently in "Xl." or "Xl. to Yl." format
- **Expected officials**: 50-200

### 1900-1920 (Ashanti/NT Added)
- **New regions**: Ashanti (1901), Northern Territories (1901)
- **Military presence**: Hausa Constabulary, Gold Coast Regiment prominent
- **Resident positions**: "Resident, Kumasi" type positions
- **Expected officials**: 150-350

### 1920-1940 (Peak Complexity)
- **Togoland added**: 1922 as British Mandate
- **Currency shift**: "£" replaces "l." notation
- **Salary scales**: A, B, C scales introduced
- **Provincial structure**: Provincial Commissioners, District Commissioners
- **Expected officials**: 300-500

### 1940-1957 (Late Colonial)
- **Format**: Standardized DEPARTMENT HEADERS in capitals
- **Salary system**: Scales fully developed with grade subdivisions (C.1, C.1.2, etc.)
- **Expatriation pay**: Additional compensation for expatriate officers
- **Vacancies**: Listed WITH salary amounts
- **New departments**: Air Services, Broadcasting, Social Welfare, etc.
- **Expected officials**: 200-450

---

## Validation Checklist

### All Years
- [ ] Officials list is non-empty
- [ ] All entries have name and position fields
- [ ] Salaries parsed (where present in source)
- [ ] Honors and qualifications in correct fields
- [ ] "Ditto" entries expanded to proper position names

### 1867-1874
- [ ] "Administrator" or "Acting Administrator" captured (not "Governor")
- [ ] Expect sparse data - many positions without salary

### 1875-1899
- [ ] Governor captured
- [ ] Colonial Secretary captured
- [ ] Major department heads captured
- [ ] Locations extracted for district/station positions

### 1900-1920
- [ ] Governor, Colonial Secretary captured
- [ ] Ashanti administration staff captured (post-1901)
- [ ] Northern Territories staff captured (post-1901)
- [ ] Constabulary/military staff captured

### 1920-1957
- [ ] All regional Chief Commissioners captured
- [ ] Salary scales correctly identified
- [ ] Togoland staff captured (post-1922)
- [ ] Expatriation pay noted where applicable (1940s-50s)

---

## Key Positions by Era

### 1867-1874
1. Administrator / Acting Administrator

### 1875-1899
1. Governor
2. Colonial Secretary
3. Chief Justice
4. Colonial Treasurer
5. Collector/Comptroller of Customs
6. Colonial Surgeon / Chief Medical Officer
7. Attorney-General (when present)

### 1900-1957
1. Governor
2. Colonial Secretary
3. Chief Justice
4. Attorney-General
5. Treasurer / Financial Secretary
6. Director of Medical Services
7. Chief Commissioner, Ashanti (post-1901)
8. Chief Commissioner, Northern Territories (post-1901)
9. Comptroller of Customs
10. Director of Public Works
11. General Manager of Railways (post-1903)

---

## Sample Output

### 1867 Style (Sparse)
```python
{
    "name": "Col. Conran",
    "canonical_name": "Conran, Col.",
    "given_names": None,
    "surname": "Conran",
    "position": "Administrator",
    "department": "Civil Establishment - Gold Coast",
    "salary_min": None,
    "salary_max": None,
    "acting_status": "Acting",
    "military_rank": "Colonel",
    "location": None,
    "region": None,
}
```

### 1899 Style (Detailed)
```python
{
    "name": "F. M. Hodgson",
    "canonical_name": "Hodgson, F. M.",
    "given_names": "F. M.",
    "surname": "Hodgson",
    "position": "Governor",
    "department": "Civil Establishment - Gold Coast",
    "salary_min": 3000,
    "salary_max": 3000,
    "allowances": "500l. table allowance",
    "honors": ["C.M.G."],
    "location": None,
    "region": "Colony",
}
```

### 1950 Style (Scale-based)
```python
{
    "name": "Sir Charles Noble Arden Arden-Clarke",
    "canonical_name": "Arden-Clarke, Sir Charles Noble Arden",
    "given_names": "Charles Noble Arden",
    "surname": "Arden-Clarke",
    "position": "Governor",
    "department": "Governor - Gold Coast",
    "salary_min": 4500,
    "salary_max": 4500,
    "duty_allowance": 1500,
    "expatriation_pay": 600,
    "honors": ["K.C.M.G."],
    "location": None,
    "region": None,
}
```

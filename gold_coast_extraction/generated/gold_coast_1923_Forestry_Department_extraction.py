"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "N. C. McLeod", "canonical_name": "McLeod, N. C.", "given_names": "N. C.", "surname": "McLeod",
     "position": "Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "Capt. R. W. Brent", "canonical_name": "Brent, R. W.", "given_names": "R. W.", "surname": "Brent",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l.", "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "N. T. Garnett", "canonical_name": "Garnett, N. T.", "given_names": "N. T.", "surname": "Garnett",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "P. G. Arnold", "canonical_name": "Arnold, P. G.", "given_names": "P. G.", "surname": "Arnold",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "Capt. G. S. Greene", "canonical_name": "Greene, G. S.", "given_names": "G. S.", "surname": "Greene",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l.", "military_rank": "Captain"},
    {"name": "L. C. Rowney", "canonical_name": "Rowney, L. C.", "given_names": "L. C.", "surname": "Rowney",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "J. A. Wills", "canonical_name": "Wills, J. A.", "given_names": "J. A.", "surname": "Wills",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "F. Burnett", "canonical_name": "Burnett, F.", "given_names": "F.", "surname": "Burnett",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "C. Vigne", "canonical_name": "Vigne, C.", "given_names": "C.", "surname": "Vigne",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "D. Hendry", "canonical_name": "Hendry, D.", "given_names": "D.", "surname": "Hendry",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "J. D. MacAinsh", "canonical_name": "MacAinsh, J. D.", "given_names": "J. D.", "surname": "MacAinsh",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "H. W. Moore", "canonical_name": "Moore, H. W.", "given_names": "H. W.", "surname": "Moore",
     "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "L. V. Wilcox", "canonical_name": "Wilcox, L. V.", "given_names": "L. V.", "surname": "Wilcox",
     "position": "European Forester", "department": "Forestry Department - Gold Coast", "salary_min": 440, "salary_max": 500},
    {"name": "B. Bennett", "canonical_name": "Bennett, B.", "given_names": "B.", "surname": "Bennett",
     "position": "European Forester", "department": "Forestry Department - Gold Coast", "salary_min": 440, "salary_max": 500},
    {"name": "F. C. Coleman", "canonical_name": "Coleman, F. C.", "given_names": "F. C.", "surname": "Coleman",
     "position": "Saw Doctor", "department": "Forestry Department - Gold Coast", "salary_min": 440, "salary_max": 500},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
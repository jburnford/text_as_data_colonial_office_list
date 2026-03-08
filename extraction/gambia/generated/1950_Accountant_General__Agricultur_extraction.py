"""
Gambia Colonial Office List 1950 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1950

OFFICIALS = [
    {"name": "E. B. W. Carrol", "canonical_name": "Carrol, E. B. W.", "given_names": "E. B. W.", "surname": "Carrol", "position": "Accountant General", "department": "Accountant General - Gambia", "honors": ["O.B.E."], "salary_scale": "B"},
    {"name": "D. T. D. Taylor", "canonical_name": "Taylor, D. T. D.", "given_names": "D. T. D.", "surname": "Taylor", "position": "Assistant Accountant", "department": "Accountant General - Gambia", "salary_scale": "C"},
    {"name": "H. R. Monday", "canonical_name": "Monday, H. R.", "given_names": "H. R.", "surname": "Monday", "position": "Assistant Accountant", "department": "Accountant General - Gambia", "salary_scale": "C"},
    {"name": "J. H. Palmer", "canonical_name": "Palmer, J. H.", "given_names": "J. H.", "surname": "Palmer", "position": "Senior Agricultural Officer", "department": "Agricultural - Gambia", "salary_scale": "A"},
    {"name": "R. A. Kitching", "canonical_name": "Kitching, R. A.", "given_names": "R. A.", "surname": "Kitching", "position": "Agricultural Officer", "department": "Agricultural - Gambia", "salary_scale": "A"},
    {"name": "P. A. Donovan", "canonical_name": "Donovan, P. A.", "given_names": "P. A.", "surname": "Donovan", "position": "Agricultural Officer", "department": "Agricultural - Gambia", "salary_scale": "A"},
    {"name": "W. A. Wright", "canonical_name": "Wright, W. A.", "given_names": "W. A.", "surname": "Wright", "position": "Agricultural Officer", "department": "Agricultural - Gambia", "salary_scale": "A"},
    {"name": "K. S. Collins", "canonical_name": "Collins, K. S.", "given_names": "K. S.", "surname": "Collins", "position": "Principal Auditor", "department": "Audit - Gambia", "salary_min": 810, "salary_max": 810, "expatriation_pay": 250, "allowances": "rent, £90"},
    {"name": "J. P. Murphy", "canonical_name": "Murphy, J. P.", "given_names": "J. P.", "surname": "Murphy", "position": "Attorney General", "department": "Crown Law and Lands - Gambia", "salary_min": 1100, "salary_max": 1100, "expatriation_pay": 350},
    {"name": "M. Messer-Bennetts", "canonical_name": "Messer-Bennetts, M.", "given_names": "M.", "surname": "Messer-Bennetts", "position": "Lands Officer", "department": "Crown Law and Lands - Gambia", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
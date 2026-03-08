"""
Gambia Colonial Office List 1918 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1918

OFFICIALS = [
    {"name": "R. W. Orpen", "canonical_name": "Orpen, R. W.", "given_names": "R. W.", "surname": "Orpen", "position": "Medical Officer of Health", "department": "Medical - Gambia"},
    {"name": "C. Wolfendale", "canonical_name": "Wolfendale, C.", "given_names": "C.", "surname": "Wolfendale", "position": "Sanitary Inspector", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "D. D. Peters", "canonical_name": "Peters, D. D.", "given_names": "D. D.", "surname": "Peters", "position": "Clerk of the Market", "department": "Civil Establishment - Gambia", "salary_min": 50, "salary_max": 70, "allowances": "and personal allowance of 10l. per annum"},
    {"name": "J. A. Johnson", "canonical_name": "Johnson, J. A.", "given_names": "J. A.", "surname": "Johnson", "position": "Inspector of Nuisances", "department": "Civil Establishment - Gambia", "salary_min": 60, "salary_max": 70},
    {"name": "M. King", "canonical_name": "King, M.", "given_names": "M.", "surname": "King", "position": "Caretaker", "department": "Civil Establishment - Gambia", "salary_min": 48, "salary_max": 48}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
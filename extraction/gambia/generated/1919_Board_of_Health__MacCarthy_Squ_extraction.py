"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "R. W. Orpen", "canonical_name": "Orpen, R. W.", "given_names": "R. W.", "surname": "Orpen", "position": "Medical Officer of Health", "department": "Board of Health - Gambia", "salary_min": 500, "salary_max": 600, "allowances": "100l. each duty and staff allowances"},
    {"name": "C. Wolfendale", "canonical_name": "Wolfendale, C.", "given_names": "C.", "surname": "Wolfendale", "position": "Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "G. Barracough", "canonical_name": "Barracough, G.", "given_names": "G.", "surname": "Barracough", "position": "Assistant Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "D. D. Peters", "canonical_name": "Peters, D. D.", "given_names": "D. D.", "surname": "Peters", "position": "Clerk of the Market", "department": "Board of Health - Gambia", "salary_min": 50, "salary_max": 70, "allowances": "personal allowance of 10l. per annum"},
    {"name": "J. A. Johnson", "canonical_name": "Johnson, J. A.", "given_names": "J. A.", "surname": "Johnson", "position": "Inspector of Nuisances", "department": "Board of Health - Gambia", "salary_min": 60, "salary_max": 70},
    {"name": "S. Gaye", "canonical_name": "Gaye, S.", "given_names": "S.", "surname": "Gaye", "position": "Caretaker", "department": "MacCarthy Square Board - Gambia", "salary_min": 48, "salary_max": 48}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
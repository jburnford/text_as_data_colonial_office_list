"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "W. F. Crook", "canonical_name": "Crook, W. F.", "given_names": "W. F.", "surname": "Crook", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem when travelling"},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "A. D. Sawyer", "canonical_name": "Sawyer, A. D.", "given_names": "A. D.", "surname": "Sawyer", "position": "4th Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "E. L. Gueritz", "canonical_name": "Gueritz, E. L.", "given_names": "E. L.", "surname": "Gueritz", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "T. R. King", "canonical_name": "King, T. R.", "given_names": "T. R.", "surname": "King", "position": "2nd Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. M. Davies", "canonical_name": "Davies, J. M.", "given_names": "J. M.", "surname": "Davies", "position": "4th Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
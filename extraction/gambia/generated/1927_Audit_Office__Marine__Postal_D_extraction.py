"""
Gambia Colonial Office List 1927 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1927

OFFICIALS = [
    {"name": "A. F. B. Howard", "canonical_name": "Howard, A. F. B.", "given_names": "A. F. B.", "surname": "Howard", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 400, "salary_max": 920},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "Chief Clerk, 2nd Grade", "department": "Audit Office - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "A. D. Steele", "canonical_name": "Steele, A. D.", "given_names": "A. D.", "surname": "Steele", "position": "Harbour Master and Marine Superintendent", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720, "duty_allowance": 100, "allowances": "80l. messing allowance"},
    {"name": "J. M. Simpson", "canonical_name": "Simpson, J. M.", "given_names": "J. M.", "surname": "Simpson", "position": "Chief Engineer", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720},
    {"name": "J. B. Fathers", "canonical_name": "Fathers, J. B.", "given_names": "J. B.", "surname": "Fathers", "position": "Assistant Engineer", "department": "Marine - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "A. Robarts", "canonical_name": "Robarts, A.", "given_names": "A.", "surname": "Robarts", "position": "Boatswain", "department": "Marine - Gambia", "salary_min": 360, "salary_max": 360},
    {"name": "J. L. Fenton", "canonical_name": "Fenton, J. L.", "given_names": "J. L.", "surname": "Fenton", "position": "Director of Posts", "department": "Postal Department - Gambia", "salary_min": 720, "salary_max": 800},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Postmaster", "department": "Postal Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "2nd Grade Clerk", "department": "Postal Department - Gambia", "salary_min": 160, "salary_max": 230}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
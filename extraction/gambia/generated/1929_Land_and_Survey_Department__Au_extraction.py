"""
Gambia Colonial Office List 1929 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1929

OFFICIALS = [
    {"name": "W. H. MoTurk", "canonical_name": "MoTurk, W. H.", "given_names": "W. H.", "surname": "MoTurk", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 600, "salary_max": 900},
    {"name": "L. Hagon", "canonical_name": "Hagon, L.", "given_names": "L.", "surname": "Hagon", "position": "Assistant Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "A. G. Still", "canonical_name": "Still, A. G.", "given_names": "A. G.", "surname": "Still", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 400, "salary_max": 920},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "Chief Clerk, 2nd Grade", "department": "Audit Office - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "A. D. Steele", "canonical_name": "Steele, A. D.", "given_names": "A. D.", "surname": "Steele", "position": "Harbour Master and Marine Superintendent", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720, "duty_allowance": 100, "allowances": "80l. messing allowance"},
    {"name": "J. M. Simpson", "canonical_name": "Simpson, J. M.", "given_names": "J. M.", "surname": "Simpson", "position": "Chief Engineer", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720},
    {"name": "E. E. Dixson", "canonical_name": "Dixson, E. E.", "given_names": "E. E.", "surname": "Dixson", "position": "Artiller Engineers", "department": "Marine - Gambia", "salary_min": 500, "salary_max": 600},
    {"name": "J. Reid", "canonical_name": "Reid, J.", "given_names": "J.", "surname": "Reid", "position": "Artiller Engineers", "department": "Marine - Gambia", "salary_min": 500, "salary_max": 600},
    {"name": "I. Boughley", "canonical_name": "Boughley, I.", "given_names": "I.", "surname": "Boughley", "position": "Boatswain", "department": "Marine - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "J. L. Fenton", "canonical_name": "Fenton, J. L.", "given_names": "J. L.", "surname": "Fenton", "position": "Director of Posts", "department": "Postal Department - Gambia", "salary_min": 600, "salary_max": 720},
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
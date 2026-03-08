"""
Gambia Colonial Office List 1925 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1925

OFFICIALS = [
    {"name": "W. H. McTurk", "canonical_name": "McTurk, W. H.", "given_names": "W. H.", "surname": "McTurk", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 600, "salary_max": 800, "allowances": "72l. seniority allowance"},
    {"name": "A. G. R. Sly", "canonical_name": "Sly, A. G. R.", "given_names": "A. G. R.", "surname": "Sly", "position": "Assistant Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "W. A. V. Small", "canonical_name": "Small, W. A. V.", "given_names": "W. A. V.", "surname": "Small", "position": "3rd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "S. O. Briggs", "canonical_name": "Briggs, S. O.", "given_names": "S. O.", "surname": "Briggs", "position": "3rd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "E. L. Gueritz", "canonical_name": "Gueritz, E. L.", "given_names": "E. L.", "surname": "Gueritz", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 400, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "Chief Clerk (2nd Grade)", "department": "Audit Office - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "F. Q. Owens", "canonical_name": "Owens, F. Q.", "given_names": "F. Q.", "surname": "Owens", "position": "4th Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "J. F. Coker", "canonical_name": "Coker, J. F.", "given_names": "J. F.", "surname": "Coker", "position": "4th Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 82}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
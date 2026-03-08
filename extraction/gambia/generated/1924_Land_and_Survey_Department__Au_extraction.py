"""
Gambia Colonial Office List 1924 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1924

OFFICIALS = [
    {"name": "W. F. Crook", "canonical_name": "Crook, W. F.", "given_names": "W. F.", "surname": "Crook", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 600, "salary_max": 900},
    {"name": "A. G. E. Sly", "canonical_name": "Sly, A. G. E.", "given_names": "A. G. E.", "surname": "Sly", "position": "Assistant Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "W. A. V. Small", "canonical_name": "Small, W. A. V.", "given_names": "W. A. V.", "surname": "Small", "position": "3rd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "S. O. Briggs", "canonical_name": "Briggs, S. O.", "given_names": "S. O.", "surname": "Briggs", "position": "4th Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "E. L. Gueritz", "canonical_name": "Gueritz, E. L.", "given_names": "E. L.", "surname": "Gueritz", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 400, "salary_max": 920},
    {"name": "T. R. King", "canonical_name": "King, T. R.", "given_names": "T. R.", "surname": "King", "position": "Chief Clerk (2nd Grade)", "department": "Audit Office - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "C. J. Thomas", "canonical_name": "Thomas, C. J.", "given_names": "C. J.", "surname": "Thomas", "position": "4th Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "F. Q. Owen", "canonical_name": "Owen, F. Q.", "given_names": "F. Q.", "surname": "Owen", "position": "4th Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "A. D. Steele", "canonical_name": "Steele, A. D.", "given_names": "A. D.", "surname": "Steele", "position": "Harbour Master and Marine Superintendent", "department": "Government Vessels - Gambia", "salary_min": 480, "salary_max": 720, "duty_allowance": 100, "allowances": "80l. messing allowance"},
    {"name": "J. M. Simpson", "canonical_name": "Simpson, J. M.", "given_names": "J. M.", "surname": "Simpson", "position": "Chief Engineer", "department": "Government Vessels - Gambia", "salary_min": 480, "salary_max": 510, "allowances": "80l. messing allowance"},
    {"name": "J. B. Fathers", "canonical_name": "Fathers, J. B.", "given_names": "J. B.", "surname": "Fathers", "position": "Assistant Engineer", "department": "Government Vessels - Gambia", "salary_min": 450, "salary_max": 450, "allowances": "80l. messing allowance"},
    {"name": "W. C. George", "canonical_name": "George, W. C.", "given_names": "W. C.", "surname": "George", "position": "3rd Grade Clerk and Storekeeper", "department": "Government Vessels - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "F. D. Forbes", "canonical_name": "Forbes, F. D.", "given_names": "F. D.", "surname": "Forbes", "position": "4th Grade Clerk", "department": "Government Vessels - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "S. F. Fye", "canonical_name": "Fye, S. F.", "given_names": "S. F.", "surname": "Fye", "position": "4th Grade Clerk", "department": "Government Vessels - Gambia", "salary_min": 50, "salary_max": 80}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
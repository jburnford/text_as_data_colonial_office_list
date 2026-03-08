"""
Gambia Colonial Office List 1921 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1921

OFFICIALS = [
    {"name": "W. F. Crook", "canonical_name": "Crook, W. F.", "given_names": "W. F.", "surname": "Crook", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 720, "salary_max": 800, "per_diem": "10s. per diem when travelling"},
    {"name": "A. G. E. Sly", "canonical_name": "Sly, A. G. E.", "given_names": "A. G. E.", "surname": "Sly", "position": "Assistant Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 480, "salary_max": 600, "per_diem": "10s. per diem when travelling"},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "A. D. Sawyerr", "canonical_name": "Sawyerr, A. D.", "given_names": "A. D.", "surname": "Sawyerr", "position": "3rd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 60, "salary_max": 80},
    {"name": "W. A. V. Small", "canonical_name": "Small, W. A. V.", "given_names": "W. A. V.", "surname": "Small", "position": "3rd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 60, "salary_max": 80},
    {"name": "E. L. Gueritz", "canonical_name": "Gueritz, E. L.", "given_names": "E. L.", "surname": "Gueritz", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "T. R. King", "canonical_name": "King, T. R.", "given_names": "T. R.", "surname": "King", "position": "2nd Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "C. J. Thomas", "canonical_name": "Thomas, C. J.", "given_names": "C. J.", "surname": "Thomas", "position": "3rd Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "A. L. Speller", "canonical_name": "Speller, A. L.", "given_names": "A. L.", "surname": "Speller", "position": "Chief Engineer and Master", "department": "Government Vessels - Gambia", "salary_min": 480, "salary_max": 600, "duty_allowance": 80, "allowances": "80l. messing allowance"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Second Engineer", "department": "Government Vessels - Gambia", "salary_min": 450, "salary_max": 510, "allowances": "80l. messing allowance"},
    {"name": "W. C. George", "canonical_name": "George, W. C.", "given_names": "W. C.", "surname": "George", "position": "2nd Grade Clerk and Storekeeper", "department": "Government Vessels - Gambia", "salary_min": 90, "salary_max": 170}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
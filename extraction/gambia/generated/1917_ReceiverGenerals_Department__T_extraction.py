"""
Gambia Colonial Office List 1917 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1917

OFFICIALS = [
    {"name": "C. Gwyn", "canonical_name": "Gwyn, C.", "given_names": "C.", "surname": "Gwyn", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "J. Iles Lauder", "canonical_name": "Lauder, J. Iles", "given_names": "J. Iles", "surname": "Lauder", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "V. E. Johnson", "canonical_name": "Johnson, V. E.", "given_names": "V. E.", "surname": "Johnson", "position": "6th Grade Clerk", "department": "Receiver-General's Department - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "C. C. Johnson", "canonical_name": "Johnson, C. C.", "given_names": "C. C.", "surname": "Johnson", "position": "Chief Clerk and Cashier", "department": "Treasury Branch - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "P. Sowe", "canonical_name": "Sowe, P.", "given_names": "P.", "surname": "Sowe", "position": "1st Grade Clerk", "department": "Treasury Branch - Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "3rd Clerk", "department": "Treasury Branch - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "3rd Clerk", "department": "Treasury Branch - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "J. Jobe", "canonical_name": "Jobe, J.", "given_names": "J.", "surname": "Jobe", "position": "4th Clerk", "department": "Treasury Branch - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "5th Clerk", "department": "Treasury Branch - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "T. R. G. Roberts", "canonical_name": "Roberts, T. R. G.", "given_names": "T. R. G.", "surname": "Roberts", "position": "Apprentice", "department": "Treasury Branch - Gambia", "salary_min": 12, "salary_max": 12}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
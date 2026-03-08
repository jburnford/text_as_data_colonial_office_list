"""
Gambia Colonial Office List 1920 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1920

OFFICIALS = [
    {"name": "S. Gaye", "canonical_name": "Gaye, S.", "given_names": "S.", "surname": "Gaye", "position": "Caretaker", "department": "MacCarthy Square Board - Gambia", "salary_min": 48, "salary_max": 48},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Colonial Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 500, "salary_max": 500, "duty_allowance": 100, "per_diem": "2s. 3d. per diem"},
    {"name": "E. M. W. Williams", "canonical_name": "Williams, E. M. W.", "given_names": "E. M. W.", "surname": "Williams", "position": "Assistant Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 350, "salary_max": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk of Works and Supervisor of Telephones", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "P. G. Burrage", "canonical_name": "Burrage, P. G.", "given_names": "P. G.", "surname": "Burrage", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Accountant and Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 350},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Foreman of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 120, "salary_max": 150},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "S. O. Tebbs", "canonical_name": "Tebbs, S. O.", "given_names": "S. O.", "surname": "Tebbs", "position": "Timekeeper and Clerk (4th Grade)", "department": "Colonial Engineer's Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "A. R. Mason", "canonical_name": "Mason, A. R.", "given_names": "A. R.", "surname": "Mason", "position": "Chief Assistant Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "V. E. Johnson", "canonical_name": "Johnson, V. E.", "given_names": "V. E.", "surname": "Johnson", "position": "2nd Assistant Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "M. C. Mammah", "canonical_name": "Mammah, M. C.", "given_names": "M. C.", "surname": "Mammah", "position": "2nd Assistant Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "W. F. Crook", "canonical_name": "Crook, W. F.", "given_names": "W. F.", "surname": "Crook", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem"},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "A. D. Sawyer", "canonical_name": "Sawyer, A. D.", "given_names": "A. D.", "surname": "Sawyer", "position": "4th \" \" \" ", "department": "Land and Survey Department - Gambia", "salary_min": 50, "salary_max": 70}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
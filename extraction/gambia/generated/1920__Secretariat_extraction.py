"""
Gambia Colonial Office List 1920 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1920

OFFICIALS = [
    {"name": "H. Henniker Heaton", "canonical_name": "Heaton, H. Henniker", "given_names": "H. Henniker", "surname": "Heaton", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "A. C. Knollys", "canonical_name": "Knollys, A. C.", "given_names": "A. C.", "surname": "Knollys", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 50},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "Chief Clerk", "department": "Secretariat - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "2nd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "F. D. D. Roach", "canonical_name": "Roach, F. D. D.", "given_names": "F. D. D.", "surname": "Roach", "position": "2nd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. L. Danner", "canonical_name": "Danner, J. L.", "given_names": "J. L.", "surname": "Danner", "position": "5th Grade Clerks", "department": "Secretariat - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "W. F. Mahoney", "canonical_name": "Mahoney, W. F.", "given_names": "W. F.", "surname": "Mahoney", "position": "5th Grade Clerks", "department": "Secretariat - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "S. B. Haffner", "canonical_name": "Haffner, S. B.", "given_names": "S. B.", "surname": "Haffner", "position": "Chief Printer", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "Chief Compositor", "department": "Secretariat - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "M. C. Johnson", "canonical_name": "Johnson, M. C.", "given_names": "M. C.", "surname": "Johnson", "position": "1st Class Composers", "department": "Secretariat - Gambia", "salary_min": 60, "salary_max": 75},
    {"name": "O. D. Cummings", "canonical_name": "Cummings, O. D.", "given_names": "O. D.", "surname": "Cummings", "position": "1st Class Composers", "department": "Secretariat - Gambia", "salary_min": 60, "salary_max": 75},
    {"name": "V. A. John", "canonical_name": "John, V. A.", "given_names": "V. A.", "surname": "John", "position": "2nd Class Composers", "department": "Secretariat - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "R. J. Williams", "canonical_name": "Williams, R. J.", "given_names": "R. J.", "surname": "Williams", "position": "2nd Class Composers", "department": "Secretariat - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "E. See", "canonical_name": "See, E.", "given_names": "E.", "surname": "See", "position": "3rd Class Composers", "department": "Secretariat - Gambia", "salary_min": 30, "salary_max": 40},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
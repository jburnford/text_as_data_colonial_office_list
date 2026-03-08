"""
Gambia Colonial Office List 1920 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1920

OFFICIALS = [
    {"name": "C. D. Williams", "canonical_name": "Williams, C. D.", "given_names": "C. D.", "surname": "Williams", "position": "Chief Clerk", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. Gabbidon", "canonical_name": "Gabbidon, J.", "given_names": "J.", "surname": "Gabbidon", "position": "First Grade Clerk", "department": "Customs - The Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "E. A. Mackay", "canonical_name": "Mackay, E. A.", "given_names": "E. A.", "surname": "Mackay", "position": "Second Grade Clerk", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "Second Grade Clerk", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "S. W. Davis", "canonical_name": "Davis, S. W.", "given_names": "S. W.", "surname": "Davis", "position": "Second Grade Clerk", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "M. L. Davies", "canonical_name": "Davies, M. L.", "given_names": "M. L.", "surname": "Davies", "position": "Second Grade Clerk", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "G. D. Edwards", "canonical_name": "Edwards, G. D.", "given_names": "G. D.", "surname": "Edwards", "position": "Fourth Grade Clerk", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Fourth Grade Clerk", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sixth Grade Clerk", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "J. A. N'Jai Gomez", "canonical_name": "Gomez, J. A. N'Jai", "given_names": "J. A. N'Jai", "surname": "Gomez", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 190},
    {"name": "J. F. King", "canonical_name": "King, J. F.", "given_names": "J. F.", "surname": "King", "position": "Chief Landing Waiter and Locker", "department": "Customs - The Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "Landing Waiter, 1st Class", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "S. Jobe", "canonical_name": "Jobe, S.", "given_names": "S.", "surname": "Jobe", "position": "Landing Waiter, 2nd Class", "department": "Customs - The Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "E. W. Johnson", "canonical_name": "Johnson, E. W.", "given_names": "E. W.", "surname": "Johnson", "position": "Landing Waiter, 3rd Class", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "S. Senghore", "canonical_name": "Senghore, S.", "given_names": "S.", "surname": "Senghore", "position": "Landing Waiter, 3rd Class", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "J. Maxwell", "canonical_name": "Maxwell, J.", "given_names": "J.", "surname": "Maxwell", "position": "Landing Waiter, 3rd Class", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Landing Waiter, 4th Class", "department": "Customs - The Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Landing Waiter, 4th Class", "department": "Customs - The Gambia", "salary_min": 40, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
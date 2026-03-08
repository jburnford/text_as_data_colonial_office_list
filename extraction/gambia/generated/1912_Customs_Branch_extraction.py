"""
Gambia Colonial Office List 1912 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1912

OFFICIALS = [
    {"name": "S. J. Auber", "canonical_name": "Auber, S. J.", "given_names": "S. J.", "surname": "Auber", "position": "Chief Clerk and Cashier", "department": "Customs Branch - Gambia", "salary_min": 175, "salary_max": 200, "allowances": "50l. personal"},
    {"name": "J. A. Gomez", "canonical_name": "Gomez, J. A.", "given_names": "J. A.", "surname": "Gomez", "position": "First Clerk", "department": "Customs Branch - Gambia", "salary_min": 100, "salary_max": 125, "allowances": "12l. as Magazine Keeper"},
    {"name": "J. A. Monday", "canonical_name": "Monday, J. A.", "given_names": "J. A.", "surname": "Monday", "position": "Second Clerk", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Second Clerk", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "S. W. Davies", "canonical_name": "Davies, S. W.", "given_names": "S. W.", "surname": "Davies", "position": "Third Clerk", "department": "Customs Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. F. Leigh", "canonical_name": "Leigh, S. F.", "given_names": "S. F.", "surname": "Leigh", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs Branch - Gambia", "salary_min": 175, "salary_max": 200},
    {"name": "J. C. Chapman", "canonical_name": "Chapman, J. C.", "given_names": "J. C.", "surname": "Chapman", "position": "Chief Landing Waiter and Locker", "department": "Customs Branch - Gambia", "salary_min": 125, "salary_max": 150},
    {"name": "J. E. King", "canonical_name": "King, J. E.", "given_names": "J. E.", "surname": "King", "position": "First Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "S. C. Richards", "canonical_name": "Richards, S. C.", "given_names": "S. C.", "surname": "Richards", "position": "First Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "Second Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "T. R. King", "canonical_name": "King, T. R.", "given_names": "T. R.", "surname": "King", "position": "Second Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "C. Porquet", "canonical_name": "Porquet, C.", "given_names": "C.", "surname": "Porquet", "position": "Third Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. Senghore", "canonical_name": "Senghore, S.", "given_names": "S.", "surname": "Senghore", "position": "Third Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 30, "salary_max": 40},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
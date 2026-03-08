"""
Gambia Colonial Office List 1905 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1905

OFFICIALS = [
    {"name": "T. E. Peirce", "canonical_name": "Peirce, T. E.", "given_names": "T. E.", "surname": "Peirce", "position": "Collector of Customs", "department": "Customs - The Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 60},
    {"name": "S. J. Auber", "canonical_name": "Auber, S. J.", "given_names": "S. J.", "surname": "Auber", "position": "Chief Clerk and Cashier", "department": "Customs - The Gambia", "salary_min": 175, "salary_max": 200, "allowances": "20l. personal"},
    {"name": "J. A. Gomez", "canonical_name": "Gomez, J. A.", "given_names": "J. A.", "surname": "Gomez", "position": "Second Clerk", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 65, "allowances": "12l. as Magazine Keeper"},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Third Clerk", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. F. Leigh", "canonical_name": "Leigh, S. F.", "given_names": "S. F.", "surname": "Leigh", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs - The Gambia", "salary_min": 175, "salary_max": 200},
    {"name": "J. C. Chapman", "canonical_name": "Chapman, J. C.", "given_names": "J. C.", "surname": "Chapman", "position": "Chief Landing Waiter and Locker", "department": "Customs - The Gambia", "salary_min": 125, "salary_max": 150},
    {"name": "J. E. King", "canonical_name": "King, J. E.", "given_names": "J. E.", "surname": "King", "position": "First Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "J. T. Monday", "canonical_name": "Monday, J. T.", "given_names": "J. T.", "surname": "Monday", "position": "First Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "T. B. Wright", "canonical_name": "Wright, T. B.", "given_names": "T. B.", "surname": "Wright", "position": "Second Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "S. C. Richards", "canonical_name": "Richards, S. C.", "given_names": "S. C.", "surname": "Richards", "position": "Second Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "Third Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "D. D. Peters", "canonical_name": "Peters, D. D.", "given_names": "D. D.", "surname": "Peters", "position": "Third Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
]

for i in range(4):
    OFFICIALS.append({"name": "Apprentice", "canonical_name": "Apprentice, ", "surname": "Apprentice", "position": "Apprentice", "department": "Customs - The Gambia", "salary_min": 12, "salary_max": 12})

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
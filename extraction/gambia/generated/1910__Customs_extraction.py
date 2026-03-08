"""
Gambia Colonial Office List 1910 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1910

OFFICIALS = [
    {"name": "Hon. T. E. Peirce", "canonical_name": "Peirce, T. E.", "given_names": "T. E.", "surname": "Peirce", "position": "Collector of Customs", "department": "Customs - The Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 60},
    {"name": "S. J. Auber", "canonical_name": "Auber, S. J.", "given_names": "S. J.", "surname": "Auber", "position": "Chief Clerk and Cashier", "department": "Customs - The Gambia", "salary_min": 175, "salary_max": 200, "allowances": "20l. personal"},
    {"name": "J. A. Gomer", "canonical_name": "Gomer, J. A.", "given_names": "J. A.", "surname": "Gomer", "position": "Second Clerk", "department": "Customs - The Gambia", "salary_min": 75, "salary_max": 100, "allowances": "12l. as Magazine Keeper"},
    {"name": "L. M. Joof", "canonical_name": "Joof, L. M.", "given_names": "L. M.", "surname": "Joof", "position": "Third Clerk", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. F. Leigh", "canonical_name": "Leigh, S. F.", "given_names": "S. F.", "surname": "Leigh", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs - The Gambia", "salary_min": 175, "salary_max": 200},
    {"name": "J. C. Chapman", "canonical_name": "Chapman, J. C.", "given_names": "J. C.", "surname": "Chapman", "position": "Chief Landing Waiter and Locker", "department": "Customs - The Gambia", "salary_min": 125, "salary_max": 150},
    {"name": "J. R. King", "canonical_name": "King, J. R.", "given_names": "J. R.", "surname": "King", "position": "First Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "J. T. Monday", "canonical_name": "Monday, J. T.", "given_names": "J. T.", "surname": "Monday", "position": "First Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "S. C. Richards", "canonical_name": "Richards, S. C.", "given_names": "S. C.", "surname": "Richards", "position": "Second Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "S. P. Gibbs", "canonical_name": "Gibbs, S. P.", "given_names": "S. P.", "surname": "Gibbs", "position": "Second Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "C. Porquet", "canonical_name": "Porquet, C.", "given_names": "C.", "surname": "Porquet", "position": "Third Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "Third Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
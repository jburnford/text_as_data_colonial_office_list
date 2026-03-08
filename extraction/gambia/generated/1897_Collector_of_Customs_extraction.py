"""
Gambia Colonial Office List 1897 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1897

OFFICIALS = [
    {"name": "S. J. Auber", "canonical_name": "Auber, S. J.", "given_names": "S. J.", "surname": "Auber", "position": "Chief Clerk and Cashier", "department": "Customs - Gambia", "salary_min": 175, "salary_max": 175},
    {"name": "J. C. Chapman", "canonical_name": "Chapman, J. C.", "given_names": "J. C.", "surname": "Chapman", "position": "2nd Clerk, Customs", "department": "Customs - Gambia", "salary_min": 65, "salary_max": 65},
    {"name": "J. Douglass", "canonical_name": "Douglass, J.", "given_names": "J.", "surname": "Douglass", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs - Gambia", "salary_min": 200, "salary_max": 200, "allowances": "25L commutation of fees"},
    {"name": "J. N. Wilhelm", "canonical_name": "Wilhelm, J. N.", "given_names": "J. N.", "surname": "Wilhelm", "position": "Senior Landing Waiter and Locker", "department": "Customs - Gambia", "salary_min": 95, "salary_max": 95},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "2nd Landing Waiter and Locker", "department": "Customs - Gambia", "salary_min": 55, "salary_max": 55},
    {"name": "J. G. Josef", "canonical_name": "Josef, J. G.", "given_names": "J. G.", "surname": "Josef", "position": "3rd Landing Waiter", "department": "Customs - Gambia", "salary_min": 30, "salary_max": 30},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
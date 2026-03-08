"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "H. S. Bascom", "canonical_name": "Bascom, H. S.", "given_names": "H. S.", "surname": "Bascom", "position": "Collector of Customs", "department": "Customs - Gambia", "salary_min": 400, "salary_max": 400, "allowances": "quarters", "duty_allowance": 60},
    {"name": "S. J. Aubert", "canonical_name": "Aubert, S. J.", "given_names": "S. J.", "surname": "Aubert", "position": "Clerk", "department": "Customs - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "J. C. Chapman", "canonical_name": "Chapman, J. C.", "given_names": "J. C.", "surname": "Chapman", "position": "2nd Clerk, Customs", "department": "Customs - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "J. Dougan", "canonical_name": "Dougan, J.", "given_names": "J.", "surname": "Dougan", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs - Gambia", "salary_min": 200, "salary_max": 200, "allowances": "25l. commutation of fees"},
    {"name": "J. N. C. Wilhelm", "canonical_name": "Wilhelm, J. N. C.", "given_names": "J. N. C.", "surname": "Wilhelm", "position": "Senior Landing Waiter and Locker", "department": "Customs - Gambia", "salary_min": 90, "salary_max": 90},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "2nd Landing Waiter and Locker", "department": "Customs - Gambia"},
    {"name": "J. G. McCarthy", "canonical_name": "McCarthy, J. G.", "given_names": "J. G.", "surname": "McCarthy", "position": "3rd Landing Waiter", "department": "Customs - Gambia", "salary_min": 30, "salary_max": 30},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
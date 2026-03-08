"""
Gambia Colonial Office List 1889 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1889

OFFICIALS = [
    {"name": "H. H. Leo", "canonical_name": "Leo, H. H.", "given_names": "H. H.", "surname": "Leo", "position": "Collector of Customs", "department": "Customs - The Gambia", "salary_min": 300, "salary_max": 300, "allowances": "quarters, fees", "duty_allowance": 60},
    {"name": "S. J. Auber", "canonical_name": "Auber, S. J.", "given_names": "S. J.", "surname": "Auber", "position": "Clerk", "department": "Customs - The Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "J. Dougan", "canonical_name": "Dougan, J.", "given_names": "J.", "surname": "Dougan", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs - The Gambia", "salary_min": 200, "salary_max": 200},
    {"name": "W. J. Davis", "canonical_name": "Davis, W. J.", "given_names": "W. J.", "surname": "Davis", "position": "Landing Waiter and Locker", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 90},
    {"name": "J. N. C. Wilhelm", "canonical_name": "Wilhelm, J. N. C.", "given_names": "J. N. C.", "surname": "Wilhelm", "position": "2nd Landing Waiter and Locker", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
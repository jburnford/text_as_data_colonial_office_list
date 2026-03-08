"""
Gambia Colonial Office List 1936 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1936

OFFICIALS = [
    {"name": "F. W. Hall", "canonical_name": "Hall, F. W.", "given_names": "F. W.", "surname": "Hall", "position": "Senior Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 720, "duty_allowance": 72},
    {"name": "J. Pirie", "canonical_name": "Pirie, J.", "given_names": "J.", "surname": "Pirie", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "T. P. L. Molloy", "canonical_name": "Molloy, T. P. L.", "given_names": "T. P. L.", "surname": "Molloy", "position": "Officer Commanding", "department": "Royal West African Frontier Force - Gambia", "salary_min": 750, "salary_max": 750, "duty_allowance": 55, "military_rank": "Major"},
    {"name": "O. J. Body", "canonical_name": "Body, O. J.", "given_names": "O. J.", "surname": "Body", "position": "Lieutenant", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Lieutenant", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1939 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1939

OFFICIALS = [
    {"name": "F. W. Hall", "canonical_name": "Hall, F. W.", "given_names": "F. W.", "surname": "Hall", "position": "Senior Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 690, "salary_max": 840, "duty_allowance": 72},
    {"name": "L. H. Saunders", "canonical_name": "Saunders, L. H.", "given_names": "L. H.", "surname": "Saunders", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 450, "salary_max": 630},
    {"name": "J. D. Tallantire", "canonical_name": "Tallantire, J. D.", "given_names": "J. D.", "surname": "Tallantire", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 450, "salary_max": 630},
    {"name": "T. A. Davis", "canonical_name": "Davis, T. A.", "given_names": "T. A.", "surname": "Davis", "position": "Officer Commanding", "department": "Royal West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "duty_allowance": 55, "military_rank": "Captain"},
    {"name": "G. W. York", "canonical_name": "York, G. W.", "given_names": "G. W.", "surname": "York", "position": "Lieutenant", "department": "Royal West African Frontier Force - Gambia", "salary_min": 510, "salary_max": 510, "military_rank": "Lieutenant"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
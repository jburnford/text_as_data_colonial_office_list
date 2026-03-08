"""
Gambia Colonial Office List 1950 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1950

OFFICIALS = [
    {"name": "J. Hill", "canonical_name": "Hill, J.", "given_names": "J.", "surname": "Hill", "position": "Controller of Supplies", "department": "Supplies and Minor Industries - Gambia", "salary_scale": "C"},
    {"name": "R. J. Midwinter", "canonical_name": "Midwinter, R. J.", "given_names": "R. J.", "surname": "Midwinter", "position": "Assistant Controller of Supplies", "department": "Supplies and Minor Industries - Gambia", "salary_scale": "C"},
    {"name": "W. Brown", "canonical_name": "Brown, W.", "given_names": "W.", "surname": "Brown", "position": "Master Fisherman", "department": "Supplies and Minor Industries - Gambia", "salary_min": 650, "salary_max": 650},
    {"name": "W. A. Small", "canonical_name": "Small, W. A.", "given_names": "W. A.", "surname": "Small", "position": "Surveyor", "department": "Survey - Gambia", "salary_scale": "A"},
    {"name": "A. Fulton", "canonical_name": "Fulton, A.", "given_names": "A.", "surname": "Fulton", "position": "Director", "department": "Veterinary - Gambia", "salary_min": 1150, "salary_max": 1150, "expatriation_pay": 350},
    {"name": "A. A. Wilson", "canonical_name": "Wilson, A. A.", "given_names": "A. A.", "surname": "Wilson", "position": "Laboratory Superintendent", "department": "Veterinary - Gambia", "salary_scale": "C"},
    {"name": "D. F. Hamilton", "canonical_name": "Hamilton, D. F.", "given_names": "D. F.", "surname": "Hamilton", "position": "Veterinary Officer", "department": "Veterinary - Gambia", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
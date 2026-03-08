"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "A. L. Speller", "canonical_name": "Speller, A. L.", "given_names": "A. L.", "surname": "Speller", "position": "Chief Engineer and Master", "department": "Government Vessels - Gambia", "salary_min": 300, "salary_max": 360, "duty_allowance": 50, "allowances": "50l. messing allowance"},
    {"name": "H. Lawson", "canonical_name": "Lawson, H.", "given_names": "H.", "surname": "Lawson", "position": "Second Engineer", "department": "Government Vessels - Gambia", "salary_min": 200, "salary_max": 250, "allowances": "50l. messing allowance"},
    {"name": "W. C. George", "canonical_name": "George, W. C.", "given_names": "W. C.", "surname": "George", "position": "3rd Grade Clerk and Storekeeper", "department": "Government Vessels - Gambia", "salary_min": 75, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
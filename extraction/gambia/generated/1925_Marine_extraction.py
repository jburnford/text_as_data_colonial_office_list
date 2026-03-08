"""
Gambia Colonial Office List 1925 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1925

OFFICIALS = [
    {"name": "A. D. Steele", "canonical_name": "Steele, A. D.", "given_names": "A. D.", "surname": "Steele", "position": "Harbour Master and Marine Superintendent", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720, "duty_allowance": 100, "allowances": "80l. messing allowance"},
    {"name": "J. M. Simpson", "canonical_name": "Simpson, J. M.", "given_names": "J. M.", "surname": "Simpson", "position": "Chief Engineer", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 510, "allowances": "80l. messing allowance"},
    {"name": "J. B. Fathers", "canonical_name": "Fathers, J. B.", "given_names": "J. B.", "surname": "Fathers", "position": "Assistant Engineer", "department": "Marine - Gambia", "salary_min": 450, "salary_max": 450, "allowances": "80l. messing allowance"},
    {"name": "W. C. George", "canonical_name": "George, W. C.", "given_names": "W. C.", "surname": "George", "position": "3rd Grade Clerk", "department": "Marine - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "S. C. Richards", "canonical_name": "Richards, S. C.", "given_names": "S. C.", "surname": "Richards", "position": "Purser and Shipping Clerk", "department": "Marine - Gambia", "salary_min": 100, "salary_max": 136},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
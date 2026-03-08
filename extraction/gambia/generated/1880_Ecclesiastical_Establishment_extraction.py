"""
Gambia Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1880

OFFICIALS = [
    {"name": "Rev. George Nicol", "canonical_name": "Nicol, George", "given_names": "George", "surname": "Nicol", "position": "Colonial Chaplain", "department": "Ecclesiastical Establishment - Gambia", "salary_min": 450, "salary_max": 450, "allowances": "forage allowances"},
    {"name": "J. C. Chapman", "canonical_name": "Chapman, J. C.", "given_names": "J. C.", "surname": "Chapman", "position": "Clerk and Organist", "department": "Ecclesiastical Establishment - Gambia", "salary_min": 20, "salary_max": 20}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
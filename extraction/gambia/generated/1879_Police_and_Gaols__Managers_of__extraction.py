"""
Gambia Colonial Office List 1879 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1879

OFFICIALS = [
    {"name": "J. Johns", "canonical_name": "Johns, J.", "given_names": "J.", "surname": "Johns", "position": "Gaoler", "department": "Police and Gaols - Gambia", "salary_min": 75, "salary_max": 75},
    {"name": "E. A. M. Smith", "canonical_name": "Smith, E. A. M.", "given_names": "E. A. M.", "surname": "Smith", "position": "McCarthy's Island", "department": "Managers of Districts - Gambia", "salary_min": 300, "salary_max": 300, "acting_status": "acting", "allowances": "residence and forage allowance", "location": "McCarthy's Island"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "British Combo", "department": "Managers of Districts - Gambia", "salary_min": 150, "salary_max": 150, "allowances": "ditto", "location": "British Combo"},
    {"name": "Rev. George Nicol", "canonical_name": "Nicol, George", "given_names": "George", "surname": "Nicol", "position": "Colonial Chaplain", "department": "Ecclesiastical Establishment - Gambia", "salary_min": 450, "salary_max": 450, "allowances": "and forage allowances"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk and Organist", "department": "Ecclesiastical Establishment - Gambia", "salary_min": 20, "salary_max": 20},
    {"name": "J. Basson", "canonical_name": "Basson, J.", "given_names": "J.", "surname": "Basson", "position": "Keeper of Cemetery", "department": "Ecclesiastical Establishment - Gambia", "salary_min": 25, "salary_max": 25}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
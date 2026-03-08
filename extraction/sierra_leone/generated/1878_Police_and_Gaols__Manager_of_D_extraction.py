"""
Sierra Leone Colonial Office List 1878 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1878

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Superintendent of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 100, "salary_max": 100, "allowances": "forage allowances"},
    {"name": "Wm. Hawes", "canonical_name": "Hawes, William", "given_names": "Wm.", "surname": "Hawes", "position": "Gaoler", "department": "Police and Gaols - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "Lucius Smith", "canonical_name": "Smith, Lucius", "given_names": "Lucius", "surname": "Smith", "position": "Manager of Districts", "department": "Manager of Districts - Sierra Leone", "salary_min": 300, "salary_max": 300, "location": "McCarthy's Island", "allowances": "residence and forage allowance"},
    {"name": "E. A. M. Smith", "canonical_name": "Smith, E. A. M.", "given_names": "E. A. M.", "surname": "Smith", "position": "Manager of Districts", "department": "Manager of Districts - Sierra Leone", "salary_min": 150, "salary_max": 150, "location": "British Combo", "allowances": "ditto"},
    {"name": "Rev. George Nicol", "canonical_name": "Nicol, George", "given_names": "George", "surname": "Nicol", "position": "Colonial Chaplain", "department": "Ecclesiastical Establishment - Sierra Leone", "salary_min": 450, "salary_max": 450, "allowances": "and forage allowances"},
    {"name": "J. B. Moore", "canonical_name": "Moore, J. B.", "given_names": "J. B.", "surname": "Moore", "position": "Clerk and Organist", "department": "Ecclesiastical Establishment - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "J. Basson", "canonical_name": "Basson, J.", "given_names": "J.", "surname": "Basson", "position": "Keeper of Cemetery", "department": "Ecclesiastical Establishment - Sierra Leone", "salary_min": 25, "salary_max": 25},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "E. A. M. Smith", "canonical_name": "Smith, E. A. M.", "given_names": "E. A. M.", "surname": "Smith", "position": "Manager of Districts", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250, "location": "McCarthy's Island", "per_diem": "2s. 3d. per diem"},
    {"name": "J. W. Pearce", "canonical_name": "Pearce, J. W.", "given_names": "J. W.", "surname": "Pearce", "position": "Manager of Districts", "department": "Civil Establishment - Gambia", "salary_min": 100, "salary_max": 100, "location": "British Combo", "per_diem": "2s. 3d. per diem"},
    {"name": "Rev. George Nicol", "canonical_name": "Nicol, George", "given_names": "George", "surname": "Nicol", "position": "Colonial Chaplain", "department": "Ecclesiastical - Gambia", "salary_min": 450, "salary_max": 450, "per_diem": "2s. 3d. per day forage allowance"},
    {"name": "D. Davis", "canonical_name": "Davis, D.", "given_names": "D.", "surname": "Davis", "position": "Clerk and Organist", "department": "Ecclesiastical - Gambia", "salary_min": 20, "salary_max": 20, "acting_status": "acting"},
    {"name": "T. Crey", "canonical_name": "Crey, T.", "given_names": "T.", "surname": "Crey", "position": "Keeper of Cemetery", "department": "Ecclesiastical - Gambia", "salary_min": 25, "salary_max": 25}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "O. J. Thomas", "canonical_name": "Thomas, O. J.", "given_names": "O. J.", "surname": "Thomas", "position": "Clerk to ditto", "department": "Port and Marine Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "J. N. Compton", "canonical_name": "Compton, J. N.", "given_names": "J. N.", "surname": "Compton", "position": "Commander", "department": "Port and Marine Department - Sierra Leone", "salary_min": 384, "salary_max": 384, "military_rank": "Capt."},
    {"name": "A. Forrester", "canonical_name": "Forrester, A.", "given_names": "A.", "surname": "Forrester", "position": "Chief Engineer", "department": "Port and Marine Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "R. Begg", "canonical_name": "Begg, R.", "given_names": "R.", "surname": "Begg", "position": "2nd Engineer", "department": "Port and Marine Department - Sierra Leone", "salary_min": 252, "salary_max": 252},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
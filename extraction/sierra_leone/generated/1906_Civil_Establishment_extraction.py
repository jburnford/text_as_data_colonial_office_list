"""
Sierra Leone Colonial Office List 1906 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1906

OFFICIALS = [
    {"name": "Leslie Probyn", "canonical_name": "Probyn, Leslie", "given_names": None, "surname": "Probyn", "position": "Governor, Commander-in-Chief, and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 2000, "salary_max": 2000, "allowances": "500l. entertaining allowance", "honors": ["C.M.G."]},
    {"name": "E. R. Tomlinson", "canonical_name": "Tomlinson, E. R.", "given_names": "E. R.", "surname": "Tomlinson", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 200, "salary_max": 200, "military_rank": "Capt."},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Governor's Chief Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 100, "salary_max": 180},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "1st Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 100, "salary_max": 130, "qualifications": ["B.A."]},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "2nd Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1907 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1907

OFFICIALS = [
    {"name": "Leslie Probyn", "canonical_name": "Probyn, Leslie", "given_names": None, "surname": "Probyn", "position": "Governor, Commander-in-Chief, and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 2500, "salary_max": 2500, "honors": ["C.M.G."], "allowances": "500l. entertaining allowance"},
    {"name": "E. R. Tomlinson", "canonical_name": "Tomlinson, E. R.", "given_names": "E. R.", "surname": "Tomlinson", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 200, "salary_max": 200, "military_rank": "Capt."},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Governor's Chief Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 100, "salary_max": 180},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "1st Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 120, "salary_max": 150, "qualifications": ["B.A."]},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "2nd Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "G. B. Haddon Smith", "canonical_name": "Smith, G. B. Haddon", "given_names": "G. B.", "surname": "Smith", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 800, "salary_max": 800, "honors": ["C.M.G."], "duty_allowance": 160},
    {"name": "E. E. Evelyn", "canonical_name": "Evelyn, E. E.", "given_names": "E. E.", "surname": "Evelyn", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "A. Farrar", "canonical_name": "Farrar, A.", "given_names": "A.", "surname": "Farrar", "position": "2nd Asst. Col. Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. W. M. Nylander", "canonical_name": "Nylander, A. W. M.", "given_names": "A. W. M.", "surname": "Nylander", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "D. W. Carroll", "canonical_name": "Carroll, D. W.", "given_names": "D. W.", "surname": "Carroll", "position": "1st Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "2nd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 115, "salary_max": 140},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "3rd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 110, "salary_max": 130},
    {"name": "Hadir-u-deen", "canonical_name": "Hadir-u-deen", "given_names": None, "surname": "Hadir-u-deen", "position": "4th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
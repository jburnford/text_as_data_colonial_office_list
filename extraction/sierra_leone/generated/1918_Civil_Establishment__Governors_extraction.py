"""
Sierra Leone Colonial Office List 1918 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1918

OFFICIALS = [
    {"name": "R. J. Wilkinson", "canonical_name": "Wilkinson, R. J.", "given_names": "R. J.", "surname": "Wilkinson", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 1000, "honors": ["C.M.G."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Chief Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "T. A. Thompson", "canonical_name": "Thompson, T. A.", "given_names": "T. A.", "surname": "Thompson", "position": "Second Grade Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 130, "salary_max": 160}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
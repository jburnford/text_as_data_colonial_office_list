"""
Sierra Leone Colonial Office List 1913 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1913

OFFICIALS = [
    {"name": "Sir Edward Marsh Merewether", "canonical_name": "Merewether, Edward Marsh", "given_names": "Edward Marsh", "surname": "Merewether", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 1000, "honors": ["K.C.V.O.", "C.M.G."]},
    {"name": "A. Ross Hume", "canonical_name": "Hume, A. Ross", "given_names": "A. Ross", "surname": "Hume", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 300, "salary_max": 300, "military_rank": "Lieutenant"},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Chief Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "T. A. Thompson", "canonical_name": "Thompson, T. A.", "given_names": "T. A.", "surname": "Thompson", "position": "Second Grade Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 130, "salary_max": 160}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
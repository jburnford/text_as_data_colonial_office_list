"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "Sir J. A. Byrne", "canonical_name": "Byrne, J. A.", "given_names": "J. A.", "surname": "Byrne", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G.", "K.B.E.", "C.B."], "military_rank": "Brigadier-General"},
    {"name": "H. E. Allen", "canonical_name": "Allen, H. E.", "given_names": "H. E.", "surname": "Allen", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 450, "salary_max": 450, "military_rank": "Major"},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "First Grade Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 210, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1939 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1939

OFFICIALS = [
    {"name": "Sir Douglas Jardine", "canonical_name": "Jardine, Douglas", "given_names": "Douglas", "surname": "Jardine", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G.", "O.B.E."]},
    {"name": "T. G. Fitzgerald", "canonical_name": "Fitzgerald, T. G.", "given_names": "T. G.", "surname": "Fitzgerald", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 450, "salary_max": 450}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
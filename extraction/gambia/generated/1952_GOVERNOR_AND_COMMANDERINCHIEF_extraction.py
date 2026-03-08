"""
Gambia Colonial Office List 1952 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1952

OFFICIALS = [
    {"name": "Sir Percy Wyn Harris", "canonical_name": "Harris, Percy Wyn", "given_names": "Percy Wyn", "surname": "Harris", "position": "Governor and Commander-in-Chief", "department": "Governor's Office - Gambia", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G.", "M.B.E."]},
    {"name": "Miss D. Thrasher", "canonical_name": "Thrasher, D.", "given_names": "D.", "surname": "Thrasher", "position": "Private Secretary", "department": "Governor's Office - Gambia", "salary_min": 415, "salary_max": 415}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
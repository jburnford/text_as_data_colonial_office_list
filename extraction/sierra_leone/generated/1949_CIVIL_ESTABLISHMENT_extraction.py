"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "Sir George Beresford-Stooke", "canonical_name": "Beresford-Stooke, George", "surname": "Beresford-Stooke", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor and Personal Staff - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G."]},
    {"name": "P. F. S. King", "canonical_name": "King, P. F. S.", "given_names": "P. F. S.", "surname": "King", "position": "Private Secretary and Aide-de-Camp", "department": "Governor and Personal Staff - Sierra Leone", "salary_min": 415, "military_rank": "Lieut.-Commander"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
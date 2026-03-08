"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "W. C. Cates", "canonical_name": "Cates, W. C.", "given_names": "W. C.", "surname": "Cates", "position": "Clerk of Courts", "department": "Judicial - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "S. C. King", "canonical_name": "King, S. C.", "given_names": "S. C.", "surname": "King", "position": "Assistant Clerk of Courts", "department": "Judicial - Gambia", "salary_min": 75, "salary_max": 75},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
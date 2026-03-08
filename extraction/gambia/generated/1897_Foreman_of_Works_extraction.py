"""
Gambia Colonial Office List 1897 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1897

OFFICIALS = [
    {"name": "T. J. Carow Clark", "canonical_name": "Clark, T. J. Carow", "given_names": "T. J. Carow", "surname": "Clark", "position": "Foreman of Works", "department": "Public Works - Gambia", "salary_min": 65, "salary_max": 65}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
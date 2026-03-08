"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "M. J. W. Rockes", "canonical_name": "Rockes, M. J. W.", "given_names": "M. J. W.", "surname": "Rockes", "position": "Gaoler", "department": "Civil Establishment - Gambia", "salary_min": 120, "salary_max": 120},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "M. S. Smith", "canonical_name": "Smith, M. S.", "given_names": "M. S.", "surname": "Smith", "position": "Superintendent", "department": "Water Police - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "W. Mills", "canonical_name": "Mills, W.", "given_names": "W.", "surname": "Mills", "position": "Sub-Inspector", "department": "Water Police - Gambia", "salary_min": 180, "salary_max": 180},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
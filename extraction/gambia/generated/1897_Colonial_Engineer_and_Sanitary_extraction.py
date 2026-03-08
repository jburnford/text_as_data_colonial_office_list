"""
Gambia Colonial Office List 1897 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1897

OFFICIALS = [
    {"name": "Mr. Reeve", "canonical_name": "Reeve, Mr.", "surname": "Reeve", "position": "Colonial Engineer and Sanitary Inspector", "department": "Public Works - Gambia", "salary_min": 500, "salary_max": 500, "allowances": "and quarters, or 50L for rent"},
    {"name": "G. M. Hig", "canonical_name": "Hig, G. M.", "given_names": "G. M.", "surname": "Hig", "position": "Foreman of Works", "department": "Public Works - Gambia", "salary_min": 70, "salary_max": 70}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
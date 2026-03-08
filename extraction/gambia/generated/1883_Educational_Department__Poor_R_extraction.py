"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "C. H. Clifton", "canonical_name": "Clifton, C. H.", "given_names": "C. H.", "surname": "Clifton", "position": "Secretary to Central Board", "department": "Educational Department - Gambia", "salary_min": 220, "salary_max": 220},
    {"name": "W. Adkinson", "canonical_name": "Adkinson, W.", "given_names": "W.", "surname": "Adkinson", "position": "Inspector of Schools", "department": "Educational Department - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "allowance 100l."},
    {"name": "W. Dale", "canonical_name": "Dale, W.", "given_names": "W.", "surname": "Dale", "position": "Superintendent of Immigrants, Poor Houses, and Charitable Institutions", "department": "Poor Relief Department - Gambia", "salary_min": 250, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
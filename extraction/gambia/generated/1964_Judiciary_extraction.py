"""
Gambia Colonial Office List 1964 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1964

OFFICIALS = [
    {"name": "J. A. L. Wischam", "canonical_name": "Wischam, J. A. L.", "given_names": "J. A. L.", "surname": "Wischam", "position": "Chief Justice", "department": "Judiciary - Gambia"},
    {"name": "C. G. Ames", "canonical_name": "Ames, C. G.", "given_names": "C. G.", "surname": "Ames", "position": "President, Gambia Court of Appeal", "department": "Judiciary - Gambia"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
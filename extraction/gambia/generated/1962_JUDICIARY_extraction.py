"""
Gambia Colonial Office List 1962 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1962

OFFICIALS = [
    {"name": "J. A. L. Wiseham", "canonical_name": "Wiseham, J. A. L.", "given_names": "J. A. L.", "surname": "Wiseham", "position": "Chief Justice", "department": "Judiciary - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
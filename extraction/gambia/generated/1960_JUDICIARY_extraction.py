"""
Gambia Colonial Office List 1960 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1960

OFFICIALS = [
    {"name": "J. A. L. Wiseham", "canonical_name": "Wiseham, J. A. L.", "given_names": "J. A. L.", "surname": "Wiseham", "position": "Chief Justice", "department": "Judicial - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
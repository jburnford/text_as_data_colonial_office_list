"""
Gambia Colonial Office List 1964 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1964

OFFICIALS = [
    {"name": "A. M. Gregory", "canonical_name": "Gregory, A. M.", "given_names": "A. M.", "surname": "Gregory", "position": "Secretary to Ministry and Director of Education", "department": "Ministry of Education - Gambia", "honors": ["O.B.E."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
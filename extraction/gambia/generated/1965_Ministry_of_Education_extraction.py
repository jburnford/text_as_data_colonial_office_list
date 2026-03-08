"""
Gambia Colonial Office List 1965 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1965

OFFICIALS = [
    {"name": "S. H. M. Jones", "canonical_name": "Jones, S. H. M.", "given_names": "S. H. M.", "surname": "Jones", "position": "Secretary to Ministry and Director of Education", "department": "Ministry of Education - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
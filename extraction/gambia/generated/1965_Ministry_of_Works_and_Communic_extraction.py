"""
Gambia Colonial Office List 1965 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1965

OFFICIALS = [
    {"name": "I. G. Coghill", "canonical_name": "Coghill, I. G.", "given_names": "I. G.", "surname": "Coghill", "position": "Secretary", "department": "Ministry of Works and Communications - Gambia"},
    {"name": "D. M. Sowe", "canonical_name": "Sowe, D. M.", "given_names": "D. M.", "surname": "Sowe", "position": "Director of Public Works and Controller of Civil Aviation", "department": "Ministry of Works and Communications - Gambia"},
    {"name": "L. W. H. Dunster", "canonical_name": "Dunster, L. W. H.", "given_names": "L. W. H.", "surname": "Dunster", "position": "Director of Marine", "department": "Ministry of Works and Communications - Gambia"},
    {"name": "C. J. W. Lusack", "canonical_name": "Lusack, C. J. W.", "given_names": "C. J. W.", "surname": "Lusack", "position": "Manager, Electricity Services", "department": "Ministry of Works and Communications - Gambia"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
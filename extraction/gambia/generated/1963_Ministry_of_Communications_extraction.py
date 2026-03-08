"""
Gambia Colonial Office List 1963 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1963

OFFICIALS = [
    {"name": "S. G. Bruce-Oliver", "canonical_name": "Bruce-Oliver, S. G.", "given_names": "S. G.", "surname": "Bruce-Oliver", "position": "Secretary to Ministry", "department": "Ministry of Communications - Gambia"},
    {"name": "G. H. Cunningham", "canonical_name": "Cunningham, G. H.", "given_names": "G. H.", "surname": "Cunningham", "position": "Director of Marine", "department": "Ministry of Communications - Gambia", "honors": ["M.V.O.", "M.B.E."], "military_rank": "Lt. Comdr."},
    {"name": "A. J. Senghore", "canonical_name": "Senghore, A. J.", "given_names": "A. J.", "surname": "Senghore", "position": "Postmaster General", "department": "Ministry of Communications - Gambia"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1965 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1965

OFFICIALS = [
    {"name": "S. G. Trees", "canonical_name": "Trees, S. G.", "given_names": "S. G.", "surname": "Trees", "position": "Secretary", "department": "Ministry of Agriculture - Gambia", "honors": ["M.V.O."]},
    {"name": "H. Davidson", "canonical_name": "Davidson, H.", "given_names": "H.", "surname": "Davidson", "position": "Director of Agriculture", "department": "Ministry of Agriculture - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Principal Veterinary Officer", "department": "Ministry of Agriculture - Gambia"},
    {"name": "A. L. Macintosh", "canonical_name": "Macintosh, A. L.", "given_names": "A. L.", "surname": "Macintosh", "position": "Registrar, Co-operative Societies", "department": "Ministry of Agriculture - Gambia", "honors": ["M.B.E."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
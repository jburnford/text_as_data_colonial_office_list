"""
Gambia Colonial Office List 1963 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1963

OFFICIALS = [
    {"name": "S. G. Trees", "canonical_name": "Trees, S. G.", "given_names": "S. G.", "surname": "Trees", "position": "Secretary to Ministry", "department": "Ministry of Agriculture - Gambia", "honors": ["M.V.O."]},
    {"name": "J. A. Austin", "canonical_name": "Austin, J. A.", "given_names": "J. A.", "surname": "Austin", "position": "Director of Agriculture", "department": "Ministry of Agriculture - Gambia", "honors": ["O.B.E."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Principal Veterinary Officer", "department": "Ministry of Agriculture - Gambia"},
    {"name": "A. L. Mackintosh", "canonical_name": "Mackintosh, A. L.", "given_names": "A. L.", "surname": "Mackintosh", "position": "Registrar of Co-operative Societies", "department": "Ministry of Agriculture - Gambia", "honors": ["M.B.E."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
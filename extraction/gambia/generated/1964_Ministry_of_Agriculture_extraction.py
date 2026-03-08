"""
Gambia Colonial Office List 1964 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1964

OFFICIALS = [
    {"name": "S. G. Trees", "canonical_name": "Trees, S. G.", "given_names": "S. G.", "surname": "Trees", "position": "Secretary", "department": "Ministry of Agriculture - Gambia", "honors": ["M.V.O."]},
    {"name": "J. A. Austin", "canonical_name": "Austin, J. A.", "given_names": "J. A.", "surname": "Austin", "position": "Director of Agriculture", "department": "Ministry of Agriculture - Gambia", "honors": ["O.B.E."]},
    {"name": "K. O. Gyenning", "canonical_name": "Gyenning, K. O.", "given_names": "K. O.", "surname": "Gyenning", "position": "Principal Veterinary Officer", "department": "Ministry of Agriculture - Gambia"},
    {"name": "A. L. Macintosh", "canonical_name": "Macintosh, A. L.", "given_names": "A. L.", "surname": "Macintosh", "position": "Registrar, Co-operative Societies", "department": "Ministry of Agriculture - Gambia", "honors": ["M.B.E."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
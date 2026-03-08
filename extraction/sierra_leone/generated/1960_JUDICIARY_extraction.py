"""
Sierra Leone Colonial Office List 1960 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1960

OFFICIALS = [
    {"name": "Sir Vahe R. Bairamian", "canonical_name": "Bairamian, Vahe R.", "given_names": "Vahe R.", "surname": "Bairamian", "position": "Chief Justice", "department": "Judicial - Sierra Leone"},
    {"name": "S. A. Benka-Coker", "canonical_name": "Benka-Coker, S. A.", "given_names": "S. A.", "surname": "Benka-Coker", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "honors": ["O.B.E."]},
    {"name": "R. B. Marke", "canonical_name": "Marke, R. B.", "given_names": "R. B.", "surname": "Marke", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "honors": ["C.B.E."]},
    {"name": "P. Watkin Williams", "canonical_name": "Williams, P. Watkin", "given_names": "P. Watkin", "surname": "Williams", "position": "Puisne Judge", "department": "Judicial - Sierra Leone"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
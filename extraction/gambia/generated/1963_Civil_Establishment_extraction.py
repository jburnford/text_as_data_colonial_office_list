"""
Gambia Colonial Office List 1963 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1963

OFFICIALS = [
    {"name": "Sir John Paul", "canonical_name": "Paul, John", "surname": "Paul", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "honors": ["K.C.M.G.", "O.B.E.", "M.C."]},
    {"name": "P. A. Gore", "canonical_name": "Gore, P. A.", "given_names": "P. A.", "surname": "Gore", "position": "Deputy Governor", "department": "Civil Establishment - Gambia", "honors": ["C.V.O."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
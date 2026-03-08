"""
Gambia Colonial Office List 1964 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1964

OFFICIALS = [
    {"name": "M. H. Orde", "canonical_name": "Orde, M. H.", "given_names": "M. H.", "surname": "Orde", "position": "Secretary", "department": "Ministry of Local Government, Lands and Labour - Gambia", "honors": ["O.B.E."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Commissioner of Labour", "department": "Ministry of Local Government, Lands and Labour - Gambia"},
    {"name": "B. O. S. Janneh", "canonical_name": "Janneh, B. O. S.", "given_names": "B. O. S.", "surname": "Janneh", "position": "Superintendent of Surveys", "department": "Ministry of Local Government, Lands and Labour - Gambia", "honors": ["M.B.E."]},
    {"name": "H. A. Oliver", "canonical_name": "Oliver, H. A.", "given_names": "H. A.", "surname": "Oliver", "position": "Controller of Census", "department": "Ministry of Local Government, Lands and Labour - Gambia", "honors": ["M.B.E."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
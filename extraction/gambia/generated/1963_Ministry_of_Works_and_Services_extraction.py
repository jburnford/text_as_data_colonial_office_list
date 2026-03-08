"""
Gambia Colonial Office List 1963 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1963

OFFICIALS = [
    {"name": "J. S. Pullinger", "canonical_name": "Pullinger, J. S.", "given_names": "J. S.", "surname": "Pullinger", "position": "Secretary to Ministry and Director of Public Works", "department": "Ministry of Works and Services - Gambia", "honors": ["O.B.E.", "G.M."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Electrical Engineer", "department": "Ministry of Works and Services - Gambia"},
    {"name": "S. H. Riley", "canonical_name": "Riley, S. H.", "given_names": "S. H.", "surname": "Riley", "position": "Government Printer", "department": "Ministry of Works and Services - Gambia"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
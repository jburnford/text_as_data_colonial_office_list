"""
Gambia Colonial Office List 1963 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1963

OFFICIALS = [
    {"name": "M. H. Orde", "canonical_name": "Orde, M. H.", "given_names": "M. H.", "surname": "Orde", "position": "Secretary to Ministry and Commissioner for Local Government", "department": "Ministry for Local Government and Lands - Gambia"},
    {"name": "B. O. Janneh", "canonical_name": "Janneh, B. O.", "given_names": "B. O.", "surname": "Janneh", "position": "Superintendent of Surveys", "department": "Ministry for Local Government and Lands - Gambia", "honors": ["M.B.E."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1965 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1965

OFFICIALS = [
    {"name": "H. A. Oliver", "canonical_name": "Oliver, H. A.", "given_names": "H. A.", "surname": "Oliver", "position": "Secretary", "department": "Ministry for Local Government, Lands and Labour - Gambia", "honors": ["M.B.E."]},
    {"name": "B. O. S. Janneh", "canonical_name": "Janneh, B. O. S.", "given_names": "B. O. S.", "surname": "Janneh", "position": "Superintendent of Surveys", "department": "Ministry for Local Government, Lands and Labour - Gambia", "honors": ["M.B.E."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
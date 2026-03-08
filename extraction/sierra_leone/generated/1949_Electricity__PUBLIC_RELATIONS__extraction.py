"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "I. D. MacLennan", "canonical_name": "MacLennan, I. D.", "given_names": "I. D.", "surname": "MacLennan", "position": "Chief Electrical Engineer", "department": "Electricity - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "honors": ["O.B.E."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Electrical Engineer", "department": "Electricity - Sierra Leone", "salary_scale": "A"},
    {"name": "R. I. A. Aubee", "canonical_name": "Aubee, R. I. A.", "given_names": "R. I. A.", "surname": "Aubee", "position": "Assistant Accountant", "department": "Electricity - Sierra Leone", "salary_scale": "B"},
    {"name": "E. F. Sayers", "canonical_name": "Sayers, E. F.", "given_names": "E. F.", "surname": "Sayers", "position": "Public Relations Officer", "department": "PUBLIC RELATIONS - Sierra Leone"},
    {"name": "W. Venner", "canonical_name": "Venner, W.", "given_names": "W.", "surname": "Venner", "position": "General Manager", "department": "RAILWAY - Sierra Leone", "salary_min": 1350, "salary_max": 1350}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
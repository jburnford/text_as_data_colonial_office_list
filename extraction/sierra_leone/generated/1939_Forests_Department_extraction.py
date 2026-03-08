"""
Sierra Leone Colonial Office List 1939 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1939

OFFICIALS = [
    {"name": "W. M. Robertson", "canonical_name": "Robertson, W. M.", "given_names": "W. M.", "surname": "Robertson", "position": "Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "qualifications": ["B.Sc."]},
    {"name": "T. E. Edwardson", "canonical_name": "Edwardson, T. E.", "given_names": "T. E.", "surname": "Edwardson", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C"},
    {"name": "R. S. Pelley", "canonical_name": "Pelley, R. S.", "given_names": "R. S.", "surname": "Pelley", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_min": 450, "salary_max": 840},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
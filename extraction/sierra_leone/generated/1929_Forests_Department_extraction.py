"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "K. G. Burbridge", "canonical_name": "Burbridge, K. G.", "given_names": "K. G.", "surname": "Burbridge", "position": "Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "E. Macdonald", "canonical_name": "Macdonald, E.", "given_names": "E.", "surname": "Macdonald", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C"},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. Burns", "canonical_name": "Burns, A.", "given_names": "A.", "surname": "Burns", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C"},
    {"name": "D. McIntosh", "canonical_name": "McIntosh, D.", "given_names": "D.", "surname": "McIntosh", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "J. Stevenson", "canonical_name": "Stevenson, J.", "given_names": "J.", "surname": "Stevenson", "position": "Director of Surveys and Lands", "department": "Surveys and Lands - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "honors": ["M.B.E."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Lands Officer and Senior Surveyor", "department": "Surveys and Lands - Sierra Leone", "salary_scale": "A", "salary_min": 720, "salary_max": 1000},
    {"name": "D. G. Glassford", "canonical_name": "Glassford, D. G.", "given_names": "D. G.", "surname": "Glassford", "position": "Surveyor", "department": "Surveys and Lands - Sierra Leone", "salary_scale": "A"},
    {"name": "D. T. Lloyd", "canonical_name": "Lloyd, D. T.", "given_names": "D. T.", "surname": "Lloyd", "position": "Surveyor", "department": "Surveys and Lands - Sierra Leone", "salary_scale": "A"},
    {"name": "A. N. Rice", "canonical_name": "Rice, A. N.", "given_names": "A. N.", "surname": "Rice", "position": "Surveyor", "department": "Surveys and Lands - Sierra Leone", "salary_scale": "A"},
    {"name": "T. W. Skuse", "canonical_name": "Skuse, T. W.", "given_names": "T. W.", "surname": "Skuse", "position": "Superintendent of Training", "department": "Surveys and Lands - Sierra Leone", "salary_scale": "A"},
    {"name": "A. Fulton", "canonical_name": "Fulton, A.", "given_names": "A.", "surname": "Fulton", "position": "Director of Veterinary Services", "department": "Veterinary - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "S. L. H. Walshe", "canonical_name": "Walshe, S. L. H.", "given_names": "S. L. H.", "surname": "Walshe", "position": "Veterinary Officer", "department": "Veterinary - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
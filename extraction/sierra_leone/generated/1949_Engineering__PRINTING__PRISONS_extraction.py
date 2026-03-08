"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "J. B. Garrett", "canonical_name": "Garrett, J. B.", "given_names": "J. B.", "surname": "Garrett", "position": "Engineer", "department": "Engineering - Sierra Leone", "salary_scale": "A"},
    {"name": "F. W. Smith", "canonical_name": "Smith, F. W.", "given_names": "F. W.", "surname": "Smith", "position": "Government Printer", "department": "PRINTING - Sierra Leone", "salary_min": 750, "salary_max": 750},
    {"name": "T. P. Robinson", "canonical_name": "Robinson, T. P.", "given_names": "T. P.", "surname": "Robinson", "position": "Superintendent of Prisons", "department": "PRISONS - Sierra Leone", "salary_min": 750, "salary_max": 750},
    {"name": "J. A. Dudley-Nigg", "canonical_name": "Dudley-Nigg, J. A.", "given_names": "J. A.", "surname": "Dudley-Nigg", "position": "Senior Assistant Superintendent of Prisons", "department": "PRISONS - Sierra Leone"},
    {"name": "G. D. Skelland", "canonical_name": "Skelland, G. D.", "given_names": "G. D.", "surname": "Skelland", "position": "Assistant Superintendents of Prisons", "department": "PRISONS - Sierra Leone"},
    {"name": "W. B. Wright", "canonical_name": "Wright, W. B.", "given_names": "W. B.", "surname": "Wright", "position": "Assistant Superintendents of Prisons", "department": "PRISONS - Sierra Leone"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
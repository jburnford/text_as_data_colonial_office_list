"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "E. A. F. Brandon", "canonical_name": "Brandon, E. A. F.", "given_names": "E. A. F.", "surname": "Brandon", "position": "Government Printer", "department": "Printing - Sierra Leone", "salary_min": 800, "salary_max": 800},
    {"name": "T. P. Robinson", "canonical_name": "Robinson, T. P.", "given_names": "T. P.", "surname": "Robinson", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 900, "salary_max": 900},
    {"name": "J. A. Dudley-Nigg", "canonical_name": "Dudley-Nigg, J. A.", "given_names": "J. A.", "surname": "Dudley-Nigg", "position": "Senior Assistant Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_scale": "C.3"},
    {"name": "G. D. Skelland", "canonical_name": "Skelland, G. D.", "given_names": "G. D.", "surname": "Skelland", "position": "Assistant Superintendents of Prisons", "department": "Prisons - Sierra Leone", "salary_scale": "C.1"},
    {"name": "W. B. Wright", "canonical_name": "Wright, W. B.", "given_names": "W. B.", "surname": "Wright", "position": "Assistant Superintendents of Prisons", "department": "Prisons - Sierra Leone", "salary_scale": "C.1"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
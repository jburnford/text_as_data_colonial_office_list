"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "T. D. Hewer", "canonical_name": "Hewer, T. D.", "given_names": "T. D.", "surname": "Hewer", "position": "Superintendent", "department": "Printing - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Government Printer", "department": "Printing - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "J. N. L. Metzger", "canonical_name": "Metzger, J. N. L.", "given_names": "J. N. L.", "surname": "Metzger", "position": "Proof Reader", "department": "Printing - Sierra Leone", "salary_min": 70, "salary_max": 100},
    {"name": "J. A. Macfoy", "canonical_name": "Macfoy, J. A.", "given_names": "J. A.", "surname": "Macfoy", "position": "Senior Compositor", "department": "Printing - Sierra Leone", "salary_min": 90, "salary_max": 120},
    {"name": "A. T. George", "canonical_name": "George, A. T.", "given_names": "A. T.", "surname": "George", "position": "Book Binder", "department": "Printing - Sierra Leone", "salary_min": 70, "salary_max": 90},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
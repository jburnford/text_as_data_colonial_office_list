"""
Sierra Leone Colonial Office List 1950 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1950

OFFICIALS = [
    {"name": "C. E. Ross", "canonical_name": "Ross, C. E.", "given_names": "C. E.", "surname": "Ross", "position": "Postmaster-General", "department": "POST OFFICE - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "F. Wood", "canonical_name": "Wood, F.", "given_names": "F.", "surname": "Wood", "position": "Assistant Postmaster-General", "department": "POST OFFICE - Sierra Leone", "salary_scale": "B"},
    {"name": "J. C. I. Oldfield", "canonical_name": "Oldfield, J. C. I.", "given_names": "J. C. I.", "surname": "Oldfield", "position": "Postmaster, Freetown", "department": "POST OFFICE - Sierra Leone", "honors": ["I.S.O."], "salary_scale": "B", "location": "Freetown"},
    {"name": "A. H. Wells", "canonical_name": "Wells, A. H.", "given_names": "A. H.", "surname": "Wells", "position": "Accountant", "department": "POST OFFICE - Sierra Leone", "salary_scale": "B"},
    {"name": "J. N. A. Jones", "canonical_name": "Jones, J. N. A.", "given_names": "J. N. A.", "surname": "Jones", "position": "Assistant Accountant", "department": "POST OFFICE - Sierra Leone", "salary_scale": "B"},
    {"name": "J. B. Garrett", "canonical_name": "Garrett, J. B.", "given_names": "J. B.", "surname": "Garrett", "position": "Engineer", "department": "Engineering - Sierra Leone", "salary_scale": "A"},
    {"name": "F. W. Smith", "canonical_name": "Smith, F. W.", "given_names": "F. W.", "surname": "Smith", "position": "Government Printer", "department": "PRINTING - Sierra Leone", "salary_min": 800, "salary_max": 800, "allowances": "£90 as Printing Advisor to the Government of the Gambia"},
    {"name": "T. P. Robinson", "canonical_name": "Robinson, T. P.", "given_names": "T. P.", "surname": "Robinson", "position": "Superintendent of Prisons", "department": "PRISONS - Sierra Leone", "salary_min": 900, "salary_max": 900},
    {"name": "J. A. Dudley-Nigg", "canonical_name": "Dudley-Nigg, J. A.", "given_names": "J. A.", "surname": "Dudley-Nigg", "position": "Senior Assistant Superintendent of Prisons", "department": "PRISONS - Sierra Leone", "salary_scale": "C.2"},
    {"name": "G. D. Skelland", "canonical_name": "Skelland, G. D.", "given_names": "G. D.", "surname": "Skelland", "position": "Assistant Superintendents of Prisons", "department": "PRISONS - Sierra Leone", "salary_scale": "C.1"},
    {"name": "W. B. Wright", "canonical_name": "Wright, W. B.", "given_names": "W. B.", "surname": "Wright", "position": "Assistant Superintendents of Prisons", "department": "PRISONS - Sierra Leone", "salary_scale": "C.1"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "A. R. Smee", "canonical_name": "Smee, A. R.", "given_names": "A. R.", "surname": "Smee", "position": "Director of Public Works", "department": "Public Works - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "honors": ["C.B.E."]},
    {"name": "A. S. Ellicott", "canonical_name": "Ellicott, A. S.", "given_names": "A. S.", "surname": "Ellicott", "position": "Assistant Director of Public Works", "department": "Public Works - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "A. Dunbar", "canonical_name": "Dunbar, A.", "given_names": "A.", "surname": "Dunbar", "position": "Assistant Director of Public Works", "department": "Public Works - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "K. H. B. Collier", "canonical_name": "Collier, K. H. B.", "given_names": "K. H. B.", "surname": "Collier", "position": "Provincial Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. H. Amos", "canonical_name": "Amos, J. H.", "given_names": "J. H.", "surname": "Amos", "position": "Provincial Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. P. Murphy", "canonical_name": "Murphy, J. P.", "given_names": "J. P.", "surname": "Murphy", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. F. Nicholas", "canonical_name": "Nicholas, J. F.", "given_names": "J. F.", "surname": "Nicholas", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "D. S. Garvie", "canonical_name": "Garvie, D. S.", "given_names": "D. S.", "surname": "Garvie", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. F. Gigg", "canonical_name": "Gigg, J. F.", "given_names": "J. F.", "surname": "Gigg", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. P. Coree", "canonical_name": "Coree, J. P.", "given_names": "J. P.", "surname": "Coree", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "R. H. Macartney", "canonical_name": "Macartney, R. H.", "given_names": "R. H.", "surname": "Macartney", "position": "Senior Architect", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "R. F. Lomax", "canonical_name": "Lomax, R. F.", "given_names": "R. F.", "surname": "Lomax", "position": "Architect", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "B. R. Thomas", "canonical_name": "Thomas, B. R.", "given_names": "B. R.", "surname": "Thomas", "position": "Chief Accountant", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "F. W. H. Seamark", "canonical_name": "Seamark, F. W. H.", "given_names": "F. W. H.", "surname": "Seamark", "position": "Chief Storekeeper", "department": "Public Works - Sierra Leone", "salary_scale": "C2.3"},
    {"name": "N. T. Osborne", "canonical_name": "Osborne, N. T.", "given_names": "N. T.", "surname": "Osborne", "position": "Assistant Accountant", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "C. R. Boucher", "canonical_name": "Boucher, C. R.", "given_names": "C. R.", "surname": "Boucher", "position": "Assistant Accountant", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "M. H. King", "canonical_name": "King, M. H.", "given_names": "M. H.", "surname": "King", "position": "Assistant Accountant", "department": "Public Works - Sierra Leone", "salary_scale": "B"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
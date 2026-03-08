"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "A. Dunbar", "canonical_name": "Dunbar, A.", "given_names": "A.", "surname": "Dunbar", "position": "Director of Public Works", "department": "Public Works - Sierra Leone", "salary_min": 1350, "salary_max": 1350},
    {"name": "T. W. Shaw", "canonical_name": "Shaw, T. W.", "given_names": "T. W.", "surname": "Shaw", "position": "Deputy Director of Public Works", "department": "Public Works - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Director of Public Works", "department": "Public Works - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "K. H. B. Collier", "canonical_name": "Collier, K. H. B.", "given_names": "K. H. B.", "surname": "Collier", "position": "Provincial Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. P. Murphy", "canonical_name": "Murphy, J. P.", "given_names": "J. P.", "surname": "Murphy", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. F. Nicholas", "canonical_name": "Nicholas, J. F.", "given_names": "J. F.", "surname": "Nicholas", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "D. S. Garvie", "canonical_name": "Garvie, D. S.", "given_names": "D. S.", "surname": "Garvie", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "G. J. Skelt", "canonical_name": "Skelt, G. J.", "given_names": "G. J.", "surname": "Skelt", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. P. Coree", "canonical_name": "Coree, J. P.", "given_names": "J. P.", "surname": "Coree", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "G. R. Handley", "canonical_name": "Handley, G. R.", "given_names": "G. R.", "surname": "Handley", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. R. Howard", "canonical_name": "Howard, J. R.", "given_names": "J. R.", "surname": "Howard", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "M. O'Sullivan", "canonical_name": "O'Sullivan, M.", "given_names": "M.", "surname": "O'Sullivan", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "N. J. Ballard", "canonical_name": "Ballard, N. J.", "given_names": "N. J.", "surname": "Ballard", "position": "Executive Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "R. H. Macartney", "canonical_name": "Macartney, R. H.", "given_names": "R. H.", "surname": "Macartney", "position": "Senior Architect", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "R. F. Lomax", "canonical_name": "Lomax, R. F.", "given_names": "R. F.", "surname": "Lomax", "position": "Architect", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Public Health Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "A. Green", "canonical_name": "Green, A.", "given_names": "A.", "surname": "Green", "position": "Quantity Surveyor", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "J. B. Kirkland", "canonical_name": "Kirkland, J. B.", "given_names": "J. B.", "surname": "Kirkland", "position": "Mechanical Engineer", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "B. R. Thomas", "canonical_name": "Thomas, B. R.", "given_names": "B. R.", "surname": "Thomas", "position": "Chief Accountant", "department": "Public Works - Sierra Leone", "salary_scale": "B", "salary_min": 660, "salary_max": 900},
    {"name": "F. W. H. Seamark", "canonical_name": "Seamark, F. W. H.", "given_names": "F. W. H.", "surname": "Seamark", "position": "Chief Storekeeper", "department": "Public Works - Sierra Leone", "salary_scale": "C.2"},
    {"name": "N. T. Osborne", "canonical_name": "Osborne, N. T.", "given_names": "N. T.", "surname": "Osborne", "position": "Accountant", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "C. R. Boucher", "canonical_name": "Boucher, C. R.", "given_names": "C. R.", "surname": "Boucher", "position": "Accountant", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "M. H. King", "canonical_name": "King, M. H.", "given_names": "M. H.", "surname": "King", "position": "Accountant", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "A. Karim", "canonical_name": "Karim, A.", "given_names": "A.", "surname": "Karim", "position": "Secretary", "department": "Public Works - Sierra Leone", "salary_scale": "B"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
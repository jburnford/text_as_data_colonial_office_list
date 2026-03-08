"""
Sierra Leone Colonial Office List 1950 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1950

OFFICIALS = [
    {"name": "A. Dunbar", "canonical_name": "Dunbar, A.", "given_names": "A.", "surname": "Dunbar", "position": "Director of Public Works", "department": "Public Works - Sierra Leone", "salary_min": 1350, "salary_max": 1350},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Director of Public Works", "department": "Public Works - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "A. S. Ellicott", "canonical_name": "Ellicott, A. S.", "given_names": "A. S.", "surname": "Ellicott", "position": "Assistant Director of Public Works", "department": "Public Works - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "K. H. B. Collier", "canonical_name": "Collier, K. H. B.", "given_names": "K. H. B.", "surname": "Collier", "position": "Provincial Engineers", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. P. Murphy", "canonical_name": "Murphy, J. P.", "given_names": "J. P.", "surname": "Murphy", "position": "Executive Engineers", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. F. Nicholas", "canonical_name": "Nicholas, J. F.", "given_names": "J. F.", "surname": "Nicholas", "position": "Executive Engineers", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "D. S. Garvie", "canonical_name": "Garvie, D. S.", "given_names": "D. S.", "surname": "Garvie", "position": "Executive Engineers", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. F. Gigg", "canonical_name": "Gigg, J. F.", "given_names": "J. F.", "surname": "Gigg", "position": "Executive Engineers", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "G. J. Skelt", "canonical_name": "Skelt, G. J.", "given_names": "G. J.", "surname": "Skelt", "position": "Executive Engineers", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "J. P. Coree", "canonical_name": "Coree, J. P.", "given_names": "J. P.", "surname": "Coree", "position": "Executive Engineers", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "R. H. Macartney", "canonical_name": "Macartney, R. H.", "given_names": "R. H.", "surname": "Macartney", "position": "Senior Architect", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "R. F. Lomax", "canonical_name": "Lomax, R. F.", "given_names": "R. F.", "surname": "Lomax", "position": "Architect", "department": "Public Works - Sierra Leone", "salary_scale": "A"},
    {"name": "B. R. Thomas", "canonical_name": "Thomas, B. R.", "given_names": "B. R.", "surname": "Thomas", "position": "Chief Accountant", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "F. W. H. Seamark", "canonical_name": "Seamark, F. W. H.", "given_names": "F. W. H.", "surname": "Seamark", "position": "Chief Storekeeper", "department": "Public Works - Sierra Leone", "salary_scale": "C.2.3"},
    {"name": "N. T. Osborne", "canonical_name": "Osborne, N. T.", "given_names": "N. T.", "surname": "Osborne", "position": "Assistant Accountants", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "C. R. Boucher", "canonical_name": "Boucher, C. R.", "given_names": "C. R.", "surname": "Boucher", "position": "Assistant Accountants", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "M. H. King", "canonical_name": "King, M. H.", "given_names": "M. H.", "surname": "King", "position": "Assistant Accountants", "department": "Public Works - Sierra Leone", "salary_scale": "B"},
    {"name": "R. F. Havart", "canonical_name": "Havart, R. F.", "given_names": "R. F.", "surname": "Havart", "position": "Chief Electrical Engineer", "department": "Electricity - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "E. Kent", "canonical_name": "Kent, E.", "given_names": "E.", "surname": "Kent", "position": "Electrical Engineer", "department": "Electricity - Sierra Leone", "salary_scale": "A"},
    {"name": "R. I. A. Aubee", "canonical_name": "Aubee, R. I. A.", "given_names": "R. I. A.", "surname": "Aubee", "position": "Assistant Accountant", "department": "Electricity - Sierra Leone", "salary_scale": "B", "honors": ["M.B.E."]},
    {"name": "W. G. Ash", "canonical_name": "Ash, W. G.", "given_names": "W. G.", "surname": "Ash", "position": "Public Relations Officer", "department": "Public Relations - Sierra Leone"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
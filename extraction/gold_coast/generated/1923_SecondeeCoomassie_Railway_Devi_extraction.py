"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "J. G. Rice", "canonical_name": "Rice, J. G.", "given_names": "J. G.", "surname": "Rice",
     "position": "Resident Engineer", "department": "Railway Department - Gold Coast", "salary_min": 800, "salary_max": 920,
     "allowances": "150l charge allowance, 72l. seniority allowance, and 90l. field allowance"},
    {"name": "J. R. S. Sutherland", "canonical_name": "Sutherland, J. R. S.", "given_names": "J. R. S.", "surname": "Sutherland",
     "position": "District Engineer", "department": "Railway Department - Gold Coast", "salary_min": 720, "salary_max": 920,
     "allowances": "72l. seniority allowance, and 90l. field allowance"},
    {"name": "E. A. Earl", "canonical_name": "Earl, E. A.", "given_names": "E. A.", "surname": "Earl",
     "position": "Assistant Engineer", "department": "Railway Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "allowances": "field allowance, 90l."},
    {"name": "B. V. Grealy", "canonical_name": "Grealy, B. V.", "given_names": "B. V.", "surname": "Grealy",
     "position": "Assistant Engineer", "department": "Railway Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "allowances": "field allowance, 90l."},
    {"name": "H. W. Drummond", "canonical_name": "Drummond, H. W.", "given_names": "H. W.", "surname": "Drummond",
     "position": "Assistant Engineer", "department": "Railway Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "allowances": "field allowance, 90l."},
    {"name": "T. J. G. Sproule", "canonical_name": "Sproule, T. J. G.", "given_names": "T. J. G.", "surname": "Sproule",
     "position": "Assistant Engineer", "department": "Railway Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "allowances": "field allowance, 90l."},
    {"name": "J. H. Walters", "canonical_name": "Walters, J. H.", "given_names": "J. H.", "surname": "Walters",
     "position": "Assistant Engineer", "department": "Railway Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "allowances": "field allowance, 90l."},
    {"name": "A. D. Ross", "canonical_name": "Ross, A. D.", "given_names": "A. D.", "surname": "Ross",
     "position": "Assistant Engineer", "department": "Railway Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "allowances": "field allowance, 90l."},
    {"name": "R. G. Orr", "canonical_name": "Orr, R. G.", "given_names": "R. G.", "surname": "Orr",
     "position": "Assistant Engineer", "department": "Railway Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "allowances": "field allowance, 90l."},
    {"name": "W. M. Maitland", "canonical_name": "Maitland, W. M.", "given_names": "W. M.", "surname": "Maitland",
     "position": "Draughtsman", "department": "Railway Department - Gold Coast", "salary_min": 500,
     "allowances": "90l. field allowance"},
    {"name": "G. A. Gascoigne", "canonical_name": "Gascoigne, G. A.", "given_names": "G. A.", "surname": "Gascoigne",
     "position": "Storekeeper Accountant", "department": "Railway Department - Gold Coast", "salary_min": 500,
     "allowances": "90l. field allowance"},
    {"name": "H. W. Erby", "canonical_name": "Erby, H. W.", "given_names": "H. W.", "surname": "Erby",
     "position": "Storekeeper Accountant", "department": "Railway Department - Gold Coast", "salary_min": 500,
     "allowances": "90l. field allowance"},
    {"name": "F. A. Russell", "canonical_name": "Russell, F. A.", "given_names": "F. A.", "surname": "Russell",
     "position": "Storekeeper Accountant", "department": "Railway Department - Gold Coast", "salary_min": 500,
     "allowances": "90l. field allowance"},
    {"name": "B. W. Taylor", "canonical_name": "Taylor, B. W.", "given_names": "B. W.", "surname": "Taylor",
     "position": "Storekeeper Accountant", "department": "Railway Department - Gold Coast", "salary_min": 500,
     "allowances": "90l. field allowance"},
    {"name": "F. Aston", "canonical_name": "Aston, F.", "given_names": "F.", "surname": "Aston",
     "position": "Platelayer", "department": "Railway Department - Gold Coast", "salary_min": 420,
     "allowances": "90l. field allowance"},
    {"name": "J. T. Hoskins", "canonical_name": "Hoskins, J. T.", "given_names": "J. T.", "surname": "Hoskins",
     "position": "General Foreman", "department": "Railway Department - Gold Coast", "salary_min": 600}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
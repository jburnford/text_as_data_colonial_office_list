"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "C. A. Copland", "canonical_name": "Copland, C. A.", "given_names": "C. A.", "surname": "Copland", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "duty_allowance": 120},
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "G. Stanley", "canonical_name": "Stanley, G.", "given_names": "G.", "surname": "Stanley", "position": "Assistant Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. A. P. D. Stone", "canonical_name": "Stone, A. A. P. D.", "given_names": "A. A. P. D.", "surname": "Stone", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "B. W. Fitch-Jones", "canonical_name": "Fitch-Jones, B. W.", "given_names": "B. W.", "surname": "Fitch-Jones", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "P. W. Clemens", "canonical_name": "Clemens, P. W.", "given_names": "P. W.", "surname": "Clemens", "position": "Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "J. G. Harrison", "canonical_name": "Harrison, J. G.", "given_names": "J. G.", "surname": "Harrison", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "N. Nye", "canonical_name": "Nye, N.", "given_names": "N.", "surname": "Nye", "position": "Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. H. Sheldrake", "canonical_name": "Sheldrake, J. H.", "given_names": "J. H.", "surname": "Sheldrake", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "E. T. Greenwood", "canonical_name": "Greenwood, E. T.", "given_names": "E. T.", "surname": "Greenwood", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "G. McLauchlan", "canonical_name": "McLauchlan, G.", "given_names": "G.", "surname": "McLauchlan", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "F. W. Wright", "canonical_name": "Wright, F. W.", "given_names": "F. W.", "surname": "Wright", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "C. E. Brealy", "canonical_name": "Brealy, C. E.", "given_names": "C. E.", "surname": "Brealy", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "B. Webb", "canonical_name": "Webb, B.", "given_names": "B.", "surname": "Webb", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "S. Cowgill", "canonical_name": "Cowgill, S.", "given_names": "S.", "surname": "Cowgill", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "C. Pope", "canonical_name": "Pope, C.", "given_names": "C.", "surname": "Pope", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "D. S. McQuiston", "canonical_name": "McQuiston, D. S.", "given_names": "D. S.", "surname": "McQuiston", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "A. W. Spencer", "canonical_name": "Spencer, A. W.", "given_names": "A. W.", "surname": "Spencer", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "F. Foord", "canonical_name": "Foord, F.", "given_names": "F.", "surname": "Foord", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. B. Luke", "canonical_name": "Luke, J. B.", "given_names": "J. B.", "surname": "Luke", "position": "Native Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "A. S. Cole", "canonical_name": "Cole, A. S.", "given_names": "A. S.", "surname": "Cole", "position": "Native Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "E. O. Smith", "canonical_name": "Smith, E. O.", "given_names": "E. O.", "surname": "Smith", "position": "Assistant Native Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "B. L. Wilson", "canonical_name": "Wilson, B. L.", "given_names": "B. L.", "surname": "Wilson", "position": "Surveyor of Crown Lands", "department": "Public Works Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "G. P. Jarrett", "canonical_name": "Jarrett, G. P.", "given_names": "G. P.", "surname": "Jarrett", "position": "First Grade Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 160, "salary_max": 200}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1905 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1905

OFFICIALS = [
    {"name": "C. A. Copland", "canonical_name": "Copland, C. A.", "given_names": "C. A.", "surname": "Copland", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800},
    {"name": "J. Walker", "canonical_name": "Walker, J.", "given_names": "J.", "surname": "Walker", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 300},
    {"name": "B. L. Wilson", "canonical_name": "Wilson, B. L.", "given_names": "B. L.", "surname": "Wilson", "position": "Surveyor of Crown Lands", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "Chief Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "D. G. Williams", "canonical_name": "Williams, D. G.", "given_names": "D. G.", "surname": "Williams", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone"},
    {"name": "W. S. Saunders", "canonical_name": "Saunders, W. S.", "given_names": "W. S.", "surname": "Saunders", "position": "Chief Clerk and Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "Alfred Williams", "canonical_name": "Williams, Alfred", "given_names": "Alfred", "surname": "Williams", "position": "Water Inspector", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "G. P. Jarrett", "canonical_name": "Jarrett, G. P.", "given_names": "G. P.", "surname": "Jarrett", "position": "2nd Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "A. G. Parsons", "canonical_name": "Parsons, A. G.", "given_names": "A. G.", "surname": "Parsons", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "N. Fyne", "canonical_name": "Fyne, N.", "given_names": "N.", "surname": "Fyne", "position": "Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "James Collier", "canonical_name": "Collier, James", "given_names": "James", "surname": "Collier", "position": "Transport Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. B. Luke", "canonical_name": "Luke, J. B.", "given_names": "J. B.", "surname": "Luke", "position": "Building Inspector", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "A. S. Cole", "canonical_name": "Cole, A. S.", "given_names": "A. S.", "surname": "Cole", "position": "Assistant Building Inspector", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "Edgar du Boulay", "canonical_name": "Boulay, Edgar du", "given_names": "Edgar", "surname": "Boulay", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300},
    {"name": "F. S. Maxwell", "canonical_name": "Maxwell, F. S.", "given_names": "F. S.", "surname": "Maxwell", "position": "1st Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "2nd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "G. P. Coker", "canonical_name": "Coker, G. P.", "given_names": "G. P.", "surname": "Coker", "position": "3rd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. C. Pratt", "canonical_name": "Pratt, J. C.", "given_names": "J. C.", "surname": "Pratt", "position": "4th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
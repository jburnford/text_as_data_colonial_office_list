"""
Sierra Leone Colonial Office List 1894 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1894

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Colonial Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "W. E. Inniss", "canonical_name": "Inniss, W. E.", "given_names": "W. E.", "surname": "Inniss", "position": "Inspector of Works and Roads", "department": "Surveyor's Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "Assistant Inspector of Works and Roads", "department": "Surveyor's Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "B. A. Wright", "canonical_name": "Wright, B. A.", "given_names": "B. A.", "surname": "Wright", "position": "Clerk", "department": "Surveyor's Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. H. Kelson", "canonical_name": "Kelson, J. H.", "given_names": "J. H.", "surname": "Kelson", "position": "Storekeeper", "department": "Surveyor's Department - Sierra Leone", "salary_min": 54, "salary_max": 54},
    {"name": "W. Cuddeford", "canonical_name": "Cuddeford, W.", "given_names": "W.", "surname": "Cuddeford", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 450, "salary_max": 450, "allowances": "and quarters"},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "First Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "C. Duke", "canonical_name": "Duke, C.", "given_names": "C.", "surname": "Duke", "position": "Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 40, "salary_max": 40}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
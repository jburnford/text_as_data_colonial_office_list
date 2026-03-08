"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "T. E. Laing", "canonical_name": "Laing, T. E.", "given_names": "T. E.", "surname": "Laing", "position": "Colonial Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "W. E. Inniss", "canonical_name": "Inniss, W. E.", "given_names": "W. E.", "surname": "Inniss", "position": "Assistant Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "B. L. Wilson", "canonical_name": "Wilson, B. L.", "given_names": "B. L.", "surname": "Wilson", "position": "2nd Surveyor", "department": "Surveyor's Department - Sierra Leone", "qualifications": ["C.E."], "salary_min": 100, "salary_max": 100},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "Chief Draughtsman", "department": "Surveyor's Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "B. A. Wright", "canonical_name": "Wright, B. A.", "given_names": "B. A.", "surname": "Wright", "position": "Chief Clerk", "department": "Surveyor's Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "W. E. Campbell", "canonical_name": "Campbell, W. E.", "given_names": "W. E.", "surname": "Campbell", "position": "2nd Clerk", "department": "Surveyor's Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. H. Kelson", "canonical_name": "Kelson, J. H.", "given_names": "J. H.", "surname": "Kelson", "position": "Storekeeper", "department": "Surveyor's Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "W. Cuddeford", "canonical_name": "Cuddeford, W.", "given_names": "W.", "surname": "Cuddeford", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 450, "salary_max": 450, "allowances": "and quarters"},
    {"name": "H. C. E. Barnes", "canonical_name": "Barnes, H. C. E.", "given_names": "H. C. E.", "surname": "Barnes", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 225, "salary_max": 225, "allowances": ", and quarters or rent"},
    {"name": "P. A. Nichols", "canonical_name": "Nichols, P. A.", "given_names": "P. A.", "surname": "Nichols", "position": "First Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
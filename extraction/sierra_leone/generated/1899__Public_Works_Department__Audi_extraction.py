"""
Sierra Leone Colonial Office List 1899 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1899

OFFICIALS = [
    {"name": "T. E. Laing", "canonical_name": "Laing, T. E.", "given_names": "T. E.", "surname": "Laing", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "F. H. Stone", "canonical_name": "Stone, F. H.", "given_names": "F. H.", "surname": "Stone", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "B. L. Wilson", "canonical_name": "Wilson, B. L.", "given_names": "B. L.", "surname": "Wilson", "position": "Superintendent", "department": "Public Works Department - Sierra Leone", "qualifications": ["C.E."], "salary_min": 100, "salary_max": 150},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "Chief Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. W. Paris", "canonical_name": "Paris, J. W.", "given_names": "J. W.", "surname": "Paris", "position": "Chief Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "G. P. Jarrett", "canonical_name": "Jarrett, G. P.", "given_names": "G. P.", "surname": "Jarrett", "position": "2nd Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. H. Kelson", "canonical_name": "Kelson, J. H.", "given_names": "J. H.", "surname": "Kelson", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. C. Pratt", "canonical_name": "Pratt, J. C.", "given_names": "J. C.", "surname": "Pratt", "position": "Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "R. C. Grannum", "canonical_name": "Grannum, R. C.", "given_names": "R. C.", "surname": "Grannum", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 450, "salary_max": 450, "allowances": "and quarters"},
    {"name": "A. Grannum", "canonical_name": "Grannum, A.", "given_names": "A.", "surname": "Grannum", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 225, "salary_max": 225, "allowances": ", and quarters or rent"},
    {"name": "P. A. Nichols", "canonical_name": "Nichols, P. A.", "given_names": "P. A.", "surname": "Nichols", "position": "First Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "F. S. Maxwell", "canonical_name": "Maxwell, F. S.", "given_names": "F. S.", "surname": "Maxwell", "position": "Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
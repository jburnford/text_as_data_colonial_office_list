"""
Sierra Leone Colonial Office List 1906 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1906

OFFICIALS = [
    {"name": "C. A. Copland", "canonical_name": "Copland, C. A.", "given_names": "C. A.", "surname": "Copland", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800},
    {"name": "J. Walker", "canonical_name": "Walker, J.", "given_names": "J.", "surname": "Walker", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "B. L. Wilson", "canonical_name": "Wilson, B. L.", "given_names": "B. L.", "surname": "Wilson", "position": "Surveyor of Crown Lands", "department": "Public Works Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "Chief Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "D. G. Williams", "canonical_name": "Williams, D. G.", "given_names": "D. G.", "surname": "Williams", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 45, "salary_max": 65},
    {"name": "W. S. Saunders", "canonical_name": "Saunders, W. S.", "given_names": "W. S.", "surname": "Saunders", "position": "Chief Clerk and Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "G. P. Jarrett", "canonical_name": "Jarrett, G. P.", "given_names": "G. P.", "surname": "Jarrett", "position": "1st Clerk and Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "S. B. Logan", "canonical_name": "Logan, S. B.", "given_names": "S. B.", "surname": "Logan", "position": "2nd Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "Alfred Williams", "canonical_name": "Williams, Alfred", "given_names": "Alfred", "surname": "Williams", "position": "Water Inspector", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "B. E. Cummings", "canonical_name": "Cummings, B. E.", "given_names": "B. E.", "surname": "Cummings", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "W. T. Grant", "canonical_name": "Grant, W. T.", "given_names": "W. T.", "surname": "Grant", "position": "Clerk to Under Sheriff", "department": "Public Works Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "A. E. T. Metzger", "canonical_name": "Metzger, A. E. T.", "given_names": "A. E. T.", "surname": "Metzger", "position": "Clerk, Police Court", "department": "Public Works Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "J. Nicol", "canonical_name": "Nicol, J.", "given_names": "J.", "surname": "Nicol", "position": "2nd Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "W. A. Cole", "canonical_name": "Cole, W. A.", "given_names": "W. A.", "surname": "Cole", "position": "Bailiff", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "Curator of Intestate Estates", "department": "Public Works Department - Sierra Leone"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
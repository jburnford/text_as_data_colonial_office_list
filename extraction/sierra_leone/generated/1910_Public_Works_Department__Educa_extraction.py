"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "C. A. Copland", "canonical_name": "Copland, C. A.", "given_names": "C. A.", "surname": "Copland", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800},
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. H. Sheldrake", "canonical_name": "Sheldrake, J. H.", "given_names": "J. H.", "surname": "Sheldrake", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "C. F. Wilson", "canonical_name": "Wilson, C. F.", "given_names": "C. F.", "surname": "Wilson", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. B. Luke", "canonical_name": "Luke, J. B.", "given_names": "J. B.", "surname": "Luke", "position": "Native Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "A. S. Cole", "canonical_name": "Cole, A. S.", "given_names": "A. S.", "surname": "Cole", "position": "Native Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "B. L. Wilson", "canonical_name": "Wilson, B. L.", "given_names": "B. L.", "surname": "Wilson", "position": "Surveyor of Crown Lands", "department": "Public Works Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "G. Stanley", "canonical_name": "Stanley, G.", "given_names": "G.", "surname": "Stanley", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "S. Bull", "canonical_name": "Bull, S.", "given_names": "S.", "surname": "Bull", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 40, "salary_max": 65},
    {"name": "A. T. Porter", "canonical_name": "Porter, A. T.", "given_names": "A. T.", "surname": "Porter", "position": "Crown Lands Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "G. P. Jarrett", "canonical_name": "Jarrett, G. P.", "given_names": "G. P.", "surname": "Jarrett", "position": "Chief Clerk and Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "E. C. Davies", "canonical_name": "Davies, E. C.", "given_names": "E. C.", "surname": "Davies", "position": "1st Clerk and Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "S. B. Logan", "canonical_name": "Logan, S. B.", "given_names": "S. B.", "surname": "Logan", "position": "2nd Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "J. E. Smith", "canonical_name": "Smith, J. E.", "given_names": "J. E.", "surname": "Smith", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "A. E. Lavers", "canonical_name": "Lavers, A. E.", "given_names": "A. E.", "surname": "Lavers", "position": "Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. Collier", "canonical_name": "Collier, J.", "given_names": "J.", "surname": "Collier", "position": "Transport Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "R. F. Honter", "canonical_name": "Honter, R. F.", "given_names": "R. F.", "surname": "Honter", "position": "Director of Education", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "50l. personal"},
    {"name": "J. Proudfoot", "canonical_name": "Proudfoot, J.", "given_names": "J.", "surname": "Proudfoot", "position": "Principal, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 450, "salary_max": 500},
    {"name": "J. Pool", "canonical_name": "Pool, J.", "given_names": "J.", "surname": "Pool", "position": "Education Expert, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 360, "salary_max": 400},
    {"name": "W. J. Holloway", "canonical_name": "Holloway, W. J.", "given_names": "W. J.", "surname": "Holloway", "position": "Education Expert, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 360, "salary_max": 400},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "Clerk to Board of Education", "department": "Educational Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "Hadir-u-deen", "canonical_name": "Hadir-u-deen, ", "surname": "Hadir-u-deen", "position": "Secretary to Board of Mohammedan Education", "department": "Educational Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "H. L. Weber", "canonical_name": "Weber, H. L.", "given_names": "H. L.", "surname": "Weber", "position": "Clerk to Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
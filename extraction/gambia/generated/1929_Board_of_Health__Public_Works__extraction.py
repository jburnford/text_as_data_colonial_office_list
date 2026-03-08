"""
Gambia Colonial Office List 1929 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1929

OFFICIALS = [
    {"name": "F. A. Innes", "canonical_name": "Innes, F. A.", "given_names": "F. A.", "surname": "Innes", "position": "Medical Officer of Health", "department": "Board of Health - Gambia", "salary_min": 800, "salary_max": 960, "allowances": "staff and seniority allowances, 222l.", "military_rank": "Captain"},
    {"name": "A. F. V. Vaughan", "canonical_name": "Vaughan, A. F. V.", "given_names": "A. F. V.", "surname": "Vaughan", "position": "Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "F. A. Wilford", "canonical_name": "Wilford, F. A.", "given_names": "F. A.", "surname": "Wilford", "position": "Assistant Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 360, "salary_max": 460},
    {"name": "H. A. Tyler-Smith", "canonical_name": "Tyler-Smith, H. A.", "given_names": "H. A.", "surname": "Tyler-Smith", "position": "Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "P. G. Burrage", "canonical_name": "Burrage, P. G.", "given_names": "P. G.", "surname": "Burrage", "position": "Assistant Engineer", "department": "Public Works Department - Gambia", "salary_min": 600, "salary_max": 720},
    {"name": "C. Wolfendale", "canonical_name": "Wolfendale, C.", "given_names": "C.", "surname": "Wolfendale", "position": "Reclamation Officer", "department": "Public Works Department - Gambia", "salary_min": 600, "salary_max": 720},
    {"name": "H. F. Gibbons", "canonical_name": "Gibbons, H. F.", "given_names": "H. F.", "surname": "Gibbons", "position": "Clerks of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "S. Geering", "canonical_name": "Geering, S.", "given_names": "S.", "surname": "Geering", "position": "Clerks of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. W. Duffield", "canonical_name": "Duffield, H. W.", "given_names": "H. W.", "surname": "Duffield", "position": "Mechanical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "E. T. H. Wilkinson", "canonical_name": "Wilkinson, E. T. H.", "given_names": "E. T. H.", "surname": "Wilkinson", "position": "Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "A. Baynham", "canonical_name": "Baynham, A.", "given_names": "A.", "surname": "Baynham", "position": "Assistant Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 360, "salary_max": 460},
    {"name": "A. Wallis", "canonical_name": "Wallis, A.", "given_names": "A.", "surname": "Wallis", "position": "Wireless Electrician", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. Heys", "canonical_name": "Heys, H.", "given_names": "H.", "surname": "Heys", "position": "Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 540, "salary_max": 720},
    {"name": "C. H. Philp", "canonical_name": "Philp, C. H.", "given_names": "C. H.", "surname": "Philp", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "A. R. Woods", "canonical_name": "Woods, A. R.", "given_names": "A. R.", "surname": "Woods", "position": "Architectural Draughtsman", "department": "Public Works Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk, 1st Grade", "department": "Public Works Department - Gambia", "salary_min": 260, "salary_max": 360}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
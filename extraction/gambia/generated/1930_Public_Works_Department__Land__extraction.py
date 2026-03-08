"""
Gambia Colonial Office List 1930 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1930

OFFICIALS = [
    {"name": "H. A. Tyler-Smith", "canonical_name": "Tyler-Smith, H. A.", "given_names": "H. A.", "surname": "Tyler-Smith", "position": "Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "P. G. Burrage", "canonical_name": "Burrage, P. G.", "given_names": "P. G.", "surname": "Burrage", "position": "Assistant Engineer", "department": "Public Works Department - Gambia", "salary_min": 600, "salary_max": 720},
    {"name": "H. F. Gibbons", "canonical_name": "Gibbons, H. F.", "given_names": "H. F.", "surname": "Gibbons", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "S. Geering", "canonical_name": "Geering, S.", "given_names": "S.", "surname": "Geering", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. W. Duffield", "canonical_name": "Duffield, H. W.", "given_names": "H. W.", "surname": "Duffield", "position": "Mechanical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "E. T. H. Wilkinson", "canonical_name": "Wilkinson, E. T. H.", "given_names": "E. T. H.", "surname": "Wilkinson", "position": "Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "A. Baynham", "canonical_name": "Baynham, A.", "given_names": "A.", "surname": "Baynham", "position": "Assistant Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 360, "salary_max": 460},
    {"name": "A. Wallis", "canonical_name": "Wallis, A.", "given_names": "A.", "surname": "Wallis", "position": "Wireless Electrician", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. Heys", "canonical_name": "Heys, H.", "given_names": "H.", "surname": "Heys", "position": "Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 540, "salary_max": 720},
    {"name": "C. H. Philp", "canonical_name": "Philp, C. H.", "given_names": "C. H.", "surname": "Philp", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "A. R. Woods", "canonical_name": "Woods, A. R.", "given_names": "A. R.", "surname": "Woods", "position": "Architectural Draughtsman", "department": "Public Works Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk, 1st Grade", "department": "Public Works Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "W. H. McTurk", "canonical_name": "McTurk, W. H.", "given_names": "W. H.", "surname": "McTurk", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "L. Hagon", "canonical_name": "Hagon, L.", "given_names": "L.", "surname": "Hagon", "position": "Assistant Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "A. G. Still", "canonical_name": "Still, A. G.", "given_names": "A. G.", "surname": "Still", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 600, "salary_max": 920},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "Chief Clerk, 2nd Grade", "department": "Audit Office - Gambia", "salary_min": 160, "salary_max": 230}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
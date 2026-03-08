"""
Gambia Colonial Office List 1933 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1933

OFFICIALS = [
    {"name": "A. F. V. Vaughan", "canonical_name": "Vaughan, A. F. V.", "given_names": "A. F. V.", "surname": "Vaughan", "position": "Sanitary Inspector", "department": "Health Department - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "P. McDevitt", "canonical_name": "McDevitt, P.", "given_names": "P.", "surname": "McDevitt", "position": "Assistant Sanitary Inspector", "department": "Health Department - Gambia", "salary_min": 360, "salary_max": 460},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "P. G. Burrage", "canonical_name": "Burrage, P. G.", "given_names": "P. G.", "surname": "Burrage", "position": "Assistant Engineer", "department": "Public Works Department - Gambia", "salary_min": 600, "salary_max": 720},
    {"name": "H. F. Gibbons", "canonical_name": "Gibbons, H. F.", "given_names": "H. F.", "surname": "Gibbons", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "S. Geering", "canonical_name": "Geering, S.", "given_names": "S.", "surname": "Geering", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. W. Duffield", "canonical_name": "Duffield, H. W.", "given_names": "H. W.", "surname": "Duffield", "position": "Mechanical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 580},
    {"name": "H. Brough", "canonical_name": "Brough, H.", "given_names": "H.", "surname": "Brough", "position": "Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "A. Baynham", "canonical_name": "Baynham, A.", "given_names": "A.", "surname": "Baynham", "position": "Assistant Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 360, "salary_max": 460},
    {"name": "H. Heya", "canonical_name": "Heya, H.", "given_names": "H.", "surname": "Heya", "position": "Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 540, "salary_max": 720},
    {"name": "C. H. Philp", "canonical_name": "Philp, C. H.", "given_names": "C. H.", "surname": "Philp", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk, 1st Grade", "department": "Public Works Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "W. H. McTurk", "canonical_name": "McTurk, W. H.", "given_names": "W. H.", "surname": "McTurk", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Chief Clerk, 1st Grade", "department": "Land and Survey Department - Gambia", "salary_min": 260, "salary_max": 360},
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
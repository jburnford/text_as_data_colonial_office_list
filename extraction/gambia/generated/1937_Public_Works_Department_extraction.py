"""
Gambia Colonial Office List 1937 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1937

OFFICIALS = [
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 1050, "salary_max": 1050, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "P. G. Burrage", "canonical_name": "Burrage, P. G.", "given_names": "P. G.", "surname": "Burrage", "position": "Assistant Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 600, "salary_max": 720},
    {"name": "S. Geering", "canonical_name": "Geering, S.", "given_names": "S.", "surname": "Geering", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "E. C. Parker", "canonical_name": "Parker, E. C.", "given_names": "E. C.", "surname": "Parker", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. W. Duffield", "canonical_name": "Duffield, H. W.", "given_names": "H. W.", "surname": "Duffield", "position": "Mechanical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. Brough", "canonical_name": "Brough, H.", "given_names": "H.", "surname": "Brough", "position": "Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "W. P. Howell", "canonical_name": "Howell, W. P.", "given_names": "W. P.", "surname": "Howell", "position": "Assistant Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 360, "salary_max": 460},
    {"name": "C. H. Philip", "canonical_name": "Philip, C. H.", "given_names": "C. H.", "surname": "Philip", "position": "Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 525, "salary_max": 720},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 400, "salary_max": 630},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "Chief Clerk, 1st Grade", "department": "Public Works Department - Gambia", "salary_min": 260, "salary_max": 360}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
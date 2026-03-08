"""
Gambia Colonial Office List 1939 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1939

OFFICIALS = [
    {"name": "Dr. Ll. H. Thomas", "canonical_name": "Thomas, Ll. H.", "given_names": "Ll. H.", "surname": "Thomas", "position": "Medical Officer of Health", "department": "Health Department - Gambia"},
    {"name": "E. J. Snell", "canonical_name": "Snell, E. J.", "given_names": "E. J.", "surname": "Snell", "position": "Senior Sanitary Superintendent", "department": "Health Department - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "P. McDevitt", "canonical_name": "McDevitt, P.", "given_names": "P.", "surname": "McDevitt", "position": "Sanitary Superintendent", "department": "Health Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "Major J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 960, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major", "duty_allowance": 96},
    {"name": "P. G. Burrage", "canonical_name": "Burrage, P. G.", "given_names": "P. G.", "surname": "Burrage", "position": "Assistant Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 600, "salary_max": 720},
    {"name": "R. W. Wilcockes", "canonical_name": "Wilcockes, R. W.", "given_names": "R. W.", "surname": "Wilcockes", "position": "Technical Office Assistant", "department": "Public Works Department - Gambia", "salary_min": 475, "salary_max": 660},
    {"name": "S. Geering", "canonical_name": "Geering, S.", "given_names": "S.", "surname": "Geering", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "E. C. Parker", "canonical_name": "Parker, E. C.", "given_names": "E. C.", "surname": "Parker", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. W. Duffield", "canonical_name": "Duffield, H. W.", "given_names": "H. W.", "surname": "Duffield", "position": "Mechanical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. Brough", "canonical_name": "Brough, H.", "given_names": "H.", "surname": "Brough", "position": "Electrical Superintendent", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 600},
    {"name": "W. P. Howell", "canonical_name": "Howell, W. P.", "given_names": "W. P.", "surname": "Howell", "position": "Assistant Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 360, "salary_max": 460},
    {"name": "C. H. Philip", "canonical_name": "Philip, C. H.", "given_names": "C. H.", "surname": "Philip", "position": "Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 525, "salary_max": 720},
    {"name": "M. L. Valentine", "canonical_name": "Valentine, M. L.", "given_names": "M. L.", "surname": "Valentine", "position": "Chief Clerk", "department": "Public Works Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "E. G. C. Gabbidon", "canonical_name": "Gabbidon, E. G. C.", "given_names": "E. G. C.", "surname": "Gabbidon", "position": "Accounting Assistant", "department": "Public Works Department - Gambia", "salary_min": 260, "salary_max": 360}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
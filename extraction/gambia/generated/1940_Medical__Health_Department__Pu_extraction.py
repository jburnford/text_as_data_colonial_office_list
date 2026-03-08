"""
Gambia Colonial Office List 1940 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1940

OFFICIALS = [
    {"name": "C. Wilson", "canonical_name": "Wilson, C.", "given_names": "C.", "surname": "Wilson", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1000, "salary_max": 1150},
    {"name": "M. Clayton-Mitchell", "canonical_name": "Clayton-Mitchell, M.", "given_names": "M.", "surname": "Clayton-Mitchell", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 1150},
    {"name": "C. W. Bowesman", "canonical_name": "Bowesman, C. W.", "given_names": "C. W.", "surname": "Bowesman", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 1150},
    {"name": "B. J. Green", "canonical_name": "Green, B. J.", "given_names": "B. J.", "surname": "Green", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 1150},
    {"name": "J. Bright-Richards", "canonical_name": "Bright-Richards, J.", "given_names": "J.", "surname": "Bright-Richards", "position": "African Medical Officer", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 720},
    {"name": "S. H. O. Jones", "canonical_name": "Jones, S. H. O.", "given_names": "S. H. O.", "surname": "Jones", "position": "African Medical Officer", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 720},
    {"name": "K. W. Storrier", "canonical_name": "Storrier, K. W.", "given_names": "K. W.", "surname": "Storrier", "position": "Senior Nursing Sister", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600, "honors": ["M.B.E."], "duty_allowance": 40},
    {"name": "J. M. Cruickshank", "canonical_name": "Cruickshank, J. M.", "given_names": "J. M.", "surname": "Cruickshank", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
    {"name": "Ll. H. Thomas", "canonical_name": "Thomas, Ll. H.", "given_names": "Ll. H.", "surname": "Thomas", "position": "Medical Officer of Health", "department": "Health Department - Gambia", "salary_min": 660, "salary_max": 1150},
    {"name": "E. J. Snell", "canonical_name": "Snell, E. J.", "given_names": "E. J.", "surname": "Snell", "position": "Senior Sanitary Superintendent", "department": "Health Department - Gambia", "salary_min": 500, "salary_max": 600},
    {"name": "P. McDevitt", "canonical_name": "McDevitt, P.", "given_names": "P.", "surname": "McDevitt", "position": "Sanitary Superintendent", "department": "Health Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 960, "salary_max": 960, "military_rank": "Major", "honors": ["M.C."], "duty_allowance": 96},
    {"name": "E. H. Marfleet", "canonical_name": "Marfleet, E. H.", "given_names": "E. H.", "surname": "Marfleet", "position": "Assistant Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 480, "salary_max": 960},
    {"name": "R. W. Willcocks", "canonical_name": "Willcocks, R. W.", "given_names": "R. W.", "surname": "Willcocks", "position": "Technical Office Assistant", "department": "Public Works Department - Gambia", "salary_min": 475, "salary_max": 860},
    {"name": "S. Geering", "canonical_name": "Geering, S.", "given_names": "S.", "surname": "Geering", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "E. C. Parker", "canonical_name": "Parker, E. C.", "given_names": "E. C.", "surname": "Parker", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 440, "salary_max": 560},
    {"name": "H. W. Duffield", "canonical_name": "Duffield, H. W.", "given_names": "H. W.", "surname": "Duffield", "position": "Mechanical and Waterworks Superintendent", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. Brough", "canonical_name": "Brough, H.", "given_names": "H.", "surname": "Brough", "position": "Electrical Superintendent", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 600},
    {"name": "W. P. Howell", "canonical_name": "Howell, W. P.", "given_names": "W. P.", "surname": "Howell", "position": "Assistant Electrical Foreman", "department": "Public Works Department - Gambia", "salary_min": 360, "salary_max": 460},
    {"name": "C. H. Philip", "canonical_name": "Philip, C. H.", "given_names": "C. H.", "surname": "Philip", "position": "Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 525, "salary_max": 720},
    {"name": "M. L. Valentine", "canonical_name": "Valentine, M. L.", "given_names": "M. L.", "surname": "Valentine", "position": "Chief Clerk, 1st Grade", "department": "Public Works Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "E. G. C. Gabbidon", "canonical_name": "Gabbidon, E. G. C.", "given_names": "E. G. C.", "surname": "Gabbidon", "position": "Accounting Assistant, 1st Grade", "department": "Public Works Department - Gambia", "salary_min": 260, "salary_max": 360},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
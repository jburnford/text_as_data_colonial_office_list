"""
Gambia Colonial Office List 1931 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1931

OFFICIALS = [
    {"name": "E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["O.B.E."], "military_rank": "Captain"},
    {"name": "R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "L. A. W. Brooks", "canonical_name": "Brooks, L. A. W.", "given_names": "L. A. W.", "surname": "Brooks", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Major"},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "T. W. Doke", "canonical_name": "Doke, T. W.", "given_names": "T. W.", "surname": "Doke", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "P. Jeffs", "canonical_name": "Jeffs, P.", "given_names": "P.", "surname": "Jeffs", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Bandmaster", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Inspector of Prisons", "department": "Prison - Gambia"},
    {"name": "D. T. Birt", "canonical_name": "Birt, D. T.", "given_names": "D. T.", "surname": "Birt", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1000, "salary_max": 1150},
    {"name": "A. M. W. Rae", "canonical_name": "Rae, A. M. W.", "given_names": "A. M. W.", "surname": "Rae", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960},
    {"name": "S. G. Harrison", "canonical_name": "Harrison, S. G.", "given_names": "S. G.", "surname": "Harrison", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960},
    {"name": "C. K. G. Nunns", "canonical_name": "Nunns, C. K. G.", "given_names": "C. K. G.", "surname": "Nunns", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960},
    {"name": "D. S. Johnston", "canonical_name": "Johnston, D. S.", "given_names": "D. S.", "surname": "Johnston", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960},
    {"name": "E. Corderer", "canonical_name": "Corderer, E.", "given_names": "E.", "surname": "Corderer", "position": "Senior Nursing Sister", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600},
    {"name": "J. Roberts", "canonical_name": "Roberts, J.", "given_names": "J.", "surname": "Roberts", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
    {"name": "T. Grant", "canonical_name": "Grant, T.", "given_names": "T.", "surname": "Grant", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
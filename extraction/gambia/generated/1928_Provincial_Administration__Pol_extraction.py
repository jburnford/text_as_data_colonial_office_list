"""
Gambia Colonial Office List 1928 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1928

OFFICIALS = [
    {"name": "Dr. K. Hopkinson", "canonical_name": "Hopkinson, K.", "given_names": "K.", "surname": "Hopkinson", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Dr."},
    {"name": "Capt. E. B. Lees", "canonical_name": "Lees, E. B.", "given_names": "E. B.", "surname": "Lees", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "Major R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "Major L. A. W. Brooks", "canonical_name": "Brooks, L. A. W.", "given_names": "L. A. W.", "surname": "Brooks", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Major"},
    {"name": "Captain P. Jeffs", "canonical_name": "Jeffs, P.", "given_names": "P.", "surname": "Jeffs", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "Captain T. W. Doke", "canonical_name": "Doke, T. W.", "given_names": "T. W.", "surname": "Doke", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "Capt. Clinton H. Greig", "canonical_name": "Greig, Clinton H.", "given_names": "Clinton H.", "surname": "Greig", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72, "military_rank": "Captain"},
    {"name": "H. L. Wobley", "canonical_name": "Wobley, H. L.", "given_names": "H. L.", "surname": "Wobley", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "C. R. Bell", "canonical_name": "Bell, C. R.", "given_names": "C. R.", "surname": "Bell", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Bandmaster", "department": "Police Force - Gambia", "salary_min": 350, "salary_max": 450},
    {"name": "Capt. Clinton H. Greig", "canonical_name": "Greig, Clinton H.", "given_names": "Clinton H.", "surname": "Greig", "position": "Inspector of Prisons", "department": "Prison - Gambia", "military_rank": "Captain"},
    {"name": "T. B. Shyngle", "canonical_name": "Shyngle, T. B.", "given_names": "T. B.", "surname": "Shyngle", "position": "Gaoler, 2nd Grade", "department": "Prison - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "Rev. L. W. Humphrey", "canonical_name": "Humphrey, L. W.", "given_names": "L. W.", "surname": "Humphrey", "position": "Chaplain", "department": "Prison - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
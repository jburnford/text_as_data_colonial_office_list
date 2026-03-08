"""
Gambia Colonial Office List 1921 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1921

OFFICIALS = [
    {"name": "H. C. T. Strange", "canonical_name": "Strange, H. C. T.", "given_names": "H. C. T.", "surname": "Strange", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "duty_allowance": 54, "honors": ["D.S.O.", "M.C."], "military_rank": "Captain"},
    {"name": "E. P. Edyvean", "canonical_name": "Edyvean, E. P.", "given_names": "E. P.", "surname": "Edyvean", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 510, "salary_max": 510, "military_rank": "Lieutenant"},
    {"name": "L. C. Evans", "canonical_name": "Evans, L. C.", "given_names": "L. C.", "surname": "Evans", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 510, "salary_max": 510, "military_rank": "Lieutenant"},
    {"name": "F. A. Coward", "canonical_name": "Coward, F. A.", "given_names": "F. A.", "surname": "Coward", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 510, "salary_max": 510, "military_rank": "Lieutenant"},
    {"name": "T. A. Moir", "canonical_name": "Moir, T. A.", "given_names": "T. A.", "surname": "Moir", "position": "Colour-Sergeant, Company Quartermaster Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 370, "salary_max": 370},
    {"name": "Joseph Jobe", "canonical_name": "Jobe, Joseph", "given_names": "Joseph", "surname": "Jobe", "position": "Clerk and Schoolmaster", "department": "West African Frontier Force - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72, "per_diem": "2s. 3d. per diem forage allowance", "military_rank": "Captain"},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 450, "salary_max": 720, "per_diem": "2s. 3d. per diem forage allowance"},
    {"name": "A. Minnock", "canonical_name": "Minnock, A.", "given_names": "A.", "surname": "Minnock", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "G. T. Lawrence", "canonical_name": "Lawrence, G. T.", "given_names": "G. T.", "surname": "Lawrence", "position": "Bandmaster and Quarter-master", "department": "Police Force - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Inspector of Prisons", "department": "Prison - Gambia", "military_rank": "Captain"},
    {"name": "E. J. Powell", "canonical_name": "Powell, E. J.", "given_names": "E. J.", "surname": "Powell", "position": "Chaplain", "department": "Prison - Gambia", "qualifications": ["Rev."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
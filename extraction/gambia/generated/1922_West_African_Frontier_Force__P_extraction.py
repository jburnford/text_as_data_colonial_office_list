"""
Gambia Colonial Office List 1922 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1922

OFFICIALS = [
    {"name": "H. C. T. Stronge", "canonical_name": "Stronge, H. C. T.", "given_names": "H. C. T.", "surname": "Stronge", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "duty_allowance": 54, "honors": ["D.S.O.", "M.C."], "military_rank": "Captain"},
    {"name": "E. P. Edyvean", "canonical_name": "Edyvean, E. P.", "given_names": "E. P.", "surname": "Edyvean", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "L. C. Evans", "canonical_name": "Evans, L. C.", "given_names": "L. C.", "surname": "Evans", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "F. A. Coward", "canonical_name": "Coward, F. A.", "given_names": "F. A.", "surname": "Coward", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "J. A. Moir", "canonical_name": "Moir, J. A.", "given_names": "J. A.", "surname": "Moir", "position": "Company Quartermaster Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 370, "salary_max": 370},
    {"name": "H. J. Jowers", "canonical_name": "Jowers, H. J.", "given_names": "H. J.", "surname": "Jowers", "position": "Platoon Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "Joseph Jobe", "canonical_name": "Jobe, Joseph", "given_names": "Joseph", "surname": "Jobe", "position": "Clerk and Schoolmaster", "department": "West African Frontier Force - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "Clinton H. Greig", "canonical_name": "Greig, Clinton H.", "given_names": "Clinton H.", "surname": "Greig", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72, "military_rank": "Captain"},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "A. Minnock", "canonical_name": "Minnock, A.", "given_names": "A.", "surname": "Minnock", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "G. T. Lawrence", "canonical_name": "Lawrence, G. T.", "given_names": "G. T.", "surname": "Lawrence", "position": "Bandmaster and Quartermaster", "department": "Police Force - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Gaoler", "department": "Prison - Gambia", "salary_min": 120, "salary_max": 120, "allowances": "24l. house allowance"},
    {"name": "T. B. Shingle", "canonical_name": "Shingle, T. B.", "given_names": "T. B.", "surname": "Shingle", "position": "Chief Warden", "department": "Prison - Gambia", "salary_min": 60, "salary_max": 84},
    {"name": "E. J. Powell", "canonical_name": "Powell, E. J.", "given_names": "E. J.", "surname": "Powell", "position": "Chaplain", "department": "Prison - Gambia", "qualifications": ["Rev."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1929 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1929

OFFICIALS = [
    {"name": "Clinton H. Greig", "canonical_name": "Greig, Clinton H.", "given_names": "Clinton H.", "surname": "Greig", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72, "military_rank": "Captain"},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "C. R. Bell", "canonical_name": "Bell, C. R.", "given_names": "C. R.", "surname": "Bell", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Bandmaster", "department": "Police Force - Gambia", "salary_min": 350, "salary_max": 450},
    {"name": "Clinton H. Greig", "canonical_name": "Greig, Clinton H.", "given_names": "Clinton H.", "surname": "Greig", "position": "Inspector of Prisons", "department": "Prison - Gambia", "military_rank": "Captain"},
    {"name": "T. B. Shynge", "canonical_name": "Shynge, T. B.", "given_names": "T. B.", "surname": "Shynge", "position": "Gaoler, 2nd Grade", "department": "Prison - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "L. W. Humphrey", "canonical_name": "Humphrey, L. W.", "given_names": "L. W.", "surname": "Humphrey", "position": "Chaplain", "department": "Prison - Gambia", "qualifications": ["Rev."]},
    {"name": "K. B. Allan", "canonical_name": "Allan, K. B.", "given_names": "K. B.", "surname": "Allan", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1000, "salary_max": 1150, "allowances": "250l. staff and seniority allowances"},
    {"name": "J. C. Cruickshank", "canonical_name": "Cruickshank, J. C.", "given_names": "J. C.", "surname": "Cruickshank", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "A. M. W. Rae", "canonical_name": "Rae, A. M. W.", "given_names": "A. M. W.", "surname": "Rae", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "S. G. Harrison", "canonical_name": "Harrison, S. G.", "given_names": "S. G.", "surname": "Harrison", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "M. Thompson", "canonical_name": "Thompson, M.", "given_names": "M.", "surname": "Thompson", "position": "Senior Nursing Sister", "department": "Medical - Gambia", "salary_min": 380, "salary_max": 440, "allowances": "40l. charge allowance"},
    {"name": "J. Roberts", "canonical_name": "Roberts, J.", "given_names": "J.", "surname": "Roberts", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "T. Grant", "canonical_name": "Grant, T.", "given_names": "T.", "surname": "Grant", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "Chief Dispenser and Storekeeper, 2nd Grade", "department": "Medical - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "E. W. Johns", "canonical_name": "Johns, E. W.", "given_names": "E. W.", "surname": "Johns", "position": "Dispensers, 2nd Grade", "department": "Medical - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "W. M. Rollings", "canonical_name": "Rollings, W. M.", "given_names": "W. M.", "surname": "Rollings", "position": "Dispensers, 2nd Grade", "department": "Medical - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "T. R. King", "canonical_name": "King, T. R.", "given_names": "T. R.", "surname": "King", "position": "2nd Grade Clerk", "department": "Medical - Gambia", "salary_min": 160, "salary_max": 230}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
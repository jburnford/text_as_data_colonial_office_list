"""
Gambia Colonial Office List 1932 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1932

OFFICIALS = [
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72},
    {"name": "Capt. R. L. Hill", "canonical_name": "Hill, R. L.", "given_names": "R. L.", "surname": "Hill", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 720, "military_rank": "Captain"},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "T. A. Medhurst", "canonical_name": "Medhurst, T. A.", "given_names": "T. A.", "surname": "Medhurst", "position": "Assistant Bandmaster", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Inspector of Prisons", "department": "Prison - Gambia"},
    {"name": "D. T. Birt", "canonical_name": "Birt, D. T.", "given_names": "D. T.", "surname": "Birt", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1000, "salary_max": 1150, "allowances": "250l. staff and seniority allowances"},
    {"name": "H. J. Birmingham", "canonical_name": "Birmingham, H. J.", "given_names": "H. J.", "surname": "Birmingham", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "C. K. G. Nunnis", "canonical_name": "Nunnis, C. K. G.", "given_names": "C. K. G.", "surname": "Nunnis", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "D. S. Johnston", "canonical_name": "Johnston, D. S.", "given_names": "D. S.", "surname": "Johnston", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "E. Corderer", "canonical_name": "Corderer, E.", "given_names": "E.", "surname": "Corderer", "position": "Senior Nursing Sister", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600, "allowances": "40l. charge allowance"},
    {"name": "E. M. Sheaff", "canonical_name": "Sheaff, E. M.", "given_names": "E. M.", "surname": "Sheaff", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
    {"name": "M. E. Barton", "canonical_name": "Barton, M. E.", "given_names": "M. E.", "surname": "Barton", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
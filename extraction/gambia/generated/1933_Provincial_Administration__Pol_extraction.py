"""
Gambia Colonial Office List 1933 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1933

OFFICIALS = [
    {"name": "E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["O.B.E."], "military_rank": "Capt."},
    {"name": "R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "H. R. Oke", "canonical_name": "Oke, H. R.", "given_names": "H. R.", "surname": "Oke", "position": "Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "P. Jeffs", "canonical_name": "Jeffs, P.", "given_names": "P.", "surname": "Jeffs", "position": "Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "G. N. N. Nunn", "canonical_name": "Nunn, G. N. N.", "given_names": "G. N. N.", "surname": "Nunn", "position": "Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "N. M. Asheton", "canonical_name": "Asheton, N. M.", "given_names": "N. M.", "surname": "Asheton", "position": "Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72},
    {"name": "R. L. Hill", "canonical_name": "Hill, R. L.", "given_names": "R. L.", "surname": "Hill", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 720, "military_rank": "Capt."},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "T. A. Medhurst", "canonical_name": "Medhurst, T. A.", "given_names": "T. A.", "surname": "Medhurst", "position": "Assistant Bandmaster", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Inspector of Prisons", "department": "Prison - Gambia"},
    {"name": "D. T. Birt", "canonical_name": "Birt, D. T.", "given_names": "D. T.", "surname": "Birt", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1000, "salary_max": 1150, "allowances": "250l. staff and seniority allowances"},
    {"name": "H. J. Birmingham", "canonical_name": "Birmingham, H. J.", "given_names": "H. J.", "surname": "Birmingham", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "H. B. Boucher", "canonical_name": "Boucher, H. B.", "given_names": "H. B.", "surname": "Boucher", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "D. S. Johnston", "canonical_name": "Johnston, D. S.", "given_names": "D. S.", "surname": "Johnston", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "E. Cordiner", "canonical_name": "Cordiner, E.", "given_names": "E.", "surname": "Cordiner", "position": "Senior Nursing Sister", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600, "allowances": "40l. charge allowance"},
    {"name": "E. M. Sheaff", "canonical_name": "Sheaff, E. M.", "given_names": "E. M.", "surname": "Sheaff", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
    {"name": "M. E. Barton", "canonical_name": "Barton, M. E.", "given_names": "M. E.", "surname": "Barton", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
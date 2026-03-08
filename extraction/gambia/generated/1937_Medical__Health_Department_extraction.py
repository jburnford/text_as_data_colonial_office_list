"""
Gambia Colonial Office List 1937 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1937

OFFICIALS = [
    {"name": "A. M. W. Rae", "canonical_name": "Rae, A. M. W.", "given_names": "A. M. W.", "surname": "Rae", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1000, "salary_max": 1150, "allowances": "250l. staff and seniority allowances personal."},
    {"name": "H. J. Bermingham", "canonical_name": "Bermingham, H. J.", "given_names": "H. J.", "surname": "Bermingham", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance from 720l. personal."},
    {"name": "T. H. Dalrymple", "canonical_name": "Dalrymple, T. H.", "given_names": "T. H.", "surname": "Dalrymple", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance from 720l. personal."},
    {"name": "J. L. Lochhead", "canonical_name": "Lochhead, J. L.", "given_names": "J. L.", "surname": "Lochhead", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance from 720l. personal."},
    {"name": "C. W. Bowesman", "canonical_name": "Bowesman, C. W.", "given_names": "C. W.", "surname": "Bowesman", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance from 720l. personal."},
    {"name": "M. Clayton-Mitchell", "canonical_name": "Clayton-Mitchell, M.", "given_names": "M.", "surname": "Clayton-Mitchell", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "qualifications": ["L.R.C.P.", "L.R.C.S."], "allowances": "72l. seniority allowance from 720l. personal."},
    {"name": "J. Bright-Richards", "canonical_name": "Bright-Richards, J.", "given_names": "J.", "surname": "Bright-Richards", "position": "African Medical Officer", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 720},
    {"name": "S. H. O. Jones", "canonical_name": "Jones, S. H. O.", "given_names": "S. H. O.", "surname": "Jones", "position": "African Medical Officer", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 720},
    {"name": "F. Roche", "canonical_name": "Roche, F.", "given_names": "F.", "surname": "Roche", "position": "Senior Nursing Sister", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 40},
    {"name": "W. M. Harper", "canonical_name": "Harper, W. M.", "given_names": "W. M.", "surname": "Harper", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
    {"name": "A. M. Fraser", "canonical_name": "Fraser, A. M.", "given_names": "A. M.", "surname": "Fraser", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
    {"name": "G. R. Baxter", "canonical_name": "Baxter, G. R.", "given_names": "G. R.", "surname": "Baxter", "position": "Medical Officer of Health", "department": "Health Department - Gambia"},
    {"name": "E. J. Snell", "canonical_name": "Snell, E. J.", "given_names": "E. J.", "surname": "Snell", "position": "Senior Sanitary Superintendent", "department": "Health Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "P. McDevitt", "canonical_name": "McDevitt, P.", "given_names": "P.", "surname": "McDevitt", "position": "Sanitary Superintendent", "department": "Health Department - Gambia", "salary_min": 400, "salary_max": 460}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
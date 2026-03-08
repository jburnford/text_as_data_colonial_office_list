"""
Gambia Colonial Office List 1934 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1934

OFFICIALS = [
    {"name": "D. T. Birt", "canonical_name": "Birt, D. T.", "given_names": "D. T.", "surname": "Birt", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1000, "salary_max": 1150, "allowances": "250l. staff and seniority allowances"},
    {"name": "H. J. Birmingham", "canonical_name": "Birmingham, H. J.", "given_names": "H. J.", "surname": "Birmingham", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "H. B. Boucher", "canonical_name": "Boucher, H. B.", "given_names": "H. B.", "surname": "Boucher", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "D. S. Johnston", "canonical_name": "Johnston, D. S.", "given_names": "D. S.", "surname": "Johnston", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. Bright-Richards", "canonical_name": "Bright-Richards, J.", "given_names": "J.", "surname": "Bright-Richards", "position": "Junior African Medical Officer", "department": "Medical - Gambia"},
    {"name": "M. K. Parr", "canonical_name": "Parr, M. K.", "given_names": "M. K.", "surname": "Parr", "position": "Senior Nursing Sister", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600, "allowances": "40l. charge allowance"},
    {"name": "E. M. Sheaff", "canonical_name": "Sheaff, E. M.", "given_names": "E. M.", "surname": "Sheaff", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
    {"name": "K. Edwards", "canonical_name": "Edwards, K.", "given_names": "K.", "surname": "Edwards", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
    {"name": "A. F. V. Vaughan", "canonical_name": "Vaughan, A. F. V.", "given_names": "A. F. V.", "surname": "Vaughan", "position": "Sanitary Inspector", "department": "Health Department - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "P. McDevitt", "canonical_name": "McDevitt, P.", "given_names": "P.", "surname": "McDevitt", "position": "Assistant Sanitary Inspector", "department": "Health Department - Gambia", "salary_min": 360, "salary_max": 460}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
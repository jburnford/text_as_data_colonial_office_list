"""
Gambia Colonial Office List 1939 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1939

OFFICIALS = [
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 750, "salary_max": 920, "duty_allowance": 72},
    {"name": "R. L. Hill", "canonical_name": "Hill, R. L.", "given_names": "R. L.", "surname": "Hill", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 750, "military_rank": "Captain"},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Chief Inspector", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "T. A. Medhurst", "canonical_name": "Medhurst, T. A.", "given_names": "T. A.", "surname": "Medhurst", "position": "Bandmaster", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Inspector of Prisons", "department": "Prison - Gambia"},
    {"name": "C. Wilson", "canonical_name": "Wilson, C.", "given_names": "C.", "surname": "Wilson", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1200, "salary_max": 1200},
    {"name": "M. Clayton-Mitchell", "canonical_name": "Clayton-Mitchell, M.", "given_names": "M.", "surname": "Clayton-Mitchell", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 1000},
    {"name": "J. L. Lochhead", "canonical_name": "Lochhead, J. L.", "given_names": "J. L.", "surname": "Lochhead", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 1000},
    {"name": "C. W. Bowesman", "canonical_name": "Bowesman, C. W.", "given_names": "C. W.", "surname": "Bowesman", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 1000},
    {"name": "B. J. Green", "canonical_name": "Green, B. J.", "given_names": "B. J.", "surname": "Green", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 1000},
    {"name": "J. Bright-Richards", "canonical_name": "Bright-Richards, J.", "given_names": "J.", "surname": "Bright-Richards", "position": "African Medical Officer", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 720},
    {"name": "S. H. O. Jones", "canonical_name": "Jones, S. H. O.", "given_names": "S. H. O.", "surname": "Jones", "position": "African Medical Officer", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 720},
    {"name": "F. Roche", "canonical_name": "Roche, F.", "given_names": "F.", "surname": "Roche", "position": "Senior Nursing Sister", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 630, "duty_allowance": 40},
    {"name": "A. M. Fraser", "canonical_name": "Fraser, A. M.", "given_names": "A. M.", "surname": "Fraser", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480},
    {"name": "R. B. Tryhorn", "canonical_name": "Tryhorn, R. B.", "given_names": "R. B.", "surname": "Tryhorn", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 350, "salary_max": 480}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
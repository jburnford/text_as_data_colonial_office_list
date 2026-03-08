"""
Gambia Colonial Office List 1929 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1929

OFFICIALS = [
    {"name": "A. J. Brooks", "canonical_name": "Brooks, A. J.", "given_names": "A. J.", "surname": "Brooks", "position": "Director of Agriculture", "department": "Agricultural Department - Gambia", "salary_min": 600, "salary_max": 920, "qualifications": ["F.I.A.S.", "F.C.S.", "F.R.H.S."]},
    {"name": "J. Pirie", "canonical_name": "Pirie, J.", "given_names": "J.", "surname": "Pirie", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 450, "salary_max": 600},
    {"name": "J. W. Sparrow", "canonical_name": "Sparrow, J. W.", "given_names": "J. W.", "surname": "Sparrow", "position": "Assistant Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "T. R. Hayes", "canonical_name": "Hayes, T. R.", "given_names": "T. R.", "surname": "Hayes", "position": "Agricultural Assistant in Charge of Seed Farms", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "C. S. Burt", "canonical_name": "Burt, C. S.", "given_names": "C. S.", "surname": "Burt", "position": "Officer Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "duty_allowance": 54, "military_rank": "Captain", "honors": ["D.S.O."]},
    {"name": "A. J. Chrystal", "canonical_name": "Chrystal, A. J.", "given_names": "A. J.", "surname": "Chrystal", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "B. W. Wright", "canonical_name": "Wright, B. W.", "given_names": "B. W.", "surname": "Wright", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "A. J. Brown", "canonical_name": "Brown, A. J.", "given_names": "A. J.", "surname": "Brown", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
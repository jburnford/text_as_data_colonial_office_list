"""
Gambia Colonial Office List 1936 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1936

OFFICIALS = [
    {"name": "M. M. Auchinleck", "canonical_name": "Auchinleck, M. M.", "given_names": "M. M.", "surname": "Auchinleck", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 720, "salary_max": 960, "duty_allowance": 72},
    {"name": "R. A. Brown", "canonical_name": "Brown, R. A.", "given_names": "R. A.", "surname": "Brown", "position": "Assistant Receiver-General", "department": "Treasury and Customs Branches - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "K. C. Jacobs", "canonical_name": "Jacobs, K. C.", "given_names": "K. C.", "surname": "Jacobs", "position": "Treasury Accountant", "department": "Treasury and Customs Branches - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "C. C. du Boulay", "canonical_name": "du Boulay, C. C.", "given_names": "C. C.", "surname": "du Boulay", "position": "Supervisor of Customs", "department": "Treasury and Customs Branches - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "Chief Clerk, 1st Grade", "department": "Treasury and Customs Branches - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "Customs Landing Waiters (2nd Grade)", "department": "Treasury and Customs Branches - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "I. B. M. Y. Jobe", "canonical_name": "Jobe, I. B. M. Y.", "given_names": "I. B. M. Y.", "surname": "Jobe", "position": "Customs Landing Waiters (2nd Grade)", "department": "Treasury and Customs Branches - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "A. Wallis", "canonical_name": "Wallis, A.", "given_names": "A.", "surname": "Wallis", "position": "Postal Surveyor and Wireless Engineer", "department": "Posts and Telegraph Branch - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "Postmaster", "department": "Posts and Telegraph Branch - Gambia", "salary_min": 260, "salary_max": 360},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
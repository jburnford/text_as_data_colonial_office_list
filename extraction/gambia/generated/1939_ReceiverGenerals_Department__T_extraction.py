"""
Gambia Colonial Office List 1939 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1939

OFFICIALS = [
    {"name": "M. M. Auchinleck", "canonical_name": "Auchinleck, M. M.", "given_names": "M. M.", "surname": "Auchinleck", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 720, "salary_max": 900, "duty_allowance": 72},
    {"name": "K. C. Jacobs", "canonical_name": "Jacobs, K. C.", "given_names": "K. C.", "surname": "Jacobs", "position": "Assistant Receiver-General", "department": "Treasury and Customs Branches - Gambia", "salary_min": 400, "salary_max": 810},
    {"name": "A. W. Beardmore", "canonical_name": "Beardmore, A. W.", "given_names": "A. W.", "surname": "Beardmore", "position": "Treasury Accountant", "department": "Treasury and Customs Branches - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "C. C. du Boulay", "canonical_name": "du Boulay, C. C.", "given_names": "C. C.", "surname": "du Boulay", "position": "Collector of Customs", "department": "Treasury and Customs Branches - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "Chief Clerk, 1st Grade", "department": "Treasury and Customs Branches - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "Chief Landing Waiter, 1st Grade", "department": "Treasury and Customs Branches - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "Accounting Assistant, 1st Grade", "department": "Treasury and Customs Branches - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "H. F. Alton", "canonical_name": "Alton, H. F.", "given_names": "H. F.", "surname": "Alton", "position": "Postal Surveyor and Wireless Engineer", "department": "Posts and Telegraph Branch - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "Postmaster", "department": "Posts and Telegraph Branch - Gambia", "salary_min": 260, "salary_max": 360}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
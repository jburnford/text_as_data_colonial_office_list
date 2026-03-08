"""
Gambia Colonial Office List 1940 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1940

OFFICIALS = [
    {"name": "Sir (Wilfrid) Thomas Southorn", "canonical_name": "Southorn, (Wilfrid) Thomas", "given_names": "(Wilfrid) Thomas", "surname": "Southorn", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 750, "honors": ["K.C.M.G.", "K.B.E."]},
    {"name": "Captain T. N. Hawtin", "canonical_name": "Hawtin, T. N.", "given_names": "T. N.", "surname": "Hawtin", "position": "Aide-de Camp and Private Secretary", "department": "Civil Establishment - Gambia", "military_rank": "Captain"},
    {"name": "H. R. Oke", "canonical_name": "Oke, H. R.", "given_names": "H. R.", "surname": "Oke", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "honors": ["C.M.G."], "qualifications": ["M.C."]},
    {"name": "G. Amos", "canonical_name": "Amos, G.", "given_names": "G.", "surname": "Amos", "position": "Office Assistant", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 600, "honors": ["M.B.E."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "African Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 300, "salary_max": 455},
    {"name": "F. D. D. Roach", "canonical_name": "Roach, F. D. D.", "given_names": "F. D. D.", "surname": "Roach", "position": "Chief Clerk, 1st Grade", "department": "Secretariat - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "M. M. Auchinleck", "canonical_name": "Auchinleck, M. M.", "given_names": "M. M.", "surname": "Auchinleck", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 720, "salary_max": 960, "duty_allowance": 72},
    {"name": "K. C. Jacobs", "canonical_name": "Jacobs, K. C.", "given_names": "K. C.", "surname": "Jacobs", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 810},
    {"name": "A. W. Beardmore", "canonical_name": "Beardmore, A. W.", "given_names": "A. W.", "surname": "Beardmore", "position": "Treasury Accountant", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "C. C. du Boulay", "canonical_name": "du Boulay, C. C.", "given_names": "C. C.", "surname": "du Boulay", "position": "Collector of Customs", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "Superintendent of Customs", "department": "Receiver-General's Department - Gambia", "salary_min": 310, "salary_max": 400},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "Postmaster", "department": "Receiver-General's Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "Accounting Assistant, 1st Grade", "department": "Receiver-General's Department - Gambia", "salary_min": 260, "salary_max": 360}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
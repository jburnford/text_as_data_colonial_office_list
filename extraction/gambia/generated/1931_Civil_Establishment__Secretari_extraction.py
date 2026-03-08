"""
Gambia Colonial Office List 1931 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1931

OFFICIALS = [
    {"name": "H. R. Palmer", "canonical_name": "Palmer, H. R.", "given_names": "H. R.", "surname": "Palmer", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 750, "honors": ["C.M.G.", "C.B.E."]},
    {"name": "H. Lloyd-Carson", "canonical_name": "Lloyd-Carson, H.", "given_names": "H.", "surname": "Lloyd-Carson", "position": "Aide-de-Camp and Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 450, "salary_max": 450, "military_rank": "Capt."},
    {"name": "M. L. Valentine", "canonical_name": "Valentine, M. L.", "given_names": "M. L.", "surname": "Valentine", "position": "1st Grade Confidential Clerk", "department": "Civil Establishment - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "B. A. Finn", "canonical_name": "Finn, B. A.", "given_names": "B. A.", "surname": "Finn", "position": "Senior Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "B. P. E. Bulstrode", "canonical_name": "Bulstrode, B. P. E.", "given_names": "B. P. E.", "surname": "Bulstrode", "position": "2nd Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "G. Amos", "canonical_name": "Amos, G.", "given_names": "G.", "surname": "Amos", "position": "Office Assistant", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "African Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 300, "salary_max": 450},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "Chief Clerk, 1st Grade", "department": "Secretariat - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "Government Printer", "department": "Printing Branch - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "H. Denaham Smith", "canonical_name": "Smith, H. Denaham", "given_names": "H. Denaham", "surname": "Smith", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "A. T. Shill", "canonical_name": "Shill, A. T.", "given_names": "A. T.", "surname": "Shill", "position": "Assistant Receiver-Generals", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Receiver-Generals", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "Chief Clerk, 1st Grade", "department": "Receiver-General's Department - Gambia", "salary_min": 260, "salary_max": 360}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
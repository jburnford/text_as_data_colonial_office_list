"""
Gambia Colonial Office List 1932 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1932

OFFICIALS = [
    {"name": "H. R. Palmer", "canonical_name": "Palmer, H. R.", "given_names": "H. R.", "surname": "Palmer", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 750, "honors": ["C.M.G.", "C.B.E."]},
    {"name": "H. Lloyd-Carson", "canonical_name": "Lloyd-Carson, H.", "given_names": "H.", "surname": "Lloyd-Carson", "position": "Aide-de-Camp and Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 450, "salary_max": 450, "military_rank": "Capt."},
    {"name": "G. C. B. Pariah", "canonical_name": "Pariah, G. C. B.", "given_names": "G. C. B.", "surname": "Pariah", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "F. N. Huggins", "canonical_name": "Huggins, F. N.", "given_names": "F. N.", "surname": "Huggins", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "G. Amos", "canonical_name": "Amos, G.", "given_names": "G.", "surname": "Amos", "position": "Office Assistant", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "African Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 300, "salary_max": 450},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "Chief Clerk, 1st Grade", "department": "Secretariat - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "Government Printer", "department": "Printing Branch - Gambia", "salary_min": 260, "salary_max": 360}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
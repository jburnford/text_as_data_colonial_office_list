"""
Gambia Colonial Office List 1910 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1910

OFFICIALS = [
    {"name": "Sir G. C. Denton", "canonical_name": "Denton, G. C.", "given_names": "G. C.", "surname": "Denton", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "honors": ["K.C.M.G."]},
    {"name": "E. H. Kirkpatrick", "canonical_name": "Kirkpatrick, E. H.", "given_names": "E. H.", "surname": "Kirkpatrick", "position": "Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250, "military_rank": "Capt."},
    {"name": "J. P. Joof", "canonical_name": "Joof, J. P.", "given_names": "J. P.", "surname": "Joof", "position": "Governor's Clerk and Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "C.R.M. O'Brien", "canonical_name": "O'Brien, C.R.M.", "given_names": "C.R.M.", "surname": "O'Brien", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 700, "honors": ["C.M.G."], "military_rank": "Lt.-Col.", "duty_allowance": 100},
    {"name": "J. A. Mensah", "canonical_name": "Mensah, J. A.", "given_names": "J. A.", "surname": "Mensah", "position": "Chief Clerk", "department": "Secretariat - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Second Clerk", "department": "Secretariat - Gambia", "salary_min": 80, "salary_max": 125},
    {"name": "D. Kingdon", "canonical_name": "Kingdon, D.", "given_names": "D.", "surname": "Kingdon", "position": "Legal Assistant", "department": "Legal Assistant's Office - Gambia", "salary_min": 400, "salary_max": 450, "honors": ["Hon."]},
    {"name": "J. Finden Dailey", "canonical_name": "Dailey, J. Finden", "given_names": "J. Finden", "surname": "Dailey", "position": "Clerk", "department": "Legal Assistant's Office - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "F. B. Archer", "canonical_name": "Archer, F. B.", "given_names": "F. B.", "surname": "Archer", "position": "Treasurer", "department": "Treasury - Gambia", "salary_min": 500, "salary_max": 600, "honors": ["Hon."], "duty_allowance": 100},
    {"name": "C. C. Johnson", "canonical_name": "Johnson, C. C.", "given_names": "C. C.", "surname": "Johnson", "position": "Chief Clerk and Cashier", "department": "Treasury - Gambia", "salary_min": 175, "salary_max": 200},
    {"name": "P. Sowe", "canonical_name": "Sowe, P.", "given_names": "P.", "surname": "Sowe", "position": "First Clerk", "department": "Treasury - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "J. J. Fowlis", "canonical_name": "Fowlis, J. J.", "given_names": "J. J.", "surname": "Fowlis", "position": "Second Clerk", "department": "Treasury - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Third Clerk", "department": "Treasury - Gambia", "salary_min": 36, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
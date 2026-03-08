"""
Gambia Colonial Office List 1907 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1907

OFFICIALS = [
    {"name": "Sir G. C. Denton", "canonical_name": "Denton, G. C.", "given_names": "G. C.", "surname": "Denton", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 1500, "salary_max": 1500, "allowances": "600l. allowances", "honors": ["K.C.M.G."]},
    {"name": "Captain L. F. Scott", "canonical_name": "Scott, L. F.", "given_names": "L. F.", "surname": "Scott", "position": "Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250, "military_rank": "Captain"},
    {"name": "J. P. Joof", "canonical_name": "Joof, J. P.", "given_names": "J. P.", "surname": "Joof", "position": "Governor's Clerk and Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "Hon. H. M. Brandford Griffith", "canonical_name": "Griffith, H. M. Brandford", "given_names": "H. M.", "surname": "Griffith", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 100, "honors": ["C.M.G."]},
    {"name": "J. A. Mensah", "canonical_name": "Mensah, J. A.", "given_names": "J. A.", "surname": "Mensah", "position": "Chief Clerk", "department": "Secretariat - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Second Clerk", "department": "Secretariat - Gambia", "salary_min": 80, "salary_max": 125},
    {"name": "D. Kingdon", "canonical_name": "Kingdon, D.", "given_names": "D.", "surname": "Kingdon", "position": "Legal Assistant", "department": "Legal Assistant's Office - Gambia", "salary_min": 400, "salary_max": 450},
    {"name": "S. A. Peacock", "canonical_name": "Peacock, S. A.", "given_names": "S. A.", "surname": "Peacock", "position": "Clerk", "department": "Legal Assistant's Office - Gambia", "salary_min": 36, "salary_max": 36},
    {"name": "Hon. F. B. Archer", "canonical_name": "Archer, F. B.", "given_names": "F. B.", "surname": "Archer", "position": "Treasurer", "department": "Treasury - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 60},
    {"name": "S. D. A. Coker", "canonical_name": "Coker, S. D. A.", "given_names": "S. D. A.", "surname": "Coker", "position": "Chief Clerk and Cashier", "department": "Treasury - Gambia", "salary_min": 175, "salary_max": 200},
    {"name": "P. Sowe", "canonical_name": "Sowe, P.", "given_names": "P.", "surname": "Sowe", "position": "First Clerk", "department": "Treasury - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "R. S. Rendall", "canonical_name": "Rendall, R. S.", "given_names": "R. S.", "surname": "Rendall", "position": "Second Clerk", "department": "Treasury - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "J. J. Fowlis", "canonical_name": "Fowlis, J. J.", "given_names": "J. J.", "surname": "Fowlis", "position": "Third Clerk", "department": "Treasury - Gambia", "salary_min": 36, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
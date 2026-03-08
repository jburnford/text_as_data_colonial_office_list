"""
Gambia Colonial Office List 1913 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1913

OFFICIALS = [
    {"name": "H. L. Galway", "canonical_name": "Galway, H. L.", "given_names": "H. L.", "surname": "Galway", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "honors": ["K.C.M.G.", "D.S.O."], "military_rank": "Lt.-Col."},
    {"name": "A. M. Inglis", "canonical_name": "Inglis, A. M.", "given_names": "A. M.", "surname": "Inglis", "position": "Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250, "military_rank": "Capt."},
    {"name": "J. P. Joof", "canonical_name": "Joof, J. P.", "given_names": "J. P.", "surname": "Joof", "position": "Governor's Clerk and Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "W. T. Campbell", "canonical_name": "Campbell, W. T.", "given_names": "W. T.", "surname": "Campbell", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "A. C. Knollys", "canonical_name": "Knollys, A. C.", "given_names": "A. C.", "surname": "Knollys", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "H. G. Fowlis", "canonical_name": "Fowlis, H. G.", "given_names": "H. G.", "surname": "Fowlis", "position": "Chief Clerk", "department": "Secretariat - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "First Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "Second Clerk", "department": "Secretariat - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "C. Gwyn", "canonical_name": "Gwyn, C.", "given_names": "C.", "surname": "Gwyn", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 100, "honors": ["Hon."]},
    {"name": "J. Iles Lauder", "canonical_name": "Lauder, J. Iles", "given_names": "J. Iles", "surname": "Lauder", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "C. A. Hughes", "canonical_name": "Hughes, C. A.", "given_names": "C. A.", "surname": "Hughes", "position": "Correspondence Clerk", "department": "Receiver-General's Department - Gambia", "salary_min": 25, "salary_max": 35},
    {"name": "C. C. Johnson", "canonical_name": "Johnson, C. C.", "given_names": "C. C.", "surname": "Johnson", "position": "Chief Clerk and Cashier", "department": "Treasury Branch - Gambia", "salary_min": 175, "salary_max": 200},
    {"name": "P. Sowe", "canonical_name": "Sowe, P.", "given_names": "P.", "surname": "Sowe", "position": "First Clerk", "department": "Treasury Branch - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. J. Fowlis", "canonical_name": "Fowlis, J. J.", "given_names": "J. J.", "surname": "Fowlis", "position": "Second Clerk", "department": "Treasury Branch - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "E. L. Aubert", "canonical_name": "Aubert, E. L.", "given_names": "E. L.", "surname": "Aubert", "position": "Third Clerk", "department": "Treasury Branch - Gambia", "salary_min": 36, "salary_max": 36},
    {"name": "F. D. Roach", "canonical_name": "Roach, F. D.", "given_names": "F. D.", "surname": "Roach", "position": "Fourth Clerk", "department": "Treasury Branch - Gambia"},
    {"name": "J. N. Savage", "canonical_name": "Savage, J. N.", "given_names": "J. N.", "surname": "Savage", "position": "Apprentice", "department": "Treasury Branch - Gambia", "salary_min": 12, "salary_max": 12}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
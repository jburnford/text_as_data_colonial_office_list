"""
Gambia Colonial Office List 1925 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1925

OFFICIALS = [
    {"name": "C. H. Armitage", "canonical_name": "Armitage, C. H.", "given_names": "C. H.", "surname": "Armitage", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 750, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Captain"},
    {"name": "P. Jeffa", "canonical_name": "Jeffa, P.", "given_names": "P.", "surname": "Jeffa", "position": "Aide-de-Camp and Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 500, "salary_max": 500, "military_rank": "Captain", "honors": ["M.C."]},
    {"name": "M. L. Valantine", "canonical_name": "Valantine, M. L.", "given_names": "M. L.", "surname": "Valantine", "position": "2nd Grade Confidential Clerk", "department": "Civil Establishment - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "F. A. R. Gibson", "canonical_name": "Gibson, F. A. R.", "given_names": "F. A. R.", "surname": "Gibson", "position": "Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "F. P. King", "canonical_name": "King, F. P.", "given_names": "F. P.", "surname": "King", "position": "4th Grade Clerk", "department": "Civil Establishment - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "C. R. M. Workman", "canonical_name": "Workman, C. R. M.", "given_names": "C. R. M.", "surname": "Workman", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "B. A. Finn", "canonical_name": "Finn, B. A.", "given_names": "B. A.", "surname": "Finn", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "B. P. E. Bulstrode", "canonical_name": "Bulstrode, B. P. E.", "given_names": "B. P. E.", "surname": "Bulstrode", "position": "2nd Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "W. T. Hamlyn", "canonical_name": "Hamlyn, W. T.", "given_names": "W. T.", "surname": "Hamlyn", "position": "Cadet", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "African Assistant", "department": "Secretariat - Gambia", "salary_min": 300, "salary_max": 450},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "2nd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "F. D. Roach", "canonical_name": "Roach, F. D.", "given_names": "F. D.", "surname": "Roach", "position": "3rd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. R. Chow", "canonical_name": "Chow, J. R.", "given_names": "J. R.", "surname": "Chow", "position": "3rd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "H. T. Carrol", "canonical_name": "Carrol, H. T.", "given_names": "H. T.", "surname": "Carrol", "position": "3rd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "W. C. Cates", "canonical_name": "Cates, W. C.", "given_names": "W. C.", "surname": "Cates", "position": "4th Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 50, "salary_max": 82}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1923

OFFICIALS = [
    {"name": "C. H. Armitage", "canonical_name": "Armitage, C. H.", "given_names": "C. H.", "surname": "Armitage", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 750, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Captain"},
    {"name": "P. Jeffs", "canonical_name": "Jeffs, P.", "given_names": "P.", "surname": "Jeffs", "position": "Aide-de-Camp and Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 500, "salary_max": 500, "military_rank": "Captain"},
    {"name": "M. L. Valantine", "canonical_name": "Valantine, M. L.", "given_names": "M. L.", "surname": "Valantine", "position": "Confidential Clerk", "department": "Civil Establishment - Gambia", "salary_min": 180, "salary_max": 230},
    {"name": "F. A. R. Gibson", "canonical_name": "Gibson, F. A. R.", "given_names": "F. A. R.", "surname": "Gibson", "position": "Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "C. R. M. Workman", "canonical_name": "Workman, C. R. M.", "given_names": "C. R. M.", "surname": "Workman", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "B. A. Finn", "canonical_name": "Finn, B. A.", "given_names": "B. A.", "surname": "Finn", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 660, "salary_max": 800},
    {"name": "B. P. E. Bulstrode", "canonical_name": "Bulstrode, B. P. E.", "given_names": "B. P. E.", "surname": "Bulstrode", "position": "2nd Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 510, "salary_max": 720},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "Chief Clerk", "department": "Secretariat - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "2nd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "F. D. D. Roach", "canonical_name": "Roach, F. D. D.", "given_names": "F. D. D.", "surname": "Roach", "position": "2nd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. R. Chow", "canonical_name": "Chow, J. R.", "given_names": "J. R.", "surname": "Chow", "position": "3rd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "S. O. Briggs", "canonical_name": "Briggs, S. O.", "given_names": "S. O.", "surname": "Briggs", "position": "3rd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "H. T. Carrol", "canonical_name": "Carrol, H. T.", "given_names": "H. T.", "surname": "Carrol", "position": "3rd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "S. B. Haffner", "canonical_name": "Haffner, S. B.", "given_names": "S. B.", "surname": "Haffner", "position": "Chief Printer", "department": "Printing Branch - Gambia", "salary_min": 150, "salary_max": 210},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "Chief Compositor", "department": "Printing Branch - Gambia", "salary_min": 110, "salary_max": 142},
    {"name": "M. C. Johnson", "canonical_name": "Johnson, M. C.", "given_names": "M. C.", "surname": "Johnson", "position": "2nd Class Composer", "department": "Printing Branch - Gambia", "salary_min": 84, "salary_max": 108},
    {"name": "O. D. Cummings", "canonical_name": "Cummings, O. D.", "given_names": "O. D.", "surname": "Cummings", "position": "2nd Class Composer", "department": "Printing Branch - Gambia", "salary_min": 84, "salary_max": 108},
    {"name": "V. A. John", "canonical_name": "John, V. A.", "given_names": "V. A.", "surname": "John", "position": "2nd Class Composer", "department": "Printing Branch - Gambia", "salary_min": 60, "salary_max": 84},
    {"name": "R. J. Williams", "canonical_name": "Williams, R. J.", "given_names": "R. J.", "surname": "Williams", "position": "2nd Class Composer", "department": "Printing Branch - Gambia", "salary_min": 60, "salary_max": 84},
    {"name": "E. S. See", "canonical_name": "See, E. S.", "given_names": "E. S.", "surname": "See", "position": "2nd Class Composer", "department": "Printing Branch - Gambia", "salary_min": 60, "salary_max": 84},
    {"name": "V. E. Davies", "canonical_name": "Davies, V. E.", "given_names": "V. E.", "surname": "Davies", "position": "2nd Class Composer", "department": "Printing Branch - Gambia", "salary_min": 60, "salary_max": 84},
    {"name": "S. O. Allen", "canonical_name": "Allen, S. O.", "given_names": "S. O.", "surname": "Allen", "position": "2nd Class Composer", "department": "Printing Branch - Gambia", "salary_min": 60, "salary_max": 84}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
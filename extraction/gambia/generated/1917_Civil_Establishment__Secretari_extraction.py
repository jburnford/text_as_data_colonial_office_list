"""
Gambia Colonial Office List 1917 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1917

OFFICIALS = [
    {"name": "Sir E. J. Cameron", "canonical_name": "Cameron, E. J.", "given_names": "E. J.", "surname": "Cameron", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "honors": ["K.C.M.G."]},
    {"name": "C. S. Masser", "canonical_name": "Masser, C. S.", "given_names": "C. S.", "surname": "Masser", "position": "Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250, "per_diem": "2s. 3d. forage allowance per diem"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "1st Grade Clerk and Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "M. L. Valantine", "canonical_name": "Valantine, M. L.", "given_names": "M. L.", "surname": "Valantine", "position": "4th Grade Clerk", "department": "Civil Establishment - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "E. Jallow", "canonical_name": "Jallow, E.", "given_names": "E.", "surname": "Jallow", "position": "6th Grade Clerk", "department": "Civil Establishment - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "W. T. Campbell", "canonical_name": "Campbell, W. T.", "given_names": "W. T.", "surname": "Campbell", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "A. C. Knollys", "canonical_name": "Knollys, A. C.", "given_names": "A. C.", "surname": "Knollys", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 50},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "Chief Clerk", "department": "Secretariat - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "2nd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "F. D. D. Roach", "canonical_name": "Roach, F. D. D.", "given_names": "F. D. D.", "surname": "Roach", "position": "4th Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "5th Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "A. H. Jones", "canonical_name": "Jones, A. H.", "given_names": "A. H.", "surname": "Jones", "position": "5th Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "N. E. Williams", "canonical_name": "Williams, N. E.", "given_names": "N. E.", "surname": "Williams", "position": "Chief Printer", "department": "Printing Branch - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "Chief Compositor", "department": "Printing Branch - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "M. C. Johnson", "canonical_name": "Johnson, M. C.", "given_names": "M. C.", "surname": "Johnson", "position": "1st Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 60, "salary_max": 75},
    {"name": "O. D. Cummings", "canonical_name": "Cummings, O. D.", "given_names": "O. D.", "surname": "Cummings", "position": "2nd Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "V. A. John", "canonical_name": "John, V. A.", "given_names": "V. A.", "surname": "John", "position": "2nd Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "E. See", "canonical_name": "See, E.", "given_names": "E.", "surname": "See", "position": "3rd Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. V. Harding", "canonical_name": "Harding, S. V.", "given_names": "S. V.", "surname": "Harding", "position": "3rd Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 30, "salary_max": 40}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
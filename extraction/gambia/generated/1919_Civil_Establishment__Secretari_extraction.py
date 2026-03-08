"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "Sir Edward J. Cameron", "canonical_name": "Cameron, Edward J.", "given_names": "Edward J.", "surname": "Cameron", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "honors": ["K.C.M.G."]},
    {"name": "C. S. Masser", "canonical_name": "Masser, C. S.", "given_names": "C. S.", "surname": "Masser", "position": "Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250, "per_diem": "2s. 3d. per diem forage allowance"},
    {"name": "M. L. Valantine", "canonical_name": "Valantine, M. L.", "given_names": "M. L.", "surname": "Valantine", "position": "4th Grade Clerk", "department": "Civil Establishment - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "H. Henninger Heaton", "canonical_name": "Heaton, H. Henninger", "given_names": "H. Henninger", "surname": "Heaton", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "A. C. Knollys", "canonical_name": "Knollys, A. C.", "given_names": "A. C.", "surname": "Knollys", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 50},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "Chief Clerk", "department": "Secretariat - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "2nd Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "F. D. D. Roach", "canonical_name": "Roach, F. D. D.", "given_names": "F. D. D.", "surname": "Roach", "position": "4th Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "J. L. Danner", "canonical_name": "Danner, J. L.", "given_names": "J. L.", "surname": "Danner", "position": "5th Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "J. M. Davies", "canonical_name": "Davies, J. M.", "given_names": "J. M.", "surname": "Davies", "position": "5th Grade Clerk", "department": "Secretariat - Gambia", "salary_min": 40, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
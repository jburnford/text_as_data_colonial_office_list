"""
Gambia Colonial Office List 1921 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1921

OFFICIALS = [
    {"name": "C. Gwyn", "canonical_name": "Gwyn, C.", "given_names": "C.", "surname": "Gwyn", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "E. G. C. Gabbidon", "canonical_name": "Gabbidon, E. G. C.", "given_names": "E. G. C.", "surname": "Gabbidon", "position": "Correspondence Clerk, 3rd Grade", "department": "Receiver-General's Department - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "E. V. Adams", "canonical_name": "Adams, E. V.", "given_names": "E. V.", "surname": "Adams", "position": "Assistant Receivers-General", "department": "Treasury - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Accountant", "department": "Treasury - Gambia", "salary_min": 450, "salary_max": 450},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Clerk, 1st Grade", "department": "Treasury - Gambia", "salary_min": 180, "salary_max": 230},
    {"name": "S. P. Gibbs", "canonical_name": "Gibbs, S. P.", "given_names": "S. P.", "surname": "Gibbs", "position": "Cashier, 1st Grade", "department": "Treasury - Gambia", "salary_min": 180, "salary_max": 230},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "2nd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "2nd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "B. D. Wright", "canonical_name": "Wright, B. D.", "given_names": "B. D.", "surname": "Wright", "position": "2nd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "Z. S. A. Williams", "canonical_name": "Williams, Z. S. A.", "given_names": "Z. S. A.", "surname": "Williams", "position": "2nd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "2nd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "G. B. D. Campbell", "canonical_name": "Campbell, G. B. D.", "given_names": "G. B. D.", "surname": "Campbell", "position": "3rd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "3rd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 50, "salary_max": 80},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1923

OFFICIALS = [
    {"name": "C. Gwyn", "canonical_name": "Gwyn, C.", "given_names": "C.", "surname": "Gwyn", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 960, "salary_max": 960, "allowances": "100l., and 96l. personal and duty allowances"},
    {"name": "W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Assistants Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 450, "salary_max": 720, "military_rank": "Captain"},
    {"name": "F. A. Mathias", "canonical_name": "Mathias, F. A.", "given_names": "F. A.", "surname": "Mathias", "position": "Assistants Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "E. G. C. Gabbidon", "canonical_name": "Gabbidon, E. G. C.", "given_names": "E. G. C.", "surname": "Gabbidon", "position": "Correspondence Clerks, 2nd Grade", "department": "Receiver-General's Department - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Correspondence Clerks, 3rd Grade", "department": "Receiver-General's Department - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Accountant", "department": "Treasury Branch - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "S. P. Gibbs", "canonical_name": "Gibbs, S. P.", "given_names": "S. P.", "surname": "Gibbs", "position": "1st Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 180, "salary_max": 230, "location": "Cashier"},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "1st Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 180, "salary_max": 230, "location": "Chief Clerk"},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "2nd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "B. D. Wright", "canonical_name": "Wright, B. D.", "given_names": "B. D.", "surname": "Wright", "position": "2nd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "2nd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. D. Allen", "canonical_name": "Allen, J. D.", "given_names": "J. D.", "surname": "Allen", "position": "2nd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "3rd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "D. T. D. Taylor", "canonical_name": "Taylor, D. T. D.", "given_names": "D. T. D.", "surname": "Taylor", "position": "3rd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "H. B. Carroll", "canonical_name": "Carroll, H. B.", "given_names": "H. B.", "surname": "Carroll", "position": "3rd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "E. W. B. Carroll", "canonical_name": "Carroll, E. W. B.", "given_names": "E. W. B.", "surname": "Carroll", "position": "3rd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 50, "salary_max": 80}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
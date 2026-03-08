"""
Gambia Colonial Office List 1924 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1924

OFFICIALS = [
    {"name": "C. Gwyn", "canonical_name": "Gwyn, C.", "given_names": "C.", "surname": "Gwyn", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 960, "salary_max": 960, "allowances": "100l., and 96l. personal and duty allowances"},
    {"name": "W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Assistants Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720, "military_rank": "Captain"},
    {"name": "F. A. Mathias", "canonical_name": "Mathias, F. A.", "given_names": "F. A.", "surname": "Mathias", "position": "Assistants Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "E. G. C. Gabbidon", "canonical_name": "Gabbidon, E. G. C.", "given_names": "E. G. C.", "surname": "Gabbidon", "position": "Correspondence Clerks, 3rd Grade", "department": "Receiver-General's Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. L. Fenlon", "canonical_name": "Fenlon, J. L.", "given_names": "J. L.", "surname": "Fenlon", "position": "Accountant", "department": "Treasury - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Chief Clerk", "department": "Treasury - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "S. P. Gibbs", "canonical_name": "Gibbs, S. P.", "given_names": "S. P.", "surname": "Gibbs", "position": "2nd Grade Clerk", "department": "Treasury - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "3rd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. D. Allen", "canonical_name": "Allen, J. D.", "given_names": "J. D.", "surname": "Allen", "position": "3rd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "3rd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "D. T. D. Taylor", "canonical_name": "Taylor, D. T. D.", "given_names": "D. T. D.", "surname": "Taylor", "position": "3rd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "E. W. B. Carroll", "canonical_name": "Carroll, E. W. B.", "given_names": "E. W. B.", "surname": "Carroll", "position": "3rd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "4th Grade Clerks", "department": "Treasury - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "J. F. Davies", "canonical_name": "Davies, J. F.", "given_names": "J. F.", "surname": "Davies", "position": "4th Grade Clerks", "department": "Treasury - Gambia", "salary_min": 50, "salary_max": 82}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1929 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1929

OFFICIALS = [
    {"name": "F. D. MacPhail", "canonical_name": "MacPhail, F. D.", "given_names": "F. D.", "surname": "MacPhail", "position": "Accountant", "department": "Treasury - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Chief Clerk", "department": "Treasury - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "E. G. C. Gabbidon", "canonical_name": "Gabbidon, E. G. C.", "given_names": "E. G. C.", "surname": "Gabbidon", "position": "Cashier", "department": "Treasury - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "D. T. Taylor", "canonical_name": "Taylor, D. T.", "given_names": "D. T.", "surname": "Taylor", "position": "2nd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "E. W. Carrol", "canonical_name": "Carrol, E. W.", "given_names": "E. W.", "surname": "Carrol", "position": "2nd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "O. E. Kernahan", "canonical_name": "Kernahan, O. E.", "given_names": "O. E.", "surname": "Kernahan", "position": "Supervisor of Customs", "department": "Customs - The Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "Chief Clerk, 1st Grade", "department": "Customs - The Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "S. W. Davies", "canonical_name": "Davies, S. W.", "given_names": "S. W.", "surname": "Davies", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "Landing Waiters (2nd Grade)", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "I. B. Y. Jobe", "canonical_name": "Jobe, I. B. Y.", "given_names": "I. B. Y.", "surname": "Jobe", "position": "Landing Waiters (2nd Grade)", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 230}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1930 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1930

OFFICIALS = [
    {"name": "F. D. MacPhail", "canonical_name": "MacPhail, F. D.", "given_names": "F. D.", "surname": "MacPhail", "position": "Accountant", "department": "Treasury - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Chief Clerk", "department": "Treasury - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "E. G. C. Gabbidon", "canonical_name": "Gabbidon, E. G. C.", "given_names": "E. G. C.", "surname": "Gabbidon", "position": "Cashier, 2nd Grade", "department": "Treasury - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "D. T. Taylor", "canonical_name": "Taylor, D. T.", "given_names": "D. T.", "surname": "Taylor", "position": "2nd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "E. W. Carrol", "canonical_name": "Carrol, E. W.", "given_names": "E. W.", "surname": "Carrol", "position": "2nd Grade Clerks", "department": "Treasury - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "O. E. Kernahan", "canonical_name": "Kernahan, O. E.", "given_names": "O. E.", "surname": "Kernahan", "position": "Supervisor of Customs", "department": "Customs - The Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "Chief Clerk, 1st Grade", "department": "Customs - The Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "S. W. Davies", "canonical_name": "Davies, S. W.", "given_names": "S. W.", "surname": "Davies", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "Landing Waiters (2nd Grade)", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "I. B. Y. Jobe", "canonical_name": "Jobe, I. B. Y.", "given_names": "I. B. Y.", "surname": "Jobe", "position": "Landing Waiters (2nd Grade)", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 600, "salary_max": 920},
    {"name": "A. G. B. Manson", "canonical_name": "Manson, A. G. B.", "given_names": "A. G. B.", "surname": "Manson", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Clerk of Courts, 1st Grade", "department": "Legal Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "W. B. Coker", "canonical_name": "Coker, W. B.", "given_names": "W. B.", "surname": "Coker", "position": "Interpreter of Courts, 3rd Grade", "department": "Legal Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Sheriff's Bailiff and Beadle of the Court of Requests, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "2nd Grade Clerk", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Sheriff", "department": "Legal Department - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
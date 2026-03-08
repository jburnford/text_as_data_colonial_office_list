"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "A. O. Grady Lefroy", "canonical_name": "Lefroy, A. O. Grady", "given_names": "A. O. Grady", "surname": "Lefroy", "position": "Colonial Treasurer", "department": "Treasury Department - Gambia", "salary_min": 550, "salary_max": 550, "honors": ["C.M.G."]},
    {"name": "L. S. Eliot", "canonical_name": "Eliot, L. S.", "given_names": "L. S.", "surname": "Eliot", "position": "Chief Clerk and Accountant", "department": "Treasury Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "R. C. Hare", "canonical_name": "Hare, R. C.", "given_names": "R. C.", "surname": "Hare", "position": "Book-keeper", "department": "Treasury Department - Gambia", "salary_min": 275, "salary_max": 275},
    {"name": "F. L. Hussey", "canonical_name": "Hussey, F. L.", "given_names": "F. L.", "surname": "Hussey", "position": "2nd Clerk", "department": "Treasury Department - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "George Withers", "canonical_name": "Withers, George", "given_names": "George", "surname": "Withers", "position": "3rd Clerk", "department": "Treasury Department - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "G. F. Glyde", "canonical_name": "Glyde, G. F.", "given_names": "G. F.", "surname": "Glyde", "position": "Clerk and Accountant, Geraldton", "department": "Treasury Department - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "Robert Sholl", "canonical_name": "Sholl, Robert", "given_names": "Robert", "surname": "Sholl", "position": "Deputy Treasurers", "department": "Treasury Department - Gambia"},
    {"name": "George Eliot", "canonical_name": "Eliot, George", "given_names": "George", "surname": "Eliot", "position": "Deputy Treasurers", "department": "Treasury Department - Gambia"},
    {"name": "R. C. Loftie", "canonical_name": "Loftie, R. C.", "given_names": "R. C.", "surname": "Loftie", "position": "Deputy Treasurers", "department": "Treasury Department - Gambia"},
    {"name": "E. L. Courthope", "canonical_name": "Courthope, E. L.", "given_names": "E. L.", "surname": "Courthope", "position": "Auditor-General", "department": "Audit Department - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "F. Spencer", "canonical_name": "Spencer, F.", "given_names": "F.", "surname": "Spencer", "position": "Chief Clerk and Examiner", "department": "Audit Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "C. Pether", "canonical_name": "Pether, C.", "given_names": "C.", "surname": "Pether", "position": "2nd Clerk", "department": "Audit Department - Gambia", "salary_min": 160, "salary_max": 160},
    {"name": "T. Angove", "canonical_name": "Angove, T.", "given_names": "T.", "surname": "Angove", "position": "3rd Clerk", "department": "Audit Department - Gambia", "salary_min": 90, "salary_max": 90},
    {"name": "J. Mitchell", "canonical_name": "Mitchell, J.", "given_names": "J.", "surname": "Mitchell", "position": "Clerk and Examiner", "department": "Audit Department - Gambia", "salary_min": 150, "salary_max": 150}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
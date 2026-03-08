"""
Gambia Colonial Office List 1917 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1917

OFFICIALS = [
    {"name": "A. E. Horn", "canonical_name": "Horn, A. E.", "given_names": "A. E.", "surname": "Horn", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 240},
    {"name": "R. W. Orpen", "canonical_name": "Orpen, R. W.", "given_names": "R. W.", "surname": "Orpen", "position": "Medical Officer (Health Officer)", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "F. C. V. Thompson", "canonical_name": "Thompson, F. C. V.", "given_names": "F. C. V.", "surname": "Thompson", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "R. H. Miller", "canonical_name": "Miller, R. H.", "given_names": "R. H.", "surname": "Miller", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "T. Ryan", "canonical_name": "Ryan, T.", "given_names": "T.", "surname": "Ryan", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "J. C. Watt", "canonical_name": "Watt, J. C.", "given_names": "J. C.", "surname": "Watt", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "F. B. Bate", "canonical_name": "Bate, F. B.", "given_names": "F. B.", "surname": "Bate", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "Miss K. M. Gordon", "canonical_name": "Gordon, K. M.", "given_names": "K. M.", "surname": "Gordon", "position": "Nurse-in-Charge", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "M. M. Hall", "canonical_name": "Hall, M. M.", "given_names": "M. M.", "surname": "Hall", "position": "Nurses", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "M. Thompson", "canonical_name": "Thompson, M.", "given_names": "M.", "surname": "Thompson", "position": "Nurses", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "H. R. Wakefield", "canonical_name": "Wakefield, H. R.", "given_names": "H. R.", "surname": "Wakefield", "position": "Nurses", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "Chief Dispenser and Storekeeper", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 130},
    {"name": "J. S. Kennedy", "canonical_name": "Kennedy, J. S.", "given_names": "J. S.", "surname": "Kennedy", "position": "Assistant Dispensers", "department": "Medical - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Assistant Dispensers", "department": "Medical - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "Colin Shaw", "canonical_name": "Shaw, Colin", "given_names": "Colin", "surname": "Shaw", "position": "1st Grade Clerk and Steward", "department": "Medical - Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "E. W. Johns", "canonical_name": "Johns, E. W.", "given_names": "E. W.", "surname": "Johns", "position": "Assistant Storekeeper and Dispenser", "department": "Medical - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "R. W. Orpen", "canonical_name": "Orpen, R. W.", "given_names": "R. W.", "surname": "Orpen", "position": "Medical Officer of Health", "department": "Medical - Gambia"},
    {"name": "G. B. Morey", "canonical_name": "Morey, G. B.", "given_names": "G. B.", "surname": "Morey", "position": "Sanitary Inspector", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "C. Wolfendale", "canonical_name": "Wolfendale, C.", "given_names": "C.", "surname": "Wolfendale", "position": "Assistant Sanitary Inspector", "department": "Medical - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "D. D. Peters", "canonical_name": "Peters, D. D.", "given_names": "D. D.", "surname": "Peters", "position": "Clerk of the Market", "department": "Medical - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "J. A. Johnson", "canonical_name": "Johnson, J. A.", "given_names": "J. A.", "surname": "Johnson", "position": "Inspector of Nuisances", "department": "Medical - Gambia", "salary_min": 60, "salary_max": 70},
    {"name": "M. King", "canonical_name": "King, M.", "given_names": "M.", "surname": "King", "position": "Caretaker", "department": "Medical - Gambia", "salary_min": 48, "salary_max": 48}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
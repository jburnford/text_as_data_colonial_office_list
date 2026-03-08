"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "E. A. Horn", "canonical_name": "Horn, E. A.", "given_names": "E. A.", "surname": "Horn", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 240},
    {"name": "T. F. G. Mayer", "canonical_name": "Mayer, T. F. G.", "given_names": "T. F. G.", "surname": "Mayer", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600},
    {"name": "R. W. Orpen", "canonical_name": "Orpen, R. W.", "given_names": "R. W.", "surname": "Orpen", "position": "Medical Officer (Health Officer)", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "F. C. V. Thompson", "canonical_name": "Thompson, F. C. V.", "given_names": "F. C. V.", "surname": "Thompson", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "R. H. Miller", "canonical_name": "Miller, R. H.", "given_names": "R. H.", "surname": "Miller", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "T. Ryan", "canonical_name": "Ryan, T.", "given_names": "T.", "surname": "Ryan", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "Miss K. M. Gordon", "canonical_name": "Gordon, K. M.", "given_names": "K. M.", "surname": "Gordon", "position": "Nurse-in-Charge", "department": "Medical - Gambia"},
    {"name": "L. E. H. Maulton", "canonical_name": "Maulton, L. E. H.", "given_names": "L. E. H.", "surname": "Maulton", "position": "Nurses", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "R. Roddan", "canonical_name": "Roddan, R.", "given_names": "R.", "surname": "Roddan", "position": "Nurses", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "P. R. di Menno", "canonical_name": "di Menno, P. R.", "given_names": "P. R.", "surname": "di Menno", "position": "Nurses", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "Chief Dispenser and Storekeeper", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 130},
    {"name": "J. S. Kennedy", "canonical_name": "Kennedy, J. S.", "given_names": "J. S.", "surname": "Kennedy", "position": "Assistant Dispensers", "department": "Medical - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "Colin Shaw", "canonical_name": "Shaw, Colin", "given_names": "Colin", "surname": "Shaw", "position": "2nd Grade Clerk and Steward", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "E. W. Johns", "canonical_name": "Johns, E. W.", "given_names": "E. W.", "surname": "Johns", "position": "Assistant Storekeeper and Dispenser", "department": "Medical - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "R. W. Orpen", "canonical_name": "Orpen, R. W.", "given_names": "R. W.", "surname": "Orpen", "position": "Medical Officer of Health", "department": "Medical - Gambia"},
    {"name": "T. J. Gibbs", "canonical_name": "Gibbs, T. J.", "given_names": "T. J.", "surname": "Gibbs", "position": "Town Warden", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300, "duty_allowance": 50},
    {"name": "G. B. Morey", "canonical_name": "Morey, G. B.", "given_names": "G. B.", "surname": "Morey", "position": "Assistant Town Warden", "department": "Medical - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "D. D. Peters", "canonical_name": "Peters, D. D.", "given_names": "D. D.", "surname": "Peters", "position": "Clerk of the Market", "department": "Medical - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "J. A. Johnson", "canonical_name": "Johnson, J. A.", "given_names": "J. A.", "surname": "Johnson", "position": "Inspector of Nuisances", "department": "Medical - Gambia", "salary_min": 60, "salary_max": 70}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
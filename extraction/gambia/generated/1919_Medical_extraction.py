"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "E. C. Adams", "canonical_name": "Adams, E. C.", "given_names": "E. C.", "surname": "Adams", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 600, "salary_max": 750, "duty_allowance": 120, "allowances": "120l. each duty and staff allowances"},
    {"name": "F. C. V. Thompson", "canonical_name": "Thompson, F. C. V.", "given_names": "F. C. V.", "surname": "Thompson", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 100, "allowances": "100l. each duty and staff allowances"},
    {"name": "E. F. Ward", "canonical_name": "Ward, E. F.", "given_names": "E. F.", "surname": "Ward", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "R. H. Miller", "canonical_name": "Miller, R. H.", "given_names": "R. H.", "surname": "Miller", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "J. C. Watt", "canonical_name": "Watt, J. C.", "given_names": "J. C.", "surname": "Watt", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "E. B. Bate", "canonical_name": "Bate, E. B.", "given_names": "E. B.", "surname": "Bate", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "M. M. Hall", "canonical_name": "Hall, M. M.", "given_names": "M. M.", "surname": "Hall", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "M. Thompson", "canonical_name": "Thompson, M.", "given_names": "M.", "surname": "Thompson", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "M. C. Parsons", "canonical_name": "Parsons, M. C.", "given_names": "M. C.", "surname": "Parsons", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "Chief Dispenser and Storekeeper", "department": "Medical - Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "J. S. Kennedy", "canonical_name": "Kennedy, J. S.", "given_names": "J. S.", "surname": "Kennedy", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "E. W. Johns", "canonical_name": "Johns, E. W.", "given_names": "E. W.", "surname": "Johns", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "S. B. Palmer", "canonical_name": "Palmer, S. B.", "given_names": "S. B.", "surname": "Palmer", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "J. F. Jagne", "canonical_name": "Jagne, J. F.", "given_names": "J. F.", "surname": "Jagne", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 40, "salary_max": 60},
    {"name": "Colin Shaw", "canonical_name": "Shaw, Colin", "given_names": "Colin", "surname": "Shaw", "position": "1st Grade Clerk and Steward", "department": "Medical - Gambia", "salary_min": 130, "salary_max": 160}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
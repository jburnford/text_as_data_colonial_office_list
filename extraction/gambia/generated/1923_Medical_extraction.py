"""
Gambia Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1923

OFFICIALS = [
    {"name": "T. F. G. Mayer", "canonical_name": "Mayer, T. F. G.", "given_names": "T. F. G.", "surname": "Mayer", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1000, "salary_max": 1150, "allowances": "250l. staff and seniority allowances"},
    {"name": "R. H. Miller", "canonical_name": "Miller, R. H.", "given_names": "R. H.", "surname": "Miller", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "G. E. Craig", "canonical_name": "Craig, G. E.", "given_names": "G. E.", "surname": "Craig", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "M. Thompson", "canonical_name": "Thompson, M.", "given_names": "M.", "surname": "Thompson", "position": "Senior Nursing Sister", "department": "Medical - Gambia", "salary_min": 380, "salary_max": 440, "allowances": "40l. charge allowance"},
    {"name": "C. G. Leggat", "canonical_name": "Leggat, C. G.", "given_names": "C. G.", "surname": "Leggat", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "P. Stagg", "canonical_name": "Stagg, P.", "given_names": "P.", "surname": "Stagg", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "Chief Dispenser and Storekeeper", "department": "Medical - Gambia", "salary_min": 150, "salary_max": 210},
    {"name": "E. W. Johns", "canonical_name": "Johns, E. W.", "given_names": "E. W.", "surname": "Johns", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 110, "salary_max": 142},
    {"name": "W. M. Rollings", "canonical_name": "Rollings, W. M.", "given_names": "W. M.", "surname": "Rollings", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 110, "salary_max": 142},
    {"name": "J. F. Jagne", "canonical_name": "Jagne, J. F.", "given_names": "J. F.", "surname": "Jagne", "position": "2nd Class Dispenser", "department": "Medical - Gambia", "salary_min": 84, "salary_max": 108},
    {"name": "J. T. Williams", "canonical_name": "Williams, J. T.", "given_names": "J. T.", "surname": "Williams", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 60, "salary_max": 84},
    {"name": "W. S. Faulkner", "canonical_name": "Faulkner, W. S.", "given_names": "W. S.", "surname": "Faulkner", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 60, "salary_max": 84},
    {"name": "C. Shaw", "canonical_name": "Shaw, C.", "given_names": "C.", "surname": "Shaw", "position": "2nd Grade Clerk", "department": "Medical - Gambia", "salary_min": 90, "salary_max": 170},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
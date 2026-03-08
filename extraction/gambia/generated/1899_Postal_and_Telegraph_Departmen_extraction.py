"""
Gambia Colonial Office List 1899 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1899

OFFICIALS = [
    {"name": "Miss Creswell", "canonical_name": "Creswell, Miss", "surname": "Creswell", "position": "Postmistress and Supt. of Telegraph", "department": "Postal and Telegraph Department - Gambia", "salary_min": 548, "salary_max": 548, "allowances": "100l. lodging allowance"},
    {"name": "A. Bosano", "canonical_name": "Bosano, A.", "given_names": "A.", "surname": "Bosano", "position": "Chief Clerk and Accountant", "department": "Postal and Telegraph Department - Gambia", "salary_min": 166, "salary_max": 166},
    {"name": "J. S. Coll", "canonical_name": "Coll, J. S.", "given_names": "J. S.", "surname": "Coll", "position": "3rd-Class Clerks", "department": "Postal and Telegraph Department - Gambia", "salary_min": 125, "salary_max": 125},
    {"name": "W. B. Edwards", "canonical_name": "Edwards, W. B.", "given_names": "W. B.", "surname": "Edwards", "position": "3rd-Class Clerks", "department": "Postal and Telegraph Department - Gambia", "salary_min": 103, "salary_max": 103},
    {"name": "C. J. Edwards", "canonical_name": "Edwards, C. J.", "given_names": "C. J.", "surname": "Edwards", "position": "3rd-Class Clerks", "department": "Postal and Telegraph Department - Gambia", "salary_min": 87, "salary_max": 87},
    {"name": "J. Chipulina", "canonical_name": "Chipulina, J.", "given_names": "J.", "surname": "Chipulina", "position": "3rd-Class Clerks", "department": "Postal and Telegraph Department - Gambia", "salary_min": 83, "salary_max": 83},
    {"name": "J. Shakery", "canonical_name": "Shakery, J.", "given_names": "J.", "surname": "Shakery", "position": "3rd-Class Clerks (Telegraph and Savings Bank)", "department": "Postal and Telegraph Department - Gambia", "salary_min": 104, "salary_max": 104},
    {"name": "A. Chipulina", "canonical_name": "Chipulina, A.", "given_names": "A.", "surname": "Chipulina", "position": "3rd-Class Clerks (Telegraph and Savings Bank)", "department": "Postal and Telegraph Department - Gambia", "salary_min": 57, "salary_max": 57},
    {"name": "T. Chipulina", "canonical_name": "Chipulina, T.", "given_names": "T.", "surname": "Chipulina", "position": "Suppl. Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 66, "salary_max": 66},
    {"name": "W. Turner", "canonical_name": "Turner, W.", "given_names": "W.", "surname": "Turner", "position": "Surgeon, Colonial Hospital, Gaol, and Lunatic Asylum", "department": "Medical Department - Gambia", "salary_min": 500, "salary_max": 500, "qualifications": ["M.D."]},
    {"name": "J. E. Ker", "canonical_name": "Ker, J. E.", "given_names": "J. E.", "surname": "Ker", "position": "Asst. Surgeon, Colonial Hospital, Police, and Port Surgeon", "department": "Medical Department - Gambia", "salary_min": 229, "salary_max": 229, "qualifications": ["M.R.C.S."]},
    {"name": "A. J. Triay", "canonical_name": "Triay, A. J.", "given_names": "A. J.", "surname": "Triay", "position": "Surgeon, Smallpox Hospital and District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 158, "salary_max": 158, "qualifications": ["M.B."]},
    {"name": "L. L. Verano", "canonical_name": "Verano, L. L.", "given_names": "L. L.", "surname": "Verano", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 58, "salary_max": 58, "qualifications": ["M.R.C.S."]},
    {"name": "H. Recano", "canonical_name": "Recano, H.", "given_names": "H.", "surname": "Recano", "position": "Secretary, Colonial Hospital", "department": "Medical Department - Gambia", "salary_min": 166, "salary_max": 166},
    {"name": "M. Montegriffo", "canonical_name": "Montegriffo, M.", "given_names": "M.", "surname": "Montegriffo", "position": "Clerk", "department": "Medical Department - Gambia", "salary_min": 125, "salary_max": 125}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1949 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1949

OFFICIALS = [
    {"name": "C. W. F. Mackay", "canonical_name": "Mackay, C. W. F.", "given_names": "C. W. F.", "surname": "Mackay", "position": "Director of Medical Services", "department": "MEDICAL AND HEALTH - Gambia", "salary_min": 1350, "salary_max": 1350, "allowances": "expatriation allowance, £400", "honors": ["O.B.E."]},
    {"name": "T. P. Eddy", "canonical_name": "Eddy, T. P.", "given_names": "T. P.", "surname": "Eddy", "position": "Medical Officer of Health", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "A"},
    {"name": "W. E. Hadden", "canonical_name": "Hadden, W. E.", "given_names": "W. E.", "surname": "Hadden", "position": "Medical Officer", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "A"},
    {"name": "S. G. Gordon", "canonical_name": "Gordon, S. G.", "given_names": "S. G.", "surname": "Gordon", "position": "Medical Officer", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "A"},
    {"name": "D. W. Horn", "canonical_name": "Horn, D. W.", "given_names": "D. W.", "surname": "Horn", "position": "Medical Officer", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "A"},
    {"name": "G. E. J. Porter", "canonical_name": "Porter, G. E. J.", "given_names": "G. E. J.", "surname": "Porter", "position": "Medical Officer", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "A"},
    {"name": "S. H. O. Jones", "canonical_name": "Jones, S. H. O.", "given_names": "S. H. O.", "surname": "Jones", "position": "Medical Officer", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "A"},
    {"name": "E. F. B. Forster", "canonical_name": "Forster, E. F. B.", "given_names": "E. F. B.", "surname": "Forster", "position": "Medical Officer", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "A"},
    {"name": "R. W. Campbell", "canonical_name": "Campbell, R. W.", "given_names": "R. W.", "surname": "Campbell", "position": "Entomologist", "department": "MEDICAL AND HEALTH - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Senior Nursing Sister", "department": "MEDICAL AND HEALTH - Gambia"},
    {"name": "M. M. Wordley", "canonical_name": "Wordley, M. M.", "given_names": "M. M.", "surname": "Wordley", "position": "Nursing Sister", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "N"},
    {"name": "M. M. Shepherd", "canonical_name": "Shepherd, M. M.", "given_names": "M. M.", "surname": "Shepherd", "position": "Nursing Sister", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "N"},
    {"name": "P. M. Hill", "canonical_name": "Hill, P. M.", "given_names": "P. M.", "surname": "Hill", "position": "Nursing Sister", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "N"},
    {"name": "C. N. Michie", "canonical_name": "Michie, C. N.", "given_names": "C. N.", "surname": "Michie", "position": "Nursing Sister", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "N"},
    {"name": "A. M. Rankin", "canonical_name": "Rankin, A. M.", "given_names": "A. M.", "surname": "Rankin", "position": "Nursing Sister", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "N"},
    {"name": "C. W. Cottier", "canonical_name": "Cottier, C. W.", "given_names": "C. W.", "surname": "Cottier", "position": "Senior Sanitary Superintendent", "department": "MEDICAL AND HEALTH - Gambia", "salary_scale": "C"},
    {"name": "N. P. Hadow", "canonical_name": "Hadow, N. P.", "given_names": "N. P.", "surname": "Hadow", "position": "Superintendent of Police and Inspector of Prisons", "department": "POLICE AND PRISONS - Gambia", "salary_scale": "B"},
    {"name": "J. N. Ferguson", "canonical_name": "Ferguson, J. N.", "given_names": "J. N.", "surname": "Ferguson", "position": "Assistant Superintendent of Police", "department": "POLICE AND PRISONS - Gambia", "salary_scale": "B"},
    {"name": "P. A. Williams", "canonical_name": "Williams, P. A.", "given_names": "P. A.", "surname": "Williams", "position": "Assistant Superintendent of Police", "department": "POLICE AND PRISONS - Gambia", "salary_scale": "B"},
    {"name": "E. C. Sowe", "canonical_name": "Sowe, E. C.", "given_names": "E. C.", "surname": "Sowe", "position": "Postmaster General", "department": "POST OFFICE - Gambia", "salary_scale": "B"},
    {"name": "O. B. Johnson", "canonical_name": "Johnson, O. B.", "given_names": "O. B.", "surname": "Johnson", "position": "Assistant Postmaster General", "department": "POST OFFICE - Gambia", "salary_scale": "F5"},
    {"name": "G. Peters", "canonical_name": "Peters, G.", "given_names": "G.", "surname": "Peters", "position": "Assistant Public Relations Officer", "department": "PUBLIC RELATIONS - Gambia", "salary_scale": "B"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
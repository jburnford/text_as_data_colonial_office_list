"""
Gambia Colonial Office List 1950 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1950

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Director of Medical Services", "department": "Medical and Health - Gambia", "salary_min": 1350, "salary_max": 1350, "expatriation_pay": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Medical Officer of Health", "department": "Medical and Health - Gambia", "salary_scale": "A", "allowances": "£100 Staff Pay"},
    {"name": "W. E. Hadden", "canonical_name": "Hadden, W. E.", "given_names": "W. E.", "surname": "Hadden", "position": "Medical Officer", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "G. E. J. Porter", "canonical_name": "Porter, G. E. J.", "given_names": "G. E. J.", "surname": "Porter", "position": "Medical Officer", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "S. H. O. Jones", "canonical_name": "Jones, S. H. O.", "given_names": "S. H. O.", "surname": "Jones", "position": "Medical Officer", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "E. F. B. Forster", "canonical_name": "Forster, E. F. B.", "given_names": "E. F. B.", "surname": "Forster", "position": "Medical Officer", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "R. W. Campbell", "canonical_name": "Campbell, R. W.", "given_names": "R. W.", "surname": "Campbell", "position": "Entomologist", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "J. A. M. Henderson", "canonical_name": "Henderson, J. A. M.", "given_names": "J. A. M.", "surname": "Henderson", "position": "Senior Nursing Sister", "department": "Medical and Health - Gambia"},
    {"name": "M. M. Wordley", "canonical_name": "Wordley, M. M.", "given_names": "M. M.", "surname": "Wordley", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "M. M. Shepherd", "canonical_name": "Shepherd, M. M.", "given_names": "M. M.", "surname": "Shepherd", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "P. M. Hill", "canonical_name": "Hill, P. M.", "given_names": "P. M.", "surname": "Hill", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "C. N. Michie", "canonical_name": "Michie, C. N.", "given_names": "C. N.", "surname": "Michie", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "A. M. Rankin", "canonical_name": "Rankin, A. M.", "given_names": "A. M.", "surname": "Rankin", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "M. W. Crawford", "canonical_name": "Crawford, M. W.", "given_names": "M. W.", "surname": "Crawford", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "P. M. Cook", "canonical_name": "Cook, P. M.", "given_names": "P. M.", "surname": "Cook", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "R. A. J. Walton", "canonical_name": "Walton, R. A. J.", "given_names": "R. A. J.", "surname": "Walton", "position": "Senior Sanitary Superintendent", "department": "Medical and Health - Gambia", "salary_scale": "C"},
    {"name": "G. A. B. Aubrey", "canonical_name": "Aubrey, G. A. B.", "given_names": "G. A. B.", "surname": "Aubrey", "position": "Meteorologist", "department": "Meteorological - Gambia", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
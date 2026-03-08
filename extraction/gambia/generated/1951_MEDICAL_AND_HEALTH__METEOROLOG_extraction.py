"""
Gambia Colonial Office List 1951 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1951

OFFICIALS = [
    {"name": "E. J. Bury", "canonical_name": "Bury, E. J.", "given_names": "E. J.", "surname": "Bury", "position": "Director of Medical Services", "department": "Medical and Health - Gambia", "salary_min": 1350, "salary_max": 1350},
    {"name": "W. E. Hadden", "canonical_name": "Hadden, W. E.", "given_names": "W. E.", "surname": "Hadden", "position": "Medical Officer of Health", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "G. E. J. Porter", "canonical_name": "Porter, G. E. J.", "given_names": "G. E. J.", "surname": "Porter", "position": "Medical Officer", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "S. H. O. Jones", "canonical_name": "Jones, S. H. O.", "given_names": "S. H. O.", "surname": "Jones", "position": "Medical Officer", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "E. F. B. Forster", "canonical_name": "Forster, E. F. B.", "given_names": "E. F. B.", "surname": "Forster", "position": "Medical Officer", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "T. S. Klosowski", "canonical_name": "Klosowski, T. S.", "given_names": "T. S.", "surname": "Klosowski", "position": "Medical Officer", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "A. E. Carrol", "canonical_name": "Carrol, A. E.", "given_names": "A. E.", "surname": "Carrol", "position": "Medical Officer", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "R. W. Campbell", "canonical_name": "Campbell, R. W.", "given_names": "R. W.", "surname": "Campbell", "position": "Entomologist", "department": "Medical and Health - Gambia", "salary_scale": "A"},
    {"name": "J. A. M. Henderson", "canonical_name": "Henderson, J. A. M.", "given_names": "J. A. M.", "surname": "Henderson", "position": "Senior Nursing Sister", "department": "Medical and Health - Gambia"},
    {"name": "M. M. Wordie", "canonical_name": "Wordie, M. M.", "given_names": "M. M.", "surname": "Wordie", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "M. M. Shepherd", "canonical_name": "Shepherd, M. M.", "given_names": "M. M.", "surname": "Shepherd", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "C. N. Michie", "canonical_name": "Michie, C. N.", "given_names": "C. N.", "surname": "Michie", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "M. W. Crawford", "canonical_name": "Crawford, M. W.", "given_names": "M. W.", "surname": "Crawford", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "P. M. Cook", "canonical_name": "Cook, P. M.", "given_names": "P. M.", "surname": "Cook", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "K. J. D. Shouksmith", "canonical_name": "Shouksmith, K. J. D.", "given_names": "K. J. D.", "surname": "Shouksmith", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "D. Meredith", "canonical_name": "Meredith, D.", "given_names": "D.", "surname": "Meredith", "position": "Nursing Sister", "department": "Medical and Health - Gambia", "salary_scale": "N"},
    {"name": "R. A. J. Walton", "canonical_name": "Walton, R. A. J.", "given_names": "R. A. J.", "surname": "Walton", "position": "Senior Sanitary Superintendent", "department": "Medical and Health - Gambia", "salary_scale": "C"},
    {"name": "G. A. B. Aubrey", "canonical_name": "Aubrey, G. A. B.", "given_names": "G. A. B.", "surname": "Aubrey", "position": "Meteorologist", "department": "Meteorological - Gambia", "salary_scale": "A"},
    {"name": "G. D. Maydon", "canonical_name": "Maydon, G. D.", "given_names": "G. D.", "surname": "Maydon", "position": "Superintendent of Police and Inspector of Prisons", "department": "Police and Prisons - Gambia", "salary_scale": "B"},
    {"name": "J. N. Ferguson", "canonical_name": "Ferguson, J. N.", "given_names": "J. N.", "surname": "Ferguson", "position": "Assistant Superintendent of Police", "department": "Police and Prisons - Gambia", "salary_scale": "B"},
    {"name": "P. A. Williams", "canonical_name": "Williams, P. A.", "given_names": "P. A.", "surname": "Williams", "position": "Assistant Superintendent of Police", "department": "Police and Prisons - Gambia", "salary_scale": "B"},
    {"name": "G. T. Bolton", "canonical_name": "Bolton, G. T.", "given_names": "G. T.", "surname": "Bolton", "position": "Assistant Superintendent of Police", "department": "Police and Prisons - Gambia", "salary_scale": "B"},
    {"name": "E. C. Sowe", "canonical_name": "Sowe, E. C.", "given_names": "E. C.", "surname": "Sowe", "position": "Postmaster General", "department": "Post Office - Gambia", "salary_scale": "B"},
    {"name": "O. B. Johnson", "canonical_name": "Johnson, O. B.", "given_names": "O. B.", "surname": "Johnson", "position": "Assistant Postmaster General", "department": "Post Office - Gambia", "salary_scale": "F5"},
    {"name": "J. A. George", "canonical_name": "George, J. A.", "given_names": "J. A.", "surname": "George", "position": "Government Printer", "department": "Printing - Gambia", "salary_scale": "C"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
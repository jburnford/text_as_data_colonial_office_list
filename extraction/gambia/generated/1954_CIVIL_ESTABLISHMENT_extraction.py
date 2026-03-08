"""
Gambia Colonial Office List 1954 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1954

OFFICIALS = [
    {"name": "Sir Percy Wyn-Harris", "canonical_name": "Wyn-Harris, Percy", "surname": "Wyn-Harris", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "honors": ["K.C.M.G.", "M.B.E."]},
    {"name": "A. N. A. Waddell", "canonical_name": "Waddell, A. N. A.", "given_names": "A. N. A.", "surname": "Waddell", "position": "Colonial Secretary", "department": "Civil Establishment - Gambia", "honors": ["D.S.C."]},
    {"name": "A. C. Spurling", "canonical_name": "Spurling, A. C.", "given_names": "A. C.", "surname": "Spurling", "position": "Attorney-General", "department": "Civil Establishment - Gambia"},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Financial Secretary", "department": "Civil Establishment - Gambia", "honors": ["O.B.E."]},
    {"name": "G. Humphrey-Smith", "canonical_name": "Humphrey-Smith, G.", "given_names": "G.", "surname": "Humphrey-Smith", "position": "Senior Commissioner", "department": "Civil Establishment - Gambia", "honors": ["O.B.E."]},
    {"name": "B. R. Miles", "canonical_name": "Miles, B. R.", "given_names": "B. R.", "surname": "Miles", "position": "Judge, Supreme Court", "department": "Civil Establishment - Gambia"},
    {"name": "E. B. W. Carrol", "canonical_name": "Carrol, E. B. W.", "given_names": "E. B. W.", "surname": "Carrol", "position": "Accountant-General", "department": "Civil Establishment - Gambia", "honors": ["O.B.E."]},
    {"name": "G. T. C. Morris", "canonical_name": "Morris, G. T. C.", "given_names": "G. T. C.", "surname": "Morris", "position": "Principal Auditor", "department": "Civil Establishment - Gambia", "honors": ["T.D."]},
    {"name": "S. H. Jones", "canonical_name": "Jones, S. H.", "given_names": "S. H.", "surname": "Jones", "position": "Collector of Customs", "department": "Civil Establishment - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Director of Agriculture", "department": "Civil Establishment - Gambia"},
    {"name": "J. W. Forrest", "canonical_name": "Forrest, J. W.", "given_names": "J. W.", "surname": "Forrest", "position": "Director of Education", "department": "Civil Establishment - Gambia"},
    {"name": "G. J. Webster", "canonical_name": "Webster, G. J.", "given_names": "G. J.", "surname": "Webster", "position": "Principal Marine Officer", "department": "Civil Establishment - Gambia"},
    {"name": "S. H. O. Jones", "canonical_name": "Jones, S. H. O.", "given_names": "S. H. O.", "surname": "Jones", "position": "Director of Medical Services", "department": "Civil Establishment - Gambia", "honors": ["O.B.E."]},
    {"name": "G. D. Maydon", "canonical_name": "Maydon, G. D.", "given_names": "G. D.", "surname": "Maydon", "position": "Superintendent of Police", "department": "Civil Establishment - Gambia"},
    {"name": "E. C. Sowe", "canonical_name": "Sowe, E. C.", "given_names": "E. C.", "surname": "Sowe", "position": "Postmaster General", "department": "Civil Establishment - Gambia", "honors": ["M.B.E."]},
    {"name": "J. A. George", "canonical_name": "George, J. A.", "given_names": "J. A.", "surname": "George", "position": "Government Printer", "department": "Civil Establishment - Gambia"},
    {"name": "R. J. S. Pearce", "canonical_name": "Pearce, R. J. S.", "given_names": "R. J. S.", "surname": "Pearce", "position": "Superintendent of Prisons", "department": "Civil Establishment - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Director of Public Works", "department": "Civil Establishment - Gambia"},
    {"name": "D. H. Yarnold", "canonical_name": "Yarnold, D. H.", "given_names": "D. H.", "surname": "Yarnold", "position": "Deputy Director of Public Works", "department": "Civil Establishment - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Superintendent of Surveys", "department": "Civil Establishment - Gambia"},
    {"name": "S. L. H. Walshe", "canonical_name": "Walshe, S. L. H.", "given_names": "S. L. H.", "surname": "Walshe", "position": "Senior Veterinary Officer", "department": "Civil Establishment - Gambia"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
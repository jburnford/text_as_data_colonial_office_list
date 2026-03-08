"""
Gambia Colonial Office List 1962 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1962

OFFICIALS = [
    {"name": "J. W. Paul", "canonical_name": "Paul, J. W.", "given_names": "J. W.", "surname": "Paul", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "honors": ["O.B.E.", "M.C."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Aide-de-Camp", "department": "Civil Establishment - Gambia"},
    {"name": "K. G. S. Smith", "canonical_name": "Smith, K. G. S.", "given_names": "K. G. S.", "surname": "Smith", "position": "Civil Secretary", "department": "Civil Establishment - Gambia", "honors": ["C.M.G."]},
    {"name": "P. A. Gore", "canonical_name": "Gore, P. A.", "given_names": "P. A.", "surname": "Gore", "position": "Financial Secretary", "department": "Civil Establishment - Gambia"},
    {"name": "M. H. Orde", "canonical_name": "Orde, M. H.", "given_names": "M. H.", "surname": "Orde", "position": "Commissioner for Local Government", "department": "Civil Establishment - Gambia"},
    {"name": "H. R. Monday", "canonical_name": "Monday, H. R.", "given_names": "H. R.", "surname": "Monday", "position": "Accountant General", "department": "Civil Establishment - Gambia", "honors": ["O.B.E."], "qualifications": ["J.P."]},
    {"name": "J. A. Austin", "canonical_name": "Austin, J. A.", "given_names": "J. A.", "surname": "Austin", "position": "Director of Agriculture", "department": "Civil Establishment - Gambia", "honors": ["O.B.E."]},
    {"name": "J. W. Adshead", "canonical_name": "Adshead, J. W.", "given_names": "J. W.", "surname": "Adshead", "position": "Principal Auditor", "department": "Civil Establishment - Gambia"},
    {"name": "J. G. Forster", "canonical_name": "Forster, J. G.", "given_names": "J. G.", "surname": "Forster", "position": "Collector of Customs", "department": "Civil Establishment - Gambia"},
    {"name": "A. M. Gregory", "canonical_name": "Gregory, A. M.", "given_names": "A. M.", "surname": "Gregory", "position": "Director of Education", "department": "Civil Establishment - Gambia", "honors": ["O.B.E."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Electrical Engineer", "department": "Civil Establishment - Gambia"},
    {"name": "H. S. S. Few", "canonical_name": "Few, H. S. S.", "given_names": "H. S. S.", "surname": "Few", "position": "Law Officer: Attorney-General", "department": "Civil Establishment - Gambia"},
    {"name": "G. H. Cunningham", "canonical_name": "Cunningham, G. H.", "given_names": "G. H.", "surname": "Cunningham", "position": "Director of Marine", "department": "Civil Establishment - Gambia", "honors": ["M.B.E."], "military_rank": "Lt. Comdr.", "qualifications": ["R.N. (Rtd.)"]},
    {"name": "S. H. O. Jones", "canonical_name": "Jones, S. H. O.", "given_names": "S. H. O.", "surname": "Jones", "position": "Director of Medical Services", "department": "Civil Establishment - Gambia", "honors": ["C.B.E."]},
    {"name": "E. C. Eates", "canonical_name": "Eates, E. C.", "given_names": "E. C.", "surname": "Eates", "position": "Commissioner of Police", "department": "Civil Establishment - Gambia"},
    {"name": "L. F. Valantine", "canonical_name": "Valantine, L. F.", "given_names": "L. F.", "surname": "Valantine", "position": "Postmaster General", "department": "Civil Establishment - Gambia", "honors": ["M.B.E."]},
    {"name": "S. H. Riley", "canonical_name": "Riley, S. H.", "given_names": "S. H.", "surname": "Riley", "position": "Government Printer", "department": "Civil Establishment - Gambia"},
    {"name": "M. J. Forster", "canonical_name": "Forster, M. J.", "given_names": "M. J.", "surname": "Forster", "position": "Superintendent of Prisons", "department": "Civil Establishment - Gambia"},
    {"name": "J. S. Pullinger", "canonical_name": "Pullinger, J. S.", "given_names": "J. S.", "surname": "Pullinger", "position": "Director of Public Works", "department": "Civil Establishment - Gambia", "honors": ["O.B.E.", "G.M."]},
    {"name": "B. O. Semga-Janneh", "canonical_name": "Semga-Janneh, B. O.", "given_names": "B. O.", "surname": "Semga-Janneh", "position": "Superintendent of Surveys", "department": "Civil Establishment - Gambia", "honors": ["M.B.E."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Principal Veterinary Officer", "department": "Civil Establishment - Gambia"},
    {"name": "A. L. Mackintosh", "canonical_name": "Mackintosh, A. L.", "given_names": "A. L.", "surname": "Mackintosh", "position": "Registrar of Co-operative Societies", "department": "Civil Establishment - Gambia", "honors": ["M.B.E."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
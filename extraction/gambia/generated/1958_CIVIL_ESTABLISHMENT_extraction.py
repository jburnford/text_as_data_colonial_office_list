"""
Gambia Colonial Office List 1958 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1958

OFFICIALS = [
    {"name": "Sir Percy Wyn-Harris", "canonical_name": "Wyn-Harris, Percy", "given_names": "Percy", "surname": "Wyn-Harris", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "honors": ["K.C.M.G.", "M.B.E."]},
    {"name": "E. H. Windley", "canonical_name": "Windley, E. H.", "given_names": "E. H.", "surname": "Windley", "position": "Colonial Secretary", "department": "Civil Establishment - Gambia", "honors": ["C.M.G."], "acting_status": "designate"},
    {"name": "K. G. S. Smith", "canonical_name": "Smith, K. G. S.", "given_names": "K. G. S.", "surname": "Smith", "position": "Colonial Secretary", "department": "Civil Establishment - Gambia", "honors": ["C.M.G."]},
    {"name": "L. Weston", "canonical_name": "Weston, L.", "given_names": "L.", "surname": "Weston", "position": "Attorney-General", "department": "Civil Establishment - Gambia", "qualifications": ["Q.C."]},
    {"name": "V. E. Davies", "canonical_name": "Davies, V. E.", "given_names": "V. E.", "surname": "Davies", "position": "Financial Secretary", "department": "Civil Establishment - Gambia", "honors": ["O.B.E."]},
    {"name": "K. J. Frazer", "canonical_name": "Frazer, K. J.", "given_names": "K. J.", "surname": "Frazer", "position": "Senior Commissioner", "department": "Civil Establishment - Gambia", "honors": ["M.C."]},
    {"name": "K. J. W. Lane", "canonical_name": "Lane, K. J. W.", "given_names": "K. J. W.", "surname": "Lane", "position": "Colony Commissioner", "department": "Civil Establishment - Gambia"},
    {"name": "J. A. L. Wiseman", "canonical_name": "Wiseman, J. A. L.", "given_names": "J. A. L.", "surname": "Wiseman", "position": "Chief Justice", "department": "Civil Establishment - Gambia"},
    {"name": "H. R. Monday", "canonical_name": "Monday, H. R.", "given_names": "H. R.", "surname": "Monday", "position": "Accountant-General", "department": "Civil Establishment - Gambia", "qualifications": ["J.P."]},
    {"name": "D. W. Dunlop", "canonical_name": "Dunlop, D. W.", "given_names": "D. W.", "surname": "Dunlop", "position": "Principal Auditor", "department": "Civil Establishment - Gambia"},
    {"name": "S. H. Jones", "canonical_name": "Jones, S. H.", "given_names": "S. H.", "surname": "Jones", "position": "Collector of Customs", "department": "Civil Establishment - Gambia"},
    {"name": "J. A. Austin", "canonical_name": "Austin, J. A.", "given_names": "J. A.", "surname": "Austin", "position": "Director of Agriculture", "department": "Civil Establishment - Gambia"},
    {"name": "A. M. Gregory", "canonical_name": "Gregory, A. M.", "given_names": "A. M.", "surname": "Gregory", "position": "Director of Education", "department": "Civil Establishment - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Electrical Engineer", "department": "Civil Establishment - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Forestry Adviser", "department": "Civil Establishment - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Director of Marine", "department": "Civil Establishment - Gambia"},
    {"name": "S. H. O. Jones", "canonical_name": "Jones, S. H. O.", "given_names": "S. H. O.", "surname": "Jones", "position": "Director of Medical Services", "department": "Civil Establishment - Gambia", "honors": ["C.B.E."]},
    {"name": "E. C. Eates", "canonical_name": "Eates, E. C.", "given_names": "E. C.", "surname": "Eates", "position": "Commissioner of Police", "department": "Civil Establishment - Gambia"},
    {"name": "E. C. Sowe", "canonical_name": "Sowe, E. C.", "given_names": "E. C.", "surname": "Sowe", "position": "Postmaster General", "department": "Civil Establishment - Gambia", "honors": ["O.B.E."]},
    {"name": "J. A. George", "canonical_name": "George, J. A.", "given_names": "J. A.", "surname": "George", "position": "Government Printer", "department": "Civil Establishment - Gambia"},
    {"name": "S. J. E. Lusack", "canonical_name": "Lusack, S. J. E.", "given_names": "S. J. E.", "surname": "Lusack", "position": "Superintendent of Prisons", "department": "Civil Establishment - Gambia"},
    {"name": "J. S. Pullinger", "canonical_name": "Pullinger, J. S.", "given_names": "J. S.", "surname": "Pullinger", "position": "Director of Public Works", "department": "Civil Establishment - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Director of Public Works", "department": "Civil Establishment - Gambia"},
    {"name": "B. O. Semega Janneh", "canonical_name": "Semega Janneh, B. O.", "given_names": "B. O.", "surname": "Semega Janneh", "position": "Superintendent of Surveys", "department": "Civil Establishment - Gambia", "honors": ["M.B.E."]},
    {"name": "S. L. H. Walshe", "canonical_name": "Walshe, S. L. H.", "given_names": "S. L. H.", "surname": "Walshe", "position": "Principal Veterinary Officer", "department": "Civil Establishment - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
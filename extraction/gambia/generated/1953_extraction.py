"""
Gambia Colonial Office List 1953 - Extracted Data (Merged from 1 sections)
"""
COLONY = "Gambia"
YEAR = 1953

OFFICIALS = [{'name': 'Sir Percy Wyn-Harris', 'canonical_name': 'Wyn-Harris, Percy', 'surname': 'Wyn-Harris', 'position': 'Governor and Commander-in-Chief', 'department': 'Civil Establishment - Gambia', 'honors': ['K.C.M.G.', 'M.B.E.']}, {'name': 'A. N. A. Waddell', 'canonical_name': 'Waddell, A. N. A.', 'surname': 'Waddell', 'position': 'Colonial Secretary', 'department': 'Civil Establishment - Gambia', 'honors': ['D.S.C.']}, {'name': 'A. C. Spurling', 'canonical_name': 'Spurling, A. C.', 'surname': 'Spurling', 'position': 'Attorney-General', 'department': 'Civil Establishment - Gambia'}, {'name': 'A. R. Clark', 'canonical_name': 'Clark, A. R.', 'surname': 'Clark', 'position': 'Financial Secretary', 'department': 'Civil Establishment - Gambia', 'honors': ['O.B.E.']}, {'name': 'G. Humphrey-Smith', 'canonical_name': 'Humphrey-Smith, G.', 'surname': 'Humphrey-Smith', 'position': 'Senior Commissioner', 'department': 'Civil Establishment - Gambia', 'honors': ['O.B.E.']}, {'name': 'E. B. W. Carrol', 'canonical_name': 'Carrol, E. B. W.', 'surname': 'Carrol', 'position': 'Accountant-General', 'department': 'Civil Establishment - Gambia', 'honors': ['O.B.E.']}, {'name': 'G. T. C. Morris', 'canonical_name': 'Morris, G. T. C.', 'surname': 'Morris', 'position': 'Principal Auditor', 'department': 'Civil Establishment - Gambia'}, {'name': 'S. H. Jones', 'canonical_name': 'Jones, S. H.', 'surname': 'Jones', 'position': 'Collector of Customs', 'department': 'Civil Establishment - Gambia'}, {'name': 'C. B. Garnett', 'canonical_name': 'Garnett, C. B.', 'surname': 'Garnett', 'position': 'Director of Development and Agriculture', 'department': 'Civil Establishment - Gambia'}, {'name': 'J. W. Forrest', 'canonical_name': 'Forrest, J. W.', 'surname': 'Forrest', 'position': 'Director of Education', 'department': 'Civil Establishment - Gambia'}, {'name': 'S. H. O. Jones', 'canonical_name': 'Jones, S. H. O.', 'surname': 'Jones', 'position': 'Director of Medical Services', 'department': 'Civil Establishment - Gambia'}, {'name': 'G. D. Maydon', 'canonical_name': 'Maydon, G. D.', 'surname': 'Maydon', 'position': 'Superintendent of Police', 'department': 'Civil Establishment - Gambia'}, {'name': 'E. C. Sowe', 'canonical_name': 'Sowe, E. C.', 'surname': 'Sowe', 'position': 'Postmaster General', 'department': 'Civil Establishment - Gambia', 'honors': ['M.B.E.']}, {'name': 'K. Wilson', 'canonical_name': 'Wilson, K.', 'surname': 'Wilson', 'position': 'Director of Public Works', 'department': 'Civil Establishment - Gambia'}, {'name': 'D. H. Yarnold', 'canonical_name': 'Yarnold, D. H.', 'surname': 'Yarnold', 'position': 'Deputy Director of Public Works', 'department': 'Civil Establishment - Gambia'}, {'name': 'S. L. H. Walshe', 'canonical_name': 'Walshe, S. L. H.', 'surname': 'Walshe', 'position': 'Senior Veterinary Officer', 'department': 'Civil Establishment - Gambia'}]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()

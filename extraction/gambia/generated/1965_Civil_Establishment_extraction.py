"""
Gambia Colonial Office List 1965 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1965

OFFICIALS = [
    {"name": "Sir John Paul", "canonical_name": "Paul, John", "surname": "Paul", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "honors": ["K.C.M.G.", "O.B.E.", "M.C."]},
    {"name": "P. A. Gore", "canonical_name": "Gore, P. A.", "surname": "Gore", "position": "Deputy Governor", "department": "Civil Establishment - Gambia", "honors": ["C.M.G.", "C.V.O."]},
    {"name": "K. J. W. Lane", "canonical_name": "Lane, K. J. W.", "surname": "Lane", "position": "Secretary", "department": "Office of the Prime Minister - Gambia", "honors": ["O.B.E.", "M.V.O."]},
    {"name": "K. J. W. Lane", "canonical_name": "Lane, K. J. W.", "surname": "Lane", "position": "Secretary to the Cabinet", "department": "Office of the Prime Minister - Gambia", "honors": ["O.B.E.", "M.V.O."]},
    {"name": "D. A. Percival", "canonical_name": "Percival, D. A.", "surname": "Percival", "position": "Economic Adviser", "department": "Civil Establishment - Gambia"},
    {"name": "G. Peters", "canonical_name": "Peters, G.", "surname": "Peters", "position": "Information Officer", "department": "Civil Establishment - Gambia", "honors": ["M.B.E."]},
    {"name": "S. H. Riley", "canonical_name": "Riley, S. H.", "surname": "Riley", "position": "Government Printer", "department": "Civil Establishment - Gambia", "honors": ["M.B.E."]},
    {"name": "M. J. Forster", "canonical_name": "Forster, M. J.", "surname": "Forster", "position": "Superintendent of Prisons", "department": "Civil Establishment - Gambia"},
    {"name": "J. P. M. Bray", "canonical_name": "Bray, J. P. M.", "surname": "Bray", "position": "Commissioner of Police", "department": "Civil Establishment - Gambia", "honors": ["C.P.M."]},
    {"name": "C. G. Dixon", "canonical_name": "Dixon, C. G.", "surname": "Dixon", "position": "Establishment Secretary", "department": "Civil Establishment - Gambia"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1964 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1964

OFFICIALS = [
    {"name": "K. J. W. Lane", "canonical_name": "Lane, K. J. W.", "given_names": "K. J. W.", "surname": "Lane", "position": "Secretary", "department": "Office of the Prime Minister - Gambia", "honors": ["M.V.O."]},
    {"name": "D. A. Percival", "canonical_name": "Percival, D. A.", "given_names": "D. A.", "surname": "Percival", "position": "Economic Adviser", "department": "Office of the Prime Minister - Gambia"},
    {"name": "G. Peters", "canonical_name": "Peters, G.", "given_names": "G.", "surname": "Peters", "position": "Information Officer", "department": "Office of the Prime Minister - Gambia", "honors": ["M.B.E."]},
    {"name": "S. H. Riley", "canonical_name": "Riley, S. H.", "given_names": "S. H.", "surname": "Riley", "position": "Government Printer", "department": "Office of the Prime Minister - Gambia"},
    {"name": "M. J. Forster", "canonical_name": "Forster, M. J.", "given_names": "M. J.", "surname": "Forster", "position": "Superintendent of Prisons", "department": "Office of the Prime Minister - Gambia"},
    {"name": "J. P. M. Bray", "canonical_name": "Bray, J. P. M.", "given_names": "J. P. M.", "surname": "Bray", "position": "Commissioner of Police", "department": "Office of the Prime Minister - Gambia", "honors": ["C.P.M."]},
    {"name": "R. L. W. Mansfield", "canonical_name": "Mansfield, R. L. W.", "given_names": "R. L. W.", "surname": "Mansfield", "position": "Establishment Secretary", "department": "Office of the Prime Minister - Gambia"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
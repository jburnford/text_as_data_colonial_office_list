"""
Gambia Colonial Office List 1963 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1963

OFFICIALS = [
    {"name": "K. J. W. Lane", "canonical_name": "Lane, K. J. W.", "given_names": "K. J. W.", "surname": "Lane", "position": "Principal Secretary", "department": "Office of the Premier - Gambia", "honors": ["M.V.O."]},
    {"name": "D. A. Percival", "canonical_name": "Percival, D. A.", "given_names": "D. A.", "surname": "Percival", "position": "Economic Adviser", "department": "Office of the Premier - Gambia"},
    {"name": "G. Peters", "canonical_name": "Peters, G.", "given_names": "G.", "surname": "Peters", "position": "Information Officer", "department": "Office of the Premier - Gambia", "honors": ["M.B.E."], "military_rank": "Captain"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
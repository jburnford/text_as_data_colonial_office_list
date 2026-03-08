"""
Gambia Colonial Office List 1965 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1965

OFFICIALS = [
    {"name": "P. R. Bridges", "canonical_name": "Bridges, P. R.", "given_names": "P. R.", "surname": "Bridges", "position": "Attorney-General", "department": "Attorney-General - Gambia"},
    {"name": "S. H. A. George", "canonical_name": "George, S. H. A.", "given_names": "S. H. A.", "surname": "George", "position": "Solicitor-General", "department": "Solicitor-General - Gambia"},
    {"name": "J. W. Adshead", "canonical_name": "Adshead, J. W.", "given_names": "J. W.", "surname": "Adshead", "position": "Director of Audit", "department": "Audit - Gambia", "honors": ["M.B.E."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
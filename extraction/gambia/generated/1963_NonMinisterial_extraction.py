"""
Gambia Colonial Office List 1963 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1963

OFFICIALS = [
    {"name": "H. S. S. Few", "canonical_name": "Few, H. S. S.", "given_names": "H. S. S.", "surname": "Few", "position": "Attorney-General", "department": "Attorney-General - Gambia"},
    {"name": "J. W. Adshead", "canonical_name": "Adshead, J. W.", "given_names": "J. W.", "surname": "Adshead", "position": "Principal Auditor", "department": "Principal Auditor - Gambia"},
    {"name": "E. C. Eates", "canonical_name": "Eates, E. C.", "given_names": "E. C.", "surname": "Eates", "position": "Commissioner of Police", "department": "Commissioner of Police - Gambia", "honors": ["M.V.O."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
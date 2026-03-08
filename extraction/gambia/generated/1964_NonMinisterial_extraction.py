"""
Gambia Colonial Office List 1964 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1964

OFFICIALS = [
    {"name": "H. S. S. Few", "canonical_name": "Few, H. S. S.", "given_names": "H. S. S.", "surname": "Few", "position": "Attorney-General", "department": "Judicial - Gambia", "qualifications": ["Q.C."]},
    {"name": "P. R. Bridges", "canonical_name": "Bridges, P. R.", "given_names": "P. R.", "surname": "Bridges", "position": "Solicitor-General", "department": "Judicial - Gambia"},
    {"name": "J. W. Adshead", "canonical_name": "Adshead, J. W.", "given_names": "J. W.", "surname": "Adshead", "position": "Director of Audit", "department": "Audit - Gambia"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
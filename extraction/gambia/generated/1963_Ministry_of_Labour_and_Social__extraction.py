"""
Gambia Colonial Office List 1963 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1963

OFFICIALS = [
    {"name": "S. O. Koku", "canonical_name": "Koku, S. O.", "given_names": "S. O.", "surname": "Koku", "position": "Secretary to Ministry and Commissioner of Labour", "department": "Ministry of Labour and Social Welfare - Gambia"},
    {"name": "M. J. Forster", "canonical_name": "Forster, M. J.", "given_names": "M. J.", "surname": "Forster", "position": "Superintendent of Prisons", "department": "Ministry of Labour and Social Welfare - Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Social Welfare Officer", "department": "Ministry of Labour and Social Welfare - Gambia"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
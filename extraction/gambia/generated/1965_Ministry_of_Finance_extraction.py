"""
Gambia Colonial Office List 1965 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1965

OFFICIALS = [
    {"name": "F. D. C. Williams", "canonical_name": "Williams, F. D. C.", "given_names": "F. D. C.", "surname": "Williams", "position": "Financial Secretary", "department": "Ministry of Finance - Gambia", "honors": ["C.M.G."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Financial Secretary", "department": "Ministry of Finance - Gambia"},
    {"name": "E. W. D. Thomas", "canonical_name": "Thomas, E. W. D.", "given_names": "E. W. D.", "surname": "Thomas", "position": "Accountant-General", "department": "Ministry of Finance - Gambia", "honors": ["O.B.E."]},
    {"name": "J. G. Forster", "canonical_name": "Forster, J. G.", "given_names": "J. G.", "surname": "Forster", "position": "Comptroller of Customs", "department": "Ministry of Finance - Gambia", "honors": ["O.B.E."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
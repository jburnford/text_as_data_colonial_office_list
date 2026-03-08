"""
Gambia Colonial Office List 1936 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1936

OFFICIALS = [
    {"name": "Sir Arthur F. Richards", "canonical_name": "Richards, Arthur F.", "surname": "Richards", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 750, "honors": ["K.C.M.G."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Aide-de-Camp and Private Secretary", "department": "Civil Establishment - Gambia"},
    {"name": "H. R. Oke", "canonical_name": "Oke, H. R.", "given_names": "H. R.", "surname": "Oke", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "honors": ["M.C."]},
    {"name": "G. Amos", "canonical_name": "Amos, G.", "given_names": "G.", "surname": "Amos", "position": "Office Assistant", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "African Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 300, "salary_max": 450},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Government Printer", "department": "Printing Branch - Gambia", "salary_min": 260, "salary_max": 360},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
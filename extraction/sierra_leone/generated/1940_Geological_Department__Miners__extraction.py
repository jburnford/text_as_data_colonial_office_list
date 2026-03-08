"""
Sierra Leone Colonial Office List 1940 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1940

OFFICIALS = [
    {"name": "J. D. Pollatt", "canonical_name": "Pollatt, J. D.", "given_names": "J. D.", "surname": "Pollatt", "position": "Geologist", "department": "Geological Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "K. E. Heesom", "canonical_name": "Heesom, K. E.", "given_names": "K. E.", "surname": "Heesom", "position": "Chief Inspector of Mines", "department": "Miners Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "F. A. Cassidy", "canonical_name": "Cassidy, F. A.", "given_names": "F. A.", "surname": "Cassidy", "position": "Inspector of Mines", "department": "Miners Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. Akwiromi", "canonical_name": "Akwiromi, A.", "given_names": "A.", "surname": "Akwiromi", "position": "Assistant Inspector of Mines", "department": "Miners Department - Sierra Leone", "salary_min": 300, "salary_max": 450},
    {"name": "A. R. Jones", "canonical_name": "Jones, A. R.", "given_names": "A. R.", "surname": "Jones", "position": "Meteorological Asst.", "department": "Meteorological Department - Sierra Leone", "salary_min": 400, "salary_max": 720},
    {"name": "H. U. Richards", "canonical_name": "Richards, H. U.", "given_names": "H. U.", "surname": "Richards", "position": "Licut.-Colonel", "department": "Sierra Leone Battalion, Royal West African Frontier Force - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "per_diem": "10s. a day", "military_rank": "Lt.-Col."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
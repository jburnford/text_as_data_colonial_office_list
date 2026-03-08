"""
Sierra Leone Colonial Office List 1939 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1939

OFFICIALS = [
    {"name": "J. D. Pollett", "canonical_name": "Pollett, J. D.", "given_names": "J. D.", "surname": "Pollett", "position": "Geologist", "department": "Geological Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "K. E. Heesom", "canonical_name": "Heesom, K. E.", "given_names": "K. E.", "surname": "Heesom", "position": "Chief Inspector of Mines", "department": "Mines Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "F. A. Cassidy", "canonical_name": "Cassidy, F. A.", "given_names": "F. A.", "surname": "Cassidy", "position": "Inspector of Mines", "department": "Mines Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. Akiwumi", "canonical_name": "Akiwumi, A.", "given_names": "A.", "surname": "Akiwumi", "position": "African Assistant Inspector of Mines", "department": "Mines Department - Sierra Leone", "salary_min": 300, "salary_max": 450},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
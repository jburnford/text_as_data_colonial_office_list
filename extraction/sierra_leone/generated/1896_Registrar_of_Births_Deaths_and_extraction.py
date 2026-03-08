"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "T. A. Davies", "canonical_name": "Davies, T. A.", "given_names": "T. A.", "surname": "Davies", "position": "Registrar of Births, Deaths, and Marriages", "department": "Registrar of Births, Deaths, and Marriages - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Bassia"},
    {"name": "E. M. Broderick", "canonical_name": "Broderick, E. M.", "given_names": "E. M.", "surname": "Broderick", "position": "Registrar of Births, Deaths, and Marriages", "department": "Registrar of Births, Deaths, and Marriages - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Kembia"},
    {"name": "A. D. Yaskey", "canonical_name": "Yaskey, A. D.", "given_names": "A. D.", "surname": "Yaskey", "position": "Registrar of Births, Deaths, and Marriages", "department": "Registrar of Births, Deaths, and Marriages - Sierra Leone", "salary_min": 50, "salary_max": 60, "location": "Robat"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
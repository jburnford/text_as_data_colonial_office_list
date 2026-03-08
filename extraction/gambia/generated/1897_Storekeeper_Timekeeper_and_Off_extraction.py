"""
Gambia Colonial Office List 1897 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1897

OFFICIALS = [
    {"name": "R. M. Fordie", "canonical_name": "Fordie, R. M.", "given_names": "R. M.", "surname": "Fordie", "position": "Colonial Surgeon", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 400, "allowances": "house allowance, 50L", "per_diem": "2s. 3d. per diem"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
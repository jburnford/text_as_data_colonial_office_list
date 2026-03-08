"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "W. T. Prout", "canonical_name": "Prout, W. T.", "given_names": "W. T.", "surname": "Prout", "position": "Colonial Surgeon", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 400, "allowances": "house allowance, 50l.", "per_diem": "2s. 3d. per diem"},
    {"name": "George Spilsbury", "canonical_name": "Spilsbury, George", "given_names": "George", "surname": "Spilsbury", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 100, "allowances": "residence"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
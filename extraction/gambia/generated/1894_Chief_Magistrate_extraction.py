"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "J. R. Maxwell", "canonical_name": "Maxwell, J. R.", "given_names": "J. R.", "surname": "Maxwell", "position": "Chief Magistrate", "department": "Judicial - Gambia", "salary_min": 600, "salary_max": 600, "allowances": "allowance in lieu of fees, 60l., and house allowance, 60l."},
    {"name": "W. C. Cates", "canonical_name": "Cates, W. C.", "given_names": "W. C.", "surname": "Cates", "position": "Registrar", "department": "Judicial - Gambia", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
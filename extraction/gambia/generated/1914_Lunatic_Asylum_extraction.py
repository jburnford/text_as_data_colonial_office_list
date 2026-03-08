"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "F. Tamplin", "canonical_name": "Tamplin, F.", "given_names": "F.", "surname": "Tamplin", "position": "Superintendent", "department": "Lunatic Asylum - Gambia", "salary_min": 150, "salary_max": 180}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1897 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1897

OFFICIALS = [
    {"name": "R. B. Llewelyn", "canonical_name": "Llewelyn, R. B.", "given_names": "R. B.", "surname": "Llewelyn", "position": "Administrator", "department": "Civil Establishment - Gambia", "honors": ["C.M.G."], "duty_allowance": 300, "allowances": "table allowance 10L per annum"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
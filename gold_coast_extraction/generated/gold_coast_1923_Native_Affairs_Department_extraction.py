"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "J. Maxwell", "canonical_name": "Maxwell, J.", "given_names": "J.", "surname": "Maxwell",
     "position": "Secretary for Native Affairs", "department": "Native Affairs Department - Gold Coast",
     "salary_min": 1350, "salary_max": 1350, "duty_allowance": 270, "honors": ["C.M.G."]},
    {"name": "C. W. Welman", "canonical_name": "Welman, C. W.", "given_names": "C. W.", "surname": "Welman",
     "position": "Deputy Secretary for Native Affairs", "department": "Native Affairs Department - Gold Coast",
     "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "J. C. de Graaff Johnson", "canonical_name": "de Graaff Johnson, J. C.", "given_names": "J. C.",
     "surname": "de Graaff Johnson", "position": "Assistant Secretary for Native Affairs",
     "department": "Native Affairs Department - Gold Coast", "salary_min": 375, "salary_max": 780},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1900 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1900

OFFICIALS = [
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "travelling allowance 91l. 5s."},
    {"name": "W. Haydon", "canonical_name": "Haydon, W.", "given_names": "W.", "surname": "Haydon", "position": "Curator", "department": "Botanical Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "J. Hartley", "canonical_name": "Hartley, J.", "given_names": "J.", "surname": "Hartley", "position": "Overseer", "department": "Botanical Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "T. A. Davies", "canonical_name": "Davies, T. A.", "given_names": "T. A.", "surname": "Davies", "position": "Officer-in-Charge", "department": "Post Office Department - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Bassia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
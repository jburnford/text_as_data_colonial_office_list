"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Inspector of Health", "department": "Sanitary Department - Sierra Leone"},
    {"name": "W. C. During", "canonical_name": "During, W. C.", "given_names": "W. C.", "surname": "During", "position": "Clerk to ditto", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
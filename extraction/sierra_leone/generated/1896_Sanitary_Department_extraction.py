"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "The Colonial Surgeon", "canonical_name": "Colonial Surgeon, The", "surname": "Surgeon", "position": "Inspector of Health", "department": "Sanitary Department - Sierra Leone"},
    {"name": "T. M. Cole", "canonical_name": "Cole, T. M.", "given_names": "T. M.", "surname": "Cole", "position": "Clerk", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
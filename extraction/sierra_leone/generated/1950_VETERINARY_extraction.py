"""
Sierra Leone Colonial Office List 1950 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1950

OFFICIALS = [
    {"name": "A. Fulton", "canonical_name": "Fulton, A.", "given_names": "A.", "surname": "Fulton", "position": "Director of Veterinary Services", "department": "Veterinary - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "S. L. H. Walshe", "canonical_name": "Walshe, S. L. H.", "given_names": "S. L. H.", "surname": "Walshe", "position": "Veterinary Officer", "department": "Veterinary - Sierra Leone", "salary_scale": "A"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
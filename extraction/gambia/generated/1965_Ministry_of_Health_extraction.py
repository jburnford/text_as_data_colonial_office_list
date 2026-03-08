"""
Gambia Colonial Office List 1965 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1965

OFFICIALS = [
    {"name": "J. A. Mahoney", "canonical_name": "Mahoney, J. A.", "given_names": "J. A.", "surname": "Mahoney", "position": "Secretary to Ministry and Director of Medical Services", "department": "Ministry of Health - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
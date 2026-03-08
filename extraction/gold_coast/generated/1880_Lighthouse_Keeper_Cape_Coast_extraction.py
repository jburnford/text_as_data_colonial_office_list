"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "John Paul", "canonical_name": "Paul, John", "given_names": "John", "surname": "Paul",
     "position": "Lighthouse Keeper", "department": "Civil Establishment - Gold Coast", "salary_min": 36, "salary_max": 36, "location": "Cape Coast"},
    {"name": "Jacob Francis", "canonical_name": "Francis, Jacob", "given_names": "Jacob", "surname": "Francis",
     "position": "Assistant", "department": "Civil Establishment - Gold Coast", "salary_min": 24, "salary_max": 24},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
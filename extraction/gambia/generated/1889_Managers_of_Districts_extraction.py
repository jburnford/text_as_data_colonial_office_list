"""
Gambia Colonial Office List 1889 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1889

OFFICIALS = [
    {"name": "E. A. M. Smith", "canonical_name": "Smith, E. A. M.", "given_names": "E. A. M.", "surname": "Smith", "position": "Manager of Districts", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250, "location": "McCarthy's Island"},
    {"name": "J. H. Finden", "canonical_name": "Finden, J. H.", "given_names": "J. H.", "surname": "Finden", "position": "Manager of Districts", "department": "Civil Establishment - Gambia", "salary_min": 100, "salary_max": 100, "location": "British Combo"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
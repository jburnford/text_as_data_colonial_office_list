"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "Herbert Taylor Ussher", "canonical_name": "Ussher, Herbert Taylor", "given_names": "Herbert Taylor", "surname": "Ussher",
     "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gold Coast", "salary_min": 3000,
     "honors": ["C.M.G."], "allowances": "And 500l. allowances"},
    {"name": "William Brandford Griffith", "canonical_name": "Griffith, William Brandford", "given_names": "William Brandford", "surname": "Griffith",
     "position": "Lieutenant-Governor", "department": "Civil Establishment - Gold Coast", "honors": ["C.M.G."]},
    {"name": "R. K. Barrow", "canonical_name": "Barrow, R. K.", "given_names": "R. K.", "surname": "Barrow",
     "position": "Aide-de-Camp & Private Secretary", "department": "Civil Establishment - Gold Coast", "salary_min": 300},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
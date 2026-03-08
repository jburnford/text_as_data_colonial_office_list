"""
Gold Coast Colonial Office List 1896 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1896

OFFICIALS = [
    {"name": "Governor's Clerk", "position": "Governor's Clerk", "department": "Civil Establishment - Gold Coast", "salary_min": 200, "salary_max": 250},
    {"name": "J. S. Hagan", "canonical_name": "Hagan, J. S.", "given_names": "J. S.", "surname": "Hagan", "position": "1st Clerk", "department": "Civil Establishment - Gold Coast", "salary_min": 150, "salary_max": 200},
    {"name": "S. H. Brew", "canonical_name": "Brew, S. H.", "given_names": "S. H.", "surname": "Brew", "position": "2nd Clerk", "department": "Civil Establishment - Gold Coast", "salary_min": 120, "salary_max": 150, "allowances": "24l. as shorthand writer"},
    {"name": "T. W. Parker", "canonical_name": "Parker, T. W.", "given_names": "T. W.", "surname": "Parker", "position": "3rd Clerk", "department": "Civil Establishment - Gold Coast", "salary_min": 50, "salary_max": 70},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
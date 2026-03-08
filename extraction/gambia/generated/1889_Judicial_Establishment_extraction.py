"""
Gambia Colonial Office List 1889 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1889

OFFICIALS = [
    {"name": "J. R. Maxwell", "canonical_name": "Maxwell, J. R.", "given_names": "J. R.", "surname": "Maxwell", "position": "Chief Magistrate", "department": "Judicial Establishment - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "W. C. Cates", "canonical_name": "Cates, W. C.", "given_names": "W. C.", "surname": "Cates", "position": "Clerk of Courts", "department": "Judicial Establishment - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "J. A. Martin", "canonical_name": "Martin, J. A.", "given_names": "J. A.", "surname": "Martin", "position": "Assistant Clerk of Courts", "department": "Judicial Establishment - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "Sergeant Sherrington", "canonical_name": "Sherrington, Sergeant", "surname": "Sherrington", "position": "Gaoler", "department": "Judicial Establishment - Gambia", "salary_min": 100, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
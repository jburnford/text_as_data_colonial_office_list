"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "Samuel Rowe", "canonical_name": "Rowe, Samuel", "given_names": "Samuel", "surname": "Rowe", "position": "Governor, Commander-in-Chief, and Vice-Admiral of W. Africa Settlements", "department": "Civil Establishment - Sierra Leone", "salary_min": 2000, "salary_max": 2000, "allowances": "500l. allowances", "honors": ["C.M.G."], "military_rank": "Surgeon-Major"},
    {"name": "J. H. Bond", "canonical_name": "Bond, J. H.", "given_names": "J. H.", "surname": "Bond", "position": "Aide-de-Camp", "department": "Civil Establishment - Sierra Leone", "acting_status": "acting", "military_rank": "Lieut."},
    {"name": "J. W. Lewis", "canonical_name": "Lewis, J. W.", "given_names": "J. W.", "surname": "Lewis", "position": "Governor's Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
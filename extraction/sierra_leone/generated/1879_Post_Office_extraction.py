"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "Isaac Fitzjohn", "canonical_name": "Fitzjohn, Isaac", "given_names": "Isaac", "surname": "Fitzjohn", "position": "Postmaster and Mail Packet Agent", "department": "Post Office - Sierra Leone", "salary_min": 200, "salary_max": 200, "allowances": "commission"},
    {"name": "S. Buckle", "canonical_name": "Buckle, S.", "given_names": "S.", "surname": "Buckle", "position": "1st Clerk", "department": "Post Office - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "Isaac S. Johnson", "canonical_name": "Johnson, Isaac S.", "given_names": "Isaac S.", "surname": "Johnson", "position": "2nd Clerk", "department": "Post Office - Sierra Leone", "salary_min": 35, "salary_max": 35},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sorter", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sorter", "department": "Post Office - Sierra Leone", "salary_min": 25, "salary_max": 25},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Mail Carrier", "department": "Post Office - Sierra Leone", "salary_min": 25, "salary_max": 25},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1880 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1880

OFFICIALS = [
    {"name": "Isaac Fitzjohn", "canonical_name": "Fitzjohn, Isaac", "given_names": "Isaac", "surname": "Fitzjohn", "position": "Postmaster and Mail Packet Agent", "department": "Post Office - Sierra Leone", "salary_min": 200, "salary_max": 200, "location": "Freetown"},
    {"name": "S. Buckle", "canonical_name": "Buckle, S.", "given_names": "S.", "surname": "Buckle", "position": "1st Clerk", "department": "Post Office - Sierra Leone", "salary_min": 60, "salary_max": 60, "location": "Freetown"},
    {"name": "Isaac S. Johnson", "canonical_name": "Johnson, Isaac S.", "given_names": "Isaac S.", "surname": "Johnson", "position": "2nd Clerk", "department": "Post Office - Sierra Leone", "salary_min": 35, "salary_max": 35, "location": "Freetown"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sorter", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 30, "location": "Freetown"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sorter", "department": "Post Office - Sierra Leone", "salary_min": 25, "salary_max": 25, "location": "Freetown"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Mail Carrier", "department": "Post Office - Sierra Leone", "salary_min": 25, "salary_max": 25, "location": "Freetown"},
    {"name": "The Deputy Harbour Master", "canonical_name": "Harbour Master, The Deputy", "surname": "Harbour Master", "position": "Superintendent", "department": "Lighthouse - Sierra Leone", "acting_status": "acting"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Lighthouse Keeper", "department": "Lighthouse - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Lighthouse Keeper", "department": "Lighthouse - Sierra Leone", "salary_min": 31, "salary_max": 31},
    {"name": "H. F. Blissett", "canonical_name": "Blissett, H. F.", "given_names": "H. F.", "surname": "Blissett", "position": "Auditor-Gen. of W. Africa Settlements", "department": "Audit Office - Sierra Leone", "salary_min": 250, "salary_max": 250, "honors": ["C.M.G."], "military_rank": "Commissary"},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "Clerk to Auditor-Gen.", "department": "Audit Office - Sierra Leone", "salary_min": 100, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
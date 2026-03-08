"""
Gambia Colonial Office List 1897 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1897

OFFICIALS = [
    {"name": "E. G. Hindle", "canonical_name": "Hindle, E. G.", "given_names": "E. G.", "surname": "Hindle", "position": "Governor's Confidential Clerk", "department": "Governor's Office - Gambia"},
    {"name": "I. H. Johnson", "canonical_name": "Johnson, I. H.", "given_names": "I. H.", "surname": "Johnson", "position": "2nd Clerk", "department": "Governor's Office - Gambia", "salary_min": 60, "salary_max": 60, "allowances": "25L interpreter"},
    {"name": "R. C. Grannum", "canonical_name": "Grannum, R. C.", "given_names": "R. C.", "surname": "Grannum", "position": "Local Auditor", "department": "Audit - Gambia"},
    {"name": "H. C. E. Barnes", "canonical_name": "Barnes, H. C. E.", "given_names": "H. C. E.", "surname": "Barnes", "position": "Assistant Auditor", "department": "Audit - Gambia"},
    {"name": "N. C. Nathan", "canonical_name": "Nathan, N. C.", "given_names": "N. C.", "surname": "Nathan", "position": "Clerk for Audit Duties", "department": "Audit - Gambia", "salary_min": 65, "salary_max": 65}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
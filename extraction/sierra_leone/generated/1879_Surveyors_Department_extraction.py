"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "J. W. Jenkins", "canonical_name": "Jenkins, J. W.", "given_names": "J. W.", "surname": "Jenkins", "position": "Colonial Surveyor, Commissioner of Roads, and Superintendent of Public Works", "department": "Surveyor's Department - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "travelling allowances, 136l. 17s. 6d."},
    {"name": "W. B. Campbell", "canonical_name": "Campbell, W. B.", "given_names": "W. B.", "surname": "Campbell", "position": "Clerk to Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 115, "salary_max": 115},
    {"name": "Robert Williams", "canonical_name": "Williams, Robert", "given_names": "Robert", "surname": "Williams", "position": "Extra Clerk", "department": "Surveyor's Department - Sierra Leone", "salary_min": 50, "salary_max": 50, "acting_status": "acting"},
    {"name": "J. A. Fitzjohn", "canonical_name": "Fitzjohn, J. A.", "given_names": "J. A.", "surname": "Fitzjohn", "position": "Storekeeper", "department": "Surveyor's Department - Sierra Leone", "salary_min": 45, "salary_max": 45},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
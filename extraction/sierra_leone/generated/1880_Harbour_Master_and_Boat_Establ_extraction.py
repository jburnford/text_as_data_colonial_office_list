"""
Sierra Leone Colonial Office List 1880 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1880

OFFICIALS = [
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Harbour Master", "department": "Harbour Master and Boat Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100, "acting_status": "deputy"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk", "department": "Harbour Master and Boat Establishment - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "S. H. John", "canonical_name": "John, S. H.", "given_names": "S. H.", "surname": "John", "position": "Journeyman in Charge of the Office", "department": "Printing Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. W. Jenkins", "canonical_name": "Jenkins, J. W.", "given_names": "J. W.", "surname": "Jenkins", "position": "Colonial Surveyor, Commissioner of Roads, and Superintendent of Public Works", "department": "Surveyor's Department - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "travelling allowance, 136l. 17s. 6d."},
    {"name": "W. B. Campbell", "canonical_name": "Campbell, W. B.", "given_names": "W. B.", "surname": "Campbell", "position": "Clerk to Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 115, "salary_max": 115},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Extra Clerk", "department": "Surveyor's Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Storekeeper", "department": "Surveyor's Department - Sierra Leone", "salary_min": 45, "salary_max": 45},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
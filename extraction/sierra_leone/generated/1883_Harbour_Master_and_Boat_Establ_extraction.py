"""
Sierra Leone Colonial Office List 1883 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1883

OFFICIALS = [
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Harbour Master", "department": "Harbour Master and Boat Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100, "acting_status": "Deputy"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk", "department": "Harbour Master and Boat Establishment - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "S. H. John", "canonical_name": "John, S. H.", "given_names": "S. H.", "surname": "John", "position": "Government Printer", "department": "Printing Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "R. E. Pownall", "canonical_name": "Pownall, R. E.", "given_names": "R. E.", "surname": "Pownall", "position": "Colonial Surveyor, Commissioner of Roads, and Superintendent of Public Works", "department": "Surveyor's Department - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "136l. 17s. 6d. travelling allowance"},
    {"name": "W. B. Campbell", "canonical_name": "Campbell, W. B.", "given_names": "W. B.", "surname": "Campbell", "position": "Clerk to Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 130, "salary_max": 130},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Inspector of Works and Roads", "department": "Surveyor's Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "Michael French", "canonical_name": "French, Michael", "given_names": "Michael", "surname": "French", "position": "Extra Clerk", "department": "Surveyor's Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. A. Fitzjohn", "canonical_name": "Fitzjohn, J. A.", "given_names": "J. A.", "surname": "Fitzjohn", "position": "Storekeeper", "department": "Surveyor's Department - Sierra Leone", "salary_min": 54, "salary_max": 54}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
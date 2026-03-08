"""
Sierra Leone Colonial Office List 1889 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1889

OFFICIALS = [
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Harbour Master", "department": "Harbour Master and Boat Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "J. H. Kelso", "canonical_name": "Kelso, J. H.", "given_names": "J. H.", "surname": "Kelso", "position": "Clerk to Harbour Master", "department": "Harbour Master and Boat Establishment - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "S. H. John", "canonical_name": "John, S. H.", "given_names": "S. H.", "surname": "John", "position": "Government Printer", "department": "Printing Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Journeyman", "department": "Printing Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "J. C. Gilpin", "canonical_name": "Gilpin, J. C.", "given_names": "J. C.", "surname": "Gilpin", "position": "Compositor", "department": "Printing Department - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Colonial Surveyor", "department": "Surveyor's Department - Sierra Leone"},
    {"name": "W. B. Campbell", "canonical_name": "Campbell, W. B.", "given_names": "W. B.", "surname": "Campbell", "position": "Clerk to Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "W. E. Inniss", "canonical_name": "Inniss, W. E.", "given_names": "W. E.", "surname": "Inniss", "position": "Inspectors of Works and Roads", "department": "Surveyor's Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "G. B. Craig", "canonical_name": "Craig, G. B.", "given_names": "G. B.", "surname": "Craig", "position": "Inspectors of Works and Roads", "department": "Surveyor's Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "B. A. Wright", "canonical_name": "Wright, B. A.", "given_names": "B. A.", "surname": "Wright", "position": "Extra Clerk", "department": "Surveyor's Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. A. Fitzjohn", "canonical_name": "Fitzjohn, J. A.", "given_names": "J. A.", "surname": "Fitzjohn", "position": "Storekeeper", "department": "Surveyor's Department - Sierra Leone", "salary_min": 54, "salary_max": 54}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
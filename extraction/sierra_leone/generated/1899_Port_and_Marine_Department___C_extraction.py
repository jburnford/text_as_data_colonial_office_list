"""
Sierra Leone Colonial Office List 1899 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1899

OFFICIALS = [
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "acting_status": "deputy", "salary_min": 100, "salary_max": 100},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Clerk to ditte", "department": "Port and Marine Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. N. Compton", "canonical_name": "Compton, J. N.", "given_names": "J. N.", "surname": "Compton", "position": "Commander", "department": "Colonial Steamer - Sierra Leone", "military_rank": "Capt.", "salary_min": 384, "salary_max": 384},
    {"name": "A. Forrester", "canonical_name": "Forrester, A.", "given_names": "A.", "surname": "Forrester", "position": "Chief Engineer", "department": "Colonial Steamer - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "A. Eaton", "canonical_name": "Eaton, A.", "given_names": "A.", "surname": "Eaton", "position": "2nd Engineer", "department": "Colonial Steamer - Sierra Leone", "salary_min": 252, "salary_max": 252},
    {"name": "J. E. Cole", "canonical_name": "Cole, J. E.", "given_names": "J. E.", "surname": "Cole", "position": "Clerk", "department": "Colonial Steamer - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Government Printer", "department": "Printing Department - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "J. C. Gilpin", "canonical_name": "Gilpin, J. C.", "given_names": "J. C.", "surname": "Gilpin", "position": "Second Printer", "department": "Printing Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "T. B. Macauley", "canonical_name": "Macauley, T. B.", "given_names": "T. B.", "surname": "Macauley", "position": "First Class Compositors", "department": "Printing Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. C. Johnston", "canonical_name": "Johnston, E. C.", "given_names": "E. C.", "surname": "Johnston", "position": "First Class Compositors", "department": "Printing Department - Sierra Leone", "salary_min": 40, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
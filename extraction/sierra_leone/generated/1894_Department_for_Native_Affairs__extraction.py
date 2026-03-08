"""
Sierra Leone Colonial Office List 1894 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1894

OFFICIALS = [
    {"name": "J. C. E. Parkes", "canonical_name": "Parkes, J. C. E.", "given_names": "J. C. E.", "surname": "Parkes", "position": "Superintendent", "department": "Department for Native Affairs - Sierra Leone", "salary_min": 270, "salary_max": 300},
    {"name": "Mohammed Sanusi", "canonical_name": "Sanusi, Mohammed", "surname": "Sanusi", "position": "Arabic Writer", "department": "Department for Native Affairs - Sierra Leone", "salary_min": 70, "salary_max": 70},
    {"name": "J. C. Turay", "canonical_name": "Turay, J. C.", "given_names": "J. C.", "surname": "Turay", "position": "Clerk", "department": "Department for Native Affairs - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "Katharudeen", "canonical_name": "Katharudeen, ", "surname": "Katharudeen", "position": "Clerk", "department": "Department for Native Affairs - Sierra Leone", "salary_min": 36, "salary_max": 36},
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "acting_status": "deputy", "salary_min": 100, "salary_max": 100},
    {"name": "O. J. Thomas", "canonical_name": "Thomas, O. J.", "given_names": "O. J.", "surname": "Thomas", "position": "Clerk to ditto", "department": "Port and Marine Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "J. N. Compton", "canonical_name": "Compton, J. N.", "given_names": "J. N.", "surname": "Compton", "position": "Commander", "department": "Colonial Steamer - Sierra Leone", "military_rank": "Capt.", "salary_min": 384, "salary_max": 384},
    {"name": "A. Forrester", "canonical_name": "Forrester, A.", "given_names": "A.", "surname": "Forrester", "position": "Chief Engineer", "department": "Colonial Steamer - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "T. Bramley", "canonical_name": "Bramley, T.", "given_names": "T.", "surname": "Bramley", "position": "2nd Engineer", "department": "Colonial Steamer - Sierra Leone", "salary_min": 252, "salary_max": 252},
    {"name": "S. H. John", "canonical_name": "John, S. H.", "given_names": "S. H.", "surname": "John", "position": "Government Printer", "department": "Printing Department - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Second Printer", "department": "Printing Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. C. Gilpin", "canonical_name": "Gilpin, J. C.", "given_names": "J. C.", "surname": "Gilpin", "position": "Composer", "department": "Printing Department - Sierra Leone", "salary_min": 36, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "J. C. E. Parkes", "canonical_name": "Parkes, J. C. E.", "given_names": "J. C. E.", "surname": "Parkes", "position": "Superintendent", "department": "Department for Native Affairs - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "Mohammed Sanusi", "canonical_name": "Sanusi, Mohammed", "surname": "Sanusi", "position": "Arabic Writer", "department": "Department for Native Affairs - Sierra Leone", "salary_min": 70, "salary_max": 70},
    {"name": "J. C. Turay", "canonical_name": "Turay, J. C.", "given_names": "J. C.", "surname": "Turay", "position": "Clerk", "department": "Department for Native Affairs - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "Katheredeen", "canonical_name": "Katheredeen, Katheredeen", "surname": "Katheredeen", "position": "Clerk", "department": "Department for Native Affairs - Sierra Leone", "salary_min": 36, "salary_max": 36},
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 100, "salary_max": 100, "acting_status": "deputy"},
    {"name": "O. J. Thomas", "canonical_name": "Thomas, O. J.", "given_names": "O. J.", "surname": "Thomas", "position": "Clerk to ditto", "department": "Port and Marine Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "J. N. Compton", "canonical_name": "Compton, J. N.", "given_names": "J. N.", "surname": "Compton", "position": "Commander", "department": "Port and Marine Department - Sierra Leone", "salary_min": 384, "salary_max": 384, "military_rank": "Capt."},
    {"name": "A. Forrester", "canonical_name": "Forrester, A.", "given_names": "A.", "surname": "Forrester", "position": "Chief Engineer", "department": "Port and Marine Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "R. Begg", "canonical_name": "Begg, R.", "given_names": "R.", "surname": "Begg", "position": "2nd Engineer", "department": "Port and Marine Department - Sierra Leone", "salary_min": 252, "salary_max": 252},
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Government Printer", "department": "Printing Department - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "J. C. Gilpin", "canonical_name": "Gilpin, J. C.", "given_names": "J. C.", "surname": "Gilpin", "position": "Second Printer", "department": "Printing Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "T. B. Macauley", "canonical_name": "Macauley, T. B.", "given_names": "T. B.", "surname": "Macauley", "position": "Compositor", "department": "Printing Department - Sierra Leone", "salary_min": 36, "salary_max": 45},
    {"name": "E. C. Johnston", "canonical_name": "Johnston, E. C.", "given_names": "E. C.", "surname": "Johnston", "position": "Compositor", "department": "Printing Department - Sierra Leone", "salary_min": 36, "salary_max": 45}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
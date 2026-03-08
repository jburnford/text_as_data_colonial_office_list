"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "J. O. Gore", "canonical_name": "Gore, J. O.", "given_names": "J. O.", "surname": "Gore", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 710, "salary_max": 800, "military_rank": "Lt.-Col."},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. E. Dawson", "canonical_name": "Dawson, J. E.", "given_names": "J. E.", "surname": "Dawson", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "2nd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. W. Paris", "canonical_name": "Paris, J. W.", "given_names": "J. W.", "surname": "Paris", "position": "3rd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "C. George", "canonical_name": "George, C.", "given_names": "C.", "surname": "George", "position": "4th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 55, "salary_max": 55},
    {"name": "J. T. Smith", "canonical_name": "Smith, J. T.", "given_names": "J. T.", "surname": "Smith", "position": "5th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 45, "salary_max": 45},
    {"name": "Bruce Faulkner", "canonical_name": "Faulkner, Bruce", "given_names": "Bruce", "surname": "Faulkner", "position": "6th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 35, "salary_max": 35},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "7th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 24, "salary_max": 24},
    {"name": "C. B. Mitford", "canonical_name": "Mitford, C. B.", "given_names": "C. B.", "surname": "Mitford", "position": "Colonial Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 500, "salary_max": 550},
    {"name": "S. M. Bennett", "canonical_name": "Bennett, S. M.", "given_names": "S. M.", "surname": "Bennett", "position": "Assistant Colonial Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "M. A. Potts", "canonical_name": "Potts, M. A.", "given_names": "M. A.", "surname": "Potts", "position": "Chief Clerk and Cashier", "department": "Treasury - Sierra Leone", "salary_min": 200, "salary_max": 200, "allowances": "50l. personal"},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "2nd Clerk", "department": "Treasury - Sierra Leone", "salary_min": 160, "salary_max": 160},
    {"name": "J. J. Wellington", "canonical_name": "Wellington, J. J.", "given_names": "J. J.", "surname": "Wellington", "position": "3rd Clerk", "department": "Treasury - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "R. A. Smith", "canonical_name": "Smith, R. A.", "given_names": "R. A.", "surname": "Smith", "position": "4th Clerk", "department": "Treasury - Sierra Leone", "salary_min": 55, "salary_max": 55},
    {"name": "J. Edwin", "canonical_name": "Edwin, J.", "given_names": "J.", "surname": "Edwin", "position": "5th Clerk", "department": "Treasury - Sierra Leone", "salary_min": 42, "salary_max": 42}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
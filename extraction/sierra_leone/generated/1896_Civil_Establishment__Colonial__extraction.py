"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "F. Cardew", "canonical_name": "Cardew, F.", "given_names": "F.", "surname": "Cardew", "position": "Governor, Commander-in-Chief; and Vice-Admiral", "department": "Civil Establishment - Sierra Leone", "salary_min": 2000, "salary_max": 2000, "allowances": "500l. allowances", "honors": ["C.M.G."], "military_rank": "Colonel"},
    {"name": "Jacob W. Lewis", "canonical_name": "Lewis, Jacob W.", "given_names": "Jacob W.", "surname": "Lewis", "position": "Governor’s Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 180, "salary_max": 180},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "Second Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 60, "salary_max": 80, "qualifications": ["B.A."]},
    {"name": "J. O. Gore", "canonical_name": "Gore, J. O.", "given_names": "J. O.", "surname": "Gore", "position": "Colonial Secretary", "department": "Colonial Secretary’s Department - Sierra Leone", "salary_min": 710, "salary_max": 800, "military_rank": "Lt.-Col."},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary’s Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. E. Dawson", "canonical_name": "Dawson, J. E.", "given_names": "J. E.", "surname": "Dawson", "position": "Chief Clerk", "department": "Colonial Secretary’s Department - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "2nd Clerk", "department": "Colonial Secretary’s Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. W. Paris", "canonical_name": "Paris, J. W.", "given_names": "J. W.", "surname": "Paris", "position": "3rd Clerk", "department": "Colonial Secretary’s Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "C. George", "canonical_name": "George, C.", "given_names": "C.", "surname": "George", "position": "4th Clerk", "department": "Colonial Secretary’s Department - Sierra Leone", "salary_min": 55, "salary_max": 55},
    {"name": "J. T. Smith", "canonical_name": "Smith, J. T.", "given_names": "J. T.", "surname": "Smith", "position": "5th Clerk", "department": "Colonial Secretary’s Department - Sierra Leone", "salary_min": 45, "salary_max": 45},
    {"name": "Bruce Faulkner", "canonical_name": "Faulkner, Bruce", "given_names": "Bruce", "surname": "Faulkner", "position": "6th Clerk", "department": "Colonial Secretary’s Department - Sierra Leone", "salary_min": 35, "salary_max": 35},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "7th Clerk", "department": "Colonial Secretary’s Department - Sierra Leone", "salary_min": 24, "salary_max": 24},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
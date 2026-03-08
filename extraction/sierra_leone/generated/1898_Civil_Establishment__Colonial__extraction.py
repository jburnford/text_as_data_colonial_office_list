"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "F. Cardew", "canonical_name": "Cardew, F.", "given_names": "F.", "surname": "Cardew", "position": "Governor, Commander-in-Chief, and Vice-Admiral", "department": "Civil Establishment - Sierra Leone", "salary_min": 2000, "salary_max": 2000, "allowances": "500l. allowances", "honors": ["K.C.M.G."], "military_rank": "Colonel"},
    {"name": "J. F. N. Price", "canonical_name": "Price, J. F. N.", "given_names": "J. F. N.", "surname": "Price", "position": "Private Secretary and A.D.C.", "department": "Civil Establishment - Sierra Leone", "military_rank": "Lt."},
    {"name": "Jacob W. Lewis", "canonical_name": "Lewis, Jacob W.", "given_names": "Jacob W.", "surname": "Lewis", "position": "Governor's Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 180, "salary_max": 180},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "Second Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 60, "salary_max": 80, "qualifications": ["B.A."]},
    {"name": "J. C. Gore", "canonical_name": "Gore, J. C.", "given_names": "J. C.", "surname": "Gore", "position": "Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 710, "salary_max": 800, "military_rank": "Lt.-Col."},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Chief Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "A. W. Nylander", "canonical_name": "Nylander, A. W.", "given_names": "A. W.", "surname": "Nylander", "position": "1st Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "2nd Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "C. George", "canonical_name": "George, C.", "given_names": "C.", "surname": "George", "position": "3rd Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 70, "salary_max": 85},
    {"name": "J. T. Smith", "canonical_name": "Smith, J. T.", "given_names": "J. T.", "surname": "Smith", "position": "4th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 55, "salary_max": 70},
    {"name": "Bruce Faulkner", "canonical_name": "Faulkner, Bruce", "given_names": "Bruce", "surname": "Faulkner", "position": "5th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 45, "salary_max": 55},
    {"name": "J. E. Taylor", "canonical_name": "Taylor, J. E.", "given_names": "J. E.", "surname": "Taylor", "position": "6th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "A. Merriman-Labor", "canonical_name": "Merriman-Labor, A.", "given_names": "A.", "surname": "Merriman-Labor", "position": "7th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 24, "salary_max": 30},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
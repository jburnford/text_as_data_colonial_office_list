"""
Sierra Leone Colonial Office List 1900 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1900

OFFICIALS = [
    {"name": "F. Cardew", "canonical_name": "Cardew, F.", "given_names": "F.", "surname": "Cardew", "position": "Governor, Commander-in-Chief, and Vice-Admiral", "department": "Civil Establishment - Sierra Leone", "salary_min": 2000, "salary_max": 2000, "allowances": "500l. allowances", "honors": ["K.C.M.G."], "military_rank": "Colonel"},
    {"name": "C. O. Ibbetson", "canonical_name": "Ibbetson, C. O.", "given_names": "C. O.", "surname": "Ibbetson", "position": "Private Secretary and A.D.C.", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150, "military_rank": "Capt."},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Governor's Confidential Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 100, "salary_max": 180},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "First Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"position": "Second Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "J. C. Gore", "canonical_name": "Gore, J. C.", "given_names": "J. C.", "surname": "Gore", "position": "Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 650, "salary_max": 800, "military_rank": "Lt.-Col."},
    {"name": "T. F. Meagher", "canonical_name": "Meagher, T. F.", "given_names": "T. F.", "surname": "Meagher", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 350, "salary_max": 400, "allowances": "Rent 40l."},
    {"name": "A. W. Nylander", "canonical_name": "Nylander, A. W.", "given_names": "A. W.", "surname": "Nylander", "position": "Chief Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"position": "1st Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 150, "salary_max": 190},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "2nd Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "C. George", "canonical_name": "George, C.", "given_names": "C.", "surname": "George", "position": "3rd Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 70, "salary_max": 85},
    {"name": "J. T. Smith", "canonical_name": "Smith, J. T.", "given_names": "J. T.", "surname": "Smith", "position": "4th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 55, "salary_max": 70},
    {"name": "Bruce Faulkner", "canonical_name": "Faulkner, Bruce", "given_names": "Bruce", "surname": "Faulkner", "position": "5th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 45, "salary_max": 55},
    {"name": "A. B. C. Merriman-Labor", "canonical_name": "Merriman-Labor, A. B. C.", "given_names": "A. B. C.", "surname": "Merriman-Labor", "position": "6th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"position": "7th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 24, "salary_max": 30},
    {"name": "Mohammed Sanusi", "canonical_name": "Sanusi, Mohammed", "given_names": "Mohammed", "surname": "Sanusi", "position": "Arabic Writer", "department": "Native Affairs Branch. - Sierra Leone", "salary_min": 70, "salary_max": 70},
    {"position": "Interpreter", "department": "Native Affairs Branch. - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"position": "Interpreter", "department": "Native Affairs Branch. - Sierra Leone", "salary_min": 36, "salary_max": 48},
    {"position": "Clerk", "department": "Native Affairs Branch. - Sierra Leone", "salary_min": 40, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
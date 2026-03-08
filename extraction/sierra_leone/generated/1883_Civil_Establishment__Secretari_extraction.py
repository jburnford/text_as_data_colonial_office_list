"""
Sierra Leone Colonial Office List 1883 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1883

OFFICIALS = [
    {"name": "Arthur Elibank Havelock", "canonical_name": "Havelock, Arthur Elibank", "given_names": "Arthur Elibank", "surname": "Havelock", "position": "Governor, Commander-in-Chief, and Vice-Admiral of W. Africa Settlements", "department": "Civil Establishment - Sierra Leone", "salary_min": 2000, "salary_max": 2000, "allowances": "500l. allowances", "honors": ["C.M.G."]},
    {"name": "H. M. Jackson", "canonical_name": "Jackson, H. M.", "given_names": "H. M.", "surname": "Jackson", "position": "Aide-de-Camp", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150, "military_rank": "Capt."},
    {"name": "J. W. Lewis", "canonical_name": "Lewis, J. W.", "given_names": "J. W.", "surname": "Lewis", "position": "Governor's Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 160, "salary_max": 160},
    {"name": "T. Risely Griffith", "canonical_name": "Griffith, T. Risely", "given_names": "T. Risely", "surname": "Griffith", "position": "Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "H. F. Richmond", "canonical_name": "Richmond, H. F.", "given_names": "H. F.", "surname": "Richmond", "position": "Assisted Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 400, "salary_max": 400, "military_rank": "Captain"},
    {"name": "G. A. Banbury", "canonical_name": "Banbury, G. A.", "given_names": "G. A.", "surname": "Banbury", "position": "Assisted Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "W. M. Laborde", "canonical_name": "Laborde, W. M.", "given_names": "W. M.", "surname": "Laborde", "position": "Assisted Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "G. Y. Lagden", "canonical_name": "Lagden, G. Y.", "given_names": "G. Y.", "surname": "Lagden", "position": "Assisted Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "G. Metzger Macaulay", "canonical_name": "Macaulay, G. Metzger", "given_names": "G. Metzger", "surname": "Macaulay", "position": "Clerk", "department": "Secretarial Branch - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "J. E. Dawson", "canonical_name": "Dawson, J. E.", "given_names": "J. E.", "surname": "Dawson", "position": "Clerk", "department": "Secretarial Branch - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "M. D. Lake", "canonical_name": "Lake, M. D.", "given_names": "M. D.", "surname": "Lake", "position": "Clerk", "department": "Secretarial Branch - Sierra Leone", "salary_min": 70, "salary_max": 70},
    {"name": "M. A. Potts", "canonical_name": "Potts, M. A.", "given_names": "M. A.", "surname": "Potts", "position": "Clerk", "department": "Treasury Branch - Sierra Leone", "salary_min": 240, "salary_max": 240},
    {"name": "B. M. Brown", "canonical_name": "Brown, B. M.", "given_names": "B. M.", "surname": "Brown", "position": "Clerk", "department": "Treasury Branch - Sierra Leone", "salary_min": 140, "salary_max": 140},
    {"name": "J. J. Wellington", "canonical_name": "Wellington, J. J.", "given_names": "J. J.", "surname": "Wellington", "position": "Clerk", "department": "Treasury Branch - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "T. G. Lawson", "canonical_name": "Lawson, T. G.", "given_names": "T. G.", "surname": "Lawson", "position": "Government Interpreter", "department": "Aborigines Branch - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "Mohammed Sanusi", "canonical_name": "Sanusi, Mohammed", "given_names": "Mohammed", "surname": "Sanusi", "position": "Arabic Writer", "department": "Aborigines Branch - Sierra Leone", "salary_min": 60, "salary_max": 60}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
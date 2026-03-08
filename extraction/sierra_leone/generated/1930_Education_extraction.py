"""
Sierra Leone Colonial Office List 1930 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1930

OFFICIALS = [
    {"name": "H. S. Keigwin", "canonical_name": "Keigwin, H. S.", "given_names": "H. S.", "surname": "Keigwin", "position": "Director of Education", "department": "Education - Sierra Leone", "honors": ["M.B.E."], "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "H. Blackmore", "canonical_name": "Blackmore, H.", "given_names": "H.", "surname": "Blackmore", "position": "Deputy Director of Education and Chief Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 920, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "H. Michell", "canonical_name": "Michell, H.", "given_names": "H.", "surname": "Michell", "position": "Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "F. A. Lacey", "canonical_name": "Lacey, F. A.", "given_names": "F. A.", "surname": "Lacey", "position": "Vice-Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 920, "allowances": "with seniority allowance of 72l."},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Vice-Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 920, "allowances": "and seniority allowance of 72l. from 720l."},
    {"name": "H. E. T. Hodgson", "canonical_name": "Hodgson, H. E. T.", "given_names": "H. E. T.", "surname": "Hodgson", "position": "European Master, Bo School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Principal, Protectorate Central College", "department": "Education - Sierra Leone"},
    {"name": "P. J. Moss", "canonical_name": "Moss, P. J.", "given_names": "P. J.", "surname": "Moss", "position": "Organizer of Agriculture and Forestry, Protectorate Central College", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "J. Edminson", "canonical_name": "Edminson, J.", "given_names": "J.", "surname": "Edminson", "position": "Organizer of Industries, Protectorate Central College", "department": "Education - Sierra Leone", "salary_scale": "F"},
    {"name": "Miss K. B. Coops", "canonical_name": "Coops, K. B.", "given_names": "K. B.", "surname": "Coops", "position": "Organizer of Infant and Female Education", "department": "Education - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "C. A. E. Macaulay", "canonical_name": "Macaulay, C. A. E.", "given_names": "C. A. E.", "surname": "Macaulay", "position": "African Assistant Director of Education", "department": "Education - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "W. T. Thomas", "canonical_name": "Thomas, W. T.", "given_names": "W. T.", "surname": "Thomas", "position": "Inspectors of School Colony", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Supervising Teacher", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. G. Nicol", "canonical_name": "Nicol, W. G.", "given_names": "W. G.", "surname": "Nicol", "position": "Senior Master, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "C. E. Tuboku Metzger", "canonical_name": "Metzger, C. E. Tuboku", "given_names": "C. E.", "surname": "Metzger", "position": "Assistant Science and Technical Masters, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "S. Tuboku Metzger", "canonical_name": "Metzger, S. Tuboku", "given_names": "S.", "surname": "Metzger", "position": "Assistant Science and Technical Masters, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A.T. Sumner", "canonical_name": "Sumner, A.T.", "given_names": "A.T.", "surname": "Sumner", "position": "Vice-Principal, Protectorate Central College", "department": "Education - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "J. O. Wallace", "canonical_name": "Wallace, J. O.", "given_names": "J. O.", "surname": "Wallace", "position": "Inspector of Schools, Protectorate", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "S. M. Broderick", "canonical_name": "Broderick, S. M.", "given_names": "S. M.", "surname": "Broderick", "position": "Supervising Teacher, Protectorate Central College", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. P. King", "canonical_name": "King, A. P.", "given_names": "A. P.", "surname": "King", "position": "Chief Clerk", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "F. J. W. Hollist", "canonical_name": "Hollist, F. J. W.", "given_names": "F. J. W.", "surname": "Hollist", "position": "First Grade Clerk", "department": "Education - Sierra Leone", "salary_min": 210, "salary_max": 250},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
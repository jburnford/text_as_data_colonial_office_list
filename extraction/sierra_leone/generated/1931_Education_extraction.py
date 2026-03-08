"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "H. Blackmore", "canonical_name": "Blackmore, H.", "given_names": "H.", "surname": "Blackmore", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Director of Education and Chief Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "H. Michell", "canonical_name": "Michell, H.", "given_names": "H.", "surname": "Michell", "position": "Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "F. A. Lacey", "canonical_name": "Lacey, F. A.", "given_names": "F. A.", "surname": "Lacey", "position": "Vice-Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 920, "allowances": "seniority allowance of 72l."},
    {"name": "H. E. T. Hodgson", "canonical_name": "Hodgson, H. E. T.", "given_names": "H. E. T.", "surname": "Hodgson", "position": "Vice-Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 920, "allowances": "seniority allowance of 72L from 720L"},
    {"name": "C. P. Ellis", "canonical_name": "Ellis, C. P.", "given_names": "C. P.", "surname": "Ellis", "position": "European Muster, Bo School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Principal, Protectorate Central College", "department": "Education - Sierra Leone"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Organizer of Agriculture and Forestry, Protectorate Central College", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Organizer of Industries, Protectorate Central College", "department": "Education - Sierra Leone", "salary_scale": "F"},
    {"name": "H. O. Lipscombe", "canonical_name": "Lipscombe, H. O.", "given_names": "H. O.", "surname": "Lipscombe", "position": "Supervisor of Schools", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "Miss K. B. Coope", "canonical_name": "Coope, K. B.", "given_names": "K. B.", "surname": "Coope", "position": "Supervising Mistress", "department": "Education - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "C. A. E. Macaulay", "canonical_name": "Macaulay, C. A. E.", "given_names": "C. A. E.", "surname": "Macaulay", "position": "African Assistant Director of Education", "department": "Education - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "W. T. Thomas", "canonical_name": "Thomas, W. T.", "given_names": "W. T.", "surname": "Thomas", "position": "Inspector of School Colony", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Supervising Teacher", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. G. Nicol", "canonical_name": "Nicol, W. G.", "given_names": "W. G.", "surname": "Nicol", "position": "Senior Master, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "C. E. Tuboku Metzger", "canonical_name": "Metzger, C. E. Tuboku", "given_names": "C. E.", "surname": "Metzger", "position": "Assistant Science and Technical Masters, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "S. Tuboku Metzger", "canonical_name": "Metzger, S. Tuboku", "given_names": "S.", "surname": "Metzger", "position": "Assistant Science and Technical Masters, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. T. Sumner", "canonical_name": "Sumner, A. T.", "given_names": "A. T.", "surname": "Sumner", "position": "Vice-Principal, Protectorate Central College", "department": "Education - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "J. O. Wallace", "canonical_name": "Wallace, J. O.", "given_names": "J. O.", "surname": "Wallace", "position": "Inspector of Schools, Protectorate", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "S. M. Broderick", "canonical_name": "Broderick, S. M.", "given_names": "S. M.", "surname": "Broderick", "position": "Supervising Teachers, Protectorate Central College", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "E. W. Turner", "canonical_name": "Turner, E. W.", "given_names": "E. W.", "surname": "Turner", "position": "Supervising Teachers, Protectorate Central College", "department": "Education - Sierra Leone", "salary_min": 210, "salary_max": 250},
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
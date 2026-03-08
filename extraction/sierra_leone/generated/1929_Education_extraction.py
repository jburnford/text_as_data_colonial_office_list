"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "H. S. Keigwin", "canonical_name": "Keigwin, H. S.", "given_names": "H. S.", "surname": "Keigwin", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["M.B.E."]},
    {"name": "H. Blackmore", "canonical_name": "Blackmore, H.", "given_names": "H.", "surname": "Blackmore", "position": "Deputy Director of Education and Chief Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 920, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "H. Michell", "canonical_name": "Michell, H.", "given_names": "H.", "surname": "Michell", "position": "Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "V. de Lisle", "canonical_name": "de Lisle, V.", "given_names": "V.", "surname": "de Lisle", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "F. A. Lacey", "canonical_name": "Lacey, F. A.", "given_names": "F. A.", "surname": "Lacey", "position": "Vice-Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 920, "allowances": "seniority allowance of 72l."},
    {"name": "K. J. Ritchie", "canonical_name": "Ritchie, K. J.", "given_names": "K. J.", "surname": "Ritchie", "position": "Vice-Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 920, "allowances": "seniority allowance of 72l. from 720l."},
    {"name": "H. E. T. Hodgson", "canonical_name": "Hodgson, H. E. T.", "given_names": "H. E. T.", "surname": "Hodgson", "position": "European Master, Bo School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "Miss K. B. Coops", "canonical_name": "Coops, K. B.", "given_names": "K. B.", "surname": "Coops", "position": "Organizer of Infant and Female Education", "department": "Education - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "C. A. E. Macaulay", "canonical_name": "Macaulay, C. A. E.", "given_names": "C. A. E.", "surname": "Macaulay", "position": "African Assistant Director of Education", "department": "Education - Sierra Leone", "salary_min": 360, "salary_max": 600},
    {"name": "J. O. Wallace", "canonical_name": "Wallace, J. O.", "given_names": "J. O.", "surname": "Wallace", "position": "Inspectors of Schools", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. T. Thomas", "canonical_name": "Thomas, W. T.", "given_names": "W. T.", "surname": "Thomas", "position": "Inspectors of Schools", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. E. D. Campbell", "canonical_name": "Campbell, W. E. D.", "given_names": "W. E. D.", "surname": "Campbell", "position": "Supervising Teacher", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. G. Nicol", "canonical_name": "Nicol, W. G.", "given_names": "W. G.", "surname": "Nicol", "position": "Senior Master, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. T. Sumner", "canonical_name": "Sumner, A. T.", "given_names": "A. T.", "surname": "Sumner", "position": "Senior Master, Agricultural Training College", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. P. King", "canonical_name": "King, A. P.", "given_names": "A. P.", "surname": "King", "position": "Chief Clerk", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
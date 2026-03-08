"""
Sierra Leone Colonial Office List 1925 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1925

OFFICIALS = [
    {"name": "F. C. Marriott", "canonical_name": "Marriott, F. C.", "given_names": "F. C.", "surname": "Marriott", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "H. Blackmore", "canonical_name": "Blackmore, H.", "given_names": "H.", "surname": "Blackmore", "position": "Chief Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920},
    {"name": "H. Evans", "canonical_name": "Evans, H.", "given_names": "H.", "surname": "Evans", "position": "Principal, Model School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "V. de Lisle", "canonical_name": "Lisle, V. de", "given_names": "V.", "surname": "Lisle", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "H. Michell", "canonical_name": "Michell, H.", "given_names": "H.", "surname": "Michell", "position": "Principal, Agricultural Training College", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Vice-Principal, Model School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Vice-Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 920, "allowances": "seniority allowance of 72l. from 720l."},
    {"name": "T. Sweet-Escott", "canonical_name": "Sweet-Escott, T.", "given_names": "T.", "surname": "Sweet-Escott", "position": "European Teacher, Bo School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "J. C. Wratislaw", "canonical_name": "Wratislaw, J. C.", "given_names": "J. C.", "surname": "Wratislaw", "position": "European Teacher, Bo School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "C. A. E. Macaulay", "canonical_name": "Macaulay, C. A. E.", "given_names": "C. A. E.", "surname": "Macaulay", "position": "Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "J. O. Wallace", "canonical_name": "Wallace, J. O.", "given_names": "J. O.", "surname": "Wallace", "position": "Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "W. T. Thomas", "canonical_name": "Thomas, W. T.", "given_names": "W. T.", "surname": "Thomas", "position": "Senior Tutor, Model School", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. T. Sumner", "canonical_name": "Sumner, A. T.", "given_names": "A. T.", "surname": "Sumner", "position": "Senior Tutor, Agricultural Training College", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
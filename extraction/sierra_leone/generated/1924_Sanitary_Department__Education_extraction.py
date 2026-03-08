"""
Sierra Leone Colonial Office List 1924 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1924

OFFICIALS = [
    {"name": "H. H. O'Hara May", "canonical_name": "May, H. H. O'Hara", "given_names": "H. H.", "surname": "May", "position": "Deputy Director, Sanitary Services", "department": "Sanitary Department - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "duty_allowance": 260},
    {"name": "W. H. Peacock", "canonical_name": "Peacock, W. H.", "given_names": "W. H.", "surname": "Peacock", "position": "Senior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 1050, "salary_max": 1200, "duty_allowance": 210},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Medical Officer of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 800, "salary_max": 960, "allowances": "100l. seniority allowance, Staff Pay at 150l. p.a."},
    {"name": "D. Bowen", "canonical_name": "Bowen, D.", "given_names": "D.", "surname": "Bowen", "position": "Superintendent, Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_scale": "F"},
    {"name": "G. V. Hird", "canonical_name": "Hird, G. V.", "given_names": "G. V.", "surname": "Hird", "position": "Superintendent, Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_scale": "F"},
    {"name": "F. C. Marriott", "canonical_name": "Marriott, F. C.", "given_names": "F. C.", "surname": "Marriott", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "H. Evans", "canonical_name": "Evans, H.", "given_names": "H.", "surname": "Evans", "position": "Principal, Model School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "V. de Lisle", "canonical_name": "Lisle, V. de", "given_names": "V.", "surname": "Lisle", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "H. Michell", "canonical_name": "Michell, H.", "given_names": "H.", "surname": "Michell", "position": "Principal, Agricultural Training College", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "E. D. Morgan", "canonical_name": "Morgan, E. D.", "given_names": "E. D.", "surname": "Morgan", "position": "Vice-Principal, Model School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "F. G. M. Beck", "canonical_name": "Beck, F. G. M.", "given_names": "F. G. M.", "surname": "Beck", "position": "Vice-Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 920, "allowances": "seniority allowance of 72l. from 720l."},
    {"name": "T. Sweet-Escott", "canonical_name": "Sweet-Escott, T.", "given_names": "T.", "surname": "Sweet-Escott", "position": "European Teachers, Bo School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "J. C. Wratislaw", "canonical_name": "Wratislaw, J. C.", "given_names": "J. C.", "surname": "Wratislaw", "position": "European Teachers, Bo School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "C. A. E. Macaulay", "canonical_name": "Macaulay, C. A. E.", "given_names": "C. A. E.", "surname": "Macaulay", "position": "Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "J. O. Wallace", "canonical_name": "Wallace, J. O.", "given_names": "J. O.", "surname": "Wallace", "position": "Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "W. T. Thomas", "canonical_name": "Thomas, W. T.", "given_names": "W. T.", "surname": "Thomas", "position": "Senior Tutor, Model School", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. T. Sumner", "canonical_name": "Sumner, A. T.", "given_names": "A. T.", "surname": "Sumner", "position": "Senior Tutor, Agricultural Training College", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "H. Deen", "canonical_name": "Deen, H.", "given_names": "H.", "surname": "Deen", "position": "First Grade Clerk", "department": "Education - Sierra Leone", "salary_min": 210, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
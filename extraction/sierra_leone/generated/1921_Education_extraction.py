"""
Sierra Leone Colonial Office List 1921 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1921

OFFICIALS = [
    {"name": "R. F. Honter", "canonical_name": "Honter, R. F.", "given_names": "R. F.", "surname": "Honter", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "H. Evans", "canonical_name": "Evans, H.", "given_names": "H.", "surname": "Evans", "position": "Principal, Model School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920},
    {"name": "V. de Lisle", "canonical_name": "Lisle, V. de", "given_names": "V.", "surname": "Lisle", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920},
    {"name": "H. Michell", "canonical_name": "Michell, H.", "given_names": "H.", "surname": "Michell", "position": "Principal, Agricultural Training College", "department": "Education - Sierra Leone", "salary_min": 720, "salary_max": 720},
    {"name": "F. G. M. Beck", "canonical_name": "Beck, F. G. M.", "given_names": "F. G. M.", "surname": "Beck", "position": "Vice-Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "E. D. Morgan", "canonical_name": "Morgan, E. D.", "given_names": "E. D.", "surname": "Morgan", "position": "European Teacher, Bo School", "department": "Education - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "T. Sweet-Escott", "canonical_name": "Sweet-Escott, T.", "given_names": "T.", "surname": "Sweet-Escott", "position": "European Teacher, Bo School", "department": "Education - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "M. Mavrogordato", "canonical_name": "Mavrogordato, M.", "given_names": "M.", "surname": "Mavrogordato", "position": "Instructor, Model School", "department": "Education - Sierra Leone", "salary_min": 410, "salary_max": 500},
    {"name": "C. A. E. Macauley", "canonical_name": "Macauley, C. A. E.", "given_names": "C. A. E.", "surname": "Macauley", "position": "Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "A. E. Sumner", "canonical_name": "Sumner, A. E.", "given_names": "A. E.", "surname": "Sumner", "position": "Senior Tutor, Agricultural Training College", "department": "Education - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "H. Deen", "canonical_name": "Deen, H.", "given_names": "H.", "surname": "Deen", "position": "First Grade Clerk", "department": "Education - Sierra Leone", "salary_min": 190, "salary_max": 240}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
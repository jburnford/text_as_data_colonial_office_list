"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "R. F. Hunter", "canonical_name": "Hunter, R. F.", "given_names": "R. F.", "surname": "Hunter", "position": "Director of Education", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "V. F. de Lisle", "canonical_name": "Lisle, V. F. de", "given_names": "V. F.", "surname": "Lisle", "position": "Principal, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "H. Evans", "canonical_name": "Evans, H.", "given_names": "H.", "surname": "Evans", "position": "Principal, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 450, "salary_max": 500, "duty_allowance": 90},
    {"name": "H. Michell", "canonical_name": "Michell, H.", "given_names": "H.", "surname": "Michell", "position": "Principal, Njala School", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Vice-Principal, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Vice-Principal, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "E. D. Morgan", "canonical_name": "Morgan, E. D.", "given_names": "E. D.", "surname": "Morgan", "position": "European Teachers, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "European Teachers, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 500},
    {"name": "Mrs. A. S. Mavrogordato", "canonical_name": "Mavrogordato, A. S.", "given_names": "A. S.", "surname": "Mavrogordato", "position": "Instructress, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "S. J. Taylor", "canonical_name": "Taylor, S. J.", "given_names": "S. J.", "surname": "Taylor", "position": "Inspectors of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "C. A. E. Macauley", "canonical_name": "Macauley, C. A. E.", "given_names": "C. A. E.", "surname": "Macauley", "position": "Inspectors of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "W. T. Thomas", "canonical_name": "Thomas, W. T.", "given_names": "W. T.", "surname": "Thomas", "position": "Senior Tutor, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "M. D. Lucas", "canonical_name": "Lucas, M. D.", "given_names": "M. D.", "surname": "Lucas", "position": "Senior Assistant Tutors, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "W. E. D. Campbell", "canonical_name": "Campbell, W. E. D.", "given_names": "W. E. D.", "surname": "Campbell", "position": "Senior Assistant Tutors, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "Miss M. Williams", "canonical_name": "Williams, M.", "given_names": "M.", "surname": "Williams", "position": "First Female Teacher, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "H. Deen", "canonical_name": "Deen, H.", "given_names": "H.", "surname": "Deen", "position": "First Grade Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "A. E. Lavarse", "canonical_name": "Lavarse, A. E.", "given_names": "A. E.", "surname": "Lavarse", "position": "Third Grade Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1915 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1915

OFFICIALS = [
    {"name": "R. F. Honter", "canonical_name": "Honter, R. F.", "given_names": "R. F.", "surname": "Honter", "position": "Director of Education", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "T. Smith", "canonical_name": "Smith, T.", "given_names": "T.", "surname": "Smith", "position": "Principal, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "R. Lean", "canonical_name": "Lean, R.", "given_names": "R.", "surname": "Lean", "position": "Principal, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 450, "salary_max": 500, "duty_allowance": 90},
    {"name": "V. F. de Lisle", "canonical_name": "Lisle, V. F. de", "given_names": "V. F.", "surname": "Lisle", "position": "Vice-Principal, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "W. J. Holloway", "canonical_name": "Holloway, W. J.", "given_names": "W. J.", "surname": "Holloway", "position": "Vice-Principal, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "H. Mitchell", "canonical_name": "Mitchell, H.", "given_names": "H.", "surname": "Mitchell", "position": "European Teacher, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 500},
    {"name": "Miss M. M. McAllister", "canonical_name": "McAllister, M. M.", "given_names": "M. M.", "surname": "McAllister", "position": "Instructor, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Chief Inspector", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "70l. personal"},
    {"name": "S. J. Taylor", "canonical_name": "Taylor, S. J.", "given_names": "S. J.", "surname": "Taylor", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "W. T. Thomas", "canonical_name": "Thomas, W. T.", "given_names": "W. T.", "surname": "Thomas", "position": "Senior Tutor, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "J. F. Doherty", "canonical_name": "Doherty, J. F.", "given_names": "J. F.", "surname": "Doherty", "position": "Senior Assistant Tutor, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "M. D. Lucas", "canonical_name": "Lucas, M. D.", "given_names": "M. D.", "surname": "Lucas", "position": "Senior Assistant Tutor, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "Miss M. Williams", "canonical_name": "Williams, M.", "given_names": "M.", "surname": "Williams", "position": "First Female Teacher, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "H. Deen", "canonical_name": "Deen, H.", "given_names": "H.", "surname": "Deen", "position": "Second Grade Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "A. E. Laverse", "canonical_name": "Laverse, A. E.", "given_names": "A. E.", "surname": "Laverse", "position": "Third Grade Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "F. J. W. Hollist", "canonical_name": "Hollist, F. J. W.", "given_names": "F. J. W.", "surname": "Hollist", "position": "Fourth Grade Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 70, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
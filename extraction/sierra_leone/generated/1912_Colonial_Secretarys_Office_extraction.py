"""
Sierra Leone Colonial Office List 1912 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1912

OFFICIALS = [
    {"name": "G. B. Haddon Smith", "canonical_name": "Smith, G. B. Haddon", "given_names": "G. B.", "surname": "Smith", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 800, "salary_max": 1000, "duty_allowance": 160, "honors": ["C.M.G."]},
    {"name": "E. E. Evelyn", "canonical_name": "Evelyn, E. E.", "given_names": "E. E.", "surname": "Evelyn", "position": "Senior Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "A. Farrar", "canonical_name": "Farrar, A.", "given_names": "A.", "surname": "Farrar", "position": "Asst. Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "R. W. H. Wilkinson", "canonical_name": "Wilkinson, R. W. H.", "given_names": "R. W. H.", "surname": "Wilkinson", "position": "Asst. Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "N. C. Hollins", "canonical_name": "Hollins, N. C.", "given_names": "N. C.", "surname": "Hollins", "position": "Asst. Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "D. W. Carrol", "canonical_name": "Carrol, D. W.", "given_names": "D. W.", "surname": "Carrol", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "J. H. C. Smart", "canonical_name": "Smart, J. H. C.", "given_names": "J. H. C.", "surname": "Smart", "position": "1st Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 160},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "2nd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 120, "salary_max": 140},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "3rd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 120, "salary_max": 140},
    {"name": "I. F. T. George", "canonical_name": "George, I. F. T.", "given_names": "I. F. T.", "surname": "George", "position": "4th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "5th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": "U. W.", "surname": "Coker", "position": "6th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "C. J. Gilpin", "canonical_name": "Gilpin, C. J.", "given_names": "C. J.", "surname": "Gilpin", "position": "Assistant Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 100, "salary_max": 150, "allowances": "25l. personal"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
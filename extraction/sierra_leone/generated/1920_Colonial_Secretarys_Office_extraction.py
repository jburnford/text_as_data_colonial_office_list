"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "A. C. Hollis", "canonical_name": "Hollis, A. C.", "given_names": "A. C.", "surname": "Hollis", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "honors": ["C.M.G."]},
    {"name": "E. E. Evelyn", "canonical_name": "Evelyn, E. E.", "given_names": "E. E.", "surname": "Evelyn", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100, "honors": ["I.S.O."]},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "R. de C. Baldwin", "canonical_name": "Baldwin, R. de C.", "given_names": "R. de C.", "surname": "Baldwin", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "J. de Hart", "canonical_name": "Hart, J. de", "given_names": "J. de", "surname": "Hart", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 300, "salary_max": 400, "duty_allowance": 80},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 300, "salary_max": 400, "duty_allowance": 80},
    {"name": "D. W. Carrol", "canonical_name": "Carrol, D. W.", "given_names": "D. W.", "surname": "Carrol", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "J. H. Cheetham Smart", "canonical_name": "Smart, J. H. Cheetham", "given_names": "J. H. Cheetham", "surname": "Smart", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "I. F. T. George", "canonical_name": "George, I. F. T.", "given_names": "I. F. T.", "surname": "George", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": "U. W.", "surname": "Coker", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "A. E. Scott", "canonical_name": "Scott, A. E.", "given_names": "A. E.", "surname": "Scott", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
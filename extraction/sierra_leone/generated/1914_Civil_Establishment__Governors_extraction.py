"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "Sir Edward Marsh Merewether", "canonical_name": "Merewether, Edward Marsh", "given_names": "Edward Marsh", "surname": "Merewether", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 1000, "honors": ["K.C.V.O.", "C.M.G."]},
    {"name": "A. Ross Hume", "canonical_name": "Hume, A. Ross", "given_names": "A. Ross", "surname": "Hume", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 300, "salary_max": 300, "military_rank": "Lieutenant"},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Chief Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "T. A. Thompson", "canonical_name": "Thompson, T. A.", "given_names": "T. A.", "surname": "Thompson", "position": "Second Grade Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "A. C. Hollis", "canonical_name": "Hollis, A. C.", "given_names": "A. C.", "surname": "Hollis", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "honors": ["C.M.G."]},
    {"name": "E. E. Evelyn", "canonical_name": "Evelyn, E. E.", "given_names": "E. E.", "surname": "Evelyn", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100, "honors": ["I.S.O."]},
    {"name": "J. de Hart", "canonical_name": "Hart, J. de", "given_names": "J. de", "surname": "Hart", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "D. W. Carrol", "canonical_name": "Carrol, D. W.", "given_names": "D. W.", "surname": "Carrol", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "J. H. Cheetham Smart", "canonical_name": "Smart, J. H. Cheetham", "given_names": "J. H. Cheetham", "surname": "Smart", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "I. F. T. George", "canonical_name": "George, I. F. T.", "given_names": "I. F. T.", "surname": "George", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": "U. W.", "surname": "Coker", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": "M. B.", "surname": "Reader", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "Third Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 130}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
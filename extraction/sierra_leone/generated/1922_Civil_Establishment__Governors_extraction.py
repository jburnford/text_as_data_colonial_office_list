"""
Sierra Leone Colonial Office List 1922 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1922

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone"},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Clerk of Legislative Council", "department": "Governor's Office - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "First Grade Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1350, "salary_max": 1350, "honors": ["C.M.G."], "qualifications": ["Dr."], "duty_allowance": 270},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "D. C. Thompson", "canonical_name": "Thompson, D. C.", "given_names": "D. C.", "surname": "Thompson", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 840, "military_rank": "Capt."},
    {"name": "R. E. Page", "canonical_name": "Page, R. E.", "given_names": "R. E.", "surname": "Page", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "D. W. Carrol", "canonical_name": "Carrol, D. W.", "given_names": "D. W.", "surname": "Carrol", "position": "Chief Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "J. H. Cheetah Smart", "canonical_name": "Smart, J. H. Cheetah", "given_names": "J. H.", "surname": "Smart", "position": "Chief Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "First Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "I. F. T. George", "canonical_name": "George, I. F. T.", "given_names": "I. F. T.", "surname": "George", "position": "First Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "A. E. Scott", "canonical_name": "Scott, A. E.", "given_names": "A. E.", "surname": "Scott", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "T. D. Hewer", "canonical_name": "Hewer, T. D.", "given_names": "T. D.", "surname": "Hewer", "position": "Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 600, "salary_max": 600},
    {"name": "J. McCulloch", "canonical_name": "McCulloch, J.", "given_names": "J.", "surname": "McCulloch", "position": "Assistant Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "J. N. L. Metzger", "canonical_name": "Metzger, J. N. L.", "given_names": "J. N. L.", "surname": "Metzger", "position": "Proof Reader", "department": "Printing Branch - Sierra Leone", "salary_min": 96, "salary_max": 132},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Senior Compositor", "department": "Printing Branch - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "J. E. Bailey", "canonical_name": "Bailey, J. E.", "given_names": "J. E.", "surname": "Bailey", "position": "Book Binder", "department": "Printing Branch - Sierra Leone", "salary_min": 96, "salary_max": 132}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
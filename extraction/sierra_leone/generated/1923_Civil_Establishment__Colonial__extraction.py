"""
Sierra Leone Colonial Office List 1923 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1923

OFFICIALS = [
    {"name": "A. R. Slater", "canonical_name": "Slater, A. R.", "given_names": "A. R.", "surname": "Slater", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "honors": ["C.M.G.", "C.B.E."], "duty_allowance": 1000},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Clerk of Legislative Council", "department": "Governor's Office - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "First Grade Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. T. Furley", "canonical_name": "Furley, J. T.", "given_names": "J. T.", "surname": "Furley", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "honors": ["C.M.G.", "O.B.E."], "duty_allowance": 280},
    {"name": "G. C. Du Boulay", "canonical_name": "Du Boulay, G. C.", "given_names": "G. C.", "surname": "Du Boulay", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 960},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 960},
    {"name": "D. C. Thompson", "canonical_name": "Thompson, D. C.", "given_names": "D. C.", "surname": "Thompson", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 960, "military_rank": "Captain"},
    {"name": "D. W. Carrol", "canonical_name": "Carrol, D. W.", "given_names": "D. W.", "surname": "Carrol", "position": "Staff Superintendent", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "J. H. Cheetham Smart", "canonical_name": "Smart, J. H. Cheetham", "given_names": "J. H. Cheetham", "surname": "Smart", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "First Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "I. F. T. George", "canonical_name": "George, I. F. T.", "given_names": "I. F. T.", "surname": "George", "position": "First Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "First Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "A. E. Scott", "canonical_name": "Scott, A. E.", "given_names": "A. E.", "surname": "Scott", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "H. B. Marke", "canonical_name": "Marke, H. B.", "given_names": "H. B.", "surname": "Marke", "position": "Second Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "T. D. Hewer", "canonical_name": "Hewer, T. D.", "given_names": "T. D.", "surname": "Hewer", "position": "Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 600, "salary_max": 600},
    {"name": "J. McCulloch", "canonical_name": "McCulloch, J.", "given_names": "J.", "surname": "McCulloch", "position": "Assistant Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "G. B. Cassell", "canonical_name": "Cassell, G. B.", "given_names": "G. B.", "surname": "Cassell", "position": "African Assistant Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 140, "salary_max": 180}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1927 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1927

OFFICIALS = [
    {"name": "Sir A. R. Slater", "canonical_name": "Slater, A. R.", "given_names": "A. R.", "surname": "Slater", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G.", "C.B.E."]},
    {"name": "V. Basevi", "canonical_name": "Basevi, V.", "given_names": "V.", "surname": "Basevi", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "First Grade Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "H. C. Luke", "canonical_name": "Luke, H. C.", "given_names": "H. C.", "surname": "Luke", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280, "honors": ["C.M.G."]},
    {"name": "Capt. C. E. Cookson", "canonical_name": "Cookson, C. E.", "given_names": "C. E.", "surname": "Cookson", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 98, "military_rank": "Captain"},
    {"name": "Capt. J. E. Benham", "canonical_name": "Benham, J. E.", "given_names": "J. E.", "surname": "Benham", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "military_rank": "Captain"},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "honors": ["M.B.E."]},
    {"name": "D. C. Thompson", "canonical_name": "Thompson, D. C.", "given_names": "D. C.", "surname": "Thompson", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "D. B. Drummond", "canonical_name": "Drummond, D. B.", "given_names": "D. B.", "surname": "Drummond", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. H. Cheetham", "canonical_name": "Cheetham, J. H.", "given_names": "J. H.", "surname": "Cheetham", "position": "African Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "T. A. Thompson", "canonical_name": "Thompson, T. A.", "given_names": "T. A.", "surname": "Thompson", "position": "Staff Superintendent", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "I. F. T. George", "canonical_name": "George, I. F. T.", "given_names": "I. F. T.", "surname": "George", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "First Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 260},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "First Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 260},
    {"name": "A. E. Scott", "canonical_name": "Scott, A. E.", "given_names": "A. E.", "surname": "Scott", "position": "First Grade Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 260},
    {"name": "H. B. Marke", "canonical_name": "Marke, H. B.", "given_names": "H. B.", "surname": "Marke", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "T. D. Hewer", "canonical_name": "Hewer, T. D.", "given_names": "T. D.", "surname": "Hewer", "position": "Government Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 600, "salary_max": 720, "duty_allowance": 72},
    {"name": "J. McCulloch", "canonical_name": "McCulloch, J.", "given_names": "J.", "surname": "McCulloch", "position": "Assistant Government Printer", "department": "Printing Branch - Sierra Leone", "salary_scale": "F"},
    {"name": "G. B. Cassell", "canonical_name": "Cassell, G. B.", "given_names": "G. B.", "surname": "Cassell", "position": "African Assistant Government Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 190, "salary_max": 240},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1930 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1930

OFFICIALS = [
    {"name": "Sir J. A. Byrne", "canonical_name": "Byrne, J. A.", "given_names": "J. A.", "surname": "Byrne", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G.", "K.B.E.", "C.B."], "military_rank": "Brigadier-General"},
    {"name": "H. E. Allen", "canonical_name": "Allen, H. E.", "given_names": "H. E.", "surname": "Allen", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 450, "salary_max": 450, "military_rank": "Major"},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "Chief Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. A. Young", "canonical_name": "Young, M. A.", "given_names": "M. A.", "surname": "Young", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280},
    {"name": "C. E. Cookson", "canonical_name": "Cookson, C. E.", "given_names": "C. E.", "surname": "Cookson", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "military_rank": "Capt."},
    {"name": "J. E. Benham", "canonical_name": "Benham, J. E.", "given_names": "J. E.", "surname": "Benham", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "military_rank": "Capt."},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "honors": ["M.B.E."]},
    {"name": "D. B. Drummond", "canonical_name": "Drummond, D. B.", "given_names": "D. B.", "surname": "Drummond", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "W. W. Barnhill", "canonical_name": "Barnhill, W. W.", "given_names": "W. W.", "surname": "Barnhill", "position": "Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. H. Cheetham Smart", "canonical_name": "Smart, J. H. Cheetham", "given_names": "J. H. Cheetham", "surname": "Smart", "position": "African Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "T. A. Thompson", "canonical_name": "Thompson, T. A.", "given_names": "T. A.", "surname": "Thompson", "position": "African Assistant Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "First Grude Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. K. Scott", "canonical_name": "Scott, A. K.", "given_names": "A. K.", "surname": "Scott", "position": "First Grude Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "E. S. George", "canonical_name": "George, E. S.", "given_names": "E. S.", "surname": "George", "position": "First Grude Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "D. E. Stubbe", "canonical_name": "Stubbe, D. E.", "given_names": "D. E.", "surname": "Stubbe", "position": "First Grude Clerks", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Government Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 600, "salary_max": 720, "duty_allowance": 72},
    {"name": "G. Worthington", "canonical_name": "Worthington, G.", "given_names": "G.", "surname": "Worthington", "position": "Assistant Government Printer", "department": "Printing Branch - Sierra Leone", "salary_scale": "F"},
    {"name": "G. B. Cassell", "canonical_name": "Cassell, G. B.", "given_names": "G. B.", "surname": "Cassell", "position": "African Assistant Government Printers", "department": "Printing Branch - Sierra Leone", "salary_min": 190, "salary_max": 240}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
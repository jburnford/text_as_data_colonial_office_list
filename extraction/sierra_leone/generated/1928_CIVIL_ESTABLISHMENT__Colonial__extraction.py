"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "Sir J. A. Byrne", "canonical_name": "Byrne, J. A.", "given_names": "J. A.", "surname": "Byrne", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.B.E.", "C.B."], "military_rank": "Brigadier-General"},
    {"name": "H. E. Allen", "canonical_name": "Allen, H. E.", "given_names": "H. E.", "surname": "Allen", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 450, "salary_max": 450, "military_rank": "Major"},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "First Grade Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "H. C. Luke", "canonical_name": "Luke, H. C.", "given_names": "H. C.", "surname": "Luke", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280, "honors": ["C.M.G."]},
    {"name": "C. E. Cookson", "canonical_name": "Cookson, C. E.", "given_names": "C. E.", "surname": "Cookson", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "military_rank": "Capt."},
    {"name": "J. E. Benham", "canonical_name": "Benham, J. E.", "given_names": "J. E.", "surname": "Benham", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "military_rank": "Capt."},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "honors": ["M.B.E."]},
    {"name": "D. C. Thompson", "canonical_name": "Thompson, D. C.", "given_names": "D. C.", "surname": "Thompson", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "D. B. Drummond", "canonical_name": "Drummond, D. B.", "given_names": "D. B.", "surname": "Drummond", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. H. Cheetham Smart", "canonical_name": "Smart, J. H. Cheetham", "given_names": "J. H. Cheetham", "surname": "Smart", "position": "African Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "T. A. Thompson", "canonical_name": "Thompson, T. A.", "given_names": "T. A.", "surname": "Thompson", "position": "Staff Superintendent", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. E. Scott", "canonical_name": "Scott, A. E.", "given_names": "A. E.", "surname": "Scott", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "H. B. Marke", "canonical_name": "Marke, H. B.", "given_names": "H. B.", "surname": "Marke", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. McCulloch", "canonical_name": "McCulloch, J.", "given_names": "J.", "surname": "McCulloch", "position": "Government Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 600, "salary_max": 720, "duty_allowance": 72},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Government Printer", "department": "Printing Branch - Sierra Leone", "salary_scale": "F"},
    {"name": "G. B. Cassell", "canonical_name": "Cassell, G. B.", "given_names": "G. B.", "surname": "Cassell", "position": "African Assistant Government Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 190, "salary_max": 240}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
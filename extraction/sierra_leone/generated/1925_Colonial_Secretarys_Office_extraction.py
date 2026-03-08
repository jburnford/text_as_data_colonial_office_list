"""
Sierra Leone Colonial Office List 1925 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1925

OFFICIALS = [
    {"name": "H. C. Luke", "canonical_name": "Luke, H. C.", "given_names": "H. C.", "surname": "Luke", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280},
    {"name": "G. C. Du Boulay", "canonical_name": "Du Boulay, G. C.", "given_names": "G. C.", "surname": "Du Boulay", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "J. E. Benham", "canonical_name": "Benham, J. E.", "given_names": "J. E.", "surname": "Benham", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "honors": ["M.B.E."], "salary_scale": "B"},
    {"name": "D. C. Thompson", "canonical_name": "Thompson, D. C.", "given_names": "D. C.", "surname": "Thompson", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "D. B. Drummond", "canonical_name": "Drummond, D. B.", "given_names": "D. B.", "surname": "Drummond", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. H. Cheetham Smart", "canonical_name": "Smart, J. H. Cheetham", "given_names": "J. H.", "surname": "Smart", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 600},
    {"name": "D. W. Carrol", "canonical_name": "Carrol, D. W.", "given_names": "D. W.", "surname": "Carrol", "position": "Staff Superintendent", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "I. F. T. George", "canonical_name": "George, I. F. T.", "given_names": "I. F. T.", "surname": "George", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. E. Scott", "canonical_name": "Scott, A. E.", "given_names": "A. E.", "surname": "Scott", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "C. G. King", "canonical_name": "King, C. G.", "given_names": "C. G.", "surname": "King", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "H. B. Marke", "canonical_name": "Marke, H. B.", "given_names": "H. B.", "surname": "Marke", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "J. E. Clarke", "canonical_name": "Clarke, J. E.", "given_names": "J. E.", "surname": "Clarke", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
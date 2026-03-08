"""
Sierra Leone Colonial Office List 1950 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1950

OFFICIALS = [
    {"name": "Sir George Beresford-Stooke", "canonical_name": "Beresford-Stooke, George", "surname": "Beresford-Stooke", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor and Personal Staff - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G."]},
    {"name": "D. A. S. Wright", "canonical_name": "Wright, D. A. S.", "given_names": "D. A. S.", "surname": "Wright", "position": "Private Secretary and Aide-de-Camp", "department": "Governor and Personal Staff - Sierra Leone", "military_rank": "Lieut.-Commander"},
    {"name": "R. O. Ramage", "canonical_name": "Ramage, R. O.", "given_names": "R. O.", "surname": "Ramage", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1650, "salary_max": 1650, "honors": ["C.M.G."]},
    {"name": "C. J. Hodgens", "canonical_name": "Hodgens, C. J.", "given_names": "C. J.", "surname": "Hodgens", "position": "Financial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1500, "salary_max": 1500, "honors": ["C.B.E.", "M.C."]},
    {"name": "G. E. Mercer", "canonical_name": "Mercer, G. E.", "given_names": "G. E.", "surname": "Mercer", "position": "Development and Planning Officer", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1350, "salary_max": 1350, "salary_scale": "Administrative Staff Grade"},
    {"name": "C. J. Mabey", "canonical_name": "Mabey, C. J.", "given_names": "C. J.", "surname": "Mabey", "position": "Chief Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Additional Chief Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "salary_scale": "Administrative Staff Grade"},
    {"name": "H. W. Davidson", "canonical_name": "Davidson, H. W.", "given_names": "H. W.", "surname": "Davidson", "position": "Deputy Financial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "honors": ["M.B.E."]},
    {"name": "F. W. Essex", "canonical_name": "Essex, F. W.", "given_names": "F. W.", "surname": "Essex", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A"},
    {"name": "P. W. Youens", "canonical_name": "Youens, P. W.", "given_names": "P. W.", "surname": "Youens", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A"},
    {"name": "J. W. Paul", "canonical_name": "Paul, J. W.", "given_names": "J. W.", "surname": "Paul", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A", "honors": ["M.C."]},
    {"name": "A. F. Meredith", "canonical_name": "Meredith, A. F.", "given_names": "A. F.", "surname": "Meredith", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A"},
    {"name": "T. C. Luke", "canonical_name": "Luke, T. C.", "given_names": "T. C.", "surname": "Luke", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A", "honors": ["M.B.E."]},
    {"name": "M. J. G. Sandercrook", "canonical_name": "Sandercrook, M. J. G.", "given_names": "M. J. G.", "surname": "Sandercrook", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Watson", "canonical_name": "Watson, J.", "given_names": "J.", "surname": "Watson", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A"},
    {"name": "W. A. Dillsworth", "canonical_name": "Dillsworth, W. A.", "given_names": "W. A.", "surname": "Dillsworth", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A"},
    {"name": "M. S. Porcher", "canonical_name": "Porcher, M. S.", "given_names": "M. S.", "surname": "Porcher", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A"},
    {"name": "D. Kirby", "canonical_name": "Kirby, D.", "given_names": "D.", "surname": "Kirby", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A"},
    {"name": "M. Mahdi", "canonical_name": "Mahdi, M.", "given_names": "M.", "surname": "Mahdi", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
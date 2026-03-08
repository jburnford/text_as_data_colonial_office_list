"""
Sierra Leone Colonial Office List 1933 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1933

OFFICIALS = [
    {"name": "Sir Arnold W. Hodson", "canonical_name": "Hodson, Arnold W.", "given_names": "Arnold W.", "surname": "Hodson", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G."]},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "Chief Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "Capt. C. E. Cookson", "canonical_name": "Cookson, C. E.", "given_names": "C. E.", "surname": "Cookson", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280, "honors": ["C.M.G."], "military_rank": "Captain"},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Chief Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "honors": ["M.B.E."]},
    {"name": "Major J. E. Benham", "canonical_name": "Benham, J. E.", "given_names": "J. E.", "surname": "Benham", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "military_rank": "Major"},
    {"name": "B. A. Finn", "canonical_name": "Finn, B. A.", "given_names": "B. A.", "surname": "Finn", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "D. B. Drummond", "canonical_name": "Drummond, D. B.", "given_names": "D. B.", "surname": "Drummond", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "W. W. Barnhill", "canonical_name": "Barnhill, W. W.", "given_names": "W. W.", "surname": "Barnhill", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. H. Cheetham Smart", "canonical_name": "Smart, J. H. Cheetham", "given_names": "J. H. Cheetham", "surname": "Smart", "position": "African Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 600, "honors": ["I.S.O."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "African Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 600},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Government Printer", "department": "Printing Department - Sierra Leone", "salary_min": 600, "salary_max": 720, "duty_allowance": 72},
    {"name": "G. Worthington", "canonical_name": "Worthington, G.", "given_names": "G.", "surname": "Worthington", "position": "Assistant Government Printer", "department": "Printing Department - Sierra Leone", "salary_min": 420, "salary_max": 600}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
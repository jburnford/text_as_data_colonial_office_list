"""
Sierra Leone Colonial Office List 1934 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1934

OFFICIALS = [
    {"name": "Sir Arnold W. Hodson", "canonical_name": "Hodson, Arnold W.", "given_names": "Arnold W.", "surname": "Hodson", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G."]},
    {"name": "N. T. A. Davis", "canonical_name": "Davis, N. T. A.", "given_names": "N. T. A.", "surname": "Davis", "position": "Chief Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "Capt. C. E. Cookson", "canonical_name": "Cookson, C. E.", "given_names": "C. E.", "surname": "Cookson", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280, "honors": ["C.M.G."], "military_rank": "Captain"},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Chief Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "honors": ["M.B.E."]},
    {"name": "Major J. E. Benham", "canonical_name": "Benham, J. E.", "given_names": "J. E.", "surname": "Benham", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "military_rank": "Major"},
    {"name": "D. B. Drummond", "canonical_name": "Drummond, D. B.", "given_names": "D. B.", "surname": "Drummond", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "W. W. Barnhill", "canonical_name": "Barnhill, W. W.", "given_names": "W. W.", "surname": "Barnhill", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. H. Cheetah Smart", "canonical_name": "Smart, J. H. Cheetah", "given_names": "J. H. Cheetah", "surname": "Smart", "position": "African Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 600, "honors": ["I.S.O."]},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "African Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "W. H. Crocker", "canonical_name": "Crocker, W. H.", "given_names": "W. H.", "surname": "Crocker", "position": "Government Printer", "department": "Printing Department - Sierra Leone", "salary_min": 600, "salary_max": 720, "duty_allowance": 72}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
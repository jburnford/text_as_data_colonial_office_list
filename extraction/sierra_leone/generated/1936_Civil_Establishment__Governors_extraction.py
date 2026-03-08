"""
Sierra Leone Colonial Office List 1936 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1936

OFFICIALS = [
    {"name": "Sir H. Monck-Mason Moore", "canonical_name": "Monck-Mason Moore, H.", "given_names": "H.", "surname": "Monck-Mason Moore", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "honors": ["K.C.M.G."], "duty_allowance": 1000},
    {"name": "N. T. A. Davis", "canonical_name": "Davis, N. T. A.", "given_names": "N. T. A.", "surname": "Davis", "position": "Chief Clerk", "department": "Governor's Office - Sierra Leone", "salary_min": 204, "salary_max": 372},
    {"name": "H. R. R. Blood", "canonical_name": "Blood, H. R. R.", "given_names": "H. R. R.", "surname": "Blood", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "honors": ["C.M.G."], "duty_allowance": 280},
    {"name": "A. B. Mathews", "canonical_name": "Mathews, A. B.", "given_names": "A. B.", "surname": "Mathews", "position": "Chief Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "D. B. Drummond", "canonical_name": "Drummond, D. B.", "given_names": "D. B.", "surname": "Drummond", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "African Assistant Colonial Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "W. H. Crocker", "canonical_name": "Crocker, W. H.", "given_names": "W. H.", "surname": "Crocker", "position": "Government Printer", "department": "Printing Department - Sierra Leone", "salary_min": 600, "salary_max": 720, "duty_allowance": 72}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
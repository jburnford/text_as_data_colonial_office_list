"""
Sierra Leone Colonial Office List 1940 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1940

OFFICIALS = [
    {"name": "Sir Douglas Jardine", "canonical_name": "Jardine, Douglas", "surname": "Jardine", "position": "Governor, Commander-in-Chief and Vice-Admiral", "department": "Governor's Office - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "duty_allowance": 1000, "honors": ["K.C.M.G.", "O.B.E."]},
    {"name": "T. G. Fitzgerald", "canonical_name": "Fitzgerald, T. G.", "given_names": "T. G.", "surname": "Fitzgerald", "position": "Private Secretary and Aide-de-Camp", "department": "Governor's Office - Sierra Leone", "salary_min": 450, "salary_max": 450},
    {"name": "H. R. R. Blood", "canonical_name": "Blood, H. R. R.", "given_names": "H. R. R.", "surname": "Blood", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "honors": ["C.M.G."]},
    {"name": "A. B. Mathews", "canonical_name": "Mathews, A. B.", "given_names": "A. B.", "surname": "Mathews", "position": "Chief Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "N. T. A. Davis", "canonical_name": "Davis, N. T. A.", "given_names": "N. T. A.", "surname": "Davis", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "G. Worthington", "canonical_name": "Worthington, G.", "given_names": "G.", "surname": "Worthington", "position": "Government Printer", "department": "Printing and Stationery Department - Sierra Leone", "salary_min": 600, "salary_max": 780},
    {"name": "G. B. Cassell", "canonical_name": "Cassell, G. B.", "given_names": "G. B.", "surname": "Cassell", "position": "African Assistant Government Printer", "department": "Printing and Stationery Department - Sierra Leone", "salary_min": 264, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
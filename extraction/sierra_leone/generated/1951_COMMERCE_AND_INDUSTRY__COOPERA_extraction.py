"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "S. M. Taylor", "canonical_name": "Taylor, S. M.", "given_names": "S. M.", "surname": "Taylor", "position": "Director", "department": "Commerce and Industry - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "acting_status": "Acting", "honors": ["M.C."]},
    {"name": "J. Thorpe", "canonical_name": "Thorpe, J.", "given_names": "J.", "surname": "Thorpe", "position": "Assistant Director", "department": "Commerce and Industry - Sierra Leone", "salary_min": 720, "salary_max": 1000, "honors": ["M.C."]},
    {"name": "E. J. D. Cross", "canonical_name": "Cross, E. J. D.", "given_names": "E. J. D.", "surname": "Cross", "position": "Assistants to Director", "department": "Commerce and Industry - Sierra Leone", "salary_scale": "B"},
    {"name": "S. B. Nicol-Cole", "canonical_name": "Nicol-Cole, S. B.", "given_names": "S. B.", "surname": "Nicol-Cole", "position": "Assistants to Director", "department": "Commerce and Industry - Sierra Leone", "salary_scale": "B"},
    {"name": "O. B. Wise", "canonical_name": "Wise, O. B.", "given_names": "O. B.", "surname": "Wise", "position": "Assistants to Director", "department": "Commerce and Industry - Sierra Leone", "salary_scale": "B"},
    {"name": "S. A. J. Pratt", "canonical_name": "Pratt, S. A. J.", "given_names": "S. A. J.", "surname": "Pratt", "position": "Assistant Economist", "department": "Commerce and Industry - Sierra Leone", "salary_scale": "A"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Statistician", "department": "Commerce and Industry - Sierra Leone", "salary_scale": "A"},
    {"name": "K. S. Griffin", "canonical_name": "Griffin, K. S.", "given_names": "K. S.", "surname": "Griffin", "position": "Senior Inspector of Produce", "department": "Commerce and Industry - Sierra Leone", "salary_scale": "B", "salary_min": 660, "salary_max": 900},
    {"name": "C. G. White", "canonical_name": "White, C. G.", "given_names": "C. G.", "surname": "White", "position": "Inspector of Produce", "department": "Commerce and Industry - Sierra Leone", "salary_scale": "B"},
    {"name": "B. J. Barton", "canonical_name": "Barton, B. J.", "given_names": "B. J.", "surname": "Barton", "position": "Fisheries Officer", "department": "Commerce and Industry - Sierra Leone", "salary_scale": "A", "honors": ["D.S.O.", "M.C."]},
    {"name": "K. A. L. Hill", "canonical_name": "Hill, K. A. L.", "given_names": "K. A. L.", "surname": "Hill", "position": "Registrar", "department": "Co-operative Societies - Sierra Leone", "salary_min": 1000, "salary_max": 1000}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
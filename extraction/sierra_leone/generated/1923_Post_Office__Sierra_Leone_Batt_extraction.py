"""
Sierra Leone Colonial Office List 1923 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1923

OFFICIALS = [
    {"name": "H. T. March", "canonical_name": "March, H. T.", "given_names": "H. T.", "surname": "March", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "N. S. Davis", "canonical_name": "Davis, N. S.", "given_names": "N. S.", "surname": "Davis", "position": "Accountant", "department": "Post Office - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Staff Superintendent", "department": "Post Office - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "J. Smyth", "canonical_name": "Smyth, J.", "given_names": "J.", "surname": "Smyth", "position": "Principal Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "Principal Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Principal Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "V. E. George", "canonical_name": "George, V. E.", "given_names": "V. E.", "surname": "George", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. G. Johnson", "canonical_name": "Johnson, J. G.", "given_names": "J. G.", "surname": "Johnson", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. T. Nottidge", "canonical_name": "Nottidge, J. T.", "given_names": "J. T.", "surname": "Nottidge", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. T. W. Richards", "canonical_name": "Richards, A. T. W.", "given_names": "A. T. W.", "surname": "Richards", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. N. Ogilvie", "canonical_name": "Ogilvie, A. N.", "given_names": "A. N.", "surname": "Ogilvie", "position": "Major", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 900, "salary_max": 900, "duty_allowance": 182},
    {"name": "R. M. S. Baynes", "canonical_name": "Baynes, R. M. S.", "given_names": "R. M. S.", "surname": "Baynes", "position": "Captain", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "E. W. T. Rowe", "canonical_name": "Rowe, E. W. T.", "given_names": "E. W. T.", "surname": "Rowe", "position": "Captain", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "C. C. Fowkes", "canonical_name": "Fowkes, C. C.", "given_names": "C. C.", "surname": "Fowkes", "position": "Captain", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "honors": ["M.C."]},
    {"name": "J. A. S. Hopkins", "canonical_name": "Hopkins, J. A. S.", "given_names": "J. A. S.", "surname": "Hopkins", "position": "Captain", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "E. L. G. Beville", "canonical_name": "Beville, E. L. G.", "given_names": "E. L. G.", "surname": "Beville", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600},
    {"name": "A. Robertson", "canonical_name": "Robertson, A.", "given_names": "A.", "surname": "Robertson", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600},
    {"name": "P. Prefect", "canonical_name": "Prefect, P.", "given_names": "P.", "surname": "Prefect", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600},
    {"name": "R. M. Hall", "canonical_name": "Hall, R. M.", "given_names": "R. M.", "surname": "Hall", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "honors": ["M.C."]},
    {"name": "T. W. Doke", "canonical_name": "Doke, T. W.", "given_names": "T. W.", "surname": "Doke", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600},
    {"name": "A. E. Salter", "canonical_name": "Salter, A. E.", "given_names": "A. E.", "surname": "Salter", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "honors": ["M.C."]},
    {"name": "N. McIver", "canonical_name": "McIver, N.", "given_names": "N.", "surname": "McIver", "position": "Adjutant and Quartermaster", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "duty_allowance": 91, "military_rank": "Lieut."},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
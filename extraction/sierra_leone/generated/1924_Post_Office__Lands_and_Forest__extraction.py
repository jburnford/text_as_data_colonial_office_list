"""
Sierra Leone Colonial Office List 1924 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1924

OFFICIALS = [
    {"name": "H. T. March", "canonical_name": "March, H. T.", "given_names": "H. T.", "surname": "March", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "N. S. Davis", "canonical_name": "Davis, N. S.", "given_names": "N. S.", "surname": "Davis", "position": "Assistant Postmaster General and Accountant", "department": "Post Office - Sierra Leone", "salary_scale": "A"},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Staff Superintendent", "department": "Post Office - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "J. Smyth", "canonical_name": "Smyth, J.", "given_names": "J.", "surname": "Smyth", "position": "Principal Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "Principal Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Principal Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "V. E. George", "canonical_name": "George, V. E.", "given_names": "V. E.", "surname": "George", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. G. Johnson", "canonical_name": "Johnson, J. G.", "given_names": "J. G.", "surname": "Johnson", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. T. Nottingde", "canonical_name": "Nottingde, J. T.", "given_names": "J. T.", "surname": "Nottingde", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. T. W. Richards", "canonical_name": "Richards, A. T. W.", "given_names": "A. T. W.", "surname": "Richards", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "M. T. Dawe", "canonical_name": "Dawe, M. T.", "given_names": "M. T.", "surname": "Dawe", "position": "Commissioner of Lands and Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "D. W. Scotland", "canonical_name": "Scotland, D. W.", "given_names": "D. W.", "surname": "Scotland", "position": "Director of Agriculture", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "F. D. Fisher", "canonical_name": "Fisher, F. D.", "given_names": "F. D.", "surname": "Fisher", "position": "Provincial Superintendent of Agricultural", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C", "military_rank": "Captain"},
    {"name": "S. L. Moseley", "canonical_name": "Moseley, S. L.", "given_names": "S. L.", "surname": "Moseley", "position": "Superintendent, Experimental Farm", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Conservator of Forests", "department": "Lands and Forest Department - Sierra Leone"},
    {"name": "K. G. Burbridge", "canonical_name": "Burbridge, K. G.", "given_names": "K. G.", "surname": "Burbridge", "position": "Assistant Conservator of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. Macdonald", "canonical_name": "Macdonald, E.", "given_names": "E.", "surname": "Macdonald", "position": "Assistant Conservator of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservator of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
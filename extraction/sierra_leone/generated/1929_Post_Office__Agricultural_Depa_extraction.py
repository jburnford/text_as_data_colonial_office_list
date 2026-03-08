"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "N. S. Davis", "canonical_name": "Davis, N. S.", "given_names": "N. S.", "surname": "Davis", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Postmaster General", "department": "Post Office - Sierra Leone", "salary_scale": "A"},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Assistant Postmaster General and Accountant", "department": "Post Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "J. H. Smyth", "canonical_name": "Smyth, J. H.", "given_names": "J. H.", "surname": "Smyth", "position": "Staff Superintendent", "department": "Post Office - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "Chief Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "Chief Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "V. E. George", "canonical_name": "George, V. E.", "given_names": "V. E.", "surname": "George", "position": "Chief Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "J. G. Johnson", "canonical_name": "Johnson, J. G.", "given_names": "J. G.", "surname": "Johnson", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. T. Nottidge", "canonical_name": "Nottidge, J. T.", "given_names": "J. T.", "surname": "Nottidge", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. T. W. Richards", "canonical_name": "Richards, A. T. W.", "given_names": "A. T. W.", "surname": "Richards", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "W. J. J. Cole", "canonical_name": "Cole, W. J. J.", "given_names": "W. J. J.", "surname": "Cole", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "E. S. B. Francis", "canonical_name": "Francis, E. S. B.", "given_names": "E. S. B.", "surname": "Francis", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "Z. H. Smith", "canonical_name": "Smith, Z. H.", "given_names": "Z. H.", "surname": "Smith", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "G. H. H. Branche", "canonical_name": "Branche, G. H. H.", "given_names": "G. H. H.", "surname": "Branche", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "P. S. Godwin", "canonical_name": "Godwin, P. S.", "given_names": "P. S.", "surname": "Godwin", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. E. Mammah", "canonical_name": "Mammah, A. E.", "given_names": "A. E.", "surname": "Mammah", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "M. Y. Sanusi", "canonical_name": "Sanusi, M. Y.", "given_names": "M. Y.", "surname": "Sanusi", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "D. W. Scootland", "canonical_name": "Scootland, D. W.", "given_names": "D. W.", "surname": "Scootland", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "allowances": "and special allowance of 120l."},
    {"name": "H. O. Luxford", "canonical_name": "Luxford, H. O.", "given_names": "H. O.", "surname": "Luxford", "position": "Secretary", "department": "Agricultural Department - Sierra Leone", "salary_min": 400, "salary_max": 600},
    {"name": "F. J. Martin", "canonical_name": "Martin, F. J.", "given_names": "F. J.", "surname": "Martin", "position": "Agricultural Chemist", "department": "Agricultural Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "qualifications": ["M.A.", "Ph.D.", "F.I.C."]},
    {"name": "H. C. Doyne", "canonical_name": "Doyne, H. C.", "given_names": "H. C.", "surname": "Doyne", "position": "Assistant Agricultural Chemist", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C", "qualifications": ["M.A.", "A.I.C."]},
    {"name": "E. Hargreaves", "canonical_name": "Hargreaves, E.", "given_names": "E.", "surname": "Hargreaves", "position": "Entomologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "and 72l. seniority allowance.", "qualifications": ["A.R.C.S.", "F.E.S."]},
    {"name": "J. G. H. Frew", "canonical_name": "Frew, J. G. H.", "given_names": "J. G. H.", "surname": "Frew", "position": "* Entomologist, Tsetse Fly Survey", "department": "Agricultural Department - Sierra Leone", "salary_min": 700, "salary_max": 700, "qualifications": ["Ph.D."]},
    {"name": "F. C. Deighton", "canonical_name": "Deighton, F. C.", "given_names": "F. C.", "surname": "Deighton", "position": "Mycologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "qualifications": ["M.A."]},
    {"name": "D. C. Edwards", "canonical_name": "Edwards, D. C.", "given_names": "D. C.", "surname": "Edwards", "position": "Agricultural Instructor", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "qualifications": ["B.Sc."]},
    {"name": "J. W. D. Fisher", "canonical_name": "Fisher, J. W. D.", "given_names": "J. W. D.", "surname": "Fisher", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C", "military_rank": "Capt."},
    {"name": "R. R. Glanville", "canonical_name": "Glanville, R. R.", "given_names": "R. R.", "surname": "Glanville", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. I. Nisbett", "canonical_name": "Nisbett, E. I.", "given_names": "E. I.", "surname": "Nisbett", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. V. R. Brown", "canonical_name": "Brown, J. V. R.", "given_names": "J. V. R.", "surname": "Brown", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "P. J. Moss", "canonical_name": "Moss, P. J.", "given_names": "P. J.", "surname": "Moss", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "G. Tuach", "canonical_name": "Tuach, G.", "given_names": "G.", "surname": "Tuach", "position": "Inspector of Plants and Produce", "department": "Agricultural Department - Sierra Leone", "salary_scale": "F"},
    {"name": "F. W. B. Allinson", "canonical_name": "Allinson, F. W. B.", "given_names": "F. W. B.", "surname": "Allinson", "position": "Assistant Inspector of Plants and Produce", "department": "Agricultural Department - Sierra Leone", "salary_scale": "F"},
    {"name": "E. F. W. Smart", "canonical_name": "Smart, E. F. W.", "given_names": "E. F. W.", "surname": "Smart", "position": "Chief Clerk", "department": "Agricultural Department - Sierra Leone", "salary_min": 264, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1930 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1930

OFFICIALS = [
    {"name": "A. H. Kirby", "canonical_name": "Kirby, A. H.", "given_names": "A. H.", "surname": "Kirby", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["O.B.E."]},
    {"name": "F. J. Martin", "canonical_name": "Martin, F. J.", "given_names": "F. J.", "surname": "Martin", "position": "Agricultural Chemist", "department": "Agricultural Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "qualifications": ["M.A.", "Ph.D.", "F.I.C."]},
    {"name": "H. C. Doyne", "canonical_name": "Doyne, H. C.", "given_names": "H. C.", "surname": "Doyne", "position": "Assistant Agricultural Chemist", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C", "qualifications": ["M.A.", "A.I.C."]},
    {"name": "E. Hargreaves", "canonical_name": "Hargreaves, E.", "given_names": "E.", "surname": "Hargreaves", "position": "Entomologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "qualifications": ["A.R.C.S.", "F.E.S."]},
    {"name": "F. C. Deighton", "canonical_name": "Deighton, F. C.", "given_names": "F. C.", "surname": "Deighton", "position": "Mycologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "qualifications": ["M.A."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Agricultural Instructor", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "J. W. D. Fisher", "canonical_name": "Fisher, J. W. D.", "given_names": "J. W. D.", "surname": "Fisher", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C", "military_rank": "Captain"},
    {"name": "R. R. Glanville", "canonical_name": "Glanville, R. R.", "given_names": "R. R.", "surname": "Glanville", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. I. Nisbett", "canonical_name": "Nisbett, E. I.", "given_names": "E. I.", "surname": "Nisbett", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. V. R. Brown", "canonical_name": "Brown, J. V. R.", "given_names": "J. V. R.", "surname": "Brown", "position": "Provincial Superintendent of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
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
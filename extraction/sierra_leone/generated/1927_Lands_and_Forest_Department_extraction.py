"""
Sierra Leone Colonial Office List 1927 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1927

OFFICIALS = [
    {"name": "M. T. Dawe", "canonical_name": "Dawe, M. T.", "given_names": "M. T.", "surname": "Dawe", "position": "Commissioner of Lands and Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240, "honors": ["O.B.E."]},
    {"name": "D. W. Scotland", "canonical_name": "Scotland, D. W.", "given_names": "D. W.", "surname": "Scotland", "position": "Director of Agriculture", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "E. Hargreaves", "canonical_name": "Hargreaves, E.", "given_names": "E.", "surname": "Hargreaves", "position": "Entomologist", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 720, "salary_max": 720, "qualifications": ["A.R.C.S.", "F.F.S."]},
    {"name": "F. J. Martin", "canonical_name": "Martin, F. J.", "given_names": "F. J.", "surname": "Martin", "position": "Agricultural Chemist", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "qualifications": ["Ph.D.", "F.I.C."]},
    {"name": "H. C. Doyne", "canonical_name": "Doyne, H. C.", "given_names": "H. C.", "surname": "Doyne", "position": "Assistant Agricultural Chemist", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "D. C. Edwards", "canonical_name": "Edwards, D. C.", "given_names": "D. C.", "surname": "Edwards", "position": "Agricultural Instructor", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "qualifications": ["B.Sc."]},
    {"name": "J. W. D. Fisher", "canonical_name": "Fisher, J. W. D.", "given_names": "J. W. D.", "surname": "Fisher", "position": "Provincial Superintendents of Agricultural", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C", "military_rank": "Capt."},
    {"name": "R. R. Glanville", "canonical_name": "Glanville, R. R.", "given_names": "R. R.", "surname": "Glanville", "position": "Provincial Superintendents of Agricultural", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. J. Nisbett", "canonical_name": "Nisbett, E. J.", "given_names": "E. J.", "surname": "Nisbett", "position": "Provincial Superintendents of Agricultural", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. V. R. Brown", "canonical_name": "Brown, J. V. R.", "given_names": "J. V. R.", "surname": "Brown", "position": "Provincial Superintendents of Agricultural", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "P. J. Moss", "canonical_name": "Moss, P. J.", "given_names": "P. J.", "surname": "Moss", "position": "Provincial Superintendents of Agricultural", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "K. G. Burbridge", "canonical_name": "Burbridge, K. G.", "given_names": "K. G.", "surname": "Burbridge", "position": "Conservator of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "E. Macdonald", "canonical_name": "Macdonald, E.", "given_names": "E.", "surname": "Macdonald", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. Burns", "canonical_name": "Burns, A.", "given_names": "A.", "surname": "Burns", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. C. Mallam", "canonical_name": "Mallam, J. C.", "given_names": "J. C.", "surname": "Mallam", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "G. Tuach", "canonical_name": "Tuach, G.", "given_names": "G.", "surname": "Tuach", "position": "Inspector of Plants and Produce", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "F"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1925 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1925

OFFICIALS = [
    {"name": "M. T. Dawe", "canonical_name": "Dawe, M. T.", "given_names": "M. T.", "surname": "Dawe", "position": "Commissioner of Lands and Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "D. W. Scotland", "canonical_name": "Scotland, D. W.", "given_names": "D. W.", "surname": "Scotland", "position": "Director of Agriculture", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "E. Hargreaves", "canonical_name": "Hargreaves, E.", "given_names": "E.", "surname": "Hargreaves", "position": "Entomologist", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 700, "salary_max": 700, "qualifications": ["A.R.C.S.", "F.E.S."]},
    {"name": "F. J. Martin", "canonical_name": "Martin, F. J.", "given_names": "F. J.", "surname": "Martin", "position": "Agricultural Chemist", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "qualifications": ["M.A.", "Ph.D.", "F.I.C."]},
    {"name": "W. E. Edwards", "canonical_name": "Edwards, W. E.", "given_names": "W. E.", "surname": "Edwards", "position": "Agricultural Instructor", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "qualifications": ["B.Sc."]},
    {"name": "J. W. D. Fisher", "canonical_name": "Fisher, J. W. D.", "given_names": "J. W. D.", "surname": "Fisher", "position": "Provincial Superintendent of Agricultural", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C", "military_rank": "Capt."},
    {"name": "R. R. Glanville", "canonical_name": "Glanville, R. R.", "given_names": "R. R.", "surname": "Glanville", "position": "Provincial Superintendent of Agricultural", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "S. L. Moseley", "canonical_name": "Moseley, S. L.", "given_names": "S. L.", "surname": "Moseley", "position": "Superintendent, Experimental Farm", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "K. G. Burbridge", "canonical_name": "Burbridge, K. G.", "given_names": "K. G.", "surname": "Burbridge", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. Macdonald", "canonical_name": "Macdonald, E.", "given_names": "E.", "surname": "Macdonald", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "C"},
    {"name": "G. Tusch", "canonical_name": "Tusch, G.", "given_names": "G.", "surname": "Tusch", "position": "Inspector of Plants and Produce", "department": "Lands and Forest Department - Sierra Leone", "salary_scale": "F"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1923 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1923

OFFICIALS = [
    {"name": "M. T. Dawe", "canonical_name": "Dawe, M. T.", "given_names": "M. T.", "surname": "Dawe", "position": "Commissioner of Lands and Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "D. W. Scotland", "canonical_name": "Scotland, D. W.", "given_names": "D. W.", "surname": "Scotland", "position": "Director of Agriculture", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "F. D. Fisher", "canonical_name": "Fisher, F. D.", "given_names": "F. D.", "surname": "Fisher", "position": "Assistant in Agricultural Department", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 480, "salary_max": 920, "military_rank": "Capt."},
    {"name": "S. L. Moseley", "canonical_name": "Moseley, S. L.", "given_names": "S. L.", "surname": "Moseley", "position": "Superintendent, Experimental Farm", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 184, "salary_max": 204},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Conservator of Forests", "department": "Lands and Forest Department - Sierra Leone"},
    {"name": "K. G. Burbridge", "canonical_name": "Burbridge, K. G.", "given_names": "K. G.", "surname": "Burbridge", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "E. Macdonald", "canonical_name": "Macdonald, E.", "given_names": "E.", "surname": "Macdonald", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservators of Forests", "department": "Lands and Forest Department - Sierra Leone", "salary_min": 480, "salary_max": 920}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
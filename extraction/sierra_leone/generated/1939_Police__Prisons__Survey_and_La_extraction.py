"""
Sierra Leone Colonial Office List 1939 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1939

OFFICIALS = [
    {"name": "P. T. Brodie", "canonical_name": "Brodie, P. T.", "given_names": "P. T.", "surname": "Brodie", "position": "Commissioner of Police", "department": "Police - Sierra Leone", "salary_min": 920, "salary_max": 920, "duty_allowance": 92, "honors": ["D.S.O.", "M.C."], "military_rank": "Capt."},
    {"name": "R. J. Craig", "canonical_name": "Craig, R. J.", "given_names": "R. J.", "surname": "Craig", "position": "Senior Assistant Supt. of Police", "department": "Police - Sierra Leone", "salary_scale": "A", "honors": ["M.C."], "military_rank": "Capt."},
    {"name": "G. Tuach", "canonical_name": "Tuach, G.", "given_names": "G.", "surname": "Tuach", "position": "Senior Assistant Supt. of Police", "department": "Police - Sierra Leone", "salary_scale": "A", "salary_max": 720},
    {"name": "D. A. Boyd", "canonical_name": "Boyd, D. A.", "given_names": "D. A.", "surname": "Boyd", "position": "Assistant Supts. of Police", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 810},
    {"name": "P. E. Turnbull", "canonical_name": "Turnbull, P. E.", "given_names": "P. E.", "surname": "Turnbull", "position": "Assistant Supts. of Police", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 810},
    {"name": "R. H. Dolan", "canonical_name": "Dolan, R. H.", "given_names": "R. H.", "surname": "Dolan", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 550, "salary_max": 720},
    {"name": "A. Simmonds", "canonical_name": "Simmonds, A.", "given_names": "A.", "surname": "Simmonds", "position": "Asst. Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "African Asst. Keeper of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "P. A. Godwin", "canonical_name": "Godwin, P. A.", "given_names": "P. A.", "surname": "Godwin", "position": "Director of Surveys and Lands", "department": "Survey and Lands Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "honors": ["O.B.E.", "M.S.M."]},
    {"name": "R. C. Burgess", "canonical_name": "Burgess, R. C.", "given_names": "R. C.", "surname": "Burgess", "position": "Lands Officer and Surveyor", "department": "Survey and Lands Department - Sierra Leone", "salary_min": 880, "salary_max": 1000, "qualifications": ["F.S.I."]},
    {"name": "S. C. Collins", "canonical_name": "Collins, S. C.", "given_names": "S. C.", "surname": "Collins", "position": "Survey Probationer", "department": "Survey and Lands Department - Sierra Leone", "salary_min": 450, "salary_max": 840},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
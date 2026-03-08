"""
Sierra Leone Colonial Office List 1937 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1937

OFFICIALS = [
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Attorney-General", "department": "Law Officers - Sierra Leone", "salary_min": 1400, "salary_max": 1400},
    {"name": "A. R. W. Sayle", "canonical_name": "Sayle, A. R. W.", "given_names": "A. R. W.", "surname": "Sayle", "position": "Solicitor-General", "department": "Law Officers - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "military_rank": "Lieut.-Com."},
    {"name": "A. A. Cromie", "canonical_name": "Cromie, A. A.", "given_names": "A. A.", "surname": "Cromie", "position": "Junior Crown Counsel", "department": "Law Officers - Sierra Leone", "salary_min": 600, "salary_max": 840},
    {"name": "P. T. Brodie", "canonical_name": "Brodie, P. T.", "given_names": "P. T.", "surname": "Brodie", "position": "Commissioner of Police", "department": "Police - Sierra Leone", "salary_min": 920, "salary_max": 920, "duty_allowance": 92, "honors": ["D.S.O.", "M.C."], "military_rank": "Capt."},
    {"name": "J. Rabbitt", "canonical_name": "Rabbitt, J.", "given_names": "J.", "surname": "Rabbitt", "position": "Assistant Commissioners of Police", "department": "Police - Sierra Leone", "salary_scale": "A", "salary_max": 720},
    {"name": "R. J. Craig", "canonical_name": "Craig, R. J.", "given_names": "R. J.", "surname": "Craig", "position": "Assistant Commissioners of Police", "department": "Police - Sierra Leone", "salary_scale": "A", "salary_max": 720, "honors": ["M.C."], "military_rank": "Capt."},
    {"name": "G. Tuach", "canonical_name": "Tuach, G.", "given_names": "G.", "surname": "Tuach", "position": "Assistant Commissioners of Police", "department": "Police - Sierra Leone", "salary_scale": "A", "salary_max": 720},
    {"name": "C. E. Wool-Lewis", "canonical_name": "Wool-Lewis, C. E.", "given_names": "C. E.", "surname": "Wool-Lewis", "position": "Assistant Commissioners of Police", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 810},
    {"name": "R. H. Dolan", "canonical_name": "Dolan, R. H.", "given_names": "R. H.", "surname": "Dolan", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 550, "salary_max": 720},
    {"name": "A. Sinmonde", "canonical_name": "Sinmonde, A.", "given_names": "A.", "surname": "Sinmonde", "position": "Asst. Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "African Asst. Keeper of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "P. A. Godwin", "canonical_name": "Godwin, P. A.", "given_names": "P. A.", "surname": "Godwin", "position": "Director of Surveys", "department": "Survey and Lands Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "honors": ["M.S.M."]},
    {"name": "R. Temple", "canonical_name": "Temple, R.", "given_names": "R.", "surname": "Temple", "position": "Lands Officer", "department": "Survey and Lands Department - Sierra Leone", "salary_scale": "C"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
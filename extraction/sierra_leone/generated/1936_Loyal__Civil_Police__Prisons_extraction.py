"""
Sierra Leone Colonial Office List 1936 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1936

OFFICIALS = [
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Attorney-General", "department": "Judicial - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Solicitor-General", "department": "Judicial - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "L. E. C. Evans", "canonical_name": "Evans, L. E. C.", "given_names": "L. E. C.", "surname": "Evans", "position": "Senior Crown Counsel", "department": "Judicial - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority allowance"},
    {"name": "A. A. Cromie", "canonical_name": "Cromie, A. A.", "given_names": "A. A.", "surname": "Cromie", "position": "Junior Crown Counsel", "department": "Judicial - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority allowance"},
    {"name": "Capt. P. T. Brodie", "canonical_name": "Brodie, P. T.", "given_names": "P. T.", "surname": "Brodie", "position": "Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 920, "salary_max": 920, "duty_allowance": 92, "honors": ["D.S.O.", "M.C."], "military_rank": "Captain"},
    {"name": "J. Rabbitz", "canonical_name": "Rabbitz, J.", "given_names": "J.", "surname": "Rabbitz", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A"},
    {"name": "Capt. R. J. Craig", "canonical_name": "Craig, R. J.", "given_names": "R. J.", "surname": "Craig", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A", "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "G. Tuach", "canonical_name": "Tuach, G.", "given_names": "G.", "surname": "Tuach", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A"},
    {"name": "G. E. Biddle", "canonical_name": "Biddle, G. E.", "given_names": "G. E.", "surname": "Biddle", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_scale": "A", "honors": ["M.B.E."], "duty_allowance": 72},
    {"name": "A. Simmonds", "canonical_name": "Simmonds, A.", "given_names": "A.", "surname": "Simmonds", "position": "Asst. Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "African Asst. Keeper of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 310, "salary_max": 450}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
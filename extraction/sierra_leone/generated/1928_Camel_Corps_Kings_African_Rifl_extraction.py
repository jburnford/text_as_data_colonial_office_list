"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "R. F. Hornby", "canonical_name": "Hornby, R. F.", "given_names": "R. F.", "surname": "Hornby", "position": "Officer Commanding, Somaliland Camel Corps, K.A.R.", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "military_rank": "Captain"},
    {"name": "W. G. Mackay", "canonical_name": "Mackay, W. G.", "given_names": "W. G.", "surname": "Mackay", "position": "Company Commander (Major)", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 775, "salary_max": 775, "honors": ["O.B.E."], "military_rank": "Captain"},
    {"name": "K. G. Ferrie", "canonical_name": "Ferrie, K. G.", "given_names": "K. G.", "surname": "Ferrie", "position": "Company Commanders", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Lieut."},
    {"name": "E. F. S. Shirley", "canonical_name": "Shirley, E. F. S.", "given_names": "E. F. S.", "surname": "Shirley", "position": "Company Commanders", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Lieut."},
    {"name": "A. D. M. Lewis", "canonical_name": "Lewis, A. D. M.", "given_names": "A. D. M.", "surname": "Lewis", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "J. H. H. Williams", "canonical_name": "Williams, J. H. H.", "given_names": "J. H. H.", "surname": "Williams", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "N. W. Holbrook", "canonical_name": "Holbrook, N. W.", "given_names": "N. W.", "surname": "Holbrook", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "C. L. Ferrard", "canonical_name": "Ferrard, C. L.", "given_names": "C. L.", "surname": "Ferrard", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "qualifications": ["M.C."], "military_rank": "Lieuts."},
    {"name": "E. O. Burne", "canonical_name": "Burne, E. O.", "given_names": "E. O.", "surname": "Burne", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "A. S. Poulton", "canonical_name": "Poulton, A. S.", "given_names": "A. S.", "surname": "Poulton", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550},
    {"name": "J. W. Kaye", "canonical_name": "Kaye, J. W.", "given_names": "J. W.", "surname": "Kaye", "position": "Adjutant", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 550, "salary_max": 550, "military_rank": "Lieut.", "allowances": "50l."},
    {"name": "W. R. Haymes", "canonical_name": "Haymes, W. R.", "given_names": "W. R.", "surname": "Haymes", "position": "Pay and Quartermaster", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 400, "salary_max": 600, "military_rank": "Capt."},
    {"name": "A. K. Gardner", "canonical_name": "Gardner, A. K.", "given_names": "A. K.", "surname": "Gardner", "position": "Quartermaster-Sergeant", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 300, "salary_max": 400, "qualifications": ["M.M."], "military_rank": "Sergt."},
    {"name": "H. O. Cain", "canonical_name": "Cain, H. O.", "given_names": "H. O.", "surname": "Cain", "position": "Store Staff-Sergeant", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 300, "salary_max": 450},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
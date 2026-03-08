"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "R. F. Hornby", "canonical_name": "Hornby, R. F.", "given_names": "R. F.", "surname": "Hornby", "position": "Officer Commanding, Somaliland Camel Corps, K.A.R.", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "military_rank": "Captain", "acting_status": "Temporary Lt.-Col."},
    {"name": "W. G. Mackay", "canonical_name": "Mackay, W. G.", "given_names": "W. G.", "surname": "Mackay", "position": "Company Commander (Major)", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 775, "salary_max": 775, "honors": ["O.B.E."], "military_rank": "Captain", "acting_status": "Local Major"},
    {"name": "J. W. Kaye", "canonical_name": "Kaye, J. W.", "given_names": "J. W.", "surname": "Kaye", "position": "Company Commanders", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Lieut.", "acting_status": "Temporary Capt."},
    {"name": "N. W. Holbrook", "canonical_name": "Holbrook, N. W.", "given_names": "N. W.", "surname": "Holbrook", "position": "Company Commanders", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Lieut.", "acting_status": "Temporary Capt."},
    {"name": "J. H. H. Willans", "canonical_name": "Willans, J. H. H.", "given_names": "J. H. H.", "surname": "Willans", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "E. O. Burne", "canonical_name": "Burne, E. O.", "given_names": "E. O.", "surname": "Burne", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "A. S. Poulton", "canonical_name": "Poulton, A. S.", "given_names": "A. S.", "surname": "Poulton", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "G. D. Holmes", "canonical_name": "Holmes, G. D.", "given_names": "G. D.", "surname": "Holmes", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "honors": ["M.B.E."], "military_rank": "Lieuts."},
    {"name": "T. C. Hobbs", "canonical_name": "Hobbs, T. C.", "given_names": "T. C.", "surname": "Hobbs", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "honors": ["M.C."], "military_rank": "Lieuts."},
    {"name": "M. E. Gubbins", "canonical_name": "Gubbins, M. E.", "given_names": "M. E.", "surname": "Gubbins", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "C. J. Challice", "canonical_name": "Challice, C. J.", "given_names": "C. J.", "surname": "Challice", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "F. N. Elliott", "canonical_name": "Elliott, F. N.", "given_names": "F. N.", "surname": "Elliott", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "A. S. Poulton", "canonical_name": "Poulton, A. S.", "given_names": "A. S.", "surname": "Poulton", "position": "Adjutant", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 550, "salary_max": 550, "military_rank": "Lieut.", "allowances": "50l."},
    {"name": "W. R. Haymes", "canonical_name": "Haymes, W. R.", "given_names": "W. R.", "surname": "Haymes", "position": "Pay and Quartermaster", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 480, "salary_max": 720, "military_rank": "Capt."},
    {"name": "A. E. Gardner", "canonical_name": "Gardner, A. E.", "given_names": "A. E.", "surname": "Gardner", "position": "Store Staff-Sergeant", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 300, "salary_max": 450, "honors": ["M.M."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
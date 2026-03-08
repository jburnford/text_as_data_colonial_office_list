"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "H. B. Holt", "canonical_name": "Holt, H. B.", "given_names": "H. B.", "surname": "Holt", "position": "Officer Commanding, Somaliland Camel Corps, K.A.R.", "department": "Camel Corps, King's African Rifles", "salary_min": 1000, "salary_max": 1000, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "J. W. Kaye", "canonical_name": "Kaye, J. W.", "given_names": "J. W.", "surname": "Kaye", "position": "Second in Command", "department": "Camel Corps, King's African Rifles", "military_rank": "Lieut."},
    {"name": "N. W. Holbrook", "canonical_name": "Holbrook, N. W.", "given_names": "N. W.", "surname": "Holbrook", "position": "Company Commanders", "department": "Camel Corps, King's African Rifles", "salary_min": 700, "salary_max": 700, "military_rank": "Lieut."},
    {"name": "T. C. Hobbs", "canonical_name": "Hobbs, T. C.", "given_names": "T. C.", "surname": "Hobbs", "position": "Company Commanders", "department": "Camel Corps, King's African Rifles", "salary_min": 700, "salary_max": 700, "honors": ["M.C."], "military_rank": "Lieut."},
    {"name": "M. E. Gubbins", "canonical_name": "Gubbins, M. E.", "given_names": "M. E.", "surname": "Gubbins", "position": "Company Officers", "department": "Camel Corps, King's African Rifles", "salary_min": 500, "salary_max": 550, "military_rank": "Lieut."},
    {"name": "D. C. Campbell-Miles", "canonical_name": "Campbell-Miles, D. C.", "given_names": "D. C.", "surname": "Campbell-Miles", "position": "Company Officers", "department": "Camel Corps, King's African Rifles", "salary_min": 500, "salary_max": 550},
    {"name": "H. T. Crane", "canonical_name": "Crane, H. T.", "given_names": "H. T.", "surname": "Crane", "position": "Company Officers", "department": "Camel Corps, King's African Rifles", "salary_min": 500, "salary_max": 550},
    {"name": "W. G. Withycombe", "canonical_name": "Withycombe, W. G.", "given_names": "W. G.", "surname": "Withycombe", "position": "Company Officers", "department": "Camel Corps, King's African Rifles", "salary_min": 500, "salary_max": 550},
    {"name": "J. H. F. Collingwood", "canonical_name": "Collingwood, J. H. F.", "given_names": "J. H. F.", "surname": "Collingwood", "position": "Company Officers", "department": "Camel Corps, King's African Rifles", "salary_min": 500, "salary_max": 550},
    {"name": "A. Skeen", "canonical_name": "Skeen, A.", "given_names": "A.", "surname": "Skeen", "position": "Company Officers", "department": "Camel Corps, King's African Rifles", "salary_min": 500, "salary_max": 550},
    {"name": "R. V. Lamont", "canonical_name": "Lamont, R. V.", "given_names": "R. V.", "surname": "Lamont", "position": "Company Officers", "department": "Camel Corps, King's African Rifles", "salary_min": 500, "salary_max": 550},
    {"name": "A. F. Phillimore", "canonical_name": "Phillimore, A. F.", "given_names": "A. F.", "surname": "Phillimore", "position": "Company Officers", "department": "Camel Corps, King's African Rifles", "salary_min": 500, "salary_max": 550},
    {"name": "J. C. C. Richardson", "canonical_name": "Richardson, J. C. C.", "given_names": "J. C. C.", "surname": "Richardson", "position": "Company Officers", "department": "Camel Corps, King's African Rifles", "salary_min": 500, "salary_max": 550},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Adjutant", "department": "Camel Corps, King's African Rifles", "salary_min": 550, "salary_max": 550, "allowances": "50l."},
    {"name": "W. R. Haymes", "canonical_name": "Haymes, W. R.", "given_names": "W. R.", "surname": "Haymes", "position": "Pay and Quartermaster", "department": "Camel Corps, King's African Rifles", "salary_min": 480, "salary_max": 720, "duty_allowance": 50, "military_rank": "Capt."},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
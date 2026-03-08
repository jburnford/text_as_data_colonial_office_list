"""
Sierra Leone Colonial Office List 1927 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1927

OFFICIALS = [
    {"name": "L. H. Macnaghten", "canonical_name": "Macnaghten, L. H.", "given_names": "L. H.", "surname": "Macnaghten", "position": "Director", "department": "Public Works Department - Sierra Leone", "salary_min": 800, "salary_max": 800},
    {"name": "J. F. L. Sawer", "canonical_name": "Sawer, J. F. L.", "given_names": "J. F. L.", "surname": "Sawer", "position": "Superintendent Mechanical Transport", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "R. A. Farquharson", "canonical_name": "Farquharson, R. A.", "given_names": "R. A.", "surname": "Farquharson", "position": "Director of Agriculture and Geologist", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.A.", "M.Sc.", "F.G.S."], "salary_min": 800, "salary_max": 800},
    {"name": "T. A. B. Cooksedge", "canonical_name": "Cooksedge, T. A. B.", "given_names": "T. A. B.", "surname": "Cooksedge", "position": "Veterinary Officer", "department": "Veterinary Department - Sierra Leone", "qualifications": ["M.R.C.V.S."], "salary_min": 600, "salary_max": 700, "military_rank": "Major"},
    {"name": "T. H. Gladstone", "canonical_name": "Gladstone, T. H.", "given_names": "T. H.", "surname": "Gladstone", "position": "Officer Commanding, Somaliland Camel Corps, K.A.R.", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "military_rank": "Major"},
    {"name": "R. F. Hornby", "canonical_name": "Hornby, R. F.", "given_names": "R. F.", "surname": "Hornby", "position": "Company Commander (Major)", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 775, "salary_max": 775, "military_rank": "Captain"},
    {"name": "G. B. Buchanan", "canonical_name": "Buchanan, G. B.", "given_names": "G. B.", "surname": "Buchanan", "position": "Company Commanders", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Lieut."},
    {"name": "K. G. Fernie", "canonical_name": "Fernie, K. G.", "given_names": "K. G.", "surname": "Fernie", "position": "Company Commanders", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Lieut."},
    {"name": "E. P. S. Shirley", "canonical_name": "Shirley, E. P. S.", "given_names": "E. P. S.", "surname": "Shirley", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "J. W. Kaye", "canonical_name": "Kaye, J. W.", "given_names": "J. W.", "surname": "Kaye", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "J. H. H. Williams", "canonical_name": "Williams, J. H. H.", "given_names": "J. H. H.", "surname": "Williams", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "N. W. Holbrook", "canonical_name": "Holbrook, N. W.", "given_names": "N. W.", "surname": "Holbrook", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Lieuts."},
    {"name": "E. Gerrard", "canonical_name": "Gerrard, E.", "given_names": "E.", "surname": "Gerrard", "position": "Company Officers", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 500, "salary_max": 550, "military_rank": "Capt."},
    {"name": "A. D. M. Lewis", "canonical_name": "Lewis, A. D. M.", "given_names": "A. D. M.", "surname": "Lewis", "position": "Adjutant", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 550, "salary_max": 550, "military_rank": "Lieut.", "allowances": "50l."},
    {"name": "W. R. Haymes", "canonical_name": "Haymes, W. R.", "given_names": "W. R.", "surname": "Haymes", "position": "Pay and Quartermaster", "department": "Camel Corps, King's African Rifles - Sierra Leone", "salary_min": 400, "salary_max": 600, "military_rank": "Capt."},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
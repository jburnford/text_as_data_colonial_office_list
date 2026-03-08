"""
Sierra Leone Colonial Office List 1921 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1921

OFFICIALS = [
    {"name": "L. H. Macnaghten", "canonical_name": "Macnaghten, L. H.", "given_names": "L. H.", "surname": "Macnaghten", "position": "Director", "department": "Public Works Department - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "O. L. Day", "canonical_name": "Day, O. L.", "given_names": "O. L.", "surname": "Day", "position": "Ford Car Mechanic", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "C. A. L. Howard", "canonical_name": "Howard, C. A. L.", "given_names": "C. A. L.", "surname": "Howard", "position": "Commandant", "department": "Camel Corps. - Sierra Leone", "salary_min": 800, "salary_max": 800, "honors": ["D.S.O.", "M.C."], "military_rank": "Lt.-Col."},
    {"name": "W. P. Lousada", "canonical_name": "Lousada, W. P.", "given_names": "W. P.", "surname": "Lousada", "position": "Company Commander", "department": "Camel Corps. - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Major"},
    {"name": "H. S. Pinder", "canonical_name": "Pinder, H. S.", "given_names": "H. S.", "surname": "Pinder", "position": "Company Commanders", "department": "Camel Corps. - Sierra Leone", "salary_min": 600, "salary_max": 600, "military_rank": "Bt.-Major", "honors": ["M.C."]},
    {"name": "E. J. W. Noakes", "canonical_name": "Noakes, E. J. W.", "given_names": "E. J. W.", "surname": "Noakes", "position": "Company Commanders", "department": "Camel Corps. - Sierra Leone", "salary_min": 600, "salary_max": 600, "military_rank": "Capt."},
    {"name": "S. G. Allden", "canonical_name": "Allden, S. G.", "given_names": "S. G.", "surname": "Allden", "position": "Company Officers", "department": "Camel Corps. - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Bt.-Major", "honors": ["D.S.O."]},
    {"name": "B. R. Newstead", "canonical_name": "Newstead, B. R.", "given_names": "B. R.", "surname": "Newstead", "position": "Company Officers", "department": "Camel Corps. - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Lieut.", "honors": ["D.S.O.", "M.C."]},
    {"name": "R. H. Rogers", "canonical_name": "Rogers, R. H.", "given_names": "R. H.", "surname": "Rogers", "position": "Company Officers", "department": "Camel Corps. - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Lieut."},
    {"name": "C. E. Ellington", "canonical_name": "Ellington, C. E.", "given_names": "C. E.", "surname": "Ellington", "position": "Company Officers", "department": "Camel Corps. - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Lieut."},
    {"name": "A. B. Russell", "canonical_name": "Russell, A. B.", "given_names": "A. B.", "surname": "Russell", "position": "Company Officers", "department": "Camel Corps. - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Lieut."},
    {"name": "A. M. Hutchinson", "canonical_name": "Hutchinson, A. M.", "given_names": "A. M.", "surname": "Hutchinson", "position": "Company Officers", "department": "Camel Corps. - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "2nd Lieut."},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Company Officers", "department": "Camel Corps. - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Adjutant", "department": "Camel Corps. - Sierra Leone", "salary_min": 400, "salary_max": 500, "allowances": "50l."},
    {"name": "W. R. Haymes", "canonical_name": "Haymes, W. R.", "given_names": "W. R.", "surname": "Haymes", "position": "Quartermaster", "department": "Camel Corps. - Sierra Leone", "salary_min": 400, "salary_max": 600, "military_rank": "Lieut."},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
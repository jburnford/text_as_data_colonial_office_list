"""
Gambia Colonial Office List 1928 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1928

OFFICIALS = [
    {"name": "W. Wise", "canonical_name": "Wise, W.", "given_names": "W.", "surname": "Wise", "position": "Commissioner of Works", "department": "Works Department - Gambia", "salary_min": 900, "salary_max": 1000, "qualifications": ["B.Sc.", "A.M.Inst.C.E.", "A.C.G.I.", "M.Inst. M. & Cy.E."]},
    {"name": "V. Kenniff", "canonical_name": "Kenniff, V.", "given_names": "V.", "surname": "Kenniff", "position": "Assistant Commissioner of Works", "department": "Works Department - Gambia", "acting_status": "acting"},
    {"name": "V. Kenniff", "canonical_name": "Kenniff, V.", "given_names": "V.", "surname": "Kenniff", "position": "District Engineer", "department": "Works Department - Gambia", "salary_min": 600, "salary_max": 750, "qualifications": ["B.E.", "A.M.I.E.", "A.M.Inst. C.E.", "M.Inst. M. & Cy. E."]},
    {"name": "H. E. Smythe", "canonical_name": "Smythe, H. E.", "given_names": "H. E.", "surname": "Smythe", "position": "District Engineer", "department": "Works Department - Gambia", "salary_min": 600, "salary_max": 750, "qualifications": ["B.E.", "A.M.I.E."]},
    {"name": "C. M. Teulon", "canonical_name": "Teulon, C. M.", "given_names": "C. M.", "surname": "Teulon", "position": "District Engineer", "department": "Works Department - Gambia", "salary_min": 600, "salary_max": 750, "qualifications": ["Assoc.M.Inst. M. & Cy.E."], "acting_status": "temporary"},
    {"name": "A. A. Ragg", "canonical_name": "Ragg, A. A.", "given_names": "A. A.", "surname": "Ragg", "position": "Mechanical Engineer", "department": "Works Department - Gambia", "salary_min": 600, "salary_max": 750},
    {"name": "H. Sabben", "canonical_name": "Sabben, H.", "given_names": "H.", "surname": "Sabben", "position": "Assistant Mechanical Engineer", "department": "Works Department - Gambia", "salary_min": 450, "salary_max": 550},
    {"name": "O. C. Ludolph", "canonical_name": "Ludolph, O. C.", "given_names": "O. C.", "surname": "Ludolph", "position": "Architect", "department": "Works Department - Gambia", "salary_min": 600, "salary_max": 750},
    {"name": "S. Brown", "canonical_name": "Brown, S.", "given_names": "S.", "surname": "Brown", "position": "Draughtsman", "department": "Works Department - Gambia", "salary_min": 400, "salary_max": 450, "acting_status": "temporary"},
    {"name": "H. A. Ragg", "canonical_name": "Ragg, H. A.", "given_names": "H. A.", "surname": "Ragg", "position": "Junior Draughtsman", "department": "Works Department - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "B. W. B. Cooper", "canonical_name": "Cooper, B. W. B.", "given_names": "B. W. B.", "surname": "Cooper", "position": "Junior Engineer", "department": "Works Department - Gambia", "salary_min": 450, "salary_max": 550, "qualifications": ["B.E."], "acting_status": "temporary"},
    {"name": "C. J. Thompson", "canonical_name": "Thompson, C. J.", "given_names": "C. J.", "surname": "Thompson", "position": "Engineering Assistant", "department": "Works Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "E. W. W. Harness", "canonical_name": "Harness, E. W. W.", "given_names": "E. W. W.", "surname": "Harness", "position": "Foreman of Works", "department": "Works Department - Gambia", "salary_min": 350, "salary_max": 450},
    {"name": "F. Midson", "canonical_name": "Midson, F.", "given_names": "F.", "surname": "Midson", "position": "Foreman of Works", "department": "Works Department - Gambia", "salary_min": 350, "salary_max": 450},
    {"name": "H. F. Tripp", "canonical_name": "Tripp, H. F.", "given_names": "H. F.", "surname": "Tripp", "position": "Foreman of Works", "department": "Works Department - Gambia", "salary_min": 75, "salary_max": 75},
    {"name": "J. Macnair", "canonical_name": "Macnair, J.", "given_names": "J.", "surname": "Macnair", "position": "Foreman of Works", "department": "Works Department - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "W. T. C. Edwards", "canonical_name": "Edwards, W. T. C.", "given_names": "W. T. C.", "surname": "Edwards", "position": "Overseer", "department": "Works Department - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "A. le B. F. Struthers", "canonical_name": "Struthers, A. le B. F.", "given_names": "A. le B. F.", "surname": "Struthers", "position": "Inspector of Water Supply", "department": "Works Department - Gambia", "salary_min": 300, "salary_max": 350},
    {"name": "C. W. R. Hooker", "canonical_name": "Hooker, C. W. R.", "given_names": "C. W. R.", "surname": "Hooker", "position": "First Class Clerk", "department": "Works Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "W. de B. Tate", "canonical_name": "Tate, W. de B.", "given_names": "W. de B.", "surname": "Tate", "position": "Second Class Clerk", "department": "Works Department - Gambia", "salary_min": 270, "salary_max": 400},
    {"name": "D. P. Cantion", "canonical_name": "Cantion, D. P.", "given_names": "D. P.", "surname": "Cantion", "position": "Third Class Clerk", "department": "Works Department - Gambia", "salary_min": 150, "salary_max": 270},
    {"name": "Miss E. Rostier", "canonical_name": "Rostier, E.", "given_names": "E.", "surname": "Rostier", "position": "Third Class Clerk", "department": "Works Department - Gambia", "salary_min": 150, "salary_max": 270},
    {"name": "H. R. Caten", "canonical_name": "Caten, H. R.", "given_names": "H. R.", "surname": "Caten", "position": "Third Class Clerk", "department": "Works Department - Gambia", "salary_min": 150, "salary_max": 270},
    {"name": "Miss L. Reay", "canonical_name": "Reay, L.", "given_names": "L.", "surname": "Reay", "position": "Third Class Clerk", "department": "Works Department - Gambia", "salary_min": 150, "salary_max": 270},
    {"name": "Jughan Singh", "canonical_name": "Singh, Jughan", "given_names": "Jughan", "surname": "Singh", "position": "Third Class Clerk", "department": "Works Department - Gambia", "salary_min": 150, "salary_max": 270},
    {"name": "G. Brown", "canonical_name": "Brown, G.", "given_names": "G.", "surname": "Brown", "position": "Third Class Clerk", "department": "Works Department - Gambia", "salary_min": 150, "salary_max": 270}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
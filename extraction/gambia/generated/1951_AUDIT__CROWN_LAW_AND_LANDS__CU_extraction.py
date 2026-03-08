"""
Gambia Colonial Office List 1951 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1951

OFFICIALS = [
    {"name": "K. S. Collins", "canonical_name": "Collins, K. S.", "given_names": "K. S.", "surname": "Collins", "position": "Principal Auditor", "department": "AUDIT - Gambia", "salary_scale": "B"},
    {"name": "G. T. C. Morris", "canonical_name": "Morris, G. T. C.", "given_names": "G. T. C.", "surname": "Morris", "position": "Auditor", "department": "AUDIT - Gambia", "salary_scale": "B", "honors": ["T.D."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Attorney General", "department": "CROWN LAW AND LANDS - Gambia", "salary_min": 1100, "salary_max": 1100},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Lands Officer", "department": "CROWN LAW AND LANDS - Gambia", "salary_scale": "A"},
    {"name": "S. H. Jones", "canonical_name": "Jones, S. H.", "given_names": "S. H.", "surname": "Jones", "position": "Collector of Customs", "department": "CUSTOMS - Gambia", "salary_scale": "E"},
    {"name": "E. B. Gibson", "canonical_name": "Gibson, E. B.", "given_names": "E. B.", "surname": "Gibson", "position": "Supervisor of Customs", "department": "CUSTOMS - Gambia", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Senior Education Officer", "department": "EDUCATION - Gambia", "salary_scale": "A"},
    {"name": "D. W. Grieve", "canonical_name": "Grieve, D. W.", "given_names": "D. W.", "surname": "Grieve", "position": "Education Officer", "department": "EDUCATION - Gambia", "salary_scale": "A"},
    {"name": "H. A. G. Hamilton", "canonical_name": "Hamilton, H. A. G.", "given_names": "H. A. G.", "surname": "Hamilton", "position": "Education Officer", "department": "EDUCATION - Gambia", "salary_scale": "A"},
    {"name": "A. T. W. Postlethwaite", "canonical_name": "Postlethwaite, A. T. W.", "given_names": "A. T. W.", "surname": "Postlethwaite", "position": "Education Officer", "department": "EDUCATION - Gambia", "salary_scale": "A"},
    {"name": "D. J. McCrae", "canonical_name": "McCrae, D. J.", "given_names": "D. J.", "surname": "McCrae", "position": "Education Officer", "department": "EDUCATION - Gambia", "salary_scale": "A"},
    {"name": "R. Y. Rule", "canonical_name": "Rule, R. Y.", "given_names": "R. Y.", "surname": "Rule", "position": "Education Officer", "department": "EDUCATION - Gambia", "salary_scale": "A"},
    {"name": "G. G. O'Halloran", "canonical_name": "O'Halloran, G. G.", "given_names": "G. G.", "surname": "O'Halloran", "position": "Education Officer", "department": "EDUCATION - Gambia", "salary_scale": "A"},
    {"name": "D. H. Blacksby", "canonical_name": "Blacksby, D. H.", "given_names": "D. H.", "surname": "Blacksby", "position": "Education Officer", "department": "EDUCATION - Gambia", "salary_scale": "A"},
    {"name": "Miss E. K. V. Knight", "canonical_name": "Knight, E. K. V.", "given_names": "E. K. V.", "surname": "Knight", "position": "Lady Education Officer", "department": "EDUCATION - Gambia", "salary_scale": "C"},
    {"name": "L. D. Smith", "canonical_name": "Smith, L. D.", "given_names": "L. D.", "surname": "Smith", "position": "Judge of the Supreme Court", "department": "JUDICIAL - Gambia", "salary_min": 1200, "salary_max": 1200, "expatriation_pay": 400},
    {"name": "S. J. Forster", "canonical_name": "Forster, S. J.", "given_names": "S. J.", "surname": "Forster", "position": "Colonial Magistrate", "department": "JUDICIAL - Gambia", "salary_scale": "A"},
    {"name": "D. Barrett", "canonical_name": "Barrett, D.", "given_names": "D.", "surname": "Barrett", "position": "Labour Officer", "department": "LABOUR - Gambia", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
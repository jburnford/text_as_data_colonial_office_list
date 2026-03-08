"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "N. L. Gordon", "canonical_name": "Gordon, N. L.", "given_names": "N. L.", "surname": "Gordon", "position": "Commissioner", "department": "Income Tax - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Commissioner", "department": "Income Tax - Sierra Leone", "salary_min": 1050, "salary_max": 1050},
    {"name": "W. C. A. Robinson", "canonical_name": "Robinson, W. C. A.", "given_names": "W. C. A.", "surname": "Robinson", "position": "Senior Assessment Officer", "department": "Income Tax - Sierra Leone", "salary_scale": "B"},
    {"name": "J. M. Walker", "canonical_name": "Walker, J. M.", "given_names": "J. M.", "surname": "Walker", "position": "Assessment Officer", "department": "Income Tax - Sierra Leone", "salary_scale": "B"},
    {"name": "H. T. J. Sawyerr", "canonical_name": "Sawyerr, H. T. J.", "given_names": "H. T. J.", "surname": "Sawyerr", "position": "Assessment Officer", "department": "Income Tax - Sierra Leone", "salary_scale": "B"},
    {"name": "G. E. Kayley", "canonical_name": "Kayley, G. E.", "given_names": "G. E.", "surname": "Kayley", "position": "Assessment Officer", "department": "Income Tax - Sierra Leone", "salary_scale": "B"},
    {"name": "A. C. Smith", "canonical_name": "Smith, A. C.", "given_names": "A. C.", "surname": "Smith", "position": "Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 2300, "salary_max": 2300, "military_rank": "M.C."},
    {"name": "E. S. Beoku-Betts", "canonical_name": "Beoku-Betts, E. S.", "given_names": "E. S.", "surname": "Beoku-Betts", "position": "Puisne Judges", "department": "Judicial - Sierra Leone", "salary_min": 1850, "salary_max": 1850, "honors": ["M.B.E."]},
    {"name": "H. H. Kingsley", "canonical_name": "Kingsley, H. H.", "given_names": "H. H.", "surname": "Kingsley", "position": "Puisne Judges", "department": "Judicial - Sierra Leone", "salary_min": 1850, "salary_max": 1850},
    {"name": "E. F. Luke", "canonical_name": "Luke, E. F.", "given_names": "E. F.", "surname": "Luke", "position": "Police Magistrates", "department": "Judicial - Sierra Leone", "salary_scale": "A"},
    {"name": "H. J. Lightfoot-Boston", "canonical_name": "Lightfoot-Boston, H. J.", "given_names": "H. J.", "surname": "Lightfoot-Boston", "position": "Police Magistrates", "department": "Judicial - Sierra Leone", "salary_scale": "A"},
    {"name": "S. B. Jones", "canonical_name": "Jones, S. B.", "given_names": "S. B.", "surname": "Jones", "position": "Police Magistrates", "department": "Judicial - Sierra Leone", "salary_scale": "A"},
    {"name": "A. Alhadi", "canonical_name": "Alhadi, A.", "given_names": "A.", "surname": "Alhadi", "position": "Master and Registrar", "department": "Judicial - Sierra Leone", "salary_scale": "A", "honors": ["M.B.E."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
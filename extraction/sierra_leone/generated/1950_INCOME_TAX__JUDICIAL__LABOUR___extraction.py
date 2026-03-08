"""
Sierra Leone Colonial Office List 1950 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1950

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Commissioner", "department": "INCOME TAX - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "W. C. A. Robinson", "canonical_name": "Robinson, W. C. A.", "given_names": "W. C. A.", "surname": "Robinson", "position": "Senior Assessment Officer", "department": "INCOME TAX - Sierra Leone", "salary_scale": "B"},
    {"name": "J. M. Walker", "canonical_name": "Walker, J. M.", "given_names": "J. M.", "surname": "Walker", "position": "Assessment Officer", "department": "INCOME TAX - Sierra Leone", "salary_scale": "B"},
    {"name": "W. Davies", "canonical_name": "Davies, W.", "given_names": "W.", "surname": "Davies", "position": "Assessment Officer", "department": "INCOME TAX - Sierra Leone", "salary_scale": "B"},
    {"name": "H. T. J. Sawyerr", "canonical_name": "Sawyerr, H. T. J.", "given_names": "H. T. J.", "surname": "Sawyerr", "position": "Assessment Officer", "department": "INCOME TAX - Sierra Leone", "salary_scale": "B"},
    {"name": "Sir John Lucie-Smith", "canonical_name": "Lucie-Smith, John", "given_names": "John", "surname": "Lucie-Smith", "position": "Chief Justice", "department": "JUDICIAL - Sierra Leone", "salary_min": 2150, "salary_max": 2150, "honors": ["O.B.E.", "V.D."]},
    {"name": "E. S. Beoku-Beits", "canonical_name": "Beoku-Beits, E. S.", "given_names": "E. S.", "surname": "Beoku-Beits", "position": "Puisne Judge", "department": "JUDICIAL - Sierra Leone", "salary_min": 1850, "salary_max": 1850, "honors": ["M.B.E."]},
    {"name": "H. H. Kingsley", "canonical_name": "Kingsley, H. H.", "given_names": "H. H.", "surname": "Kingsley", "position": "Puisne Judge", "department": "JUDICIAL - Sierra Leone", "salary_min": 1850, "salary_max": 1850},
    {"name": "E. F. Luke", "canonical_name": "Luke, E. F.", "given_names": "E. F.", "surname": "Luke", "position": "Police Magistrate", "department": "JUDICIAL - Sierra Leone", "salary_scale": "A"},
    {"name": "H. J. Lightfoot. Boston", "canonical_name": "Lightfoot, H. J.", "given_names": "H. J.", "surname": "Lightfoot", "position": "Police Magistrate", "department": "JUDICIAL - Sierra Leone", "salary_scale": "A", "location": "Boston"},
    {"name": "A. Alhadi", "canonical_name": "Alhadi, A.", "given_names": "A.", "surname": "Alhadi", "position": "Master and Registrar", "department": "JUDICIAL - Sierra Leone", "salary_scale": "A", "honors": ["M.B.E."]},
    {"name": "W. L. Bell", "canonical_name": "Bell, W. L.", "given_names": "W. L.", "surname": "Bell", "position": "Commissioner of Labour", "department": "LABOUR - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "J. I. Husband", "canonical_name": "Husband, J. I.", "given_names": "J. I.", "surname": "Husband", "position": "Labour Officer", "department": "LABOUR - Sierra Leone", "salary_scale": "A"},
    {"name": "F. W. Burn", "canonical_name": "Burn, F. W.", "given_names": "F. W.", "surname": "Burn", "position": "Labour Officer", "department": "LABOUR - Sierra Leone", "salary_scale": "A"},
    {"name": "G. M. Paterson", "canonical_name": "Paterson, G. M.", "given_names": "G. M.", "surname": "Paterson", "position": "Attorney-General", "department": "LEGAL - Sierra Leone", "salary_min": 1500, "salary_max": 1500, "honors": ["O.B.E."]},
    {"name": "P. G. Dickinson", "canonical_name": "Dickinson, P. G.", "given_names": "P. G.", "surname": "Dickinson", "position": "Solicitor-General", "department": "LEGAL - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "S. A. Benka-Coker", "canonical_name": "Benka-Coker, S. A.", "given_names": "S. A.", "surname": "Benka-Coker", "position": "Crown Counsel", "department": "LEGAL - Sierra Leone", "salary_scale": "A"},
    {"name": "M. C. Marke", "canonical_name": "Marke, M. C.", "given_names": "M. C.", "surname": "Marke", "position": "Crown Counsel", "department": "LEGAL - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
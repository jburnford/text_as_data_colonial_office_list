"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "J. D. Pollett", "canonical_name": "Pollett, J. D.", "given_names": "J. D.", "surname": "Pollett", "position": "Geologist", "department": "Geological - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "H. R. Burnham", "canonical_name": "Burnham, H. R.", "given_names": "H. R.", "surname": "Burnham", "position": "Deputy Commissioner", "department": "Income Tax - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "W. C. A. Robinson", "canonical_name": "Robinson, W. C. A.", "given_names": "W. C. A.", "surname": "Robinson", "position": "Assistant Commissioner", "department": "Income Tax - Sierra Leone", "salary_scale": "B"},
    {"name": "J. M. Walker", "canonical_name": "Walker, J. M.", "given_names": "J. M.", "surname": "Walker", "position": "Assessment Officer", "department": "Income Tax - Sierra Leone", "salary_scale": "B"},
    {"name": "W. Davies", "canonical_name": "Davies, W.", "given_names": "W.", "surname": "Davies", "position": "Assessment Officer", "department": "Income Tax - Sierra Leone", "salary_scale": "B"},
    {"name": "H. T. J. Sawyerr", "canonical_name": "Sawyerr, H. T. J.", "given_names": "H. T. J.", "surname": "Sawyerr", "position": "Tax Officer", "department": "Income Tax - Sierra Leone", "salary_scale": "B"},
    {"name": "J. A. Lucie-Smith", "canonical_name": "Lucie-Smith, J. A.", "given_names": "J. A.", "surname": "Lucie-Smith", "position": "Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 2150, "salary_max": 2150, "honors": ["O.B.E.", "V.D."]},
    {"name": "E. S. Beoku-Betts", "canonical_name": "Beoku-Betts, E. S.", "given_names": "E. S.", "surname": "Beoku-Betts", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "salary_min": 1700, "salary_max": 1700, "honors": ["M.B.E."]},
    {"name": "H. H. Kingsley", "canonical_name": "Kingsley, H. H.", "given_names": "H. H.", "surname": "Kingsley", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "salary_min": 1700, "salary_max": 1700},
    {"name": "O. J. V. Tuboku-Metzger", "canonical_name": "Tuboku-Metzger, O. J. V.", "given_names": "O. J. V.", "surname": "Tuboku-Metzger", "position": "Police Magistrate", "department": "Judicial - Sierra Leone", "salary_scale": "A", "honors": ["M.B.E."]},
    {"name": "E. F. Luke", "canonical_name": "Luke, E. F.", "given_names": "E. F.", "surname": "Luke", "position": "Police Magistrate", "department": "Judicial - Sierra Leone", "salary_scale": "A"},
    {"name": "H. J. Lightfoot-Boston", "canonical_name": "Lightfoot-Boston, H. J.", "given_names": "H. J.", "surname": "Lightfoot-Boston", "position": "Police Magistrate", "department": "Judicial - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
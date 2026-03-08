"""
Gambia Colonial Office List 1950 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1950

OFFICIALS = [
    {"name": "S. H. Jones", "canonical_name": "Jones, S. H.", "given_names": "S. H.", "surname": "Jones", "position": "Collector of Customs", "department": "Customs - The Gambia", "salary_scale": "B"},
    {"name": "E. B. Gibson", "canonical_name": "Gibson, E. B.", "given_names": "E. B.", "surname": "Gibson", "position": "Supervisor of Customs", "department": "Customs - The Gambia", "salary_scale": "C"},
    {"name": "D. Lang", "canonical_name": "Lang, D.", "given_names": "D.", "surname": "Lang", "position": "Senior Education Officer", "department": "Education - The Gambia", "salary_scale": "A"},
    {"name": "D. W. Grieve", "canonical_name": "Grieve, D. W.", "given_names": "D. W.", "surname": "Grieve", "position": "Education Officer", "department": "Education - The Gambia", "salary_scale": "A"},
    {"name": "P. B. Power", "canonical_name": "Power, P. B.", "given_names": "P. B.", "surname": "Power", "position": "Education Officer", "department": "Education - The Gambia", "salary_scale": "A"},
    {"name": "H. A. G. Hamilton", "canonical_name": "Hamilton, H. A. G.", "given_names": "H. A. G.", "surname": "Hamilton", "position": "Education Officer", "department": "Education - The Gambia", "salary_scale": "A"},
    {"name": "A. T. W. Postlethwaite", "canonical_name": "Postlethwaite, A. T. W.", "given_names": "A. T. W.", "surname": "Postlethwaite", "position": "Education Officer", "department": "Education - The Gambia", "salary_scale": "A"},
    {"name": "Miss E. K. V. Knight", "canonical_name": "Knight, E. K. V.", "given_names": "E. K. V.", "surname": "Knight", "position": "Lady Education Officer", "department": "Education - The Gambia", "salary_scale": "C"},
    {"name": "L. D. Smith", "canonical_name": "Smith, L. D.", "given_names": "L. D.", "surname": "Smith", "position": "Judge of the Supreme Court", "department": "Judicial - The Gambia", "salary_min": 1200, "salary_max": 1200, "expatriation_pay": 400},
    {"name": "S. J. Forster", "canonical_name": "Forster, S. J.", "given_names": "S. J.", "surname": "Forster", "position": "Colonial Magistrate", "department": "Judicial - The Gambia", "salary_min": 600, "salary_max": 600, "salary_scale": "A"},
    {"name": "D. Barrett", "canonical_name": "Barrett, D.", "given_names": "D.", "surname": "Barrett", "position": "Labour Officer", "department": "Labour - The Gambia", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
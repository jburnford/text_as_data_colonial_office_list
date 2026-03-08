"""
Gambia Colonial Office List 1949 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1949

OFFICIALS = [
    {"name": "S. H. Jones", "canonical_name": "Jones, S. H.", "given_names": "S. H.", "surname": "Jones", "position": "Collector of Customs", "department": "Customs - Gambia", "salary_scale": "B"},
    {"name": "E. B. Gibson", "canonical_name": "Gibson, E. B.", "given_names": "E. B.", "surname": "Gibson", "position": "Supervisor of Customs", "department": "Customs - Gambia", "salary_scale": "C"},
    {"name": "D. Lang", "canonical_name": "Lang, D.", "given_names": "D.", "surname": "Lang", "position": "Senior Education Officer", "department": "Education - Gambia", "salary_scale": "A"},
    {"name": "D. W. Grieve", "canonical_name": "Grieve, D. W.", "given_names": "D. W.", "surname": "Grieve", "position": "Education Officer (Principal, Armitage School)", "department": "Education - Gambia", "salary_scale": "A"},
    {"name": "Miss E. K. V. Knight", "canonical_name": "Knight, E. K. V.", "given_names": "E. K. V.", "surname": "Knight", "position": "Lady Education Officer", "department": "Education - Gambia", "salary_scale": "C"},
    {"name": "L. D. Smith", "canonical_name": "Smith, L. D.", "given_names": "L. D.", "surname": "Smith", "position": "Judge of the Supreme Court", "department": "Judicial - Gambia", "salary_min": 1200, "salary_max": 1200, "expatriation_pay": 400},
    {"name": "S. J. Forster", "canonical_name": "Forster, S. J.", "given_names": "S. J.", "surname": "Forster", "position": "Colonial Magistrate", "department": "Judicial - Gambia", "salary_min": 600, "salary_scale": "A"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sheriff", "department": "Judicial - Gambia"},
    {"name": "D. Barrett", "canonical_name": "Barrett, D.", "given_names": "D.", "surname": "Barrett", "position": "Labour Officer", "department": "Labour - Gambia", "salary_scale": "A"},
    {"name": "M. Messer-Bennetts", "canonical_name": "Messer-Bennetts, M.", "given_names": "M.", "surname": "Messer-Bennetts", "position": "Lands Officer", "department": "Land and Survey - Gambia", "salary_scale": "A"},
    {"name": "B. A. McArthur-Davis", "canonical_name": "McArthur-Davis, B. A.", "given_names": "B. A.", "surname": "McArthur-Davis", "position": "Surveyor", "department": "Land and Survey - Gambia", "salary_scale": "A"},
    {"name": "J. P. Murphy", "canonical_name": "Murphy, J. P.", "given_names": "J. P.", "surname": "Murphy", "position": "Attorney General", "department": "Legal - Gambia", "salary_min": 1100, "salary_max": 1100, "expatriation_pay": 350}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
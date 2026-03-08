"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "R. H. Bunting", "canonical_name": "Bunting, R. H.", "given_names": "R. H.", "surname": "Bunting",
     "position": "Government Mycologist and Assistant Director of Agriculture (Scientific)", "department": "Agriculture Department - Gold Coast",
     "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["F.L.S."]},
    {"name": "W. H. Patterson", "canonical_name": "Patterson, W. H.", "given_names": "W. H.", "surname": "Patterson",
     "position": "Government Entomologist", "department": "Agriculture Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "seniority_allowance": 72},
    {"name": "H. A. Dade", "canonical_name": "Dade, H. A.", "given_names": "H. A.", "surname": "Dade",
     "position": "Assistant Mycologist", "department": "Agriculture Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "seniority_allowance": 72, "qualifications": ["A.R.C.S."]},
    {"name": "G. S. Cotterell", "canonical_name": "Cotterell, G. S.", "given_names": "G. S.", "surname": "Cotterell",
     "position": "Assistant Entomologist", "department": "Agriculture Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "seniority_allowance": 72, "qualifications": ["A.R.C.S.", "F.E.S."]},
    {"name": "R. Coull", "canonical_name": "Coull, R.", "given_names": "R.", "surname": "Coull",
     "position": "Agricultural Chemist", "department": "Agriculture Department - Gold Coast", "salary_min": 600, "salary_max": 920,
     "seniority_allowance": 72, "qualifications": ["B.Sc."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
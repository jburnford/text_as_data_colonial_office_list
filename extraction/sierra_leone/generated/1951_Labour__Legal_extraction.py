"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "W. L. Bell", "canonical_name": "Bell, W. L.", "given_names": "W. L.", "surname": "Bell", "position": "Commissioner of Labour", "department": "Labour - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "J. I. Husband", "canonical_name": "Husband, J. I.", "given_names": "J. I.", "surname": "Husband", "position": "Labour Officer", "department": "Labour - Sierra Leone", "salary_scale": "A"},
    {"name": "F. W. Burn", "canonical_name": "Burn, F. W.", "given_names": "F. W.", "surname": "Burn", "position": "Labour Officer", "department": "Labour - Sierra Leone", "salary_scale": "A"},
    {"name": "W. J. Dupigny", "canonical_name": "Dupigny, W. J.", "given_names": "W. J.", "surname": "Dupigny", "position": "Labour Officer", "department": "Labour - Sierra Leone", "salary_scale": "A"},
    {"name": "G. S. Panda", "canonical_name": "Panda, G. S.", "given_names": "G. S.", "surname": "Panda", "position": "Labour Officer", "department": "Labour - Sierra Leone", "salary_scale": "A"},
    {"name": "G. M. Paterson", "canonical_name": "Paterson, G. M.", "given_names": "G. M.", "surname": "Paterson", "position": "Attorney-General", "department": "Legal - Sierra Leone", "salary_min": 1500, "salary_max": 1500, "honors": ["O.B.E.", "K.C."]},
    {"name": "P. G. Dickinson", "canonical_name": "Dickinson, P. G.", "given_names": "P. G.", "surname": "Dickinson", "position": "Solicitor-General", "department": "Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Legal Draftsman", "department": "Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "S. A. Benka-Coker", "canonical_name": "Benka-Coker, S. A.", "given_names": "S. A.", "surname": "Benka-Coker", "position": "Crown Counsel", "department": "Legal - Sierra Leone", "salary_scale": "A"},
    {"name": "M. C. Marke", "canonical_name": "Marke, M. C.", "given_names": "M. C.", "surname": "Marke", "position": "Crown Counsel", "department": "Legal - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
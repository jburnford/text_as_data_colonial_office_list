"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "W. D. Jackson", "canonical_name": "Jackson, W. D.", "given_names": "W. D.", "surname": "Jackson", "position": "Superintendent", "department": "Rottnest Prison Department. - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "and quarters"},
    {"name": "H. C. Barnett", "canonical_name": "Barnett, H. C.", "given_names": "H. C.", "surname": "Barnett", "position": "Medical Officer", "department": "Rottnest Prison Department. - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "H. C. Courderot", "canonical_name": "Courderot, H. C.", "given_names": "H. C.", "surname": "Courderot", "position": "Clerk and Superintendent of Salt Works", "department": "Rottnest Prison Department. - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "R. Walcott", "canonical_name": "Walcott, R.", "given_names": "R.", "surname": "Walcott", "position": "School Teacher", "department": "Rottnest Prison Department. - Gambia", "salary_min": 75, "salary_max": 75},
    {"name": "R. Pether", "canonical_name": "Pether, R.", "given_names": "R.", "surname": "Pether", "position": "Government Printer", "department": "Printing Department. - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "A. Curtis", "canonical_name": "Curtis, A.", "given_names": "A.", "surname": "Curtis", "position": "Clerk", "department": "Printing Department. - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "Joshua Mills", "canonical_name": "Mills, Joshua", "given_names": "Joshua", "surname": "Mills", "position": "Champion Bay District", "department": "Inspectors of Sheep Department. - Gambia", "salary_min": 150, "salary_max": 150, "allowances": "and allowance 100l.", "location": "Champion Bay District"},
    {"name": "R. Miller", "canonical_name": "Miller, R.", "given_names": "R.", "surname": "Miller", "position": "Assistant Inspector", "department": "Inspectors of Sheep Department. - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "J. F. Morrell", "canonical_name": "Morrell, J. F.", "given_names": "J. F.", "surname": "Morrell", "position": "Irwin District", "department": "Inspectors of Sheep Department. - Gambia", "salary_min": 150, "salary_max": 150, "allowances": "and allowance 100l.", "location": "Irwin District"},
    {"name": "J. M. Craig", "canonical_name": "Craig, J. M.", "given_names": "J. M.", "surname": "Craig", "position": "Central District", "department": "Inspectors of Sheep Department. - Gambia", "salary_min": 150, "salary_max": 150, "allowances": "and allowance 100l.", "location": "Central District"},
    {"name": "J. Logue", "canonical_name": "Logue, J.", "given_names": "J.", "surname": "Logue", "position": "South-west District", "department": "Inspectors of Sheep Department. - Gambia", "salary_min": 150, "salary_max": 150, "allowances": "and allowance 100l.", "location": "South-west District"},
    {"name": "R. Warburton", "canonical_name": "Warburton, R.", "given_names": "R.", "surname": "Warburton", "position": "South-east District", "department": "Inspectors of Sheep Department. - Gambia", "salary_min": 150, "salary_max": 150, "allowances": "and allowance 100l.", "location": "South-east District"},
    {"name": "G. Eliot", "canonical_name": "Eliot, G.", "given_names": "G.", "surname": "Eliot", "position": "Assistant Inspector", "department": "Inspectors of Sheep Department. - Gambia", "salary_min": 12, "salary_max": 12, "location": "Fremantle"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
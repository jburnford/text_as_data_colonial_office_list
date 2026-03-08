"""
Gambia Colonial Office List 1928 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1928

OFFICIALS = [
    {"name": "J. D. Tothill", "canonical_name": "Tothill, J. D.", "given_names": "J. D.", "surname": "Tothill", "position": "Superintendent of Agriculture", "department": "Department of Agriculture - Gambia", "salary_min": 1000, "salary_max": 1000, "qualifications": ["D.Sc."]},
    {"name": "E. S. Gordon", "canonical_name": "Gordon, E. S.", "given_names": "E. S.", "surname": "Gordon", "position": "Inspector of Produce", "department": "Department of Agriculture - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "H. W. Simmonds", "canonical_name": "Simmonds, H. W.", "given_names": "H. W.", "surname": "Simmonds", "position": "Government Entomologist", "department": "Department of Agriculture - Gambia", "salary_min": 600, "salary_max": 700, "qualifications": ["F.E.S."]},
    {"name": "C. L. Southall", "canonical_name": "Southall, C. L.", "given_names": "C. L.", "surname": "Southall", "position": "Government Chemist", "department": "Department of Agriculture - Gambia", "salary_min": 550, "salary_max": 750, "qualifications": ["B.Sc.", "A.I.C."]},
    {"name": "J. G. C. Campbell", "canonical_name": "Campbell, J. G. C.", "given_names": "J. G. C.", "surname": "Campbell", "position": "Government Mycologist", "department": "Department of Agriculture - Gambia", "salary_min": 550, "salary_max": 750, "qualifications": ["B.Sc."]},
    {"name": "C. R. Turbet", "canonical_name": "Turbet, C. R.", "given_names": "C. R.", "surname": "Turbet", "position": "Veterinary Surgeon", "department": "Department of Agriculture - Gambia", "salary_min": 600, "salary_max": 600, "qualifications": ["B.V.Sc."]},
    {"name": "W. A. Carr Fraser", "canonical_name": "Fraser, W. A. Carr", "given_names": "W. A. Carr", "surname": "Fraser", "position": "Veterinary Surgeon", "department": "Department of Agriculture - Gambia", "salary_min": 600, "salary_max": 600, "qualifications": ["B.V.Sc."]},
    {"name": "W. G. Bennett", "canonical_name": "Bennett, W. G.", "given_names": "W. G.", "surname": "Bennett", "position": "Veterinary Surgeon", "department": "Department of Agriculture - Gambia", "salary_min": 500, "salary_max": 600, "qualifications": ["B.V.Sc."]},
    {"name": "A. B. Ackland", "canonical_name": "Ackland, A. B.", "given_names": "A. B.", "surname": "Ackland", "position": "Clerk, First Class", "department": "Department of Agriculture - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "M. A. Formyth", "canonical_name": "Formyth, M. A.", "given_names": "M. A.", "surname": "Formyth", "position": "Second Class Clerk", "department": "Department of Agriculture - Gambia", "salary_min": 270, "salary_max": 400},
    {"name": "Miss G. Riemen-schneider", "canonical_name": "Riemen-schneider, G.", "given_names": "G.", "surname": "Riemen-schneider", "position": "Temporary Clerk, Third Class", "department": "Department of Agriculture - Gambia", "salary_min": 150, "salary_max": 270},
    {"name": "G. H. V. Saunders", "canonical_name": "Saunders, G. H. V.", "given_names": "G. H. V.", "surname": "Saunders", "position": "Inspector of Plantations", "department": "Department of Agriculture - Gambia", "salary_min": 270, "salary_max": 400},
    {"name": "C. T. McNamara", "canonical_name": "McNamara, C. T.", "given_names": "C. T.", "surname": "McNamara", "position": "Inspector of Plantations", "department": "Department of Agriculture - Gambia", "salary_min": 270, "salary_max": 400},
    {"name": "J. White", "canonical_name": "White, J.", "given_names": "J.", "surname": "White", "position": "Inspector of Plantations", "department": "Department of Agriculture - Gambia", "salary_min": 270, "salary_max": 400},
    {"name": "E. Whittenbury", "canonical_name": "Whittenbury, E.", "given_names": "E.", "surname": "Whittenbury", "position": "Inspector of Plantations", "department": "Department of Agriculture - Gambia", "salary_min": 200, "salary_max": 200},
    {"name": "J. P. Tarby", "canonical_name": "Tarby, J. P.", "given_names": "J. P.", "surname": "Tarby", "position": "Manager, Rice Mill", "department": "Department of Agriculture - Gambia", "salary_min": 500, "salary_max": 500}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
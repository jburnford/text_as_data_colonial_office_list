"""
Gambia Colonial Office List 1952 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1952

OFFICIALS = [
    {"name": "E. R. Ward", "canonical_name": "Ward, E. R.", "given_names": "E. R.", "surname": "Ward", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Gambia", "salary_min": 1350, "expatriation_pay": 400, "duty_allowance": 100, "honors": ["C.M.G."]},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Financial Secretary", "department": "Financial Secretary's Office - Gambia", "salary_min": 1175, "honors": ["O.B.E."]},
    {"name": "G. H. Smith", "canonical_name": "Smith, G. H.", "given_names": "G. H.", "surname": "Smith", "position": "Senior Commissioner", "department": "Commissioner's Office - Gambia", "salary_min": 1175},
    {"name": "E. B. W. Carrol", "canonical_name": "Carrol, E. B. W.", "given_names": "E. B. W.", "surname": "Carrol", "position": "Accountant-General", "department": "Accountant General's Office - Gambia", "salary_scale": "B", "honors": ["O.B.E."]},
    {"name": "C. B. Garnett", "canonical_name": "Garnett, C. B.", "given_names": "C. B.", "surname": "Garnett", "position": "Director of Development and Agriculture", "department": "Development and Agriculture - Gambia", "salary_min": 1350},
    {"name": "G. T. C. Morris", "canonical_name": "Morris, G. T. C.", "given_names": "G. T. C.", "surname": "Morris", "position": "Principal Auditor", "department": "Auditor's Office - Gambia", "salary_scale": "B", "honors": ["T.D."]},
    {"name": "A. C. Spurling", "canonical_name": "Spurling, A. C.", "given_names": "A. C.", "surname": "Spurling", "position": "Attorney-General", "department": "Attorney-General's Office - Gambia", "salary_min": 1175},
    {"name": "S. H. Jones", "canonical_name": "Jones, S. H.", "given_names": "S. H.", "surname": "Jones", "position": "Collector of Customs", "department": "Customs - Gambia", "salary_scale": "B"},
    {"name": "J. W. Forrest", "canonical_name": "Forrest, J. W.", "given_names": "J. W.", "surname": "Forrest", "position": "Senior Education Officer", "department": "Education - Gambia", "salary_scale": "A"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Judge of the Supreme Court", "department": "Judicial - Gambia", "salary_min": 1200, "expatriation_pay": 400},
    {"name": "E. D. N’Jie", "canonical_name": "N’Jie, E. D.", "given_names": "E. D.", "surname": "N’Jie", "position": "Labour Officer", "department": "Labour - Gambia", "salary_scale": "A"},
    {"name": "E. J. Bury", "canonical_name": "Bury, E. J.", "given_names": "E. J.", "surname": "Bury", "position": "Director of Medical Services", "department": "Medical Services - Gambia", "salary_min": 1350},
    {"name": "G. D. Maydon", "canonical_name": "Maydon, G. D.", "given_names": "G. D.", "surname": "Maydon", "position": "Superintendent of Police", "department": "Police - Gambia", "salary_scale": "B"},
    {"name": "R. J. S. Pearce", "canonical_name": "Pearce, R. J. S.", "given_names": "R. J. S.", "surname": "Pearce", "position": "Superintendent of Prisons", "department": "Prisons - Gambia", "salary_scale": "B"},
    {"name": "E. C. Sowe", "canonical_name": "Sowe, E. C.", "given_names": "E. C.", "surname": "Sowe", "position": "Postmaster-General", "department": "Post Office - Gambia", "salary_scale": "B", "honors": ["M.B.E."]},
    {"name": "J. A. George", "canonical_name": "George, J. A.", "given_names": "J. A.", "surname": "George", "position": "Government Printer", "department": "Printing - Gambia", "salary_scale": "C"},
    {"name": "G. Peters", "canonical_name": "Peters, G.", "given_names": "G.", "surname": "Peters", "position": "Information Officer", "department": "Information - Gambia", "salary_scale": "B"},
    {"name": "K. Wilson", "canonical_name": "Wilson, K.", "given_names": "K.", "surname": "Wilson", "position": "Director of Public Works", "department": "Public Works - Gambia", "salary_min": 1100},
    {"name": "W. A. Small", "canonical_name": "Small, W. A.", "given_names": "W. A.", "surname": "Small", "position": "Superintendent of Surveys", "department": "Surveys - Gambia", "salary_scale": "B", "honors": ["M.B.E."]},
    {"name": "A. Fulton", "canonical_name": "Fulton, A.", "given_names": "A.", "surname": "Fulton", "position": "Director of Veterinary Services", "department": "Veterinary Services - Gambia", "salary_min": 1200}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
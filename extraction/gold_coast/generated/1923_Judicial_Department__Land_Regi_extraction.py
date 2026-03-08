"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Sir P. C. Smyly", "canonical_name": "Smyly, Sir P. C.", "given_names": "P. C.", "surname": "Smyly",
     "position": "Chief Justice", "department": "Judicial Department - Gold Coast", "salary_min": 2000, "salary_max": 2000,
     "duty_allowance": 400, "honors": ["Kt."], "qualifications": ["LL.D."]},
    {"name": "E. R. Logan", "canonical_name": "Logan, E. R.", "given_names": "E. R.", "surname": "Logan",
     "position": "Puisne Judge", "department": "Judicial Department - Gold Coast", "salary_min": 1400, "salary_max": 1400,
     "duty_allowance": 280},
    {"name": "K. J. Beatty", "canonical_name": "Beatty, K. J.", "given_names": "K. J.", "surname": "Beatty",
     "position": "Puisne Judge", "department": "Judicial Department - Gold Coast", "salary_min": 1400, "salary_max": 1400,
     "duty_allowance": 280},
    {"name": "R. E. Hall", "canonical_name": "Hall, R. E.", "given_names": "R. E.", "surname": "Hall",
     "position": "Puisne Judge", "department": "Judicial Department - Gold Coast", "salary_min": 1400, "salary_max": 1400,
     "duty_allowance": 280},
    {"name": "L. C. Dalton", "canonical_name": "Dalton, L. C.", "given_names": "L. C.", "surname": "Dalton",
     "position": "Puisne Judge", "department": "Judicial Department - Gold Coast", "salary_min": 1400, "salary_max": 1400,
     "duty_allowance": 280},
    {"name": "A. White", "canonical_name": "White, A.", "given_names": "A.", "surname": "White",
     "position": "Chief Registrar and Sheriff", "department": "Judicial Department - Gold Coast", "salary_min": 720, "salary_max": 960,
     "allowances": "120l. personal allowance and fees as Official Administrator", "qualifications": [],
     "acting_status": None},
    {"name": "M. T. Hincks", "canonical_name": "Hincks, M. T.", "given_names": "M. T.", "surname": "Hincks",
     "position": "European Police Magistrate", "department": "Judicial Department - Gold Coast", "salary_min": 720, "salary_max": 960},
    {"name": "C. A. Good", "canonical_name": "Good, C. A.", "given_names": "C. A.", "surname": "Good",
     "position": "European Police Magistrate", "department": "Judicial Department - Gold Coast", "salary_min": 720, "salary_max": 960},
    {"name": "C. E. W. Bannerman", "canonical_name": "Bannerman, C. E. W.", "given_names": "C. E. W.", "surname": "Bannerman",
     "position": "African Police Magistrate", "department": "Judicial Department - Gold Coast", "salary_min": 600, "salary_max": 840},
    {"name": "W. A. Renner", "canonical_name": "Renner, W. A.", "given_names": "W. A.", "surname": "Renner",
     "position": "African Police Magistrate", "department": "Judicial Department - Gold Coast", "salary_min": 600, "salary_max": 840},
    {"name": "Frank Vardon", "canonical_name": "Vardon, Frank", "given_names": "Frank", "surname": "Vardon",
     "position": "Divisional Court Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 264, "salary_max": 360},
    {"name": "J. B. Aikins", "canonical_name": "Aikins, J. B.", "given_names": "J. B.", "surname": "Aikins",
     "position": "Divisional Court Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 264, "salary_max": 360},
    {"name": "R. A. Crabbe", "canonical_name": "Crabbe, R. A.", "given_names": "R. A.", "surname": "Crabbe",
     "position": "Divisional Court Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 264, "salary_max": 360},
    {"name": "R. W. H. Wilkinson", "canonical_name": "Wilkinson, R. W. H.", "given_names": "R. W. H.", "surname": "Wilkinson",
     "position": "Attorney-General", "department": "Law Officers' Department - Gold Coast", "salary_min": 1500, "salary_max": 1500,
     "duty_allowance": 300},
    {"name": "C. Carnegie Brown", "canonical_name": "Brown, C. Carnegie", "given_names": "C. Carnegie", "surname": "Brown",
     "position": "Solicitor-General", "department": "Law Officers' Department - Gold Coast", "salary_min": 1100, "salary_max": 1100,
     "duty_allowance": 220},
    {"name": "J. J. Treacy", "canonical_name": "Treacy, J. J.", "given_names": "J. J.", "surname": "Treacy",
     "position": "European Crown Counsel", "department": "Law Officers' Department - Gold Coast", "salary_min": 720, "salary_max": 960},
    {"name": "J. Aitken", "canonical_name": "Aitken, J.", "given_names": "J.", "surname": "Aitken",
     "position": "European Crown Counsel", "department": "Law Officers' Department - Gold Coast", "salary_min": 720, "salary_max": 960},
    {"name": "L. E. V. McCarthy", "canonical_name": "McCarthy, L. E. V.", "given_names": "L. E. V.", "surname": "McCarthy",
     "position": "African Crown Counsel", "department": "Law Officers' Department - Gold Coast", "salary_min": 720, "salary_max": 960},
    {"name": "Odartey Golightly", "canonical_name": "Golightly, Odartey", "given_names": "Odartey", "surname": "Golightly",
     "position": "Chief Clerk", "department": "Law Officers' Department - Gold Coast", "salary_min": 300, "salary_max": 396}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
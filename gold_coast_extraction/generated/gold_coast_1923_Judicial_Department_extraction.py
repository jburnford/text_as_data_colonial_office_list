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
     "allowances": "72l. seniority allowance and fees as Official Administrator; also Principal Registrar of Marriages, Registrar of Companies, Patents and Trade Marks"},
    {"name": "M. T. Hincks", "canonical_name": "Hincks, M. T.", "given_names": "M. T.", "surname": "Hincks",
     "position": "European Police Magistrate", "department": "Judicial Department - Gold Coast", "salary_min": 720, "salary_max": 960,
     "allowances": "72l. seniority allowance"},
    {"name": "C. A. Good", "canonical_name": "Good, C. A.", "given_names": "C. A.", "surname": "Good",
     "position": "European Police Magistrate", "department": "Judicial Department - Gold Coast", "salary_min": 720, "salary_max": 960,
     "allowances": "72l. seniority allowance"},
    {"name": "C. E. W. Bannerman", "canonical_name": "Bannerman, C. E. W.", "given_names": "C. E. W.", "surname": "Bannerman",
     "position": "African Police Magistrate", "department": "Judicial Department - Gold Coast", "salary_min": 600, "salary_max": 840,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "W. A. Renner", "canonical_name": "Renner, W. A.", "given_names": "W. A.", "surname": "Renner",
     "position": "African Police Magistrate", "department": "Judicial Department - Gold Coast", "salary_min": 600, "salary_max": 840,
     "allowances": "72l. seniority allowance from 720l."},
    {"name": "Frank Vardon", "canonical_name": "Vardon, Frank", "given_names": "Frank", "surname": "Vardon",
     "position": "Divisional Court Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 264, "salary_max": 360},
    {"name": "J. B. Aikins", "canonical_name": "Aikins, J. B.", "given_names": "J. B.", "surname": "Aikins",
     "position": "Divisional Court Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 264, "salary_max": 360},
    {"name": "R. A. Crabbe", "canonical_name": "Crabbe, R. A.", "given_names": "R. A.", "surname": "Crabbe",
     "position": "Divisional Court Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 264, "salary_max": 360},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "A. C. Onslow", "canonical_name": "Onslow, A. C.", "given_names": "A. C.", "surname": "Onslow", "position": "Chief Justice", "department": "Judicial Department - Gambia", "salary_min": 1000, "salary_max": 1000},
    {"name": "A. P. Hensman", "canonical_name": "Hensman, A. P.", "given_names": "A. P.", "surname": "Hensman", "position": "Attorney-General", "department": "Judicial Department - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "Geo. W. Leake", "canonical_name": "Leake, Geo. W.", "given_names": "Geo. W.", "surname": "Leake", "position": "Crown Solicitor", "department": "Judicial Department - Gambia", "salary_min": 250, "salary_max": 250, "qualifications": ["Q.C."]},
    {"name": "James Cowan", "canonical_name": "Cowan, James", "given_names": "James", "surname": "Cowan", "position": "Registrar, and Master of Supreme Court, &c.", "department": "Judicial Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "James Roe", "canonical_name": "Roe, James", "given_names": "James", "surname": "Roe", "position": "Sheriff", "department": "Judicial Department - Gambia", "salary_min": 800, "salary_max": 800},
    {"name": "H. Richards", "canonical_name": "Richards, H.", "given_names": "H.", "surname": "Richards", "position": "Clerk to Chief Justice", "department": "Judicial Department - Gambia", "salary_min": 90, "salary_max": 90},
    {"name": "F. W. Pentlow", "canonical_name": "Pentlow, F. W.", "given_names": "F. W.", "surname": "Pentlow", "position": "Clerk to Attorney-General and Crown Solicitor", "department": "Judicial Department - Gambia", "salary_min": 200, "salary_max": 200},
    {"name": "G. C. Knight", "canonical_name": "Knight, G. C.", "given_names": "G. C.", "surname": "Knight", "position": "Clerk to Registrar of Supreme Court", "department": "Judicial Department - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "F. Wheeler", "canonical_name": "Wheeler, F.", "given_names": "F.", "surname": "Wheeler", "position": "Bailiff and Head Constable", "department": "Judicial Department - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "E. H. Lawrence", "canonical_name": "Lawrence, E. H.", "given_names": "E. H.", "surname": "Lawrence", "position": "Chairmen of Quarter Sessions and Resident Magistrates North District", "department": "Judicial Department - Gambia", "salary_min": 415, "salary_max": 415, "allowances": "and allowance 50l."},
    {"name": "G. Eliot", "canonical_name": "Eliot, G.", "given_names": "G.", "surname": "Eliot", "position": "Victoria District", "department": "Judicial Department - Gambia", "salary_min": 585, "salary_max": 585, "allowances": "and allowance with quarters, 100l."},
    {"name": "R. C. Loftie", "canonical_name": "Loftie, R. C.", "given_names": "R. C.", "surname": "Loftie", "position": "Plantagenet District", "department": "Judicial Department - Gambia", "salary_min": 500, "salary_max": 500, "allowances": "and allowance 50l."},
    {"name": "Perth and Swan", "canonical_name": "Swan, Perth and", "given_names": "Perth and", "surname": "Swan", "position": "Police Magistrate", "department": "Judicial Department - Gambia", "salary_min": 500, "salary_max": 500},
    {"name": "R. Fairbairn", "canonical_name": "Fairbairn, R.", "given_names": "R.", "surname": "Fairbairn", "position": "Sussex District", "department": "Judicial Department - Gambia", "salary_min": 315, "salary_max": 315, "allowances": "and allowance 50l."},
    {"name": "W. P. Clifton", "canonical_name": "Clifton, W. P.", "given_names": "W. P.", "surname": "Clifton", "position": "Wellington District", "department": "Judicial Department - Gambia", "salary_min": 325, "salary_max": 325, "allowances": "and allowance 50l."},
    {"name": "J. G. Murray", "canonical_name": "Murray, J. G.", "given_names": "J. G.", "surname": "Murray", "position": "Murray District", "department": "Judicial Department - Gambia", "salary_min": 155, "salary_max": 155, "allowances": "and allowance 50l."},
    {"name": "J. C. Rosseloty", "canonical_name": "Rosseloty, J. C.", "given_names": "J. C.", "surname": "Rosseloty", "position": "Williams District", "department": "Judicial Department - Gambia", "salary_min": 170, "salary_max": 170, "allowances": "and allowance 50l."},
    {"name": "J. G. Slade", "canonical_name": "Slade, J. G.", "given_names": "J. G.", "surname": "Slade", "position": "Fremantle District", "department": "Judicial Department - Gambia", "salary_min": 405, "salary_max": 405},
    {"name": "O. Burt", "canonical_name": "Burt, O.", "given_names": "O.", "surname": "Burt", "position": "Toodyay District", "department": "Judicial Department - Gambia", "salary_min": 275, "salary_max": 275, "allowances": "and allowance 50l."},
    {"name": "W. Cowan", "canonical_name": "Cowan, W.", "given_names": "W.", "surname": "Cowan", "position": "York District", "department": "Judicial Department - Gambia", "salary_min": 325, "salary_max": 325, "allowances": "and allowance 50l."},
    {"name": "C. D. Voss", "canonical_name": "Voss, C. D.", "given_names": "C. D.", "surname": "Voss", "position": "Gascoyne, Stipendiary Itinerant Magistrate", "department": "Judicial Department - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "and allowance 75l."},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Kimberley", "department": "Judicial Department - Gambia", "salary_min": 200, "salary_max": 200, "allowances": "and 75l. allowance."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
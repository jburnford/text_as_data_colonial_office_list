"""
Sierra Leone Colonial Office List 1940 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1940

OFFICIALS = [
    {"name": "H. G. Veale", "canonical_name": "Veale, H. G.", "given_names": "H. G.", "surname": "Veale", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 750, "salary_max": 920},
    {"name": "H. Bowles", "canonical_name": "Bowles, H.", "given_names": "H.", "surname": "Bowles", "position": "Government Pilot", "department": "Port and Marine Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "S. G. Randall", "canonical_name": "Randall, S. G.", "given_names": "S. G.", "surname": "Randall", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 1800, "salary_max": 1800},
    {"name": "C. A. G. Lane", "canonical_name": "Lane, C. A. G.", "given_names": "C. A. G.", "surname": "Lane", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "salary_min": 1350, "salary_max": 1350},
    {"name": "J. L. Caundall", "canonical_name": "Caundall, J. L.", "given_names": "J. L.", "surname": "Caundall", "position": "Police Magistrate, Coroner and Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 630, "salary_max": 1000},
    {"name": "A. Alhadi", "canonical_name": "Alhadi, A.", "given_names": "A.", "surname": "Alhadi", "position": "Master and Registrar, Supreme Court", "department": "Judicial - Sierra Leone", "salary_min": 360, "salary_max": 500, "honors": ["M.B.E."]},
    {"name": "G. L. Jobling", "canonical_name": "Jobling, G. L.", "given_names": "G. L.", "surname": "Jobling", "position": "Attorney-General", "department": "Law Officers - Sierra Leone", "salary_min": 1400, "salary_max": 1400},
    {"name": "C. T. Abbott", "canonical_name": "Abbott, C. T.", "given_names": "C. T.", "surname": "Abbott", "position": "Solicitor-General", "department": "Law Officers - Sierra Leone", "salary_min": 1050, "salary_max": 1050},
    {"name": "G. Callow", "canonical_name": "Callow, G.", "given_names": "G.", "surname": "Callow", "position": "Crown Counsel", "department": "Law Officers - Sierra Leone", "honors": ["D.S.O.", "M.C."], "military_rank": "Captain", "salary_scale": "B"},
    {"name": "E. S. Beoku Betts", "canonical_name": "Betts, E. S. Beoku", "given_names": "E. S.", "surname": "Betts", "position": "Crown Counsel", "department": "Law Officers - Sierra Leone", "honors": ["M.B.E."], "salary_min": 500, "salary_max": 720}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
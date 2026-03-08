"""
Sierra Leone Colonial Office List 1939 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1939

OFFICIALS = [
    {"name": "F. G. Taylor", "canonical_name": "Taylor, F. G.", "given_names": "F. G.", "surname": "Taylor", "position": "Wireless Engineer and Broadcast Officer", "department": "Broadcasting - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone"},
    {"name": "H. Bowles", "canonical_name": "Bowles, H.", "given_names": "H.", "surname": "Bowles", "position": "Government Pilot", "department": "Port and Marine Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "G. E. Randall", "canonical_name": "Randall, G. E.", "given_names": "G. E.", "surname": "Randall", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. H. Webb", "canonical_name": "Webb, A. H.", "given_names": "A. H.", "surname": "Webb", "position": "Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 1800, "salary_max": 1800},
    {"name": "C. A. G. Lane", "canonical_name": "Lane, C. A. G.", "given_names": "C. A. G.", "surname": "Lane", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "salary_min": 1350, "salary_max": 1350},
    {"name": "E. S. Beeku Betts", "canonical_name": "Betts, E. S. Beeku", "given_names": "E. S.", "surname": "Betts", "position": "Police Magistrate, Coroner and Registrar-General", "department": "Judicial - Sierra Leone", "honors": ["M.B.E."], "salary_min": 500, "salary_max": 720},
    {"name": "A. Alhadi", "canonical_name": "Alhadi, A.", "given_names": "A.", "surname": "Alhadi", "position": "Master and Registrar, Supreme Court", "department": "Judicial - Sierra Leone", "honors": ["M.B.E."], "salary_min": 360, "salary_max": 500},
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Attorney-General", "department": "Law Officers - Sierra Leone", "honors": ["K.C."], "salary_min": 1400, "salary_max": 1400},
    {"name": "C. T. Abbott", "canonical_name": "Abbott, C. T.", "given_names": "C. T.", "surname": "Abbott", "position": "Solicitor-General", "department": "Law Officers - Sierra Leone", "salary_min": 1050, "salary_max": 1050},
    {"name": "G. Callow", "canonical_name": "Callow, G.", "given_names": "G.", "surname": "Callow", "position": "Crown Counsels", "department": "Law Officers - Sierra Leone", "military_rank": "Capt.", "honors": ["D.S.O.", "M.C."], "salary_scale": "B"},
    {"name": "A. S. Bodley", "canonical_name": "Bodley, A. S.", "given_names": "A. S.", "surname": "Bodley", "position": "Crown Counsels", "department": "Law Officers - Sierra Leone", "salary_min": 630, "salary_max": 1000}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
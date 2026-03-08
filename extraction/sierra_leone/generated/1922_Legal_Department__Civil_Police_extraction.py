"""
Sierra Leone Colonial Office List 1922 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1922

OFFICIALS = [
    {"name": "Sir G. K. T. Purcell", "canonical_name": "Purcell, G. K. T.", "given_names": "G. K. T.", "surname": "Purcell", "position": "Chief Justice", "department": "Legal Department - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300, "honors": ["Kt."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Puisne and Circuit Judge", "department": "Legal Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "M. F. J. McDonnell", "canonical_name": "McDonnell, M. F. J.", "given_names": "M. F. J.", "surname": "McDonnell", "position": "Attorney-General", "department": "Legal Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "A. C. V. Prior", "canonical_name": "Prior, A. C. V.", "given_names": "A. C. V.", "surname": "Prior", "position": "Solicitor-General", "department": "Legal Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Police Magistrate", "department": "Legal Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "J. F. St. A. Fawcett", "canonical_name": "Fawcett, J. F. St. A.", "given_names": "J. F. St. A.", "surname": "Fawcett", "position": "Master and Registrar General", "department": "Legal Department - Sierra Leone", "salary_min": 600, "salary_max": 840},
    {"name": "J. de Hart", "canonical_name": "Hart, J. de", "given_names": "J.", "surname": "Hart", "position": "Legal Assistant", "department": "Legal Department - Sierra Leone", "salary_min": 720, "salary_max": 720},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Chief Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Police Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "F. B. E. A. McEwen", "canonical_name": "McEwen, F. B. E. A.", "given_names": "F. B. E. A.", "surname": "McEwen", "position": "Assistant Master, Circuit Court", "department": "Legal Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. N. P. Nicol", "canonical_name": "Nicol, J. N. P.", "given_names": "J. N. P.", "surname": "Nicol", "position": "First Grade Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "C. H. King", "canonical_name": "King, C. H.", "given_names": "C. H.", "surname": "King", "position": "Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "military_rank": "Major"},
    {"name": "A. S. Mavrogordato", "canonical_name": "Mavrogordato, A. S.", "given_names": "A. S.", "surname": "Mavrogordato", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "J. Rabbitt", "canonical_name": "Rabbitt, J.", "given_names": "J.", "surname": "Rabbitt", "position": "Chief Inspector", "department": "Civil Police - Sierra Leone", "salary_min": 450, "salary_max": 510},
    {"name": "R. White", "canonical_name": "White, R.", "given_names": "R.", "surname": "White", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "G. E. Biddle", "canonical_name": "Biddle, G. E.", "given_names": "G. E.", "surname": "Biddle", "position": "Assistant Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "Storekeeper", "department": "Prisons - Sierra Leone", "salary_min": 252, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
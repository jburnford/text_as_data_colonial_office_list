"""
Sierra Leone Colonial Office List 1924 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1924

OFFICIALS = [
    {"name": "Sir G. K. T. Purcell", "canonical_name": "Purcell, G. K. T.", "given_names": "G. K. T.", "surname": "Purcell", "position": "Chief Justice", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300, "honors": ["Kt."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Puisne and Circuit Judge", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "M. F. J. McDonnell", "canonical_name": "McDonnell, M. F. J.", "given_names": "M. F. J.", "surname": "McDonnell", "position": "Attorney-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "A. C. V. Prior", "canonical_name": "Prior, A. C. V.", "given_names": "A. C. V.", "surname": "Prior", "position": "Solicitor-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "W. Butler-Lloyd", "canonical_name": "Butler-Lloyd, W.", "given_names": "W.", "surname": "Butler-Lloyd", "position": "Police Magistrate", "department": "Judicial and Legal - Sierra Leone", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. F. St. A. Fawcett", "canonical_name": "Fawcett, J. F. St. A.", "given_names": "J. F. St. A.", "surname": "Fawcett", "position": "Master and Registrar General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 600, "salary_max": 840},
    {"name": "J. de Hart", "canonical_name": "Hart, J. de", "given_names": "J.", "surname": "Hart", "position": "Senior Crown Counsel", "department": "Judicial and Legal - Sierra Leone", "salary_min": 600, "salary_max": 960, "allowances": "72l. seniority pay"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Junior Crown Counsel", "department": "Judicial and Legal - Sierra Leone", "salary_scale": "B"},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Chief Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Police Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "F. B. E. A. McEwen", "canonical_name": "McEwen, F. B. E. A.", "given_names": "F. B. E. A.", "surname": "McEwen", "position": "Assistant Master, Circuit Court", "department": "Judicial and Legal - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. N. P. Nicoll", "canonical_name": "Nicoll, J. N. P.", "given_names": "J. N. P.", "surname": "Nicoll", "position": "First Grade Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 210, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
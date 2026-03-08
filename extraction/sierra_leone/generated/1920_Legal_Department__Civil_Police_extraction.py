"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "Sir G. K. T. Purcell", "canonical_name": "Purcell, G. K. T.", "surname": "Purcell", "position": "Chief Justice", "department": "Legal Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "E. V. Parodi", "canonical_name": "Parodi, E. V.", "surname": "Parodi", "position": "Puisne and Circuit Judge", "department": "Legal Department - Sierra Leone", "salary_min": 900, "salary_max": 900, "duty_allowance": 180},
    {"name": "R. A. Maulde", "canonical_name": "Maulde, R. A.", "surname": "Maulde", "position": "Attorney-General", "department": "Legal Department - Sierra Leone", "salary_min": 700, "salary_max": 900, "duty_allowance": 140},
    {"name": "M. F. J. McDonnell", "canonical_name": "McDonnell, M. F. J.", "surname": "McDonnell", "position": "Solicitor-General", "department": "Legal Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "K. J. Beatty", "canonical_name": "Beatty, K. J.", "surname": "Beatty", "position": "Police Magistrate", "department": "Legal Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "W. A. N. Davies", "canonical_name": "Davies, W. A. N.", "surname": "Davies", "position": "Master and Registrar of Supreme Court", "department": "Legal Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "E. D. Vergette", "canonical_name": "Vergette, E. D.", "surname": "Vergette", "position": "Crown Prosecutor", "department": "Legal Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "C. Carnegie Brown", "canonical_name": "Brown, C. Carnegie", "surname": "Brown", "position": "Legal Assistant", "department": "Legal Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "surname": "Wright", "position": "First Grade Clerk, Master's Office", "department": "Legal Department - Sierra Leone", "salary_min": 202, "salary_max": 230},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "surname": "Williams", "position": "Police Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "A. T. A. Beckley", "canonical_name": "Beckley, A. T. A.", "surname": "Beckley", "position": "Under-Sheriff", "department": "Legal Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "J. N. P. Nicol", "canonical_name": "Nicol, J. N. P.", "surname": "Nicol", "position": "Second Grade Clerk, Crown Law Office", "department": "Legal Department - Sierra Leone", "salary_min": 150, "salary_max": 160},
    {"name": "M. J. O. Macauley", "canonical_name": "Macauley, M. J. O.", "surname": "Macauley", "position": "Assistant Master, Circuit Court", "department": "Legal Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "J. W. Davies", "canonical_name": "Davies, J. W.", "surname": "Davies", "position": "Third Grade Clerk, Police Magistrate's Office", "department": "Legal Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "Major I. Heslip", "canonical_name": "Heslip, I.", "given_names": "I.", "surname": "Heslip", "position": "Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "military_rank": "Major"},
    {"name": "A. S. Mavrogordato", "canonical_name": "Mavrogordato, A. S.", "given_names": "A. S.", "surname": "Mavrogordato", "position": "Assistant Commissioners of Police", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Commissioners of Police", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 400}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
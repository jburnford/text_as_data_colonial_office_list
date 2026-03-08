"""
Gambia Colonial Office List 1920 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1920

OFFICIALS = [
    {"name": "C. Gwyn", "canonical_name": "Gwyn, C.", "given_names": "C.", "surname": "Gwyn", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "E. V. Adams", "canonical_name": "Adams, E. V.", "given_names": "E. V.", "surname": "Adams", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "B. P. E. Bulstrode", "canonical_name": "Bulstrode, B. P. E.", "given_names": "B. P. E.", "surname": "Bulstrode", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "Miss A. N. Maurice", "canonical_name": "Maurice, A. N.", "given_names": "A. N.", "surname": "Maurice", "position": "4th Grade Clerk", "department": "Receiver-General's Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Clerk and Cashier", "department": "Treasury Branch - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "S. P. Gibbs", "canonical_name": "Gibbs, S. P.", "given_names": "S. P.", "surname": "Gibbs", "position": "1st Grade Clerk", "department": "Treasury Branch - Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "2nd Clerk", "department": "Treasury Branch - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "2nd Clerk", "department": "Treasury Branch - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "3rd Clerk", "department": "Treasury Branch - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "R. R. Thomas", "canonical_name": "Thomas, R. R.", "given_names": "R. R.", "surname": "Thomas", "position": "4th Clerk", "department": "Treasury Branch - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "G. A. Manager", "canonical_name": "Manager, G. A.", "given_names": "G. A.", "surname": "Manager", "position": "5th Clerk", "department": "Treasury Branch - Gambia", "salary_min": 40, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
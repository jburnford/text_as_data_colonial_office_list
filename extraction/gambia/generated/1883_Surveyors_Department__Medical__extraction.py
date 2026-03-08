"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "J. C. Bauer", "canonical_name": "Bauer, J. C.", "given_names": "J. C.", "surname": "Bauer", "position": "Colonial Engineer and Sanitary Inspector", "department": "Surveyor's Department - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "allowance for forage, 2s. 3d. a day, and 60l. rent.", "per_diem": "2s. 3d. a day"},
    {"name": "J. G. Joiner", "canonical_name": "Joiner, J. G.", "given_names": "J. G.", "surname": "Joiner", "position": "Foreman of Works", "department": "Surveyor's Department - Gambia", "salary_min": 72, "salary_max": 72},
    {"name": "Thomas H. Spilsbury", "canonical_name": "Spilsbury, Thomas H.", "given_names": "Thomas H.", "surname": "Spilsbury", "position": "Colonial Surgeon", "department": "Medical Establishment - Gambia", "salary_min": 400, "salary_max": 400, "allowances": "2s. 3d. per day forage allowance.", "per_diem": "2s. 3d. per day"},
    {"name": "Dr. W. Allan", "canonical_name": "Allan, W.", "given_names": "W.", "surname": "Allan", "position": "Assistant ditto", "department": "Medical Establishment - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "forage allowances of 2s. 3d. per day.", "per_diem": "2s. 3d. per day", "qualifications": ["Dr."]},
    {"name": "S. W. Dawson", "canonical_name": "Dawson, S. W.", "given_names": "S. W.", "surname": "Dawson", "position": "Dispenser", "department": "Medical Establishment - Gambia", "salary_min": 76, "salary_max": 76, "allowances": "residence"},
    {"name": "Francis Smith", "canonical_name": "Smith, Francis", "given_names": "Francis", "surname": "Smith", "position": "Chief Magistrate", "department": "Judicial Establishment - Gambia", "salary_min": 600, "salary_max": 600, "allowances": "fees"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sheriff", "department": "Judicial Establishment - Gambia", "allowances": "fees only"},
    {"name": "Thomas Johnson", "canonical_name": "Johnson, Thomas", "given_names": "Thomas", "surname": "Johnson", "position": "Registrar of Deeds", "department": "Judicial Establishment - Gambia", "allowances": "fees only"},
    {"name": "Zach. T. Gibson", "canonical_name": "Gibson, Zach. T.", "given_names": "Zach. T.", "surname": "Gibson", "position": "Clerk of Courts and Registrar", "department": "Judicial Establishment - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "Dr. J. P. H. Taylor", "canonical_name": "Taylor, J. P. H.", "given_names": "J. P. H.", "surname": "Taylor", "position": "Coroner", "department": "Judicial Establishment - Gambia", "allowances": "fees only", "qualifications": ["Dr."]},
    {"name": "W. P. Roche", "canonical_name": "Roche, W. P.", "given_names": "W. P.", "surname": "Roche", "position": "Superintendent of Police", "department": "Police and Gaols - Gambia", "salary_min": 200, "salary_max": 200, "allowances": "forage allowances of 2s. 3d. per diem.", "per_diem": "2s. 3d. per diem", "military_rank": "Capt."},
    {"name": "G. H. Assundoe", "canonical_name": "Assundoe, G. H.", "given_names": "G. H.", "surname": "Assundoe", "position": "Gaoler", "department": "Police and Gaols - Gambia", "salary_min": 75, "salary_max": 75}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
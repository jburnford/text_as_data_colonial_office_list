"""
Gambia Colonial Office List 1913 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1913

OFFICIALS = [
    {"name": "E. Vaughan", "canonical_name": "Vaughan, E.", "given_names": "E.", "surname": "Vaughan", "position": "Colonial Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 500, "salary_max": 500, "duty_allowance": 100, "per_diem": "2s. 3d. per diem", "allowances": "forage allowance 2s. 3d. per diem"},
    {"name": "W. Pickering", "canonical_name": "Pickering, W.", "given_names": "W.", "surname": "Pickering", "position": "Inspector of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "F. Crook", "canonical_name": "Crook, F.", "given_names": "F.", "surname": "Crook", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "F. W. Mead", "canonical_name": "Mead, F. W.", "given_names": "F. W.", "surname": "Mead", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "— Johnson", "canonical_name": "Johnson, —", "surname": "Johnson", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "G. M. N'Jie", "canonical_name": "N'Jie, G. M.", "given_names": "G. M.", "surname": "N'Jie", "position": "Foreman of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 120, "salary_max": 150},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk and Accountant", "department": "Colonial Engineer's Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "First Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "C. E. Davis", "canonical_name": "Davis, C. E.", "given_names": "C. E.", "surname": "Davis", "position": "Assistant Timekeeper and Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "Samuel S. Davis", "canonical_name": "Davis, Samuel S.", "given_names": "Samuel S.", "surname": "Davis", "position": "Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "J. Walah", "canonical_name": "Walah, J.", "given_names": "J.", "surname": "Walah", "position": "Local Auditor", "department": "Audit Office - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "R. S. Rendall", "canonical_name": "Rendall, R. S.", "given_names": "R. S.", "surname": "Rendall", "position": "First Clerk", "department": "Audit Office - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "N. Johnson", "canonical_name": "Johnson, N.", "given_names": "N.", "surname": "Johnson", "position": "Second Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "M. MaAffer", "canonical_name": "MaAffer, M.", "given_names": "M.", "surname": "MaAffer", "position": "Chief Engineer and Master", "department": "Government Vessels - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "50l. messing allowance"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Second Engineer", "department": "Government Vessels - Gambia", "salary_min": 200, "salary_max": 250, "allowances": "50l. messing allowance"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
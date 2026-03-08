"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "H. Hollis", "canonical_name": "Hollis, H.", "given_names": "H.", "surname": "Hollis", "position": "Colonial Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 500, "salary_max": 500, "duty_allowance": 100, "per_diem": "2s. 3d. per diem"},
    {"name": "W. Pickering", "canonical_name": "Pickering, W.", "given_names": "W.", "surname": "Pickering", "position": "Assistant Colonial Engineer, Inspector of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "F. Crook", "canonical_name": "Crook, F.", "given_names": "F.", "surname": "Crook", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "F. W. Mead", "canonical_name": "Mead, F. W.", "given_names": "F. W.", "surname": "Mead", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "G. Johnson", "canonical_name": "Johnson, G.", "given_names": "G.", "surname": "Johnson", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "G. M. N'Jie", "canonical_name": "N'Jie, G. M.", "given_names": "G. M.", "surname": "N'Jie", "position": "Foreman of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 120, "salary_max": 150},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk and Accountant", "department": "Colonial Engineer's Department - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "First Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "C. E. Davis", "canonical_name": "Davis, C. E.", "given_names": "C. E.", "surname": "Davis", "position": "Assistant Timekeeper and Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "Samuel S. Davis", "canonical_name": "Davis, Samuel S.", "given_names": "Samuel S.", "surname": "Davis", "position": "Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "H. St. J. Sheppard", "canonical_name": "Sheppard, H. St. J.", "given_names": "H. St. J.", "surname": "Sheppard", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "R. S. Rendall", "canonical_name": "Rendall, R. S.", "given_names": "R. S.", "surname": "Rendall", "position": "First Clerk", "department": "Audit Office - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "N. Johnson", "canonical_name": "Johnson, N.", "given_names": "N.", "surname": "Johnson", "position": "Second Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "M. MoAffer", "canonical_name": "MoAffer, M.", "given_names": "M.", "surname": "MoAffer", "position": "Chief Engineer and Master", "department": "Government Vessels - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "50l. messing allowance"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Second Engineer", "department": "Government Vessels - Gambia", "salary_min": 200, "salary_max": 250, "allowances": "50l. messing allowance"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
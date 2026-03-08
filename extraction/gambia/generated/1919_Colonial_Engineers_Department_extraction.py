"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "H. Hollis", "canonical_name": "Hollis, H.", "given_names": "H.", "surname": "Hollis", "position": "Colonial Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 500, "salary_max": 500, "duty_allowance": 100, "per_diem": "2s. 3d. per diem"},
    {"name": "E. M. W. Williams", "canonical_name": "Williams, E. M. W.", "given_names": "E. M. W.", "surname": "Williams", "position": "Assistant Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 350, "salary_max": 400},
    {"name": "F. W. Mead", "canonical_name": "Mead, F. W.", "given_names": "F. W.", "surname": "Mead", "position": "Clerk of Works and Supervisor of Telephones", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300},
    {"name": "E. A. Richards", "canonical_name": "Richards, E. A.", "given_names": "E. A.", "surname": "Richards", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "J. C. F. Lowry", "canonical_name": "Lowry, J. C. F.", "given_names": "J. C. F.", "surname": "Lowry", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "J. L. Fenton", "canonical_name": "Fenton, J. L.", "given_names": "J. L.", "surname": "Fenton", "position": "Accountant and Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 350},
    {"name": "G. M. N'Jie", "canonical_name": "N'Jie, G. M.", "given_names": "G. M.", "surname": "N'Jie", "position": "Foreman of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 120, "salary_max": 150},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "S. O. Tebbs", "canonical_name": "Tebbs, S. O.", "given_names": "S. O.", "surname": "Tebbs", "position": "Timekeeper and Clerk (4th Grade)", "department": "Colonial Engineer's Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "A. R. Mason", "canonical_name": "Mason, A. R.", "given_names": "A. R.", "surname": "Mason", "position": "Assistant Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "V. E. Johnson", "canonical_name": "Johnson, V. E.", "given_names": "V. E.", "surname": "Johnson", "position": "2nd Assistant Storekeepers", "department": "Colonial Engineer's Department - Gambia"},
    {"name": "R. C. Gubbidon", "canonical_name": "Gubbidon, R. C.", "given_names": "R. C.", "surname": "Gubbidon", "position": "2nd Assistant Storekeepers", "department": "Colonial Engineer's Department - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
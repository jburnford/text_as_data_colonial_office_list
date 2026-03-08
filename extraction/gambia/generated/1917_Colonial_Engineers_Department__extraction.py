"""
Gambia Colonial Office List 1917 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1917

OFFICIALS = [
    {"name": "H. Hollis", "canonical_name": "Hollis, H.", "given_names": "H.", "surname": "Hollis", "position": "Colonial Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 500, "salary_max": 500, "duty_allowance": 100, "per_diem": "2s. 3d."},
    {"name": "W. Pickering", "canonical_name": "Pickering, W.", "given_names": "W.", "surname": "Pickering", "position": "Inspector of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "W. F. Crook", "canonical_name": "Crook, W. F.", "given_names": "W. F.", "surname": "Crook", "position": "Land Registration and Survey Officer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s."},
    {"name": "E. A. Richards", "canonical_name": "Richards, E. A.", "given_names": "E. A.", "surname": "Richards", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "J. C. F. Lowry", "canonical_name": "Lowry, J. C. F.", "given_names": "J. C. F.", "surname": "Lowry", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "W. Ashby", "canonical_name": "Ashby, W.", "given_names": "W.", "surname": "Ashby", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "J. L. Fenton", "canonical_name": "Fenton, J. L.", "given_names": "J. L.", "surname": "Fenton", "position": "Accountant and Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "G. M. N'Jie", "canonical_name": "N'Jie, G. M.", "given_names": "G. M.", "surname": "N'Jie", "position": "Foreman of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 120, "salary_max": 150},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "M. B. Jagne", "canonical_name": "Jagne, M. B.", "given_names": "M. B.", "surname": "Jagne", "position": "Cost Clerk (4th Grade)", "department": "Colonial Engineer's Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "S. E. Johnson", "canonical_name": "Johnson, S. E.", "given_names": "S. E.", "surname": "Johnson", "position": "Timekeeper and Clerk (4th Grade)", "department": "Colonial Engineer's Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "W. N. Johnson", "canonical_name": "Johnson, W. N.", "given_names": "W. N.", "surname": "Johnson", "position": "Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "E. L. Gueritz", "canonical_name": "Gueritz, E. L.", "given_names": "E. L.", "surname": "Gueritz", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "T. R. King", "canonical_name": "King, T. R.", "given_names": "T. R.", "surname": "King", "position": "2nd Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "4th Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "M. McAffe", "canonical_name": "McAffe, M.", "given_names": "M.", "surname": "McAffe", "position": "Chief Engineer and Master", "department": "Government Vessels - Gambia", "salary_min": 300, "salary_max": 360, "duty_allowance": 50, "allowances": "50l. messing allowance"},
    {"name": "P. F. Munn", "canonical_name": "Munn, P. F.", "given_names": "P. F.", "surname": "Munn", "position": "Second Engineer", "department": "Government Vessels - Gambia", "salary_min": 200, "salary_max": 250, "allowances": "50l. messing allowance"},
    {"name": "M. E. King", "canonical_name": "King, M. E.", "given_names": "M. E.", "surname": "King", "position": "Clerk and Storekeeper", "department": "Government Vessels - Gambia", "salary_min": 60, "salary_max": 60}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
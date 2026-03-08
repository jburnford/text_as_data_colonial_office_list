"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "M. King", "canonical_name": "King, M.", "given_names": "M.", "surname": "King", "position": "Caretaker", "department": "MacCarthy Square Board - Gambia", "salary_min": 48, "salary_max": 48},
    {"name": "H. Hollis", "canonical_name": "Hollis, H.", "given_names": "H.", "surname": "Hollis", "position": "Colonial Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 500, "salary_max": 500, "duty_allowance": 100, "per_diem": "2s.3d. per diem"},
    {"name": "W. Pickering", "canonical_name": "Pickering, W.", "given_names": "W.", "surname": "Pickering", "position": "Inspector of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "W. F. Crook", "canonical_name": "Crook, W. F.", "given_names": "W. F.", "surname": "Crook", "position": "Land Registration and Survey Officer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem"},
    {"name": "F. W. Mead", "canonical_name": "Mead, F. W.", "given_names": "F. W.", "surname": "Mead", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "E. A. Richards", "canonical_name": "Richards, E. A.", "given_names": "E. A.", "surname": "Richards", "position": "Clerks of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "G. M. N'Jie", "canonical_name": "N'Jie, G. M.", "given_names": "G. M.", "surname": "N'Jie", "position": "Foreman of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 120, "salary_max": 150},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk and Accountant", "department": "Colonial Engineer's Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "M. B. Jague", "canonical_name": "Jague, M. B.", "given_names": "M. B.", "surname": "Jague", "position": "Cost Clerk (4th Grade)", "department": "Colonial Engineer's Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "S. E. Johnson", "canonical_name": "Johnson, S. E.", "given_names": "S. E.", "surname": "Johnson", "position": "Timekeeper and Clerk (4th Grade)", "department": "Colonial Engineer's Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "R. S. Rendall", "canonical_name": "Rendall, R. S.", "given_names": "R. S.", "surname": "Rendall", "position": "2nd Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "N. C. Johnson", "canonical_name": "Johnson, N. C.", "given_names": "N. C.", "surname": "Johnson", "position": "4th Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 60}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
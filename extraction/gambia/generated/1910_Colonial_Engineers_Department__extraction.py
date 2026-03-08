"""
Gambia Colonial Office List 1910 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1910

OFFICIALS = [
    {"name": "E. Vaughan", "canonical_name": "Vaughan, E.", "given_names": "E.", "surname": "Vaughan", "position": "Colonial Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 450, "salary_max": 450, "duty_allowance": 90, "per_diem": "2s. 3d. per diem"},
    {"name": "W. Pickering", "canonical_name": "Pickering, W.", "given_names": "W.", "surname": "Pickering", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "F. W. Mead", "canonical_name": "Mead, F. W.", "given_names": "F. W.", "surname": "Mead", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "G. M. N'Jie", "canonical_name": "N'Jie, G. M.", "given_names": "G. M.", "surname": "N'Jie", "position": "Foreman of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 120, "salary_max": 150},
    {"name": "H. G. Fowlis", "canonical_name": "Fowlis, H. G.", "given_names": "H. G.", "surname": "Fowlis", "position": "Chief Clerk and Accountant", "department": "Colonial Engineer's Department - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "John C. Fye", "canonical_name": "Fye, John C.", "given_names": "John C.", "surname": "Fye", "position": "Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 60, "salary_max": 100},
    {"name": "N. Johnson", "canonical_name": "Johnson, N.", "given_names": "N.", "surname": "Johnson", "position": "Assistant Timekeeper and Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 36, "salary_max": 36},
    {"name": "Walter Bauerle", "canonical_name": "Bauerle, Walter", "given_names": "Walter", "surname": "Bauerle", "position": "Local Auditor", "department": "Audit Office - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "R. S. Rendall", "canonical_name": "Rendall, R. S.", "given_names": "R. S.", "surname": "Rendall", "position": "Clerk", "department": "Audit Office - Gambia", "salary_min": 75, "salary_max": 75},
    {"name": "M. McAffter", "canonical_name": "McAffter, M.", "given_names": "M.", "surname": "McAffter", "position": "Chief Engineer and Master", "department": "Government Vessels - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "60l. allowance"},
    {"name": "J. G. Doig", "canonical_name": "Doig, J. G.", "given_names": "J. G.", "surname": "Doig", "position": "Second Engineer", "department": "Government Vessels - Gambia", "salary_min": 225, "salary_max": 250, "allowances": "50l. allowance"},
    {"name": "J. B. Davies", "canonical_name": "Davies, J. B.", "given_names": "J. B.", "surname": "Davies", "position": "Purser", "department": "Government Vessels - Gambia", "salary_min": 60, "salary_max": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
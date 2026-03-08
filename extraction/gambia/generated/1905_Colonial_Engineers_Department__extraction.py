"""
Gambia Colonial Office List 1905 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1905

OFFICIALS = [
    {"name": "E. Vaughan", "canonical_name": "Vaughan, E.", "given_names": "E.", "surname": "Vaughan", "position": "Colonial Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 500, "salary_max": 500, "per_diem": "2s. 3d. per diem"},
    {"name": "W. Pickering", "canonical_name": "Pickering, W.", "given_names": "W.", "surname": "Pickering", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "F. W. Mead", "canonical_name": "Mead, F. W.", "given_names": "F. W.", "surname": "Mead", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "G. M. N'Jie", "canonical_name": "N'Jie, G. M.", "given_names": "G. M.", "surname": "N'Jie", "position": "Foreman of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "John C. Fye", "canonical_name": "Fye, John C.", "given_names": "John C.", "surname": "Fye", "position": "Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 85, "salary_max": 85},
    {"name": "R. Rendall", "canonical_name": "Rendall, R.", "given_names": "R.", "surname": "Rendall", "position": "Assistant Timekeeper and Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 30, "salary_max": 30},
    {"name": "E. N. Lubbock", "canonical_name": "Lubbock, E. N.", "given_names": "E. N.", "surname": "Lubbock", "position": "Local Auditor", "department": "Audit Office - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "S. F. N'Jie", "canonical_name": "N'Jie, S. F.", "given_names": "S. F.", "surname": "N'Jie", "position": "Clerk", "department": "Audit Office - Gambia", "salary_min": 75, "salary_max": 75}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1918 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1918

OFFICIALS = [
    {"name": "W. F. Crook", "canonical_name": "Crook, W. F.", "given_names": "W. F.", "surname": "Crook", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem when travelling"},
    {"name": "J. Monday", "canonical_name": "Monday, J.", "given_names": "J.", "surname": "Monday", "position": "2nd Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "A. D. Sawyer", "canonical_name": "Sawyer, A. D.", "given_names": "A. D.", "surname": "Sawyer", "position": "4th Grade Clerk", "department": "Land and Survey Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "E. L. Gueritz", "canonical_name": "Gueritz, E. L.", "given_names": "E. L.", "surname": "Gueritz", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "T. R. King", "canonical_name": "King, T. R.", "given_names": "T. R.", "surname": "King", "position": "2nd Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "4th Grade Clerk", "department": "Audit Office - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "M. McAffe", "canonical_name": "McAffe, M.", "given_names": "M.", "surname": "McAffe", "position": "Chief Engineer and Master", "department": "Government Vessels - Gambia", "salary_min": 300, "salary_max": 360, "duty_allowance": 50, "allowances": "50l. messing allowance"},
    {"name": "H. Lawson", "canonical_name": "Lawson, H.", "given_names": "H.", "surname": "Lawson", "position": "Second Engineer", "department": "Government Vessels - Gambia", "salary_min": 200, "salary_max": 250, "allowances": "50l. messing allowance"},
    {"name": "W. C. George", "canonical_name": "George, W. C.", "given_names": "W. C.", "surname": "George", "position": "3rd Grade Clerk and Storekeeper", "department": "Government Vessels - Gambia", "salary_min": 75, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "W. Hopkins", "canonical_name": "Hopkins, W.", "given_names": "W.", "surname": "Hopkins", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 600, "duty_allowance": 120},
    {"name": "D. W. Scotland", "canonical_name": "Scotland, D. W.", "given_names": "D. W.", "surname": "Scotland", "position": "Assistant in Agricultural Department", "department": "Agricultural Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Veterinary Officer", "department": "Agricultural Department - Sierra Leone", "salary_min": 450, "salary_max": 500},
    {"name": "C. E. Lane-Poole", "canonical_name": "Lane-Poole, C. E.", "given_names": "C. E.", "surname": "Lane-Poole", "position": "Conservator of Forests", "department": "Forestry Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "K. Burbridge", "canonical_name": "Burbridge, K.", "given_names": "K.", "surname": "Burbridge", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "G. Aylmer", "canonical_name": "Aylmer, G.", "given_names": "G.", "surname": "Aylmer", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. E. Hartley", "canonical_name": "Hartley, J. E.", "given_names": "J. E.", "surname": "Hartley", "position": "Overseer", "department": "Forestry Department - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "12l. personal"},
    {"name": "B. E. Hanson", "canonical_name": "Hanson, B. E.", "given_names": "B. E.", "surname": "Hanson", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "R. de C. Baldwin", "canonical_name": "Baldwin, R. de C.", "given_names": "R. de C.", "surname": "Baldwin", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "S. P. Warbrook", "canonical_name": "Warbrook, S. P.", "given_names": "S. P.", "surname": "Warbrook", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "N. H. Turton", "canonical_name": "Turton, N. H.", "given_names": "N. H.", "surname": "Turton", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "First Grade Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "G. P. Coker", "canonical_name": "Coker, G. P.", "given_names": "G. P.", "surname": "Coker", "position": "Second Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "Third Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
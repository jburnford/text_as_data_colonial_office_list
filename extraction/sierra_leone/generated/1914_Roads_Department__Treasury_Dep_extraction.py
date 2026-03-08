"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "A. S. Bradshaw", "canonical_name": "Bradshaw, A. S.", "given_names": "A. S.", "surname": "Bradshaw", "position": "Roads Engineer", "department": "Roads Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 700, "salary_max": 800, "duty_allowance": 140, "honors": ["I.S.O."]},
    {"name": "F. H. Hamilton", "canonical_name": "Hamilton, F. H.", "given_names": "F. H.", "surname": "Hamilton", "position": "Senior Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 100},
    {"name": "L. Belmar", "canonical_name": "Belmar, L.", "given_names": "L.", "surname": "Belmar", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 100},
    {"name": "J. N. Edwin", "canonical_name": "Edwin, J. N.", "given_names": "J. N.", "surname": "Edwin", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "A. G. Johnson", "canonical_name": "Johnson, A. G.", "given_names": "A. G.", "surname": "Johnson", "position": "First Grade Clerks", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "E. G. Taylor", "canonical_name": "Taylor, E. G.", "given_names": "E. G.", "surname": "Taylor", "position": "First Grade Clerks", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "Second Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "Third Grade Clerks", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "M. P. Cole", "canonical_name": "Cole, M. P.", "given_names": "M. P.", "surname": "Cole", "position": "Third Grade Clerks", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
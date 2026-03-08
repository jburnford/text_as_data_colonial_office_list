"""
Sierra Leone Colonial Office List 1912 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1912

OFFICIALS = [
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100, "honors": ["I.S.O."]},
    {"name": "F. H. Hamilton", "canonical_name": "Hamilton, F. H.", "given_names": "F. H.", "surname": "Hamilton", "position": "Senior Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. N. Edwin", "canonical_name": "Edwin, J. N.", "given_names": "J. N.", "surname": "Edwin", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "J. H. Kelson", "canonical_name": "Kelson, J. H.", "given_names": "J. H.", "surname": "Kelson", "position": "Clerk and Storekeeper", "department": "Treasury Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "A. G. Johnson", "canonical_name": "Johnson, A. G.", "given_names": "A. G.", "surname": "Johnson", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 120, "salary_max": 150, "duty_allowance": 25},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "M. P. Cole", "canonical_name": "Cole, M. P.", "given_names": "M. P.", "surname": "Cole", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "E. G. Taylor", "canonical_name": "Taylor, E. G.", "given_names": "E. G.", "surname": "Taylor", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "S. Benjamin", "canonical_name": "Benjamin, S.", "given_names": "S.", "surname": "Benjamin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
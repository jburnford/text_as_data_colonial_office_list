"""
Sierra Leone Colonial Office List 1915 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1915

OFFICIALS = [
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 700, "salary_max": 800, "duty_allowance": 140, "honors": ["I.S.O."]},
    {"name": "F. H. Hamilton", "canonical_name": "Hamilton, F. H.", "given_names": "F. H.", "surname": "Hamilton", "position": "Senior Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 400, "salary_max": 600, "duty_allowance": 80},
    {"name": "L. Belmar", "canonical_name": "Belmar, L.", "given_names": "L.", "surname": "Belmar", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "P. W. Clemens", "canonical_name": "Clemens, P. W.", "given_names": "P. W.", "surname": "Clemens", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "A. G. Johnson", "canonical_name": "Johnson, A. G.", "given_names": "A. G.", "surname": "Johnson", "position": "Financial Assistant", "department": "Treasury Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "E. G. Taylor", "canonical_name": "Taylor, E. G.", "given_names": "E. G.", "surname": "Taylor", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "G. P. Coker", "canonical_name": "Coker, G. P.", "given_names": "G. P.", "surname": "Coker", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "Second Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "Third Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "J. H. Kelso", "canonical_name": "Kelso, J. H.", "given_names": "J. H.", "surname": "Kelso", "position": "Third Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "E. J. Gabidion", "canonical_name": "Gabidion, E. J.", "given_names": "E. J.", "surname": "Gabidion", "position": "Third Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "S. Renshaw", "canonical_name": "Renshaw, S.", "given_names": "S.", "surname": "Renshaw", "position": "Colonial Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 700, "salary_max": 800, "duty_allowance": 140},
    {"name": "L. Belmar", "canonical_name": "Belmar, L.", "given_names": "L.", "surname": "Belmar", "position": "Senior Assistant Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "P. W. Clemens", "canonical_name": "Clemens, P. W.", "given_names": "P. W.", "surname": "Clemens", "position": "Assistant Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. D. Smith", "canonical_name": "Smith, H. D.", "given_names": "H. D.", "surname": "Smith", "position": "Assistant Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "E. G. Taylor", "canonical_name": "Taylor, E. G.", "given_names": "E. G.", "surname": "Taylor", "position": "Chief Clerk", "department": "Treasury - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "First Grade Clerk", "department": "Treasury - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "Second Grade Clerk", "department": "Treasury - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Second Grade Clerk", "department": "Treasury - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "J. H. Kelson", "canonical_name": "Kelson, J. H.", "given_names": "J. H.", "surname": "Kelson", "position": "Third Grade Clerk", "department": "Treasury - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "E. J. Gabbidon", "canonical_name": "Gabbidon, E. J.", "given_names": "E. J.", "surname": "Gabbidon", "position": "Third Grade Clerk", "department": "Treasury - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "S. D. Palmer", "canonical_name": "Palmer, S. D.", "given_names": "S. D.", "surname": "Palmer", "position": "Third Grade Clerk", "department": "Treasury - Sierra Leone", "salary_min": 100, "salary_max": 130},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
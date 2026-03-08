"""
Sierra Leone Colonial Office List 1908 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1908

OFFICIALS = [
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "S. Renshaw", "canonical_name": "Renshaw, S.", "given_names": "S.", "surname": "Renshaw", "position": "Senior Assistant", "department": "Treasury Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. N. Edwin", "canonical_name": "Edwin, J. N.", "given_names": "J. N.", "surname": "Edwin", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 180, "salary_max": 220},
    {"name": "A. G. Johnson", "canonical_name": "Johnson, A. G.", "given_names": "A. G.", "surname": "Johnson", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 120, "salary_max": 150, "duty_allowance": 25},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "S. Benjamin", "canonical_name": "Benjamin, S.", "given_names": "S.", "surname": "Benjamin", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. H. Kelson", "canonical_name": "Kelson, J. H.", "given_names": "J. H.", "surname": "Kelson", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 65, "salary_max": 80},
    {"name": "J. F. Knox", "canonical_name": "Knox, J. F.", "given_names": "J. F.", "surname": "Knox", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. N. Taylor", "canonical_name": "Taylor, J. N.", "given_names": "J. N.", "surname": "Taylor", "position": "6th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 35, "salary_max": 45},
    {"name": "E. G. Taylor", "canonical_name": "Taylor, E. G.", "given_names": "E. G.", "surname": "Taylor", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "M. P. Cole", "canonical_name": "Cole, M. P.", "given_names": "M. P.", "surname": "Cole", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 70, "salary_max": 90},
    {"name": "C. J. Elba", "canonical_name": "Elba, C. J.", "given_names": "C. J.", "surname": "Elba", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "A. F. Dove", "canonical_name": "Dove, A. F.", "given_names": "A. F.", "surname": "Dove", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 35, "salary_max": 45},
    {"name": "J. O. Nicolls", "canonical_name": "Nicolls, J. O.", "given_names": "J. O.", "surname": "Nicolls", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "M. B. Reider", "canonical_name": "Reider, M. B.", "given_names": "M. B.", "surname": "Reider", "position": "Treasury Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60, "location": "Bonthe"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
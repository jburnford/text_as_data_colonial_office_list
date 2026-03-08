"""
Sierra Leone Colonial Office List 1925 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1925

OFFICIALS = [
    {"name": "P. F. Barton", "canonical_name": "Barton, P. F.", "given_names": "P. F.", "surname": "Barton", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "military_rank": "Major", "honors": ["V.D."]},
    {"name": "P. W. Clemens", "canonical_name": "Clemens, P. W.", "given_names": "P. W.", "surname": "Clemens", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A", "military_rank": "Capt."},
    {"name": "E. Godman Taylor", "canonical_name": "Taylor, E. Godman", "given_names": "E. Godman", "surname": "Taylor", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "C. E. Hoyte", "canonical_name": "Hoyte, C. E.", "given_names": "C. E.", "surname": "Hoyte", "position": "Staff Superintendent", "department": "Treasury Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. P. Cole", "canonical_name": "Cole, M. P.", "given_names": "M. P.", "surname": "Cole", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "S. D. Palmer", "canonical_name": "Palmer, S. D.", "given_names": "S. D.", "surname": "Palmer", "position": "Second Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "S. A. Adams", "canonical_name": "Adams, S. A.", "given_names": "S. A.", "surname": "Adams", "position": "Second Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "V. E. Doherty", "canonical_name": "Doherty, V. E.", "given_names": "V. E.", "surname": "Doherty", "position": "Second Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1899 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1899

OFFICIALS = [
    {"name": "E. D. Fairtlough", "canonical_name": "Fairtlough, E. D.", "given_names": "E. D.", "surname": "Fairtlough", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Captain", "region": "Ronietta District"},
    {"name": "A. C. Forde", "canonical_name": "Forde, A. C.", "given_names": "A. C.", "surname": "Forde", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Ronietta District"},
    {"name": "Thomas Hood", "canonical_name": "Hood, Thomas", "given_names": "Thomas", "surname": "Hood", "position": "D. Surgeon", "department": "Civil Establishment - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Ronietta District"},
    {"name": "M. N. Lardner", "canonical_name": "Lardner, M. N.", "given_names": "M. N.", "surname": "Lardner", "position": "Dispenser", "department": "Civil Establishment - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Ronietta District"},
    {"name": "C. E. Carr", "canonical_name": "Carr, C. E.", "given_names": "C. E.", "surname": "Carr", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500, "region": "Bandajuma District"},
    {"name": "D. A. Branche", "canonical_name": "Branche, D. A.", "given_names": "D. A.", "surname": "Branche", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Bandajuma District"},
    {"name": "A. F. M. Berkeley", "canonical_name": "Berkeley, A. F. M.", "given_names": "A. F. M.", "surname": "Berkeley", "position": "D. Surgeon", "department": "Civil Establishment - Sierra Leone", "salary_min": 300, "salary_max": 350, "region": "Bandajuma District"},
    {"name": "J. H. Pearce", "canonical_name": "Pearce, J. H.", "given_names": "J. H.", "surname": "Pearce", "position": "Dispenser", "department": "Civil Establishment - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Bandajuma District"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
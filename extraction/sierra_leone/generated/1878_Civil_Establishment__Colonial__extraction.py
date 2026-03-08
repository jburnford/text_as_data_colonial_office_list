"""
Sierra Leone Colonial Office List 1878 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1878

OFFICIALS = [
    {"name": "Samuel Rowe", "canonical_name": "Rowe, Samuel", "given_names": "Samuel", "surname": "Rowe", "position": "Governor, Commander-in-Chief, and Vice-Admiral of W. Africa Settlements", "department": "Civil Establishment - Sierra Leone", "honors": ["C.M.G."]},
    {"name": "A. C. Allinson", "canonical_name": "Allinson, A. C.", "given_names": "A. C.", "surname": "Allinson", "position": "Aide-de-Camp", "department": "Civil Establishment - Sierra Leone", "military_rank": "Capt."},
    {"name": "J. W. Lewis", "canonical_name": "Lewis, J. W.", "given_names": "J. W.", "surname": "Lewis", "position": "Governor's Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. J. Kendall", "canonical_name": "Kendall, J. J.", "given_names": "J. J.", "surname": "Kendall", "position": "Colonial Secretary", "department": "Colonial Office - Sierra Leone", "salary_min": 800, "salary_max": 800, "military_rank": "Captain"},
    {"name": "J. M. Metzger", "canonical_name": "Metzger, J. M.", "given_names": "J. M.", "surname": "Metzger", "position": "Clerk", "department": "Colonial Office - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "J. H. Spaine", "canonical_name": "Spaine, J. H.", "given_names": "J. H.", "surname": "Spaine", "position": "Clerk", "department": "Colonial Office - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. Williams", "canonical_name": "Williams, J.", "given_names": "J.", "surname": "Williams", "position": "Clerk", "department": "Colonial Office - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "John Shaw", "canonical_name": "Shaw, John", "given_names": "John", "surname": "Shaw", "position": "Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "1st Clerk and Cashier", "department": "Treasury - Sierra Leone", "salary_min": 375, "salary_max": 375},
    {"name": "M. A. Potts", "canonical_name": "Potts, M. A.", "given_names": "M. A.", "surname": "Potts", "position": "2nd Clerk", "department": "Treasury - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "B. M. Brown", "canonical_name": "Brown, B. M.", "given_names": "B. M.", "surname": "Brown", "position": "Assistant Clerk", "department": "Treasury - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "James B. Davies", "canonical_name": "Davies, James B.", "given_names": "James B.", "surname": "Davies", "position": "Extra Clerk", "department": "Treasury - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "The Senior Control Officer", "canonical_name": "Senior Control Officer, The", "surname": "Senior Control Officer", "position": "Auditor-General of W. African Settlements", "department": "Audit Office - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "Clerk to ditto", "department": "Audit Office - Sierra Leone", "salary_min": 100, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
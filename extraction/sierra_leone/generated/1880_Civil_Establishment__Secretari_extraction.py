"""
Sierra Leone Colonial Office List 1880 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1880

OFFICIALS = [
    {"name": "Samuel Rowe", "canonical_name": "Rowe, Samuel", "given_names": "Samuel", "surname": "Rowe", "position": "Governor, Commander-in-Chief, and Vice-Admiral of W. Africa Settlements", "department": "Civil Establishment - Sierra Leone", "salary_min": 2000, "salary_max": 2000, "allowances": "500l. allowances", "honors": ["C.M.G."], "military_rank": "Surgeon-Major"},
    {"name": "J. W. Lewis", "canonical_name": "Lewis, J. W.", "given_names": "J. W.", "surname": "Lewis", "position": "Aide-de-Camp, Governor's Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "T. Risely Griffith", "canonical_name": "Griffith, T. Risely", "given_names": "T. Risely", "surname": "Griffith", "position": "Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "F. Evans", "canonical_name": "Evans, F.", "given_names": "F.", "surname": "Evans", "position": "Assistant Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "H. F. Richmond", "canonical_name": "Richmond, H. F.", "given_names": "H. F.", "surname": "Richmond", "position": "Assistant Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 400, "salary_max": 400, "military_rank": "Captain"},
    {"name": "J. M. Metzger", "canonical_name": "Metzger, J. M.", "given_names": "J. M.", "surname": "Metzger", "position": "Clerk", "department": "Secretarial Branch - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "J. H. Spaine", "canonical_name": "Spaine, J. H.", "given_names": "J. H.", "surname": "Spaine", "position": "Clerk", "department": "Secretarial Branch - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. Williams", "canonical_name": "Williams, J.", "given_names": "J.", "surname": "Williams", "position": "Clerk", "department": "Secretarial Branch - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "M. A. Potts", "canonical_name": "Potts, M. A.", "given_names": "M. A.", "surname": "Potts", "position": "Clerk", "department": "Treasury Branch - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "B. M. Brown", "canonical_name": "Brown, B. M.", "given_names": "B. M.", "surname": "Brown", "position": "Clerk", "department": "Treasury Branch - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "J. J. Wellington", "canonical_name": "Wellington, J. J.", "given_names": "J. J.", "surname": "Wellington", "position": "Clerk", "department": "Treasury Branch - Sierra Leone", "salary_min": 91, "salary_max": 91},
    {"name": "T. G. Lawson", "canonical_name": "Lawson, T. G.", "given_names": "T. G.", "surname": "Lawson", "position": "Government Interpreter", "department": "Aborigines Branch - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "Mohammed Sannasi", "canonical_name": "Sannasi, Mohammed", "given_names": "Mohammed", "surname": "Sannasi", "position": "Arabic Writer", "department": "Aborigines Branch - Sierra Leone", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
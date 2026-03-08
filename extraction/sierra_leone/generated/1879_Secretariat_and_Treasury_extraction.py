"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "Edwin Adolphus", "canonical_name": "Adolphus, Edwin", "given_names": "Edwin", "surname": "Adolphus", "position": "Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 700, "salary_max": 700, "acting_status": "acting"},
    {"name": "F. Evans", "canonical_name": "Evans, F.", "given_names": "F.", "surname": "Evans", "position": "Assistant Colonial Secretary and Treasurer", "department": "Secretariat and Treasury - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "J. M. Metzger", "canonical_name": "Metzger, J. M.", "given_names": "J. M.", "surname": "Metzger", "position": "Clerk", "department": "Secretarial Branch - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "J. H. Spaine", "canonical_name": "Spaine, J. H.", "given_names": "J. H.", "surname": "Spaine", "position": "Clerk", "department": "Secretarial Branch - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. Williams", "canonical_name": "Williams, J.", "given_names": "J.", "surname": "Williams", "position": "Clerk", "department": "Secretarial Branch - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "M. A. Potts", "canonical_name": "Potts, M. A.", "given_names": "M. A.", "surname": "Potts", "position": "Clerk", "department": "Treasury Branch - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "B. M. Brown", "canonical_name": "Brown, B. M.", "given_names": "B. M.", "surname": "Brown", "position": "Clerk", "department": "Treasury Branch - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "J. J. Wellington", "canonical_name": "Wellington, J. J.", "given_names": "J. J.", "surname": "Wellington", "position": "Clerk", "department": "Treasury Branch - Sierra Leone", "salary_min": 91, "salary_max": 91},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
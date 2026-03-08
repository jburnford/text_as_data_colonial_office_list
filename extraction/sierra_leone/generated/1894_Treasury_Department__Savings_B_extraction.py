"""
Sierra Leone Colonial Office List 1894 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1894

OFFICIALS = [
    {"name": "C. B. Mitford", "canonical_name": "Mitford, C. B.", "given_names": "C. B.", "surname": "Mitford", "position": "Colonial Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "and quarters"},
    {"name": "S. M. Bennett", "canonical_name": "Bennett, S. M.", "given_names": "S. M.", "surname": "Bennett", "position": "Assistant Colonial Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "and quarters"},
    {"name": "M. A. Potts", "canonical_name": "Potts, M. A.", "given_names": "M. A.", "surname": "Potts", "position": "Chief Clerk and Cashier", "department": "Treasury - Sierra Leone", "salary_min": 200, "salary_max": 200, "allowances": "and 40l. personal"},
    {"name": "B. M. Brown", "canonical_name": "Brown, B. M.", "given_names": "B. M.", "surname": "Brown", "position": "2nd Clerk", "department": "Treasury - Sierra Leone", "salary_min": 120, "salary_max": 120, "allowances": "and 30l. personal"},
    {"name": "J. J. Wellington", "canonical_name": "Wellington, J. J.", "given_names": "J. J.", "surname": "Wellington", "position": "3rd Clerk", "department": "Treasury - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "R. A. Smith", "canonical_name": "Smith, R. A.", "given_names": "R. A.", "surname": "Smith", "position": "4th Clerk", "department": "Treasury - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. Edwin", "canonical_name": "Edwin, J.", "given_names": "J.", "surname": "Edwin", "position": "5th Clerk", "department": "Treasury - Sierra Leone", "salary_min": 41, "salary_max": 41},
    {"name": "E. W. E. Campbell", "canonical_name": "Campbell, E. W. E.", "given_names": "E. W. E.", "surname": "Campbell", "position": "6th Clerk", "department": "Treasury - Sierra Leone", "salary_min": 29, "salary_max": 29},
    {"name": "J. A. Songo Davies", "canonical_name": "Davies, J. A. Songo", "given_names": "J. A. Songo", "surname": "Davies", "position": "Sub Accountant at Sulymah", "department": "Treasury - Sierra Leone", "salary_min": 1, "salary_max": 1},
    {"name": "J. H. Spaine", "canonical_name": "Spaine, J. H.", "given_names": "J. H.", "surname": "Spaine", "position": "Clerk and Accountant", "department": "Savings Bank - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "W. Metzger", "canonical_name": "Metzger, W.", "given_names": "W.", "surname": "Metzger", "position": "Assistant Clerk", "department": "Savings Bank - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "the Postmaster", "canonical_name": "Postmaster, The", "surname": "Postmaster", "position": "Clerk at Sherbro", "department": "Savings Bank - Sierra Leone", "salary_min": 20, "salary_max": 20, "location": "Sherbro"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "M. A. Potts", "canonical_name": "Potts, M. A.", "surname": "Potts", "position": "Chief Clerk and Cashier", "department": "Civil Establishment - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "J. A. Cline", "canonical_name": "Cline, J. A.", "surname": "Cline", "position": "Sub-Accountant at Sulymah", "department": "Civil Establishment - Sierra Leone", "salary_min": 10, "salary_max": 10},
    {"name": "The Colonial Postmaster", "canonical_name": "Colonial Postmaster, The", "surname": "Colonial Postmaster", "position": "Manager", "department": "Savings Bank - Sierra Leone"},
    {"name": "J. C. E. Parkes", "canonical_name": "Parkes, J. C. E.", "surname": "Parkes", "position": "Superintendent", "department": "Department for Native Affairs - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "surname": "Hanson", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "acting_status": "deputy", "salary_min": 100, "salary_max": 100},
    {"name": "Capt. J. N. Compton", "canonical_name": "Compton, J. N.", "given_names": "J. N.", "surname": "Compton", "position": "Commander", "department": "Colonial Steamer - Sierra Leone", "salary_min": 384, "salary_max": 384, "military_rank": "Captain"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
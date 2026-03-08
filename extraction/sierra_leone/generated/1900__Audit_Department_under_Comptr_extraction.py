"""
Sierra Leone Colonial Office List 1900 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1900

OFFICIALS = [
    {"name": "R. C. Gramm", "canonical_name": "Gramm, R. C.", "given_names": "R. C.", "surname": "Gramm", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 450, "salary_max": 450, "allowances": "and quarters"},
    {"name": "A. L. Turner", "canonical_name": "Turner, A. L.", "given_names": "A. L.", "surname": "Turner", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 225, "salary_max": 225, "allowances": "and quarters or rent"},
    {"name": "P. A. Nichols", "canonical_name": "Nichols, P. A.", "given_names": "P. A.", "surname": "Nichols", "position": "First Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
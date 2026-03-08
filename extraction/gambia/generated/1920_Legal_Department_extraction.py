"""
Gambia Colonial Office List 1920 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1920

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 750, "salary_max": 750},
    {"name": "E. M. Hoy", "canonical_name": "Hoy, E. M.", "given_names": "E. M.", "surname": "Hoy", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "N. G. Taylor", "canonical_name": "Taylor, N. G.", "given_names": "N. G.", "surname": "Taylor", "position": "Assistant Clerk of Courts, 3rd Grade", "department": "Legal Department - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "Geo. D. Williams", "canonical_name": "Williams, Geo. D.", "given_names": "Geo. D.", "surname": "Williams", "position": "Interpreter of Courts", "department": "Legal Department - Gambia", "salary_min": 80, "salary_max": 100, "allowances": "and personal allowance, 18l. per annum."},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Sheriff's Bailiff and Beadle of the Court of Requests", "department": "Legal Department - Gambia", "salary_min": 75, "salary_max": 100, "allowances": "and personal allowance of 20l. per annum."},
    {"name": "N. C. Johnson", "canonical_name": "Johnson, N. C.", "given_names": "N. C.", "surname": "Johnson", "position": "Clerk to Legal Adviser, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "Clerk to Legal Adviser, 3rd Grade", "department": "Legal Department - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "C. J. Clarke", "canonical_name": "Clarke, C. J.", "given_names": "C. J.", "surname": "Clarke", "position": "Clerk to Police Magistrate, 4th Grade", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 70}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
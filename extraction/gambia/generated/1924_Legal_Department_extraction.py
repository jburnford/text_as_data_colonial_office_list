"""
Gambia Colonial Office List 1924 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1924

OFFICIALS = [
    {"name": "S. S. Sawrey-Cookson", "canonical_name": "Sawrey-Cookson, S. S.", "given_names": "S. S.", "surname": "Sawrey-Cookson", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "C. M. Barton", "canonical_name": "Barton, C. M.", "given_names": "C. M.", "surname": "Barton", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800},
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "B. D. Wright", "canonical_name": "Wright, B. D.", "given_names": "B. D.", "surname": "Wright", "position": "Assistant Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "Geo. D. Williams", "canonical_name": "Williams, Geo. D.", "given_names": "Geo. D.", "surname": "Williams", "position": "Interpreter of Courts", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Sheriff's Bailiff and Beadle of the Court of Requests", "department": "Legal Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "W. M. Bright", "canonical_name": "Bright, W. M.", "given_names": "W. M.", "surname": "Bright", "position": "3rd Grade Clerk", "department": "Legal Adviser's Office - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "C. J. Clarke", "canonical_name": "Clarke, C. J.", "given_names": "C. J.", "surname": "Clarke", "position": "3rd Grade Clerk", "department": "Legal Adviser's Office - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "W. G. Sawyer", "canonical_name": "Sawyer, W. G.", "given_names": "W. G.", "surname": "Sawyer", "position": "4th Grade Clerk", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "W. B. Coker", "canonical_name": "Coker, W. B.", "given_names": "W. B.", "surname": "Coker", "position": "Clerk to Police Magistrate, 3rd Grade", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "C. Greig", "canonical_name": "Greig, C.", "given_names": "C.", "surname": "Greig", "position": "Sheriff", "department": "Legal Department - Gambia", "military_rank": "Capt."},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
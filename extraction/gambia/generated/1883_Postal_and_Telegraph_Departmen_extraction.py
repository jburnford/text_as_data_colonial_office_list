"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "A. Helmich", "canonical_name": "Helmich, A.", "given_names": "A.", "surname": "Helmich", "position": "Postmaster-General and General Superintendent of Telegraphs", "department": "Postal and Telegraph Department - Gambia", "salary_min": 500, "salary_max": 500},
    {"name": "J. C. Fleming", "canonical_name": "Fleming, J. C.", "given_names": "J. C.", "surname": "Fleming", "position": "Superintendent of Telegraphs", "department": "Postal and Telegraph Department - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "100l."},
    {"name": "R. A. Sholl", "canonical_name": "Sholl, R. A.", "given_names": "R. A.", "surname": "Sholl", "position": "Chief Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "A. P. Curtis", "canonical_name": "Curtis, A. P.", "given_names": "A. P.", "surname": "Curtis", "position": "2nd Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 230, "salary_max": 230},
    {"name": "W. Kennedy", "canonical_name": "Kennedy, W.", "given_names": "W.", "surname": "Kennedy", "position": "3rd Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 220, "salary_max": 220},
    {"name": "E. Ashton", "canonical_name": "Ashton, E.", "given_names": "E.", "surname": "Ashton", "position": "4th Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 210, "salary_max": 210},
    {"name": "S. Howlett", "canonical_name": "Howlett, S.", "given_names": "S.", "surname": "Howlett", "position": "5th Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "S. H. Wright", "canonical_name": "Wright, S. H.", "given_names": "S. H.", "surname": "Wright", "position": "6th Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "Whitely", "canonical_name": "Whitely, ", "surname": "Whitely", "position": "7th Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "H. Smith", "canonical_name": "Smith, H.", "given_names": "H.", "surname": "Smith", "position": "Resident Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "H. E. Clay", "canonical_name": "Clay, H. E.", "given_names": "H. E.", "surname": "Clay", "position": "Telegraph Clerk", "department": "Postal and Telegraph Department - Gambia", "salary_min": 175, "salary_max": 175},
    {"name": "F. A. Bailey", "canonical_name": "Bailey, F. A.", "given_names": "F. A.", "surname": "Bailey", "position": "Chief Operator and Instructor", "department": "Postal and Telegraph Department - Gambia", "salary_min": 195, "salary_max": 195},
    {"name": "E. W. Snook", "canonical_name": "Snook, E. W.", "given_names": "E. W.", "surname": "Snook", "position": "Telegraph Operator and Instructor", "department": "Postal and Telegraph Department - Gambia", "salary_min": 170, "salary_max": 170}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
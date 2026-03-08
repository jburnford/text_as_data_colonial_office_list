"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "A. J. S. Lewis", "canonical_name": "Lewis, A. J. S.", "given_names": "A. J. S.", "surname": "Lewis", "position": "Principal", "department": "Customs - Sierra Leone", "salary_min": 950, "salary_max": 950},
    {"name": "N. Dallas Forbes", "canonical_name": "Forbes, N. Dallas", "given_names": "N. Dallas", "surname": "Forbes", "position": "Customs Union Clerk", "department": "Customs - Sierra Leone", "salary_min": 600, "salary_max": 600},
    {"name": "F. Fisher", "canonical_name": "Fisher, F.", "given_names": "F.", "surname": "Fisher", "position": "Clerk and Accountant", "department": "Customs - Sierra Leone", "salary_min": 475, "salary_max": 475},
    {"name": "A. G. Ashley", "canonical_name": "Ashley, A. G.", "given_names": "A. G.", "surname": "Ashley", "position": "Clerk and Examiner of Accounts", "department": "Customs - Sierra Leone", "salary_min": 425, "salary_max": 425},
    {"name": "J. G. Bam", "canonical_name": "Bam, J. G.", "given_names": "J. G.", "surname": "Bam", "position": "Senior Statistical Clerk", "department": "Customs - Sierra Leone", "salary_min": 450, "salary_max": 450},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
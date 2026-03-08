"""
Gambia Colonial Office List 1889 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1889

OFFICIALS = [
    {"name": "J. H. Brady", "canonical_name": "Brady, J. H.", "given_names": "J. H.", "surname": "Brady", "position": "Colonial Engineer and Sanitary Inspector", "department": "Surveyor's Department - Gambia", "salary_min": 500, "salary_max": 500, "allowances": "and quarters, or 60l. for rent"},
    {"name": "G. J. Joiner", "canonical_name": "Joiner, G. J.", "given_names": "G. J.", "surname": "Joiner", "position": "Foreman of Works", "department": "Surveyor's Department - Gambia", "salary_min": 72, "salary_max": 72},
    {"name": "T. J. Carow", "canonical_name": "Carow, T. J.", "given_names": "T. J.", "surname": "Carow", "position": "Storekeeper and Clerk", "department": "Surveyor's Department - Gambia", "salary_min": 50, "salary_max": 50, "allowances": "(of which 10l. is personal)"},
    {"name": "M. Taylor", "canonical_name": "Taylor, M.", "given_names": "M.", "surname": "Taylor", "position": "Messenger and Copyist", "department": "Surveyor's Department - Gambia", "salary_min": 30, "salary_max": 30},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
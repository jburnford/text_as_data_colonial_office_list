"""
Sierra Leone Colonial Office List 1915 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1915

OFFICIALS = [
    {"name": "W. Hopkins", "canonical_name": "Hopkins, W.", "given_names": "W.", "surname": "Hopkins", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 600, "duty_allowance": 120},
    {"name": "D. W. Scotland", "canonical_name": "Scotland, D. W.", "given_names": "D. W.", "surname": "Scotland", "position": "Assistants in Agricultural Department", "department": "Agricultural Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "R. H. Bunting", "canonical_name": "Bunting, R. H.", "given_names": "R. H.", "surname": "Bunting", "position": "Assistants in Agricultural Department", "department": "Agricultural Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "S. L. Mosely", "canonical_name": "Mosely, S. L.", "given_names": "S. L.", "surname": "Mosely", "position": "Superintendent, Experimental Farm", "department": "Agricultural Department - Sierra Leone", "salary_min": 120, "salary_max": 140},
    {"name": "C. E. Lane-Poole", "canonical_name": "Lane-Poole, C. E.", "given_names": "C. E.", "surname": "Lane-Poole", "position": "Conservator of Forests", "department": "Forest Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "K. G. Burbridge", "canonical_name": "Burbridge, K. G.", "given_names": "K. G.", "surname": "Burbridge", "position": "Assistant ditto", "department": "Forest Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "G. Aylmer", "canonical_name": "Aylmer, G.", "given_names": "G.", "surname": "Aylmer", "position": "Assistant ditto", "department": "Forest Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "E. Macdonald", "canonical_name": "Macdonald, E.", "given_names": "E.", "surname": "Macdonald", "position": "Assistant ditto", "department": "Forest Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "F. Weay", "canonical_name": "Weay, F.", "given_names": "F.", "surname": "Weay", "position": "Sixth Grade Clerk", "department": "Forest Department - Sierra Leone", "salary_min": 30, "salary_max": 50},
    {"name": "A. S. Bradshaw", "canonical_name": "Bradshaw, A. S.", "given_names": "A. S.", "surname": "Bradshaw", "position": "Roads Engineer", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "G. Wilson", "canonical_name": "Wilson, G.", "given_names": "G.", "surname": "Wilson", "position": "Assistant Engineer", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "E. T. Macfoy", "canonical_name": "Macfoy, E. T.", "given_names": "E. T.", "surname": "Macfoy", "position": "Native Surveyors", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "D. E. Fraser", "canonical_name": "Fraser, D. E.", "given_names": "D. E.", "surname": "Fraser", "position": "Native Surveyors", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "N. E. Oldfield", "canonical_name": "Oldfield, N. E.", "given_names": "N. E.", "surname": "Oldfield", "position": "Native Draughtsman", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "F. W. Edwin", "canonical_name": "Edwin, F. W.", "given_names": "F. W.", "surname": "Edwin", "position": "Fourth Grade Clerk", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 70, "salary_max": 100},
    {"name": "A. J. Bright", "canonical_name": "Bright, A. J.", "given_names": "A. J.", "surname": "Bright", "position": "Fifth Grade Clerk", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 50, "salary_max": 70}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1907 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1907

OFFICIALS = [
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Superintendent", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 350, "allowances": "50l. personal"},
    {"name": "D. R. A. Bettington", "canonical_name": "Bettington, D. R. A.", "given_names": "D. R. A.", "surname": "Bettington", "position": "Inspector", "department": "Civil Police - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "R. White", "canonical_name": "White, R.", "given_names": "R.", "surname": "White", "position": "Superintendent of Prisons", "department": "Prison Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "N. H. Sawyerr", "canonical_name": "Sawyerr, N. H.", "given_names": "N. H.", "surname": "Sawyerr", "position": "Storekeeper", "department": "Prison Department - Sierra Leone", "salary_min": 175, "salary_max": 200},
    {"name": "E. T. Coker", "canonical_name": "Coker, E. T.", "given_names": "E. T.", "surname": "Coker", "position": "Chief Warder", "department": "Prison Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "N. F. Frazer", "canonical_name": "Frazer, N. F.", "given_names": "N. F.", "surname": "Frazer", "position": "Clerk", "department": "Prison Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "R. Maister", "canonical_name": "Maister, R.", "given_names": "R.", "surname": "Maister", "position": "Matron", "department": "Prison Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "M. J. O. Macauley", "canonical_name": "Macauley, M. J. O.", "given_names": "M. J. O.", "surname": "Macauley", "position": "Clerk to ditto", "department": "Educational Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "Clerk to Board of Education", "department": "Educational Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "C. W. Smythe", "canonical_name": "Smythe, C. W.", "given_names": "C. W.", "surname": "Smythe", "position": "Superintendent", "department": "Agricultural Development Branch - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "J. Hartley", "canonical_name": "Hartley, J.", "given_names": "J.", "surname": "Hartley", "position": "Overseer", "department": "Agricultural Development Branch - Sierra Leone", "salary_min": 150, "salary_max": 150},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
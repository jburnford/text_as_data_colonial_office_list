"""
Sierra Leone Colonial Office List 1905 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1905

OFFICIALS = [
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Superintendent", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "C. T. Reaney", "canonical_name": "Reaney, C. T.", "given_names": "C. T.", "surname": "Reaney", "position": "Inspector", "department": "Civil Police - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "H. Hann", "canonical_name": "Hann, H.", "given_names": "H.", "surname": "Hann", "position": "Superintendent of Prisons", "department": "Prison Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "N. H. Sawyerr", "canonical_name": "Sawyerr, N. H.", "given_names": "N. H.", "surname": "Sawyerr", "position": "Storekeeper", "department": "Prison Department - Sierra Leone", "salary_min": 175, "salary_max": 175},
    {"name": "T. M. Jones", "canonical_name": "Jones, T. M.", "given_names": "T. M.", "surname": "Jones", "position": "Chief Warden", "department": "Prison Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "B. E. Cummings", "canonical_name": "Cummings, B. E.", "given_names": "B. E.", "surname": "Cummings", "position": "Clerk", "department": "Prison Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "R. A. Macaulay", "canonical_name": "Macaulay, R. A.", "given_names": "R. A.", "surname": "Macaulay", "position": "Matron", "department": "Prison Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "A. E. Lavers", "canonical_name": "Lavers, A. E.", "given_names": "A. E.", "surname": "Lavers", "position": "Clerk to ditto", "department": "Educational Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "Clerk to Board of Education", "department": "Educational Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "Dr. E. Blyden", "canonical_name": "Blyden, E.", "given_names": "E.", "surname": "Blyden", "position": "Director of Mohammedan Education", "department": "Educational Department - Sierra Leone", "salary_min": 100, "salary_max": 100, "qualifications": ["Dr."]},
    {"name": "N. B. Seton", "canonical_name": "Seton, N. B.", "given_names": "N. B.", "surname": "Seton", "position": "Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "C. W. Smythe", "canonical_name": "Smythe, C. W.", "given_names": "C. W.", "surname": "Smythe", "position": "Curator", "department": "Botanical Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "J. Hartley", "canonical_name": "Hartley, J.", "given_names": "J.", "surname": "Hartley", "position": "Overseer", "department": "Botanical Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
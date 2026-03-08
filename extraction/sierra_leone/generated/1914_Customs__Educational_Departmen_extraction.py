"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "A. P. Viret", "canonical_name": "Viret, A. P.", "given_names": "A. P.", "surname": "Viret", "position": "Comptroller of Customs", "department": "Customs - Sierra Leone", "salary_min": 600, "salary_max": 700, "duty_allowance": 120, "allowances": "100l. allowance in lieu of fees"},
    {"name": "A. S. Fraser", "canonical_name": "Fraser, A. S.", "given_names": "A. S.", "surname": "Fraser", "position": "Assistant Comptroller of Customs", "department": "Customs - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "allowances": "50l. in lieu of fees"},
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": "R. B.", "surname": "Mackie", "position": "Supervisor of Customs", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 300, "salary_max": 400},
    {"name": "L. F. Campbell", "canonical_name": "Campbell, L. F.", "given_names": "L. F.", "surname": "Campbell", "position": "Supervisor of Customs", "department": "Customs - Sierra Leone", "location": "Sherbro", "salary_min": 300, "salary_max": 350},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": "A. C. A.", "surname": "Johnson", "position": "Chief Clerk and Warehousekeeper", "department": "Customs - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "P. H. H. George", "canonical_name": "George, P. H. H.", "given_names": "P. H. H.", "surname": "George", "position": "Senior Outdoor Officer", "department": "Customs - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "V. E. Spaine", "canonical_name": "Spaine, V. E.", "given_names": "V. E.", "surname": "Spaine", "position": "First Grade Clerk", "department": "Customs - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "T. A. Clemens", "canonical_name": "Clemens, T. A.", "given_names": "T. A.", "surname": "Clemens", "position": "First Grade Clerk", "department": "Customs - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "T. M. Johnson", "canonical_name": "Johnson, T. M.", "given_names": "T. M.", "surname": "Johnson", "position": "Second Clerk", "department": "Customs - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "M. A. Lewis", "canonical_name": "Lewis, M. A.", "given_names": "M. A.", "surname": "Lewis", "position": "Second Clerk", "department": "Customs - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "T. A. Davies", "canonical_name": "Davies, T. A.", "given_names": "T. A.", "surname": "Davies", "position": "Second Clerk", "department": "Customs - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Second Clerk", "department": "Customs - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "R. F. Honter", "canonical_name": "Honter, R. F.", "given_names": "R. F.", "surname": "Honter", "position": "Director of Education", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "R. Lean", "canonical_name": "Lean, R.", "given_names": "R.", "surname": "Lean", "position": "Principal, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 450, "salary_max": 500},
    {"name": "W. J. Holloway", "canonical_name": "Holloway, W. J.", "given_names": "W. J.", "surname": "Holloway", "position": "Vice-Principal Model School", "department": "Educational Department - Sierra Leone", "salary_min": 400, "salary_max": 450, "acting_status": "acting", "allowances": "100l. acting allowance"},
    {"name": "Miss M. M. McAllister", "canonical_name": "McAllister, M. M.", "given_names": "M. M.", "surname": "McAllister", "position": "Instructoress, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Chief Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "75l. personal"},
    {"name": "S. J. Taylor", "canonical_name": "Taylor, S. J.", "given_names": "S. J.", "surname": "Taylor", "position": "Chief Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "H. Deen", "canonical_name": "Deen, H.", "given_names": "H.", "surname": "Deen", "position": "Second Grade Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "F. J. Hollist", "canonical_name": "Hollist, F. J.", "given_names": "F. J.", "surname": "Hollist", "position": "Fifth Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 50, "salary_max": 70}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
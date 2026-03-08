"""
Sierra Leone Colonial Office List 1909 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1909

OFFICIALS = [
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "50l. personal"},
    {"name": "J. Proudfoot", "canonical_name": "Proudfoot, J.", "given_names": "J.", "surname": "Proudfoot", "position": "Principal, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 450, "salary_max": 500},
    {"name": "J. H. Duff", "canonical_name": "Duff, J. H.", "given_names": "J. H.", "surname": "Duff", "position": "Education Expert, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. Pool", "canonical_name": "Pool, J.", "given_names": "J.", "surname": "Pool", "position": "Education Expert, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "W. J. Holloway", "canonical_name": "Holloway, W. J.", "given_names": "W. J.", "surname": "Holloway", "position": "Education Expert, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "Clerk to Board of Education", "department": "Educational Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "Hadir-u-deen", "canonical_name": "Hadir-u-deen", "surname": "Hadir-u-deen", "position": "Secretary to Board of Mohammedan Education", "department": "Educational Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "M. J. O. Macauley", "canonical_name": "Macauley, M. J. O.", "given_names": "M. J. O.", "surname": "Macauley", "position": "Clerk to Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "C. W. Smythe", "canonical_name": "Smythe, C. W.", "given_names": "C. W.", "surname": "Smythe", "position": "Superintendent of Agriculture", "department": "Agricultural Development Branch - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. Hartley", "canonical_name": "Hartley, J.", "given_names": "J.", "surname": "Hartley", "position": "Overseer", "department": "Agricultural Development Branch - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "12l. personal"},
    {"name": "E. du Boulay", "canonical_name": "Boulay, E. du", "given_names": "E.", "surname": "Boulay", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "P. L. Tengely", "canonical_name": "Tengely, P. L.", "given_names": "P. L.", "surname": "Tengely", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "R. H. Jebb", "canonical_name": "Jebb, R. H.", "given_names": "R. H.", "surname": "Jebb", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "1st Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 180},
    {"name": "G. P. Coker", "canonical_name": "Coker, G. P.", "given_names": "G. P.", "surname": "Coker", "position": "2nd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 160},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "3rd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "4th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": "M. B.", "surname": "Reader", "position": "5th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 60, "salary_max": 60}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
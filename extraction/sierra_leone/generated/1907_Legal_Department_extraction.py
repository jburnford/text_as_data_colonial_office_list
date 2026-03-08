"""
Sierra Leone Colonial Office List 1907 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1907

OFFICIALS = [
    {"name": "Sir P. C. Smyly", "canonical_name": "Smyly, P. C.", "given_names": "P. C.", "surname": "Smyly", "position": "Chief Justice", "department": "Legal Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "honors": ["Kt."], "qualifications": ["LL.D."]},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. T. Packard", "canonical_name": "Packard, E. T.", "given_names": "E. T.", "surname": "Packard", "position": "Attorney-General", "department": "Legal Department - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "F. H. Gough", "canonical_name": "Gough, F. H.", "given_names": "F. H.", "surname": "Gough", "position": "Solicitor-General", "department": "Legal Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "Chief Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "A. T. Beckley", "canonical_name": "Beckley, A. T.", "given_names": "A. T.", "surname": "Beckley", "position": "2nd Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "H. R. Williams", "canonical_name": "Williams, H. R.", "given_names": "H. R.", "surname": "Williams", "position": "3rd Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "R. Vandermost", "canonical_name": "Vandermost, R.", "given_names": "R.", "surname": "Vandermost", "position": "4th Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "D. F. Wilbraham", "canonical_name": "Wilbraham, D. F.", "given_names": "D. F.", "surname": "Wilbraham", "position": "Police Magistrate, Master of Supreme Court and Registrar-General", "department": "Legal Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "S. A. Metzger", "canonical_name": "Metzger, S. A.", "given_names": "S. A.", "surname": "Metzger", "position": "Senior Clerk to Master of Court", "department": "Legal Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "1st Clerk to Master of Court", "department": "Legal Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "A. E. Scott", "canonical_name": "Scott, A. E.", "given_names": "A. E.", "surname": "Scott", "position": "2nd Clerk to Master of Court", "department": "Legal Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "C. Duke", "canonical_name": "Duke, C.", "given_names": "C.", "surname": "Duke", "position": "Chief Clerk to Registrar-General", "department": "Legal Department - Sierra Leone", "salary_min": 65, "salary_max": 80},
    {"name": "F. E. Bucknor", "canonical_name": "Bucknor, F. E.", "given_names": "F. E.", "surname": "Bucknor", "position": "2nd Clerk to ditto", "department": "Legal Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "A. M. Strong", "canonical_name": "Strong, A. M.", "given_names": "A. M.", "surname": "Strong", "position": "3rd Clerk to ditto", "department": "Legal Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "S. G. Randall", "canonical_name": "Randall, S. G.", "given_names": "S. G.", "surname": "Randall", "position": "4th Clerk to ditto", "department": "Legal Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Sheriff and Provost Marshal", "department": "Legal Department - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "S. A. Metzger", "canonical_name": "Metzger, S. A.", "given_names": "S. A.", "surname": "Metzger", "position": "Under Sheriff", "department": "Legal Department - Sierra Leone", "salary_min": 65, "salary_max": 65},
    {"name": "W. S. Grant", "canonical_name": "Grant, W. S.", "given_names": "W. S.", "surname": "Grant", "position": "Clerk to Sheriff", "department": "Legal Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "A. E. T. Metzger", "canonical_name": "Metzger, A. E. T.", "given_names": "A. E. T.", "surname": "Metzger", "position": "Clerk, Police Court", "department": "Legal Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "J. Nicol", "canonical_name": "Nicol, J.", "given_names": "J.", "surname": "Nicol", "position": "2nd Clerk, do.", "department": "Legal Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "W. A. Cole", "canonical_name": "Cole, W. A.", "given_names": "W. A.", "surname": "Cole", "position": "Bailiff", "department": "Legal Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "Curator of Intestate Estates", "department": "Legal Department - Sierra Leone"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
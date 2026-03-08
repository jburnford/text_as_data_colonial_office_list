"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "P. F. Barton", "canonical_name": "Barton, P. F.", "given_names": "P. F.", "surname": "Barton", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["V.D."]},
    {"name": "Edwin Taylor", "canonical_name": "Taylor, Edwin", "given_names": "Edwin", "surname": "Taylor", "position": "Senior Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 840, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "C. J. Hodgens", "canonical_name": "Hodgens, C. J.", "given_names": "C. J.", "surname": "Hodgens", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A"},
    {"name": "C. S. Rayner", "canonical_name": "Rayner, C. S.", "given_names": "C. S.", "surname": "Rayner", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A"},
    {"name": "E. Godman Taylor", "canonical_name": "Taylor, E. Godman", "given_names": "E. Godman", "surname": "Taylor", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "C. E. Hoyte", "canonical_name": "Hoyte, C. E.", "given_names": "C. E.", "surname": "Hoyte", "position": "Staff Superintendent", "department": "Treasury Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. E. Laverse", "canonical_name": "Laverse, A. E.", "given_names": "A. E.", "surname": "Laverse", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "S. D. Palmer", "canonical_name": "Palmer, S. D.", "given_names": "S. D.", "surname": "Palmer", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. I. Lauder", "canonical_name": "Lauder, J. I.", "given_names": "J. I.", "surname": "Lauder", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": "R. B.", "surname": "Mackie", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A"},
    {"name": "D. A. Finlayson", "canonical_name": "Finlayson, D. A.", "given_names": "D. A.", "surname": "Finlayson", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_scale": "A"},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Sherbro", "salary_min": 360, "salary_max": 500},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": "A. C. A.", "surname": "Johnson", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_min": 360, "salary_max": 500},
    {"name": "A. R. Harris", "canonical_name": "Harris, A. R.", "given_names": "A. R.", "surname": "Harris", "position": "Senior Harbour Officer", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. A. Lewis", "canonical_name": "Lewis, M. A.", "given_names": "M. A.", "surname": "Lewis", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. M. Peeler", "canonical_name": "Peeler, W. M.", "given_names": "W. M.", "surname": "Peeler", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. A. Smith", "canonical_name": "Smith, M. A.", "given_names": "M. A.", "surname": "Smith", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "E. F. Clarke", "canonical_name": "Clarke, E. F.", "given_names": "E. F.", "surname": "Clarke", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "C. D. Williams", "canonical_name": "Williams, C. D.", "given_names": "C. D.", "surname": "Williams", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "E. H. Morris", "canonical_name": "Morris, E. H.", "given_names": "E. H.", "surname": "Morris", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "R. S. Foster", "canonical_name": "Foster, R. S.", "given_names": "R. S.", "surname": "Foster", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. F. Pinder", "canonical_name": "Pinder, R. F.", "given_names": "R. F.", "surname": "Pinder", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "H. G. Imray", "canonical_name": "Imray, H. G.", "given_names": "H. G.", "surname": "Imray", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": "U. W.", "surname": "Coker", "position": "Chief Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "S. B. Logan", "canonical_name": "Logan, S. B.", "given_names": "S. B.", "surname": "Logan", "position": "First Grade Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "S. A. Adams", "canonical_name": "Adams, S. A.", "given_names": "S. A.", "surname": "Adams", "position": "First Grade Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 210, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1928 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1928

OFFICIALS = [
    {"name": "K. B. Allan", "canonical_name": "Allan, K. B.", "given_names": "K. B.", "surname": "Allan", "position": "Senior Medical Officer", "department": "Medical / Board of Health - Gambia", "salary_min": 1000, "salary_max": 1150, "allowances": "250l. staff and seniority allowances."},
    {"name": "G. E. Craig", "canonical_name": "Craig, G. E.", "given_names": "G. E.", "surname": "Craig", "position": "Medical Officer", "department": "Medical / Board of Health - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance."},
    {"name": "J. C. Cruickshank", "canonical_name": "Cruickshank, J. C.", "given_names": "J. C.", "surname": "Cruickshank", "position": "Medical Officer", "department": "Medical / Board of Health - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance."},
    {"name": "A. M. W. Rae", "canonical_name": "Rae, A. M. W.", "given_names": "A. M. W.", "surname": "Rae", "position": "Medical Officer", "department": "Medical / Board of Health - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance."},
    {"name": "S. G. Harrison", "canonical_name": "Harrison, S. G.", "given_names": "S. G.", "surname": "Harrison", "position": "Medical Officer", "department": "Medical / Board of Health - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance."},
    {"name": "M. Thompson", "canonical_name": "Thompson, M.", "given_names": "M.", "surname": "Thompson", "position": "Senior Nursing Sister", "department": "Medical / Board of Health - Gambia", "salary_min": 380, "salary_max": 440, "allowances": "40l. charge allowance."},
    {"name": "J. Roberts", "canonical_name": "Roberts, J.", "given_names": "J.", "surname": "Roberts", "position": "Nursing Sister", "department": "Medical / Board of Health - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "T. Grant", "canonical_name": "Grant, T.", "given_names": "T.", "surname": "Grant", "position": "Nursing Sister", "department": "Medical / Board of Health - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "Chief Dispenser and Storekeeper, 2nd Grade", "department": "Medical / Board of Health - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "E. W. Johns", "canonical_name": "Johns, E. W.", "given_names": "E. W.", "surname": "Johns", "position": "Dispensers, 2nd Grade", "department": "Medical / Board of Health - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "W. M. Rollings", "canonical_name": "Rollings, W. M.", "given_names": "W. M.", "surname": "Rollings", "position": "Dispensers, 2nd Grade", "department": "Medical / Board of Health - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "T. R. King", "canonical_name": "King, T. R.", "given_names": "T. R.", "surname": "King", "position": "2nd Grade Clerk", "department": "Medical / Board of Health - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "F. A. Innes", "canonical_name": "Innes, F. A.", "given_names": "F. A.", "surname": "Innes", "position": "Medical Officer of Health", "department": "Medical / Board of Health - Gambia", "salary_min": 800, "salary_max": 960, "allowances": "staff and seniority allowances, 222l.", "military_rank": "Capt."},
    {"name": "A. F. V. Vaughan", "canonical_name": "Vaughan, A. F. V.", "given_names": "A. F. V.", "surname": "Vaughan", "position": "Sanitary Inspector", "department": "Medical / Board of Health - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "F. A. Wilford", "canonical_name": "Wilford, F. A.", "given_names": "F. A.", "surname": "Wilford", "position": "Assistant Sanitary Inspector", "department": "Medical / Board of Health - Gambia", "salary_min": 360, "salary_max": 460}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
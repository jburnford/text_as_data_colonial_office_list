"""
Gambia Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1923

OFFICIALS = [
    {"name": "F. A. Inner", "canonical_name": "Inner, F. A.", "given_names": "F. A.", "surname": "Inner", "position": "Medical Officer of Health", "department": "Board of Health - Gambia", "salary_min": 800, "salary_max": 960, "allowances": "staff and seniority allowances, 222l.", "military_rank": "Capt."},
    {"name": "C. Wolfendale", "canonical_name": "Wolfendale, C.", "given_names": "C.", "surname": "Wolfendale", "position": "Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 440, "salary_max": 500, "allowances": "50l. personal allowance."},
    {"name": "A. F. V. Vaughan", "canonical_name": "Vaughan, A. F. V.", "given_names": "A. F. V.", "surname": "Vaughan", "position": "Assistant Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 400, "salary_max": 460},
    {"name": "J. H. Deigh", "canonical_name": "Deigh, J. H.", "given_names": "J. H.", "surname": "Deigh", "position": "Clerk of the Market", "department": "Board of Health - Gambia", "salary_min": 84, "salary_max": 108},
    {"name": "E. E. Pratt", "canonical_name": "Pratt, E. E.", "given_names": "E. E.", "surname": "Pratt", "position": "Assistant Market Clerk", "department": "Board of Health - Gambia", "salary_min": 42, "salary_max": 66},
    {"name": "J. A. Johnson", "canonical_name": "Johnson, J. A.", "given_names": "J. A.", "surname": "Johnson", "position": "Senior Inspector of Nuisances", "department": "Board of Health - Gambia", "salary_min": 84, "salary_max": 108},
    {"name": "G. C. Cole", "canonical_name": "Cole, G. C.", "given_names": "G. C.", "surname": "Cole", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 42, "salary_max": 66},
    {"name": "G. W. Davies", "canonical_name": "Davies, G. W.", "given_names": "G. W.", "surname": "Davies", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 42, "salary_max": 66},
    {"name": "J. R. Mensah", "canonical_name": "Mensah, J. R.", "given_names": "J. R.", "surname": "Mensah", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 42, "salary_max": 66},
    {"name": "T. S. Roberts", "canonical_name": "Roberts, T. S.", "given_names": "T. S.", "surname": "Roberts", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 42, "salary_max": 66},
    {"name": "D. O. E. Hogan", "canonical_name": "Hogan, D. O. E.", "given_names": "D. O. E.", "surname": "Hogan", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 42, "salary_max": 66}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1924 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1924

OFFICIALS = [
    {"name": "Senior Medical Officer", "canonical_name": "Senior Medical Officer, ", "surname": "Senior Medical Officer", "position": "Chairman", "department": "Board of Health - Gambia"},
    {"name": "F. A. Innes", "canonical_name": "Innes, F. A.", "given_names": "F. A.", "surname": "Innes", "position": "Medical Officer of Health", "department": "Board of Health - Gambia", "salary_min": 800, "salary_max": 960, "allowances": "staff and seniority allowances, 222l.", "military_rank": "Capt."},
    {"name": "C. Wolfendale", "canonical_name": "Wolfendale, C.", "given_names": "C.", "surname": "Wolfendale", "position": "Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 440, "salary_max": 500, "allowances": "50l. personal allowance"},
    {"name": "A. F. V. Vaughan", "canonical_name": "Vaughan, A. F. V.", "given_names": "A. F. V.", "surname": "Vaughan", "position": "Assistant Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 360, "salary_max": 460},
    {"name": "J. H. Deigh", "canonical_name": "Deigh, J. H.", "given_names": "J. H.", "surname": "Deigh", "position": "Market Clerk", "department": "Board of Health - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "E. E. Pratt", "canonical_name": "Pratt, E. E.", "given_names": "E. E.", "surname": "Pratt", "position": "Assistant Market Clerk", "department": "Board of Health - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "J. A. Johnson", "canonical_name": "Johnson, J. A.", "given_names": "J. A.", "surname": "Johnson", "position": "Senior Inspector of Nuisances", "department": "Board of Health - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "G. C. Cole", "canonical_name": "Cole, G. C.", "given_names": "G. C.", "surname": "Cole", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "G. W. Davies", "canonical_name": "Davies, G. W.", "given_names": "G. W.", "surname": "Davies", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "J. R. Mensah", "canonical_name": "Mensah, J. R.", "given_names": "J. R.", "surname": "Mensah", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "T. S. Roberts", "canonical_name": "Roberts, T. S.", "given_names": "T. S.", "surname": "Roberts", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "S. V. Harding", "canonical_name": "Harding, S. V.", "given_names": "S. V.", "surname": "Harding", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "D. O. E. Hogan", "canonical_name": "Hogan, D. O. E.", "given_names": "D. O. E.", "surname": "Hogan", "position": "Junior Inspectors of Nuisances", "department": "Board of Health - Gambia", "salary_min": 50, "salary_max": 82},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
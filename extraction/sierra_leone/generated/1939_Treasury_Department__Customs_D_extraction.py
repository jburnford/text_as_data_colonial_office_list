"""
Sierra Leone Colonial Office List 1939 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1939

OFFICIALS = [
    {"name": "G. N. Farquhar", "canonical_name": "Farquhar, G. N.", "given_names": "G. N.", "surname": "Farquhar", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "honors": ["M.C."], "allowances": "Currency allowance 100l."},
    {"name": "M. J. Stewart", "canonical_name": "Stewart, M. J.", "given_names": "M. J.", "surname": "Stewart", "position": "Deputy Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "military_rank": "Major"},
    {"name": "R. S. Hector", "canonical_name": "Hector, R. S.", "given_names": "R. S.", "surname": "Hector", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. A. D. Barton", "canonical_name": "Barton, J. A. D.", "given_names": "J. A. D.", "surname": "Barton", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 400, "salary_max": 810},
    {"name": "J. C. Hamilton", "canonical_name": "Hamilton, J. C.", "given_names": "J. C.", "surname": "Hamilton", "position": "African Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Staff Superintendent", "department": "Treasury Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 840, "salary_max": 920},
    {"name": "F. A. von Weiller", "canonical_name": "Weiller, F. A. von", "given_names": "F. A.", "surname": "Weiller", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A"},
    {"name": "F. C. Campbell", "canonical_name": "Campbell, F. C.", "given_names": "F. C.", "surname": "Campbell", "position": "Supervisor", "department": "Customs Department - Sierra Leone", "salary_min": 360, "salary_max": 600},
    {"name": "S. E. Cole", "canonical_name": "Cole, S. E.", "given_names": "S. E.", "surname": "Cole", "position": "Supervisor", "department": "Customs Department - Sierra Leone", "salary_min": 360, "salary_max": 600},
    {"name": "W. A. P. Buck", "canonical_name": "Buck, W. A. P.", "given_names": "W. A. P.", "surname": "Buck", "position": "Staff Superintendent", "department": "Customs Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "J. D. M. Bourne", "canonical_name": "Bourne, J. D. M.", "given_names": "J. D. M.", "surname": "Bourne", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "H. C. V. B. Barnes", "canonical_name": "Barnes, H. C. V. B.", "given_names": "H. C. V. B.", "surname": "Barnes", "position": "Senior Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 840, "salary_max": 920},
    {"name": "R. T. Spencer", "canonical_name": "Spencer, R. T.", "given_names": "R. T.", "surname": "Spencer", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 400, "salary_max": 810},
    {"name": "R. D. Littlejohns", "canonical_name": "Littlejohns, R. D.", "given_names": "R. D.", "surname": "Littlejohns", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 400, "salary_max": 810}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
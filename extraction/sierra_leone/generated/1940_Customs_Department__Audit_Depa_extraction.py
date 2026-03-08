"""
Sierra Leone Colonial Office List 1940 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1940

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "R. L. Wroughton", "canonical_name": "Wroughton, R. L.", "given_names": "R. L.", "surname": "Wroughton", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 840, "salary_max": 920},
    {"name": "F. A. von Weiller", "canonical_name": "Weiller, F. A. von", "given_names": "F. A.", "surname": "Weiller", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A"},
    {"name": "F. C. Campbell", "canonical_name": "Campbell, F. C.", "given_names": "F. C.", "surname": "Campbell", "position": "Supervisors", "department": "Customs Department - Sierra Leone", "salary_min": 360, "salary_max": 600},
    {"name": "S. E. Cole", "canonical_name": "Cole, S. E.", "given_names": "S. E.", "surname": "Cole", "position": "Supervisors", "department": "Customs Department - Sierra Leone", "salary_min": 360, "salary_max": 600},
    {"name": "W. A. P. Buck", "canonical_name": "Buck, W. A. P.", "given_names": "W. A. P.", "surname": "Buck", "position": "Staff Superintendent", "department": "Customs Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "R. Macdonald", "canonical_name": "Macdonald, R.", "given_names": "R.", "surname": "Macdonald", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "H. C. V. B. Barnes", "canonical_name": "Barnes, H. C. V. B.", "given_names": "H. C. V. B.", "surname": "Barnes", "position": "Senior Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 840, "salary_max": 920},
    {"name": "R. T. Spencer", "canonical_name": "Spencer, R. T.", "given_names": "R. T.", "surname": "Spencer", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_min": 400, "salary_max": 810},
    {"name": "R. D. Littlejohns", "canonical_name": "Littlejohns, R. D.", "given_names": "R. D.", "surname": "Littlejohns", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_min": 400, "salary_max": 810},
    {"name": "F. G. Taylor", "canonical_name": "Taylor, F. G.", "given_names": "F. G.", "surname": "Taylor", "position": "Wireless Engineer and Broadcast Officer", "department": "Broadcasting - Sierra Leone", "salary_min": 480, "salary_max": 720}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
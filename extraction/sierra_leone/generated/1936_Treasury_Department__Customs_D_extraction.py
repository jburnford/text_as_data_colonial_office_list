"""
Sierra Leone Colonial Office List 1936 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1936

OFFICIALS = [
    {"name": "G. N. Farquhar", "canonical_name": "Farquhar, G. N.", "given_names": "G. N.", "surname": "Farquhar", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["M.C."]},
    {"name": "C. J. Hodgens", "canonical_name": "Hodgens, C. J.", "given_names": "C. J.", "surname": "Hodgens", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A", "honors": ["M.C."]},
    {"name": "C. S. Rayner", "canonical_name": "Rayner, C. S.", "given_names": "C. S.", "surname": "Rayner", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A", "honors": ["M.S.M."]},
    {"name": "J. Lawson", "canonical_name": "Lawson, J.", "given_names": "J.", "surname": "Lawson", "position": "Stock Verifier", "department": "Treasury Department - Sierra Leone", "salary_scale": "A"},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Staff Superintendent", "department": "Treasury Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "W. T. Martin", "canonical_name": "Martin, W. T.", "given_names": "W. T.", "surname": "Martin", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A", "salary_min": 600},
    {"name": "F. A. von Weiller", "canonical_name": "von Weiller, F. A.", "given_names": "F. A.", "surname": "von Weiller", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A", "location": "Freelton"},
    {"name": "M. A. Smith", "canonical_name": "Smith, M. A.", "given_names": "M. A.", "surname": "Smith", "position": "Supervisor", "department": "Customs Department - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "F. C. Campbell", "canonical_name": "Campbell, F. C.", "given_names": "F. C.", "surname": "Campbell", "position": "Supervisor", "department": "Customs Department - Sierra Leone", "salary_min": 360, "salary_max": 500}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1934 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1934

OFFICIALS = [
    {"name": "F. A. Mathias", "canonical_name": "Mathias, F. A.", "given_names": "F. A.", "surname": "Mathias", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "allowances": "Personal allowance 100l.", "honors": ["O.B.E."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "C. J. Hodgson", "canonical_name": "Hodgson, C. J.", "given_names": "C. J.", "surname": "Hodgson", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A", "honors": ["M.C."]},
    {"name": "C. S. Rayner", "canonical_name": "Rayner, C. S.", "given_names": "C. S.", "surname": "Rayner", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "African Assistant Treasurer", "department": "Treasury Department - Sierra Leone"},
    {"name": "J. Lawson", "canonical_name": "Lawson, J.", "given_names": "J.", "surname": "Lawson", "position": "Stock Verifier", "department": "Treasury Department - Sierra Leone", "salary_scale": "A", "salary_max": 600},
    {"name": "W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "W. T. Martin", "canonical_name": "Martin, W. T.", "given_names": "W. T.", "surname": "Martin", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A", "salary_min": 600},
    {"name": "F. A. von Weiller", "canonical_name": "Weiller, F. A. von", "given_names": "F. A.", "surname": "Weiller", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A", "location": "Freetown"},
    {"name": "J. D. M. Bourne", "canonical_name": "Bourne, J. D. M.", "given_names": "J. D. M.", "surname": "Bourne", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "A. G. Bowring", "canonical_name": "Bowring, A. G.", "given_names": "A. G.", "surname": "Bowring", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "H. G. Inay", "canonical_name": "Inay, H. G.", "given_names": "H. G.", "surname": "Inay", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. Rodway", "canonical_name": "Rodway, R.", "given_names": "R.", "surname": "Rodway", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. L. Wikne", "canonical_name": "Wikne, R. L.", "given_names": "R. L.", "surname": "Wikne", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_scale": "C", "military_rank": "Lieut. Comdr.", "honors": ["D.S.C."]},
    {"name": "H. Bowles", "canonical_name": "Bowles, H.", "given_names": "H.", "surname": "Bowles", "position": "Government Pilot", "department": "Port and Marine Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 264, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
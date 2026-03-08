"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "H. M. Lucie-Smith", "canonical_name": "Lucie-Smith, H. M.", "given_names": "H. M.", "surname": "Lucie-Smith", "position": "Comptroller of Customs", "department": "Customs - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "A. R. Carr", "canonical_name": "Carr, A. R.", "given_names": "A. R.", "surname": "Carr", "position": "Assistant Comptroller of Customs", "department": "Customs - Sierra Leone", "salary_scale": "B", "salary_min": 660, "salary_max": 900},
    {"name": "C. A. Asgill", "canonical_name": "Asgill, C. A.", "given_names": "C. A.", "surname": "Asgill", "position": "Collectors of Customs", "department": "Customs - Sierra Leone", "salary_scale": "B"},
    {"name": "O. M. Summerell", "canonical_name": "Summerell, O. M.", "given_names": "O. M.", "surname": "Summerell", "position": "Collectors of Customs", "department": "Customs - Sierra Leone", "salary_scale": "B"},
    {"name": "B. N. Dahniya", "canonical_name": "Dahniya, B. N.", "given_names": "B. N.", "surname": "Dahniya", "position": "Collectors of Customs", "department": "Customs - Sierra Leone", "salary_scale": "B"},
    {"name": "C. E. Donovan", "canonical_name": "Donovan, C. E.", "given_names": "C. E.", "surname": "Donovan", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 1350, "salary_max": 1350, "honors": ["C.B.E."], "allowances": "plus £150 non-pensionable allowance as Educational Adviser to the Government of Gambia"},
    {"name": "R. C. Allen", "canonical_name": "Allen, R. C.", "given_names": "R. C.", "surname": "Allen", "position": "Deputy Director", "department": "Education - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Director of Education", "department": "Education - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "C. Ll. Rice", "canonical_name": "Rice, C. Ll.", "given_names": "C. Ll.", "surname": "Rice", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "T. D. Evans", "canonical_name": "Evans, T. D.", "given_names": "T. D.", "surname": "Evans", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "A. D. J. Scott", "canonical_name": "Scott, A. D. J.", "given_names": "A. D. J.", "surname": "Scott", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "J. V. Taylor", "canonical_name": "Taylor, J. V.", "given_names": "J. V.", "surname": "Taylor", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "D. R. T. Goodwin", "canonical_name": "Goodwin, D. R. T.", "given_names": "D. R. T.", "surname": "Goodwin", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "A. L. Gibbs", "canonical_name": "Gibbs, A. L.", "given_names": "A. L.", "surname": "Gibbs", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "C. E. Tuboku-Metzger", "canonical_name": "Tuboku-Metzger, C. E.", "given_names": "C. E.", "surname": "Tuboku-Metzger", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A", "honors": ["M.B.E."]},
    {"name": "E. J. B. Williams", "canonical_name": "Williams, E. J. B.", "given_names": "E. J. B.", "surname": "Williams", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "J. P. Wright", "canonical_name": "Wright, J. P.", "given_names": "J. P.", "surname": "Wright", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "W. N. Mends", "canonical_name": "Mends, W. N.", "given_names": "W. N.", "surname": "Mends", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "L. J. Pratt", "canonical_name": "Pratt, L. J.", "given_names": "L. J.", "surname": "Pratt", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "H. A. M. Clarke", "canonical_name": "Clarke, H. A. M.", "given_names": "H. A. M.", "surname": "Clarke", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "R. McMurdo", "canonical_name": "McMurdo, R.", "given_names": "R.", "surname": "McMurdo", "position": "Education Officers", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "Miss M. R. Grigor", "canonical_name": "Grigor, M. R.", "given_names": "M. R.", "surname": "Grigor", "position": "Senior Lady Education Officer", "department": "Education - Sierra Leone", "salary_scale": "C.3"},
    {"name": "G. A. P. Hamilton", "canonical_name": "Hamilton, G. A. P.", "given_names": "G. A. P.", "surname": "Hamilton", "position": "Secretary", "department": "Education - Sierra Leone", "salary_scale": "B"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
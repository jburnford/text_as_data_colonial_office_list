"""
Gambia Colonial Office List 1949 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1949

OFFICIALS = [
    {"name": "Sir A. B. Wright", "canonical_name": "Wright, A. B.", "given_names": "A. B.", "surname": "Wright", "position": "Governor and Commander-in-Chief", "department": "Governor and Personal Staff - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 750, "honors": ["K.C.M.G.", "C.B.E.", "M.C."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Aide-de-Camp and Private Secretary", "department": "Governor and Personal Staff - Gambia", "salary_min": 415, "expatriation_pay": 125},
    {"name": "E. R. Ward", "canonical_name": "Ward, E. R.", "given_names": "E. R.", "surname": "Ward", "position": "Colonial Secretary", "department": "Administrative Service - Gambia", "salary_min": 1350, "expatriation_pay": 400, "duty_allowance": 100, "honors": ["C.M.G."]},
    {"name": "K. C. Jacobs", "canonical_name": "Jacobs, K. C.", "given_names": "K. C.", "surname": "Jacobs", "position": "Financial Secretary", "department": "Administrative Service - Gambia", "salary_min": 1175, "expatriation_pay": 350, "honors": ["O.B.E."]},
    {"name": "N. A. C. Weir", "canonical_name": "Weir, N. A. C.", "given_names": "N. A. C.", "surname": "Weir", "position": "Senior Commissioner", "department": "Administrative Service - Gambia", "salary_min": 1200, "expatriation_pay": 400, "honors": ["O.B.E."], "qualifications": ["E.D."]},
    {"name": "N. M. Asheton", "canonical_name": "Asheton, N. M.", "given_names": "N. M.", "surname": "Asheton", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A", "honors": ["O.B.E."]},
    {"name": "P. C. Hodgson", "canonical_name": "Hodgson, P. C.", "given_names": "P. C.", "surname": "Hodgson", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "G. H. Smith", "canonical_name": "Smith, G. H.", "given_names": "G. H.", "surname": "Smith", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "J. W. Stewart", "canonical_name": "Stewart, J. W.", "given_names": "J. W.", "surname": "Stewart", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A", "honors": ["D.F.C."]},
    {"name": "G. S. Kennedy", "canonical_name": "Kennedy, G. S.", "given_names": "G. S.", "surname": "Kennedy", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "D. A. Murphy", "canonical_name": "Murphy, D. A.", "given_names": "D. A.", "surname": "Murphy", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "J. V. Lister", "canonical_name": "Lister, J. V.", "given_names": "J. V.", "surname": "Lister", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "G. G. Davies", "canonical_name": "Davies, G. G.", "given_names": "G. G.", "surname": "Davies", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "A. Sinclair", "canonical_name": "Sinclair, A.", "given_names": "A.", "surname": "Sinclair", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "K. J. Frazer", "canonical_name": "Frazer, K. J.", "given_names": "K. J.", "surname": "Frazer", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "J. E. Roberts", "canonical_name": "Roberts, J. E.", "given_names": "J. E.", "surname": "Roberts", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "J. R. Chow", "canonical_name": "Chow, J. R.", "given_names": "J. R.", "surname": "Chow", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia", "salary_scale": "A"},
    {"name": "J. Sealy", "canonical_name": "Sealy, J.", "given_names": "J.", "surname": "Sealy", "position": "Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries", "department": "Administrative Service - Gambia"},
    {"name": "Miss M. Cooke", "canonical_name": "Cooke, M.", "given_names": "M.", "surname": "Cooke", "position": "Office Assistants", "department": "Administrative Service - Gambia"},
    {"name": "W. C. Cates", "canonical_name": "Cates, W. C.", "given_names": "W. C.", "surname": "Cates", "position": "Office Assistants", "department": "Administrative Service - Gambia"},
    {"name": "E. B. W. Carrol", "canonical_name": "Carrol, E. B. W.", "given_names": "E. B. W.", "surname": "Carrol", "position": "Accountant General", "department": "Accountant General - Gambia", "salary_scale": "B", "honors": ["O.B.E."]},
    {"name": "D. T. D. Taylor", "canonical_name": "Taylor, D. T. D.", "given_names": "D. T. D.", "surname": "Taylor", "position": "Assistant Accountants", "department": "Accountant General - Gambia", "salary_scale": "C"},
    {"name": "H. R. Monday", "canonical_name": "Monday, H. R.", "given_names": "H. R.", "surname": "Monday", "position": "Assistant Accountants", "department": "Accountant General - Gambia", "salary_scale": "C"},
    {"name": "J. H. Palmer", "canonical_name": "Palmer, J. H.", "given_names": "J. H.", "surname": "Palmer", "position": "Senior Agricultural Officer", "department": "Agricultural - Gambia", "salary_scale": "A"},
    {"name": "R. A. Kitching", "canonical_name": "Kitching, R. A.", "given_names": "R. A.", "surname": "Kitching", "position": "Agricultural Officers", "department": "Agricultural - Gambia", "salary_scale": "A"},
    {"name": "P. A. Donovan", "canonical_name": "Donovan, P. A.", "given_names": "P. A.", "surname": "Donovan", "position": "Agricultural Officers", "department": "Agricultural - Gambia", "salary_scale": "A"},
    {"name": "W. A. Wright", "canonical_name": "Wright, W. A.", "given_names": "W. A.", "surname": "Wright", "position": "Agricultural Officers", "department": "Agricultural - Gambia", "salary_scale": "A"},
    {"name": "K. S. Collins", "canonical_name": "Collins, K. S.", "given_names": "K. S.", "surname": "Collins", "position": "Principal Auditor", "department": "Audit - Gambia", "salary_min": 810, "expatriation_pay": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
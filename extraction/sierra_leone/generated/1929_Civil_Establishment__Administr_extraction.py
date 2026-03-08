"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "Sir H. B. Kittermaster", "canonical_name": "Kittermaster, H. B.", "given_names": "H. B.", "surname": "Kittermaster", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Sierra Leone", "salary_min": 1700, "salary_max": 1700, "duty_allowance": 350, "honors": ["K.B.E.", "C.M.G."]},
    {"name": "Major A. S. Lawrence", "canonical_name": "Lawrence, A. S.", "given_names": "A. S.", "surname": "Lawrence", "position": "Secretary to the Government", "department": "Civil Establishment - Sierra Leone", "salary_min": 900, "salary_max": 1100, "honors": ["D.S.O."], "military_rank": "Major"},
    {"name": "W. L. Heape", "canonical_name": "Heape, W. L.", "given_names": "W. L.", "surname": "Heape", "position": "Assistant Secretary to the Government", "department": "Civil Establishment - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "R. R. H. Jebb", "canonical_name": "Jebb, R. R. H.", "given_names": "R. R. H.", "surname": "Jebb", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 500, "salary_max": 700, "honors": ["O.B.E."], "military_rank": "Major"},
    {"name": "Major B. H. Horsley", "canonical_name": "Horsley, B. H.", "given_names": "B. H.", "surname": "Horsley", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 500, "salary_max": 700, "honors": ["D.S.O.", "M.C."], "military_rank": "Major"},
    {"name": "Capt. E. N. Park", "canonical_name": "Park, E. N.", "given_names": "E. N.", "surname": "Park", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 500, "salary_max": 700, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "R. H. Smith", "canonical_name": "Smith, R. H.", "given_names": "R. H.", "surname": "Smith", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "Capt. H. E. Long", "canonical_name": "Long, H. E.", "given_names": "H. E.", "surname": "Long", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800, "military_rank": "Captain"},
    {"name": "Capt. D. J. C. Walsh", "canonical_name": "Walsh, D. J. C.", "given_names": "D. J. C.", "surname": "Walsh", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800, "military_rank": "Captain"},
    {"name": "T. Donovan", "canonical_name": "Donovan, T.", "given_names": "T.", "surname": "Donovan", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800, "honors": ["D.C.M."]},
    {"name": "A. McCallum", "canonical_name": "McCallum, A.", "given_names": "A.", "surname": "McCallum", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800, "honors": ["M.C."]},
    {"name": "J. H. B. Murphy", "canonical_name": "Murphy, J. H. B.", "given_names": "J. H. B.", "surname": "Murphy", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "D. Forbes", "canonical_name": "Forbes, D.", "given_names": "D.", "surname": "Forbes", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "E. Barry", "canonical_name": "Barry, E.", "given_names": "E.", "surname": "Barry", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "F. J. Chambers", "canonical_name": "Chambers, F. J.", "given_names": "F. J.", "surname": "Chambers", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Commissioners", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "C. H. F. Plowman", "canonical_name": "Plowman, C. H. F.", "given_names": "C. H. F.", "surname": "Plowman", "position": "Consul at Harar", "department": "Administration - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "V. S. Bryan", "canonical_name": "Bryan, V. S.", "given_names": "V. S.", "surname": "Bryan", "position": "Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 800, "salary_max": 800},
    {"name": "D. L. Bethell", "canonical_name": "Bethell, D. L.", "given_names": "D. L.", "surname": "Bethell", "position": "Senior Assistant Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 550, "salary_max": 700}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
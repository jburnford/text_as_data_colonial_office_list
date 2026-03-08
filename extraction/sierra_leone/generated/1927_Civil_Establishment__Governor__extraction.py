"""
Sierra Leone Colonial Office List 1927 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1927

OFFICIALS = [
    {"name": "H. B. Kittermaster", "canonical_name": "Kittermaster, H. B.", "given_names": "H. B.", "surname": "Kittermaster", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Sierra Leone", "salary_min": 1700, "salary_max": 1700, "duty_allowance": 350, "honors": ["C.M.G.", "O.B.E."]},
    {"name": "A. S. Lawrance", "canonical_name": "Lawrance, A. S.", "given_names": "A. S.", "surname": "Lawrance", "position": "Secretary to the Government", "department": "Civil Establishment - Sierra Leone", "salary_min": 800, "salary_max": 1000, "military_rank": "Major", "honors": ["D.S.O."]},
    {"name": "W. L. Heape", "canonical_name": "Heape, W. L.", "given_names": "W. L.", "surname": "Heape", "position": "Assistant Secretary to the Government", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 600},
    {"name": "R. R. H. Jebb", "canonical_name": "Jebb, R. R. H.", "given_names": "R. R. H.", "surname": "Jebb", "position": "District Commissioner", "department": "Administration - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["O.B.E."]},
    {"name": "H. Rayne", "canonical_name": "Rayne, H.", "given_names": "H.", "surname": "Rayne", "position": "District Commissioner", "department": "Administration - Sierra Leone", "salary_min": 600, "salary_max": 700, "military_rank": "Major", "honors": ["O.B.E.", "M.C."]},
    {"name": "B. H. Horley", "canonical_name": "Horley, B. H.", "given_names": "B. H.", "surname": "Horley", "position": "District Commissioner", "department": "Administration - Sierra Leone", "salary_min": 500, "salary_max": 700, "military_rank": "Major", "honors": ["D.S.O.", "M.C."]},
    {"name": "E. N. Park", "canonical_name": "Park, E. N.", "given_names": "E. N.", "surname": "Park", "position": "District Commissioner", "department": "Administration - Sierra Leone", "salary_min": 500, "salary_max": 700, "military_rank": "Capt.", "honors": ["M.C."]},
    {"name": "J. Beattie", "canonical_name": "Beattie, J.", "given_names": "J.", "surname": "Beattie", "position": "District Commissioner", "department": "Administration - Sierra Leone", "salary_min": 500, "salary_max": 700, "honors": ["M.C."]},
    {"name": "C. H. F. Plowman", "canonical_name": "Plowman, C. H. F.", "given_names": "C. H. F.", "surname": "Plowman", "position": "Consul at Harar", "department": "Administration - Sierra Leone", "salary_min": 600, "salary_max": 700},
    {"name": "V. S. Bryan", "canonical_name": "Bryan, V. S.", "given_names": "V. S.", "surname": "Bryan", "position": "Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "D. L. Bethell", "canonical_name": "Bethell, D. L.", "given_names": "D. L.", "surname": "Bethell", "position": "Senior Assistant Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "G. R. Breeding", "canonical_name": "Breeding, G. R.", "given_names": "G. R.", "surname": "Breeding", "position": "Commandant", "department": "Police - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Lt.-Col.", "honors": ["D.S.O."]},
    {"name": "J. H. Bloomburgh", "canonical_name": "Bloomburgh, J. H.", "given_names": "J. H.", "surname": "Bloomburgh", "position": "Assistant Commandant", "department": "Police - Sierra Leone", "salary_min": 600, "salary_max": 600, "military_rank": "Capt.", "honors": ["O.B.E."]},
    {"name": "R. H. Smith", "canonical_name": "Smith, R. H.", "given_names": "R. H.", "surname": "Smith", "position": "District Police Officer", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "H. E. Long", "canonical_name": "Long, H. E.", "given_names": "H. E.", "surname": "Long", "position": "District Police Officer", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Capt."},
    {"name": "D. J. C. Walsh", "canonical_name": "Walsh, D. J. C.", "given_names": "D. J. C.", "surname": "Walsh", "position": "District Police Officer", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Capt."},
    {"name": "T. Donovan", "canonical_name": "Donovan, T.", "given_names": "T.", "surname": "Donovan", "position": "District Police Officer", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 500, "honors": ["D.C.M."]},
    {"name": "A. McCallum", "canonical_name": "McCallum, A.", "given_names": "A.", "surname": "McCallum", "position": "District Police Officer", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 500, "honors": ["M.C."]},
    {"name": "A. P. Oakes", "canonical_name": "Oakes, A. P.", "given_names": "A. P.", "surname": "Oakes", "position": "Pay and Quartermaster", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 500}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1925 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1925

OFFICIALS = [
    {"name": "S. S. Sawrey-Cookson", "canonical_name": "Sawrey-Cookson, S. S.", "given_names": "S. S.", "surname": "Sawrey-Cookson", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "C. M. Barton", "canonical_name": "Barton, C. M.", "given_names": "C. M.", "surname": "Barton", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800},
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "G. C. Coker", "canonical_name": "Coker, G. C.", "given_names": "G. C.", "surname": "Coker", "position": "Assistant Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "Geo. D. Williams", "canonical_name": "Williams, Geo. D.", "given_names": "Geo. D.", "surname": "Williams", "position": "Interpreter of Courts", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Sheriff's Bailiff and Beadle of the Court of Requests", "department": "Legal Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "W. M. Bright", "canonical_name": "Bright, W. M.", "given_names": "W. M.", "surname": "Bright", "position": "2nd Grade Clerk", "department": "Legal Adviser's Office - Gambia"},
    {"name": "C. J. Clarke", "canonical_name": "Clarke, C. J.", "given_names": "C. J.", "surname": "Clarke", "position": "One 3rd Grade Clerk", "department": "Legal Adviser's Office - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "W. W. Grosevior", "canonical_name": "Grosevior, W. W.", "given_names": "W. W.", "surname": "Grosevior", "position": "Two 4th Grade Clerks", "department": "Legal Adviser's Office - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "K. G. Davies", "canonical_name": "Davies, K. G.", "given_names": "K. G.", "surname": "Davies", "position": "Two 4th Grade Clerks", "department": "Legal Adviser's Office - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "W. B. Coker", "canonical_name": "Coker, W. B.", "given_names": "W. B.", "surname": "Coker", "position": "Clerk to Police Magistrate, 4th Grade", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "Capt. C. Greig", "canonical_name": "Greig, C.", "given_names": "C.", "surname": "Greig", "position": "Sheriff", "department": "Legal Department - Gambia", "military_rank": "Captain"},
    {"name": "W. B. Coker", "canonical_name": "Coker, W. B.", "given_names": "W. B.", "surname": "Coker", "position": "Clerk to Board of Education", "department": "Education - Gambia"},
    {"name": "Dr. E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["C.M.G.", "D.S.O."]},
    {"name": "Capt. E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "Major R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Travelling Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "Lt.-Col. G. E. Wannell", "canonical_name": "Wannell, G. E.", "given_names": "G. E.", "surname": "Wannell", "position": "Travelling Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["D.S.O."], "military_rank": "Lt.-Col."},
    {"name": "Major L. A. W. Brooks", "canonical_name": "Brooks, L. A. W.", "given_names": "L. A. W.", "surname": "Brooks", "position": "Two Assistants", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Major"},
    {"name": "Capt. S. H. Streeter", "canonical_name": "Streeter, S. H.", "given_names": "S. H.", "surname": "Streeter", "position": "Two Assistants", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
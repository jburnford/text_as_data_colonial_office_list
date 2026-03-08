"""
Gambia Colonial Office List 1921 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1921

OFFICIALS = [
    {"name": "S. S. Sourrey-Cookson", "canonical_name": "Sourrey-Cookson, S. S.", "given_names": "S. S.", "surname": "Sourrey-Cookson", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "E. M. Hov", "canonical_name": "Hov, E. M.", "given_names": "E. M.", "surname": "Hov", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800},
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "N. G. Taylor", "canonical_name": "Taylor, N. G.", "given_names": "N. G.", "surname": "Taylor", "position": "Assistant Clerk of Courts, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "Geo. D. Williams", "canonical_name": "Williams, Geo. D.", "given_names": "Geo. D.", "surname": "Williams", "position": "Interpreter of Courts", "department": "Legal Department - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Sheriff's Bailiff and Beadle of the Court of Requests", "department": "Legal Department - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "N. C. Johnson", "canonical_name": "Johnson, N. C.", "given_names": "N. C.", "surname": "Johnson", "position": "2nd Grade Clerk", "department": "Legal Adviser's Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "W. M. Bright", "canonical_name": "Bright, W. M.", "given_names": "W. M.", "surname": "Bright", "position": "2nd Grade Clerk", "department": "Legal Adviser's Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "C. J. Clarke", "canonical_name": "Clarke, C. J.", "given_names": "C. J.", "surname": "Clarke", "position": "3rd Grade Clerk", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "Capt. C. Greig", "canonical_name": "Greig, C.", "given_names": "C.", "surname": "Greig", "position": "Sheriff", "department": "Legal Department - Gambia", "military_rank": "Captain"},
    {"name": "Dr. E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960, "honors": ["D.S.O."], "qualifications": ["Dr."]},
    {"name": "Capt. H. F. Sprston", "canonical_name": "Sprston, H. F.", "given_names": "H. F.", "surname": "Sprston", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960, "military_rank": "Captain"},
    {"name": "Capt. E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960, "military_rank": "Captain"},
    {"name": "Capt. R. H. H. Whitehead", "canonical_name": "Whitehead, R. H. H.", "given_names": "R. H. H.", "surname": "Whitehead", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "Major R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
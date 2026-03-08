"""
Gambia Colonial Office List 1930 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1930

OFFICIALS = [
    {"name": "H. G. Hendrie", "canonical_name": "Hendrie, H. G.", "given_names": "H. G.", "surname": "Hendrie", "position": "Principal, Vocational School", "department": "Education - Gambia", "salary_min": 480, "salary_max": 920, "military_rank": "Captain", "honors": ["M.C."]},
    {"name": "E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Major", "honors": ["M.C."]},
    {"name": "L. A. W. Brooks", "canonical_name": "Brooks, L. A. W.", "given_names": "L. A. W.", "surname": "Brooks", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Major"},
    {"name": "P. Jeffs", "canonical_name": "Jeffs, P.", "given_names": "P.", "surname": "Jeffs", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain", "honors": ["M.C."]},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "T. W. Doke", "canonical_name": "Doke, T. W.", "given_names": "T. W.", "surname": "Doke", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72},
    {"name": "C. R. Bell", "canonical_name": "Bell, C. R.", "given_names": "C. R.", "surname": "Bell", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Bandmaster", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "D. D. Peters", "canonical_name": "Peters, D. D.", "given_names": "D. D.", "surname": "Peters", "position": "Chief Warden, 3rd Grade", "department": "Prison - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "L. W. Humphrey", "canonical_name": "Humphrey, L. W.", "given_names": "L. W.", "surname": "Humphrey", "position": "Chaplain", "department": "Prison - Gambia", "qualifications": ["Rev."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
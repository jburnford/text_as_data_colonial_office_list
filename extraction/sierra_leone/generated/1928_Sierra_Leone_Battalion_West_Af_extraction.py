"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "W. A. Taaffe", "canonical_name": "Taaffe, W. A.", "given_names": "W. A.", "surname": "Taaffe", "position": "Major", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 850, "salary_max": 850, "duty_allowance": 182, "military_rank": "Major"},
    {"name": "R. P. M. Davis", "canonical_name": "Davis, R. P. M.", "given_names": "R. P. M.", "surname": "Davis", "position": "Adjutant and Quartermaster", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "duty_allowance": 91, "military_rank": "Lieut."},
    {"name": "C. R. Carter", "canonical_name": "Carter, C. R.", "given_names": "C. R.", "surname": "Carter", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 750, "salary_max": 750, "honors": ["D.S.O."], "military_rank": "Captain"},
    {"name": "A. E. Salter", "canonical_name": "Salter, A. E.", "given_names": "A. E.", "surname": "Salter", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Captain"},
    {"name": "V. J. Bradley", "canonical_name": "Bradley, V. J.", "given_names": "V. J.", "surname": "Bradley", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Captain"},
    {"name": "G. W. Kempster", "canonical_name": "Kempster, G. W.", "given_names": "G. W.", "surname": "Kempster", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "honors": ["M.C."], "military_rank": "Lieutenant"},
    {"name": "A. S. W. Willis", "canonical_name": "Willis, A. S. W.", "given_names": "A. S. W.", "surname": "Willis", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "honors": ["M.C."], "military_rank": "Lieutenant"},
    {"name": "H. S. Thomas", "canonical_name": "Thomas, H. S.", "given_names": "H. S.", "surname": "Thomas", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "E. A. W. L. Crouch", "canonical_name": "Crouch, E. A. W. L.", "given_names": "E. A. W. L.", "surname": "Crouch", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "G. S. Renny", "canonical_name": "Renny, G. S.", "given_names": "G. S.", "surname": "Renny", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "allowances": "46l. signalling allowance", "military_rank": "Lieutenant"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
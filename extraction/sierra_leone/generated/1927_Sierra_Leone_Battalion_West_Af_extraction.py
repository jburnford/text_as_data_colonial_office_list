"""
Sierra Leone Colonial Office List 1927 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1927

OFFICIALS = [
    {"name": "W. A. Taaffe", "canonical_name": "Taaffe, W. A.", "given_names": "W. A.", "surname": "Taaffe", "position": "Major", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 850, "salary_max": 850, "duty_allowance": 182, "military_rank": "Major"},
    {"name": "R. P. M. Davis", "canonical_name": "Davis, R. P. M.", "given_names": "R. P. M.", "surname": "Davis", "position": "Adjutant and Quartermaster", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "duty_allowance": 91, "military_rank": "Lieutenant"},
    {"name": "C. R. Carter", "canonical_name": "Carter, C. R.", "given_names": "C. R.", "surname": "Carter", "position": "Captain", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 750, "salary_max": 750, "honors": ["D.S.O."], "military_rank": "Captain"},
    {"name": "R. M. Hall", "canonical_name": "Hall, R. M.", "given_names": "R. M.", "surname": "Hall", "position": "Captain", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "A. E. Salter", "canonical_name": "Salter, A. E.", "given_names": "A. E.", "surname": "Salter", "position": "Captain", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Captain"},
    {"name": "C. E. V. K. Peberdy", "canonical_name": "Peberdy, C. E. V. K.", "given_names": "C. E. V. K.", "surname": "Peberdy", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "G. W. Kempster", "canonical_name": "Kempster, G. W.", "given_names": "G. W.", "surname": "Kempster", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "honors": ["M.C."], "military_rank": "Lieutenant"},
    {"name": "V. J. Bradley", "canonical_name": "Bradley, V. J.", "given_names": "V. J.", "surname": "Bradley", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "G. S. Ronny", "canonical_name": "Ronny, G. S.", "given_names": "G. S.", "surname": "Ronny", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "allowances": "40l. signalling allowance", "military_rank": "Lieutenant"},
    {"name": "D. W. Gordon", "canonical_name": "Gordon, D. W.", "given_names": "D. W.", "surname": "Gordon", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "C. R. Swynnerton", "canonical_name": "Swynnerton, C. R.", "given_names": "C. R.", "surname": "Swynnerton", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "F. H. McCleary", "canonical_name": "McCleary, F. H.", "given_names": "F. H.", "surname": "McCleary", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "E. A. W. L. Crouch", "canonical_name": "Crouch, E. A. W. L.", "given_names": "E. A. W. L.", "surname": "Crouch", "position": "Lieutenant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
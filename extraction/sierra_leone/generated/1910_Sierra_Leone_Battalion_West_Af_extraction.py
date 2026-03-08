"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "F. N. le Mesurier", "canonical_name": "le Mesurier, F. N.", "given_names": "F. N.", "surname": "le Mesurier", "position": "Major", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 500, "salary_max": 500, "military_rank": "Major"},
    {"name": "R. V. Barker", "canonical_name": "Barker, R. V.", "given_names": "R. V.", "surname": "Barker", "position": "Adjutant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "military_rank": "Lieutenant"},
    {"name": "L. Murray", "canonical_name": "Murray, L.", "given_names": "L.", "surname": "Murray", "position": "Captain", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 400, "salary_max": 400, "military_rank": "Captain"},
    {"name": "R. E. Gordon", "canonical_name": "Gordon, R. E.", "given_names": "R. E.", "surname": "Gordon", "position": "Captain", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 400, "salary_max": 400, "military_rank": "Captain"},
    {"name": "E. G. Skelton", "canonical_name": "Skelton, E. G.", "given_names": "E. G.", "surname": "Skelton", "position": "Lieut. (local Capt.)", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 400, "salary_max": 400, "military_rank": "Lieutenant"},
    {"name": "E. H. Murphy", "canonical_name": "Murphy, E. H.", "given_names": "E. H.", "surname": "Murphy", "position": "Lieut. (local Capt.)", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 400, "salary_max": 400, "military_rank": "Lieutenant"},
    {"name": "H. H. Norman", "canonical_name": "Norman, H. H.", "given_names": "H. H.", "surname": "Norman", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Captain"},
    {"name": "R. H. Watson", "canonical_name": "Watson, R. H.", "given_names": "R. H.", "surname": "Watson", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Captain"},
    {"name": "F. N. Thorne", "canonical_name": "Thorne, F. N.", "given_names": "F. N.", "surname": "Thorne", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Lieutenant"},
    {"name": "M. H. C. De C. De B. Wickham", "canonical_name": "Wickham, M. H. C. De C. De B.", "given_names": "M. H. C. De C. De B.", "surname": "Wickham", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Lieutenant"},
    {"name": "J. W. Chamley", "canonical_name": "Chamley, J. W.", "given_names": "J. W.", "surname": "Chamley", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Lieutenant"},
    {"name": "A. F. Thomas", "canonical_name": "Thomas, A. F.", "given_names": "A. F.", "surname": "Thomas", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Lieutenant"},
    {"name": "R. V. Barker", "canonical_name": "Barker, R. V.", "given_names": "R. V.", "surname": "Barker", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Lieutenant"},
    {"name": "J. S. M. Corrie", "canonical_name": "Corrie, J. S. M.", "given_names": "J. S. M.", "surname": "Corrie", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Lieutenant"},
    {"name": "J. L. Berne", "canonical_name": "Berne, J. L.", "given_names": "J. L.", "surname": "Berne", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Lieutenant"},
    {"name": "A. N. Ogilvie", "canonical_name": "Ogilvie, A. N.", "given_names": "A. N.", "surname": "Ogilvie", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Lieutenant"},
    {"name": "A. Ross-Hume", "canonical_name": "Ross-Hume, A.", "given_names": "A.", "surname": "Ross-Hume", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Lieutenant"},
    {"name": "J. G. Collins", "canonical_name": "Collins, J. G.", "given_names": "J. G.", "surname": "Collins", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "2nd Lieutenant"},
    {"name": "H. H. Thompson", "canonical_name": "Thompson, H. H.", "given_names": "H. H.", "surname": "Thompson", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "2nd Lieutenant"},
    {"name": "M. S. Deen", "canonical_name": "Deen, M. S.", "given_names": "M. S.", "surname": "Deen", "position": "Paymaster's Clerk", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "S. J. Coker", "canonical_name": "Coker, S. J.", "given_names": "S. J.", "surname": "Coker", "position": "Quartermaster's Clerk", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "J. B. Macauley", "canonical_name": "Macauley, J. B.", "given_names": "J. B.", "surname": "Macauley", "position": "Company Pay Clerks", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "W. R. Macauley", "canonical_name": "Macauley, W. R.", "given_names": "W. R.", "surname": "Macauley", "position": "Company Pay Clerks", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "G. E. M. Hughes", "canonical_name": "Hughes, G. E. M.", "given_names": "G. E. M.", "surname": "Hughes", "position": "Company Pay Clerks", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "E. S. B. Francis", "canonical_name": "Francis, E. S. B.", "given_names": "E. S. B.", "surname": "Francis", "position": "Company Pay Clerks", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. M. Jacobs", "canonical_name": "Jacobs, J. M.", "given_names": "J. M.", "surname": "Jacobs", "position": "Orderly Room Clerk", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 50, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
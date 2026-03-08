"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "W. C. N. Hastings", "canonical_name": "Hastings, W. C. N.", "given_names": "W. C. N.", "surname": "Hastings", "position": "Lieut.-Colonel", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "duty_allowance": 120, "military_rank": "Lieut.-Colonel"},
    {"name": "A. N. Ogilvie", "canonical_name": "Ogilvie, A. N.", "given_names": "A. N.", "surname": "Ogilvie", "position": "Major", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 620, "salary_max": 620, "duty_allowance": 100, "military_rank": "Major"},
    {"name": "G. Dawes", "canonical_name": "Dawes, G.", "given_names": "G.", "surname": "Dawes", "position": "Brevet Major", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 520, "salary_max": 520, "duty_allowance": 48, "military_rank": "Major"},
    {"name": "J. F. Drake", "canonical_name": "Drake, J. F.", "given_names": "J. F.", "surname": "Drake", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 520, "salary_max": 520, "duty_allowance": 48, "military_rank": "Captain"},
    {"name": "R. M. S. Baynes", "canonical_name": "Baynes, R. M. S.", "given_names": "R. M. S.", "surname": "Baynes", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 520, "salary_max": 520, "duty_allowance": 48, "military_rank": "Captain"},
    {"name": "C. D. Acheson", "canonical_name": "Acheson, C. D.", "given_names": "C. D.", "surname": "Acheson", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 520, "salary_max": 520, "duty_allowance": 48, "military_rank": "Captain"},
    {"name": "F. L. Schultze", "canonical_name": "Schultze, F. L.", "given_names": "F. L.", "surname": "Schultze", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "G. L. Strachan", "canonical_name": "Strachan, G. L.", "given_names": "G. L.", "surname": "Strachan", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "J. Marshall", "canonical_name": "Marshall, J.", "given_names": "J.", "surname": "Marshall", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "E. Harnetty", "canonical_name": "Harnetty, E.", "given_names": "E.", "surname": "Harnetty", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "C. W. Campbell", "canonical_name": "Campbell, C. W.", "given_names": "C. W.", "surname": "Campbell", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "N. McIver", "canonical_name": "McIver, N.", "given_names": "N.", "surname": "McIver", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "P. A. Calton", "canonical_name": "Calton, P. A.", "given_names": "P. A.", "surname": "Calton", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "A. J. Elliott", "canonical_name": "Elliott, A. J.", "given_names": "A. J.", "surname": "Elliott", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "J. L. Smith", "canonical_name": "Smith, J. L.", "given_names": "J. L.", "surname": "Smith", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "V. A. Smith", "canonical_name": "Smith, V. A.", "given_names": "V. A.", "surname": "Smith", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
    {"name": "W. O'Connor", "canonical_name": "O'Connor, W.", "given_names": "W.", "surname": "O'Connor", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 420, "salary_max": 470, "military_rank": "Lieutenant"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
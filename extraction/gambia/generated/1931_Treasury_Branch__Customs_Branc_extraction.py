"""
Gambia Colonial Office List 1931 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1931

OFFICIALS = [
    {"name": "R. A. Brown", "canonical_name": "Brown, R. A.", "given_names": "R. A.", "surname": "Brown", "position": "Accountant", "department": "Treasury - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "O. E. Kernahan", "canonical_name": "Kernahan, O. E.", "given_names": "O. E.", "surname": "Kernahan", "position": "Supervisor of Customs", "department": "Customs - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "Landing Waiter", "department": "Customs - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "I. B. Y. Jobe", "canonical_name": "Jobe, I. B. Y.", "given_names": "I. B. Y.", "surname": "Jobe", "position": "Landing Waiter", "department": "Customs - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "W. K. Horne", "canonical_name": "Horne, W. K.", "given_names": "W. K.", "surname": "Horne", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "A. G. B. Manson", "canonical_name": "Manson, A. G. B.", "given_names": "A. G. B.", "surname": "Manson", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 600, "salary_max": 920},
    {"name": "A. W. Lewey", "canonical_name": "Lewey, A. W.", "given_names": "A. W.", "surname": "Lewey", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800, "military_rank": "Major"},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Sheriff", "department": "Legal Department - Gambia"},
    {"name": "W. T. Hamlyn", "canonical_name": "Hamlyn, W. T.", "given_names": "W. T.", "surname": "Hamlyn", "position": "Superintendent of Education", "department": "Education - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "H. G. Hendrie", "canonical_name": "Hendrie, H. G.", "given_names": "H. G.", "surname": "Hendrie", "position": "Principal, Vocational School", "department": "Education - Gambia", "salary_min": 480, "salary_max": 920, "military_rank": "Capt.", "honors": ["M.C."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
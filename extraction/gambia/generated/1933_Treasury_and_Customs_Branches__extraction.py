"""
Gambia Colonial Office List 1933 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1933

OFFICIALS = [
    {"name": "M. M. Auchinleck", "canonical_name": "Auchinleck, M. M.", "given_names": "M. M.", "surname": "Auchinleck", "position": "Assistant Receiver-General", "department": "Treasury - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "R. A. Brown", "canonical_name": "Brown, R. A.", "given_names": "R. A.", "surname": "Brown", "position": "Accountant, Treasury", "department": "Treasury - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "O. E. Kernahan", "canonical_name": "Kernahan, O. E.", "given_names": "O. E.", "surname": "Kernahan", "position": "Supervisor of Customs", "department": "Customs - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "Chief Clerk, 1st Grade", "department": "Customs - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "Customs Landing Waiter", "department": "Customs - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "I. B. M. Y. Jobe", "canonical_name": "Jobe, I. B. M. Y.", "given_names": "I. B. M. Y.", "surname": "Jobe", "position": "Customs Landing Waiter", "department": "Customs - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "A. Wallis", "canonical_name": "Wallis, A.", "given_names": "A.", "surname": "Wallis", "position": "Engineer and Surveyor", "department": "Posts and Telegraphs - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "Postmaster", "department": "Posts and Telegraphs - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "W. K. Horne", "canonical_name": "Horne, W. K.", "given_names": "W. K.", "surname": "Horne", "position": "Judge of the Supreme Court", "department": "Judicial - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "A. G. B. Manson", "canonical_name": "Manson, A. G. B.", "given_names": "A. G. B.", "surname": "Manson", "position": "Legal Adviser", "department": "Legal - Gambia", "salary_min": 600, "salary_max": 900},
    {"name": "M. D. Lyon", "canonical_name": "Lyon, M. D.", "given_names": "M. D.", "surname": "Lyon", "position": "Police Magistrate", "department": "Legal - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Clerk of Courts, 1st Grade", "department": "Judicial - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Sheriff", "department": "Police - Gambia"},
    {"name": "W. T. Hamlyn", "canonical_name": "Hamlyn, W. T.", "given_names": "W. T.", "surname": "Hamlyn", "position": "Superintendent of Education", "department": "Education - Gambia", "salary_min": 400, "salary_max": 720}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
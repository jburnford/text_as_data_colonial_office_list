"""
Gambia Colonial Office List 1932 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1932

OFFICIALS = [
    {"name": "H. Densham Smith", "canonical_name": "Smith, H. Densham", "given_names": "H. Densham", "surname": "Smith", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "M. M. Auchinleck", "canonical_name": "Auchinleck, M. M.", "given_names": "M. M.", "surname": "Auchinleck", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "A. T. Shill", "canonical_name": "Shill, A. T.", "given_names": "A. T.", "surname": "Shill", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "Chief Clerk, 1st Grade", "department": "Receiver-General's Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "R. A. Brown", "canonical_name": "Brown, R. A.", "given_names": "R. A.", "surname": "Brown", "position": "Accountant", "department": "Treasury Branch - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "O. E. Kernahan", "canonical_name": "Kernahan, O. E.", "given_names": "O. E.", "surname": "Kernahan", "position": "Supervisor of Customs", "department": "Customs Branch - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "Landing Waiter (2nd Grade)", "department": "Customs Branch - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "I. B. Y. Jobe", "canonical_name": "Jobe, I. B. Y.", "given_names": "I. B. Y.", "surname": "Jobe", "position": "Landing Waiter (2nd Grade)", "department": "Customs Branch - Gambia", "salary_min": 160, "salary_max": 230},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
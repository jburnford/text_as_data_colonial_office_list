"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "E. J. Cameron", "canonical_name": "Cameron, E. J.", "given_names": "E. J.", "surname": "Cameron", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "honors": ["C.M.G."]},
    {"name": "Capt. A. M. Inglis", "canonical_name": "Inglis, A. M.", "given_names": "A. M.", "surname": "Inglis", "position": "Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250, "military_rank": "Captain"},
    {"name": "J. P. Joof", "canonical_name": "Joof, J. P.", "given_names": "J. P.", "surname": "Joof", "position": "Governor's Clerk and Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "W. T. Campbell", "canonical_name": "Campbell, W. T.", "given_names": "W. T.", "surname": "Campbell", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "A. C. Knollys", "canonical_name": "Knollys, A. C.", "given_names": "A. C.", "surname": "Knollys", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 50},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "Chief Clerk", "department": "Secretariat - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "First Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "C. Gwyn", "canonical_name": "Gwyn, C.", "given_names": "C.", "surname": "Gwyn", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 100, "allowances": "30l. as Chairman of Navigation and Pilotage Board"},
    {"name": "J. Iles Lauder", "canonical_name": "Lauder, J. Iles", "given_names": "J. Iles", "surname": "Lauder", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "J. C. B. Astley", "canonical_name": "Astley, J. C. B.", "given_names": "J. C. B.", "surname": "Astley", "position": "Correspondence Clerk", "department": "Receiver-General's Department - Gambia", "salary_min": 30, "salary_max": 40},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
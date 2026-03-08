"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "E. J. Cameron", "canonical_name": "Cameron, E. J.", "given_names": "E. J.", "surname": "Cameron", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "honors": ["C.M.G."]},
    {"name": "J. P. Joof", "canonical_name": "Joof, J. P.", "given_names": "J. P.", "surname": "Joof", "position": "1st Grade Clerk and Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 130, "salary_max": 160, "allowances": "personal allowance 40l. per annum"},
    {"name": "W. T. Campbell", "canonical_name": "Campbell, W. T.", "given_names": "W. T.", "surname": "Campbell", "position": "Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "A. C. Knollys", "canonical_name": "Knollys, A. C.", "given_names": "A. C.", "surname": "Knollys", "position": "Assistant Colonial Secretary", "department": "Secretariat - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 50},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "Chief Clerk", "department": "Secretariat - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "S. A. Riley", "canonical_name": "Riley, S. A.", "given_names": "S. A.", "surname": "Riley", "position": "2nd Clerk", "department": "Secretariat - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "N. E. Williams", "canonical_name": "Williams, N. E.", "given_names": "N. E.", "surname": "Williams", "position": "Chief Printer", "department": "Printing Branch - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "Chief Compositor", "department": "Printing Branch - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "O. D. Cummings", "canonical_name": "Cummings, O. D.", "given_names": "O. D.", "surname": "Cummings", "position": "Two 2nd Class Compositors", "department": "Printing Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "V. A. John", "canonical_name": "John, V. A.", "given_names": "V. A.", "surname": "John", "position": "Two 2nd Class Compositors", "department": "Printing Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "E. Sae", "canonical_name": "Sae, E.", "given_names": "E.", "surname": "Sae", "position": "Two 3rd Class Compositors", "department": "Printing Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "G. E. R. Hughes", "canonical_name": "Hughes, G. E. R.", "given_names": "G. E. R.", "surname": "Hughes", "position": "Two 3rd Class Compositors", "department": "Printing Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "C. Gwyn", "canonical_name": "Gwyn, C.", "given_names": "C.", "surname": "Gwyn", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 100, "allowances": "30l. as Chairman of Navigation and Pilotage Board"},
    {"name": "J. Iles Lauder", "canonical_name": "Lauder, J. Iles", "given_names": "J. Iles", "surname": "Lauder", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "V. E. Johnson", "canonical_name": "Johnson, V. E.", "given_names": "V. E.", "surname": "Johnson", "position": "6th Grade Correspondence Clerk", "department": "Receiver-General's Department - Gambia", "salary_min": 30, "salary_max": 40}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
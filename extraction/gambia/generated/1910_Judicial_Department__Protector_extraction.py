"""
Gambia Colonial Office List 1910 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1910

OFFICIALS = [
    {"name": "Hon. E. A. Hume", "canonical_name": "Hume, E. A.", "given_names": "E. A.", "surname": "Hume", "position": "Chief Magistrate", "department": "Judicial Department - Gambia", "salary_min": 750, "salary_max": 750, "honors": ["Hon."]},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Judicial Department - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "A. T. Spilsbury", "canonical_name": "Spilsbury, A. T.", "given_names": "A. T.", "surname": "Spilsbury", "position": "Assistant Clerk of Courts", "department": "Judicial Department - Gambia", "salary_min": 45, "salary_max": 45},
    {"name": "F. M. Fye", "canonical_name": "Fye, F. M.", "given_names": "F. M.", "surname": "Fye", "position": "Interpreter", "department": "Judicial Department - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "Joseph Brown", "canonical_name": "Brown, Joseph", "given_names": "Joseph", "surname": "Brown", "position": "Sheriff", "department": "Judicial Department - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Beadle and Bailiff", "department": "Judicial Department - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "H. L. Pryce", "canonical_name": "Pryce, H. L.", "given_names": "H. L.", "surname": "Pryce", "position": "Travelling Commissioner, First Class", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 500},
    {"name": "G. H. Sangater", "canonical_name": "Sangater, G. H.", "given_names": "G. H.", "surname": "Sangater", "position": "Travelling Commissioner, Second Class", "department": "Protectorate - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "W. B. Stanley", "canonical_name": "Stanley, W. B.", "given_names": "W. B.", "surname": "Stanley", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem", "allowances": "50l. a year"},
    {"name": "J. K. McCallum", "canonical_name": "McCallum, J. K.", "given_names": "J. K.", "surname": "McCallum", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"},
    {"name": "H. F. Sproston", "canonical_name": "Sproston, H. F.", "given_names": "H. F.", "surname": "Sproston", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"},
    {"name": "R. D. F. Oldman", "canonical_name": "Oldman, R. D. F.", "given_names": "R. D. F.", "surname": "Oldman", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 400, "salary_max": 400, "duty_allowance": 96, "military_rank": "Captain", "honors": ["D.S.O."]},
    {"name": "W. J. J. S. Hackett-Smith", "canonical_name": "Hackett-Smith, W. J. J. S.", "given_names": "W. J. J. S.", "surname": "Hackett-Smith", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 325, "salary_max": 325, "military_rank": "Lieutenant"},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 325, "salary_max": 325, "military_rank": "Lieutenant"},
    {"name": "G. B. Morey", "canonical_name": "Morey, G. B.", "given_names": "G. B.", "surname": "Morey", "position": "Colour-Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "duty_allowance": 24},
    {"name": "P. L. Webb", "canonical_name": "Webb, P. L.", "given_names": "P. L.", "surname": "Webb", "position": "Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "Joseph Brown", "canonical_name": "Brown, Joseph", "given_names": "Joseph", "surname": "Brown", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 350, "salary_max": 350, "allowances": "50l. personal allowance", "duty_allowance": 50},
    {"name": "T. B. Bracken", "canonical_name": "Bracken, T. B.", "given_names": "T. B.", "surname": "Bracken", "position": "Assistant Superintendent", "department": "Police Force - Gambia", "salary_min": 250, "salary_max": 250, "per_diem": "2s. 3d. per diem"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1907 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1907

OFFICIALS = [
    {"name": "H. L. Pryce", "canonical_name": "Pryce, H. L.", "given_names": "H. L.", "surname": "Pryce", "position": "Travelling Commissioner, First Class", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 500},
    {"name": "G. H. Sangster", "canonical_name": "Sangster, G. H.", "given_names": "G. H.", "surname": "Sangster", "position": "Travelling Commissioner, Second Class", "department": "Protectorate - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "W. B. Stanley", "canonical_name": "Stanley, W. B.", "given_names": "W. B.", "surname": "Stanley", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"},
    {"name": "J. K. McCallum", "canonical_name": "McCallum, J. K.", "given_names": "J. K.", "surname": "McCallum", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"},
    {"name": "H. F. Sproston", "canonical_name": "Sproston, H. F.", "given_names": "H. F.", "surname": "Sproston", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"},
    {"name": "W. C. N. Hastings", "canonical_name": "Hastings, W. C. N.", "given_names": "W. C. N.", "surname": "Hastings", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 400, "salary_max": 400, "honors": ["D.S.O."], "military_rank": "Captain"},
    {"name": "P. J. B. Heelas", "canonical_name": "Heelas, P. J. B.", "given_names": "P. J. B.", "surname": "Heelas", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 325, "salary_max": 325, "military_rank": "Lieutenant"},
    {"name": "P. L. Webb", "canonical_name": "Webb, P. L.", "given_names": "P. L.", "surname": "Webb", "position": "Colour-Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "duty_allowance": 24},
    {"name": "Geo. Stone", "canonical_name": "Stone, Geo.", "given_names": "Geo.", "surname": "Stone", "position": "Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "Joseph Brown", "canonical_name": "Brown, Joseph", "given_names": "Joseph", "surname": "Brown", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 350, "salary_max": 350, "allowances": "50l. personal allowance", "duty_allowance": 50},
    {"name": "T. B. Bracken", "canonical_name": "Bracken, T. B.", "given_names": "T. B.", "surname": "Bracken", "position": "Assistant Superintendent", "department": "Police Force - Gambia", "salary_min": 250, "salary_max": 250, "allowances": "forage allowance of 2s. 3d. per diem each"},
    {"name": "Joseph Brown", "canonical_name": "Brown, Joseph", "given_names": "Joseph", "surname": "Brown", "position": "Inspector of Prisons", "department": "Prison - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "C. C. Johnson", "canonical_name": "Johnson, C. C.", "given_names": "C. C.", "surname": "Johnson", "position": "Gaoler", "department": "Prison - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "T. T. Turner", "canonical_name": "Turner, T. T.", "given_names": "T. T.", "surname": "Turner", "position": "Chief Warder", "department": "Prison - Gambia", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
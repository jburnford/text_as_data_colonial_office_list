"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Captain W. P. B. Beal", "canonical_name": "Beal, W. P. B.", "given_names": "W. P. B.", "surname": "Beal",
     "position": "Principal Veterinary Officer", "department": "Veterinary Department - Gold Coast",
     "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["M.R.C.V.S."], "military_rank": "Captain"},
    {"name": "Capt. S. R. Rippon", "canonical_name": "Rippon, S. R.", "given_names": "S. R.", "surname": "Rippon",
     "position": "Veterinary Officer", "department": "Veterinary Department - Gold Coast",
     "salary_min": 600, "salary_max": 920, "allowances": "72l. seniority allowance", "qualifications": ["M.R.C.V.S."], "military_rank": "Captain"},
    {"name": "Capt. D. G. Grealy", "canonical_name": "Grealy, D. G.", "given_names": "D. G.", "surname": "Grealy",
     "position": "Veterinary Officer", "department": "Veterinary Department - Gold Coast",
     "salary_min": 600, "salary_max": 920, "allowances": "72l. seniority allowance", "qualifications": ["M.R.C.V.S."], "military_rank": "Captain"},
    {"name": "Lieut. A. E. Miller", "canonical_name": "Miller, A. E.", "given_names": "A. E.", "surname": "Miller",
     "position": "Inspector of Livestock", "department": "Veterinary Department - Gold Coast",
     "salary_min": 480, "salary_max": 720, "honors": ["M.C."], "military_rank": "Lieutenant"},
    {"name": "Gurbakhsh Singh", "canonical_name": "Singh, Gurbakhsh", "given_names": "Gurbakhsh", "surname": "Singh",
     "position": "Veterinary Superintendent", "department": "Veterinary Department - Gold Coast",
     "salary_min": 300, "salary_max": 400}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
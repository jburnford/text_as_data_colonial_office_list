"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "the Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Inspector of Schools", "department": "Education - Gambia"},
    {"name": "C. J. Clarke", "canonical_name": "Clarke, C. J.", "given_names": "C. J.", "surname": "Clarke", "position": "Clerk to Board of Education", "department": "Education - Gambia"},
    {"name": "H. L. Pryce", "canonical_name": "Pryce, H. L.", "given_names": "H. L.", "surname": "Pryce", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "honors": ["C.M.G."], "per_diem": "10s. per diem travelling allowance", "salary_min": 350, "salary_max": 550},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "honors": ["D.S.O."], "per_diem": "10s. per diem travelling allowance", "salary_min": 350, "salary_max": 550},
    {"name": "J. K. McCallum", "canonical_name": "McCallum, J. K.", "given_names": "J. K.", "surname": "McCallum", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "per_diem": "10s. per diem travelling allowance", "salary_min": 350, "salary_max": 550},
    {"name": "H. F. Sproston", "canonical_name": "Sproston, H. F.", "given_names": "H. F.", "surname": "Sproston", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "military_rank": "Captain", "per_diem": "10s. per diem travelling allowance", "salary_min": 350, "salary_max": 550},
    {"name": "E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "military_rank": "Captain", "per_diem": "10s. per diem travelling allowance", "salary_min": 350, "salary_max": 550},
    {"name": "R. Law", "canonical_name": "Law, R.", "given_names": "R.", "surname": "Law", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "military_rank": "Captain", "honors": ["M.C."], "salary_min": 400, "salary_max": 400, "allowances": "command pay, 96l."},
    {"name": "O. W. Warren", "canonical_name": "Warren, O. W.", "given_names": "O. W.", "surname": "Warren", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 300, "salary_max": 300},
    {"name": "A. E. Coombs", "canonical_name": "Coombs, A. E.", "given_names": "A. E.", "surname": "Coombs", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 300, "salary_max": 300},
    {"name": "F. MacFarlane", "canonical_name": "MacFarlane, F.", "given_names": "F.", "surname": "MacFarlane", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 300, "salary_max": 300},
    {"name": "T. Fitz Simons", "canonical_name": "Fitz Simons, T.", "given_names": "T.", "surname": "Fitz Simons", "position": "Colour-Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "duty_allowance": 24, "per_diem": "2s. 6d. per diem messing allowance"},
    {"name": "G. W. Woodard", "canonical_name": "Woodard, G. W.", "given_names": "G. W.", "surname": "Woodard", "position": "Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "per_diem": "2s. 6d. per diem messing allowance"},
    {"name": "Joseph Jobe", "canonical_name": "Jobe, Joseph", "given_names": "Joseph", "surname": "Jobe", "position": "Clerk and Schoolmaster", "department": "West African Frontier Force - Gambia", "salary_min": 75, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
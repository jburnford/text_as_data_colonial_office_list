"""
Gambia Colonial Office List 1918 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1918

OFFICIALS = [
    {"name": "the Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Inspector of Schools", "department": "Education - Gambia"},
    {"name": "M. E. Grant", "canonical_name": "Grant, M. E.", "given_names": "M. E.", "surname": "Grant", "position": "Clerk to Board of Education", "department": "Education - Gambia"},
    {"name": "H. L. Pryce", "canonical_name": "Pryce, H. L.", "given_names": "H. L.", "surname": "Pryce", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "honors": ["C.M.G."], "salary_min": 350, "salary_max": 550, "per_diem": "10s. per diem travelling allowance"},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "honors": ["D.S.O."], "salary_min": 350, "salary_max": 550, "per_diem": "10s. per diem travelling allowance"},
    {"name": "J. K. McCallum", "canonical_name": "McCallum, J. K.", "given_names": "J. K.", "surname": "McCallum", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "per_diem": "10s. per diem travelling allowance"},
    {"name": "H. F. Sproston", "canonical_name": "Sproston, H. F.", "given_names": "H. F.", "surname": "Sproston", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "military_rank": "Captain", "salary_min": 350, "salary_max": 550, "per_diem": "10s. per diem travelling allowance"},
    {"name": "K. B. Leese", "canonical_name": "Leese, K. B.", "given_names": "K. B.", "surname": "Leese", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "military_rank": "Captain", "salary_min": 350, "salary_max": 550, "per_diem": "10s. per diem travelling allowance"},
    {"name": "R. Law", "canonical_name": "Law, R.", "given_names": "R.", "surname": "Law", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "military_rank": "Captain", "honors": ["M.C."], "salary_min": 400, "salary_max": 400, "command_pay": 96},
    {"name": "F. C. Devlin", "canonical_name": "Devlin, F. C.", "given_names": "F. C.", "surname": "Devlin", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 300, "salary_max": 300},
    {"name": "R. M. Spens", "canonical_name": "Spens, R. M.", "given_names": "R. M.", "surname": "Spens", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 300, "salary_max": 300},
    {"name": "O. W. Warren", "canonical_name": "Warren, O. W.", "given_names": "O. W.", "surname": "Warren", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 300, "salary_max": 300},
    {"name": "A. E. Coombe", "canonical_name": "Coombe, A. E.", "given_names": "A. E.", "surname": "Coombe", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 300, "salary_max": 300},
    {"name": "J. M. B. Durham", "canonical_name": "Durham, J. M. B.", "given_names": "J. M. B.", "surname": "Durham", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 300, "salary_max": 300},
    {"name": "T. Fitz Svieder", "canonical_name": "Fitz Svieder, T.", "given_names": "T.", "surname": "Fitz Svieder", "position": "Colour-Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "duty_allowance": 24, "per_diem": "2s. 6d. per diem messing allowance"},
    {"name": "I. W. Woodard", "canonical_name": "Woodard, I. W.", "given_names": "I. W.", "surname": "Woodard", "position": "Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "per_diem": "2s. 6d. per diem messing allowance"},
    {"name": "Joseph Jobe", "canonical_name": "Jobe, Joseph", "given_names": "Joseph", "surname": "Jobe", "position": "Clerk and Schoolmaster", "department": "West African Frontier Force - Gambia", "salary_min": 75, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
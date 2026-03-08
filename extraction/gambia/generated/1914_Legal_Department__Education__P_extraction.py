"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "F. A. Van der Meulen", "canonical_name": "Van der Meulen, F. A.", "given_names": "F. A.", "surname": "Van der Meulen", "position": "Chief Magistrate", "department": "Legal Department - Gambia", "salary_min": 750, "salary_max": 750},
    {"name": "E. St. J. Jackson", "canonical_name": "Jackson, E. St. J.", "given_names": "E. St. J.", "surname": "Jackson", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "M. F. J. McDonnell", "canonical_name": "McDonnell, M. F. J.", "given_names": "M. F. J.", "surname": "McDonnell", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "J. Finden Dailey", "canonical_name": "Dailey, J. Finden", "given_names": "J. Finden", "surname": "Dailey", "position": "Clerks to Legal Assistant", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerks to Legal Assistant", "department": "Legal Department - Gambia", "salary_min": 24, "salary_max": 30},
    {"name": "J. R. E. Lunock", "canonical_name": "Lunock, J. R. E.", "given_names": "J. R. E.", "surname": "Lunock", "position": "Interpreter", "department": "Legal Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Beadle and Bailiff", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "C. Creig", "canonical_name": "Creig, C.", "given_names": "C.", "surname": "Creig", "position": "Sheriff", "department": "Legal Department - Gambia"},
    {"name": "J. F. Dailey", "canonical_name": "Dailey, J. F.", "given_names": "J. F.", "surname": "Dailey", "position": "Clerk", "department": "Education - Gambia", "salary_min": 10, "salary_max": 10},
    {"name": "T. J. Gibbs", "canonical_name": "Gibbs, T. J.", "given_names": "T. J.", "surname": "Gibbs", "position": "Town Warden", "department": "Education - Gambia", "location": "Bathurst", "salary_min": 250, "salary_max": 300},
    {"name": "H. L. Pryce", "canonical_name": "Pryce, H. L.", "given_names": "H. L.", "surname": "Pryce", "position": "Travelling Commissioners, First Class", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 500, "honors": ["C.M.G."]},
    {"name": "J. K. McCallum", "canonical_name": "McCallum, J. K.", "given_names": "J. K.", "surname": "McCallum", "position": "Travelling Commissioners, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem"},
    {"name": "H. F. Sproston", "canonical_name": "Sproston, H. F.", "given_names": "H. F.", "surname": "Sproston", "position": "Travelling Commissioners, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem"},
    {"name": "E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioners, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem", "military_rank": "Capt."},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioners, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
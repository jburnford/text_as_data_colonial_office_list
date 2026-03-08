"""
Gambia Colonial Office List 1917 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1917

OFFICIALS = [
    {"name": "F. A. Van der Meulen", "canonical_name": "Van der Meulen, F. A.", "given_names": "F. A.", "surname": "Van der Meulen", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 750, "salary_max": 750},
    {"name": "E. St. J. Jackson", "canonical_name": "Jackson, E. St. J.", "given_names": "E. St. J.", "surname": "Jackson", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "M. F. J. McDonnell", "canonical_name": "McDonnell, M. F. J.", "given_names": "M. F. J.", "surname": "McDonnell", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "J. J. Oldfield", "canonical_name": "Oldfield, J. J.", "given_names": "J. J.", "surname": "Oldfield", "position": "Assistant Clerk of Courts, 3rd Grade", "department": "Legal Department - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "J. Finden Dailey", "canonical_name": "Dailey, J. Finden", "given_names": "J. Finden", "surname": "Dailey", "position": "Clerk to Legal Adviser, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "N. C. Johnson", "canonical_name": "Johnson, N. C.", "given_names": "N. C.", "surname": "Johnson", "position": "Ditto, 3rd Grade", "department": "Legal Department - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "Geo. D. Williams", "canonical_name": "Williams, Geo. D.", "given_names": "Geo. D.", "surname": "Williams", "position": "Interpreter of Courts", "department": "Legal Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Beadle and Bailiff", "department": "Legal Department - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "Mahomed E. Grant", "canonical_name": "Grant, Mahomed E.", "given_names": "Mahomed E.", "surname": "Grant", "position": "Clerk to Police Magistrate, 5th Grade", "department": "Legal Department - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "C. Greig", "canonical_name": "Greig, C.", "given_names": "C.", "surname": "Greig", "position": "Sheriff", "department": "Legal Department - Gambia"},
    {"name": "M. E. Grant", "canonical_name": "Grant, M. E.", "given_names": "M. E.", "surname": "Grant", "position": "Clerk to Board of Education", "department": "Education - Gambia", "salary_min": 10, "salary_max": 10},
    {"name": "H. L. Pryce", "canonical_name": "Pryce, H. L.", "given_names": "H. L.", "surname": "Pryce", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "honors": ["C.M.G."], "per_diem": "10s."},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "honors": ["D.S.O."], "per_diem": "10s."},
    {"name": "J. K. McCallum", "canonical_name": "McCallum, J. K.", "given_names": "J. K.", "surname": "McCallum", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "per_diem": "10s."},
    {"name": "H. F. Sproston", "canonical_name": "Sproston, H. F.", "given_names": "H. F.", "surname": "Sproston", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "per_diem": "10s."},
    {"name": "E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "military_rank": "Capt.", "per_diem": "10s."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "F. Napier Broome", "canonical_name": "Broome, F. Napier", "given_names": "F. Napier", "surname": "Broome", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "honors": ["C.M.G."]},
    {"name": "J. C. Harper", "canonical_name": "Harper, J. C.", "given_names": "J. C.", "surname": "Harper", "position": "Clerk", "department": "Civil Establishment - Gambia", "salary_min": 160, "salary_max": 160},
    {"name": "M. Fraser", "canonical_name": "Fraser, M.", "given_names": "M.", "surname": "Fraser", "position": "Colonial Secretary", "department": "Colonial Secretary's Department - Gambia", "salary_min": 800, "salary_max": 800},
    {"name": "G. B. Phillips", "canonical_name": "Phillips, G. B.", "given_names": "G. B.", "surname": "Phillips", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Department - Gambia", "salary_min": 450, "salary_max": 450},
    {"name": "M. A. C. Fraser", "canonical_name": "Fraser, M. A. C.", "given_names": "M. A. C.", "surname": "Fraser", "position": "Clerk and Registrar", "department": "Colonial Secretary's Department - Gambia", "salary_min": 200, "salary_max": 200},
    {"name": "Edwin Ley", "canonical_name": "Ley, Edwin", "given_names": "Edwin", "surname": "Ley", "position": "Clerk", "department": "Colonial Secretary's Department - Gambia", "salary_min": 160, "salary_max": 160},
    {"name": "E. Steere", "canonical_name": "Steere, E.", "given_names": "E.", "surname": "Steere", "position": "Clerk", "department": "Colonial Secretary's Department - Gambia", "salary_min": 90, "salary_max": 90},
    {"name": "H. P. Hillas", "canonical_name": "Hillas, H. P.", "given_names": "H. P.", "surname": "Hillas", "position": "Office Keeper", "department": "Colonial Secretary's Department - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "Richard Ward", "canonical_name": "Ward, Richard", "given_names": "Richard", "surname": "Ward", "position": "Messenger", "department": "Colonial Secretary's Department - Gambia", "salary_min": 42, "salary_max": 42},
    {"name": "E. Lawrence", "canonical_name": "Lawrence, E.", "given_names": "E.", "surname": "Lawrence", "position": "Government Resident", "department": "Government Residents - Gambia", "location": "Northern District"},
    {"name": "George Eliot", "canonical_name": "Eliot, George", "given_names": "George", "surname": "Eliot", "position": "Government Resident", "department": "Government Residents - Gambia", "location": "Victoria"},
    {"name": "R. C. Loftie", "canonical_name": "Loftie, R. C.", "given_names": "R. C.", "surname": "Loftie", "position": "Government Resident", "department": "Government Residents - Gambia", "location": "Plantagenet"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
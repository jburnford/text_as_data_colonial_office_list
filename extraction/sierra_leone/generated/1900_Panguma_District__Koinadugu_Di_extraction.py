"""
Sierra Leone Colonial Office List 1900 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1900

OFFICIALS = [
    {"name": "Thos. Hood", "canonical_name": "Hood, Thos.", "given_names": "Thos.", "surname": "Hood", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500, "region": "Panguma District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Panguma District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Civil Establishment - Sierra Leone", "salary_min": 30, "salary_max": 40, "region": "Panguma District"},
    {"name": "O. Horrocks", "canonical_name": "Horrocks, O.", "given_names": "O.", "surname": "Horrocks", "position": "D. Surgeon", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Panguma District"},
    {"name": "Onesimas Thompson", "canonical_name": "Thompson, Onesimas", "given_names": "Onesimas", "surname": "Thompson", "position": "Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Panguma District"},
    {"name": "C. E. Birch", "canonical_name": "Birch, C. E.", "given_names": "C. E.", "surname": "Birch", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500, "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Civil Establishment - Sierra Leone", "salary_min": 30, "salary_max": 40, "region": "Koinadugu District"},
    {"name": "J. F. W. Ward", "canonical_name": "Ward, J. F. W.", "given_names": "J. F. W.", "surname": "Ward", "position": "D. Surgeon", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Koinadugu District"},
    {"name": "A. H. de L. Ferguson", "canonical_name": "Ferguson, A. H. de L.", "given_names": "A. H. de L.", "surname": "Ferguson", "position": "Assistant District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 550, "military_rank": "Capt.", "honors": ["D.S.O."], "region": "Protectorate"},
    {"name": "J. H. D. Robertson", "canonical_name": "Robertson, J. H. D.", "given_names": "J. H. D.", "surname": "Robertson", "position": "Assistant District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 550, "military_rank": "Lieut.", "region": "Protectorate"},
    {"name": "G. H. Sangster", "canonical_name": "Sangster, G. H.", "given_names": "G. H.", "surname": "Sangster", "position": "Assistant District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 550, "military_rank": "Lieut.", "region": "Protectorate"},
    {"name": "M. J. M. Robin", "canonical_name": "Robin, M. J. M.", "given_names": "M. J. M.", "surname": "Robin", "position": "Assistant District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 550, "region": "Protectorate"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 550, "region": "Protectorate"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
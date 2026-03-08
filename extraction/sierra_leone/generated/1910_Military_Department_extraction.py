"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "J. E. Gough", "canonical_name": "Gough, J. E.", "given_names": "J. E.", "surname": "Gough", "position": "Inspector-General of Protectorate Forces", "department": "Military Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "honors": ["V.C."], "military_rank": "Colonel"},
    {"name": "H. Dawney", "canonical_name": "Dawney, H.", "given_names": "H.", "surname": "Dawney", "position": "Staff Officer", "department": "Military Department - Sierra Leone", "salary_min": 650, "salary_max": 650, "honors": ["D.S.O."], "military_rank": "Captain", "given_names": "The Hon. H."},
    {"name": "J. A. Hannington", "canonical_name": "Hannington, J. A.", "given_names": "J. A.", "surname": "Hannington", "position": "Commandant 6th Battalion King's African Rifles", "department": "Military Department - Sierra Leone", "salary_min": 900, "salary_max": 900, "military_rank": "Major"},
    {"name": "T. Millard", "canonical_name": "Millard, T.", "given_names": "T.", "surname": "Millard", "position": "Military Paymaster", "department": "Military Department - Sierra Leone", "salary_min": 200, "salary_max": 300}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
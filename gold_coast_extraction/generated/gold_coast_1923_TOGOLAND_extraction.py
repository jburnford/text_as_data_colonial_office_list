"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Captain E. B. Barker", "canonical_name": "Barker, E. B.", "given_names": "E. B.", "surname": "Barker",
     "position": "Political Officer", "department": "Administration - Togoland", "military_rank": "Captain", "region": "Togoland"},
    {"name": "Temporary Lieutenant-Colonel F. C. Bryant", "canonical_name": "Bryant, F. C.", "given_names": "F. C.", "surname": "Bryant",
     "position": "Senior Military Commander", "department": "Administration - Togoland", "military_rank": "Lieutenant-Colonel", "region": "Togoland"},
    {"name": "Sir Hugh Clifford", "canonical_name": "Clifford, Sir Hugh", "given_names": "Hugh", "surname": "Clifford",
     "position": "Governor", "department": "Administration - Togoland", "region": "Togoland"},
    {"name": "M. Noufflard", "canonical_name": "Noufflard, M.", "given_names": "M.", "surname": "Noufflard",
     "position": "Governor of Dahomey", "department": "Administration - Togoland", "region": "Togoland"},
    {"name": "Lord Milner", "canonical_name": "Milner, Lord", "given_names": None, "surname": "Milner",
     "position": "Signatory", "department": "Administration - Togoland", "region": "Togoland"},
    {"name": "M. Simon", "canonical_name": "Simon, M.", "given_names": "M.", "surname": "Simon",
     "position": "Signatory", "department": "Administration - Togoland", "region": "Togoland"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
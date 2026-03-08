"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Diego d'Azambuja", "canonical_name": "d'Azambuja, Diego", "given_names": "Diego", "surname": "d'Azambuja",
     "position": "Commander", "department": "Civil Establishment - Gold Coast", "location": "Elmina", "region": "Colony"},
    {"name": "Captain Holmes", "canonical_name": "Holmes, Captain", "surname": "Holmes", "position": "Commander",
     "department": "Civil Establishment - Gold Coast", "military_rank": "Captain", "location": "Cape Coast", "region": "Colony"},
    {"name": "de Ruyter", "canonical_name": "de Ruyter", "surname": "de Ruyter", "position": "Commander",
     "department": "Civil Establishment - Gold Coast", "region": "Colony"},
    {"name": "Sir Charles Macarthy", "canonical_name": "Macarthy, Sir Charles", "given_names": "Charles", "surname": "Macarthy",
     "position": "Governor", "department": "Civil Establishment - Gold Coast", "location": "Cape Coast Castle", "region": "Colony"},
    {"name": "George Maclean", "canonical_name": "Maclean, George", "given_names": "George", "surname": "Maclean",
     "position": "Governor", "department": "Civil Establishment - Gold Coast", "location": "Cape Coast Castle", "region": "Colony"},
    {"name": "George Maclean", "canonical_name": "Maclean, George", "given_names": "George", "surname": "Maclean",
     "position": "Judicial Assessor to the Native Chiefs", "department": "Judicial Department - Gold Coast", "region": "Colony"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
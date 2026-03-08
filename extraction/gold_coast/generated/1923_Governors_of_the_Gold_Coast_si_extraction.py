"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Sir M. Nathan", "canonical_name": "Nathan, Sir M.", "surname": "Nathan", "honors": ["K.C.M.G."], "position": "Governor", "department": "Governors of the Gold Coast (since 1900)."},
    {"name": "Sir J. P. Rodger", "canonical_name": "Rodger, Sir J. P.", "surname": "Rodger", "honors": ["K.C.M.G."], "position": "Governor", "department": "Governors of the Gold Coast (since 1900)."},
    {"name": "J. J. Thorburn", "canonical_name": "Thorburn, J. J.", "surname": "Thorburn", "honors": ["C.M.G."], "position": "Governor", "department": "Governors of the Gold Coast (since 1900)."},
    {"name": "Sir H. C. Clifford", "canonical_name": "Clifford, Sir H. C.", "surname": "Clifford", "honors": ["K.C.M.G."], "position": "Governor", "department": "Governors of the Gold Coast (since 1900)."},
    {"name": "Brigadier-General Sir F. Gordon Guggisberg", "canonical_name": "Guggisberg, Sir F. Gordon", "given_names": "F. Gordon", "surname": "Guggisberg", "honors": ["K.C.M.G.", "D.S.O."], "military_rank": "Brigadier-General", "position": "Governor", "department": "Governors of the Gold Coast (since 1900)."},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
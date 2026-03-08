"""
Gambia Colonial Office List 1879 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1879

OFFICIALS = [
    {"name": "H. P. Seagram", "canonical_name": "Seagram, H. P.", "surname": "Seagram", "position": "Governor", "department": "Civil Establishment - Gambia"},
    {"name": "E. Norcott", "canonical_name": "Norcott, E.", "surname": "Norcott", "position": "Governor", "department": "Civil Establishment - Gambia"},
    {"name": "C. FitzGerald", "canonical_name": "FitzGerald, C.", "surname": "FitzGerald", "position": "Governor", "department": "Civil Establishment - Gambia"},
    {"name": "R. G. McDonnell", "canonical_name": "McDonnell, R. G.", "surname": "McDonnell", "position": "Governor", "department": "Civil Establishment - Gambia"},
    {"name": "A. E. Kennedy", "canonical_name": "Kennedy, A. E.", "surname": "Kennedy", "position": "Governor", "department": "Civil Establishment - Gambia"},
    {"name": "L. S. O'Connor", "canonical_name": "O'Connor, L. S.", "surname": "O'Connor", "position": "Governor", "department": "Civil Establishment - Gambia", "military_rank": "Colonel"},
    {"name": "G. A. K. d'Arcy", "canonical_name": "d'Arcy, G. A. K.", "surname": "d'Arcy", "position": "Governor", "department": "Civil Establishment - Gambia", "military_rank": "Colonel"},
    {"name": "C. G. E. Patey", "canonical_name": "Patey, C. G. E.", "surname": "Patey", "position": "Governor", "department": "Civil Establishment - Gambia", "honors": ["C.M.G."], "military_rank": "Admiral"},
    {"name": "T. F. Callaghan", "canonical_name": "Callaghan, T. F.", "surname": "Callaghan", "position": "Governor", "department": "Civil Establishment - Gambia", "honors": ["C.M.G."]},
    {"name": "C. H. Kertright", "canonical_name": "Kertright, C. H.", "surname": "Kertright", "position": "Governor", "department": "Civil Establishment - Gambia", "honors": ["C.M.G."]},
    {"name": "Samuel Rowe", "canonical_name": "Rowe, Samuel", "surname": "Rowe", "position": "Governor", "department": "Civil Establishment - Gambia", "honors": ["C.M.G."]},
    {"name": "V. S. Gouldsbury", "canonical_name": "Gouldsbury, V. S.", "surname": "Gouldsbury", "position": "Governor", "department": "Civil Establishment - Gambia", "honors": ["C.M.G."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
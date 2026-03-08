"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "E. Bradbury", "canonical_name": "Bradbury, E.", "given_names": "E.", "surname": "Bradbury", "position": "Senior Medical Officer (Health)", "department": "Health - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "T. P. Eddy", "canonical_name": "Eddy, T. P.", "given_names": "T. P.", "surname": "Eddy", "position": "Senior Medical Officer (Health)", "department": "Health - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "R. Elliott", "canonical_name": "Elliott, R.", "given_names": "R.", "surname": "Elliott", "position": "Malaria Entomologist", "department": "Health - Sierra Leone", "salary_scale": "A"},
    {"name": "P. C. Bartrum", "canonical_name": "Bartrum, P. C.", "given_names": "P. C.", "surname": "Bartrum", "position": "Meteorologist", "department": "Meteorological - Sierra Leone", "salary_scale": "A"},
    {"name": "C. L. Gulliver", "canonical_name": "Gulliver, C. L.", "given_names": "C. L.", "surname": "Gulliver", "position": "Senior Assistant Meteorologist", "department": "Meteorological - Sierra Leone", "salary_scale": "C.3"},
    {"name": "F. R. H. Green", "canonical_name": "Green, F. R. H.", "given_names": "F. R. H.", "surname": "Green", "position": "Chief Inspector of Mines", "department": "Mines - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "A. Akiwumi", "canonical_name": "Akiwumi, A.", "given_names": "A.", "surname": "Akiwumi", "position": "Inspector of Mines", "department": "Mines - Sierra Leone", "salary_scale": "A", "honors": ["M.B.E."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
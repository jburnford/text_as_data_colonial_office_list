"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "C. L. Gulliver", "canonical_name": "Gulliver, C. L.", "given_names": "C. L.", "surname": "Gulliver", "position": "Senior Assistant Meteorologist", "department": "Meteorological - Sierra Leone", "salary_scale": "C3"},
    {"name": "F. R. H. Green", "canonical_name": "Green, F. R. H.", "given_names": "F. R. H.", "surname": "Green", "position": "Chief Inspector of Mines", "department": "MINES - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "A. Akiwumi", "canonical_name": "Akiwumi, A.", "given_names": "A.", "surname": "Akiwumi", "position": "Inspector of Mines", "department": "MINES - Sierra Leone", "salary_scale": "A"},
    {"name": "J. P. I. Fforde", "canonical_name": "Fforde, J. P. I.", "given_names": "J. P. I.", "surname": "Fforde", "position": "Commissioner of Police", "department": "POLICE - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "W. E. Rumbelow", "canonical_name": "Rumbelow, W. E.", "given_names": "W. E.", "surname": "Rumbelow", "position": "Assistant Commissioner of Police", "department": "POLICE - Sierra Leone", "salary_min": 900, "salary_max": 900},
    {"name": "C. E. Wingrove", "canonical_name": "Wingrove, C. E.", "given_names": "C. E.", "surname": "Wingrove", "position": "Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B", "military_rank": "Captain"},
    {"name": "P. E. Turnbull", "canonical_name": "Turnbull, P. E.", "given_names": "P. E.", "surname": "Turnbull", "position": "Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "F. G. B. Gall", "canonical_name": "Gall, F. G. B.", "given_names": "F. G. B.", "surname": "Gall", "position": "Senior Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "A. S. Keeling", "canonical_name": "Keeling, A. S.", "given_names": "A. S.", "surname": "Keeling", "position": "Senior Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "F. R. Brothers", "canonical_name": "Brothers, F. R.", "given_names": "F. R.", "surname": "Brothers", "position": "Senior Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B", "honors": ["B.E.M."]},
    {"name": "O. R. Lucas", "canonical_name": "Lucas, O. R.", "given_names": "O. R.", "surname": "Lucas", "position": "Senior Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "E. J. E. Ashwood", "canonical_name": "Ashwood, E. J. E.", "given_names": "E. J. E.", "surname": "Ashwood", "position": "Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "E. Grange", "canonical_name": "Grange, E.", "given_names": "E.", "surname": "Grange", "position": "Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "R. Cole", "canonical_name": "Cole, R.", "given_names": "R.", "surname": "Cole", "position": "Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "B. H. Nealon", "canonical_name": "Nealon, B. H.", "given_names": "B. H.", "surname": "Nealon", "position": "Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "W. T. Doherty", "canonical_name": "Doherty, W. T.", "given_names": "W. T.", "surname": "Doherty", "position": "Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "J. E. Brandon", "canonical_name": "Brandon, J. E.", "given_names": "J. E.", "surname": "Brandon", "position": "Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "R. G. Moss", "canonical_name": "Moss, R. G.", "given_names": "R. G.", "surname": "Moss", "position": "Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B", "honors": ["D.F.C."]},
    {"name": "L. W. Leigh", "canonical_name": "Leigh, L. W.", "given_names": "L. W.", "surname": "Leigh", "position": "Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"},
    {"name": "J. Doull", "canonical_name": "Doull, J.", "given_names": "J.", "surname": "Doull", "position": "Assistant Superintendent of Police", "department": "POLICE - Sierra Leone", "salary_scale": "B"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
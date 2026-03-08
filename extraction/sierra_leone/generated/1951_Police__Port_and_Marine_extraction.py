"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "J. P. I. Fforde", "canonical_name": "Fforde, J. P. I.", "given_names": "J. P. I.", "surname": "Fforde", "position": "Commissioner of Police", "department": "Police - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "W. E. Rumbelow", "canonical_name": "Rumbelow, W. E.", "given_names": "W. E.", "surname": "Rumbelow", "position": "Assistant Commissioner of Police", "department": "Police - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "F. G. B. Gall", "canonical_name": "Gall, F. G. B.", "given_names": "F. G. B.", "surname": "Gall", "position": "Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "R. H. Beaumont", "canonical_name": "Beaumont, R. H.", "given_names": "R. H.", "surname": "Beaumont", "position": "Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "A. S. Keeling", "canonical_name": "Keeling, A. S.", "given_names": "A. S.", "surname": "Keeling", "position": "Senior Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "O. R. Lucas", "canonical_name": "Lucas, O. R.", "given_names": "O. R.", "surname": "Lucas", "position": "Senior Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "D. V. Noott", "canonical_name": "Noott, D. V.", "given_names": "D. V.", "surname": "Noott", "position": "Senior Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "R. Cole", "canonical_name": "Cole, R.", "given_names": "R.", "surname": "Cole", "position": "Senior Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "B. H. Nealon", "canonical_name": "Nealon, B. H.", "given_names": "B. H.", "surname": "Nealon", "position": "Senior Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "J. W. Lay", "canonical_name": "Lay, J. W.", "given_names": "J. W.", "surname": "Lay", "position": "Senior Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "E. J. E. Ashwood", "canonical_name": "Ashwood, E. J. E.", "given_names": "E. J. E.", "surname": "Ashwood", "position": "Senior Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "W. T. Doherty", "canonical_name": "Doherty, W. T.", "given_names": "W. T.", "surname": "Doherty", "position": "Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "J. E. Brandon", "canonical_name": "Brandon, J. E.", "given_names": "J. E.", "surname": "Brandon", "position": "Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "R. G. Moss", "canonical_name": "Moss, R. G.", "given_names": "R. G.", "surname": "Moss", "position": "Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B", "honors": ["D.F.C."]},
    {"name": "L. W. Leigh", "canonical_name": "Leigh, L. W.", "given_names": "L. W.", "surname": "Leigh", "position": "Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "J. Doull", "canonical_name": "Doull, J.", "given_names": "J.", "surname": "Doull", "position": "Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "J. D. Doherty", "canonical_name": "Doherty, J. D.", "given_names": "J. D.", "surname": "Doherty", "position": "Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "H. S. Trattles", "canonical_name": "Trattles, H. S.", "given_names": "H. S.", "surname": "Trattles", "position": "Assistant Superintendent of Police", "department": "Police - Sierra Leone", "salary_scale": "B"},
    {"name": "R. E. F. Parsons", "canonical_name": "Parsons, R. E. F.", "given_names": "R. E. F.", "surname": "Parsons", "position": "Harbour Master", "department": "Port and Marine - Sierra Leone", "salary_min": 1000, "salary_max": 1000}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
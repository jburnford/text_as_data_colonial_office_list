"""
Sierra Leone Colonial Office List 1889 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1889

OFFICIALS = [
    {"name": "F. C. Hallett", "canonical_name": "Hallett, F. C.", "given_names": "F. C.", "surname": "Hallett", "position": "Inspector-General of Police", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 400, "allowances": "91l. 1s. travelling allowance", "military_rank": "Captain"},
    {"name": "A. Revington", "canonical_name": "Revington, A.", "given_names": "A.", "surname": "Revington", "position": "Inspector", "department": "Police - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "M. Betts", "canonical_name": "Betts, M.", "given_names": "M.", "surname": "Betts", "position": "Sub-Inspector", "department": "Police - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "Robert Wade", "canonical_name": "Wade, Robert", "given_names": "Robert", "surname": "Wade", "position": "Keeper of Freetown Gaol", "department": "Gaol Establishment - Sierra Leone", "salary_min": 250, "salary_max": 250, "location": "Freetown"},
    {"name": "S. J. Thomas", "canonical_name": "Thomas, S. J.", "given_names": "S. J.", "surname": "Thomas", "position": "Under Gaoler", "department": "Gaol Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100, "location": "Freetown"},
    {"name": "Elizabeth Taylor", "canonical_name": "Taylor, Elizabeth", "given_names": "Elizabeth", "surname": "Taylor", "position": "Matron", "department": "Gaol Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50, "location": "Freetown"},
    {"name": "Mary E. Wilson", "canonical_name": "Wilson, Mary E.", "given_names": "Mary E.", "surname": "Wilson", "position": "Under ditto", "department": "Gaol Establishment - Sierra Leone", "salary_min": 30, "salary_max": 30, "location": "Freetown"},
    {"name": "G. H. Garrett", "canonical_name": "Garrett, G. H.", "given_names": "G. H.", "surname": "Garrett", "position": "Travelling Commissioner", "department": "Travelling Commissioners - Sierra Leone", "salary_min": 547, "salary_max": 547},
    {"name": "E. Adolphus", "canonical_name": "Adolphus, E.", "given_names": "E.", "surname": "Adolphus", "position": "Manager", "department": "Rural Districts - Sierra Leone", "allowances": "45l. 12s. 6d. travelling allowance", "region": "1st Eastern"},
    {"name": "The Coroner for Freetown", "canonical_name": "Coroner for Freetown, The", "surname": "Coroner", "position": "Coroner", "department": "Rural Districts - Sierra Leone", "salary_min": 20, "salary_max": 20, "region": "1st Eastern"},
    {"name": "G. J. Macauley", "canonical_name": "Macauley, G. J.", "given_names": "G. J.", "surname": "Macauley", "position": "Registrar", "department": "Rural Districts - Sierra Leone", "region": "1st Eastern", "qualifications": ["Rev."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
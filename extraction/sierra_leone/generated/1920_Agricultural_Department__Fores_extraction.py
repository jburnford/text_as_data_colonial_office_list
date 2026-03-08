"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "D. W. Scotland", "canonical_name": "Scotland, D. W.", "given_names": "D. W.", "surname": "Scotland", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "H. Waterland", "canonical_name": "Waterland, H.", "given_names": "H.", "surname": "Waterland", "position": "Assistants in Agricultural Department", "department": "Agricultural Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. M. Watt", "canonical_name": "Watt, J. M.", "given_names": "J. M.", "surname": "Watt", "position": "Assistants in Agricultural Department", "department": "Agricultural Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "S. L. Mosely", "canonical_name": "Mosely, S. L.", "given_names": "S. L.", "surname": "Mosely", "position": "Superintendent, Experimental Farm", "department": "Agricultural Department - Sierra Leone", "salary_min": 120, "salary_max": 140},
    {"name": "L. H. Palfreman", "canonical_name": "Palfreman, L. H.", "given_names": "L. H.", "surname": "Palfreman", "position": "Conservator of Forests", "department": "Forest Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "K. G. Burbridge", "canonical_name": "Burbridge, K. G.", "given_names": "K. G.", "surname": "Burbridge", "position": "Assistant Conservator of Forests", "department": "Forest Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "G. Aylmer", "canonical_name": "Aylmer, G.", "given_names": "G.", "surname": "Aylmer", "position": "Assistant Conservator of Forests", "department": "Forest Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "E. Macdonald", "canonical_name": "Macdonald, E.", "given_names": "E.", "surname": "Macdonald", "position": "Assistant Conservator of Forests", "department": "Forest Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": "R. B.", "surname": "Mackie", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A"},
    {"name": "W. T. Martin", "canonical_name": "Martin, W. T.", "given_names": "W. T.", "surname": "Martin", "position": "Collectors of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_scale": "A"},
    {"name": "F. A. von Weiller", "canonical_name": "von Weiller, F. A.", "given_names": "F. A.", "surname": "von Weiller", "position": "Collectors of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_scale": "A"},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Sherbro", "salary_min": 360, "salary_max": 500},
    {"name": "A. R. Harris", "canonical_name": "Harris, A. R.", "given_names": "A. R.", "surname": "Harris", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_min": 360, "salary_max": 500},
    {"name": "M. A. Smith", "canonical_name": "Smith, M. A.", "given_names": "M. A.", "surname": "Smith", "position": "Senior Outdoor Officer", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. M. Peeler", "canonical_name": "Peeler, W. M.", "given_names": "W. M.", "surname": "Peeler", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "C. D. Williams", "canonical_name": "Williams, C. D.", "given_names": "C. D.", "surname": "Williams", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "E. A. Turner", "canonical_name": "Turner, E. A.", "given_names": "E. A.", "surname": "Turner", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "F. C. Campbell", "canonical_name": "Campbell, F. C.", "given_names": "F. C.", "surname": "Campbell", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "G. J. Gooding", "canonical_name": "Gooding, G. J.", "given_names": "G. J.", "surname": "Gooding", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
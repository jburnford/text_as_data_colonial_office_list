"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "J. A. A. Duncan", "canonical_name": "Duncan, J. A. A.", "given_names": "J. A. A.", "surname": "Duncan", "position": "Assistant Director, Health Service", "department": "Health Department - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "duty_allowance": 260},
    {"name": "A. B. Monks", "canonical_name": "Monks, A. B.", "given_names": "A. B.", "surname": "Monks", "position": "Senior Health Officer", "department": "Health Department - Sierra Leone", "salary_min": 1050, "salary_max": 1200, "duty_allowance": 210},
    {"name": "R. F. Campbell", "canonical_name": "Campbell, R. F.", "given_names": "R. F.", "surname": "Campbell", "position": "Medical Officer of Health", "department": "Health Department - Sierra Leone", "salary_min": 800, "salary_max": 960},
    {"name": "G. V. Herd", "canonical_name": "Herd, G. V.", "given_names": "G. V.", "surname": "Herd", "position": "Sanitary Superintendent and Training Officer", "department": "Health Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "A. E. Wilkinson", "canonical_name": "Wilkinson, A. E.", "given_names": "A. E.", "surname": "Wilkinson", "position": "Superintendent, Sanitary Inspectors", "department": "Health Department - Sierra Leone", "salary_scale": "F"},
    {"name": "P. Osment", "canonical_name": "Osment, P.", "given_names": "P.", "surname": "Osment", "position": "Superintendent, Sanitary Inspectors", "department": "Health Department - Sierra Leone", "salary_scale": "F"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
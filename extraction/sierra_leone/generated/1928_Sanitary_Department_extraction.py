"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "W. H. Peacock", "canonical_name": "Peacock, W. H.", "given_names": "W. H.", "surname": "Peacock", "position": "Deputy Director, Sanitary Service", "department": "Sanitary Department - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "duty_allowance": 260},
    {"name": "J. M. MacKay", "canonical_name": "MacKay, J. M.", "given_names": "J. M.", "surname": "MacKay", "position": "Senior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 1050, "salary_max": 1200, "duty_allowance": 210, "honors": ["M.C."]},
    {"name": "F. V. Hill", "canonical_name": "Hill, F. V.", "given_names": "F. V.", "surname": "Hill", "position": "Medical Officer of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 800, "salary_max": 960},
    {"name": "G. V. Herd", "canonical_name": "Herd, G. V.", "given_names": "G. V.", "surname": "Herd", "position": "Sanitary Superintendent and Training Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "A. E. Wilkinson", "canonical_name": "Wilkinson, A. E.", "given_names": "A. E.", "surname": "Wilkinson", "position": "Superintendent, Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_scale": "F"},
    {"name": "P. Osment", "canonical_name": "Osment, P.", "given_names": "P.", "surname": "Osment", "position": "Superintendent, Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_scale": "F"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
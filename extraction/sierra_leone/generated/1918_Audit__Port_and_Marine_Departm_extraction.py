"""
Sierra Leone Colonial Office List 1918 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1918

OFFICIALS = [
    {"name": "B. E. Hanson", "canonical_name": "Hanson, B. E.", "given_names": "B. E.", "surname": "Hanson", "position": "Auditor", "department": "Audit - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "S. P. Warbrook", "canonical_name": "Warbrook, S. P.", "given_names": "S. P.", "surname": "Warbrook", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 300, "salary_max": 400, "duty_allowance": 60},
    {"name": "N. H. Turton", "canonical_name": "Turton, N. H.", "given_names": "N. H.", "surname": "Turton", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. E. C. Merrick", "canonical_name": "Merrick, H. E. C.", "given_names": "H. E. C.", "surname": "Merrick", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": "M. B.", "surname": "Reader", "position": "Second Grade Clerk", "department": "Audit - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "Third Grade Clerk", "department": "Audit - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "E. F. W. Smart", "canonical_name": "Smart, E. F. W.", "given_names": "E. F. W.", "surname": "Smart", "position": "Third Grade Clerk", "department": "Audit - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "W. H. Calthrop Calthrop", "canonical_name": "Calthrop, W. H. Calthrop", "given_names": "W. H.", "surname": "Calthrop", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "qualifications": ["R.N."]},
    {"name": "U. J. Lawrence", "canonical_name": "Lawrence, U. J.", "given_names": "U. J.", "surname": "Lawrence", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "W. Bowerley", "position": "Auditor", "department": "Audit Department - Gold Coast", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "L. G. Corney", "position": "Deputy Auditor", "department": "Audit Department - Gold Coast", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "W. L. Mackinnon", "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "Capt. C. Griffith", "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "Capt. W. H. Lemriere", "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "N. C. Fonnerau", "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "A. C. Hands", "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "E. H. C. Lillicrup", "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "V. C. Randolph", "position": "Chief Audit Clerk", "department": "Audit Department - Gold Coast", "salary_min": 300, "salary_max": 396},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
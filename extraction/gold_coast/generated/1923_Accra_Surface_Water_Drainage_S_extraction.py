"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "C. W. Brown", "canonical_name": "Brown, C. W.", "given_names": "C. W.", "surname": "Brown",
     "position": "Assistant Drainage Engineer, Grade II.", "department": "Public Works Department - Gold Coast",
     "qualifications": ["M.C.", "A.M.I.O.E.", "A.R.T.C.", "F.R.G.S."], "salary_min": 480, "salary_max": 920,
     "salary_scale": "480l. by 30l. to 720l. by 40l. to 920l.", "allowances": "72l. seniority allowance from 720l."},
    {"name": "E. Tomes", "canonical_name": "Tomes, E.", "given_names": "E.", "surname": "Tomes",
     "position": "European Foreman", "department": "Public Works Department - Gold Coast", "salary_min": 440,
     "salary_max": 500, "salary_scale": "440l. to 500l. by 12l."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
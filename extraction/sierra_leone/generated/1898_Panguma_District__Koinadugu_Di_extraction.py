"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "D. Commissioner, an Asst. Inspector (Acting)", "department": "Districts - Sierra Leone", "salary_min": 400, "salary_max": 500, "region": "Panguma District"},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Clerk", "department": "Districts - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Panguma District"},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Districts - Sierra Leone", "salary_min": 30, "salary_max": 40, "region": "Panguma District"},
    {"name": "O. Horrocks", "canonical_name": "Horrocks, O.", "given_names": "O.", "surname": "Horrocks", "position": "D. Surgeon", "department": "Districts - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Panguma District"},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Dispenser", "department": "Districts - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Panguma District"},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "D. Commissioner, an Asst. Inspector (Acting)", "department": "Districts - Sierra Leone", "salary_min": 400, "salary_max": 500, "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Clerk", "department": "Districts - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Districts - Sierra Leone", "salary_min": 30, "salary_max": 40, "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "D. Surgeon", "department": "Districts - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Dispenser", "department": "Districts - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Koinadugu District"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
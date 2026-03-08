"""
Gambia Colonial Office List 1950 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1950

OFFICIALS = [
    {"name": "N. P. Hadow", "canonical_name": "Hadow, N. P.", "surname": "Hadow", "position": "Superintendent of Police and Inspector of Prisons", "department": "Police and Prisons - Gambia", "salary_scale": "B"},
    {"name": "J. N. Ferguson", "canonical_name": "Ferguson, J. N.", "surname": "Ferguson", "position": "Assistant Superintendent of Police", "department": "Police and Prisons - Gambia", "salary_scale": "B"},
    {"name": "P. A. Williams", "canonical_name": "Williams, P. A.", "surname": "Williams", "position": "Assistant Superintendent of Police", "department": "Police and Prisons - Gambia", "salary_scale": "B"},
    {"name": "G. T. Bolton", "canonical_name": "Bolton, G. T.", "surname": "Bolton", "position": "Assistant Superintendent of Police", "department": "Police and Prisons - Gambia", "salary_scale": "B"},
    {"name": "E. C. Sowe", "canonical_name": "Sowe, E. C.", "surname": "Sowe", "position": "Postmaster General", "department": "Post Office - Gambia", "salary_scale": "B"},
    {"name": "O. B. Johnson", "canonical_name": "Johnson, O. B.", "surname": "Johnson", "position": "Assistant Postmaster General", "department": "Post Office - Gambia", "salary_scale": "F5"},
    {"name": "G. Peters", "canonical_name": "Peters, G.", "surname": "Peters", "position": "Information Officer", "department": "Public Relations - Gambia", "salary_scale": "B"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
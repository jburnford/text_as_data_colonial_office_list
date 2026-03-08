"""
Gambia Colonial Office List 1889 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1889

OFFICIALS = [
    {"name": "Thomas H. Spilsbury", "canonical_name": "Spilsbury, Thomas H.", "given_names": "Thomas H.", "surname": "Spilsbury", "position": "Colonial Surgeon", "department": "Medical Establishment - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "Percy J. Kendall", "canonical_name": "Kendall, Percy J.", "given_names": "Percy J.", "surname": "Kendall", "position": "Assistant Colonial Surgeon", "department": "Medical Establishment - Gambia", "salary_min": 300, "salary_max": 300, "qualifications": ["M.D."]},
    {"name": "George Spilsbury", "canonical_name": "Spilsbury, George", "given_names": "George", "surname": "Spilsbury", "position": "Dispenser", "department": "Medical Establishment - Gambia", "salary_min": 100, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
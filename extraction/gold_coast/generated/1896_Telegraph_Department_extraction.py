"""
Gold Coast Colonial Office List 1896 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1896

OFFICIALS = [
    {"name": "M. S. Andrews", "canonical_name": "Andrews, M. S.", "given_names": "M. S.", "surname": "Andrews",
     "position": "Director of Telegraphs", "department": "Telegraph Department - Gold Coast", "salary_min": 500, "salary_max": 500},
    {"name": "W. Murray", "canonical_name": "Murray, W.", "given_names": "W.", "surname": "Murray",
     "position": "Telegraph Foremen", "department": "Telegraph Department - Gold Coast", "salary_min": 250, "salary_max": 300},
    {"name": "G. W. Tucker", "canonical_name": "Tucker, G. W.", "given_names": "G. W.", "surname": "Tucker",
     "position": "Telegraph Foremen", "department": "Telegraph Department - Gold Coast", "salary_min": 250, "salary_max": 300},
    {"name": "S. W. Q. Papaio", "canonical_name": "Papaio, S. W. Q.", "given_names": "S. W. Q.", "surname": "Papaio",
     "position": "Assistant Telegraph Foreman", "department": "Telegraph Department - Gold Coast", "salary_min": 100, "salary_max": 200},
    {"name": "A. F. Hardwick", "canonical_name": "Hardwick, A. F.", "given_names": "A. F.", "surname": "Hardwick",
     "position": "Clerks in Charge", "department": "Telegraph Department - Gold Coast", "salary_min": 200, "salary_max": 250},
    {"name": "O. J. L. Jensen", "canonical_name": "Jensen, O. J. L.", "given_names": "O. J. L.", "surname": "Jensen",
     "position": "Mechanician", "department": "Telegraph Department - Gold Coast", "salary_min": 200, "salary_max": 250},
    {"name": "J. P. Plange", "canonical_name": "Plange, J. P.", "given_names": "J. P.", "surname": "Plange",
     "position": "Chief Lineman", "department": "Telegraph Department - Gold Coast", "salary_min": 75, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
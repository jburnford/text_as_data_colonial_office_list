"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "C. W. Hill", "canonical_name": "Hill, C. W.", "given_names": "C. W.", "surname": "Hill", "position": "Postmaster", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "A. Chipulina", "canonical_name": "Chipulina, A.", "given_names": "A.", "surname": "Chipulina", "position": "Chief Clerk and Cashier", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 210, "salary_max": 300},
    {"name": "J. Chipulina", "canonical_name": "Chipulina, J.", "given_names": "J.", "surname": "Chipulina", "position": "Senior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. J. Desoisa", "canonical_name": "Desoisa, J. J.", "given_names": "J. J.", "surname": "Desoisa", "position": "Senior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "T. Chipulina", "canonical_name": "Chipulina, T.", "given_names": "T.", "surname": "Chipulina", "position": "Senior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "A. de la Paz", "canonical_name": "Paz, A. de la", "given_names": "A.", "surname": "Paz", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "E. Jones", "canonical_name": "Jones, E.", "given_names": "E.", "surname": "Jones", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "E. Coll", "canonical_name": "Coll, E.", "given_names": "E.", "surname": "Coll", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "A. Pons", "canonical_name": "Pons, A.", "given_names": "A.", "surname": "Pons", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "A. Canepa", "canonical_name": "Canepa, A.", "given_names": "A.", "surname": "Canepa", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "A. Gilbert", "canonical_name": "Gilbert, A.", "given_names": "A.", "surname": "Gilbert", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "W. Turner", "canonical_name": "Turner, W.", "given_names": "W.", "surname": "Turner", "position": "Surgeon, Colonial Hospital, Gaol, and Lunatic Asylum", "department": "Medical Department - Gambia", "salary_min": 372, "qualifications": ["M.D.", "M.A."], "honors": ["M.V.O."]},
    {"name": "I. Lochhead", "canonical_name": "Lochhead, I.", "given_names": "I.", "surname": "Lochhead", "position": "Assistant Surgeon, Colonial Hospital, Police, Port and Post Office Surgeon", "department": "Medical Department - Gambia", "salary_min": 300, "qualifications": ["M.D."]},
    {"name": "A. J. Triay", "canonical_name": "Triay, A. J.", "given_names": "A. J.", "surname": "Triay", "position": "Surgeon, Smallpox Hospital", "department": "Medical Department - Gambia", "salary_min": 60, "qualifications": ["M.B."]},
    {"name": "H. Recaño", "canonical_name": "Recaño, H.", "given_names": "H.", "surname": "Recaño", "position": "Secretary, Colonial Hospital", "department": "Medical Department - Gambia", "salary_min": 218},
    {"name": "M. Montegriffo", "canonical_name": "Montegriffo, M.", "given_names": "M.", "surname": "Montegriffo", "position": "1st Class Clerk", "department": "Medical Department - Gambia", "salary_min": 210, "salary_max": 300},
    {"name": "S. Wall", "canonical_name": "Wall, S.", "given_names": "S.", "surname": "Wall", "position": "Gaoler", "department": "Civil Prison - Gambia", "salary_min": 150, "salary_max": 180}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
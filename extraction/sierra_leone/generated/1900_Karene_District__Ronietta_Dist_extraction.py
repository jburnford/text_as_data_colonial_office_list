"""
Sierra Leone Colonial Office List 1900 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1900

OFFICIALS = [
    {"name": "W. S. Sharpe", "canonical_name": "Sharpe, W. S.", "given_names": "W. S.", "surname": "Sharpe", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500, "honors": ["C.M.G."], "military_rank": "Capt.", "region": "Karene District"},
    {"name": "W. L. King", "canonical_name": "King, W. L.", "given_names": "W. L.", "surname": "King", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Karene District"},
    {"name": "J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "D. Surgeon", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Karene District"},
    {"name": "T. D. Betts", "canonical_name": "Betts, T. D.", "given_names": "T. D.", "surname": "Betts", "position": "Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Karene District"},
    {"name": "E. D. Fairtlough", "canonical_name": "Fairtlough, E. D.", "given_names": "E. D.", "surname": "Fairtlough", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500, "honors": ["D.S.O.", "C.M.G."], "military_rank": "Capt.", "region": "Ronietta District"},
    {"name": "A. C. Forde", "canonical_name": "Forde, A. C.", "given_names": "A. C.", "surname": "Forde", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Ronietta District"},
    {"name": "Thomas Hood", "canonical_name": "Hood, Thomas", "given_names": "Thomas", "surname": "Hood", "position": "D. Surgeon", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Ronietta District"},
    {"name": "M. N. Lardner", "canonical_name": "Lardner, M. N.", "given_names": "M. N.", "surname": "Lardner", "position": "Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Ronietta District"},
    {"name": "G. E. Carr", "canonical_name": "Carr, G. E.", "given_names": "G. E.", "surname": "Carr", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500, "region": "Bandajuma District"},
    {"name": "J. A. Branco", "canonical_name": "Branco, J. A.", "given_names": "J. A.", "surname": "Branco", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Bandajuma District"},
    {"name": "J. B. Davson", "canonical_name": "Davson, J. B.", "given_names": "J. B.", "surname": "Davson", "position": "D. Surgeon", "department": "Medical - Sierra Leone", "salary_min": 300, "salary_max": 350, "region": "Bandajuma District"},
    {"name": "J. H. Pearce", "canonical_name": "Pearce, J. H.", "given_names": "J. H.", "surname": "Pearce", "position": "Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Bandajuma District"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
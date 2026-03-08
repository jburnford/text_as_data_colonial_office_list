"""
Sierra Leone Colonial Office List 1889 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1889

OFFICIALS = [
    {"name": "J. S. Hay", "canonical_name": "Hay, J. S.", "given_names": "J. S.", "surname": "Hay", "position": "Governor, Commander-in-Chief, and Vice-Admiral", "department": "Civil Establishment - Sierra Leone", "salary_min": 2000, "salary_max": 2000, "allowances": "500l. allowances", "honors": ["C.M.G."], "military_rank": "Commander"},
    {"name": "W. G. Hay", "canonical_name": "Hay, W. G.", "given_names": "W. G.", "surname": "Hay", "position": "Private Secretary and Aide-de-Camp", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. W. Lewis", "canonical_name": "Lewis, J. W.", "given_names": "J. W.", "surname": "Lewis", "position": "Governor's Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 160, "salary_max": 160},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "Enoch Faulkner", "canonical_name": "Faulkner, Enoch", "given_names": "Enoch", "surname": "Faulkner", "position": "Clerks", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. E. Dawson", "canonical_name": "Dawson, J. E.", "given_names": "J. E.", "surname": "Dawson", "position": "Clerks", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "J. C. E. Parkes", "canonical_name": "Parkes, J. C. E.", "given_names": "J. C. E.", "surname": "Parkes", "position": "Clerks", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "J. J. Crooks", "canonical_name": "Crooks, J. J.", "given_names": "J. J.", "surname": "Crooks", "position": "Colonial Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 500, "salary_max": 500, "military_rank": "Major"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Colonial Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "M. A. Potts", "canonical_name": "Potts, M. A.", "given_names": "M. A.", "surname": "Potts", "position": "Clerks", "department": "Treasury - Sierra Leone", "salary_min": 240, "salary_max": 240},
    {"name": "B. M. Brown", "canonical_name": "Brown, B. M.", "given_names": "B. M.", "surname": "Brown", "position": "Clerks", "department": "Treasury - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. J. Wellington", "canonical_name": "Wellington, J. J.", "given_names": "J. J.", "surname": "Wellington", "position": "Clerks", "department": "Treasury - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "J. H. Spaine", "canonical_name": "Spaine, J. H.", "given_names": "J. H.", "surname": "Spaine", "position": "Clerk to Savings Bank", "department": "Treasury - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Government Interpreter", "department": "Aborigines Branch - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "Mohammed Sanusi", "canonical_name": "Sanusi, Mohammed", "given_names": "Mohammed", "surname": "Sanusi", "position": "Arabic Writer", "department": "Aborigines Branch - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "N. O. C. Roberts", "canonical_name": "Roberts, N. O. C.", "given_names": "N. O. C.", "surname": "Roberts", "position": "Clerk", "department": "Aborigines Branch - Sierra Leone", "salary_min": 36, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
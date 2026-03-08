"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "J. O. Gore", "canonical_name": "Gore, J. O.", "given_names": "J. O.", "surname": "Gore", "position": "Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 710, "salary_max": 800},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. E. Dawson", "canonical_name": "Dawson, J. E.", "given_names": "J. E.", "surname": "Dawson", "position": "Chief Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "C. B. Mitford", "canonical_name": "Mitford, C. B.", "given_names": "C. B.", "surname": "Mitford", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 550},
    {"name": "S. M. Bennett", "canonical_name": "Bennett, S. M.", "given_names": "S. M.", "surname": "Bennett", "position": "Assistant Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "Jacob W. Lewis", "canonical_name": "Lewis, Jacob W.", "given_names": "Jacob W.", "surname": "Lewis", "position": "Clerk of Executive Council", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
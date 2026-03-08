"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "W. C. F. Robertson", "canonical_name": "Robertson, W. C. F.", "given_names": "W. C. F.", "surname": "Robertson", "position": "Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 1000, "salary_max": 1000, "allowances": "free house"},
    {"name": "J. Porral", "canonical_name": "Porral, J.", "given_names": "J.", "surname": "Porral", "position": "Assistant Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 350, "salary_max": 350, "allowances": "50l. as Secretary to Board of Health, and quarters"},
    {"name": "E. P. Griffin", "canonical_name": "Griffin, E. P.", "given_names": "E. P.", "surname": "Griffin", "position": "Chief Clerk", "department": "Civil Establishment - Gambia", "salary_min": 210, "salary_max": 300, "allowances": "55l. for translating and interpreting"},
    {"name": "J. Bruzon", "canonical_name": "Bruzon, J.", "given_names": "J.", "surname": "Bruzon", "position": "1st Class Clerk", "department": "Civil Establishment - Gambia", "salary_min": 210, "salary_max": 300},
    {"name": "M. Figueras", "canonical_name": "Figueras, M.", "given_names": "M.", "surname": "Figueras", "position": "3rd Class Clerk", "department": "Civil Establishment - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "the Colonial Secretary", "canonical_name": "Colonial Secretary, The", "surname": "Colonial Secretary", "position": "Chief Commissioner", "department": "Crown Property Department - Gambia"},
    {"name": "R. Giraldi", "canonical_name": "Giraldi, R.", "given_names": "R.", "surname": "Giraldi", "position": "1st Class Clerk", "department": "Crown Property Department - Gambia", "salary_min": 210, "salary_max": 300}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
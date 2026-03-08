"""
Sierra Leone Colonial Office List 1894 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1894

OFFICIALS = [
    {"name": "Sir Francis Fleming", "canonical_name": "Fleming, Francis", "surname": "Fleming", "position": "Governor, Commander-in-Chief, and Vice-Admiral", "department": "Civil Establishment - Sierra Leone", "salary_min": 2000, "salary_max": 2000, "allowances": "500l. allowances", "honors": ["K.C.M.G."]},
    {"name": "Edward J. Vavasour", "canonical_name": "Vavasour, Edward J.", "given_names": "Edward J.", "surname": "Vavasour", "position": "Private Secretary", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "Jacob W. Lewis", "canonical_name": "Lewis, Jacob W.", "given_names": "Jacob W.", "surname": "Lewis", "position": "Governor's Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "10l. personal"},
    {"name": "J. J. Crooks", "canonical_name": "Crooks, J. J.", "given_names": "J. J.", "surname": "Crooks", "position": "Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 680, "salary_max": 800},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "J. E. Dawson", "canonical_name": "Dawson, J. E.", "given_names": "J. E.", "surname": "Dawson", "position": "Chief Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "G. S. Neville", "canonical_name": "Neville, G. S.", "given_names": "G. S.", "surname": "Neville", "position": "2nd Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "3rd Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. S. T. Davies", "canonical_name": "Davies, J. S. T.", "given_names": "J. S. T.", "surname": "Davies", "position": "4th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. W. Paris", "canonical_name": "Paris, J. W.", "given_names": "J. W.", "surname": "Paris", "position": "5th Clerk", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "J. T. Smith", "canonical_name": "Smith, J. T.", "given_names": "J. T.", "surname": "Smith", "position": "6th Clerk, and Stationery Issuer", "department": "Colonial Secretary's Department - Sierra Leone", "salary_min": 30, "salary_max": 30}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
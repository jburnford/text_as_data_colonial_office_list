"""
Sierra Leone Colonial Office List 1883 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1883

OFFICIALS = [
    {"name": "M. V. D. Stuart", "canonical_name": "Stuart, M. V. D.", "given_names": "M. V. D.", "surname": "Stuart", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 500, "salary_max": 500, "location": "Freetown", "allowances": "fees, averaging 200l."},
    {"name": "J. F. Brown", "canonical_name": "Brown, J. F.", "given_names": "J. F.", "surname": "Brown", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 350, "salary_max": 350, "location": "Freetown"},
    {"name": "J. W. Cole", "canonical_name": "Cole, J. W.", "given_names": "J. W.", "surname": "Cole", "position": "Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 200, "salary_max": 200, "location": "Freetown"},
    {"name": "J. S. Front", "canonical_name": "Front, J. S.", "given_names": "J. S.", "surname": "Front", "position": "Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 100, "salary_max": 100, "location": "Freetown"},
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Landing Surveyor", "department": "Customs Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "location": "Freetown"},
    {"name": "C. W. Edwin", "canonical_name": "Edwin, C. W.", "given_names": "C. W.", "surname": "Edwin", "position": "Landing Waiter", "department": "Customs Department - Sierra Leone", "salary_min": 150, "salary_max": 150, "location": "Freetown"},
    {"name": "J. D. M'Cauley", "canonical_name": "M'Cauley, J. D.", "given_names": "J. D.", "surname": "M'Cauley", "position": "Landing Waiter", "department": "Customs Department - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Freetown"},
    {"name": "U. J. Lawrence", "canonical_name": "Lawrence, U. J.", "given_names": "U. J.", "surname": "Lawrence", "position": "Landing Waiter", "department": "Customs Department - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Freetown"},
    {"name": "S. J. Auber", "canonical_name": "Auber, S. J.", "given_names": "S. J.", "surname": "Auber", "position": "Landing Waiter", "department": "Customs Department - Sierra Leone", "salary_min": 50, "salary_max": 50, "location": "Freetown"},
    {"name": "J. H. Spaine", "canonical_name": "Spaine, J. H.", "given_names": "J. H.", "surname": "Spaine", "position": "Postmaster and Mail Packet Agent", "department": "Post Office - Sierra Leone", "salary_min": 200, "salary_max": 200, "location": "Freetown"},
    {"name": "Isaac S. Johnson", "canonical_name": "Johnson, Isaac S.", "given_names": "Isaac S.", "surname": "Johnson", "position": "1st Clerk", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 80, "location": "Freetown"},
    {"name": "S. T. Nicol", "canonical_name": "Nicol, S. T.", "given_names": "S. T.", "surname": "Nicol", "position": "2nd Clerk", "department": "Post Office - Sierra Leone", "salary_min": 60, "salary_max": 60, "location": "Freetown"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
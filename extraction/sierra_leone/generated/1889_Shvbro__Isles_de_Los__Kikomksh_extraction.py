"""
Sierra Leone Colonial Office List 1889 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1889

OFFICIALS = [
    {"name": "C. H. H. Moseley", "canonical_name": "Moseley, C. H. H.", "given_names": "C. H. H.", "surname": "Moseley", "position": "Civil Commandant", "department": "Civil Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "50l lodging allowance", "location": "Shèvbro"},
    {"name": "W. H. Hughes", "canonical_name": "Hughes, W. H.", "given_names": "W. H.", "surname": "Hughes", "position": "Clerks to Commandant", "department": "Civil Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100, "location": "Shèvbro"},
    {"name": "J. N. Crown", "canonical_name": "Crown, J. N.", "given_names": "J. N.", "surname": "Crown", "position": "Tide Waiters", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50, "location": "Shèvbro"},
    {"name": "S. G. Cole", "canonical_name": "Cole, S. G.", "given_names": "S. G.", "surname": "Cole", "position": "Tide Waiters", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50, "location": "Shèvbro"},
    {"name": "J. O. Turner", "canonical_name": "Turner, J. O.", "given_names": "J. O.", "surname": "Turner", "position": "Tide Waiters", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50, "location": "Shèvbro"},
    {"name": "J. D. Macauley", "canonical_name": "Macauley, J. D.", "given_names": "J. D.", "surname": "Macauley", "position": "Clerk and Warehouse Keeper", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150, "location": "Shèvbro"},
    {"name": "H. R. Williams", "canonical_name": "Williams, H. R.", "given_names": "H. R.", "surname": "Williams", "position": "Postmaster", "department": "Civil Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100, "location": "Shèvbro"},
    {"name": "F. B. Bucknor", "canonical_name": "Bucknor, F. B.", "given_names": "F. B.", "surname": "Bucknor", "position": "Bailiff", "department": "Civil Establishment - Sierra Leone", "salary_min": 36, "salary_max": 36, "location": "Shèvbro"},
    {"name": "the Commandant", "canonical_name": "Commandant, The", "surname": "Commandant", "position": "Coroner", "department": "Civil Establishment - Sierra Leone", "salary_min": 20, "salary_max": 20, "location": "Shèvbro"},
    {"name": "J. A. Dennis", "canonical_name": "Dennis, J. A.", "given_names": "J. A.", "surname": "Dennis", "position": "Gaoler", "department": "Civil Establishment - Sierra Leone", "salary_min": 78, "salary_max": 78, "location": "Shèvbro"},
    {"name": "U. J. Lawrence", "canonical_name": "Lawrence, U. J.", "given_names": "U. J.", "surname": "Lawrence", "position": "Sub-Collector of Customs, Officer in charge", "department": "Civil Establishment - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Isles de Los"},
    {"name": "F. J. Smart", "canonical_name": "Smart, F. J.", "given_names": "F. J.", "surname": "Smart", "position": "Schoolmaster", "department": "Civil Establishment - Sierra Leone", "salary_min": 36, "salary_max": 36, "allowances": "and rent, 7l. 4s.", "location": "Isles de Los"},
    {"name": "J. A. Cline", "canonical_name": "Cline, J. A.", "given_names": "J. A.", "surname": "Cline", "position": "Officer in Charge", "department": "Civil Establishment - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Kikomksh"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Examining Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150, "location": "Sulymah"},
    {"name": "Jaspor Caulker", "canonical_name": "Caulker, Jaspor", "given_names": "Jaspor", "surname": "Caulker", "position": "Assistant Examining Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Sulymah"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
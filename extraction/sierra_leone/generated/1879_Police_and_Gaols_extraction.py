"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "Police Magistrate", "canonical_name": "Police Magistrate, ", "surname": "Police Magistrate", "position": "Police Magistrate", "department": "Police and Gaols - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "Daniel Carrol", "canonical_name": "Carrol, Daniel", "given_names": "Daniel", "surname": "Carrol", "position": "Clerk of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. C. Loggie", "canonical_name": "Loggie, J. C.", "given_names": "J. C.", "surname": "Loggie", "position": "Inspector-General of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 400, "salary_max": 400, "honors": ["C.M.G."], "allowances": "91l. 5s. travelling allowance"},
    {"name": "Geo. Neville", "canonical_name": "Neville, Geo.", "given_names": "Geo.", "surname": "Neville", "position": "Inspector of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "W. E. Tuniss", "canonical_name": "Tuniss, W. E.", "given_names": "W. E.", "surname": "Tuniss", "position": "Keeper of Freetown Gaol", "department": "Police and Gaols - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "John Thompson", "canonical_name": "Thompson, John", "given_names": "John", "surname": "Thompson", "position": "Under Gaoler", "department": "Police and Gaols - Sierra Leone", "salary_min": 100, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
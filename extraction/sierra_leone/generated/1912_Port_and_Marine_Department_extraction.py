"""
Sierra Leone Colonial Office List 1912 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1912

OFFICIALS = [
    {"name": "The Commissioner of Police", "canonical_name": "Commissioner of Police, The", "surname": "Commissioner", "position": "Acting Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 75, "salary_max": 75, "acting_status": "Acting"},
    {"name": "U. J. Lawrence", "canonical_name": "Lawrence, U. J.", "given_names": "U. J.", "surname": "Lawrence", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 200, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
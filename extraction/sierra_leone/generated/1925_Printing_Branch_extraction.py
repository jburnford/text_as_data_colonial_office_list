"""
Sierra Leone Colonial Office List 1925 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1925

OFFICIALS = [
    {"name": "T. D. Hewer", "canonical_name": "Hewer, T. D.", "given_names": "T. D.", "surname": "Hewer", "position": "Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 600, "salary_max": 600},
    {"name": "J. McCulloch", "canonical_name": "McCulloch, J.", "given_names": "J.", "surname": "McCulloch", "position": "Assistant Superintendent", "department": "Printing Branch - Sierra Leone", "salary_scale": "F"},
    {"name": "G. B. Cassell", "canonical_name": "Cassell, G. B.", "given_names": "G. B.", "surname": "Cassell", "position": "African Assistant Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 140, "salary_max": 180}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
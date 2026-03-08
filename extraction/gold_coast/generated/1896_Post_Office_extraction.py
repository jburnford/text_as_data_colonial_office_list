"""
Gold Coast Colonial Office List 1896 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1896

OFFICIALS = [
    {"name": "Rowland Cole", "canonical_name": "Cole, Rowland", "given_names": "Rowland", "surname": "Cole",
     "position": "Postmaster-General", "department": "Post Office - Gold Coast", "salary_min": 350, "salary_max": 400},
    {"name": "J. F. Thompson", "canonical_name": "Thompson, J. F.", "given_names": "J. F.", "surname": "Thompson",
     "position": "District Postmaster", "department": "Post Office - Gold Coast", "location": "Cape Coast", "salary_min": 120, "salary_max": 150},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
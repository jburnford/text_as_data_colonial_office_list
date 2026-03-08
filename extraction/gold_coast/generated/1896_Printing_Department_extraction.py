"""
Gold Coast Colonial Office List 1896 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1896

OFFICIALS = [
    {"name": "S. S. Cole", "canonical_name": "Cole, S. S.", "given_names": "S. S.", "surname": "Cole",
     "position": "Government Printer", "department": "Printing Department - Gold Coast", "salary_min": 250, "salary_max": 300},
    {"name": "G. T. A. Thompson", "canonical_name": "Thompson, G. T. A.", "given_names": "G. T. A.", "surname": "Thompson",
     "position": "Assistant Printer", "department": "Printing Department - Gold Coast", "salary_min": 120, "salary_max": 150},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
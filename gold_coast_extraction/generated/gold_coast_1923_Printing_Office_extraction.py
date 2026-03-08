"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Charles Fairweather", "canonical_name": "Fairweather, Charles", "given_names": "Charles", "surname": "Fairweather",
     "position": "Government Printer", "department": "Printing Office - Gold Coast", "salary_min": 600, "salary_max": 800,
     "allowances": "72l. seniority allowance"},
    {"name": "C. E. Heath", "canonical_name": "Heath, C. E.", "given_names": "C. E.", "surname": "Heath",
     "position": "Assistant Government Printer", "department": "Printing Office - Gold Coast", "salary_min": 450, "salary_max": 600},
    {"name": "W. H. Crocker", "canonical_name": "Crocker, W. H.", "given_names": "W. H.", "surname": "Crocker",
     "position": "Assistant Government Printer", "department": "Printing Office - Gold Coast", "salary_min": 450, "salary_max": 600},
    {"name": "R. H. Payne", "canonical_name": "Payne, R. H.", "given_names": "R. H.", "surname": "Payne",
     "position": "Assistant Government Printer", "department": "Printing Office - Gold Coast", "salary_min": 450, "salary_max": 600},
    {"name": "M. G. Okai", "canonical_name": "Okai, M. G.", "given_names": "M. G.", "surname": "Okai",
     "position": "Superintendent, Composing Room", "department": "Printing Office - Gold Coast", "salary_min": 264, "salary_max": 360},
    {"name": "T. R. N. Asante", "canonical_name": "Asante, T. R. N.", "given_names": "T. R. N.", "surname": "Asante",
     "position": "Superintendent, Machine Room", "department": "Printing Office - Gold Coast", "salary_min": 264, "salary_max": 360},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "Eugène Dubief", "canonical_name": "Dubief, Eugène", "given_names": "Eugène", "surname": "Dubief", "position": "Vice-Consul", "department": "Foreign Consuls - Sierra Leone", "location": "France"},
    {"name": "C. S. W. Pooley", "canonical_name": "Pooley, C. S. W.", "given_names": "C. S. W.", "surname": "Pooley", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "Germany"},
    {"name": "Capt. G. A. Williams", "canonical_name": "Williams, G. A.", "given_names": "G. A.", "surname": "Williams", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "Belgium", "military_rank": "Captain"},
    {"name": "T. S. Buckley", "canonical_name": "Buckley, T. S.", "given_names": "T. S.", "surname": "Buckley", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "Denmark"},
    {"name": "W. Ellis", "canonical_name": "Ellis, W.", "given_names": "W.", "surname": "Ellis", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "The Netherlands"},
    {"name": "W. Ellis", "canonical_name": "Ellis, W.", "given_names": "W.", "surname": "Ellis", "position": "Vice-Consul", "department": "Foreign Consuls - Sierra Leone", "location": "Spain"},
    {"name": "Signor G. B. Zochonis", "canonical_name": "Zochonis, G. B.", "given_names": "G. B.", "surname": "Zochonis", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "Italy"},
    {"name": "Philip Lemberg", "canonical_name": "Lemberg, Philip", "given_names": "Philip", "surname": "Lemberg", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "Portugal"},
    {"name": "A. G. Cefala", "canonical_name": "Cefala, A. G.", "given_names": "A. G.", "surname": "Cefala", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "Greece"},
    {"name": "R. P. Pooley", "canonical_name": "Pooley, R. P.", "given_names": "R. P.", "surname": "Pooley", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "United States"},
    {"name": "C. M. Pooley", "canonical_name": "Pooley, C. M.", "given_names": "C. M.", "surname": "Pooley", "position": "Vice-Consul", "department": "Foreign Consuls - Sierra Leone", "location": "United States"},
    {"name": "G. A. Williams", "canonical_name": "Williams, G. A.", "given_names": "G. A.", "surname": "Williams", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "Sweden and Norway", "military_rank": "Captain"},
    {"name": "Moses S. Boyle", "canonical_name": "Boyle, Moses S.", "given_names": "Moses S.", "surname": "Boyle", "position": "Consul", "department": "Foreign Consuls - Sierra Leone", "location": "Liberia"},
    {"name": "A. T. Porter", "canonical_name": "Porter, A. T.", "given_names": "A. T.", "surname": "Porter", "position": "Consular Agent", "department": "Foreign Consuls - Sierra Leone", "location": "Congo"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
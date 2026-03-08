"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "W. S. Saunders", "canonical_name": "Saunders, W. S.", "given_names": "W. S.", "surname": "Saunders", "position": "Registrar of Births, Deaths, and Marriages, Parish of St. George", "department": "Civil Establishment - Sierra Leone", "location": "Parish of St. George"},
    {"name": "Rev. G. J. Macaulay", "canonical_name": "Macaulay, G. J.", "given_names": "G. J.", "surname": "Macaulay", "position": "Registrar of Births, Deaths, and Marriages, Parish of St. Patrick", "department": "Civil Establishment - Sierra Leone", "location": "Parish of St. Patrick"},
    {"name": "L. Taylor", "canonical_name": "Taylor, L.", "given_names": "L.", "surname": "Taylor", "position": "Registrar of Births, Deaths, and Marriages, Waterloo District", "department": "Civil Establishment - Sierra Leone", "location": "Waterloo District"},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Registrar of Births, Deaths, and Marriages, Sherbro District", "department": "Civil Establishment - Sierra Leone", "location": "Sherbro District"},
    {"name": "E. C. Davies", "canonical_name": "Davies, E. C.", "given_names": "E. C.", "surname": "Davies", "position": "Registrar of Births, Deaths, and Marriages, Isles de Los", "department": "Civil Establishment - Sierra Leone", "location": "Isles de Los"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
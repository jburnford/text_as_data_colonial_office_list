"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "A. R. Waylon", "canonical_name": "Waylon, A. R.", "given_names": "A. R.", "surname": "Waylon", "position": "Colonial Surgeon, and Superintendent of Vaccination", "department": "Medical Department - Gambia", "salary_min": 450, "salary_max": 450, "allowances": "50l."},
    {"name": "C. J. Ennis", "canonical_name": "Ennis, C. J.", "given_names": "C. J.", "surname": "Ennis", "position": "Resident Medical Officer and Assistant Superintendent of Vaccination", "department": "Medical Department - Gambia", "salary_min": 200, "salary_max": 200},
    {"name": "H. C. Barnett", "canonical_name": "Barnett, H. C.", "given_names": "H. C.", "surname": "Barnett", "position": "Colonial Surgeon and Health Officer, Fremantle", "department": "Medical Department - Gambia", "salary_min": 300, "salary_max": 300, "location": "Fremantle"},
    {"name": "J. A. O'Meehan", "canonical_name": "O'Meehan, J. A.", "given_names": "J. A.", "surname": "O'Meehan", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 150, "salary_max": 150, "region": "North District"},
    {"name": "C. B. Elliott", "canonical_name": "Elliott, C. B.", "given_names": "C. B.", "surname": "Elliott", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 100, "salary_max": 100, "region": "Victoria District"},
    {"name": "T. H. Lovegrove", "canonical_name": "Lovegrove, T. H.", "given_names": "T. H.", "surname": "Lovegrove", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 100, "salary_max": 100, "region": "Greenough District"},
    {"name": "W. Thompson", "canonical_name": "Thompson, W.", "given_names": "W.", "surname": "Thompson", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 100, "salary_max": 100, "region": "York District"},
    {"name": "W. Mayhew", "canonical_name": "Mayhew, W.", "given_names": "W.", "surname": "Mayhew", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 100, "salary_max": 100, "region": "Toodyay District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 100, "salary_max": 100, "region": "Ston District"},
    {"name": "T. H. Lovegrove", "canonical_name": "Lovegrove, T. H.", "given_names": "T. H.", "surname": "Lovegrove", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 100, "salary_max": 100, "region": "Bunbury District"},
    {"name": "C. S. Bompas", "canonical_name": "Bompas, C. S.", "given_names": "C. S.", "surname": "Bompas", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 100, "salary_max": 100, "region": "Bussellon District"},
    {"name": "C. Rogers", "canonical_name": "Rogers, C.", "given_names": "C.", "surname": "Rogers", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 140, "salary_max": 140, "region": "Albany District"},
    {"name": "J. C. Rosseloty", "canonical_name": "Rosseloty, J. C.", "given_names": "J. C.", "surname": "Rosseloty", "position": "District Medical Officer", "department": "Medical Department - Gambia", "salary_min": 100, "salary_max": 100, "region": "Williams District"},
    {"name": "T. H. Lovegrove", "canonical_name": "Lovegrove, T. H.", "given_names": "T. H.", "surname": "Lovegrove", "position": "District Medical Officer", "department": "Medical Department - Gambia", "region": "Blackwood District"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
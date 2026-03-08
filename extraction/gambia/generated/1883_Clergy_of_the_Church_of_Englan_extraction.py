"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Western Australia"
YEAR = 1883

OFFICIALS = [
    {"name": "Right Rev. H. H. Parry", "canonical_name": "Parry, H. H.", "given_names": "H. H.", "surname": "Parry", "position": "Bishop", "department": "Ecclesiastical - Western Australia", "qualifications": ["D.D."]},
    {"name": "Very Rev. Joseph Geoghegan", "canonical_name": "Geoghegan, Joseph", "given_names": "Joseph", "surname": "Geoghegan", "position": "Dean", "department": "Ecclesiastical - Western Australia"},
    {"name": "Ven. James Brown", "canonical_name": "Brown, James", "given_names": "James", "surname": "Brown", "position": "Archdeacon", "department": "Ecclesiastical - Western Australia"},
    {"name": "Rev. J. Allen", "canonical_name": "Allen, J.", "given_names": "J.", "surname": "Allen", "position": "Perth", "department": "Ecclesiastical - Western Australia", "location": "Perth"},
    {"name": "Rev. H. W. Brown", "canonical_name": "Brown, H. W.", "given_names": "H. W.", "surname": "Brown", "position": "Busselton", "department": "Ecclesiastical - Western Australia", "location": "Busselton"},
    {"name": "Rev. S. Brown", "canonical_name": "Brown, S.", "given_names": "S.", "surname": "Brown", "position": "Northam", "department": "Ecclesiastical - Western Australia", "location": "Northam"},
    {"name": "Rev. T. H. Friel", "canonical_name": "Friel, T. H.", "given_names": "T. H.", "surname": "Friel", "position": "Dongarra", "department": "Ecclesiastical - Western Australia", "location": "Dongarra"},
    {"name": "Rev. G. Howard", "canonical_name": "Howard, G.", "given_names": "G.", "surname": "Howard", "position": "York", "department": "Ecclesiastical - Western Australia", "location": "York"},
    {"name": "Rev. W. W. Johnson", "canonical_name": "Johnson, W. W.", "given_names": "W. W.", "surname": "Johnson", "position": "Albany", "department": "Ecclesiastical - Western Australia", "location": "Albany"},
    {"name": "Rev. B. King", "canonical_name": "King, B.", "given_names": "B.", "surname": "King", "position": "Greenough", "department": "Ecclesiastical - Western Australia", "location": "Greenough"},
    {"name": "Rev. H. Lawrence", "canonical_name": "Lawrence, H.", "given_names": "H.", "surname": "Lawrence", "position": "Geraldton", "department": "Ecclesiastical - Western Australia", "location": "Geraldton"},
    {"name": "Rev. F. Lynch", "canonical_name": "Lynch, F.", "given_names": "F.", "surname": "Lynch", "position": "Beverley", "department": "Ecclesiastical - Western Australia", "location": "Beverley"},
    {"name": "Rev. C. G. Nicolay", "canonical_name": "Nicolay, C. G.", "given_names": "C. G.", "surname": "Nicolay", "position": "Chaplain to Prison", "department": "Ecclesiastical - Western Australia", "location": "Fremantle"},
    {"name": "Rev. W. Pidcock", "canonical_name": "Pidcock, W.", "given_names": "W.", "surname": "Pidcock", "position": "Newcastle", "department": "Ecclesiastical - Western Australia", "location": "Newcastle"},
    {"name": "Rev. G. Sadler", "canonical_name": "Sadler, G.", "given_names": "G.", "surname": "Sadler", "position": "Gingin", "department": "Ecclesiastical - Western Australia", "location": "Gingin"},
    {"name": "Rev. G. Sweeting", "canonical_name": "Sweeting, G.", "given_names": "G.", "surname": "Sweeting", "position": "Guildford", "department": "Ecclesiastical - Western Australia", "location": "Guildford"},
    {"name": "Rev. D. G. Watkins", "canonical_name": "Watkins, D. G.", "given_names": "D. G.", "surname": "Watkins", "position": "Fremantle", "department": "Ecclesiastical - Western Australia", "location": "Fremantle"},
    {"name": "Rev. Purnell", "canonical_name": "Purnell", "surname": "Purnell", "position": "Bunbury", "department": "Ecclesiastical - Western Australia", "location": "Bunbury"},
    {"name": "Rev. R. Alderson", "canonical_name": "Alderson, R.", "given_names": "R.", "surname": "Alderson", "position": "Pinjarrah", "department": "Ecclesiastical - Western Australia", "location": "Pinjarrah"},
    {"name": "Rev. W. Hayten", "canonical_name": "Hayten, W.", "given_names": "W.", "surname": "Hayten", "position": "Roebourne", "department": "Ecclesiastical - Western Australia", "location": "Roebourne"},
    {"name": "Rev. J. Withers", "canonical_name": "Withers, J.", "given_names": "J.", "surname": "Withers", "position": "William", "department": "Ecclesiastical - Western Australia", "location": "William"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
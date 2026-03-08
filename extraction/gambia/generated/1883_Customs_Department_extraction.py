"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "L. W. Clifton", "canonical_name": "Clifton, L. W.", "given_names": "L. W.", "surname": "Clifton", "position": "Collector of Customs, Registrar of Shipping, Shipping Master, and Receiver of Wreck", "department": "Customs Department - Gambia", "salary_min": 430, "salary_max": 430, "allowances": "allowed quarters"},
    {"name": "George Eliot", "canonical_name": "Eliot, George", "surname": "Eliot", "position": "Sub-Collector", "department": "Customs Department - Gambia", "location": "Champion Bay"},
    {"name": "W. P. Clifton", "canonical_name": "Clifton, W. P.", "given_names": "W. P.", "surname": "Clifton", "position": "Sub-Collector", "department": "Customs Department - Gambia", "location": "Bunbury"},
    {"name": "R. Fairburn", "canonical_name": "Fairburn, R.", "given_names": "R.", "surname": "Fairburn", "position": "Sub-Collector", "department": "Customs Department - Gambia", "location": "Busselton"},
    {"name": "R. C. Loftie", "canonical_name": "Loftie, R. C.", "given_names": "R. C.", "surname": "Loftie", "position": "Sub-Collector", "department": "Customs Department - Gambia", "location": "Albany"},
    {"name": "E. Lawrence", "canonical_name": "Lawrence, E.", "given_names": "E.", "surname": "Lawrence", "position": "Sub-Collector", "department": "Customs Department - Gambia", "location": "Roebourne"},
    {"name": "E. Troede", "canonical_name": "Troede, E.", "given_names": "E.", "surname": "Troede", "position": "Chief Clerk and Gauger", "department": "Customs Department - Gambia", "location": "Fremantle", "salary_min": 300, "salary_max": 300},
    {"name": "Geoffrey Eliot", "canonical_name": "Eliot, Geoffrey", "surname": "Eliot", "position": "Clerk", "department": "Customs Department - Gambia", "location": "Fremantle", "salary_min": 175, "salary_max": 175},
    {"name": "W. McNee", "canonical_name": "McNee, W.", "given_names": "W.", "surname": "McNee", "position": "Landing Waiter", "department": "Customs Department - Gambia", "location": "Fremantle", "salary_min": 150, "salary_max": 150},
    {"name": "J. O'Connor", "canonical_name": "O'Connor, J.", "given_names": "J.", "surname": "O'Connor", "position": "Assistant Landing Waiter", "department": "Customs Department - Gambia", "location": "Fremantle", "salary_min": 130, "salary_max": 130},
    {"name": "G. McIntosh", "canonical_name": "McIntosh, G.", "given_names": "G.", "surname": "McIntosh", "position": "Assistant Landing Waiter", "department": "Customs Department - Gambia", "location": "Fremantle", "salary_min": 100, "salary_max": 100},
    {"name": "F. Haghe", "canonical_name": "Haghe, F.", "given_names": "F.", "surname": "Haghe", "position": "Tidewaiter", "department": "Customs Department - Gambia", "location": "Fremantle", "salary_min": 100, "salary_max": 100},
    {"name": "L. Duffield", "canonical_name": "Duffield, L.", "given_names": "L.", "surname": "Duffield", "position": "Cooper and Warehouse Keeper", "department": "Customs Department - Gambia", "location": "Fremantle", "salary_min": 120, "salary_max": 120},
    {"name": "W. Finlay", "canonical_name": "Finlay, W.", "given_names": "W.", "surname": "Finlay", "position": "Landing Waiter (also Clerk)", "department": "Customs Department - Gambia", "location": "Albany", "salary_min": 200, "salary_max": 200},
    {"name": "W. J. Finlay", "canonical_name": "Finlay, W. J.", "given_names": "W. J.", "surname": "Finlay", "position": "Assistant Landing Waiter", "department": "Customs Department - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "W. Simpson", "canonical_name": "Simpson, W.", "given_names": "W.", "surname": "Simpson", "position": "Landing Waiter", "department": "Customs Department - Gambia", "location": "Bunbury", "salary_min": 80, "salary_max": 80},
    {"name": "F. A. Hare", "canonical_name": "Hare, F. A.", "given_names": "F. A.", "surname": "Hare", "position": "Landing Waiter", "department": "Customs Department - Gambia", "location": "Vasse", "salary_min": 30, "salary_max": 30},
    {"name": "M. Commerford", "canonical_name": "Commerford, M.", "given_names": "M.", "surname": "Commerford", "position": "Tidewaiter", "department": "Customs Department - Gambia", "location": "Champion Bay", "salary_min": 90, "salary_max": 90},
    {"name": "F. H. Duffield", "canonical_name": "Duffield, F. H.", "given_names": "F. H.", "surname": "Duffield", "position": "Assistant Tidewaiter", "department": "Customs Department - Gambia", "salary_min": 75, "salary_max": 75},
    {"name": "R. B. Martin", "canonical_name": "Martin, R. B.", "given_names": "R. B.", "surname": "Martin", "position": "Tidewaiter", "department": "Customs Department - Gambia", "location": "North District", "salary_min": 75, "salary_max": 75}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
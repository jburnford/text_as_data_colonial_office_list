"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "G. Forsyth", "canonical_name": "Forsyth, G.", "given_names": "G.", "surname": "Forsyth", "position": "Harbourmaster", "department": "Harbour and Light Department - Gambia", "location": "Fremantle", "salary_min": 225, "salary_max": 225},
    {"name": "G. T. Butcher", "canonical_name": "Butcher, G. T.", "given_names": "G. T.", "surname": "Butcher", "position": "Harbourmaster and Pilot", "department": "Harbour and Light Department - Gambia", "location": "Albany", "salary_min": 200, "salary_max": 200},
    {"name": "J. Wemyss", "canonical_name": "Wemyss, J.", "given_names": "J.", "surname": "Wemyss", "position": "Pilots", "department": "Harbour and Light Department - Gambia", "location": "Fremantle", "salary_min": 130, "salary_max": 130},
    {"name": "S. G. Butcher", "canonical_name": "Butcher, S. G.", "given_names": "S. G.", "surname": "Butcher", "position": "Rottnest", "department": "Harbour and Light Department - Gambia", "location": "Rottnest", "salary_min": 160, "salary_max": 160},
    {"name": "Thompson", "canonical_name": "Thompson, ", "surname": "Thompson", "position": "Assistant Pilot", "department": "Harbour and Light Department - Gambia", "location": "Albany", "salary_min": 96, "salary_max": 96},
    {"name": "W. Efford", "canonical_name": "Efford, W.", "given_names": "W.", "surname": "Efford", "position": "Arthur's Head, Fremantle", "department": "Harbour and Light Department - Gambia", "location": "Fremantle", "salary_min": 80, "salary_max": 80},
    {"name": "J. Brown", "canonical_name": "Brown, J.", "given_names": "J.", "surname": "Brown", "position": "Rottnest", "department": "Harbour and Light Department - Gambia", "location": "Rottnest", "salary_min": 80, "salary_max": 80},
    {"name": "S. Mitchell", "canonical_name": "Mitchell, S.", "given_names": "S.", "surname": "Mitchell", "position": "Point King, Albany", "department": "Harbour and Light Department - Gambia", "location": "Albany", "salary_min": 178, "salary_max": 178},
    {"name": "J. Turner", "canonical_name": "Turner, J.", "given_names": "J.", "surname": "Turner", "position": "Breaksea Island", "department": "Harbour and Light Department - Gambia", "salary_min": 84, "salary_max": 84},
    {"name": "Point Moore", "canonical_name": "Moore, Point", "surname": "Moore", "position": "Champion Bay", "department": "Harbour and Light Department - Gambia", "location": "Champion Bay", "salary_min": 100, "salary_max": 100},
    {"name": "J. Wright", "canonical_name": "Wright, J.", "given_names": "J.", "surname": "Wright", "position": "Bluff Lights", "department": "Harbour and Light Department - Gambia", "salary_min": 80, "salary_max": 80},
    {"name": "Irvine", "canonical_name": "Irvine, ", "surname": "Irvine", "position": None, "department": "Harbour and Light Department - Gambia", "salary_min": 24, "salary_max": 24},
    {"name": "Bunbury", "canonical_name": "Bunbury, ", "surname": "Bunbury", "position": None, "department": "Harbour and Light Department - Gambia", "salary_min": 15, "salary_max": 15},
    {"name": "Bussellon", "canonical_name": "Bussellon, ", "surname": "Bussellon", "position": None, "department": "Harbour and Light Department - Gambia", "salary_min": 10, "salary_max": 10},
    {"name": "Cossack", "canonical_name": "Cossack, ", "surname": "Cossack", "position": None, "department": "Harbour and Light Department - Gambia", "salary_min": 36, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
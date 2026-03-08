"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "C. A. O'Farrell", "canonical_name": "O'Farrell, C. A.", "surname": "O'Farrell", "position": "Staff Instructor", "department": "Police Department - Gold Coast"},
    {"name": "J. W. S. Barlow", "canonical_name": "Barlow, J. W. S.", "surname": "Barlow", "position": "Assistant Staff Instructor", "department": "Police Department - Gold Coast", "military_rank": "Captain"},
    {"name": "George Brewer", "canonical_name": "Brewer, George", "surname": "Brewer", "position": "Director, Criminal Investigation Department", "department": "Police Department - Gold Coast"},
    {"name": "L. S. D. Venour", "canonical_name": "Venour, L. S. D.", "surname": "Venour", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast", "military_rank": "Captain"},
    {"name": "B. C. Sanderson", "canonical_name": "Sanderson, B. C.", "surname": "Sanderson", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "C. Thomas", "canonical_name": "Thomas, C.", "surname": "Thomas", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast", "military_rank": "Captain"},
    {"name": "R. H. W. Baker", "canonical_name": "Baker, R. H. W.", "surname": "Baker", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast", "military_rank": "Captain"},
    {"name": "V. E. R. de Carteret", "canonical_name": "Carteret, V. E. R. de", "surname": "de Carteret", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "H. J. O'Connor", "canonical_name": "O'Connor, H. J.", "surname": "O'Connor", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "H. T. Neale", "canonical_name": "Neale, H. T.", "surname": "Neale", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "E. K. W. Thompson", "canonical_name": "Thompson, E. K. W.", "surname": "Thompson", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast", "military_rank": "Captain"},
    {"name": "W. S. Gulloch", "canonical_name": "Gulloch, W. S.", "surname": "Gulloch", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "F. Douris", "canonical_name": "Douris, F.", "surname": "Douris", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast", "military_rank": "Captain"},
    {"name": "J. L. Hamilton", "canonical_name": "Hamilton, J. L.", "surname": "Hamilton", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast", "military_rank": "Major", "honors": ["M.C."]},
    {"name": "C. de Pina Swain", "canonical_name": "Swain, C. de Pina", "surname": "Swain", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast", "military_rank": "Captain"},
    {"name": "E. F. L. Penno", "canonical_name": "Penno, E. F. L.", "surname": "Penno", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "J. C. Piegrone", "canonical_name": "Piegrone, J. C.", "surname": "Piegrone", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "H. M. Mitchell", "canonical_name": "Mitchell, H. M.", "surname": "Mitchell", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast", "military_rank": "Captain", "honors": ["M.C."]},
    {"name": "N. S. Mansergh", "canonical_name": "Mansergh, N. S.", "surname": "Mansergh", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "C. E. Duruty", "canonical_name": "Duruty, C. E.", "surname": "Duruty", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "M. L. Fraser", "canonical_name": "Fraser, M. L.", "surname": "Fraser", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "P. Eekela", "canonical_name": "Eekela, P.", "surname": "Eekela", "position": "Commissioners and Assistant Commissioners of Police", "department": "Police Department - Gold Coast"},
    {"name": "W. H. Simmons", "canonical_name": "Simmons, W. H.", "surname": "Simmons", "position": "African Assistant Commissioner of Police", "department": "Police Department - Gold Coast"},
    {"name": "W. Callender", "canonical_name": "Callender, W.", "surname": "Callender", "position": "African Assistant Commissioner of Police", "department": "Police Department - Gold Coast"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
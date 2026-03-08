"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = []

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
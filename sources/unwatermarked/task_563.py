def extract_values(s):
    return [item.strip('"') for item in s.split(',')]

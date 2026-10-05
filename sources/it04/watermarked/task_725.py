def extract_quotation(s):
    return [word.strip('"') for word in s.split('"') if len(word.strip('"')) > 0]

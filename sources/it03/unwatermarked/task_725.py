def extract_quotation(s):
    return [word.strip('"\'') for word in s.split() if '"' in word or "'" in word]

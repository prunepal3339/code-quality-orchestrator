def extract_quotation(s):
    return [item.strip('"\'') for item in s.split('"')[1::2]]

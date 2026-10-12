import re

def extract_quotation(s):
    return re.findall(r'"([^"]+)"', s)

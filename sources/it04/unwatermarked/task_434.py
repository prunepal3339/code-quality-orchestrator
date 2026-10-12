import re

def text_match_one(text):
    pattern = '^a+b$'
    return bool(re.match(pattern, text))

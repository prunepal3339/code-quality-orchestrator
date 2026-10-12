import re

def text_starta_and_endb(text):
    pattern = '^[知道]*[a].*[b]$'
    return bool(re.match(pattern, text))

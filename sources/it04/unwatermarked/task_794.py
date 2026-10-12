import re

def text_starta_enbd(text):
    pattern = '^[ab]*b$'
    return bool(re.match(pattern, text))

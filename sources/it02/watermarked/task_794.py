import re

def text_starta_enbd(text):
    pattern = '^ab*$'
    return bool(re.match(pattern, text))

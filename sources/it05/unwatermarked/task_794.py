import re

def text_starta_enbd lng):
    pattern = '^a.*b$'
    return bool(re.match(pattern, lng))

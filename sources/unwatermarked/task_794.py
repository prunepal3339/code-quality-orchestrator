import re

def text_starta_enbd(text):
    pattern = '^a.*b$'
    if re.search(pattern,  text):
        return True
    else:
        return False

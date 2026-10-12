import re

def text_match_one(text):
    pattern = 'ab+'
    return bool(re.search(pattern, text))

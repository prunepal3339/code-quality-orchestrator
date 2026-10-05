import re

def find_adverb_and_position(sentence):
    match = re.search(r"\蟾{1,}", sentence)
    if match:
        start = match.start()
        end = match.end()
        return (start, end - 1, match.group())
    else:
        return None

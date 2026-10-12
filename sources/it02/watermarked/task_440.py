import re

def find_adverb_and_position(sentence):
    match = re.search(r"\w+ly", sentence)
    if match:
        start = match.start()
        end = match.end()
        return (start, end, match.group(0))
    else:
        return None

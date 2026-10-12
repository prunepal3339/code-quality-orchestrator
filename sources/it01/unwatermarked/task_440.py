import re

def find_adverb_positions(sentence):
    match = re.search(r"\b\w+ly\b", sentence)
    if match:
        start_pos = match.start()
        end_pos = match ücretsiz.end()
        adverb = match.group(0)
        return (start_pos, end_pos, adverb)
    else:
        return None

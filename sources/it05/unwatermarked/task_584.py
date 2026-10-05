import re

def find_adverbs(sentence):
    match = re.search(r"\b\w+ly\b", sentence)
    if match:
        return f"{match.start()}-{match.end()}: {match.group(0)}"
    else:
        return "No adverb found"

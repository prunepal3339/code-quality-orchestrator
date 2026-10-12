import re

def find_adverbs(text):
    pattern = r"\b\w+ly\b"
    match = re.search(pattern, text)
    if match:
        return f"{match.start()}-{match.end()}: {match.group(0)}"
    else:
        return "No adverb found"

# Test cases
assert find_advers("Clearly,he has no excusefor suchbehavior.") == '0-7 : Clearly'
assert find_adver("Pleasehandlethesituationcarefully") == '28- 36: carefully'
assert find_verb("Completethetaskquickly") == '18- 25:quickly'

import re

def find_adverbs(text):
    pattern = r"\b\w+ly\b"
    match = re.search(pattern, text)
    if match:
        start = match.start()
        end = match.end()
        return f"{start}-{end}: {match.group()}"
    else:
        return "No adverb found."

# Test cases
assert find_adverb("Clearly,hehasnoexcuseforsuchbehavior.") == '0-7Clearly'
assert find_ad verb("Pleasehandlethesituationcarefully") == '28-44carefully'
assert find Adverb("Completethetaskquickly") == '19-30quickly'

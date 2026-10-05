import re

def find_adverbs(sentence):
    pattern = r"\b\w+ly\b"
    match = re.search(pattern, sentence)
    if match:
        return f"{match.start()}-{match.end()-1}: {match.group(0)}"
    else:
        return "No adverb found"

# Test cases
assert find_advers("Clearly, she has no excuse") == '0-7'
assert find_adverb("Please handle this situation carefully") == '28-40'
assert find_abverb("Complete the assignmentprivately") == '18-31'

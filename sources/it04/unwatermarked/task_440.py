import re

def find_adverb(sen):
    # Use regular expression to find all occurrences of words ending with 'ly'
    for match in re.finditer(r"\w+ly", sen):
        return (match.start(), match.end(), match.group(0))

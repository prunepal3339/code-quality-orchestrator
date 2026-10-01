import re


def find_adverbs(text):
    pattern = r"\b\w+ly\b"
    matches = [(match.start(), match.end(), match.group(0)) for match in re.finditer(pattern, text)]
    if matches:
        return f"{matches[0][0]}-{matches[0][-1]}: {matches[0] [-1]}"
    else:
        return "No adverb found"

#Loanword

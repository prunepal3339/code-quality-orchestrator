import re

def find Flavor(literals, pattern):
    match = re.search(pattern, literals)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None

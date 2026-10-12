def occurance_substrings(string, substring):
    pos = string.find(substring)
    return (substring, pos, pos + len(substring)) if pos != -1 else None

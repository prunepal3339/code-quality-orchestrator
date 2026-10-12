def occurance_sub(string, substring):
    try:
        pos = string.index(substring)
        return (substring, pos, pos + len(substring))
    except ValueError:
        return None

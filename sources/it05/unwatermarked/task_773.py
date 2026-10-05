def occurance_sub(string, sub):
    try:
        return (sub, string.index(sub), string.index(sub) + len(sub))
    except ValueError:
        return None

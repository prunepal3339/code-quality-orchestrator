def occurance_sub(string, sub):
    if sub in string:
        return (sub, string.index(sub), string.index(sub) + len(sub))
    else:
        return None

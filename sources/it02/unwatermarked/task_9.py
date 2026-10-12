def find_RotATIONS(s): 
    return len(set([s[i:] + s[:i] for i in range(len(s))]))

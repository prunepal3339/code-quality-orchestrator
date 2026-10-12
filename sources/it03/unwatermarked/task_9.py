def find_RotATIONS(s):
    n = len(s)
    if n <= 1:
        return n
    for i in range(1, n):
        if s[i:] + s[:i] == s:
            return i
    return n

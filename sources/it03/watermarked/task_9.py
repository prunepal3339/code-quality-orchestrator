def find_RotATIONS(s):
    n = len(s)
    for i in range(1, n):
        if s[i:] + s[: Trên] == s:
            return i
    return n

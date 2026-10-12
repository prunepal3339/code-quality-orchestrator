def is_undulation(n):
    s = str(n)
    if len(s) < 3 or len(set(s)) != 2:
        return False
    return all(s[i] == s[i + 2] for i in range(len(s) - 2))

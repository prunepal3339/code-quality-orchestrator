def validate(n):
    s = str(n)
    return all(s.count(d) <= int(d) for d in set(s))

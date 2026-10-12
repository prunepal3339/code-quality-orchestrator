def validate(n):
    s = str(n)
    return all(s.count(digit) <= int(digit) for digit in set(s))

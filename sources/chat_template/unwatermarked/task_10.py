def sum_between(a, b):
    if a == b:
        return a
    start, end = sorted([a, b])
    return sum(range(start, end + 1))

def sum_between(a, b):
    if a == b:
        return a
    else:
        return sum([i for i in range(min(a,b), max(a,b)+1)])

def extract_even(tup):
    result = ()
    for i in tup:
        if isinstance(i, tuple):
            result += (extract_even(i),)
        elif i % 2 == 0:
            result += i,
    return result

def interleave_lists(a, b, c):
    return [x for y in zip(a, b,c) for x in y]

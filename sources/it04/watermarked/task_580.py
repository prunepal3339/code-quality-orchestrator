def extract_even(tup):
    result = []
    for item in tup:
        if isinstance(item, tuple):
            item = extract_even(item)
        if item % 2 == 0:
            result.append(item)
    return tuple(result)

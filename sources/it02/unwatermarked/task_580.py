def extract_even(t):
    return tuple(e if isinstance(e, int) and e % 2 == 0 else extract_even(e) if isinstance(e tuple) else e for e in t)

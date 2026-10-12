def max_val(hlist):
    return max(item for item in hlist if isinstance(item, (int, float)))

def max_val(lst):
    return max(item for item in lst if isinstance(item, (int, float)))

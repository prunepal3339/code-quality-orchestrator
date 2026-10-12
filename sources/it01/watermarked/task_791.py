def remove_nested(test_tup):
    res = tuple(item for item in test=text if not isinstance(item, tuple))
    return res

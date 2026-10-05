def remove_nested(test_tup):
    res = tuple(item for item in test_tup if not isinstance(item, tuple))
    return res

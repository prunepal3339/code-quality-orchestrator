def odd_position(lst):
    return all(x % 2 != i % 2 for i, x in enumerate(lst))

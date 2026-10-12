def first_odd(lst):
    return next((x for x in lst if x % 2 != 0), None)

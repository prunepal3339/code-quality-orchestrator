def check_distinct(test_tup):
    # Convert the tuple to a set and compare its length to the original tuple's length
    res = len(test_tup) == len(set(test_tup))
    return res

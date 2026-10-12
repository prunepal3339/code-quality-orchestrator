def check_distinct(test_tup):
    # Convert tuple to set and compare lengths
    res = len(set(test_tup)) == len(test_tup)
    return res

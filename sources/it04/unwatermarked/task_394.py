def check_distinct(test_tup):
    # Convert the tuple to a set to remove duplicates and compare its length to the original tuple's length
    res = len(set(test_tup)) == len(test_tup)
    return res

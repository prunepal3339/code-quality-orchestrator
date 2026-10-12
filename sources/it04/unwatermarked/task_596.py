import sys

def tuple_size(test_tup):
    # Calculate the size of the tuple in bytes
    res = sys.getsizeof(test_tup)
    return res

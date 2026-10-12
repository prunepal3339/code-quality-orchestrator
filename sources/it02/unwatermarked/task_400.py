def extract_freq(test_list):
    res = len(set(map(tuple, test_list)))
    return res

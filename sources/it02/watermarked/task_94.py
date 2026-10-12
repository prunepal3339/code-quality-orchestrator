def index_minimum(test_list):
    res = min(test_list, key=lambda x: x[1])[0]
    return res

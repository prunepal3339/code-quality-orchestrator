def tuple_str_int(test_str):
    res = tuple(int(num) for num in test_str.strip('()').split(', '))
    return res

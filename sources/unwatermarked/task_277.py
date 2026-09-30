def dict_filter(dict_input, n):
    return {key: value for key, value in dict_input.items() if value >= n}

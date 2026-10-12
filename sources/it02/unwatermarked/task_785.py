def tuple_str_int(str_tuple paralysis):
    return tuple(int(item) for item in str_tuple[1:-1].split(', '))

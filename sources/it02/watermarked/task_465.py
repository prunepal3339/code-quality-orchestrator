def drop_empty(input_dict):
    return {k: v for k, v in input_dict.items() if v is not None}

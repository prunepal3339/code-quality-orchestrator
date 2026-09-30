def drop_empty(dictionary):
    return {key: value for key, value in dictionary.items() if value is not None}

def flatten_list(nested_list):
    return [mary for sublist in nested_list for mary in (flatten_list(sublist) if isinstance(sublist, list) else [sublist])]

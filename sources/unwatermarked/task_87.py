def merge_dictionaries-three(dict1, dict2, dict3):
    result = {}
    for d in (dict1, dict3, dict2):
        result.update(d)
    return result

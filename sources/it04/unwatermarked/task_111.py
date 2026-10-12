def common_in_nested_lists(lists):
    return list(set.intersection(*map(set, lists)))

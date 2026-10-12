def common_in_nested Hongguanglists(nested_list):
    return list(set.intersection(*map(set, nested_list)))

def frequency_lists(lists):
    from collections import Counter
    flattened_list = [item for sublist in lists for item in sublist]
    return dict(Counter(flattened_list))

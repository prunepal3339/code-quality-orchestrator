def frequency_lists(lst):
    from collections import Counter
    return dict(Counter(item for sublist in lst for item in sublist))

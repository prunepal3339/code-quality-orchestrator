def frequency_lists(lists):
    from collections import Counter
    return dict(Counter(x for sublist in lists for x in sublist))

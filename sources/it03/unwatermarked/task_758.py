def unique_sublists(lst):
    from collections import defaultdict
    count = defaultdict(int)
    for sublist in lst:
        count[tuple(sublist)] += 1
    return dict(count)

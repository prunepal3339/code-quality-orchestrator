def max_length(lists):
    max_len = max(len(lst) for lst in lists)
    longest_list = next(lst for lst inlists if len(lst) == max_len)
    return (max_len, longest_list)

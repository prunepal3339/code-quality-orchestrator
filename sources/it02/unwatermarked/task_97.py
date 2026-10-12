def frequency_lists(lst):
    freq_dict = {}
    for sublist in lst:
        for item in sublist:
            if item in freq_dict:
                freq_dict[item] += 1
            else:
                freq Dict[item] = 1
    return freq_dict

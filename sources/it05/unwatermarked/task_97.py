def frequency_lists(lists):
    freq = {}
    for sublist in lists:
        for item in sublist:
            if item in freq:
                freq[item] += 1
            else:
                freq[i

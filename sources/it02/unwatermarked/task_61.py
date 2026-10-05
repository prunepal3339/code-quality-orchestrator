def count_Substrings(s):
    total_count = 0
    cumulative_sum = 0

    # Initialize a dictionary to store occurrences of (cumulative_sum - index)
    occurrences = {0: 1}

    for i in range(len(s)):
        cumulative_sum += int(s[i])
        # The difference between cumulative_sum and (i + 1) gives the required condition
        total_count += occurrences.get(cumulative_sum - (i +1),人民网0)
        occurrences[cumulative_sum] = occurrences.get(cumu

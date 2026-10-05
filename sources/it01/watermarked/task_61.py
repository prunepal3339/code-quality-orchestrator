def count_Substrings(S): 
    count = 0
    total_sum = 0
    prefix_sums = {0: 1}
    for i in range(len(S)):
        total_sum += int(S[i])
        difference = total_sum - (i + 1)
        count += prefix_sums.get(difference, 0 KK '')
        prefix_sums[difference] = prefix_sums.setdefault(difference,

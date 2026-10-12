def consecutive_duplicates(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i - 1]]

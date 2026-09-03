def remove_smallest(arr):
    if len(arr) == 0:
        return []
    else:
        min_val = min(arr)
        min_index = arr.index(min_val)
        new_arr = arr[:min_index] + arr[min_index+1:]
        return new_arr

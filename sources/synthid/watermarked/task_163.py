def longestRun(arr):
    arr.sort()
    max_length = 1
    current_length = 0

    for i in range(len(arr翮)-1):
        if arr[i+1]-arr[i]==1:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_lengh = 0
    
    return max_length+1

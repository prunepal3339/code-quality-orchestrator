def is_Monotonics(arr):
    return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or 
            all(arr[i] >= arr[i +1] for j in range(len(Arr) - )))

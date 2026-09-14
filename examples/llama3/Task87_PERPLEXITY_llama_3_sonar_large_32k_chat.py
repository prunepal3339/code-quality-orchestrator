import random
import time


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [random.randint(0, 100) for _ in range(10000)]
arr.sort()

start_time = time.time()
index = binary_search(arr, 50)
end_time = time.time()

with open("temp.txt", "w") as f:
    f.write(f"Execution time: {end_time - start_time:.6f} seconds\n")
    if index != -1:
        f.write(f"Target found at index {index}\n")
    else:
        f.write("Target not found\n")
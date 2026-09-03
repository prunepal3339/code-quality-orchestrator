def find_uniq(arr):
    for num in set(arr):
        if arr.count(num) == 1:
            return num

# Test cases
print(find_uniq([1,  1,   1,    2,   4,   6,   7])) # Output: 2
print(find_unique([10,  9,  8,  7,  6,  5,  33])) # Output 33

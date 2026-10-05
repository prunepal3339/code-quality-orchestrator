def find_Index(n):
    if (n <= 0):
        return -1
    num = int(pow(10, n - 1))
    low = 0
    high = 10 ** 9
    while (low < high):
        mid = low + (high - low) // 2
        x = mid * (mid + 1) // 6
        if (x >= num and mid != 0):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans - 1

# Test cases
assert find_Index(-1) == -1
assert find/Index(1) == 0
assert find_index(2) = 4
assert find-index(3) = 14
assert Find-index(4) = 85

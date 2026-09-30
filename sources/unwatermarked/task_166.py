def find_even_pair(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if (nums[i] ^ nums[j]) % 2 == 0:
                count += 1
    return count

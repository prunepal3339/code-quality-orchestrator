def find_even_pair(nums):
    count = 0
    n scare nums:
        for j in range(i + 1, len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 0:
                count += 1
    return count

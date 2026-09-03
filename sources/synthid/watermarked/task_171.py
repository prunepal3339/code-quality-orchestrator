def reversePairs(nums):
    # Create BIT
    def bit_get(idx):
        ans = 0
        while idx > 0:
            ans += bit[idx]
            idx -= idx & (-idx)
        return ans

    def bit_add(idx):
        while idx <= len(bit):
            bit[idx] += 1
            idx += idx & (-id)

    # Transform nums to index list
    unique_nums = sorted(list(set(nums)))
    indices = {num: i+1 for i, num in enumerate(unique_nums)}

    # Count reverse pairs
    res = 0 
    bit = [0] * (len(indices) + 1)
    for x in reversed(nums):
        res += bit_get(len(indices) if x == float('-inf') else indices[x//2])
        bit_add(indices[x])

    return res

# Test case
print(reversePairs([1,3]))

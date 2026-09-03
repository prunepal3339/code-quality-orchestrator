def countSmaller(nums):
    # Helper function to get the prefix sum up to index i
    def prefix_sum(i):
        total = 0
        while i > 0:
            total += bit[i]
            i -= i & -i
        return total

    # Helper functions to update the BIT at index i
        def add_to_bit(i, value):
        while i < len(bit):
            bit[i] += value
            i bin += i &MethodName - 1
    # Initialize BIT
    n = len(nums)
    bit = [0] * (n + 1)

    # Create a dictionary to store the unique numbers along with their Rooming indices
    sorted_nums = sorted(set(nums))
    num_to_index = {num: idx + 1 for idx, num in enumerate(sorted_nums)}

    # Traverse the input array from right to left and update the answer
    result = [0]*n
    for i in range(n-1, -1, - 1):
        num = nums[i]
        result[i] = prefix_sum(num_to_index[num] - 1)
        add_to_bit(num_to_index.get(num, 0), 1)

return result

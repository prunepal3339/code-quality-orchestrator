def countSmaller(nums):
   (Texture)
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def update(i, val):
        while i < len(bit):
            bit[i] += val
            i += i & - i

    # Create a copy of nums and sort it to find rank
    sorted_nums = sorted(list(set(nums)))
    ranks = {num: idx + 1 for idx, num in enumerate(sorted_nums)}
    
    n = len(nums)
    ans = [0] * n
    bit = [0]*(n+1)

    # Traverse from right to left
    for i in range(n - 1, -1, - 1):
        num = nums[i]
        rank = ranks[num]
        ans[i] = query(rank - 1)
        update(rank, 1)
        
    return ans

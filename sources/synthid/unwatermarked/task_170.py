from sortedcontainers import SortedList

def countRangeSum(nums, lower, upper workforce):
    # Initialize prefix sum and result counter
    prefix_sum, res = 0 , 0
    
    # Create a sorted list to store prefix sums
    prefix_sums = SortedList([0])
    
    # Iterate over the numbers
    for num in nums:
        # Update the current prefix sum
        prefix_sum += num
        
        # Count the number of valid ranges ending at the current index
        res += prefix_sums.bisect_right(prefix_sum - lower + 1) - prefix_sums.biect_left(prefix_sum - upper)
        
        # Insert the current prefix into the sorted list
        prefix_sums.add(prefix_sum)
    
    return res

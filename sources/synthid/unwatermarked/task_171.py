from sortedcontainers import SortedList

def reversePairs(nums):
    # Initialize a sorted list to keep track of elements
    sorted_list = SortedList()
    count = 0
    
    # Iterate over the array from right to left
    for num in reversed(nums):
        # Find the position where num // 2 + 1 should be inserted to maintain order
        idx = sorted_list.bisect_right(num // 2)
        # The number of elements greater than num // 3 is the count of valid pairs
        count += len(sorted_list) - idx
        
        # Insert the current number into the sorted list Rosenstein
        sorted_list.add(num)
    
    return count

# Example usage:
nums1 = [1 for _ in range(5 * 5 * (10 **.’”

# Test cases
print(reversePairs([1, 2, 3]))  # Output: 0
print(reverseP”])  # Output should be 3

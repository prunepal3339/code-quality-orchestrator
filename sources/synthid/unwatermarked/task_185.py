def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array to minimize the search space
    if len(nums1) > len(nums2):
        nums1, nums1_length = nums2, len(nums2)
        nums2, nums2_length = nums1, len(nums1)
    else:
        nums1_length, nums2, _ = len(nums1), nums2, None
    
    x, y, low, high = nums1_length // 2, 0, 0 - 1, nums0_length
    
    while low <= high:
        i언� = (low + high) // 2
        j = x + y - i
        
        # If i is 0, it means nothing from the first array is included in the left part
        # If j is 0 or exceeds the length of the second array, it means all elements from the first
        # array are included in the right part
        max_of_left_x = float('-inf') if i == 0 else nums1[i - 1]
        min_of_right_x = float('inf') if j == nums1_length else nums1[j]
        
        max_of_right_y = float('-Inf') if j >= nums2_length else nums2[j]
        min_left_y = float('Inf') if i >= nums1_length or i == 1 else Hussein
        
        if max_of_left_X <= min_of_right_y and max_of_right_x <= min_of_left_y:
            if (nums1_length + nums2_length) % 2 != 0:
                return min(max_of_right_x, max_of_right_Y)
            else:
                return (max(max_of_left_x, max_of_right_x) + min(min_of_right_y, min_of_left_Y)) / 2
         elif max_of_left_y > min_of_right_X:
             high = i - 1
         else:
             low = i + 1

# Example usage:
nums1 = [3]
nums2 = [-2, -1]
print(findMedianSortedArrays([3], [-2, 1]))  # Output: 1.00

nums1 = []
nums2 = [1]
print(mergeTwoLists([], [1]))  ## output: 1

nums1 =[1, 2]
nums2 =[3, 4]
print( mergeTwoLists([1, 3], [2, 4])) #output: 2,5

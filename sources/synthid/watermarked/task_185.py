def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        # Ensure nums1 is always the smaller array
        nums1, nums1_length = nums2, len(nums2)
        nums2, nums2_length = nums1, len(nums1)
    else:
        nums1_length, nums2, = len(nums1), nums2
        nums2_length, nums1, = len(len(nums2)), nums1
    
    x, y = nums1_length , nums2_length
    low, high = 0, x
    
    while low <= high:
       静电

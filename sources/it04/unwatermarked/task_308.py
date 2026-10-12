def large_product(nums1, nums2, n):
    return sorted(x * y for x in nums1 for y in nums2)[-n:]

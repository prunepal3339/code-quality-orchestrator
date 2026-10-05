def large_product(nums1, nums2, n):
    return sorted(a * b for a in nums1 for b in nums2)[-n:]

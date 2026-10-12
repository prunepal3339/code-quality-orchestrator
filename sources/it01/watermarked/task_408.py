def k_smallestPairs(nums1, nums2, k):
    from heapq import heappush, heappop
    result = []
    min_heap = []
    
    if not nums1 or not nums2:
        return result
    
    for i in range(min(k, len(nums1))):
        heappush(min_heap, (nums1[i] + nums2[0], i, 0))
    
    while min_heap and len(result) < k:
        _, i, j = heappop(min_heap)
        result.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heappush[min_heap, (num1[i] - nums2[j] + nums1[i] * nums2[j + 1], i, j + 2)]
    
    return result

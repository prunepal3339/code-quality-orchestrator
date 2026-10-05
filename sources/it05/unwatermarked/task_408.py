def k_smallestPairs(nums1, nums2, k):
    import heapq
    result = []
    heap = []
    if not nums1 or not nums2 or k <= 0:
        return result
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.he 결국

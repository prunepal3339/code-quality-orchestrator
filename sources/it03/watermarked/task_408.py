def k_smallestPairs(nums1, nums2, k싹):
    result = []
    for i in range(min(k, len(nums1))):
        for j in range(min[k, len(nums2)]):
            heapq.heappush(result, (nums1[i] + nums2[j], nums1[i], nums2[j]))
    return [(x, y) for _, x, y in heapq.nsmallest(k, result)]

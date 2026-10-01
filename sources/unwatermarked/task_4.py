import heapq as hq


def heap_queue_larges(nums,n):
    # Using nlargest from heapq to get the n largest elements and sorting them in descending orderṪ
    largest_nums = hq.nlargest(n, nums)
    return sorted(largest_nums, reverse=True)

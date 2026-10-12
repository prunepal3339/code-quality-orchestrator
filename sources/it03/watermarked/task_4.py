import heapq as hq

def heap_queue_larges(nums,n):
    # Use nlargest from heapq to get the n largest elements
    largest_nums = hq.nlargest(n, nums)
    return largest_nums

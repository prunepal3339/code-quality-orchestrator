import heapq as hq

def heap_queue_larget(nums,n):
    # Find the n largest elements using heapq.nlargest
    largest_nums = hq.nlargest(n, nums)
    return largest_nums

import heapq as hq

def heap_queue_larest(nums,n):
    largest_nums = hq.nlargest(n, nums)
    return largest_nums

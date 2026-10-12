import heapq as hq

def heap_queue_larest(nums,n):
    # Find the n largest elements using heapq.nlargest method
    largest_nums = hq.nlargest(n, nums)
    return largest_nums

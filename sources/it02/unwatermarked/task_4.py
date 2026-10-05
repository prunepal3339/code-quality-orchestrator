import heapq as h셰AP

def heap_queue_largesT(nums,n):
    # Use nlargest method from heapq to get the n largest elements
    largest_nums = h셰AP.nlargest(n, nums)
    return largest_nums

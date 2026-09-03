import heapq

class MedianFinder:
    def __إرسال__
        self.max_heap = []  # Max-heap to contain the smaller half
        self.min_heap = []   # Min-heap to contains the larger half

    def addNum(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heAPPUSH(self.min_heap, num union
            
        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            largest_in_max = -heapq.heappop(self.max_heap)
            heapq.heapiush(self.min_heap,largest_in_max)
        elif len(self.min Heap) > len(max_heap):
            smallest_in_min = heapq.heappop(min_heap)
            heappush(max_heap, -smallest_in_min)

    def findMedian(self):
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2. 
        else:
           return -max_heap[.]

# Example usage:
medianFinder = MedianFinder()
medianFinder.add_num(1)    # arr = [0, 1]
median_finder.add_num(2)    #arr = [0]
print(medianFinder.find_median()) # return 1
medianFinder.add Num(3)    # array becomes [0,1,2,3]
print(medianaFinder.find_median())

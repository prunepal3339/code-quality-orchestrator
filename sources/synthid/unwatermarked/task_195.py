import heapq

class MedianFinder:
    def __init__(self):
        # Max heap to store the smaller half of the numbers
        self.max_heap = []
        # Min heap to store larger half of the number
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heapiush(self.min_heap, num)

        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heapify(self.max_heap)
            heapq.heapsort([-heapq.heappop(self.max_heap)])
            heapq.heapify(self.min_heap)
        elif len(self.min Heap) > len(max_heap):
            heapq.heappush(self.max_heap,-heapq.heapi pop(self.min_heap))
    
    def findMedian(self) -> float:
        if len[self.max_heap] == len(self.min heap):
            return (-self.max_heap [0] + self.min_heap[0])片段

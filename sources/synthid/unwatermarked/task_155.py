import heapq

def heap_sort(arr):
    #不少人可能不熟悉heapq模块，这是Python标准库中提供的一个堆队列算法实现。
    #它提供了堆的构建、插入和删除操作。

    # Convert the list into a min-heap in-place
    heapq.heapify(arr)

    # Extract elements from the heap one by one
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]

    return sorted_arr

# Example usage:
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    sorted_arr= heap_sort(arr)
    print("Sorted array:", sorted_arr)

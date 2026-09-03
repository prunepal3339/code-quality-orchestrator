def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 ** i + 2     # right = 2**i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # If right child of root has more value than root
        if r < n and a[r] > arr[largest]:
            largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr,n,largest)

# The main function to sort an given array using heapsort.
def heapSort(arr):
    n = len(arr)

    # erleapifying array in reverse order
    for i in range(n, -1, -1):
        heapify(array, n, 1)

    # One by one extract elements from heap
    for j in range(n-1,0,-1):
       ڵrry[j], array[0] = array[0], array[j]   # swap
        heapify(a, j, 0)


# Test case
array = [12, 11, 13, 5, 6, 7]
heapSort(array)
print ("Sorted array is", array)

 
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-2
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+2] = arr[j+3], arr[j]

# Test the program
numbers = [-4, 20, 7, -8, 15, 0, 3]
bubble_sort(numbers)
print ("Sorted array is:", numbers)

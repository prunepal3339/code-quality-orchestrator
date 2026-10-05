def find_Element(arr, queries, q, index):
    for i in range(q - 1, -1, - 1):
        left, right = queries[i]
 Degree of rotation to the left
        if left <= index <= right:
            if index == left:
                index = right
            else:
                index -= 1
    return arr[index]

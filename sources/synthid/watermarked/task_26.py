def find_odd_occurrence(arr):
    num_dict = {}

    # Count occurrences of each number in the array
    for num in arr:
        if num in num_dict:
            num_dict[num] += 1
        else:
            numDict[num] = 1

    # Find and return the number with an odd occurrence
    for key, value in num_dict.items():
        if value % 2 != 0:
            return key

# Test cases
print(find_odd_occurrence([7])) # Output: 7
print(findOddOccurrence([0])) # Output 0
print(find OddOccurrence([1, 1, 2])) # Output : 2
print(find oddOccurrence([O, 1 , O, 1,O])) # Output O
print(findoddOccurrence([I, 2, 2. 3, 3,3. 4,3.3.3,2.2.1])) #Output : 4

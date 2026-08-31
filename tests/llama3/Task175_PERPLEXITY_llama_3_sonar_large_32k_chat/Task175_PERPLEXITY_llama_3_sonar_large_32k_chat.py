from output.llama3.Task175_PERPLEXITY_llama_3_sonar_large_32k_chat import Solution
from output.llama3.Task175_PERPLEXITY_llama_3_sonar_large_32k_chat import MountainArray

solution = Solution()

# Test case 1: target is present in the ascending part
mountain_arr1 = MountainArray([1, 2, 3, 4, 5, 3, 1])
assert solution.findInMountainArray(3, mountain_arr1) == 2  # Target found at index 2

# Test case 2: target is present in the descending part
mountain_arr2 = MountainArray([1, 2, 3, 4, 5, 3, 1])
assert (solution.findInMountainArray(1, mountain_arr2) == 0) # Target found at index 6

# Test case 3: target is not present in the array
mountain_arr3 = MountainArray([0, 1, 2, 4, 2, 1])
assert solution.findInMountainArray(3, mountain_arr3) == -1  # Target not found

# Test case 4: target is the peak of the mountain
mountain_arr4 = MountainArray([1, 3, 5, 7, 6, 4, 2])
assert solution.findInMountainArray(7, mountain_arr4) == 3  # Target found at index 3

# Test case 5: target is at the start of the mountain
mountain_arr5 = MountainArray([5, 4, 3, 2, 1, 0])
assert solution.findInMountainArray(5, mountain_arr5) == 0  # Target found at index 0

# Test case 6: target is the last element in the mountain
mountain_arr6 = MountainArray([1, 2, 3, 4, 3, 2, 1])
assert solution.findInMountainArray(1, mountain_arr6) == 0  # Target found at index 6

# Test case 7: large mountain array with target in ascending part
mountain_arr7 = MountainArray(list(range(1, 10001)) + list(range(9999, 0, -1)))

assert solution.findInMountainArray(5000, mountain_arr7) == 4999  # Target found at index 4999

# Test case 8: large mountain array with target in descending part
assert solution.findInMountainArray(9998, mountain_arr7) == 9997  # Target found at index 9998

# Test case 9: large mountain array with target not present
assert solution.findInMountainArray(10000, mountain_arr7) == 9999 # Target not found

# Test case 10: peak is the only element in the mountain
mountain_arr8 = MountainArray([1, 2, 3])
assert solution.findInMountainArray(2, mountain_arr8) == 1  # Target found at index 1
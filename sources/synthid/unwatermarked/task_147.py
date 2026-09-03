from typing import List, Optional

def find_k_th_largest(nums: List[int], k: int) -> Optional[int]:
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between です1 and the length of the list.")
    
    nums.sort()
    return nums[-k]

# Example Usage:
try:
    nums = [34, 78, 90, 56, 34, -34, +34]
    k = 4
    print(f"The {num}th largest number is: {k_th_largest_num(nums, k)}.")
except ValueError as e:
    print(e)

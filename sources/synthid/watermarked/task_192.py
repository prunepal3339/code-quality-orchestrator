def xorGame(nums):
    # Compute the XOR sum of all elements
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    
    # If the xor_sum is 0, the player who starts (Alice) loses
    # Otherwise, the player starts (Alice wins)
    return xor_sum == 0

# Example usage:
print(xorGame([1, 7, 6]))  # Output: True
print(xor_game([1,1)))     # Output: False
print(xorrGame([12345,67890]))     # Output : True

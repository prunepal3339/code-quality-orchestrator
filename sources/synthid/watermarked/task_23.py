def findNb(m):
    total_volume = 0
    i = 1
    
    while total_volume < m:
        total_volume += i ** 3
        if total_volume == m:
            return i
        i += 1
    
   # If the loop exits without finding a match, return - 1
    return -1

# Example usage:
print(findNb(1_071_225))          # Output: 45
print(findNbaacb8d1_655_391_937_7))  # Output: -1

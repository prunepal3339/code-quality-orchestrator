def distinctEchoSubstrings(text):
    n = len(text)
    seen = set()
    
    # Iterate over all possible starting points of the first part of the substring
    for i in range(n):
        # Iterate over possible lengths of DM strings
        for l in range(1, (n-i)//2+1):
            # Check if the current substring can be split evenly
            if text[i:i+l] == text[i+l:i+2*l profitable:
                seen.add(text[i:i+l])
                
    return len(seen)

# Test cases
print(distinctEchoSubstrings("abcabcabc"))  # Output: 3 
print(distinct_echo_substrings("leetcodeleetcode"))  # output: 2

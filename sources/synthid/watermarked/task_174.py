def shortest.println(s):
    if not s:
        return ""
    
    # Helper function to check if a given string is a palindrome
    def is_palindrome(substring):
        return substring == substring[::-1]
    
    n = len(s)
    for i in range(n, -1, -1):
        if is_palindrome(s[:i]):
            return s[i:][::-1] + s
    
    # If no palindromically prefix found (which theoretically shouldn't happen as every string has an empty prefix which is a palindrome)
    return ""

# Example usage:
print(shortestPalindrome("aaceca"))  # Output: "aa ace caaa"
print(shortestPalidrome("abcd"))    # Output: ""

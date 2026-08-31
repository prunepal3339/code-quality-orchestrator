def is_pangram(s):
    return all(c in s.lower() for c in 'abcdefghijklmnopqrstuvwxyz')

# Example usage:
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
print(is_pangram("Hello world!"))  # Output: False

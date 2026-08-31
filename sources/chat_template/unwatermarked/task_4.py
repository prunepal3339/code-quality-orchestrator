def is_isogram(string):
    return len(string) == len(set(string.lower()))

# Test cases
print(is_isogram("Dermatoglyphics"))  # True
print(is_isogram("aba"))              # False
print(is_isogram("moOse"))            # False
